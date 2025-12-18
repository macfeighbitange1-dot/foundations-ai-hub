import streamlit as st
import numpy as np
from sklearn.ensemble import IsolationForest
import pandas as pd

st.title("Money Shield: Spot Fraud Fast")
st.write("Upload transactions and detect risks. Earn points for each scan!")

uploaded_file = st.file_uploader("Upload CSV (amount, time, etc.)", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    data = df.values  # Assume numerical features
    model = IsolationForest(contamination=0.1).fit(data)
    anomalies = model.predict(data)
    fraud_count = np.sum(anomalies == -1)
    st.metric("Potential Frauds", fraud_count)
    st.dataframe(df[anomalies == -1].style.highlight_max(color='red'))

    # Addictiveness
    st.session_state.user_profile['points'] += 10
    if st.session_state.user_profile['points'] >= 50:
        if "Fraud Fighter" not in st.session_state.user_profile['badges']:
            st.session_state.user_profile['badges'].append("Fraud Fighter")
            st.success("Badge Unlocked: Fraud Fighter! 🎉")
    st.info(f"Your streak: {st.session_state.user_profile['streak']} days. Keep scanning daily!")
