from flask import Flask

from controller import create_controller
from service import ChamadoService


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(create_controller(ChamadoService()))
    return app


if __name__ == "__main__":
    create_app().run(host="127.0.0.1", port=8080)
