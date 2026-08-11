from fastapi import APIRouter, HTTPException

from app import schemas
from app.backend_client import get_client

router = APIRouter(prefix="/users", tags=["users"])


@router.get("", response_model=list[schemas.UserOut])
async def list_users(skip: int = 0, limit: int = 100):
    async with get_client() as client:
        resp = await client.get("/users", params={"skip": skip, "limit": limit})
    if resp.status_code >= 400:
        raise HTTPException(status_code=resp.status_code, detail=resp.text)
    return resp.json()


@router.get("/{user_id}", response_model=schemas.UserOut)
async def get_user(user_id: int):
    async with get_client() as client:
        resp = await client.get(f"/users/{user_id}")
    if resp.status_code >= 400:
        raise HTTPException(status_code=resp.status_code, detail=resp.text)
    return resp.json()


@router.post("", response_model=schemas.UserOut, status_code=201)
async def create_user(user: schemas.UserCreate):
    async with get_client() as client:
        resp = await client.post("/users", json=user.model_dump())
    if resp.status_code >= 400:
        raise HTTPException(status_code=resp.status_code, detail=resp.text)
    return resp.json()


@router.put("/{user_id}", response_model=schemas.UserOut)
async def update_user(user_id: int, user: schemas.UserUpdate):
    async with get_client() as client:
        resp = await client.put(f"/users/{user_id}", json=user.model_dump())
    if resp.status_code >= 400:
        raise HTTPException(status_code=resp.status_code, detail=resp.text)
    return resp.json()


@router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: int):
    async with get_client() as client:
        resp = await client.delete(f"/users/{user_id}")
    if resp.status_code >= 400:
        raise HTTPException(status_code=resp.status_code, detail=resp.text)
