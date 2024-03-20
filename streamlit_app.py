from uuid import UUID

import streamlit as st

from talk2web import (
    Conversation,
    Loader,
    prepare_vector_store,
    prepare_vector_store_from_local,
)

st.set_page_config(page_title="Talk2web - Main Page", page_icon="🤖")

st.title("Talk to the Web")

if "dialog" not in st.session_state:
    st.session_state.dialog = Conversation()

if "url_keys" not in st.session_state:
    st.session_state.url_keys = {}

with st.sidebar:
    st.header("Settings")
    target_url = st.text_input("Enter a valid url...")

if target_url:
    with st.sidebar:
        st.header("Logs")

    if target_url in st.session_state.url_keys:
        key: UUID | None = st.session_state.url_keys.get(target_url)
        if not key:
            raise Exception("Could not locate the key for the given url")
        vector_store = prepare_vector_store_from_local(key)
    else:
        documents, key = Loader(target_url).load()
        vector_store = prepare_vector_store(documents, key)
        st.session_state.url_keys[target_url] = key

    st.session_state.dialog.add_context(vector_store)

    with st.sidebar:
        st.write(f"Vector store loaded successfully at key ({key})")

    question = st.chat_input("Write your question here...")
    if question:
        st.session_state.dialog.add_message(actor="human", content=question)
        st.session_state.dialog.add_message(
            actor="ai", content=st.session_state.dialog.ask(question)
        )

    for message in st.session_state.dialog.get_history():
        with st.chat_message(message.type):
            st.write(message.content)

else:
    st.info("Waiting for a valid url...")
