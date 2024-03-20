# Talk to Web

This is a personal project to help me to query documents and webpages on the web, usually I find documentations or articles online and have to go thru it to find the answer for my questions, which can be boring and takes too much time, with this tool, I can simple put the website link in the app and ask the llm to answer me according to the context, it isn't that amazing?

It works by making good use of RAG. Which does a semantic search on the database of context and retrieve the snippets that most make sense for the question, limiting the size of the input on the LLM, saving money and resources, the speed is not incredable, but goes very close to the `chatgpt`.

I'm using FAISS (for database and search) and OPENAI (for llm). Those 2 makes a great app.

## How to start

This project uses `poetry` to manage python dependencies, so make sure it is installed and running properly. There is also a .devcontainer if you want to use `Vscode Dev Container`.

First, install the system wide dependencies by running the following commands

    chmod +x dependencies.sh
    ./dependencies.sh

After that, install the python project and its dependencies according to what we have on poetry.lock

    poetry install

There is one single configuration with is to create a `.env` file or set the following variables on your system

    OPENAI_API_KEY=<from openai api manager>

With all set, run the application with the following command

    poetry run task start

Alternatively, you can run direct from docker.io, since the image was built there, this way you can test even without pulling the repository

    docker run --env-file .env igormcsouza/talk2web:0.1.0

Streamlit app will pop up on the browser.

## Contribution

I'm accepting contribution if that means to bring value to the project

## License

Do what ever you want with it.
