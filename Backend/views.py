import os
import pandas as pd
import joblib
import traceback
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from scipy import stats

from advisor.serializer import ContactMessageSerializer, PredictionRecordSerializer
from .train_model import predict_from_user_input

from .models import PredictionRecord

# ==========================================================
# HOME VIEW
# ==========================================================
def home(request):
    return HttpResponse("Welcome to the Smart Personal Finance Advisor API!")


# ==========================================================
# 🔹 FIXED MODEL LOADING PATHS (this caused your FileNotFoundError)
# ==========================================================
# Use absolute path based on BASE_DIR instead of relative path
model_path = os.path.join(settings.BASE_DIR, 'advisor', 'ml_models', 'ridge_model.pkl')
features_path = os.path.join(settings.BASE_DIR, 'advisor', 'ml_models', 'model_features.pkl')

# Check if files exist before loading
if not os.path.exists(model_path):
    raise FileNotFoundError(f"ridge_model.pkl not found at {model_path}")
if not os.path.exists(features_path):
    raise FileNotFoundError(f"model_features.pkl not found at {features_path}")

# Load models
ridge = joblib.load(model_path)
model_features = joblib.load(features_path)


# ==========================
# 🔹 Expense Columns
# ==========================
expense_cols = [
    "Rent", "Loan_Repayment", "Insurance", "Groceries", "Transport",
    "Eating_Out", "Entertainment", "Utilities", "Healthcare", "Education", "Miscellaneous"
]


# ==========================
# 🔹 Recommendation Function
# ==========================
def generate_recommendations(user):
    recs = []

    income = user["Income"] + user["Additional_Income"]
    total_exp = sum([user[col] for col in expense_cols])
    actual_savings = income - total_exp
    savings_rate = actual_savings / income if income > 0 else 0
    debt_ratio = user["Loan_Repayment"] / income if income > 0 else 0
    health_score = 0.4 * savings_rate + 0.3 * (1 - debt_ratio) + 0.3 * user["Credit_Score"] / 900

    # Identify top flexible expense
    flexible_expenses = ["Eating_Out", "Entertainment", "Groceries", "Miscellaneous", "Transport", "Utilities"]
    top_expense = max(flexible_expenses, key=lambda x: user[x])
    top_exp_value = user[top_expense]

    suggestion = f"Your highest flexible expense is {top_expense} at ₹{top_exp_value:.0f}. "
    if top_expense in ["Eating_Out", "Entertainment"]:
        suggestion += "Reduce by 20–30% through meal planning or fewer outings — the saved amount can go toward clearing your loan repayment faster."
    elif top_expense == "Groceries":
        suggestion += "Track grocery waste and buy in bulk; use savings to increase insurance or emergency fund."
    elif top_expense == "Transport":
        suggestion += "Try carpooling or public transport twice a week; redirect saved money into investments."
    elif top_expense == "Utilities":
        suggestion += "Switch to energy-efficient devices; the reduction can offset monthly insurance or EMI costs."
    elif top_expense == "Miscellaneous":
        suggestion += "Track impulsive buys. Saved cash can strengthen your emergency fund."
    else:
        suggestion += "Review this category for optimization."

    # 💡 Savings-based recommendations
    if savings_rate < 0:
        recs.append(f"⚠️ Your expenses exceed your income by ₹{-actual_savings:.0f}. Immediate cost reduction is required.")
    elif savings_rate < 0.2:
        recs.append(f"💡 You’re saving only {savings_rate*100:.1f}% of your income. Automate savings and reduce discretionary costs.")
    elif savings_rate < 0.35:
        recs.append(f"✅ Good savings rate ({savings_rate*100:.1f}%). Aim for 30–35% for better security.")
    else:
        recs.append(f"🌟 Excellent! You’re saving {savings_rate*100:.1f}%. Consider investing extra funds wisely.")

    # 💳 Debt management tips
    if debt_ratio > 0.5:
        recs.append("📉 High debt load (>50% of income). Prioritize repaying high-interest loans first or consider refinancing options.")
    elif debt_ratio > 0.3:
        recs.append("⚠️ Moderate debt ratio. Focus on reducing EMIs before taking on new financial commitments.")
    else:
        recs.append("🟢 Low debt level — maintain this by avoiding unnecessary loans.")

    # 💠 Credit score advice
    if user["Credit_Score"] < 600:
        recs.append("🔴 Low credit score — pay bills on time and limit card usage under 30%.")
    elif user["Credit_Score"] < 750:
        recs.append("🟠 Average credit score — avoid missed payments and monitor your score monthly.")
    else:
        recs.append("🟢 Excellent credit score — you qualify for low-interest offers; use wisely.")

    recs.append(suggestion)

    # 🩺 Financial health summary
    if health_score > 0.75:
        recs.append("💪 Financial health is strong! Explore mutual funds or SIPs for long-term wealth building.")
    elif health_score > 0.5:
        recs.append("📈 Financial health is okay. Reduce small expenses to improve cash flow stability.")
    else:
        recs.append("🚨 Financial health is weak. Cut discretionary costs and prioritize essential payments first.")

    return recs, health_score, top_expense


# ==========================
# 🔹 Prediction Function (Backend Entry Point)
# ==========================
def predict_expense_and_recommend(user_input: dict):
    """
    user_input: dict containing financial details
    returns: dict with predicted savings, health score, top expense, and recommendations
    """

    df = pd.DataFrame([user_input])
    df_X = pd.get_dummies(df, columns=["Occupation"], drop_first=True)

    # Ensure consistent columns with training model
    for col in model_features:
        if col not in df_X.columns:
            df_X[col] = 0
    df_X = df_X[model_features]

    # Prediction
    predicted_savings = ridge.predict(df_X)[0]

    # Recommendations
    recs, health_score, top_expense = generate_recommendations(user_input)

    # Return response as dict (for API or frontend use)
    return {
        "predicted_savings": round(float(predicted_savings), 2),
        "financial_health_score": round(health_score * 100, 1),
        "top_expense_to_cut": top_expense,
        "recommendations": recs
    }


# ==========================
# 🔹 Example Usage (For Testing)
# ==========================
if __name__ == "__main__":
    example_user = {
        "Income": 60000,
        "Additional_Income": 5000,
        "Credit_Score": 720,
        "Age": 30,
        "Dependents": 2,
        "Occupation": "Salaried Employee",
        "Rent": 12000,
        "Loan_Repayment": 8000,
        "Insurance": 2000,
        "Groceries": 7000,
        "Transport": 3000,
        "Eating_Out": 4000,
        "Entertainment": 2500,
        "Utilities": 2500,
        "Healthcare": 1500,
        "Education": 2000,
        "Miscellaneous": 1500
    }

    result = predict_expense_and_recommend(example_user)
    print(result)


# ==========================================================
# API ENDPOINT
# ==========================================================
@api_view(["POST"])
def predict(request):
    user_data = request.data
    try:
        result = predict_expense_and_recommend(user_data)
        print("Got Data")
        row=PredictionRecord.objects.create(input_data=user_data,result=result)
        row.save()
        return Response(result, status=200)
    except Exception as e:
        print("\n===================== ERROR TRACEBACK =====================")
        traceback.print_exc()
        print("===========================================================\n")
        return Response({"error": str(e)}, status=400)


@api_view(['GET'])
def get_history(request):
    """Return all stored user predictions"""
    try:
        records = PredictionRecord.objects.all().order_by('-id')
        serializer = PredictionRecordSerializer(records, many=True)
        return Response(serializer.data, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=400)
    

@api_view(['POST'])
def contact_message(request):
    serializer = ContactMessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Message received successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)