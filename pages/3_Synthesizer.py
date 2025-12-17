import streamlit as st

st.markdown("<style>[data-testid='stSidebarNav'] {display: none;}</style>", unsafe_allow_html=True)
with st.sidebar:
    st.title("💠 AI Ecosystem")
    st.page_link("hub.py", label="Home Dashboard", icon="🏠")
    st.markdown("---")
    st.page_link("pages/1_Guardian.py", label="1. The Guardian", icon="🛡️")
    st.page_link("pages/2_Architect.py", label="2. The Architect", icon="🏗️")
    st.page_link("pages/3_Synthesizer.py", label="3. The Synthesizer", icon="🎨")
    st.page_link("pages/4_Amplifier.py", label="4. The Amplifier", icon="📈")

st.title("🎨 The Synthesizer: Creative Lab")
st.write("Generate culturally inclusive marketing content using AI prompts.")

# Interactive Features
audience = st.text_input("Who is your target audience?", "Local artisans")
message = st.text_area("What is your core message?", "Fair trade empowers communities.")
tone = st.radio("Select Tone", ["Professional", "Inspirational", "Friendly"], horizontal=True)

if st.button("Synthesize Now"):
    with st.spinner("Generating..."):
        st.subheader("Draft Output:")
        st.write(f"**{tone} Version:** Our mission is to ensure that {audience.lower()} are recognized and rewarded fairly. Because {message.lower()}")
        st.balloons()
