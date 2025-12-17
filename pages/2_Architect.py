import streamlit as st

# Hide default nav
st.markdown("<style>[data-testid='stSidebarNav'] {display: none;}</style>", unsafe_allow_html=True)

# Consistent Sidebar
with st.sidebar:
    st.title("💠 AI Ecosystem")
    st.page_link("hub.py", label="Home Dashboard", icon="🏠")
    st.markdown("---")
    st.write("🌍 **Industry Modules**")
    st.page_link("pages/1_Guardian.py", label="1. The Guardian", icon="🛡️")
    st.page_link("pages/2_Architect.py", label="2. The Architect", icon="🏗️")
    st.page_link("pages/3_Synthesizer.py", label="3. The Synthesizer", icon="🎨")
    st.page_link("pages/4_Amplifier.py", label="4. The Amplifier", icon="📈")
    st.markdown("---")
    st.info("Foundations AI v1.0")

# Content
st.title("🏗️ The Architect")
st.subheader("Predictive Model Generator")
st.write("Generating optimized logistics and manufacturing workflows...")
st.divider()
st.info("Status: Ready for Model Training")
