from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Preencha com a URL do backend real quando ele existir.
    backend_url: str = "http://CHANGE_ME:8000"
    # Preencha com a URL do banco de dados externo quando ele existir.
    database_url: str = "postgresql://user:password@CHANGE_ME:5432/dbname"

    class Config:
        env_file = ".env"


settings = Settings()
