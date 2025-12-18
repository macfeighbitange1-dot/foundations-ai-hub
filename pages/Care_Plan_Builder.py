import streamlit as st

st.title("Care Plan Builder: Custom Health Paths")
st.write("Input symptoms and build. Master with stars!")

symptoms = st.text_area("Symptoms")
if st.button("Build"):
    plan = "Step 1: Rest. Step 2: Medicate. Step 3: Follow-up."
    st.text_area("Your Plan", plan)

    # Addictiveness
    st.session_state.user_profile['points'] += 15
    if "Plan Master" not in st.session_state.user_profile['badges']:
        st.session_state.user_profile['badges'].append("Plan Master")
        st.info("Master Unlock: Personalized health recipes!")
