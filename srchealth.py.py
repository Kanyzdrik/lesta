from redis.exceptions import RedisError

def check_redis_health(redis_client) -> bool:
    try:
        return redis_client.ping()
    except RedisError:
        return False