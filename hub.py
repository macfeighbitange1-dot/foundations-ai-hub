import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Foundations AI Hub", page_icon="🌍", layout="wide")

# 2. Sidebar Navigation (Fixing the KeyError)
with st.sidebar:
    st.title("💠 AI Ecosystem")
    
    # We use the label "Home" but don't force the URL link to 'hub.py' 
    # if it's already the page we are on.
    if st.button("🏠 Back to Home"):
        st.switch_page("hub.py")
        
    st.markdown("---")
    st.write("🌍 **Industry Modules**")
    
    # These are the direct links to your sub-pages
    try:
        st.page_link("pages/1_Guardian.py", label="1. The Guardian", icon="🛡️")
        st.page_link("pages/2_Architect.py", label="2. The Architect", icon="🏗️")
        st.page_link("pages/3_Synthesizer.py", label="3. The Synthesizer", icon="🎨")
        st.page_link("pages/4_Amplifier.py", label="4. The Amplifier", icon="📈")
    except Exception as e:
        st.error("Sidebar loading... please refresh.")

    st.markdown("---")
    st.info("Foundations AI v1.0")

# 3. Main Dashboard Content
st.title("🌍 Foundations AI: Global Hub")
st.subheader("System Dashboard")

col1, col2, col3 = st.columns(3)
col1.metric("Status", "Online")
col2.metric("Modules", "4 Active")
col3.metric("Security", "Verified")

st.markdown("""
---
### Welcome to the Operating System for Responsible AI.
Select an industry module from the sidebar to launch a specific AI auditor or generator.
""")
