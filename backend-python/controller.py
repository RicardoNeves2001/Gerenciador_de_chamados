from typing import Any, Literal

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field, field_validator

from service import ChamadoNaoEncontradoError, ChamadoService


class ChamadoCriacao(BaseModel):
    titulo: str = Field(min_length=1, max_length=120)
    descricao: str = Field(min_length=1)
    prioridade: Literal["baixa", "media", "alta"]
    status: Literal["aberto", "em_andamento", "fechado"] = "aberto"

    @field_validator("titulo", "descricao")
    @classmethod
    def remove_whitespace(cls, value: str) -> str:
        return value.strip()


def create_controller(service: ChamadoService) -> APIRouter:
    controller = APIRouter()

    @controller.get("/")
    def health_check() -> dict[str, str]:
        return {"status": "ok", "mensagem": "API de chamados funcionando"}

    @controller.post("/chamados", status_code=status.HTTP_201_CREATED)
    def create_called(payload: ChamadoCriacao) -> dict[str, Any]:
        return service.criar(payload.model_dump())

    @controller.get("/chamados")
    def list_called() -> list[dict[str, Any]]:
        return service.listar()

    @controller.get("/chamados/{called_id}")
    def get_called(called_id: int) -> dict[str, Any]:
        try:
            return service.buscar(called_id)
        except ChamadoNaoEncontradoError as error:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(error)) from error

    return controller
