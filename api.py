# Bibliotecas importadas
import google.generativeai as gemini_ai
import os # Biblioteca para acessar o arquivo .env
from dotenv import load_dotenv # Importe load_dotenv

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

# A chamada da API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
gemini_ai.configure(api_key=GEMINI_API_KEY)

# A parte abaixo apenas printa os modelos (fica caso queiram mudar o modelo depois)
#    modelos = gemini_ai.list_models()
#    for model in modelos:
#        if "generateContent" in model.supported_generation_methods:
#            print(f"Nome do Modelo: {model.name}")
#
model = gemini_ai.GenerativeModel('gemini-2.5-flash') # o modelo escolhido / pode ser alterado

# A estrutura de geração de resposta é a seguinte: resposta = model.generate_content( <prompt> )
ingredientes_disponiveis = input("Digite os alimentos disponíveis: ")
qnt_porcoes = int(input("Informe a quantidade de porções desejada: "))
restricao = input("Informe quaisquer restrições alimentares que você tenha (ex: vegetariano, intolerante a lactose): ")

prompt = f"Gere uma receita apenas com os ingredientes: {ingredientes_disponiveis}, fornecendo informações como quantidade, tempo de preparo e utensílios necessários para uma receita que sirva {qnt_porcoes} porções. Evite as seguintes restrições: {restricao}"

# Geração da receita
resposta = model.generate_content(prompt)
print(resposta.text) # Resposta em texto