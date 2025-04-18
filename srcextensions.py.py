from typing import Optional
from redis import Redis, ConnectionPool
from .config import RedisConfig

class RedisManager:
    def __init__(self):
        self._pool: Optional[ConnectionPool] = None

    def init_app(self, app):
        config = RedisConfig()
        self._pool = ConnectionPool(
            host=config.host,
            port=config.port,
            db=config.db,
            username=config.username,
            password=config.password,
            ssl=config.use_ssl,
            max_connections=config.max_connections,
            decode_responses=True,
            socket_connect_timeout=3
        )

    def get_client(self) -> Redis:
        if not self._pool:
            raise RuntimeError("Redis not initialized")
        return Redis(connection_pool=self._pool)

    def close(self):
        if self._pool:
            self._pool.disconnect()

redis_manager = RedisManager()