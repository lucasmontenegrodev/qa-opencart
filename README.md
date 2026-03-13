# qa-opencart - Projeto Completo de QA

Projeto completo de Quality Assurance aplicado ao OpenCart, um e-commerce open source. Cobre planejamento, testes manuais e automacao E2E com Playwright em JavaScript utilizando Page Object Model (POM).

---

## Ambiente de Testes

OpenCart rodando localmente via Docker.

### Requisitos

- Docker Desktop instalado: https://www.docker.com/products/docker-desktop

### Subir o ambiente

```bash
docker run -d \
  --name opencart \
  -p 8080:8080 \
  -e OPENCART_USERNAME=admin \
  -e OPENCART_PASSWORD=admin1234 \
  bitnami/opencart:latest
```

Aguardar cerca de 2 minutos e acessar:

- Loja: http://localhost:8080
- Admin: http://localhost:8080/administration
- Usuario admin: admin / admin1234

---

## Estrutura do Repositorio

```
qa-opencart/
├── README.md
├── TEST-PLAN.md
│
├── testes-manuais/
│   ├── TC-001-busca-produto.md
│   ├── TC-002-pagina-produto.md
│   ├── TC-003-carrinho.md
│   ├── TC-004-cadastro.md
│   ├── TC-005-login.md
│   └── bug-reports/
│       ├── BUG-001-busca-vazia.md
│       └── BUG-002-quantidade-carrinho.md
│
├── automacao/
│   ├── package.json
│   ├── playwright.config.js
│   ├── pages/
│   │   ├── BasePage.js
│   │   ├── HomePage.js
│   │   ├── SearchPage.js
│   │   ├── ProductPage.js
│   │   ├── CartPage.js
│   │   └── RegisterPage.js
│   └── tests/
│       ├── busca.spec.js
│       ├── produto.spec.js
│       ├── carrinho.spec.js
│       └── cadastro.spec.js
│
└── evidencias/
    └── README.md
```

---

## Resumo dos Testes Manuais

| ID | Funcionalidade | Status | Bug |
|---|---|---|---|
| [TC-001](./testes-manuais/TC-001-busca-produto.md) | Busca de Produto | FAIL | [BUG-001](./testes-manuais/bug-reports/BUG-001-busca-vazia.md) |
| [TC-002](./testes-manuais/TC-002-pagina-produto.md) | Pagina do Produto | PASS | - |
| [TC-003](./testes-manuais/TC-003-carrinho.md) | Carrinho | FAIL | [BUG-002](./testes-manuais/bug-reports/BUG-002-quantidade-carrinho.md) |
| [TC-004](./testes-manuais/TC-004-cadastro.md) | Cadastro de Usuario | PASS | - |
| [TC-005](./testes-manuais/TC-005-login.md) | Login | PASS | - |

| Total | PASS | FAIL | Bugs |
|---|---|---|---|
| 5 | 3 | 2 | 2 |

---

## Automacao com Playwright + POM

```bash
cd automacao
npm install
npx playwright install chromium
npx playwright test
npx playwright show-report
```

---

## Tecnologias

| Ferramenta | Uso |
|---|---|
| Playwright | Automacao E2E |
| JavaScript | Linguagem dos testes |
| Page Object Model | Padrao de arquitetura da automacao |
| Docker | Ambiente de testes isolado e reproduzivel |
| Jira | Gestao de test cases e bugs |