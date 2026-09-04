# API de Chamados com FastAPI

## Estrutura

- `main.py`: ponto de entrada compatível com o comando padrão do Uvicorn.
- `app.py`: inicialização da API e configuração do Uvicorn.
- `controller.py`: rotas HTTP e modelo de entrada Pydantic.
- `service.py`: regras de negócio, validação e armazenamento temporário em memória.
- `test_app.py`: testes dos endpoints e das regras.

## Executar

```bash
cd backend-python
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --host 127.0.0.1 --port 8080
```

A aplicação mantém os chamados apenas em memória. Ao reiniciar a API, os registros são apagados.
Depois de iniciar, a documentação interativa fica disponível em `http://127.0.0.1:8080/docs`.

## Testar

```bash
python3 -m unittest discover -s . -p 'test*.py' -v
```

```bash
curl -i -X POST http://127.0.0.1:8080/chamados \
  -H 'Content-Type: application/json' \
  -d '{"titulo":"Acesso bloqueado","descricao":"Nao consigo acessar o painel de atendimento.","prioridade":"alta"}'
curl -i http://127.0.0.1:8080/chamados
curl -i http://127.0.0.1:8080/chamados/1
curl -i http://127.0.0.1:8080/chamados/status/aberto
```

Os retornos esperados são `201`, `200`, `200`, `422` para dados inválidos e `404` para um identificador inexistente. As prioridades permitidas são `baixa`, `media` e `alta`.

Exemplo de sucesso (`201 Created`):

```json
{"id":1,"titulo":"Acesso bloqueado","descricao":"Nao consigo acessar o painel de atendimento.","prioridade":"alta","status":"aberto"}
```

Exemplo de erro de validação (`422 Unprocessable Entity`), ao remover `titulo`:

```json
{"detail":[{"loc":["body","titulo"],"msg":"Field required","type":"missing"}]}
```

## Evidências da atividade

- `POST /chamados` com dados válidos retorna `201 Created`.
- `POST /chamados` sem `titulo` retorna `422 Unprocessable Entity`.
- `GET /docs` disponibiliza a documentação interativa do FastAPI.
- Os 6 testes automatizados passam com `python3 -m unittest discover -s . -p 'test*.py' -v`.