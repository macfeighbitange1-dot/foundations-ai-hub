import streamlit as st

st.title("Symptom Sleuth: Uncover Causes")
st.write("Describe symptoms and sleuth. Earn detective badges!")

desc = st.text_area("Symptoms")
if st.button("Sleuth"):
    diagnosis = "Possible: Flu. See doctor."
    st.info(diagnosis)

    # Addictiveness
    st.session_state.user_profile['points'] += 20
    if st.session_state.user_profile['streak'] >= 5:
        st.success("Streak Unlock: Real case studies!")
