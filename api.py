# Bibliotecas importadas

#FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware  #CORS
from fastapi.templating import Jinja2Templates  #Jinja2
from fastapi import Depends
#Modularização
from classes.receita import Receita
from classes.usuario import UserLogin
from funcoes.prompt_parser import promptParser
from funcoes.registrar_chamada import registrarChamada
from classes.banco_de_dados import UsuarioDB
from sqlalchemy.orm import Session
from classes.banco_de_dados import get_db
from funcoes.hashing_algorithm import *
# FastAPI
#
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
@app.post('/api/usuarios')
async def logarUsuario(usuario: UserLogin, db: Session = Depends(get_db)):
    print(usuario.email)
    query = db.query(UsuarioDB).filter_by(email=usuario.email).first()
    # comparando a senha digitada pelo usuario com a senha com hash
    if not verify_password_hash(usuario.senha, query.senha):
        raise HTTPException(status_code=404, detail="usuário não encontrado xd")
    
    return {
        "nome_usuario": query.username,
        "user_id": query.id
    }
    
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
    

@app.post("/gerar_receita/")
async def promptDaReceita(receita: Receita):
    
    resposta, prompt = receita.gerar()
    registrarChamada(prompt, resposta)

    # Garante que captura o texto do Gemini corretamente
    return promptParser(resposta)

    