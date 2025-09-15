from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Chave secreta para assinar os tokens JWT
    SECRET_KEY: str = "uma_chave_secreta_muito_forte"
    ALGORITHM: str = "HS256"
    # Tempo de expiração do token em minutos (conforme a documentação)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    
    # Database configuration
    DATABASE_URL: str = "postgresql://postgres:password@db:5432/atividade1_db"
    
    # PostgreSQL specific settings
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "password"
    POSTGRES_DB: str = "atividade1_db"
    POSTGRES_HOST: str = "db"
    POSTGRES_PORT: int = 5432

    class Config:
        env_file = ".env"

settings = Settings()