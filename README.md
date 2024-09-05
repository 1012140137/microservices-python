# Microservices development framework for python
A rapid development framework for exporting python code as microservices, supporting distributed asynchronous task queues

## Python version requirements
Python ❨3.8, 3.9, 3.10, 3.11❩

## Basic architecture 
![](./docs/architecture-diagram.jpg)

## License check for major components

| Component       | Description                  | License      |
| --------------- | ---------------------------- | ------------ |
| Celery          | Celery is a simple, flexible, and reliable distributed system to process vast amounts of messages, while providing operations with the tools required to maintain such a system.    | BSD License  |
| Gunicorn        | Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX.                                            | MIT License  |
| Uvicorn         | Uvicorn is an ASGI web server implementation for Python.                                          | BSD-3-Clause license |
| Nginx           | nginx [engine x] is an HTTP and reverse proxy server.                                          | BSD-2-Clause license |


> Conclusion: No any payment is required for commercial apps

## How to start the development environment
``` bash shell
$ mkdir -p runtime/logs

# Prepare the basic python environment
$ virtualenv -p python3 python3_env
$ source python3_env/bin/activate
$ pip install -r ./requirements.txt

# Execute the following command lines in separate shell Windows
$ make dev-up
$ make flower-up
$ make worker1-run
$ make uvicorn-run
```
Open Swagger Documention

http://localhost:8080/swagger, the default access_token is "token1-xx"

## How to start the prod environment
(1) Enable https support (**Optional**)
 - Edit the `docker/images/nginx/etc/nginx/conf.d/ssl.conf` file, replace with your ssl certificate
 - Rename for replace the `docker/images/nginx/etc/nginx/conf.d/default.conf` with `docker/images/nginx/etc/nginx/conf.d/default.conf.bak`

(2) Build your images, and startup the product environment
``` bash shell
$ mkdir -p runtime/logs

$ docker/images/build_images.sh
$ make prod-up
```

(3) Run the celery worker in anywhere, able to access rabbitmq and mongodb services on your private network is required
``` bash shell
$ mkdir -p runtime/logs

# Prepare the basic python environment
$ virtualenv -p python3 python3_env
$ source python3_env/bin/activate
$ pip install -r ./requirements.txt

# Set environment vars, and run celery worker
$ export RABBITMQ_HOST=localhost &&\
  export RABBITMQ_USER=admin  &&\
  export RABBITMQ_PASSWORD=secret  &&\
  export MONGODB_HOST=localhost  &&\
  export MONGODB_USER=admin  &&\
  export MONGODB_PASSWORD=secret  &&\
  make worker1-run
```
（4）Open Swagger Documention
> https://your_domain_name/uvicorn/swagger, the default access_token is "token1-xx"

