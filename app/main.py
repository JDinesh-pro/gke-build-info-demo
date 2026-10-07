import os

from fastapi import FastAPI

app = FastAPI(
    title="Build Info API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Build Info API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/build-info")
def build_info():
    return {
        "application": "build-info-api",
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "build_number": os.getenv("BUILD_NUMBER", "local"),
        "git_commit": os.getenv("GIT_COMMIT", "local"),
        "environment": os.getenv("ENVIRONMENT", "development")
    }