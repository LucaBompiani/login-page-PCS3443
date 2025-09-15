from fastapi import APIRouter

# Importa os módulos que contêm os roteadores específicos
from .endpoints import auth, users

# Cria uma instância do APIRouter que irá agrupar todas as rotas da versão v1 da API
api_router = APIRouter()

# Inclui os roteadores no agregador principal.
# Cada um pode ter um prefixo e tags para melhor organização na documentação.
api_router.include_router(auth.router, prefix="/auth", tags=["Autenticação"])
api_router.include_router(users.router, prefix="/users", tags=["Usuários"])

# Se no futuro você criasse endpoints para "produtos", por exemplo, bastaria adicionar:
# from .endpoints import products
# api_router.include_router(products.router, prefix="/products", tags=["Produtos"])