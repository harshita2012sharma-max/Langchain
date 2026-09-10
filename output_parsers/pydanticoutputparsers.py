from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field

load_dotenv()

llm=HuggingFaceEndpoint(
    repi_id="google/gema-2-2b-it",
    task="text-generation"
)

model=ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name:str=Field(description='Name of the person')
    age:int=Field(gt=18,description='Age of the person')
    city:str = Field(description='Name of the city person belong to')

parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template='Generate the name ,age,city of a fictional {place} person \n {format_instruction}',
    input_variable=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain=template | model | parser

final_result=chain.invoke({'place':'New York'})
print(final_result)