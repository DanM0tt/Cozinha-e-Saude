def promptParser(resposta): 
    texto = ""
    if hasattr(resposta, "text") and resposta.text:
        texto = resposta.text.strip()
        print("Cod 200 - OK")
    elif hasattr(resposta, "candidates"):
        print("Cod 201 - OK")
        texto = resposta.candidates[0].content.parts[0].text.strip()
    else:
        print("Cod 300 - NOK")
        texto = "Não foi possível obter resposta do modelo."
    return texto