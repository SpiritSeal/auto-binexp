from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()


model = ChatOpenAI(
    # model="claude-3-opus",
    model="oai-gpt-4o",
    base_url="http://bombshell.gtisc.gatech.edu:4000",
    api_key=os.getenv("LITELLM_API_KEY"),
    temperature=0,
)