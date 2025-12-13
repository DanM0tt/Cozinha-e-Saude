from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request, APIRouter
from fastapi.templating import Jinja2Templates  #Jinja2

from classes.receita import Receita
from funcoes.prompt_parser import promptParser
from funcoes.registrar_chamada import registrarChamada
from rotas.api import api_router

app = FastAPI(
    title="NutriCIn API",
    description="Gera receitas personalizadas usando o modelo Gemini",
    version="1.0.0"
)

app.include_router(api_router)

app.mount('/scripts', StaticFiles(directory='nutricin-frontend/scripts'))
app.mount('/css', StaticFiles(directory='nutricin-frontend/css'))
app.mount('/img', StaticFiles(directory='nutricin-frontend/img'))

# template jinja2 para renderizar html
templates = Jinja2Templates(directory="nutricin-frontend")

# endpoints para renderização html

@app.get('/', response_class=HTMLResponse)
async def renderizar_pagina_login(request: Request):
        return templates.TemplateResponse(
        request=request,
        name="login.html"
    )

@app.get('/receita', response_class=HTMLResponse)
async def renderizar_pagina_principal(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="nutricin.html"
    )
    
@app.get('/cadastro', response_class=HTMLResponse)
async def renderizar_pagina_cadastro(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="cadastro.html"
    )

@app.get('/historico', response_class=HTMLResponse)
async def renderizar_pagina_historico(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="historico.html"
    )