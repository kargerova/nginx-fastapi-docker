"""Basic hello-world application using FastAPI.
"""
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from config import app_settings

app = FastAPI(
    title=app_settings.APP_NAME,
    version=app_settings.VERSION,
    description=app_settings.DESCRIPTION,
    contact=app_settings.CONTACT,
    docs_url= app_settings.DOCS_URL,
    openapi_url=f"{app_settings.SERVER_PATH}/openapi.json",
    
)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app_settings.APP_NAME,
        version=app_settings.VERSION,
        description=app_settings.DESCRIPTION,
        routes=app.routes,
    )
    openapi_schema["servers"] = [{"url": app_settings.SERVER_PATH}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

@app.get("/hello-world/")
def read_root():
    """
    Returns a JSON response with the message "Hello World".
    """
    return {
        "message": "Hello World",
        "body": "Welcome to the FastAPI application.",
        "app name": app_settings.APP_NAME,
        "version": app_settings.VERSION,
        }