# ==========================================================
# PROJETO FACULDADE IMPACTA - GESTÃO DE PET SHOP
# Aluno: Dinho
# Matéria: Desenvolvimento Full Stack
# ==========================================================

from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from fastapi.middleware.cors import CORSMiddleware

# 1. PARTE DO BANCO DE DADOS (Onde a gente salva os pets)
SQLALCHEMY_DATABASE_URL = "postgresql://neondb_owner:npg_Pe5wqHg6tVrj@ep-round-sky-acowv5bz-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require"

# Aqui a gente liga o motor (engine) e prepara a sessão pra conseguir mexer no banco
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Aqui eu defini o que o pet precisa ter: nome, espécie e o nome do dono.
class Pet(Base):
    __tablename__ = "pets"
    id = Column(Integer, primary_key=True, index=True) # O ID é o número de registro dele
    nome = Column(String)
    especie = Column(String)
    dono = Column(String)

# Esse comando aqui é importante: ele olha o que eu escrevi acima e cria as
# tabelas lá no Supabase automaticamente pra gente não ter erro de conexão.
Base.metadata.create_all(bind=engine)

# 2. PARTE DA API (O cérebro que faz o site conversar com o banco)
app = FastAPI()

# Isso aqui é pra segurança! Permite que o nosso index.html consiga
# mandar e receber dados desse código Python aqui.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# FUNÇÃO PARA CADASTRAR: Pega o que o usuário digitou e joga na "sacola" (db.add)
@app.post("/pets/")
def cadastrar_pet(nome: str, especie: str, dono: str):
    db = SessionLocal() # Abre a conexão
    try:
        novo_pet = Pet(nome=nome, especie=especie, dono=dono)
        db.add(novo_pet) # Adiciona
        db.commit()      # Salva de verdade na nuvem
        db.refresh(novo_pet)
        return {"status": "sucesso", "mensagem": f"{nome} cadastrado!"}
    except Exception as e:
        return {"status": "erro", "mensagem": str(e)}
    finally:
        db.close() # Sempre fecha pra não gastar memória

# FUNÇÃO PARA LISTAR: Busca todo mundo que está salvo (db.query)
@app.get("/pets/")
def listar_pets():
    db = SessionLocal()
    try:
        pets = db.query(Pet).all() # Pega a lista completa do Blunt e da turma
        return pets
    finally:
        db.close()

# FUNÇÃO PARA EXCLUIR: Procura o ID e deleta o pet do banco
@app.delete("/pets/{pet_id}")
def excluir_pet(pet_id: int):
    db = SessionLocal()
    try:
        pet = db.query(Pet).filter(Pet.id == pet_id).first()
        if pet:
            db.delete(pet) # Apaga
            db.commit()    # Salva a alteração
            return {"status": "sucesso"}
        return {"status": "erro", "mensagem": "Pet não encontrado"}
    finally:
        db.close()

# FUNÇÃO PARA EDITAR: Localiza o pet e troca as informações dele
@app.put("/pets/{pet_id}")
def editar_pet(pet_id: int, nome: str, especie: str, dono: str):
    db = SessionLocal()
    try:
        # Primeiro acha o pet pelo número do ID dele
        pet = db.query(Pet).filter(Pet.id == pet_id).first()
        if pet:
            pet.nome = nome
            pet.especie = especie
            pet.dono = dono
            db.commit() # Salva a edição
            return {"status": "sucesso", "mensagem": "Dados atualizados!"}
        return {"status": "erro", "mensagem": "Pet não encontrado"}
    finally:
        db.close()