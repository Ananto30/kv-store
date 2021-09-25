from src.kvstore import KVStore


class CodeGen:
    def __init__(self, kv_store: KVStore):
        self.kv_store = kv_store

    def generate_python_code(self, service_name: str) -> str:
        code = f"""
from redis import StrictRedis

redis = StrictRedis(host="localhost", port=6379, db=0)


class RedisKVStore{service_name.title()}:
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

    def camel(self, s: str) -> str:
        return s.title().replace("_", "").replace("-", "").replace(".", "").replace(" ", "")

    def generate_java_code(self, service_name: str) -> str:
        service_name_camel = self.camel(service_name)
        code = f"""
import redis.clients.jedis.Jedis;

public class RedisKVStore{service_name_camel} {{
    Jedis redis;

    public RedisKVStore{service_name_camel}(Jedis redis) {{
        this.redis = redis;
    }}

    public String get(String key) {{
        return redis.get(key);
    }}
"""

        keys = self.kv_store.get_service_keys_full(service_name)
        for key in keys:
            key_name = key.replace(f"{self.kv_store.prefix}{service_name}__", "")
            key_name_camel = self.camel(key_name)
            code += f"""
    public String get{key_name_camel}() {{
        return this.get("{key}");
    }}
"""
        code += "}"
        return code
