# Makefile

test:
	docker-compose exec api pytest -v -s
