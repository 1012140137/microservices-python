#!/bin/bash

current_dir=$(pwd)
echo "current_dir: $current_dir"

# prepare the requirements.txt file
source python3_env/bin/activate
pip freeze > ./requirements.txt

# build the python image
cd $current_dir && cd ./docker/images/python
cp ../../../requirements.txt ./requirements.txt
docker build -t msp/python:latest .

# build the uvicorn image
cd $current_dir && cd ./docker/images/uvicorn
cp ../../../requirements.txt ./requirements.txt
docker build -t msp/uvicorn:latest .
