## Integrantes

- Ricardo da Silva Neves
- Thiago Penetra Cunha de Melo

# Gerenciador de Chamados

Sistema web para registrar, acompanhar e resolver solicitações de suporte interno em um único lugar.

## Objetivo

Substituir o controle disperso em planilhas e mensagens por um fluxo rastreável: a pessoa cliente abre o chamado, a pessoa atendente assume o atendimento e o sistema registra cada mudança até a resolução.

## MVP

- Criar chamado com título, descrição e categoria.
- Consultar os próprios chamados e seus status.
- Consultar a fila de atendimento.
- Atribuir um chamado a uma pessoa atendente.
- Alterar status, adicionar observação e encerrar o chamado.
- Filtrar chamados por status e atendente.

### Perfis

| Perfil | Pode fazer |
| --- | --- |
| Cliente | Criar chamados e acompanhar apenas os próprios registros. |
| Atendente | Consultar a fila, assumir chamados, atualizar o atendimento e encerrar chamados. |

## Fora do MVP

Notificações automáticas, anexos e relatórios de SLA ficam para uma próxima versão.

## Organização

```text
.
├── backend/    # API e regras de negócio
├── database/   # Modelo e scripts do banco
├── docs/       # Planejamento e arquitetura
└── frontend/   # Interface web
```

O planejamento está em [docs/planejamento-semana1.md](docs/planejamento-semana1.md), e a arquitetura está em [docs/diagrama-arquitetura.md](docs/diagrama-arquitetura.md).

