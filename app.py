import requests as rq
import streamlit as st
import requests as rq


def send_post(
    message_body: str,
    url: str = "http://172.16.24.60:5678/webhook/ce9a31a3-3ca8-4d03-aaad-2da31e96a93c",
):
    """Send a POST request to the webhook."""
    payload = {"prompt": message_body}
    response = rq.post(url=url, data=payload)
    return response.json()


# Streamlit UI
st.write("Hello, please write your body")
text_input = st.text_area("Body")
check_send_post = st.button("Send!")

if check_send_post:
    message = send_post(text_input)
    st.info("Message sent")
    st.success(message)
