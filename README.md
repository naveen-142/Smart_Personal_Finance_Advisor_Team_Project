# 🧠 Smart Personal Finance Advisor

![GitHub last commit](https://img.shields.io/github/last-commit/naveen-142/Smart_Personal_Finance_Advisor_Team_Project)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Django](https://img.shields.io/badge/Django-Backend-green)
![Scikit-learn](https://img.shields.io/badge/ML-Scikit--learn-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

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

---

## 🎯 Key Features

- 💰 **Savings Prediction** — Ridge Regression model for monthly savings  
- 📊 **Interactive Dashboard** — Visual representation of income and expenses  
- 💬 **Personalized Advice** — AI-driven recommendations to boost savings  
- 🧾 **History Tracking** — View previous transactions and financial records  
- ⚙️ **Admin Mode** — Access and manage all users’ records centrally  
- 🧠 **Smart Error Handling** — Shows “No data available” when inputs are missing  

---

## 🧩 System Workflow

1. **User inputs** income, expenses, and debts on the frontend.  
2. **Django backend** sends the data to the ML model.  
3. **Ridge Regression model** returns predictions and insights as JSON.  
4. **Backend** stores the results in **SQLite3** and sends them to the frontend.  
5. **Frontend** displays charts and personalized financial suggestions.

📊 *System Architecture Diagram (Add Image Here)*

---

## 🛠️ Tech Stack

| Layer | Technologies |
|-------|---------------|
| **Frontend** | HTML, CSS, JavaScript, Bootstrap, Vercel |
| **Backend** | Django, Render, REST API |
| **Machine Learning** | Python, Scikit-learn, Pandas, NumPy |
| **Database** | SQLite3 |
| **Visualization** | Matplotlib, Power BI |
| **Version Control** | Git & GitHub |

---

## 👨‍💻 Roles & Responsibilities

### 🧠 **Data Scientist (Naveen Kumar)**
- Collected and preprocessed financial datasets  
- Performed **EDA (Exploratory Data Analysis)** to identify spending patterns  
- Built and tuned **Ridge Regression model** for savings prediction  
- Evaluated model using **R²** and **MAE** metrics  
- Integrated ML model with Django backend  
- Deployed ML interface using **Streamlit**

### 💻 **Backend Developer**
- Developed Django APIs for data exchange  
- Handled **database operations (SQLite3)**  
- Managed model serving and integration with the frontend  

### 🧩 **Frontend Developer**
- Designed UI with **Bootstrap and JavaScript**  
- Implemented pages: Home, Transactions, Advisor, Dashboard, History  
- Connected frontend forms with backend APIs  

### ⚙️ **Full Stack Developer**
- Managed deployment across **Render** and **Vercel**  
- Integrated frontend, backend, and ML components  
- Handled bug fixes, testing, and optimization  

### 📊 **Data Analyst**
- Supported data exploration and visualization  
- Created Power BI dashboards for financial insights  

---

## 📸 Project Screenshots

| Page | Description |
|------|--------------|
| 🏠 **Home Page** | User overview and navigation |
| 🧾 **Transaction Form** | Collects income, expenses, and debts |
| 💡 **Advisor Page** | Displays savings insights or “No data available” |
| 📊 **Dashboard** | Visual charts and financial summaries |
| 📜 **History Page** | Shows past financial records for admin |

📷 *Add Screenshots Here for Better Readability*

---

## 📂 Repository Structure


---

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

## 👥 Contributors

| Name                     | Role                          | LinkedIn                                      | GitHub                                    |
| ------------------------ | ----------------------------- | --------------------------------------------- | ----------------------------------------- |
| **Naveen Kumar**         | Data Scientist & Project Lead | [LinkedIn](https://www.linkedin.com/in/naveen-kumar-viruvuru/) | [GitHub](https://github.com/yourusername) |
| **Aishwarya**            | Data Analyst         | [LinkedIn](#)                                 | [GitHub](#)                               |
| **Varun**                | UI/UX Design                  | [LinkedIn](#)                                 | [GitHub](#)                               |
| **Maneesha**             | Django & Database             | [LinkedIn](#)                                 | [GitHub](#)                               |
| **Hemanth**              | Deployment & Integration      | [LinkedIn](#)                                 | [GitHub](#)                               |


## 📧 Contact

- Maintainer: Naveen Kumar
- Role: Data Scientist
- 📩 [Gmail](naveenkv681@gmail.com)
- 🔗 [Linkedin](https://www.linkedin.com/in/naveen-kumar-viruvuru/)
- 📘 [GitHub Profile](https://github.com/naveen-142)
