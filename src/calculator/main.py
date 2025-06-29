import streamlit as st
import math

st.set_page_config(page_title="Loan EMI Calculator", layout="centered")

# --- Header ---
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>💰 Loan EMI Calculator</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Calculate your monthly loan repayment easily</h4>", unsafe_allow_html=True)
st.write("")

# --- Input Fields ---
st.sidebar.header("Enter Loan Details")
loan_amount = st.sidebar.number_input("Loan Amount (PKR)", min_value=1000.0, step=1000.0, format="%.2f")
interest_rate = st.sidebar.number_input("Annual Interest Rate (%)", min_value=0.0, step=0.1, format="%.2f")
loan_term = st.sidebar.slider("Loan Term (in Years)", min_value=1, max_value=30, step=1)

# --- EMI Calculation Function ---
def calculate_emi(principal, annual_rate, years):
    monthly_rate = (annual_rate / 12) / 100
    months = years * 12

    if monthly_rate == 0:
        emi = principal / months
    else:
        emi = principal * monthly_rate * ((1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)

    total_payment = emi * months
    total_interest = total_payment - principal

    return round(emi, 2), round(total_payment, 2), round(total_interest, 2)

# --- Calculation & Output ---
if st.sidebar.button("Calculate EMI"):
    if loan_amount > 0 and interest_rate >= 0 and loan_term > 0:
        emi, total_payment, total_interest = calculate_emi(loan_amount, interest_rate, loan_term)

        st.success("📊 EMI Calculation Results")
        st.markdown(f"""
        <div style="background-color: #f0f9f0; padding: 15px; border-radius: 10px;">
            <h3 style="color: #2e7d32;">Monthly EMI: PKR {emi:,.2f}</h3>
            <h4>Total Payment: PKR {total_payment:,.2f}</h4>
            <h4>Total Interest: PKR {total_interest:,.2f}</h4>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("Please enter valid loan details.")
