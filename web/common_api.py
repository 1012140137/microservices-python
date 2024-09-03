#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fastapi import File, UploadFile, APIRouter, Request
from fastapi.responses import JSONResponse
import shutil
import os
from mongo import mongo_client
from bson import ObjectId
from datetime import datetime
import pytz
from flower_proxy import get_result as flower_get_result

router = APIRouter(
    prefix="/common",
    tags=["common"],
    responses={404: {"description": "Not found"}},
)


@router.post("/upload-file/")
async def upload_file(request: Request, file: UploadFile = File(...)):
    shared_storage_path = request.app.state['shared_storage_path']
     # generate a unique resource id
    _id = ObjectId()
    unique_resource_id = str(_id)
    # get the shared storage path, it will be mount to related celery worker container
    save_as_file_path = os.path.join(shared_storage_path, unique_resource_id, file.filename)
    if not os.path.exists(os.path.dirname(save_as_file_path)):
        os.makedirs(os.path.dirname(save_as_file_path))
    # save as the uploaded file
    with open(save_as_file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    # insert a document to mongodb
    db = mongo_client['celery_backend']
    tbl_upload_file = db['tbl_upload_file']
    tbl_upload_file.insert_one({
        '_id': _id,
        'file_name': file.filename,
        'file_path': save_as_file_path.replace(shared_storage_path, ''),
        'owner': request.state.user['email'],
        'created_at': datetime.now(tz=pytz.utc)
    })
    # return the saved file path
    return JSONResponse(content={
        "status_code": 0,
        "message": "File uploaded successfully",
        "data": {
            "resource_id": unique_resource_id,
        }
    })


@router.get("/get-task-result", description="get a task result")
async def get_task_result(request: Request, task_id: str):
    resp = flower_get_result(task_id)
    return JSONResponse(content=resp.json())