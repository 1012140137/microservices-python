#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from flower_proxy import execute_task

router = APIRouter(
    prefix="/async-task/email",
    tags=["email"],
    responses={404: {"description": "Not found"}},
)


@router.post("/send-email/")
async def send_email(request: Request, subject: str, html_content: str, to: str, cc: str = None):
    task_name = 'async_tasks.email.send_email'
    data = {
        'subject': subject,
        'html_content': html_content,
        'to': to,
        'cc': cc,
    }
    resp = execute_task(task_name, data)
    return JSONResponse(content=resp.json())
