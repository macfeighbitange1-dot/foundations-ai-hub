import streamlit as st

st.title("Wellness Glow Up: Shine Brighter")
st.write("Plan wellness and level glow. Unlock challenges!")

goal = st.text_input("Wellness Goal")
if st.button("Plan"):
    plan = "Day 1: Walk. Day 2: Meditate."
    st.text_area("Your Glow Plan", plan)

    # Addictiveness
    st.session_state.user_profile['points'] += 15
    if st.session_state.user_profile['streak'] >= 5:
        st.success("Streak Unlock: New challenge—'30-day glow'!")
