import streamlit as st
import numpy as np

st.title("Test Winner Pro: Find What Wins")
st.write("Simulate A/B tests. Become a champion with wins!")

variant_a = st.number_input("Variant A Clicks", min_value=0)
variant_b = st.number_input("Variant B Clicks", min_value=0)
if st.button("Run Test"):
    p_value = np.random.uniform(0, 1)  # Simulate stats test
    winner = "A" if p_value < 0.05 else "B" if p_value > 0.95 else "Tie"
    st.metric("Winner", winner)

    # Addictiveness
    st.session_state.user_profile['points'] += 10
    if st.session_state.user_profile['streak'] >= 7:
        st.success("Streak Unlock: Pro Variant—Try multivariate!")
