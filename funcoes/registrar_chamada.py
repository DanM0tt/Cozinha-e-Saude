historico = []

def registrarChamada(prompt, resposta):
    if hasattr(resposta, "text"): 
        resp = resposta.text 
    elif hasattr(resposta, "candidates"):
        resp = resposta.candidates[0].content.parts[0].text.strip()
    else: 
        resp = None

    historico.append({
        "prompt": prompt,
        "resposta": resp
    })