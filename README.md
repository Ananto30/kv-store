<h1 align="center">
    KV Store 🗄️
</h1>
<p align="center">
    <a href="https://hub.docker.com/r/ananto30/kv-store" target="_blank">
        <img src="https://img.shields.io/docker/image-size/ananto30/kv-store?logo=docker" />
    </a>
    <a href="https://depfu.com/github/Ananto30/kv-store?project_id=38289">
        <img src="https://badges.depfu.com/badges/82614c2f1a13921b01dd4d70ec00643e/overview.svg" alt="Depfu" />
    </a>
    <a href="https://app.codacy.com/gh/Ananto30/kv-store/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade">
        <img src="https://app.codacy.com/project/badge/Grade/f5d0450ea44f4208829289d33c92983a"/>
    </a>
</p>
<p align="center">
    Web app to manage Redis key-values (config/settings related).
    <br>
    Manages your frequently changed configs without any deployment.
    <br>
    Generates Python & Java code too!
</p>

<br>
<br>

The purpose of <strong>KV Store</strong> is to provide a simple way to store
the <strong>settings or configs</strong> of your microservice applications.
As an example, you may have a settings that is frequently changed for
business requirements, say <code>session\_timeout</code> which can be 5 or 500
minutes. You can save it to <strong>KV Store</strong> and change it as
necessary.

KV Store also <strong>generates client code</strong> for you!<i>(Supports <strong>Python & Java</strong> for now)</i>

<img src="https://res.cloudinary.com/dvqpo7nkm/image/upload/v1632813083/projects/kv_store_gif.gif">

## Run just now 🚀

### Docker 🚢

Standalone docker image of KV Store is available [here](https://hub.docker.com/repository/docker/ananto30/kv-store)

*   Get the image and run -

```bash
docker pull ananto30/kv-store
docker run -d -p 8080:8080 ananto30/kv-store
```

### Repo 📁

*   Clone the repo -

```bash
git clone https://github.com/Ananto30/kv-store.git
cd kv-store
```

*   Build and run in docker -

```bash
make docker-build
make docker-run
```

<i>Please note that if you are running redis locally (with or without docker), the `Redis Host` in connect page should be you machine IP </i>(mostly 😅)

## Development 🧑‍💻

<i>Make sure you have Python 3.9 installed.</i>

*   If you want to dev only
    ```bash
    make init
    make dev-server
    # in another window/shell
    make dev-web
    ```

*   If you want to check the app
    ```bash
    make init
    make build-web
    make dev-server
    ```

Then go to http://localhost:5000

*Note that the svelte port won't load api because it's different than 5000, so go to 5000 as the flask is there, serving svelte*

#### Please give a star ⭐ if you like it

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/ananto30)
