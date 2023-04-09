SHELL := /bin/bash
init:
		python3 -m venv venv
		source venv/bin/activate && ( \
		pip install -r requirements.txt; \
		)

dev-server:
		source venv/bin/activate && ( \
		export FLASK_APP=src.main; \
		flask --debug run; \
		)

dev-web:
		cd web; \
		npm install; \
		npm run dev

build-web:
		cd web; \
		npm install; \
		npm run build
	
docker-build:
		docker build -t ananto30/kv-store .

docker-run:
		docker run -d -p 8080:8080 ananto30/kv-store
	