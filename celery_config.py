import os

# Description: Celery configuration file, https://docs.celeryq.dev/en/stable/userguide/configuration.html#general-settings

# get value from environment variables
mongodb_host = os.getenv('MONGODB_HOST', 'localhost')
mongodb_user = os.getenv('MONGODB_USER', 'admin')
mongodb_password = os.getenv('MONGODB_PASSWORD', 'secret')
rabbitmq_host = os.getenv('RABBITMQ_HOST', 'localhost')
rabbitmq_user = os.getenv('RABBITMQ_USER', 'admin')
rabbitmq_password = os.getenv('RABBITMQ_PASSWORD', 'secret')

# General settings
accept_content = ['json']
result_accept_content = ['application/json']

# Time and date settings
timezone = 'UTC'
enable_utc = True

# Task settings
task_serializer = 'json'

# Task execution settings
task_time_limit = 300

# Task result backend settings
result_backend = 'mongodb'
result_serializer = 'json'

# Database backend settings for mongodb
mongodb_backend_settings = {
    'host': mongodb_host,
    'port': 27017,
    'user': mongodb_user,
    'password': mongodb_password,
    'database': 'celery_backend',
    'taskmeta_collection': 'taskmeta',
}

# Broker Settings for rabbitmq
broker_url = 'amqp://%s:%s@%s:5672//' % (rabbitmq_user, rabbitmq_password, rabbitmq_host)
broker_connection_retry_on_startup = True
broker_connection_max_retries = 3


# Worker
include = ['async_tasks.email']

# task routing settings
task_routes = {
    'async_tasks.email.send_email': {'queue': 'email-queue'}
}

