IMAGE_NAME=app
DB_TEST="postgresql+asyncpg://test-sgi:password@test-postgres:5432/test-sgi"
DB_DEV="postgresql+asyncpg://sgi:password@postgres:5432/sgi"


.PHONY: build_no_cache
build:  # build the docker image.
	docker-compose build --no-cache

.PHONY: build
build:  # build the docker image.
	docker-compose build

.PHONY: run
run:
	docker-compose up -d postgres
	docker-compose up -d app
	docker-compose exec app alembic upgrade head

.PHONY: run_dev
run_dev:
	docker-compose up -d postgres
	DATABASE_URL=${DB_DEV} ENVIRONMENT="DEV" docker-compose up -d app
	docker-compose exec app alembic upgrade head

.PHONY: down
down:
	docker-compose down

.PHONY: inte_test
inte_test:
	# shut down everything before tests
	make down
	# raises test DB
	docker-compose up -d test-postgres
	# raises app API
	DATABASE_URL=${DB_TEST} ENVIRONMENT="TEST" docker-compose up -d app
	# run migrations
	docker-compose exec app alembic upgrade head
	# run tests
	docker-compose exec app poetry run pytest
	make down