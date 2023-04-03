SHELL := /bin/bash
init:
		python3 -m venv venv
		source venv/bin/activate && ( \
		pip install -r requirements.txt; \
		)

dev:
		source venv/bin/activate && ( \
		export FLASK_APP=src.main; \
		export FLASK_ENV=development; \
		flask run & \
		cd web; \
		npm run dev; \
		)
	
docker-build:
		docker build -t ananto30/kv-store .

docker-run:
		docker run -d -p 8080:8080 ananto30/kv-store
