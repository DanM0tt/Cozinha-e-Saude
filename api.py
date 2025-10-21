# Bibliotecas importadas
import google.generativeai as gemini_ai
import os # Biblioteca para acessar o arquivo .env
from dotenv import load_dotenv # Importe load_dotenv
import json

# Importando a FastAPI - que ajuda na integração do frontend com o backend
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

# A chamada da API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
gemini_ai.configure(api_key=GOOGLE_API_KEY)
model = gemini_ai.GenerativeModel('gemini-2.5-flash') # o modelo escolhido / pode ser alterado

# FastAPI
app = FastAPI(
    title="NutriCIn API",
    description="Gera receitas personalizadas usando o modelo Gemini",
    version="1.0.0"
)

# Aceitando requisições de outros domínios para realizar a integração com o front-end
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GerarReceita(BaseModel):
    ingredientes: str
    porcoes: int
    restricao: str | None = None

class Receita(BaseModel):
    titulo: str
    ingredientes: list[str]
    modo_preparo: str
    tempo_preparo_min: int

# Geração da receita
@app.post("/gerar_receita/")
async def gerar_receita(dados: GerarReceita):
    prompt = f"""
    Gere uma receita usando apenas os ingredientes: {dados.ingredientes}.
    Sirva {dados.porcoes} porções.
    Evite as restrições: {dados.restricao or 'nenhuma'}.
    """

    resposta = model.generate_content(prompt)

    # Garante que captura o texto do Gemini corretamente
    texto = ""
    if hasattr(resposta, "text") and resposta.text:
        texto = resposta.text.strip()
    elif hasattr(resposta, "candidates"):
        texto = resposta.candidates[0].content.parts[0].text.strip()
    else:
        texto = "Não foi possível obter resposta do modelo."

    return texto