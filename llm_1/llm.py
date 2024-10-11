from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
chave_api = os.getenv("OPENAI_API_KEY")


modelo = ChatOpenAI(model="gpt-3.5-turbo")
parser = StrOutputParser()


template_mensagem = ChatPromptTemplate.from_messages([
    ("system", "Traduza o texto a seguir para {idioma}"),
    ("user", "{texto}")
])

prompt = template_mensagem.invoke({"idioma": "inglês", "texto": "oi mundo"})

chain = modelo | parser


resultado = chain.invoke(prompt)

print(resultado)
