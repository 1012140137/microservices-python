#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import pymongo

# get value from environment variables
mongo_host = os.getenv('MONGODB_HOST', 'localhost')
mongo_port = os.getenv('MONGODB_PORT', '27017')
mongo_user = os.getenv('MONGODB_USER', 'admin')
mongo_password = os.getenv('MONGODB_PASSWORD', 'secret')

# create a connection pool to mongodb
# The Python interpreter will cache imported module objects in memory, so import the same module multiple times will actually import the same object, 
# so the mongo_client will not be created repeatedly
mongo_conn_str = f"mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}"
mongo_client = pymongo.MongoClient(mongo_conn_str)
