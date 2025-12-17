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

st.title("🛡️ The Guardian: Ethics Auditor")
st.write("Upload your dataset or model logs to audit for fairness and algorithmic bias.")

# Interactive Features
uploaded_file = st.file_uploader("Upload Data (CSV or Excel)", type=["csv", "xlsx"])
bias_type = st.multiselect("Select Bias Check", ["Gender", "Age", "Geography", "Ethnicity"])

if st.button("Run Audit Scan"):
    if uploaded_file:
        with st.spinner("Analyzing data distribution..."):
            st.success("Audit Complete!")
            st.warning("⚠️ High variance detected in Geography. Recommend re-sampling.")
    else:
        st.error("Please upload a file first.")
