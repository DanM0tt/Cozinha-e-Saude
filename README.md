# Cozinha_e_Saúde
Projeto NutriCIn - 2025.2 - CIn

Para que o programa funcione, siga os seguintes passos:
1. Clone o repositório localmente: 

    Copie o link do repositório da opção HTTPS; 
    
    No terminal do VSCode, sem as aspas, digite 
    >*git clone "link do repositório"*

2. Crie sua chave API do Gemini:

    As instruções estão no link: https://ai.google.dev/gemini-api/docs/quickstart?hl=pt-br.

3. Acesse o painel onde seu banco de dados foi criado (Render):

    Entre no link do render: https://dashboard.render.com/

    Procure pelo botão "Connect" ou "Connection String"
    
    Copie a URL completa (geralmente começa com postgresql:// ou similar)
    
4. Crie um arquivo, na mesma pasta do git clonado:

    Ele deve se chamar exatamente *.env*;
    
    Crie a variável GOOGLE_API_KEY e coloque a sua key da API do Gemini.

    Crie a variável DB_URL e coloque o URL do banco de dados
    
    Não adicione aspas nem espaços!

    Ex.:
    >GOOGLE_API_KEY="sua key"
    
    >DB_URL="seu url"

5. Instale as Dependências do projeto no terminal do VSCode:
    > pip install -r requirements.txt

6. Inicie o Servidor usando esse comando:
    > uvicorn index:app --reload

7. Acesse o projeto para ver a API rodando:
    
    Abra o link http://127.0.0.1:8000/ no seu navegador

Deploy (Render):
Para realizar o deploy na plataforma Render, siga estas configurações:

1. Instalando comandos de configuração:
    
    Build Command:
    > pip install -r requirements.txt

    Start Command:
    > uvicorn index:app --host 0.0.0.0 --port $PORT

2. Adicionar Variáveis de Ambiente na aba Environment:
    
    Adicione no painel do Render, aba "Environment":

    >GOOGLE_API_KEY="sua key"
    >DB_URL="seu url"
