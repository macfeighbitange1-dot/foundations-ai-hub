import streamlit as st

st.title("🎨 The Synthesizer: Content Lab")
st.write("Create inclusive and high-impact messaging for any audience.")

audience = st.text_input("Who is the target audience?", placeholder="e.g. Local Farmers")
topic = st.text_area("What is the main message?")

if st.button("Synthesize Content"):
    st.subheader("Your Generated Strategy")
    st.write(f"**Tone:** Inclusive & Empathetic")
    st.success(f"**Draft:** 'Welcome {audience}, here is how {topic} can transform your daily operations...'")
    st.info("💡 Content has been audited for cultural sensitivity.")
