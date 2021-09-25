# KV Store 🗄️

Beautiful UI for managing your key-value store.

The purpose of <strong>KV Store</strong> is to provide a simple way to store
the <strong>settings or configs</strong> of your microservice applications.
As an example, you may have a settings that is frequently changed for
business requirements, say <code>session_timeout</code> which can be 5 or 500
minutes. You can save it to <strong>KV Store</strong> and change it as
necessary.

<strong>KV Store</strong> also generates client code for you!<i>(Only supports Python for now)</i>
    
<img src="https://res.cloudinary.com/dvqpo7nkm/image/upload/v1632554472/projects/ezgif.com-gif-maker.gif">

## Run just now 🚀

<strong>Fix the `.env` file.</strong>

<i>Please note that if you are running redis locally (with or without docker), the `REDIS_HOST` in `.env` should be you machine IP </i>(mostly 😅)

```
make docker-build
make docker-run
```

## Development
<strong>Fix the `.env` file.</strong>

<i>Make sure you have Python 3.9 installed.</i>

```
make init
make dev
```

### Please give a star ⭐ if you like it
