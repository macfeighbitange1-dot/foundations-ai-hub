import streamlit as st

st.title("Money Habit Hero: Build Wealth Daily")
st.write("Track finances and hero up. Unlock levels!")

income = st.number_input("Monthly Income")
expenses = st.number_input("Expenses")
if st.button("Advise"):
    savings = income - expenses
    st.metric("Monthly Savings", f"${savings:,.2f}")
    advice = "Hero Tip: Save 20%!"

    # Addictiveness
    st.session_state.user_profile['points'] += 10
    if st.session_state.user_profile['points'] >= 100:
        st.session_state.user_profile['badges'].append("Wealth Hero")
        st.success("Hero Unlocked! Set goals for more.")
