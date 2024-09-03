#! /usr/bin/env bash

# Let the DB start
sleep 10;
# Run migrations
pip install --upgrade pip
pip install -r ./requirements.txt
sleep 30;
# alembic upgrade head