import os

from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from tools.search import get_audio_url
from agents.lookup_audio_urls import lookup

NAME = "Mike Onslow"

audio_file_url = lookup(name=NAME)

print(get_audio_url("Mike Onslow"))

if __name__ == "__main__":
    print("Welcome to LangChain!")
