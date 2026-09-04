# Persistencia de chamados

## Modelo

```text
Chamado
- id: identificador unico gerado pelo banco
- titulo: texto obrigatorio, ate 120 caracteres
- descricao: texto obrigatorio
- prioridade: baixa | media | alta
- status: aberto | em_andamento | fechado
- criado_em: data e hora gerada pelo banco
```

## Estrutura e preparo

- Os dados são temporários e ficam em memória durante a execução da API.
- Ao reiniciar o processo, os registros são apagados; não há credenciais ou banco externo.

```bash
cd backend-python
python3 app.py
```

## Endpoints

| Metodo | Rota | Resultado |
| --- | --- | --- |
| POST | `/chamados` | Cria e retorna o chamado com `201 Created`. |
| GET | `/chamados` | Lista chamados persistidos com `200 OK`. |
| GET | `/chamados/{id}` | Retorna um chamado ou `404 Not Found`. |

Exemplo de criacao:

```bash
curl -i -X POST http://localhost:8080/chamados \
  -H 'Content-Type: application/json' \
  -d '{"titulo":"Acesso bloqueado","descricao":"Nao consigo acessar o painel de atendimento.","prioridade":"alta"}'
```

## Validacao e evidencia

O teste `test_app.py` verifica criacao, listagem, busca pelo identificador, dados temporarios em memoria, titulo ausente, prioridade invalida e identificador inexistente.

O formato de erro e consistente: `{"erro":"dados invalidos","detalhes":[...]}` para entradas rejeitadas e `404` para chamados inexistentes.

Exemplo de sucesso: `201 Created` com o chamado criado e seu `id`. Exemplo de erro: `400 Bad Request` com `{"erro":"dados invalidos","detalhes":[...]}` quando titulo, descricao ou prioridade nao forem validos.

## Decisao tecnica

Foi adotado Flask com armazenamento em memória para atender à prática. O controller concentra HTTP, o service concentra validações e as prioridades aceitas são `baixa`, `media` e `alta`.