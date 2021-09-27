from typing import Dict, List


class KVStore:
    def __init__(self, redis):
        self.redis = redis
        self.prefix = "kv_"
        self.services_key = self.prefix + "services"

    def get_services(self) -> List[str]:
        services = self.redis.smembers(self.services_key)
        return [service.decode() for service in services]

    def add_service(self, service_name: str):
        self.redis.sadd(self.services_key, service_name)

    def delete_service(self, service_name: str):
        self.redis.srem("kv_services", service_name)

    def get_service_kvs(self, service_name: str) -> Dict[str, str]:
        service_key = self.prefix + service_name + "__"
        keys = self.redis.scan_iter(f"{service_key}*")
        kvs = dict()
        for key in keys:
            k = key.decode().replace(service_key, "")
            v = self.redis.get(key).decode()
            kvs[k] = v
        return kvs

    def get_service_keys_full(self, service_name: str) -> List[str]:
        service_key = self.prefix + service_name + "__"
        keys = self.redis.scan_iter(f"{service_key}*")
        return [key.decode() for key in keys]

    def count_service_keys(self, service_name: str) -> List[str]:
        service_key = self.prefix + service_name + "__"
        keys = self.redis.scan_iter(f"{service_key}*")
        return len([key for key in keys])

    def add_service_kv(self, service_name: str, key: str, value: str):
        service_key = self.prefix + service_name + "__"
        self.redis.set(service_key + key, value)

    def delete_service_kv(self, service_name: str, key: str):
        service_key = self.prefix + service_name + "__"
        self.redis.delete(service_key + key)
