from langchain_openai import ChatOpenAI


model = ChatOpenAI(
    # model="claude-3-opus",
    model="oai-gpt-4o",
    base_url="http://bombshell.gtisc.gatech.edu:4000",
    api_key="sk-G8auP8ht3njROVrqEe6EYQ",
    temperature=0,
)