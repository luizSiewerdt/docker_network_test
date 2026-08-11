from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import db, users

app = FastAPI(title="Proxy API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Encaminha as chamadas de CRUD de usuários para o backend externo.
app.include_router(users.router)
# Endpoints que acessam o banco de dados externo diretamente.
app.include_router(db.router)


@app.get("/health")
def health():
    return {"status": "ok"}
