import streamlit as st
st.title("🛡️ The Guardian: Fairness Auditor")
st.write("Ensuring ethical AI in Healthcare, Finance, and Education.")
st.info("Upload your dataset to check for demographic bias.")
uploaded_file = st.file_uploader("Upload CSV", type="csv")
if uploaded_file:
    st.success("File uploaded! Audit in progress...")
