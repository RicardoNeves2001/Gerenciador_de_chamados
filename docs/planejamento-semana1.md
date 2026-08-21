# Planejamento da Semana 1

**Data:** 10 de agosto de 2026
**Produto:** Sistema de Gestão de Chamados (MVP)

## Problema

As solicitações de suporte são registradas em planilhas e canais de mensagem diferentes. Isso dificulta saber quem está responsável, qual é o status de cada pedido e quais atendimentos ainda estão pendentes.

## Decisão do MVP

O primeiro ciclo terá um sistema web com API e banco relacional. O foco é garantir o ciclo básico do chamado, sem notificações, anexos ou indicadores avançados.

### Dentro do escopo

1. A pessoa cliente cria um chamado com título, descrição e categoria.
2. A pessoa cliente consulta seus chamados e o status atual.
3. A pessoa atendente consulta a fila, assume um chamado e atualiza seu status.
4. A pessoa atendente registra uma observação e encerra o atendimento.
5. A fila pode ser filtrada por status e atendente.

### Fora do escopo

- Notificações por e-mail, push ou WhatsApp.
- Upload de arquivos e imagens.
- Dashboard, SLA e relatórios analíticos.

## Perfis e permissões

| Perfil | Responsabilidade | Limite de acesso |
| --- | --- | --- |
| Cliente | Informar o problema e acompanhar o atendimento. | Visualiza e interage apenas com os próprios chamados. |
| Atendente | Organizar a fila e resolver solicitações. | Visualiza a fila e altera chamados sob atendimento. |

## Requisitos funcionais

- O sistema deve permitir que uma pessoa cliente registre um chamado com título, descrição e categoria.
- O sistema deve permitir que uma pessoa cliente consulte os chamados registrados por ela.
- O sistema deve permitir que uma pessoa atendente consulte os chamados abertos.
- O sistema deve permitir que uma pessoa atendente altere o status de um chamado.
- O sistema deve permitir que uma pessoa atendente registre uma observação e encerre um chamado.

## Recursos e informações armazenadas

| Recurso | Possíveis informações |
| --- | --- |
| Chamado | Identificador, título, descrição, status, data de abertura, data de encerramento, cliente, atendente e categoria. |
| Cliente | Identificador, nome e contato. |
| Atendente | Identificador e nome. |
| Categoria | Identificador, nome e descrição. |
| Observação | Texto, autor e data da atualização. |

## Regras essenciais

- Todo chamado nasce como **Aberto** e recebe identificador e data de abertura no back-end.
- Apenas o back-end valida permissões e aplica mudanças de status.
- Um chamado só pode ser encerrado quando houver uma solução ou observação final.
- A data de encerramento é preenchida pelo back-end no momento do fechamento.
- O cliente não pode acessar chamados de outra pessoa.

## Fluxo principal: abertura de chamado

1. A pessoa cliente acessa a tela de abertura de chamado.
2. A pessoa cliente informa título, categoria e descrição e seleciona a opção de envio.
3. A interface valida os campos obrigatórios e envia um `POST` para a API.
4. A API valida os dados e a permissão e cria o chamado como **Aberto**.
5. O banco de dados armazena o chamado com identificador e data de abertura.
6. A API responde com `201 Created` e o identificador do chamado.
7. A interface confirma a abertura e mostra o protocolo para a pessoa cliente.

## Discussão técnica

- **O que a interface faz neste fluxo?** Coleta os dados, verifica campos obrigatórios, envia a requisição e exibe o resultado para a pessoa cliente.
- **Qual regra precisa ficar no back-end?** A validação de permissões, a criação do identificador, o status inicial, as transições de status e as datas de controle.
- **Onde os chamados são armazenados?** Em um banco de dados relacional, acessado somente pelo back-end.
- **Qual componente pode ser substituído com menor impacto?** A interface web, porque se comunica com o back-end por uma API. Uma aplicação mobile poderia consumir o mesmo contrato.

## Critério de aceite do ciclo inicial

É possível criar um chamado, encontrá-lo na fila da pessoa atendente, atribuí-lo, registrar uma atualização e encerrá-lo. Em todo o percurso, cada pessoa vê somente as informações permitidas pelo seu perfil.

## Próximos passos

1. Definir a tecnologia concreta da API e da interface.
2. Modelar as tabelas de usuários, categorias, chamados e observações.
3. Implementar a API do fluxo de abertura e consulta.
4. Criar a tela de abertura e a fila de atendimento.