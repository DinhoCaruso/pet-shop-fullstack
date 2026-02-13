from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from fastapi.middleware.cors import CORSMiddleware

# 1. Configuração do Banco de Dados (Camada de Dados)
# O check_same_thread=False é necessário para o SQLite funcionar com FastAPI
SQLALCHEMY_DATABASE_URL = "sqlite:///./petshop.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Definição da Tabela de Pets
class Pet(Base):
    __tablename__ = "pets"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    especie = Column(String)
    dono = Column(String)

# Cria o arquivo de banco de dados e as tabelas
Base.metadata.create_all(bind=engine)

# 2. Lógica da API (Camada de Back-end)
app = FastAPI()

# CONFIGURAÇÃO DE SEGURANÇA (CORS)
# Isso permite que seu index.html fale com este código Python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rota para Cadastrar Novo Pet
@app.post("/pets/")
def cadastrar_pet(nome: str, especie: str, dono: str):
    db = SessionLocal()
    try:
        novo_pet = Pet(nome=nome, especie=especie, dono=dono)
        db.add(novo_pet)
        db.commit()
        db.refresh(novo_pet)
        return {"status": "sucesso", "mensagem": f"{nome} cadastrado!"}
    except Exception as e:
        return {"status": "erro", "mensagem": str(e)}
    finally:
        db.close()

# Rota para Listar todos os Pets
@app.get("/pets/")
def listar_pets():
    db = SessionLocal()
    try:
        pets = db.query(Pet).all()
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

@app.put("/pets/{pet_id}")
def editar_pet(pet_id: int, nome: str, especie: str, dono: str):
    db = SessionLocal()
    try:
        pet = db.query(Pet).filter(Pet.id == pet_id).first()
        if pet:
            pet.nome = nome
            pet.especie = especie
            pet.dono = dono
            db.commit()
            return {"status": "sucesso", "mensagem": "Dados atualizados!"}
        return {"status": "erro", "mensagem": "Pet não encontrado"}
    finally:
        db.close()