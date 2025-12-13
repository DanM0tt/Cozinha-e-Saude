from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from funcoes.hashing_algorithm import get_password_hash, verify_password_hash
from funcoes.banco_de_dados import get_db
from funcoes.registrar_chamada import registrarChamada
from funcoes.prompt_parser import promptParser

from classes.usuario import UserLogin, UserCreate
from classes.banco_de_dados import UsuarioDB, ReceitaDB
from classes.receita import Receita
from datetime import date
api_router = APIRouter(prefix='/api')

@api_router.post('/sessao')
async def logarUsuario(usuario: UserLogin, db: Session = Depends(get_db)):
    print(usuario.email)
    query = db.query(UsuarioDB).filter_by(email=usuario.email).first()
    # comparando a senha digitada pelo usuario com a senha com hash
    if not verify_password_hash(usuario.senha, query.senha):
        raise HTTPException(status_code=404, detail="usuário não encontrado xd")
    
    return {
        "nome_usuario": query.username,
        "user_id": query.id
    }

@api_router.post('/usuarios')
async def cadastrarUsuario(usuario: UserCreate, db: Session = Depends(get_db)):
    senha_hash = get_password_hash(usuario.senha)
    
    instancia_usuario = UsuarioDB(
        username=usuario.username,
        email=usuario.email,
        senha=senha_hash,
        birthday=usuario.birthday,
        gender=usuario.gender    
    )

    db.add(instancia_usuario)
    db.commit()
    db.refresh(instancia_usuario)
    
@api_router.post("/receita")
async def promptDaReceita(
    receita: Receita,
    db: Session = Depends(get_db)
):
    resposta, prompt = receita.gerar()

    receita_db = registrarChamada(
        db=db,
        user_id=receita.user_id,  # 👈 vem do frontend
        prompt=prompt,
        resposta=resposta
    )

    return {
        "id": receita_db.id,
        "resposta": receita_db.resposta
    }

@api_router.get("/receitas/ultimas/{user_id}")
async def ultimas_receitas(
    user_id: int,
    db: Session = Depends(get_db)
):
    receitas = (
        db.query(ReceitaDB)
        .filter(ReceitaDB.user_id == user_id)
        .order_by(ReceitaDB.created_at.desc())
        .limit(3)
        .all()
    )

    return [
        {
            "id": r.id,
            "prompt": r.prompt,
            "resposta": r.resposta,
            "created_at": r.created_at
        }
        for r in receitas
    ]