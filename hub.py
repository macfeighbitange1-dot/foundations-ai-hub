import streamlit as st
import os

# 1. Page Configuration
st.set_page_config(
    page_title="Foundations AI Hub",
    page_icon="🌍",
    layout="wide"
)

# 2. Sidebar Navigation
with st.sidebar:
    st.title("💠 AI Ecosystem")
    st.markdown("---")
    
    st.write("🏠 **Main Menu**")
    st.page_link("hub.py", label="Home Dashboard", icon="🏠")
    
    st.markdown("---")
    st.write("🌍 **Industry Modules**")
    
    # These paths are based on your verified GitHub folder 'pages'
    try:
        st.page_link("pages/1_Guardian.py", label="The Guardian", icon="🛡️")
        st.page_link("pages/2_Architect.py", label="The Architect", icon="🏗️")
        st.page_link("pages/3_Synthesizer.py", label="The Synthesizer", icon="🎨")
        st.page_link("pages/4_Amplifier.py", label="The Amplifier", icon="📈")
    except Exception as e:
        st.error("Sidebar Link Error")
        st.caption("Try rebooting via the 'Manage App' menu.")

    st.markdown("---")
    st.info("Foundations AI v1.0 | Global Industry OS")
    
    # Diagnostic tool (hidden in small text) to check folder health
    if os.path.exists("pages"):
        st.caption("✅ Pages folder detected")
    else:
        st.caption("❌ Pages folder not found")

# 3. Main Dashboard Interface
st.title("🌍 Foundations AI: Global Ecosystem Hub")
st.subheader("The Industry 4.0 Operating System for Responsible AI")

st.markdown("""
---
### Welcome to the Unified AI Dashboard
This platform provides high-end AI services across all sectors. 
Use the sidebar on the left to navigate between our core pillars:

* **🛡️ The Guardian:** Ethics & Fairness Auditor (Healthcare/Finance)
* **🏗️ The Architect:** Predictive Model Generator (Manufacturing/Logistics)
* **🎨 The Synthesizer:** Inclusive Content Lab (Marketing/Creators)
* **📈 The Amplifier:** ROI & Ad-Tech Optimizer (Business Growth)
---
""")

# 4. Live System Metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="System Status", value="Active", delta="Operational")
with col2:
    st.metric(label="Global Coverage", value="100%", delta="Live")
with col3:
    st.metric(label="MLOps Engine", value="Connected", delta="Ready")

st.info("👈 Select a module from the sidebar to launch the specific AI tool.")
