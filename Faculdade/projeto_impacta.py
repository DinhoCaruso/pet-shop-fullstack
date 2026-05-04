# ==========================================================
# PROJETO FACULDADE IMPACTA - GESTÃO DE PET SHOP
# Aluno: Dinho
# Matéria: Desenvolvimento Full Stack
# Funcionalidade: Agendamento de Tosa (Manifesto Ágil)
# ==========================================================

from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

# 1. PARTE DO BANCO DE DADOS (Onde a gente salva os pets)
SQLALCHEMY_DATABASE_URL = "postgresql://neondb_owner:npg_Pe5wqHg6tVrj@ep-round-sky-acowv5bz-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Ajuste: data_tosa agora permite valores vazios (nullable=True)
class Pet(Base):
    __tablename__ = "pets"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    especie = Column(String)
    dono = Column(String)
    data_tosa = Column(String, nullable=True)

Base.metadata.create_all(bind=engine)

# 2. PARTE DA API
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ajuste: data_tosa agora é opcional (Optional[str] = None)
@app.post("/pets/")
def cadastrar_pet(nome: str, especie: str, dono: str, data_tosa: Optional[str] = None):
    db = SessionLocal()
    try:
        novo_pet = Pet(nome=nome, especie=especie, dono=dono, data_tosa=data_tosa)
        db.add(novo_pet)
        db.commit()
        db.refresh(novo_pet)
        msg = f"{nome} cadastrado!" if not data_tosa else f"{nome} cadastrado com tosa para {data_tosa}!"
        return {"status": "sucesso", "mensagem": msg}
    except Exception as e:
        return {"status": "erro", "mensagem": str(e)}
    finally:
        db.close()

@app.get("/pets/")
def listar_pets():
    db = SessionLocal()
    try:
        pets = db.query(Pet).all()
        return pets
    finally:
        db.close()

@app.get("/pets/search/{nome_busca}")
def buscar_pet(nome_busca: str):
    db = SessionLocal()
    try:
        termo = f"%{nome_busca}%"
        pets = db.query(Pet).filter(Pet.nome.ilike(termo)).all()
        return pets
    finally:
        db.close()

@app.delete("/pets/{pet_id}")
def excluir_pet(pet_id: int):
    db = SessionLocal()
    try:
        pet = db.query(Pet).filter(Pet.id == pet_id).first()
        if pet:
            db.delete(pet)
            db.commit()
            return {"status": "sucesso"}
        return {"status": "erro", "mensagem": "Pet não encontrado"}
    finally:
        db.close()

# Ajuste: data_tosa agora é opcional na edição também
@app.put("/pets/{pet_id}")
def editar_pet(pet_id: int, nome: str, especie: str, dono: str, data_tosa: Optional[str] = None):
    db = SessionLocal()
    try:
        pet = db.query(Pet).filter(Pet.id == pet_id).first()
        if pet:
            pet.nome = nome
            pet.especie = especie
            pet.dono = dono
            pet.data_tosa = data_tosa
            db.commit()
            return {"status": "sucesso", "mensagem": "Dados atualizados!"}
        return {"status": "erro", "mensagem": "Pet não encontrado"}
    finally:
        db.close()