from funcoes.banco_de_dados import get_db
from sqlalchemy.orm import Session

def test_get_db_returns_session():
    gen = get_db()
    db = next(gen)

    assert isinstance(db, Session)

    # encerra o generator para disparar o finally (db.close)
    try:
        next(gen)
    except StopIteration:
        pass
