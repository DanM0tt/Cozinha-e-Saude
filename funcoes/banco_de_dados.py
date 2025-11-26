from classes.banco_de_dados import engine, SessionLocal, Base

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

