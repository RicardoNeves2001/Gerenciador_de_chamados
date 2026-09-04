from datetime import datetime, timezone
from typing import Any


class DadosInvalidosError(ValueError):
    def __init__(self, detalhes: list[str]) -> None:
        self.detalhes = detalhes
        super().__init__("dados invalidos")


class ChamadoNaoEncontradoError(LookupError):
    pass


class ChamadoService:
    PRIORIDADES_PERMITIDAS = {"baixa", "media", "alta"}
    STATUS_PERMITIDOS = {"aberto", "em_andamento", "fechado"}

    def __init__(self) -> None:
        self._chamados: list[dict[str, Any]] = []
        self._proximo_id = 1

    def criar(self, dados: object) -> dict[str, Any]:
        if not isinstance(dados, dict):
            raise DadosInvalidosError(["corpo JSON invalido"])

        titulo = dados.get("titulo")
        descricao = dados.get("descricao")
        prioridade = dados.get("prioridade")
        status = dados.get("status", "aberto")
        erros = []
        if not isinstance(titulo, str) or not titulo.strip():
            erros.append("titulo: e obrigatorio")
        elif len(titulo) > 120:
            erros.append("titulo: deve ter no maximo 120 caracteres")
        if not isinstance(descricao, str) or not descricao.strip():
            erros.append("descricao: e obrigatoria")
        if prioridade not in self.PRIORIDADES_PERMITIDAS:
            erros.append("prioridade: deve ser baixa, media ou alta")
        if status not in self.STATUS_PERMITIDOS:
            erros.append("status: deve ser aberto, em_andamento ou fechado")
        if erros:
            raise DadosInvalidosError(erros)

        chamado = {
            "id": self._proximo_id,
            "titulo": titulo.strip(),
            "descricao": descricao.strip(),
            "prioridade": prioridade,
            "status": status,
            "criado_em": datetime.now(timezone.utc).isoformat(),
        }
        self._chamados.append(chamado)
        self._proximo_id += 1
        return chamado

    def listar(self) -> list[dict[str, Any]]:
        return self._chamados.copy()

    def listar_por_status(self, status: str) -> list[dict[str, Any]]:
        return [chamado for chamado in self._chamados if chamado["status"] == status]

    def buscar(self, chamado_id: int) -> dict[str, Any]:
        for chamado in self._chamados:
            if chamado["id"] == chamado_id:
                return chamado
        raise ChamadoNaoEncontradoError(f"Chamado nao encontrado: {chamado_id}")
