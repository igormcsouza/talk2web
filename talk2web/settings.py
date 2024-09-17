from os import getenv


DEFAULT_OPENAI_MODEL_LIST = "gpt-3.5-turbo,gpt-4o-mini-2024-07-18,gpt-4o-2024-08-06,gpt-4.0-turbo"
OPENAI_MODEL_LIST = getenv("OPENAI_MODEL_LIST", DEFAULT_OPENAI_MODEL_LIST).split(',')