# Bibliotecas importadas
import google.generativeai as gemini_ai
import os # Biblioteca para acessar o arquivo .env
from dotenv import load_dotenv # Importe load_dotenv

# Importando a FastAPI - que ajuda na integração do frontend com o backend
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

# A chamada da API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
gemini_ai.configure(api_key=GEMINI_API_KEY)
model = gemini_ai.GenerativeModel('gemini-2.5-flash') # o modelo escolhido / pode ser alterado

# FastAPI
app = FastAPI(
    title="NutriCIn API",
    description="Gera receitas personalizadas usando o modelo Gemini",
    version="1.0.0"
)

class GerarReceita(BaseModel):
    ingredientes: str
    porcoes: int
    restricao: str | None = None

# Geração da receita
@app.post("/gerar_receita/")
def gerar_receita(dados: GerarReceita):
    prompt = (
        f"Gere uma receita apenas com os ingredientes: {dados.ingredientes}, "
        f"fornecendo informações como quantidade, tempo de preparo e utensílios necessários "
        f"para uma receita que sirva {dados.porcoes} porções. "
        f"Evite as seguintes restrições: {dados.restricao or 'nenhuma'}."
    )

    resposta = model.generate_content(prompt)
    print(resposta.text) # Resposta em texto