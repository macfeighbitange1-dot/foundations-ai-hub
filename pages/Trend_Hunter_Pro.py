import streamlit as st
import requests

st.title("Trend Hunter Pro: Catch the Next Big Thing")
st.write("Search trends and hunt trophies. Become the king!")

query = st.text_input("Trend Query")
if st.button("Hunt"):
    # Simulate (real: use Google Trends API)
    trends = ["AI Boom", "Crypto Rise", "Green Tech"]
    st.list_container(trends)

    # Addictiveness
    st.session_state.user_profile['points'] += 20
    if "Trend King" not in st.session_state.user_profile['badges']:
        st.session_state.user_profile['badges'].append("Trend King")
        st.success("King Badge! Hunt daily for alerts.")
