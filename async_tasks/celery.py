from celery import Celery

app = Celery('async_tasks')
# read the celery configuration from the config.py file
app.config_from_object('celery_config')

if __name__ == '__main__':
    app.start()