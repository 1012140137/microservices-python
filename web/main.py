#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import FastAPI, Query, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from auth_handler import get_user_by_access_token
from email_api import router as email_api_router
from common_api import router as common_api_router

from fastapi.openapi.docs import (
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.staticfiles import StaticFiles

async def verify_access_token(request: Request, access_token: str):
    # if reqeust come from testserver, skip access_token check
    if request.headers.get('host') == 'testserver':
        return True
    exclude_paths = ['/swagger']
    if request.url.path in exclude_paths:
        return True
    # if access_token is None, deny access
    if access_token == None:
        raise HTTPException(
            status_code=400, detail="access_token is required")
    # print("access_token: ", access_token)
    # check access_token is valid
    user = get_user_by_access_token(access_token)
    if user == None:
        raise HTTPException(
            status_code=400, detail="access_token invalid")
    else:
        # print("user type is ", type(user))
        # print("user.email", user["email"])
        request.state.user = user
        return True

# 解决用nginx反向代理fastapi时swagger-ui不能正常使用的问题
openapi_prefix = os.getenv('OPENAPI_PREFIX', '')

app = FastAPI(title="Swagger", version="1.0.0", description="", docs_url=None, redoc_url=None, openapi_prefix=openapi_prefix)
# load static resources from local
app.mount("/static", StaticFiles(directory="static"), name="static")
# add CORS allow all
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# specify the swagger version and other metadata is required
# app.openapi = {
#     "swagger": "2.0"
# }

# set global variables
app.state = {
    "shared_storage_path": os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'runtime', 'upload_files')
}

# add routers
app.include_router(common_api_router, dependencies=[Depends(verify_access_token)])
app.include_router(email_api_router, dependencies=[Depends(verify_access_token)])

# add swagger ui
@app.get("/swagger", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=openapi_prefix + app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url=openapi_prefix + "/static/swagger-ui/swagger-ui-bundle.js",
        swagger_css_url=openapi_prefix + "/static/swagger-ui/swagger-ui.css",
        swagger_favicon_url=openapi_prefix + "/static/favicon.ico"
    )


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()

# for debug fastapi website
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
