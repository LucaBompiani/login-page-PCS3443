# app/db/session.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from app.core.config import settings

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém a URL do banco de dados a partir das configurações
DATABASE_URL = settings.DATABASE_URL

# Cria o motor (engine) do SQLAlchemy
# Para PostgreSQL, não precisamos de connect_args especiais
engine = create_engine(DATABASE_URL)

# Cria uma fábrica de sessões que será usada para criar sessões de banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função de dependência para obter uma sessão de banco de dados por requisição
def get_db():
    """
    Cria uma nova sessão SQLAlchemy para uma única requisição,
    garantindo que ela seja sempre fechada após o término.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()