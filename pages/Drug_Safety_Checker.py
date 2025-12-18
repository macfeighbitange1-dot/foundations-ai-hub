import streamlit as st
# Assuming rdkit available

st.title("Drug Safety Checker: Stay Safe")
st.write("Input drugs and check. Earn shields!")

drugs = st.multiselect("Drugs", ["Aspirin", "Ibuprofen"])
if st.button("Check"):
    interaction = "No major issues." if len(drugs) < 3 else "Possible interaction!"
    st.info(interaction)

    # Addictiveness
    st.session_state.user_profile['points'] += 15
    if st.session_state.user_profile['streak'] >= 4:
        st.success("Streak Unlock: Subscribe to alerts!")
