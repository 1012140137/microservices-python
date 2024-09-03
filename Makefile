dev-up:
	docker-compose -f docker-compose-dev.yml --env-file ./dev.env up

worker1-run:
	celery -A async_tasks worker --loglevel=INFO -Q celery,email-queue -n worker1@%h --logfile="./runtime/logs/worker1.log"

flower-up:
	celery -A async_tasks flower --conf="./flower_config.py"

uvicorn-run:
	cd ./web && uvicorn main:app --port 8080  --reload
