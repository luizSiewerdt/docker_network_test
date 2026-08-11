from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database import get_db

router = APIRouter(prefix="/db", tags=["db"])


@router.get("/health")
def db_health(db: Session = Depends(get_db)):
    """Testa a conexão direta com o banco de dados externo."""
    db.execute(text("SELECT 1"))
    return {"status": "ok"}
