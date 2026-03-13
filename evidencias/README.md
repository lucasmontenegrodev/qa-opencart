# Evidencias

Organizado por bug report.

Para os testes Playwright, rode:
  npx playwright test
  npx playwright show-report

O relatorio HTML gerado automaticamente ja inclui screenshots dos testes que falharam.

Estrutura para prints manuais:
```
evidencias/
├── BUG-001/
│   ├── 01-campo-busca-vazio.png
│   ├── 02-redirecionamento-sem-mensagem.png
│   └── 03-todos-produtos-listados.png
└── BUG-002/
    ├── 01-quantidade-alterada-para-zero.png
    ├── 02-botao-update-clicado.png
    └── 03-produto-removido-sem-mensagem.png
```