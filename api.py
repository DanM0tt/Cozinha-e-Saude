from google import genai
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

class Receita(BaseModel):
    nome_receita: str
    ingredientes: list[str]

client = genai.Client(api_key = "api_key")
resposta = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="List a few popular cookie recipes, and include the amounts of ingredients.",
    config={
        "response_mime_type": "application/json",
        "response_schema": list[Receita],
    },
)

# Use instantiated objects.
minhas_receitas: list[Receita] = resposta.parsed

print()

for receita in minhas_receitas:
    print(f"{receita.nome_receita}:")

    for ingred in receita.ingredientes:
        print(f"\t- {ingred}")

    print()
