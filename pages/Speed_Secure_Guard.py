import streamlit as st
import requests

st.title("Speed Secure Guard: Make Your Site Fly Safe")
st.write("Enter URL and audit. Earn medals for secure speeds!")

url = st.text_input("Site URL")
if st.button("Audit"):
    try:
        resp = requests.get(url, timeout=5)
        speed = resp.elapsed.total_seconds()
        secure = "Yes" if url.startswith("https") else "No"
        st.metric("Load Time", f"{speed:.2f}s")
        st.metric("Secure?", secure)
        if speed > 3:
            st.warning("Tip: Optimize images!")
    except:
        st.error("URL error—try again.")

    # Addictiveness
    st.session_state.user_profile['points'] += 15
    if "Site Hero" not in st.session_state.user_profile['badges']:
        st.session_state.user_profile['badges'].append("Site Hero")
        st.success("Hero Badge! Guard daily for bonuses.")
