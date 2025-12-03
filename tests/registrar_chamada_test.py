from funcoes.registrar_chamada import registrarChamada


def test_registrar_chamada_com_text(historico=[]):
    # Limpa histórico antes do teste
    historico.clear()

    # Cria uma resposta simulada com atributo .text
    class TesteResposta:
        text = "Receita simulada"

    prompt = "Gere uma receita x"
    resposta = TesteResposta()

    registrarChamada(historico, prompt, resposta)

    assert len(historico) == 1
    assert historico[0]["prompt"] == prompt
    assert historico[0]["resposta"] == "Receita simulada"


def test_registrar_chamada_sem_text(historico=[]):
    historico.clear()

    class TesteResposta:
        pass  # sem atributo .text

    prompt = "Gere uma receita x"
    resposta = TesteResposta()

    registrarChamada(historico, prompt, resposta)

    assert len(historico) == 1
    assert historico[0]["prompt"] == prompt
    assert historico[0]["resposta"] == "Não foi possível obter resposta do modelo."
