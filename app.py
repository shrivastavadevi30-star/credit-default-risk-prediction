
import streamlit as st

st.set_page_config(
    page_title="Credit Default Risk Prediction",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Credit Default Risk Prediction System")

st.write(
    "Welcome! This application uses Machine Learning "
    "to predict credit card default risk."
)

st.info("Our Machine Learning model will be connected here.")

st.markdown("""
<style>
.stApp {
    background-color: #F4F7FB;
}

h1 {
    color: #17365D;
}

.stButton button {
    background-color: #17365D;
    color: white;
    border-radius: 8px;
}
</style>
""")

st.subheader("About This Project")

st.write("""
This system uses Machine Learning algorithms
to analyze customer credit information and
estimate the possibility of credit card default.

The system is developed for educational purposes.
""")

st.success("Website design added successfully!")

import joblib

# Load the trained Machine Learning model
model = joblib.load('best_credit_default_model.pkl')

st.success("Machine Learning model connected successfully!")

st.header("Customer Information")

with st.form("customer_form"):

    st.subheader("1. Personal and Credit Information")

    col1, col2 = st.columns(2)

    with col1:
        X1 = st.number_input("Credit Limit", value=50000)
        X2 = st.selectbox("Gender", [1, 2])
        X3 = st.selectbox("Education", [1, 2, 3, 4, 5, 6, 0])
        X4 = st.selectbox("Marital Status", [1, 2, 3, 0])
        X5 = st.number_input("Age", min_value=18, max_value=100, value=30)

    st.subheader("2. Previous Payment Status")

    col3, col4 = st.columns(2)

    with col3:
        X6 = st.selectbox("September Repayment Status", [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
        X7 = st.selectbox("August Repayment Status", [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
        X8 = st.selectbox("July Repayment Status", [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
        X9 = st.selectbox("June Repayment Status", [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
        X10 = st.selectbox("May Repayment Status", [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
        X11 = st.selectbox("April Repayment Status", [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8])

    st.subheader("3. Bill Amounts")

    with col4:
        X12 = st.number_input("September Bill Amount", value=50000)
        X13 = st.number_input("August Bill Amount", value=45000)
        X14 = st.number_input("July Bill Amount", value=40000)
        X15 = st.number_input("June Bill Amount", value=35000)
        X16 = st.number_input("May Bill Amount", value=30000)
        X17 = st.number_input("April Bill Amount", value=25000)

    st.subheader("4. Previous Payments")

    col5, col6 = st.columns(2)

    with col5:
        X18 = st.number_input("September Payment", value=2000)
        X19 = st.number_input("August Payment", value=2000)
        X20 = st.number_input("July Payment", value=2000)

    with col6:
        X21 = st.number_input("June Payment", value=2000)
        X22 = st.number_input("May Payment", value=2000)
        X23 = st.number_input("April Payment", value=2000)

    submitted = st.form_submit_button("Submit Customer Information")

import pandas as pd

if submitted:

    customer_data = pd.DataFrame([{
        'X1': X1,
        'X2': X2,
        'X3': X3,
        'X4': X4,
        'X5': X5,
        'X6': X6,
        'X7': X7,
        'X8': X8,
        'X9': X9,
        'X10': X10,
        'X11': X11,
        'X12': X12,
        'X13': X13,
        'X14': X14,
        'X15': X15,
        'X16': X16,
        'X17': X17,
        'X18': X18,
        'X19': X19,
        'X20': X20,
        'X21': X21,
        'X22': X22,
        'X23': X23
    }])

    prediction = model.predict(customer_data)[0]
    probability = model.predict_proba(customer_data)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("Higher predicted risk of credit card default.")
    else:
        st.success("Lower predicted risk of credit card default.")

    st.write(f"Model-estimated default probability: {probability * 100:.2f}%")

    st.caption(
        "Educational prototype only. This prediction is not a "
        "reliable assessment for real credit decisions."
    )
