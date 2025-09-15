from pydantic import BaseModel, EmailStr

# Esquema para receber dados de cadastro de um novo usuário
class UserCreate(BaseModel):
    login: str
    email: EmailStr
    password: str

# Esquema para retornar dados de um usuário (sem a senha)
class User(BaseModel):
    id: int
    login: str
    email: EmailStr

    class Config:
        from_attributes = True # Permite que o Pydantic leia dados de um objeto ORM