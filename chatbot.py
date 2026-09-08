from langchain_openai import ChatOpenAI, OpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


load_dotenv()
model=ChatOpenAI()

"""
while True:
    input('You: ')
    if user_input == 'exit':
        break
    result= model.invoke(user_input)
    print('AI:',result.content)

there is no chat context in the above code snippet, so the model will not be able to provide context-aware responses.
 To maintain context, you can use a conversation history or a memory mechanism to keep track of previous interactions. 
 Here's an example of how you can implement a simple conversation loop with context:
"""

"""
chat_history=[]

while True:
    user_input=input('You :')
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    result= model.invoke(chat_history)
    chat_history.append(result.content)
    print('AI:',result.content)

print(chat_history)

In this example we have stored the user input and ai response and systm response in list 
chat history but we can't just differentiate between user input and ai response. and to differentiate it we will be 
using message 
From langchain_core.message import SystemMessage,HumanMessage,AIMessage
"""

chat_history=[
SystemMessage(content="You are a helpful assistant.")

]

while True:
    user_input=input('You :')
    chat_history.append(HumanMessage=user_input)
    if user_input == 'exit':
        break
    result= model.invoke(chat_history)
    chat_history.append(AIMessage=result.content)
    print('AI:',result.content)

print(chat_history)