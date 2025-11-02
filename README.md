# 🧠 Smart Personal Finance Advisor

![GitHub last commit](https://img.shields.io/github/last-commit/naveen-142/Smart_Personal_Finance_Advisor_Team_Project)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Django](https://img.shields.io/badge/Django-Backend-green)
![Scikit-learn](https://img.shields.io/badge/ML-Scikit--learn-orange)

> A **Data-Driven Personal Finance Management System** that predicts savings, tracks expenses, and provides personalized financial recommendations using Machine Learning.

---

## 🌐 Live Deployments

| Component | Platform | Live Link |
|------------|-----------|------------|
| 🧠 **Machine Learning Model (Streamlit)** | Streamlit Cloud | [Open Streamlit App](https://smartpersonalfinanceadvisor-qkxc5x6x56uu7jv4eipszv.streamlit.app/) |
| ⚙️ **Backend API (Django)** | Render | [View Render Deployment](https://your-backend-render-link.onrender.com) |
| 💻 **Frontend Interface** | Vercel | [Open Frontend (Vercel)](https://financeadvisor-frontend.vercel.app/home) |

---

## 🚀 Overview

The **Smart Personal Finance Advisor** helps users make smarter financial decisions by analyzing their income and expenses.  
It predicts monthly savings using a **Ridge Regression model** and generates **personalized recommendations** to improve financial health.

The system bridges the gap between **raw data** and **actionable insights**, combining the strengths of **Data Science**, **Django**, and **Modern Web Technologies**.


## 🎯 Problem Statement
In today’s world, many individuals lack personalized insights into their spending and saving habits.  
Most budgeting tools only record numbers — they don’t *analyze patterns* or *offer actionable advice*.  
This project solves that gap by using **Machine Learning** to:
- Predict how much a user can save monthly
- Identify high spending categories
- Recommend practical strategies to improve financial health

  ## 🧩 System Architecture

The system follows a **three-tier architecture**:

1. **Frontend (React + Ant Design)**  
   - Collects user inputs like income and expenses  
   - Displays predictions, insights, and visual analytics  

2. **Backend (Django)**  
   - Acts as the middleware between the ML model and the frontend  
   - Sends user data to the model, retrieves predictions, and stores results in the database  

3. **Machine Learning Model (Ridge Regression)**  
   - Predicts monthly savings using income and expense data  
   - Trained with Scikit-learn and integrated as a `.pkl` model file  

4. **Database (SQLite3)**  
   - Stores user transactions, predictions, and history for analysis  


## 🎯 Key Features

- 💰 **Savings Prediction** - Ridge Regression model for monthly savings  
- 📊 **Interactive Dashboard** - Visual representation of income and expenses  
- 💬 **Personalized Advice** - AI-driven recommendations to boost savings  
- 🧾 **History Tracking** - View previous transactions and financial records  
- ⚙️ **Admin Mode** - Access and manage all users’ records centrally  
- 🧠 **Smart Error Handling** - Shows “No data available” when inputs are missing  



---

## 🧠 Machine Learning Model

| Metric | Value |
|---------|-------|
| Algorithm | Ridge Regression |
| R² Score | 0.98 |
| Mean Absolute Error | 630.15 |
| Framework | Scikit-learn |
| Language | Python |

The model was trained on synthetically generated financial data, preprocessed for accuracy.  
It captures patterns between **income, additional income, and categorized expenses** to forecast savings effectively.

---

## 🗃️ Database Overview

The project uses **SQLite3** for secure and lightweight data management.

| Table | Description |
|--------|--------------|
| **Users** | Stores registered user credentials |
| **Transactions** | Captures income and expense records |
| **Predictions** | Saves ML prediction results |
| **History** | Maintains a record of past user insights |

---

## 🧭 Workflow Description (Detailed)

1. **User Input:** The user enters income, additional income, and expenses in the React form.  
2. **Backend Processing:** Django sends this data to the Ridge model for prediction.  
3. **Model Output:** The model returns predicted savings and recommended insights in JSON format.  
4. **Storage:** Django saves results to SQLite3 for analysis and historical tracking.  
5. **Frontend Visualization:** The frontend displays results as metrics, bar charts, and recommendations.

---

## 📊 Visual Insights
*(Add screenshots below for better presentation)*

| Page | Description |
|------|--------------|
| 🏠 **Home Page** | Overview and navigation |
| 🧾 **Form Page** | User inputs income and expense details |
| 💡 **Advisor Page** | Displays recommendations and insights |
| 📈 **Dashboard** | Visualizes income vs. expenses, savings rate |
| 📜 **History** | Shows all previous transactions and predictions |
| ⚙️ **Backend JSON View** | Demonstrates how data is exchanged between ML and frontend |

---

## 🧰 Technologies Used

| Component | Technology | Purpose |
|------------|-------------|----------|
| Frontend | React, Ant Design | Interactive UI |
| Backend | Django | API communication & database management |
| Machine Learning | Python, Scikit-learn, Pandas | Model building & prediction |
| Database | SQLite3 | Data storage |
| Visualization | Power BI, Matplotlib, Seaborn | Data analysis & dashboards |
| Version Control | GitHub | Team collaboration |
| Deployment | Vercel (Frontend), Render (Backend), Streamlit Cloud (ML Demo) | Hosting & accessibility |

---

## 🧩 Challenges & Solutions

| Challenge | Solution |
|------------|-----------|
| Model integration with backend | Used Joblib + JSON for smooth data exchange |
| Inconsistent user input | Added validation logic in React |
| Overfitting in model | Used Ridge regularization |
| Visual clutter | Applied clean UI with Ant Design |
| Data persistence | Used Django ORM with SQLite3 |

---

## 👥 Roles & Responsibilities

| Team Member | Role | Contribution |
|--------------|------|--------------|
| **V. Naveen Kumar** | Data Scientist | Data preprocessing, model training, evaluation, and ML deployment via Streamlit |
| **B. Aishwarya** | Data Analyst | Performed EDA and built Power BI dashboards for analytics |
| **R. Hemanth** | Full Stack Developer | Major contributor - built and connected backend (Django), frontend (React), database (SQLite3), and handled full deployment |
| **K. Maneesha** | Backend Developer | Supported Django API creation and model integration |
| **V. Varun** | Frontend Developer | Developed UI components and integrated APIs |

## ⚙️ Installation & Setup

```bash
# 1️⃣ Clone the Repository
git clone https://github.com/yourusername/Smart_Personal_Finance_Advisor.git
cd Smart_Personal_Finance_Advisor

# 2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate # macOS/Linux

# 3️⃣ Install Dependencies
pip install -r requirements.txt

# 4️⃣ Run Server
python manage.py runserver

# 5️⃣ Open in Browser
http://127.0.0.1:8000/


```

## 🏁 Future Enhancements

- 🤖 Add AI chatbot for financial guidance

- 🔐 Enable user authentication and roles

- 🔗 Integrate real-time finance APIs

- 📈 Use clustering or time-series models for smarter forecasting

- 💬 Build multi-language support for accessibility

## 📘 References

| Resource | Description | Link |
|-----------|--------------|------|
| Scikit-learn Documentation | Ridge Regression, Model Evaluation | [https://scikit-learn.org/stable/](https://scikit-learn.org/stable/) |
| Django Documentation | Backend and ORM Guide | [https://docs.djangoproject.com/en/stable/](https://docs.djangoproject.com/en/stable/) |
| React Documentation | Frontend Components and Hooks | [https://react.dev/](https://react.dev/) |
| Power BI Learning | Data Visualization Concepts | [https://learn.microsoft.com/en-us/power-bi/](https://learn.microsoft.com/en-us/power-bi/) |

---



## 🏁 Conclusion

The **Smart Personal Finance Advisor** successfully integrates data science, backend logic, and frontend design to deliver meaningful financial insights.  
It transforms user data into actionable intelligence — helping users understand, plan, and optimize their finances in real time.

Future enhancements include:
- Multi-user authentication
- Goal-based savings recommendations
- Integration with live banking data for dynamic updates

---

## 🖋️ Author & Contributors


| Name                     | Role                          | LinkedIn                                      | GitHub                                    |
| ------------------------ | ----------------------------- | --------------------------------------------- | ----------------------------------------- |
| **Naveen Kumar**         | Data Scientist & Project Lead | [LinkedIn](https://www.linkedin.com/in/naveen-kumar-viruvuru/) | [GitHub](https://github.com/yourusername) |
| **Aishwarya**            | Data Analyst         | [LinkedIn](#)                                 | [GitHub](#)                               |
| **Hemanth**              | Full Stack Developer | [LinkedIn](#)                                 | [GitHub](#)                               |
| **Varun**                | Frontend Developer   | [LinkedIn](#)                                 | [GitHub](#)                               |
| **Maneesha**             | Backend Develope      | [LinkedIn](#)                                 | [GitHub](#)                               |




## ⭐ How to Support

If you found this project interesting:
- Star ⭐ this repository  
- Fork 🍴 and contribute  
- Connect on [LinkedIn](your_linkedin_profile_here)

  
## 📧 Contact

- Maintainer: Naveen Kumar
- Role: Data Scientist
- 📩 [Gmail](naveenkv681@gmail.com)
- 🔗 [Linkedin](https://www.linkedin.com/in/naveen-kumar-viruvuru/)
- 📘 [GitHub Profile](https://github.com/naveen-142)







