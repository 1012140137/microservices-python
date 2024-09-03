import os
from mongo import mongo_client


def get_user_by_access_token(access_token: str):
    db = mongo_client['celery_backend']
    tbl_user = db['tbl_user']
    return tbl_user.find_one({'access_token': access_token})