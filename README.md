<h1 align="center">
    KV Store 🗄️
</h1>
<p align="center">
    <a href="https://hub.docker.com/repository/docker/ananto30/kv-store" target="_blank">
        <img src="https://img.shields.io/docker/image-size/ananto30/kv-store?logo=docker" />
    </a>
</p>
<h4 align="center">
    Config or Settings key-val store in Redis with GUI.
    <br>
    Manages your frequently changed env vars without any deployment.
    <br>
    Generates Python & Java code too!
</h4>

<br>
<br>

The purpose of <strong>KV Store</strong> is to provide a simple way to store
the <strong>settings or configs</strong> of your microservice applications.
As an example, you may have a settings that is frequently changed for
business requirements, say <code>session_timeout</code> which can be 5 or 500
minutes. You can save it to <strong>KV Store</strong> and change it as
necessary.

KV Store also <strong>generates client code</strong> for you!<i>(Supports <strong>Python & Java</strong> for now)</i>

<img src="https://res.cloudinary.com/dvqpo7nkm/image/upload/v1632573669/projects/kvstore_gif.gif">

## Run just now 🚀

- Clone the repo -
```
git clone https://github.com/Ananto30/kv-store.git
cd kv-store
```

<strong>Fix the `.env` file.</strong>

<i>Please note that if you are running redis locally (with or without docker), the `REDIS_HOST` in `.env` should be you machine IP </i>(mostly 😅)

- Build and run in docker -
```
make docker-build
make docker-run
```

## Docker 🚢
Standalone docker image of KV Store is available [here](https://hub.docker.com/repository/docker/ananto30/kv-store)

- Get the image -
```
docker pull ananto30/kv-store
```
- Make an `.env` file in the same directory and paste these -
```
REDIS_HOST=<YourRedisHost_Or_MachineIP>
REDIS_PORT=6379
REDIS_DB=0
```
- Run the image
```
docker run -d -p 8080:8080 --env-file .env ananto30/kv-store
```

## Development 🧑‍💻

<strong>Fix the `.env` file.</strong>

<i>Make sure you have Python 3.9 installed.</i>

```
make init
make dev
```

### Please give a star ⭐ if you like it
