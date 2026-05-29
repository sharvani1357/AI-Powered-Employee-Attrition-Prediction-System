import streamlit as st
import pandas as pd
import pickle

# Load Model
model = pickle.load(open("employee_attrition_model.pkl", "rb"))

st.set_page_config(
    page_title="AI Employee Attrition Predictor",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

.stApp {
    background-color: #0E1117;
    color: white;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #00E5FF;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #B0BEC5;
    margin-bottom: 30px;
}

.metric-box {
    background-color: #1E293B;
    padding: 15px;
    border-radius: 15px;
    text-align: center;
}

.predict-btn {
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# Header
st.markdown(
    '<div class="title">🤖 AI Employee Attrition Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Predict employee turnover using Machine Learning</div>',
    unsafe_allow_html=True
)

# Sidebar
st.sidebar.title("⚙ Employee Information")

Age = st.sidebar.slider("Age", 18, 60, 30)

BusinessTravel = st.sidebar.selectbox(
    "Business Travel",
    [0, 1, 2]
)

MonthlyIncome = st.sidebar.slider(
    "Monthly Income",
    1000,
    50000,
    5000
)

OverTime = st.sidebar.selectbox(
    "OverTime",
    [0, 1]
)

JobLevel = st.sidebar.selectbox(
    "Job Level",
    [1, 2, 3, 4, 5]
)

TotalWorkingYears = st.sidebar.slider(
    "Total Working Years",
    0,
    40,
    8
)

YearsAtCompany = st.sidebar.slider(
    "Years At Company",
    0,
    40,
    5
)

# Metrics Row
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Age", Age)

with col2:
    st.metric("Income", MonthlyIncome)

with col3:
    st.metric("Experience", TotalWorkingYears)

st.divider()

st.subheader("📋 Employee Summary")

st.write(
    f"""
    - Age: **{Age}**
    - Monthly Income: **₹{MonthlyIncome}**
    - Job Level: **{JobLevel}**
    - OverTime: **{OverTime}**
    """
)

if st.button("🚀 Predict Attrition", use_container_width=True):

    employee_data = [[
        Age,
        BusinessTravel,
        500,
        1,
        10,
        3,
        2,
        1,
        100,
        3,
        1,
        70,
        3,
        JobLevel,
        4,
        2,
        1,
        MonthlyIncome,
        12000,
        2,
        1,
        OverTime,
        15,
        3,
        3,
        80,
        1,
        TotalWorkingYears,
        2,
        3,
        YearsAtCompany,
        3,
        1,
        3
    ]]

    prediction = model.predict(employee_data)

    st.divider()

    if prediction[0] == 1:

        st.error(
            "⚠ HIGH ATTRITION RISK\n\nEmployee is likely to leave the organization."
        )

    else:

        st.success(
            "✅ LOW ATTRITION RISK\n\nEmployee is likely to stay in the organization."
        )