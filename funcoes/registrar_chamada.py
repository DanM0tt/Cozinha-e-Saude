from funcoes.prompt_parser import promptParser

def registrarChamada(historico, prompt, resposta):
    
    historico.append({
        "prompt": prompt,
        "resposta": promptParser(resposta)
    })