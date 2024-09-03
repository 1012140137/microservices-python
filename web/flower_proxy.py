#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import os
from typing import Dict

# get value from environment variables
flower_api_base_url = os.getenv('FLOWER_API_BASE_URL', 'http://localhost:8081')
flower_user_name = os.getenv('FLOWER_USER_NAME', 'admin')
flower_password = os.getenv('FLOWER_PASSWORD', 'secret')

flower_request_timeout = 10


def execute_task(task_name: str, data: Dict = None):
    url = f'{flower_api_base_url}/api/task/send-task/{task_name}'
    # print("url: ", url)
    # print("data: ", data, ", type: ", type(data))
    return requests.post(url, json={'kwargs': data}, timeout=flower_request_timeout, auth=(
        flower_user_name, flower_password))

def get_result(task_id: str):
    url = f'{flower_api_base_url}/api/task/result/{task_id}'
    print("url: ", url)
    return requests.get(url, timeout=flower_request_timeout, auth=(
        flower_user_name, flower_password))
