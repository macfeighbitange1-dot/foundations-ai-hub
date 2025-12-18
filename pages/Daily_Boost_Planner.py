import streamlit as st

st.title("Daily Boost Planner: Power Your Day")
st.write("Build habits and boost energy. Unlock customs!")

habit = st.text_input("New Habit")
if st.button("Add"):
    st.success(f"Habit Added: {habit}")

    # Addictiveness
    st.session_state.user_profile['points'] += 15
    if st.session_state.user_profile['streak'] >= 10:
        st.info("Streak Unlock: Custom habit templates!")
