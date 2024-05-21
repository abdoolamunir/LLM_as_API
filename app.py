from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv
load_dotenv()
os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="LLM as API",
    description="An example of LLM as API",
    version="0.1.0",
) 
model = ChatOpenAI()
# OpenAI
add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

# Prompt 1 will interact with OpenAI
prompt1 = ChatPromptTemplate.from_template("Write me a short description of {topic} in less than 100 words")

# Ollama
llm = Ollama(model = "gemma")
# Prompt 2 will interact with Ollama
prompt2 = ChatPromptTemplate.from_template("Write me a short haiku about {topic} ")

add_routes(

    app,
    prompt1|model,
    path="/prompt1"
)

add_routes(

    app,
    prompt2|llm,
    path="/prompt2"
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
