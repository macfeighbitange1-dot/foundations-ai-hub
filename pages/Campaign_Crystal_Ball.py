import streamlit as st
import numpy as np

st.title("Campaign Crystal Ball: See Future Wins")
st.write("Input campaign data and predict ROI. Become a mystic!")

spend = st.number_input("Spend ($)", min_value=0.0)
expected_ctr = st.number_input("Expected CTR (%)", min_value=0.0)
if st.button("Predict"):
    roi = spend * (expected_ctr / 100) * np.random.uniform(1, 5)  # Simulate
    st.metric("Predicted ROI", f"{roi:.2f}x")

    # Addictiveness
    st.session_state.user_profile['points'] += 25
    if len(st.session_state.user_profile['badges']) >= 5:
        st.session_state.user_profile['badges'].append("Marketing Mystic")
        st.success("Mystic Badge! Predict daily for trends.")
