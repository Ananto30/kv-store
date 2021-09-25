SHELL := /bin/bash
init:
		python3 -m venv venv
		source venv/bin/activate && ( \
		pip install -r requirements.txt; \
		)
dev:
		docker-compose up -d
		source venv/bin/activate && ( \
		export FLASK_APP=src.main; \
		export FLASK_ENV=development; \
		flask run; \
		)
docker-build:
		docker build -t ananto/kv-store .
docker-run:
		docker run -d -p 8080:8080 --env-file .env ananto/kv-store