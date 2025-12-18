import streamlit as st
from sklearn.cluster import KMeans
import numpy as np

st.title("Audience Whisperer: Know Your Crowd")
st.write("Segment users and unlock secrets. Become a sage!")

data = st.text_area("User Data CSV (age,income)")
if st.button("Whisper"):
    df = pd.read_csv(io.StringIO(data))
    kmeans = KMeans(n_clusters=3).fit(df)
    st.write("Segments:", kmeans.labels_)

    # Addictiveness
    st.session_state.user_profile['points'] += 25
    if "Audience Sage" not in st.session_state.user_profile['badges']:
        st.session_state.user_profile['badges'].append("Audience Sage")
        st.success("Sage Badge! Whisper daily for insights.")
