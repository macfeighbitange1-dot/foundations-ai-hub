import streamlit as st
import numpy as np

st.title("Health Horizon Scanner: See Risks Ahead")
st.write("Input data and scan. Become a hero with points!")

age = st.number_input("Age", min_value=0)
bmi = st.number_input("BMI", min_value=0.0)
if st.button("Scan"):
    risk = np.random.uniform(0, 100)  # Simulate ML model
    st.metric("Risk Level", f"{risk:.1f}%")
    if risk > 50:
        st.warning("Tip: Exercise more!")

    # Addictiveness
    st.session_state.user_profile['points'] += 20
    if st.session_state.user_profile['streak'] >= 7:
        st.success("Streak Unlock: Weekly wellness challenge!")
