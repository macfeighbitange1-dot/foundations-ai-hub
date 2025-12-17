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

st.title("🏗️ The Architect: Model Generator")
st.write("Configure and train predictive models for logistics and manufacturing.")

# Interactive Features
industry = st.selectbox("Select Industry", ["Supply Chain", "Renewable Energy", "Smart Cities"])
complexity = st.select_slider("Model Complexity", options=["Lightweight", "Standard", "Enterprise"])
prompt = st.text_input("Describe the specific goal", placeholder="e.g., Optimize shipping routes for Kenya")

if st.button("Generate Architecture"):
    st.info(f"Building {complexity} {industry} model for: {prompt}")
    st.progress(100)
    st.code("import tensorflow as tf\nmodel = tf.keras.Sequential([...])", language="python")
