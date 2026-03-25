# 📈 TCS Stock Price Prediction App

## 📌 Project Overview

This project focuses on analyzing historical stock data of Tata Consultancy Services (TCS) and building a machine learning model to predict closing stock prices. The project also includes a Streamlit web application for real-time prediction and visualization.

---

## 🎯 Objectives

- Analyze historical stock price trends  
- Understand relationships between stock variables  
- Build a predictive model for closing price  
- Deploy the model using Streamlit for real-time use  

---

## 🗂️ Dataset Description

The dataset consists of historical stock data with the following features:

- Open Price  
- High Price  
- Low Price  
- Close Price (target variable)  
- Volume  
- Date  

---

## 🧹 Data Preprocessing

- Converted date column into datetime format  
- Extracted year feature from date  
- Handled missing values  
- Selected relevant features for modeling  
- Applied StandardScaler for feature normalization  

---

## 📊 Exploratory Data Analysis

### 🔹 Analysis Performed:

- Year-wise trend of closing price  
- Relationship between trading volume and closing price  

### 📈 Key Observations:

- Stock shows long-term upward trend  
- Price volatility increases over time  
- Trading volume has weak correlation with price  

---

## 🤖 Model Building

- Model Used: **Linear Regression**  
- Features:
  - Open  
  - High  
  - Low  
  - Year  

### ⚙️ Steps:

- Train-test split  
- Feature scaling  
- Model training  

---

## 📊 Model Performance

- Achieved high accuracy with strong R² score  
- Predictions closely align with actual values  

---

## 🚀 Streamlit Web Application

The project includes a fully interactive web application built using Streamlit.

### 🔹 Features:

- Input stock parameters (Open, High, Low, Year)  
- Real-time price prediction  
- Confidence score display  
- Visual comparison charts  
- Historical trend visualization  
- Automated market insights (Bullish/Bearish/Stable)  

---

## 🌐 Live Demo

👉 *(Add your Streamlit link here after deployment)*  
Example:
```
https://your-app-name.streamlit.app
```

---

## ▶️ How to Run Locally

1. Clone the repository:
```bash
git clone https://github.com/your-username/tcs-stock-price-prediction-app.git
```

2. Navigate to the project folder:
```bash
cd tcs-stock-price-prediction-app
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```bash
├── data/
├── app.py
├── model/
│   ├── final_lr_model.pkl
│   ├── standard_scaler_model.pkl
├── notebooks/
│   └── analysis.ipynb
├── requirements.txt
└── README.md
```
> Note: Dataset path is structured for repository usage.

---

## 🛠️ Technologies Used

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Scikit-learn  
- Streamlit  

---

## 🔍 Key Insights

- Closing price is strongly dependent on Open, High, and Low  
- Stock exhibits long-term growth trend  
- Volume alone is not a strong predictor  

---

## 🚀 Future Improvements

- Add time-series models (ARIMA, LSTM)  
- Improve prediction accuracy  
- Deploy with real-time stock API  

---

## 👨‍💻 Author

**Adityakumar Umeshkumar Ahir**  
Data Analyst Intern | Linkedin: https://www.linkedin.com/in/adityaahir/