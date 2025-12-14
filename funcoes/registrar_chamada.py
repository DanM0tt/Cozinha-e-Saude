from sqlalchemy.orm import Session
from classes.banco_de_dados import ReceitaDB
from funcoes.prompt_parser import promptParser

def registrarChamada(
    db: Session,
    user_id: int,
    prompt: str,
    resposta
):
    receita_texto = promptParser(resposta)

    nova_receita = ReceitaDB(
        user_id=user_id,
        prompt=prompt,
        resposta=receita_texto
    )

    db.add(nova_receita)
    db.commit()
    db.refresh(nova_receita)

    return nova_receita