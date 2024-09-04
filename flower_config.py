import os

# get value from environment variables
rabbitmq_host = os.getenv('RABBITMQ_HOST', 'localhost')
rabbitmq_user = os.getenv('RABBITMQ_USER', 'admin')
rabbitmq_password = os.getenv('RABBITMQ_PASSWORD', 'secret')
bower_http_port = os.getenv('BROWER_HTTP_PORT', '8081')
brower_user = os.getenv('BROWER_USER', 'admin')
brower_password = os.getenv('BROWER_PASSWORD', 'secret')

# Set RabbitMQ management api
broker_api = 'http://%s:%s@%s:15672/api/' % (rabbitmq_user, rabbitmq_password, rabbitmq_host)

# set port for flower web server
port = bower_http_port

# Enable debug logging
logging = 'DEBUG'

# basic auth
basic_auth = ['%s:%s' % (brower_user, brower_password)]
