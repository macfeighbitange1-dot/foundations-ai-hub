import streamlit as st

st.title("Journal Insight Spark: Reflect & Grow")
st.write("Journal daily and spark insights. Become a guru!")

entry = st.text_area("Your Journal Entry")
if st.button("Analyze"):
    insight = "Key Theme: Growth mindset."
    st.info(insight)

    # Addictiveness
    st.session_state.user_profile['points'] += 10
    if "Reflection Guru" not in st.session_state.user_profile['badges']:
        st.session_state.user_profile['badges'].append("Reflection Guru")
        st.success("Guru Badge! Journal daily for deeper sparks.")
