from uuid import UUID

import streamlit as st

from talk2web import (
    Conversation,
    Loader,
    prepare_vector_store,
    prepare_vector_store_from_local,
    settings
)


if "dialog" not in st.session_state:
    model = settings.OPENAI_MODEL_LIST[0]
    temperature = 0.7
    st.session_state.dialog = Conversation(model=model, temperature=temperature)

if "isWaiting" not in st.session_state:
    st.session_state.isWaiting = True

st.set_page_config(page_title="Talk2web - Main Page", page_icon="🤖")

st.title("Talk to the Web")

if "url_keys" not in st.session_state:
    st.session_state.url_keys = {}

with st.sidebar:
    st.header("Inputs")
    target_url = st.text_input("Enter a valid url...")

    st.divider()

    st.header("Settings")

    temperature = st.slider(
        "Set the temperature",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.05,
        disabled=not target_url,
    )

    model = st.selectbox(
        "Select the model",
        options=settings.OPENAI_MODEL_LIST,
        index=0,
        disabled=not target_url,
    )

    if st.button("Update Settings", disabled=not target_url):
        st.session_state.dialog.update_temperature(temperature)
        if model:
            st.session_state.dialog.update_model(model)
        st.toast("Settings updated successfully", icon="🎉")

if target_url:
    st.session_state.isWaiting = True

    with st.sidebar:
        st.divider()
        st.header("Logs")

    if target_url in st.session_state.url_keys:
        key: UUID | None = st.session_state.url_keys.get(target_url)
        if not key:
            raise Exception("Could not locate the key for the given url")
        vector_store = prepare_vector_store_from_local(key)
    else:
        documents, key = Loader(target_url).load()
        vector_store = prepare_vector_store(documents=documents, key=key)
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
    # Message to the user explaining how to use the app
    st.write(
        "Please enter a valid url in the sidebar to start the conversation."
    )
