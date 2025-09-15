from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse
import os

# Importa o agregador de rotas da sua API
from .api.v1.api import api_router

# Importa os objetos para criação das tabelas no banco de dados
from .db.base import Base
from .db.session import engine

def create_tables():
    """Cria as tabelas no banco de dados se elas ainda não existirem."""
    Base.metadata.create_all(bind=engine)

# Chama a função para garantir que as tabelas sejam criadas ao iniciar a aplicação
create_tables()

# Cria a instância principal da aplicação FastAPI
app = FastAPI(
    title="API do Componente de Login",
    description="Backend para o projeto PCS3443-2021 com autenticação JWT.",
    version="1.0.0"
)

# Configuração do CORS (Cross-Origin Resource Sharing)
# Isso é crucial para permitir que seu frontend se comunique com este backend.
# A configuração abaixo é permissiva (aceita qualquer origem), ideal para desenvolvimento.
# Para produção, restrinja a lista de origens (`origins`).
origins = [
    "https://pcs3443-2021.vercel.app", # Domínio da demo
    "http://localhost",
    "http://localhost:3000", # Origem comum para React em desenvolvimento
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"], # Permite todos os cabeçalhos
)

# Inclui as rotas definidas em app/api/v1/api.py
# Todas as rotas (auth, users) serão prefixadas com /api/v1
app.include_router(api_router, prefix="/api/v1")

# Endpoint raiz para servir a página principal do frontend
@app.get("/", response_class=HTMLResponse, tags=["Frontend"])
def serve_frontend():
    """
    Serve a página principal do frontend (index.html).
    """
    try:
        # Caminho para o arquivo index.html na pasta frontend
        html_path = os.path.join(os.path.dirname(__file__), "..", "frontend", "index.html")
        with open(html_path, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        return HTMLResponse(content="<h1>Frontend não encontrado</h1><p>Arquivo index.html não foi encontrado.</p>", status_code=404)

# Endpoint para servir o arquivo CSS
@app.get("/styles.css", tags=["Frontend"])
def serve_css():
    """
    Serve o arquivo CSS do frontend.
    """
    try:
        css_path = os.path.join(os.path.dirname(__file__), "..", "frontend", "styles.css")
        return FileResponse(css_path, media_type="text/css")
    except FileNotFoundError:
        return {"error": "CSS file not found"}, 404

# Endpoint para servir o arquivo JavaScript
@app.get("/script.js", tags=["Frontend"])
def serve_js():
    """
    Serve o arquivo JavaScript do frontend.
    """
    try:
        js_path = os.path.join(os.path.dirname(__file__), "..", "frontend", "script.js")
        return FileResponse(js_path, media_type="application/javascript")
    except FileNotFoundError:
        return {"error": "JavaScript file not found"}, 404

# Endpoint para health check da API
@app.get("/health", tags=["Root"])
def health_check():
    """
    Endpoint para verificar se a API está online.
    """
    return {"message": "API está funcionando!", "status": "healthy"}