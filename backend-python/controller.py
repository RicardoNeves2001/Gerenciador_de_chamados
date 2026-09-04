from typing import Any

from flask import Blueprint, jsonify, request

from service import ChamadoNaoEncontradoError, ChamadoService, DadosInvalidosError


def create_controller(service: ChamadoService) -> Blueprint:
    controller = Blueprint("chamados", __name__)

    @controller.errorhandler(DadosInvalidosError)
    def handle_invalid_data(error: DadosInvalidosError) -> tuple[Any, int]:
        return jsonify(erro="dados invalidos", detalhes=error.detalhes), 400

    @controller.errorhandler(ChamadoNaoEncontradoError)
    def handle_not_found(error: ChamadoNaoEncontradoError) -> tuple[Any, int]:
        return jsonify(erro=str(error)), 404

    @controller.post("/chamados")
    def create_called() -> tuple[Any, int]:
        called = service.criar(request.get_json(silent=True))
        return jsonify(called), 201

    @controller.get("/chamados")
    def list_called() -> Any:
        return jsonify(service.listar())

    @controller.get("/chamados/<int:called_id>")
    def get_called(called_id: int) -> Any:
        return jsonify(service.buscar(called_id))

    return controller
