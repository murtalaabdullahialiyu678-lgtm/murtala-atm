
import streamlit as st
import random

st.title("📈 Murtala Trader - BTC")

if "balance" not in st.session_state:
    st.session_state.balance = 50000
if "btc_price" not in st.session_state:
    st.session_state.btc_price = 95000

st.write(f"Your balance is {st.session_state.balance} Naira")
st.write(f"Bitcoin Price Now: ${st.session_state.btc_price}")

st.write("---")
amount = st.number_input("How much you wan stake?", min_value=100, max_value=10000, value=1000)

col1, col2 = st.columns(2)

with col1:
    if st.button("🟢 UP - Price go go up"):
        old_price = st.session_state.btc_price
        new_price = old_price + random.randint(-2000, 2000)
        st.session_state.btc_price = new_price
        if new_price > old_price:
            win = int(amount * 1.8)
            st.session_state.balance += win
            st.success(f"You WIN! Price go from ${old_price} to ${new_price}. You win {win} Naira!")
        else:
            st.session_state.balance -= amount
            st.error(f"You LOSE! Price go from ${old_price} to ${new_price}. You lose {amount} Naira.")

with col2:
    if st.button("🔴 DOWN - Price go go down"):
        old_price = st.session_state.btc_price
        new_price = old_price + random.randint(-2000, 2000)
        st.session_state.btc_price = new_price
        if new_price < old_price:
            win = int(amount * 1.8)
            st.session_state.balance += win
            st.success(f"You WIN! Price go from ${old_price} to ${new_price}. You win {win} Naira!")
        else:
            st.session_state.balance -= amount
            st.error(f"You LOSE! Price go from ${old_price} to ${new_price}. You lose {amount} Naira.")

if st.button("Reset Balance"):
    st.session_state.balance = 50000
    st.session_state.btc_price = 95000
