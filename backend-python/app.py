from fastapi import FastAPI
import uvicorn

from controller import create_controller
from service import ChamadoService


def create_app() -> FastAPI:
    app = FastAPI(title="API de Chamados", version="1.0.0")
    app.include_router(create_controller(ChamadoService()))
    return app


app = create_app()


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8080)
