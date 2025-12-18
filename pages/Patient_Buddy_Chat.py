import streamlit as st

st.title("Patient Buddy Chat: Your Health Pal")
st.write("Chat for support. Build bonds daily!")

message = st.text_input("Your Message")
if st.button("Send"):
    response = "I'm here! How can I help?"
    st.chat_message("bot").write(response)

    # Addictiveness
    st.session_state.user_profile['points'] += 10
    if "Health Friend" not in st.session_state.user_profile['badges']:
        st.session_state.user_profile['badges'].append("Health Friend")
        st.success("Friend Badge! Chat daily for check-ins.")
