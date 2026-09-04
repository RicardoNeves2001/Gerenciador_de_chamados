import unittest

from app import create_app


class ChamadosApiTest(unittest.TestCase):
    def setUp(self) -> None:
        self.client = create_app().test_client()

    def tearDown(self) -> None:
        pass

    def test_rota_raiz_indica_que_api_esta_disponivel(self) -> None:
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "ok")

    def test_cria_lista_e_consulta_chamado(self) -> None:
        response = self.client.post(
            "/chamados",
            json={"titulo": "Acesso bloqueado", "descricao": "Painel indisponivel", "prioridade": "alta"},
        )
        self.assertEqual(response.status_code, 201)
        called_id = response.get_json()["id"]

        self.assertEqual(self.client.get("/chamados").status_code, 200)
        found = self.client.get(f"/chamados/{called_id}")
        self.assertEqual(found.status_code, 200)
        self.assertEqual(found.get_json()["titulo"], "Acesso bloqueado")

    def test_aplica_status_padrao(self) -> None:
        response = self.client.post(
            "/chamados", json={"titulo": "Sem prioridade", "descricao": "Descricao", "prioridade": "baixa"}
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json()["status"], "aberto")

    def test_valida_dados_e_retorna_404(self) -> None:
        self.assertEqual(self.client.post("/chamados", json={"descricao": "Descricao"}).status_code, 400)
        self.assertEqual(
            self.client.post(
                "/chamados",
                json={"titulo": "Teste", "descricao": "Descricao", "prioridade": "urgente"},
            ).status_code,
            400,
        )
        self.assertEqual(self.client.get("/chamados/999999").status_code, 404)

    def test_dados_sao_temporarios_em_memoria(self) -> None:
        response = self.client.post(
            "/chamados", json={"titulo": "Temporario", "descricao": "Nao persistir", "prioridade": "media"}
        )
        called_id = response.get_json()["id"]
        new_client = create_app().test_client()
        self.assertEqual(new_client.get(f"/chamados/{called_id}").status_code, 404)


if __name__ == "__main__":
    unittest.main()
