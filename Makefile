IMAGE_NAME=app
DB_TEST="postgresql+asyncpg://test-sgi:password@test-postgres:5432/test-sgi"
DB_DEV="postgresql+asyncpg://sgi:password@postgres:5432/sgi"
ALEMBIC_CONFIG="/app/secrets/alembic.ini"

INTEGRATION_TEST_REPORTS_DIR="tests/integration/reports"
UNIT_TEST_REPORTS_DIR="tests/unit/reports"


.PHONY: build_no_cache
build_no_cache:  # build the docker image.
	docker-compose build --no-cache


.PHONY: build
build:  # build the docker image.
	docker-compose build


.PHONY: run
run:
	make down_api
	docker-compose up -d postgres
	until docker-compose exec -T postgres pg_isready -d sgi -U sgi; do sleep 1; done
	DATABASE_URL=${DB_DEV} docker-compose up -d app
	docker-compose exec app alembic -c ${ALEMBIC_CONFIG} upgrade head


.PHONY: down_api
down_api:
	docker-compose down postgres || true
	docker-compose down test-postgres || true
	docker-compose down app || true


.PHONY: down
down:
	docker-compose down


.PHONY: jenkins
jenkins:
	docker-compose up -d my-jenkins jenkins-docker


.PHONY: integration_test
integration_test:
	make down_api
	# raises test DB
	docker-compose up -d test-postgres
	until docker-compose exec -T test-postgres pg_isready -d sgi -U sgi; do sleep 1; done
	docker-compose up -d app
	# raises app API
	DATABASE_URL=${DB_TEST} ENVIRONMENT="TEST" docker-compose up -d app
	# run migrations
	docker-compose exec app alembic -c ${ALEMBIC_CONFIG} upgrade head
	# run tests
	docker-compose exec app poetry run pytest tests/integration --junitxml=${INTEGRATION_TEST_REPORTS_DIR}/report.xml --html=${INTEGRATION_TEST_REPORTS_DIR}/report.html
	make down_api


.PHONY: unit_test
unit_test:
	make down_api
	docker-compose up -d app
	# docker-compose up -d test-postgres
	docker-compose exec app poetry run pytest tests/unit --junitxml=${UNIT_TEST_REPORTS_DIR}/report.xml --html=${UNIT_TEST_REPORTS_DIR}/report.html
	make down_api


.PHONY: linter
linter:
	make down_api
	docker-compose up -d app
	# docker-compose up -d test-postgres
	docker-compose exec app poetry run pre-commit run --all-files
	make down_api
