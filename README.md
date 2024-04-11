# Talk to Web

<div style="display: flex; align-items: center; gap: 10px;">
<a href='https://hub.docker.com/repository/docker/igormcsouza/talk2web/general' target="_blank"><img alt='Docker' src='https://img.shields.io/badge/Docker_Hub-100000?style=for-the-badge&logo=Docker&logoColor=FFFFFF&labelColor=2496ED&color=2496ED'/></a>
<a href='https://github.com/igormcsouza/gpt4shell' target="_blank"><img alt='Github' src='https://img.shields.io/badge/See_also GPT4SHELL-100000?style=for-the-badge&logo=Github&logoColor=FFFFFF&labelColor=3BB02C&color=3BB02C'/></a>
<a href="https://github.com/igormcsouza/talk2web/actions/workflows/publish.yml" target="_blank"><image alt="Publish on Docker Hub" src="https://github.com/igormcsouza/talk2web/actions/workflows/publish.yml/badge.svg"></a>
</div>

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

Streamlit app will pop up on the browser.

### In a hurry? Just spin up a docker container

You can run a app container direct from docker.io, since the image was built there, this way you can test even without pulling the repository, below you can find the command to run the container even if you don't have the image built locally.

    docker run --env-file .env igormcsouza/talk2web:latest

Or just send the environment variable you already have set on your system

    docker run --e OPENAI_API_KEY igormcsouza/talk2web:latest

It should now be running at [http://localhost:8501](http://localhost:8501), no need to do any port forwarding.

You can also check the version available at [Docker Hub](https://hub.docker.com/repository/docker/igormcsouza/talk2web/tags), usually, every new tag on the repository has a match on docker hub.

### What can be used as source?

As of today, the app is able to transcript into context **any website**, **online pdfs** and **youtube videos**, just paste the link for one of the services and it is going to load the context.

## Contribution

I'm accepting contribution if that means to bring value to the project.

## License

Do what ever you want with it.
