from unittest.mock import MagicMock, patch
from sqlalchemy.orm import Session

from funcoes.prompt_parser import promptParser
from funcoes.registrar_chamada import registrarChamada
from classes.banco_de_dados import ReceitaDB


def test_registrar_chamada_sucesso():
    # mock da sessão do banco
    db = MagicMock(spec=Session)

    user_id = 1
    prompt = "Gere uma receita x"
    resposta = "resposta simulada"

    # mock do promptParser
    with patch("funcoes.registrar_chamada.promptParser") as mock_parser:
        mock_parser.return_value = "Receita simulada"

        nova_receita = registrarChamada(
            db=db,
            user_id=user_id,
            prompt=prompt,
            resposta=resposta
        )

    # Verificações
    db.add.assert_called_once()
    db.commit.assert_called_once()
    db.refresh.assert_called_once()

    assert isinstance(nova_receita, ReceitaDB)
    assert nova_receita.user_id == user_id
    assert nova_receita.prompt == prompt
    assert nova_receita.resposta == "Receita simulada"


def test_prompt_parser_sem_text():
    class Resposta:
        pass

    resposta = Resposta()

    resultado = promptParser(resposta)

    assert resultado == "Não foi possível obter resposta do modelo."
