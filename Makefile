# Makefile

# Run all tests
test:
	docker-compose exec api pytest -v -s

# Run only integration tests
test-integration:
	docker-compose exec api pytest -v tests/integration

# Run only unit tests
test-unit:
	docker-compose exec api pytest -v tests/unit
