from langchain_openai import OpenAI
fron dotenv import load_dotenv

load_dotenv()
llm=OPENAI(model='gpt-3.5-turbo-instruct')

result=llm.invoke("What is the capital of the india")
print(result)