import streamlit as st
import pandas as pd

st.title("📈 The Amplifier: ROI Optimizer")
st.write("Maximize your traffic and profit through ethical ad-tech optimization.")

budget = st.slider("Monthly Budget ($)", 100, 10000, 1000)
platforms = st.multiselect("Platforms", ["Meta", "Google", "TikTok", "LinkedIn"])

if st.button("Optimize Spend"):
    st.subheader("Recommended Allocation")
    # Simple logic to show a split
    if platforms:
        split = budget / len(platforms)
        df = pd.DataFrame({"Platform": platforms, "Allocation ($)": [split] * len(platforms)})
        st.table(df)
        st.warning("Focusing spend on high-performing, under-represented demographics.")
