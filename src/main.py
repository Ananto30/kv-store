import os

from flask import Flask, jsonify, request
from flask.helpers import make_response, send_from_directory
from flask_cors import CORS
from redis import StrictRedis

from src.codegen import CodeGen
from src.kvstore import KVStore

redis_host = os.environ.get("REDIS_HOST", "localhost")
redis_port = os.environ.get("REDIS_PORT", 6379)
redis_db = os.environ.get("REDIS_DB", 0)
redis = StrictRedis(host=redis_host, port=redis_port, db=redis_db)

kv_store = KVStore(redis)
codegen = CodeGen(kv_store)

app = Flask(__name__, static_folder="../web-app/public", static_url_path="/")

cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/api/services", methods=["GET"])
def api_get_services():
    services = kv_store.get_services()
    response = []
    for service in services:
        response.append(
            {
                "service_name": service,
                "key_count": kv_store.count_service_keys(service),
            }
        )

    return jsonify(response)


@app.route("/api/services", methods=["POST"])
def api_add_service():
    data = request.get_json()
    kv_store.add_service(data.get("service_name"))
    response = {"status": "success"}
    return jsonify(response)


@app.route("/api/services/<service_name>", methods=["DELETE"])
def api_delete_service(service_name):
    count = kv_store.count_service_keys(service_name)
    if count > 0:
        response = {"status": "error", "message": "Cannot delete service because it has key values inside."}
        return jsonify(response), 500
    response = {"status": "success"}
    kv_store.delete_service(service_name)
    return jsonify(response)


@app.route("/api/services/<service_name>", methods=["GET"])
def api_get_service(service_name):
    kvs = kv_store.get_service_kvs(service_name)
    response = {"key_values": kvs}
    return jsonify(response)


@app.route("/api/services/<service_name>/kv", methods=["POST"])
def api_add_service_kv(service_name):
    data = request.get_json()
    key = data.get("key")
    val = data.get("val")
    kv_store.add_service_kv(service_name, key, val)
    response = {"status": "success"}
    return jsonify(response)


@app.route("/api/services/<service_name>/kv/<key>", methods=["DELETE"])
def api_delete_service_kv(service_name, key):
    kv_store.delete_service_kv(service_name, key)
    response = {"status": "success"}
    return jsonify(response)


@app.route("/api/services/<service_name>/generate_code/<language>", methods=["GET"])
def api_generate_code_for_service(service_name, language):
    if language == "java":
        code = codegen.generate_java_code(service_name)
    else:
        language = "python"
        code = codegen.generate_python_code(service_name)

    response = make_response(code)
    response.headers["content-type"] = "text/plain"

    return response


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    return send_from_directory(app.static_folder, "index.html")
