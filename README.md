# 🍽️ Cozinha_e_Saúde

Projeto **NutriCIn** – 2025.2 – CIn

Este repositório contém o backend da aplicação **Cozinha_e_Saúde**, desenvolvida no contexto do projeto NutriCIn. A aplicação disponibiliza uma API para funcionalidades relacionadas à nutrição, receitas e histórico de interações, integrando banco de dados PostgreSQL e a API do **Google Gemini**.

---

## 📌 Visão Geral

* **Linguagem:** Python 3
* **Framework:** FastAPI
* **Servidor ASGI:** Uvicorn
* **Banco de Dados:** PostgreSQL (Render)
* **ORM:** SQLAlchemy
* **IA Generativa:** Google Gemini API
* **Testes:** Pytest

---

## 🏗️ Arquitetura do Projeto

A estrutura do projeto segue uma organização modular, facilitando manutenção, testes e evolução do código:

```
.
├── classes/          # Modelos ORM e entidades do domínio
├── funcoes/          # Lógica de negócio e funções auxiliares
├── rotas/            # Definição das rotas da API (endpoints)
├── tests/            # Testes unitários e de integração
├── nutricin-frontend/# Frontend (quando aplicável)
├── index.py          # Ponto de entrada da aplicação FastAPI
├── requirements.txt  # Dependências do projeto
├── pytest.ini        # Configurações do Pytest
├── CONTRIBUTING.md   # Guia de contribuição
└── README.md         # Documentação do projeto
```

### 📐 Padrões Utilizados

* **Separação de responsabilidades** (rotas, regras de negócio e modelos)
* **Arquitetura em camadas**
* **ORM para persistência de dados**
* **Variáveis de ambiente** para dados sensíveis

---

## 🚀 Como Executar o Projeto Localmente

### 1️⃣ Clonar o Repositório

Copie o link do repositório (HTTPS) e execute no terminal:

```bash
git clone <link-do-repositorio>
```

Acesse a pasta do projeto:

```bash
cd Cozinha_e_Saúde
```

---

### 2️⃣ Criar Chave da API do Gemini

Siga a documentação oficial do Google:

🔗 [https://ai.google.dev/gemini-api/docs/quickstart?hl=pt-br](https://ai.google.dev/gemini-api/docs/quickstart?hl=pt-br)

Guarde sua chave, ela será usada como variável de ambiente.

---

### 3️⃣ Configurar o Banco de Dados (Render)

1. Acesse o painel do Render:
   🔗 [https://dashboard.render.com/](https://dashboard.render.com/)
2. Localize o serviço do banco PostgreSQL
3. Copie a **Connection String** (ex.: `postgresql://...`)

---

### 4️⃣ Criar Arquivo `.env`

Na raiz do projeto, crie um arquivo chamado **`.env`** com o seguinte conteúdo:

```env
GOOGLE_API_KEY=sua_key_da_api
DB_URL=sua_url_do_banco
```

⚠️ **Observações importantes:**

* Não use aspas
* Não adicione espaços
* Não versionar o arquivo `.env`

---

### 5️⃣ Instalar Dependências

No terminal:

```bash
pip install -r requirements.txt
```

---

### 6️⃣ Iniciar o Servidor

```bash
uvicorn index:app --reload
```

---

### 7️⃣ Acessar a Aplicação

* API: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* Documentação automática (Swagger):

  * [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
  * [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧪 Testes

Para executar os testes unitários:

```bash
pytest
```

---

## ☁️ Deploy no Render

### 🔧 Configurações

**Build Command:**

```bash
pip install -r requirements.txt
```

**Start Command:**

```bash
uvicorn index:app --host 0.0.0.0 --port $PORT
```

---

### 🌱 Variáveis de Ambiente (Render)

No painel do Render, aba **Environment**, adicione:

* `GOOGLE_API_KEY`
* `DB_URL`

---

## 🤝 Contribuição

Antes de contribuir, leia o arquivo [CONTRIBUTING.md](./CONTRIBUTING.md).

Boas práticas:

* Commits pequenos e semânticos (`feat`, `fix`, `refactor`, `test`, etc.)
* Código testado
* Padronização de estilo

---

## 📄 Licença

Projeto desenvolvido para fins acadêmicos no **Centro de Informática (CIn – UFPE)**.

---

## 📬 Contato

Projeto NutriCIn – 2025.2

Em caso de dúvidas ou sugestões, utilize as *issues* do repositório.
