IMAGE_NAME=app


.PHONY: build_no_cache
build:  # build the docker image.
	docker-compose build --no-cache

.PHONY: build
build:  # build the docker image.  --no-cache
	docker-compose build

.PHONY: run
run:
	docker-compose up -d postgres
	docker-compose up -d app
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
	DATABASE_URL="postgresql+asyncpg://test-sgi:password@test-postgres:5432/test-sgi" docker-compose up -d app
	# run migrations
	docker-compose exec app sed -i 's|sqlalchemy.url = .*|sqlalchemy.url = postgresql://test-sgi:password@test-postgres:5432/test-sgi|' alembic.ini
	docker-compose exec app alembic upgrade head
	# run tests
	docker-compose exec app poetry run pytest
	make down