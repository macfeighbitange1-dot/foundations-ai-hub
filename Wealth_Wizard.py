import streamlit as st
import numpy as np
import requests
import pandas as pd

st.title("Wealth Wizard: Build Your Dream Portfolio")
st.write("Optimize investments and watch your wealth grow. Earn stars for simulations!")

assets = st.multiselect("Pick Assets (e.g., AAPL, TSLA)", ["AAPL", "TSLA", "GOOG", "MSFT"])
api_key = "your_polygon_key"  # Replace with env var
if st.button("Optimize"):
    data = {}
    for asset in assets:
        resp = requests.get(f"https://api.polygon.io/v2/aggs/ticker/{asset}/range/1/day/2024-01-01/2025-12-18?apiKey={api_key}")
        if resp.status_code == 200:
            data[asset] = [d['c'] for d in resp.json().get('results', [])]  # Close prices
    if data:
        returns = pd.DataFrame(data).pct_change().dropna()
        cov = returns.cov()
        weights = np.linalg.solve(cov, np.ones(len(assets))) / np.sum(np.linalg.solve(cov, np.ones(len(assets))))
        st.bar_chart(weights, use_container_width=True)
        st.write("Optimal Weights:", dict(zip(assets, weights)))

        # Addictiveness
        st.session_state.user_profile['points'] += 20
        if len(st.session_state.user_profile['badges']) >= 3:  # Example threshold
            st.session_state.user_profile['badges'].append("Master Investor")
            st.success("Badge Unlocked: Master Investor! Share your portfolio? 📈")
