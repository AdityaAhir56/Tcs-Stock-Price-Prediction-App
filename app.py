import streamlit as st
import numpy as np
import pickle
import matplotlib.pyplot as plt
import pandas as pd

# Load model
with open('model/final_lr_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load scaler
with open('model/standard_scaler_model.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Load dataset
data = pd.read_csv('data/tcs_data.csv')
data['Date'] = pd.to_datetime(data['Date'], dayfirst=True, errors='coerce')

# Page config
st.set_page_config(page_title="TCS Predictor", layout="wide")

# ---------------- HEADER ----------------
st.markdown("""
# 📈 TCS Stock Price Predictor  
### 🚀 Real-Time AI-Based Forecasting System
""")

st.markdown("---")

# ---------------- SIDEBAR ----------------
st.sidebar.header("⚙️ Model Info")

st.sidebar.markdown("""
**Model:** Linear Regression  
**Scaling:** StandardScaler  

**Features Used:**
- Open
- High
- Low
- Year  

**Accuracy (Approx):**
R² Score: 0.98  

**Purpose:**  
Predict stock closing price using historical data.
""")

# ---------------- INPUT SECTION ----------------
st.subheader("🔢 Input Stock Parameters")

col1, col2 = st.columns(2)

with col1:
    Open = st.number_input("Open Price", min_value=0.0, value=0.0)
    High = st.number_input("High Price", min_value=0.0, value=0.0)

with col2:
    Low = st.number_input("Low Price", min_value=0.0, value=0.0)
    Recorded_Year = st.number_input("Year", min_value=2000, max_value=2100, value=2024)

# ---------------- PREDICT ----------------
if Open != 0 or High != 0 or Low != 0:

    input_data = np.array([[Open, High, Low, Recorded_Year]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0][0]

    # ---------------- OUTPUT ----------------
    st.markdown("---")
    st.subheader("💰 Prediction Result")

    colA, colB = st.columns(2)

    with colA:
        st.metric(
            label="Predicted Closing Price",
            value=f"₹ {prediction:.2f}",
            delta=f"{prediction - Open:.2f} vs Open"
        )

    with colB:
        avg_price = (Open + High + Low) / 3
        st.metric(
            label="Average Input Price",
            value=f"₹ {avg_price:.2f}"
        )

    # ---------------- CONFIDENCE SCORE ----------------
    st.markdown("### 🎯 Confidence Score")

    confidence = 98  # Based on your R² score (update if needed)

    st.progress(confidence / 100)
    st.write(f"Model Confidence: **{confidence}%**")

    # ---------------- VISUALIZATION ----------------
    st.markdown("---")
    st.subheader("📊 Visual Analysis")

    col3, col4 = st.columns(2)

    # Bar Chart
    with col3:
        labels = ['Open', 'High', 'Low', 'Predicted']
        values = [Open, High, Low, prediction]

        fig, ax = plt.subplots()
        ax.bar(labels, values)
        ax.set_title("Price Comparison")
        st.pyplot(fig)

    # Trend Line
    with col4:
        fig2, ax2 = plt.subplots()
        ax2.plot(labels, values, marker='o')
        ax2.set_title("Price Trend")
        st.pyplot(fig2)

    # ---------------- REAL DATA GRAPH ----------------
    st.markdown("---")
    st.subheader("📉 Historical Stock Trend")

    fig3, ax3 = plt.subplots()
    ax3.plot(data['Date'], data['Close'])
    ax3.set_title("TCS Historical Close Price")
    ax3.set_xlabel("Date")
    ax3.set_ylabel("Close Price")

    st.pyplot(fig3)

    # ---------------- AI EXPLANATION ----------------
    st.markdown("---")
    st.subheader("🤖 Insight")

    if prediction > High:
        explanation = "The model predicts a bullish trend, indicating that the closing price may exceed the daily high due to strong upward momentum."
    elif prediction < Low:
        explanation = "The model predicts a bearish trend, indicating a possible drop below the daily low due to weak market conditions."
    else:
        explanation = "The model predicts a stable trend, suggesting that the closing price will remain within the expected range."

    st.info(explanation)

    # ---------------- FOOTER ----------------
    st.markdown("---")
    st.caption("Developed as part of Data Analyst Internship Project | C.K. Pithawalla College of Engineering and Technology GTU BE CO Final Year")

else:
    st.info("👆 Enter stock values to see prediction")