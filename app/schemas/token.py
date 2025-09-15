from pydantic import BaseModel

# Esquema para a resposta do token de login
class Token(BaseModel):
    access_token: str
    token_type: str

# Esquema para os dados contidos dentro do token JWT
class TokenData(BaseModel):
    login: str | None = None