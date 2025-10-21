Orientações e boas práticas para a contribuição com o projeto ***NutriCIn🌿:***

# **Issues**

Para abrir uma nova issue sobre o projeto, você deve:

> Ir até a aba *“Issues”* → *“New Issue”*
> 

> Coloque um título direto na sua issue e a descreva de forma clara e concisa
> 

> Espere que seja analisada e aprovada pelos demais integrantes do trabalho
> 

---

## Issue aprovada

> Crie uma nova branch para resolver a sua issue
> 

<aside>

git checkout -b feature/nova-funcionalidade

</aside>

> Faça as alterações necessárias e os seus próprios testes locais
> 

> Faça o commit descritivo (descrição mais abaixo no documento)
> 

<aside>

inclua o texto ”(closes #n)” ao final do texto do seu commit, sendo esse n o número da issue desse problema, para que o GitHub possa fechá-la automaticamente após a conclusão

</aside>

> Envie suas alterações para o repositório remoto
> 

<aside>

git push origin feature/nova-funcionalidade

</aside>

> Vá até o GitHub novamente e crie uma Pull Request (PR), para que os demais membros da equipe possam analisar e aprovar ou não suas mudanças
> 

> Após a aprovação complete o merge
> 

# Commits

| Tipo | Prefixo | Exemplo |
| --- | --- | --- |
| Nova funcionalidade | `feature/` | `feature/tela-de-login` |
| Correção de bug | `fix/` | `fix/erro-autenticacao` |
| Documentação | `docs/` | `docs/contributing-update` |
| Refatoração | `refactor/` | `refactor/otimizacao-batalha` |
| Style | `style/` | `style/organizacao-arquivos` |
| test | `test/` | `test/teste-login` |

## Mensagens de commits

> Seja claro, direto e siga os padrões descritos na tabela acima.
> 

# Pull Request (PR)

Antes de adicionar o seu PR no GitHub, verifique o seguinte:

- Seu código está funcionando localmente
- Todos os testes realizados tiveram êxito
- As mensagens de commit seguem o padrão descrito acima
- O código está legível, organizado e comentado (quando necessário)
- A documentação (README.md) foi atualizada (se necessário)

# Configurando o projeto localmente

1. Clone o repositório localmente

<aside>

git clone https://github.com/DanM0tt/Cozinha-e-Saude.git

</aside>

2. Instale as bibliotecas necessárias

<aside>

pip install pydantic google-generativeai python-dotenv fastapi

</aside>

3. Execute o projeto

<aside>

1. Baixe o uvicorn -> pip install uvicorn
2. Rode o comando uvicorn api:app
3. Copie o link http://127.0.0.1:8000/ no seu navegador
4. Abra o arquivo `nutricin.html`

</aside>

# Código de conduta

Mantenha um ambiente respeitoso, colaborativo e aberto a sugestões.

Discussões e revisões devem ser sempre feitas com empatia e educação. ❤️
