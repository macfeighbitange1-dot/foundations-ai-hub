import streamlit as st

# 1. Professional Page Configuration
st.set_page_config(
    page_title="Foundations AI Hub",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CSS Hack to Hide the Default Navigation
# This removes the "duplicate" list at the top of the sidebar
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {display: none;}
    </style>
""", unsafe_allow_html=True)

# 3. Custom Sidebar Navigation
with st.sidebar:
    st.title("💠 AI Ecosystem")
    st.markdown("---")
    
    # Home Link
    st.page_link("hub.py", label="Home Dashboard", icon="🏠")
    
    st.markdown("---")
    st.write("🌍 **Industry Modules**")
    
    # These link directly to your files in the 'pages' folder
    st.page_link("pages/1_Guardian.py", label="1. The Guardian", icon="🛡️")
    st.page_link("pages/2_Architect.py", label="2. The Architect", icon="🏗️")
    st.page_link("pages/3_Synthesizer.py", label="3. The Synthesizer", icon="🎨")
    st.page_link("pages/4_Amplifier.py", label="4. The Amplifier", icon="📈")
    
    st.markdown("---")
    st.info("Foundations AI v1.0 | Global Industry OS")

# 4. Main Dashboard Interface
# Note: This part only shows when you are on the "Home" page
st.title("🌍 Foundations AI: Global Hub")
st.subheader("The Industry 4.0 Operating System")

st.markdown("""
---
### Welcome to the Unified AI Dashboard
The core modules are now synchronized. Use the **Industry Modules** menu in the sidebar 
on the left to navigate through the ecosystem.
---
""")

# Professional Metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="System Status", value="Active", delta="Operational")
with col2:
    st.metric(label="Global Coverage", value="100%", delta="Live")
with col3:
    st.metric(label="MLOps Engine", value="Connected", delta="Ready")

st.success("👈 Select a module from the sidebar to begin.")
