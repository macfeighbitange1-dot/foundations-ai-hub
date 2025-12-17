import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Foundations AI Hub",
    page_icon="🌍",
    layout="wide"
)

# 2. Sidebar Navigation (Manual Override)
with st.sidebar:
    st.title("Navigation")
    st.page_link("hub.py", label="Home", icon="🏠")
    st.markdown("---")
    st.write("🌍 **Industry Modules**")
    
    # These lines force the pages to be clickable buttons
    st.page_link("pages/1_Guardian.py", label="1. The Guardian", icon="🛡️")
    st.page_link("pages/2_Architect.py", label="2. The Architect", icon="🏗️")
    st.page_link("pages/3_Synthesizer.py", label="3. The Synthesizer", icon="🎨")
    st.page_link("pages/4_Amplifier.py", label="4. The Amplifier", icon="📈")
    
    st.markdown("---")
    st.info("Foundations AI v1.0 | Global Industry OS")

# 3. Main Interface
st.title("🌍 Foundations AI: Global Ecosystem Hub")
st.subheader("The Industry 4.0 Operating System for Responsible AI")

st.markdown("""
---
### Welcome to the Unified AI Dashboard
The core modules are now active. Please use the **buttons in the sidebar** to navigate.
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
