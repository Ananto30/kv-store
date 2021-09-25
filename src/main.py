import os

from flask import Flask, redirect, render_template, request, url_for
from redis import StrictRedis

from src.codegen import CodeGen
from src.kvstore import KVStore

redis_host = os.environ.get("REDIS_HOST", "localhost")
redis_port = os.environ.get("REDIS_PORT", 6379)
redis_db = os.environ.get("REDIS_DB", 0)
redis = StrictRedis(host=redis_host, port=redis_port, db=redis_db)

kv_store = KVStore(redis)
codegen = CodeGen(kv_store)

app = Flask(__name__)


@app.route("/")
def index():
    services = kv_store.get_services()
    service_map = dict()
    for service in services:
        service_map[service] = kv_store.count_service_keys(service)
    error = request.args["error"] if "error" in request.args else None
    return render_template("index.html", service_map=service_map, error=error)


@app.route("/service", methods=["POST"])
def add_service():
    service = request.form["service_name"]
    if service == "":
        return redirect("/")
    kv_store.add_service(service)
    return redirect("/")


@app.route("/service/<service_name>", methods=["GET"])
def get_service(service_name):
    kvs = kv_store.get_service_kvs(service_name)
    return render_template("service.html", kvs=kvs, service_name=service_name)


@app.route("/service/<service_name>/delete", methods=["POST"])
def delete_service(service_name):
    count = kv_store.count_service_keys(service_name)
    if count > 0:
        return redirect(
            url_for(
                "index",
                error=f"Cannot delete service `{service_name}` because it has key values inside.",
            )
        )
    redis.srem("kv_services", service_name)
    return redirect("/")


@app.route("/service/<service_name>/kv", methods=["POST"])
def add_service_kv(service_name):
    key = request.form["key"]
    val = request.form["val"]
    kv_store.add_service_kv(service_name, key, val)
    return redirect(f"/service/{service_name}")


@app.route("/service/<service_name>/kv/<key>/delete", methods=["POST"])
def delete_service_kv(service_name, key):
    kv_store.delete_service_kv(service_name, key)
    return redirect(f"/service/{service_name}")


@app.route("/service/<service_name>/generate_code/python", methods=["GET"])
def generate_python_code_for_service(service_name):
    code = codegen.generate_python_code(service_name)
    return render_template("python.html", code=code, service_name=service_name)
