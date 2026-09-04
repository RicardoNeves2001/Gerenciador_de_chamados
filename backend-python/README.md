# API Python de chamados

## Estrutura

- `app.py`: inicialização da API.
- `controller.py`: rotas HTTP e respostas de erro.
- `service.py`: regras de negócio, validação e armazenamento temporário em memória.
- `test_app.py`: testes dos endpoints e das regras.

## Executar

```bash
cd backend-python
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

A aplicação mantém os chamados apenas em memória. Ao reiniciar a API, os registros são apagados.

## Testar

```bash
python3 -m unittest -v
```

```bash
curl -i -X POST http://127.0.0.1:8080/chamados \
  -H 'Content-Type: application/json' \
  -d '{"titulo":"Acesso bloqueado","descricao":"Nao consigo acessar o painel de atendimento.","prioridade":"alta"}'
curl -i http://127.0.0.1:8080/chamados
curl -i http://127.0.0.1:8080/chamados/1
```

Os retornos esperados são `201`, `200`, `200`, `400` para dados inválidos e `404` para um identificador inexistente. As prioridades permitidas são `baixa`, `media` e `alta`.

Exemplo de sucesso (`201 Created`):

```json
{"id":1,"titulo":"Acesso bloqueado","descricao":"Nao consigo acessar o painel de atendimento.","prioridade":"alta","status":"aberto"}
```

Exemplo de erro (`400 Bad Request`):

```json
{"erro":"dados invalidos","detalhes":["titulo: e obrigatorio"]}
```