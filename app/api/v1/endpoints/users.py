from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import User, UserCreate
from app.services import user_service
from app.db import session

router = APIRouter()

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user_endpoint(user: UserCreate, db: Session = Depends(session.get_db)):
    db_user = user_service.get_user_by_login(db, login=user.login)
    if db_user:
        raise HTTPException(status_code=400, detail="Login já cadastrado")
    return user_service.create_user(db=db, user=user)

# Aqui também poderia entrar o endpoint para obter o perfil do usuário logado