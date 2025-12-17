import streamlit as st
import os

st.set_page_config(page_title="Foundations AI Hub", page_icon="🌍", layout="wide")

# This part ensures the sidebar navigation is clickable
st.sidebar.title("💠 AI Ecosystem")

# Manual Navigation Links
st.sidebar.page_link("hub.py", label="Home Dashboard", icon="🏠")
st.sidebar.markdown("---")
st.sidebar.write("🔒 **Safety & Ethics**")
st.sidebar.page_link("pages/1_Guardian.py", label="The Guardian", icon="🛡️")

st.sidebar.write("⚙️ **Engineering**")
st.sidebar.page_link("pages/2_Architect.py", label="The Architect", icon="🏗️")

st.sidebar.write("📣 **Growth & Content**")
st.sidebar.page_link("pages/3_Synthesizer.py", label="The Synthesizer", icon="🎨")
st.sidebar.page_link("pages/4_Amplifier.py", label="The Amplifier", icon="📈")

# Main Page Content
st.title("🌍 Foundations AI: Global Hub")
st.info("The Industry 4.0 Operating System is live. Select a module from the sidebar to begin.")

# Quick-view Metrics
c1, c2, c3 = st.columns(3)
c1.metric("System", "Online")
c2.metric("Modules", "4 Active")
c3.metric("Security", "Verified")
