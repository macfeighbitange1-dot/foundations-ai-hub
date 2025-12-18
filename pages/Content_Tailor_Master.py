import streamlit as st

st.title("Content Tailor Master: Perfect Fit for Users")
st.write("Input user data and tailor content. Master levels await!")

user_age = st.slider("User Age", 18, 100)
interests = st.multiselect("Interests", ["Tech", "Finance", "Health"])
if st.button("Tailor"):
    content = f"Personalized for {user_age}-year-old: Dive into {', '.join(interests)} tips!"
    st.text_area("Tailored Content", content, height=200)

    # Addictiveness
    st.session_state.user_profile['points'] += 20
    if st.session_state.user_profile['streak'] >= 4:
        st.info("Streak Unlock: Custom template—'Add AI images!'")
