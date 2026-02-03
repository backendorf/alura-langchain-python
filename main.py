from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

numero_dias = 7
numero_criancas = 2
atividade = "Nadar"

prompt = f"Crie um roteiro de viagem de {numero_dias} dias, para uma família com {numero_criancas} crianças, que gosta de {atividade}."

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)

messages = [
    SystemMessage(content="Você é um assistente de roteiro de viagens."),
    HumanMessage(content=prompt)
]

response = llm.invoke(messages)

print(response.content)
