FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY requirements.txt /vagrant/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /vagrant/requirements.txt
