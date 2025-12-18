import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title("Click Heat Tracker: See Where Users Love")
st.write("Upload clicks and visualize. Earn guru status with tracks!")

clicks = st.file_uploader("Click Data CSV (x,y)", type="csv")
if clicks:
    df = pd.read_csv(clicks)
    fig, ax = plt.subplots()
    ax.hexbin(df['x'], df['y'], gridsize=30, cmap='viridis')
    st.pyplot(fig)

    # Addictiveness
    st.session_state.user_profile['points'] += 15
    if "Site Guru" not in st.session_state.user_profile['badges']:
        st.session_state.user_profile['badges'].append("Site Guru")
        st.success("Badge: Site Guru! Analyze daily for more.")
