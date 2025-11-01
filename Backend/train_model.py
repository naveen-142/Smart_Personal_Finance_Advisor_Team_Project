import os
import pandas as pd
import numpy as np
import joblib
from sklearn.linear_model import Ridge

# ===============================
# Paths
# ===============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # advisor/
MODELS_DIR = os.path.join(BASE_DIR, "ml_models")
os.makedirs(MODELS_DIR, exist_ok=True)

DATA_PATH = os.path.join(BASE_DIR, "data.csv")

# ===============================
# Load or create dataset
# ===============================
if os.path.exists(DATA_PATH):
    df = pd.read_csv(DATA_PATH)
    print(f"✅ Loaded dataset from {DATA_PATH}")
else:
    print("⚠️ data.csv not found. Creating dummy dataset...")
    df = pd.DataFrame({
        "Income": [50000, 60000, 40000, 70000],
        "Additional_Income": [5000, 0, 2000, 10000],
        "Desired_Savings": [15000, 20000, 10000, 25000],
        "Credit_Score": [750, 700, 680, 800],
        "Rent": [12000, 15000, 10000, 18000],
        "Loan_Repayment": [5000, 10000, 2000, 12000],
        "Insurance": [2000, 3000, 1500, 2500],
        "Groceries": [6000, 7000, 5000, 8000],
        "Transport": [3000, 4000, 2000, 5000],
        "Eating_Out": [2000, 2500, 1000, 3000],
        "Entertainment": [1500, 2000, 1000, 2500],
        "Utilities": [2500, 3000, 2000, 3500],
        "Healthcare": [1000, 1500, 500, 2000],
        "Education": [0, 0, 0, 0],
        "Miscellaneous": [1000, 1200, 800, 1500],
        "Next_Income": [18000, 22000, 12000, 25000]
    })
    df.to_csv(DATA_PATH, index=False)
    print(f"✅ Dummy dataset created at {DATA_PATH}")

# ===============================
# Feature Engineering
# ===============================
expense_cols = [
    "Rent", "Loan_Repayment", "Insurance", "Groceries", "Transport",
    "Eating_Out", "Entertainment", "Utilities", "Healthcare", "Education", "Miscellaneous"
]

df["Total_Expenses"] = df[expense_cols].sum(axis=1)
df["Actual_Savings"] = (df["Income"] + df["Additional_Income"]) - df["Total_Expenses"]
df["Savings_Rate"] = df["Actual_Savings"] / (df["Income"] + df["Additional_Income"])
df["Debt_to_Income"] = df["Loan_Repayment"] / (df["Income"] + df["Additional_Income"])

# ===============================
# Features and target
# ===============================
FEATURE_COLUMNS = ["Income", "Savings_Rate", "Debt_to_Income", "Actual_Savings"]
TARGET = "Next_Income"

X = df[FEATURE_COLUMNS]
y = df[TARGET]

# ===============================
# Train Ridge model
# ===============================
ridge_model = Ridge(alpha=1.0)
ridge_model.fit(X, y)

# ===============================
# Save model and features
# ===============================
ridge_model_path = os.path.join(MODELS_DIR, "ridge_model.pkl")
features_path = os.path.join(MODELS_DIR, "model_features.pkl")

joblib.dump(ridge_model, ridge_model_path)
joblib.dump(FEATURE_COLUMNS, features_path)

print(f"✅ Ridge model and features saved successfully at: {MODELS_DIR}")
print("📁 Files inside ml_models folder:", os.listdir(MODELS_DIR))

# ==========================================================
# 🔹 Prediction Function (Used by views.py)
# ==========================================================
def predict_from_user_input(user_data: dict):
    """
    Takes user financial input (from frontend) and predicts savings using Ridge Regression.
    Returns dictionary with prediction and recommendations.
    """

    # Load model and features (absolute paths)
    try:
        ridge_model = joblib.load(ridge_model_path)
        feature_columns = joblib.load(features_path)
    except Exception as e:
        return {"error": f"Model files not loaded: {str(e)}"}

    # Prepare user input
    df = pd.DataFrame([user_data])

    # Derived features
    income = df["Income"].iloc[0]
    add_income = df["Additional_Income"].iloc[0]
    total_income = income + add_income

    df["Total_Expenses"] = df[
        ["Rent", "Loan_Repayment", "Insurance", "Groceries", "Transport",
         "Eating_Out", "Entertainment", "Utilities", "Healthcare", "Education", "Miscellaneous"]
    ].sum(axis=1)

    df["Actual_Savings"] = total_income - df["Total_Expenses"]
    df["Savings_Rate"] = df["Actual_Savings"] / total_income
    df["Debt_to_Income"] = df["Loan_Repayment"] / total_income

    X_input = df[feature_columns]

    # Predict using Ridge model
    predicted_savings = ridge_model.predict(X_input)[0]

    return {
        "Predicted_Savings": round(float(predicted_savings), 2),
        "Recommendations": [
            f"Estimated savings potential: ₹{predicted_savings:.0f}",
            "Try cutting non-essential costs like Eating Out or Entertainment.",
            "Maintain an emergency fund of at least 3 months’ expenses.",
        ]
    }
