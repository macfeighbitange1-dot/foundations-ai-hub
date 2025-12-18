import streamlit as st

st.title("Ad Dream Maker: Craft Winning Ads")
st.write("Input ideas and make dreams. Collect stars!")

idea = st.text_area("Ad Idea")
if st.button("Make"):
    ad = f"Headline: {idea[:20]}... Body: Engage now!"
    st.text_area("Dream Ad", ad)

    # Addictiveness
    st.session_state.user_profile['points'] += 15
    if st.session_state.user_profile['streak'] >= 3:
        st.info("Streak Unlock: Gallery of pro templates!")
