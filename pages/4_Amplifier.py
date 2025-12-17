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

st.title("📈 The Amplifier: ROI Optimizer")
st.write("Analyze and scale your business impact through Ad-Tech optimization.")

# Interactive Features
budget = st.number_input("Ad Spend ($)", min_value=0)
reach = st.slider("Target Reach (Users)", 1000, 1000000, 50000)

if st.button("Calculate ROI Impact"):
    projected_roi = (reach * 0.05) / (budget + 1)
    st.metric("Estimated Conversion Rate", "5.2%", "+1.2%")
    st.metric("Projected Revenue Lift", f"${budget * 4}", "+$12,000")
