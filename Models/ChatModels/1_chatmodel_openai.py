from langchain_openai import ChatOpenAI
from dotenv import  load_dotenv

load_dotenv()

model=ChatOpenAI(model='gpt-4',temperature=1.5,max_completion_token=10)

result=model.invoke("write a 5 line poem on the cricket")

print(result.content)