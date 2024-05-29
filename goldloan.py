import streamlit as st
import math

def roundup(x):
    return int(math.floor(x / 100.0)) * 100

def goldloan(reduced_weight, weight, rate):
    
    gold_price = rate * reduced_weight
    # 85% of the reduced weight is the loan amount
    loan_amount = reduced_weight * rate * 0.85
    # 15% of the reduced weight is the margin money
    margin_money = reduced_weight * rate * 0.15

    return gold_price, reduced_weight, loan_amount, margin_money

st.title("Gold Loan Calculator")

col1, col2 = st.columns(2)

with col1:
    st.header("Enter the details")

    weight = st.number_input("Enter the weight of the gold in grams", min_value=0.0, step=0.1)

    # reduced_weight = st.number_input("Reduced weight of the gold in grams", value=1.0, step=0.1)

    rate = st.number_input("Enter the rate of gold per gram in INR", min_value=0.0, step=0.1)

    changed_weight = st.number_input("Final weight of the gold in grams", value = weight - (weight * 0.1), step=0.01)

    percent_reduction = st.number_input("No. of Grams reduced", value = weight - changed_weight, disabled=True)
    # purity = st.selectbox("Enter the purity of the gold",['20K','22K'])

    result = st.button("Calculate")

with col2:
    if result:
        gold_price, reduced_weight, loan_amount, margin_money = goldloan(changed_weight, weight, rate)
        st.header("Gold Loan Details")
        st.metric("Weight", f"{changed_weight} grams")
        st.metric(f"Total Price" ,f"₹{round(gold_price,2)}")
        st.metric("Loan Amt (85%)", f"₹{round(loan_amount,2)}")
        st.metric("Margin Amt (15%)", f"₹{round(margin_money,2)}")
        