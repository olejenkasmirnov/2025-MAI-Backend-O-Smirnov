.PHONY: build run migrate

# Строим контейнеры
build:
	docker-compose build

# Запускаем контейнеры в фоновом режиме
run:
	docker-compose up -d

# Запускаем миграции
migrate: build run
	docker-compose exec -T django python myproject/manage.py migrate
