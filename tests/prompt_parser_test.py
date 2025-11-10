from funcoes.prompt_parser import promptParser

def test_prompt_parser_com_texto():
    # Resposta tem atributo .text não vazio -> retorna texto limpo
    class Resposta:
        text = "   Olá mundo!   "

    resposta = Resposta()
    resultado = promptParser(resposta)

    assert resultado == "Olá mundo!"


def test_prompt_parser_com_candidates():
    # Resposta tem .candidates -> pega candidates[0].content.parts[0].text
    class Parte:
        text = "  Texto candidato  "

    class Conteudo:
        parts = [Parte()]

    class Candidate:
        content = Conteudo()

    class Resposta:
        candidates = [Candidate()]

    resposta = Resposta()
    resultado = promptParser(resposta)

    assert resultado == "Texto candidato"


def test_prompt_parser_sem_atributos():
    # Resposta sem .text e sem .candidates -> mensagem padrão
    class Resposta:
        pass

    resposta = Resposta()
    resultado = promptParser(resposta)

    assert resultado == "Não foi possível obter resposta do modelo."
