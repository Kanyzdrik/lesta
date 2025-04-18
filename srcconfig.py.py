from pydantic import BaseSettings, Field, validator

class RedisConfig(BaseSettings):
    host: str = Field("localhost", env="REDIS_HOST")
    port: int = Field(6379, env="REDIS_PORT")
    db: int = Field(0, env="REDIS_DB")
    username: Optional[str] = Field(None, env="REDIS_USERNAME")
    password: Optional[str] = Field(None, env="REDIS_PASSWORD")
    use_ssl: bool = Field(False, env="REDIS_USE_SSL")
    max_connections: int = Field(10, env="REDIS_MAX_CONNECTIONS")

    @validator("port")
    def validate_port(cls, port):
        if not 0 <= port <= 65535:
            raise ValueError("Port must be between 0 and 65535")
        return port

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"