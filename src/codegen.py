from src.kvstore import KVStore


class CodeGen:
    def __init__(self, kv_store: KVStore):
        self.kv_store = kv_store

    def generate_python_code(self, service_name: str) -> str:
        code = """
from redis import StrictRedis

redis = StrictRedis(host="localhost", port=6379, db=0)


class RedisKVStore:
    def __init__(self, redis):
        self.redis = redis
    
    def get(self, key) -> str:
        return self.redis.get(key).decode()
    """

        keys = self.kv_store.get_service_keys_full(service_name)
        for key in keys:
            key_name = key.replace(f"{self.kv_store.prefix}{service_name}__", "")
            code += f"""
    @property
    def {key_name}(self) -> str:
        return self.get("{key}")
        """

        return code
