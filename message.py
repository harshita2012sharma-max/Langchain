from langchain.message import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

messages=[SystemMessage(content="You are a helpful assistant."),
          HumanMessage(content="Tell me about Langchain")]

reuslt=model.invoke(messages)

messages.append(AIMessage(content=reuslt.content))
print(messages)