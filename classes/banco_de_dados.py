from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text, Date, ForeignKey, Text
from dotenv import load_dotenv

import os 
load_dotenv()
DB_URL = os.getenv("DB_URL")
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class UsuarioDB(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    senha = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    birthday = Column(Date)
    gender = Column(String)


class ReceitaDB(Base):
    __tablename__ = "receitas"

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)

    prompt = Column(Text, nullable=False)
    resposta = Column(Text, nullable=False)

    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=text("now()")
    )

    usuario = relationship("UsuarioDB")