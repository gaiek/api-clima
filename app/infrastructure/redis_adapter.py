from app.ports.cache_port import CachePort

class RedisAdapter(CachePort):
    def __init__(self, redis_client):
        self.redis_client = redis_client

    def get(self, key: str) -> str | None:
        value = self.redis_client.get(key)
        return value.decode('utf-8') if value else None

    def set(self, key: str, value: str, expire: int) -> None:
        self.redis_client.setex(key, expire, value)