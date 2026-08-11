import httpx

from app.config import settings


def get_client() -> httpx.AsyncClient:
    return httpx.AsyncClient(base_url=settings.backend_url, timeout=10.0)
