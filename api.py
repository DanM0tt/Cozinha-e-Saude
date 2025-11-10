# Bibliotecas importadas
from fastapi.responses import HTMLResponse
from classes.receita import Receita
# Importando a FastAPI - que ajuda na integração do frontend com o backend
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
# importando Jinja2
from fastapi.templating import Jinja2Templates


def promptParser(resposta): 
    texto = ""
    if hasattr(resposta, "text") and resposta.text:
        texto = resposta.text.strip()
        print("if! entrou")
    elif hasattr(resposta, "candidates"):
        print("elif entrou")
        texto = resposta.candidates[0].content.parts[0].text.strip()
    else:
        print("else entrou")
        texto = "Não foi possível obter resposta do modelo."
    return texto

# FastAPI
app = FastAPI(
    title="NutriCIn API",
    description="Gera receitas personalizadas usando o modelo Gemini",
    version="1.0.0"
)
# pip install Jinja2

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



@app.get('/', response_class=HTMLResponse)
async def renderizar_html(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="nutricin.html"
    )

@app.post("/gerar_receita/")
async def promptDaReceita(receita: Receita):
    
    resposta = receita.gerar()
    print("resposta.text: \n")
    print(resposta.text)
    print("resposta.candidates: \n")
    print(resposta.candidates[0].content.parts[0].text)
    # Garante que captura o texto do Gemini corretamente
    return promptParser(resposta)
    