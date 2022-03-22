from fastapi import FastAPI
from app.handlers import router


def get_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    return app


application = get_app()
