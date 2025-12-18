import streamlit as st
import random  # Simulate generation; use real API in prod

st.title("Content Spark Creator: Ignite Ideas")
st.write("Generate optimized content up to 5000 words. Spark your genius!")

topic = st.text_input("Topic")
word_limit = 5000
if st.button("Create"):
    # Simulate content (real: use Grok API or similar)
    content = " ".join(random.choices(["Lorem ipsum dolor sit amet,"] * 1000, k=word_limit // 5))[:word_limit]
    st.text_area("Generated Content", content, height=300)
    st.download_button("Download", content, "content.txt")

    # Addictiveness
    st.session_state.user_profile['points'] += 30
    if st.session_state.user_profile['streak'] >= 5:
        st.success("Streak Unlock: New theme—'Investment Secrets'!")
