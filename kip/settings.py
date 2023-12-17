from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    secret_key: str

    postgres_user: str 
    postgres_password: str 
    postgres_host: str
    postgres_port: int
    postgres_db: str
    
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
