import streamlit as st
from sklearn.linear_model import LogisticRegression
import numpy as np

st.title("Credit Booster: Unlock Better Scores")
st.write("Input details for personalized credit advice. Level up with each boost!")

income = st.number_input("Annual Income ($)", min_value=0)
debt = st.number_input("Current Debt ($)", min_value=0)
if st.button("Boost My Score"):
    # Simple model (train on dummy data)
    X = np.array([[50000, 10000], [30000, 20000]])  # Income, Debt
    y = [1, 0]  # Good/Bad credit
    model = LogisticRegression().fit(X, y)
    score = model.predict_proba([[income, debt]])[0][1] * 850  # FICO-like
    st.metric("Estimated Score", int(score))
    advice = "Pay down debt first!" if debt > income * 0.3 else "Great job—consider investing!"
    st.info(advice)

    # Addictiveness
    st.session_state.user_profile['points'] += 15
    if st.session_state.user_profile['streak'] >= 5:
        st.success("Streak Bonus: Unlock premium tip—'Diversify credit types for 10% boost!'")
