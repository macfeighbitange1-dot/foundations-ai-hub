import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("Rule Keeper: Stay Compliant Easily")
st.write("Upload policies and check for gaps. Earn stars for safe scans!")

doc = st.text_area("Paste Document Text")
rules = ["AML compliance required", "GDPR data protection"]  # USA rules
if st.button("Audit"):
    vectorizer = TfidfVectorizer()
    vecs = vectorizer.fit_transform([doc] + rules)
    sim = cosine_similarity(vecs[0:1], vecs[1:])[0]
    gaps = [r for s, r in zip(sim, rules) if s < 0.5]
    if gaps:
        st.warning("Gaps Found: " + ", ".join(gaps))
    else:
        st.success("All clear!")

    # Addictiveness
    st.session_state.user_profile['points'] += 10
    if st.session_state.user_profile['points'] % 100 == 0:
        st.session_state.user_profile['badges'].append("Rule Master")
        st.balloons()
