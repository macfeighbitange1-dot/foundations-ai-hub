import streamlit as st

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
    st.write("🌍 **Industry Modules**")
    
    # This block tries to find your pages. 
    # If the first way fails, it automatically tries the second way.
    try:
        st.page_link("pages/1_Guardian.py", label="1. The Guardian", icon="🛡️")
        st.page_link("pages/2_Architect.py", label="2. The Architect", icon="🏗️")
        st.page_link("pages/3_Synthesizer.py", label="3. The Synthesizer", icon="🎨")
        st.page_link("pages/4_Amplifier.py", label="4. The Amplifier", icon="📈")
    except:
        try:
            st.page_link("1_Guardian.py", label="1. The Guardian", icon="🛡️")
            st.page_link("2_Architect.py", label="2. The Architect", icon="🏗️")
            st.page_link("3_Synthesizer.py", label="3. The Synthesizer", icon="🎨")
            st.page_link("4_Amplifier.py", label="4. The Amplifier", icon="📈")
        except:
            st.error("Navigation setup in progress...")
            st.info("Check if files are inside the 'pages' folder on GitHub.")

    st.markdown("---")
    st.info("Foundations AI v1.0 | Global Industry OS")

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

st.info("👈 Use the 'Industry Modules' menu in the sidebar to explore specific tools.")
