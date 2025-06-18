# coding: utf-8

from fastapi import FastAPI

from openapi_server.apis.default_api import router as DefaultApiRouter

app = FastAPI(
    title="Formula One Fan API",
    description="API for managing Formula One fans, drivers, teams, races, and results.",
    version="1.0.0",
    servers=[
        {"url": "/", "description": "Root Server"},
    ],
)

app.include_router(DefaultApiRouter)
