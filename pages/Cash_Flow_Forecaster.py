import streamlit as st
import pandas as pd
from prophet import Prophet  # Assuming available or similar

st.title("Cash Flow Forecaster: See Tomorrow's Money")
st.write("Input data and predict flows. Unlock levels with forecasts!")

data = st.text_area("CSV: Date, Amount")
if st.button("Forecast"):
    df = pd.read_csv(io.StringIO(data))
    df.columns = ['ds', 'y']
    model = Prophet().fit(df)
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    st.line_chart(forecast[['ds', 'yhat']])

    # Addictiveness
    st.session_state.user_profile['points'] += 25
    if st.session_state.user_profile['streak'] >= 3:
        st.info("Streak Unlock: Advanced scenario—'What if rates rise 2%?'")
