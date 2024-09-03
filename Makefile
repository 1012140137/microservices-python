dev-up:
	docker-compose -f docker-compose-dev.yml --env-file ./dev.env up

flower-up:
	celery -A tasks flower --conf="./flower_config.py"
