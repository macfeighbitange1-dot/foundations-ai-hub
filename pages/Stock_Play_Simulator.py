import streamlit as st
import numpy as np

st.title("Stock Play Simulator: Learn & Win")
st.write("Simulate trades and pro up. Play daily!")

investment = st.number_input("Invest ($)", min_value=0.0)
if st.button("Simulate"):
    return_ = investment * np.random.uniform(0.9, 1.2)
    st.metric("Simulated Return", f"${return_:,.2f}")

    # Addictiveness
    st.session_state.user_profile['points'] += 20
    if "Market Pro" not in st.session_state.user_profile['badges']:
        st.session_state.user_profile['badges'].append("Market Pro")
        st.success("Pro Badge! Build virtual portfolio.")
