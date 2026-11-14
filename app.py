
import streamlit as st

st.title("Murtala ATM")

name = st.text_input("What is your name?")
pin = st.text_input("Enter your PIN:", type="password")

if "balance" not in st.session_state:
    st.session_state.balance = 50000

if st.button("Login"):
    if pin == "1234":
        st.success(f"Welcome {name}")
        st.write(f"Your balance is {st.session_state.balance} Naira")
    else:
        st.error("Wrong PIN! Access denied")

amount = st.number_input("Amount:", min_value=0)

if st.button("Deposit"):
    st.session_state.balance += amount
    st.success(f"New balance: {st.session_state.balance}")

if st.button("Withdraw"):
    if amount <= st.session_state.balance:
        st.session_state.balance -= amount
        st.success(f"New balance: {st.session_state.balance}")
    else:
        st.error("Not enough money")
