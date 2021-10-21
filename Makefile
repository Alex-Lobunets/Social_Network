up:
	docker-compose up -d

down:
	docker-compose down

build:
	docker-compose build

sh:
	docker-compose run --rm backend bash

psql:
	docker-compose run --rm postgresql psql -h 172.17.0.1 -p 5432 blog blog

migrate:
	docker-compose run --rm backend src/manage.py migrate

migrations:
	docker-compose run --rm backend src/manage.py makemigrations

flush:
	docker-compose run --rm backend src/manage.py flush

user:
	docker-compose run --rm backend src/manage.py createsuperuser

server:
	docker-compose run --rm --service-ports backend src/manage.py runserver 0.0.0.0:8000
