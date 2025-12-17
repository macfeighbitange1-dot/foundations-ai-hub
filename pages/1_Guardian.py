import streamlit as st

# 1. Hide the duplicate menu
st.markdown("<style>[data-testid='stSidebarNav'] {display: none;}</style>", unsafe_allow_html=True)

# 2. The Sidebar (Must be repeated here)
with st.sidebar:
    st.title("💠 AI Ecosystem")
    st.page_link("hub.py", label="Home Dashboard", icon="🏠")
    st.markdown("---")
    st.write("🌍 **Industry Modules**")
    st.page_link("pages/1_Guardian.py", label="1. The Guardian", icon="🛡️")
    st.page_link("pages/2_Architect.py", label="2. The Architect", icon="🏗️")
    st.page_link("pages/3_Synthesizer.py", label="3. The Synthesizer", icon="🎨")
    st.page_link("pages/4_Amplifier.py", label="4. The Amplifier", icon="📈")

# 3. The Content
st.title("🛡️ The Guardian")
st.subheader("Ethics & Fairness Auditor")
st.info("System is monitoring for algorithmic bias.")
# ... (rest of your Guardian code here)
