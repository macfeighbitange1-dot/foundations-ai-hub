import streamlit as st
import datetime

# 1. Professional Page Configuration
st.set_page_config(
    page_title="Foundations AI Hub",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CSS Hack to Hide the Default Navigation
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {display: none;}
    </style>
""", unsafe_allow_html=True)

# =============================================
# GLOBAL ADDICTIVENESS SYSTEM
# =============================================
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {
        'points': 0,
        'badges': [],
        'streak': 0,
        'last_login': None
    }

# Update daily streak
today = datetime.date.today()
if st.session_state.user_profile['last_login'] != today:
    if st.session_state.user_profile['last_login'] == today - datetime.timedelta(days=1):
        st.session_state.user_profile['streak'] += 1
    else:
        st.session_state.user_profile['streak'] = 1
    st.session_state.user_profile['last_login'] = today

    # Milestone reward
    if st.session_state.user_profile['streak'] % 7 == 0:
        st.session_state.user_profile['points'] += 50

# =============================================
# 3. Custom Sidebar Navigation
# =============================================
with st.sidebar:
    st.title("💠 AI Ecosystem")
    st.markdown("---")

    # Home Link
    st.page_link("hub.py", label="Home Dashboard", icon="🏠")

    st.markdown("---")
    st.write("🌍 **Industry Modules**")

    # Core Modules
    st.page_link("pages/1_Guardian.py", label="1. The Guardian", icon="🛡️")
    st.page_link("pages/2_Architect.py", label="2. The Architect", icon="🏗️")
    st.page_link("pages/3_Synthesizer.py", label="3. The Synthesizer", icon="🎨")
    st.page_link("pages/4_Amplifier.py", label="4. The Amplifier", icon="📈")

    # New Creative Tools Section
    st.markdown("---")
    st.write("🆕 **Creative Power Tools**")
    st.page_link("pages/Content_Spark_Creator.py", label="Content Spark Creator", icon="✨")

    # User Profile Display (Addictive Feedback)
    st.markdown("---")
    st.subheader("🏆 Your Progress")
    st.metric("Total Points", st.session_state.user_profile['points'])
    st.write(f"🔥 Current Streak: **{st.session_state.user_profile['streak']} days**")
    
    if st.session_state.user_profile['badges']:
        st.write("🏅 Badges: " + " • ".join(st.session_state.user_profile['badges']))
    else:
        st.write("🏅 Badges: None yet – start creating!")

    if st.session_state.user_profile['streak'] % 7 == 0 and st.session_state.user_profile['streak'] > 0:
        st.balloons()
        st.success(f"🎉 {st.session_state.user_profile['streak']}-day streak! +50 bonus points earned!")

    st.markdown("---")
    st.info("Foundations AI v1.0 | Global Industry OS")

# =============================================
# 4. Main Dashboard Interface (Home Page Only)
# =============================================
st.title("🌍 Foundations AI: Global Hub")
st.subheader("The Industry 4.0 Operating System")

st.markdown("""
---
### Welcome to the Unified AI Dashboard
The core modules are now synchronized. Use the **Industry Modules** and **Creative Power Tools** in the sidebar
to navigate through the ecosystem and unlock your creative potential.
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
st.caption("Come back daily to grow your streak and unlock exclusive rewards! 🔥")
