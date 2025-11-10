# Bibliotecas importadas

#FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware  #CORS
from fastapi.templating import Jinja2Templates  #Jinja2

#Modularização
from classes.receita import Receita
from funcoes.prompt_parser import promptParser
from funcoes.registrar_chamada import registrarChamada

# FastAPI
app = FastAPI(
    title="NutriCIn API",
    description="Gera receitas personalizadas usando o modelo Gemini",
    version="1.0.0"
)

# Aplicação do template Jinja2 para renderização local do projeto
app.mount('/scripts', StaticFiles(directory='nutricin-frontend/scripts'))
app.mount('/css', StaticFiles(directory='nutricin-frontend/css'))
templates = Jinja2Templates(directory="nutricin-frontend")

# Aceitando requisições de outros domínios para realizar a integração com o front-end
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoints

@app.get('/', response_class=HTMLResponse)
async def renderizar_html(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="nutricin.html"
    )

@app.post("/gerar_receita/")
async def promptDaReceita(receita: Receita):
    
    resposta, prompt = receita.gerar()
    registrarChamada(prompt, resposta)

    # Garante que captura o texto do Gemini corretamente
    return promptParser(resposta)

    