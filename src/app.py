import streamlit as st

st.set_page_config(
    page_title="Chat with Websites",
    page_icon="🚀",
)


st.title("🚀 Chat with Websites")

with st.sidebar:
    st.header("About")
    st.markdown(
        """
        This application allows you to chat with various websites.
        Simply enter the URL of the website you want to interact with,
        and start your conversation!
        """
    )
    website_url = st.text_input("Enter Website URL")



with st.chat_message("Human"):
    st.markdown("Hello! I would like to chat with a website.")

with st.chat_message("AI"):
    st.markdown("Sure! Please provide the URL of the website you want to chat with.")