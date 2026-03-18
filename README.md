# qa-opencart - Full QA Project

Complete Quality Assurance project applied to OpenCart, a real-world open source e-commerce platform. Covers test planning, manual testing with bug reports, and E2E automation with Playwright using Page Object Model (POM).

---

## Target Application

OpenCart running locally via Docker.

### Requirements

- Docker Desktop: https://www.docker.com/products/docker-desktop
- Node.js 18+: https://nodejs.org

### Setup

```bash
docker run -d \
  --name opencart \
  -p 8080:8080 \
  -e OPENCART_USERNAME=admin \
  -e OPENCART_PASSWORD=admin1234 \
  bitnami/opencart:latest
```

Wait ~2 minutes, then access:

- Store: http://localhost:8080
- Admin: http://localhost:8080/administration
- Credentials: admin / admin1234

---

## Repository Structure

```
qa-opencart/
├── README.md
├── TEST-PLAN.md
├── testes-manuais/
│   ├── TC-001-busca-produto.md
│   ├── TC-002-pagina-produto.md
│   ├── TC-003-carrinho.md
│   ├── TC-004-cadastro.md
│   ├── TC-005-login.md
│   └── bug-reports/
│       ├── BUG-001-busca-vazia.md
│       └── BUG-002-quantidade-carrinho.md
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
└── evidencias/
    └── README.md
```

---

## Manual Test Results

| ID | Feature | Status | Bug |
|---|---|---|---|
| [TC-001](./testes-manuais/TC-001-busca-produto.md) | Product Search | FAIL | [BUG-001](./testes-manuais/bug-reports/BUG-001-busca-vazia.md) |
| [TC-002](./testes-manuais/TC-002-pagina-produto.md) | Product Page | PASS | - |
| [TC-003](./testes-manuais/TC-003-carrinho.md) | Shopping Cart | FAIL | [BUG-002](./testes-manuais/bug-reports/BUG-002-quantidade-carrinho.md) |
| [TC-004](./testes-manuais/TC-004-cadastro.md) | User Registration | PASS | - |
| [TC-005](./testes-manuais/TC-005-login.md) | Login | PASS | - |

| Total | PASS | FAIL | Bugs |
|---|---|---|---|
| 5 | 3 | 2 | 2 |

---

## Automation — Playwright + POM

### Running the tests

```bash
cd automacao
npm install
npx playwright install chromium
npx playwright test
npx playwright show-report
```

### Architecture — Page Object Model

Each page has its own class under `automacao/pages/`, keeping test logic separate from page interaction logic.

```
pages/
├── BasePage.js       - base class with shared methods
├── HomePage.js       - search bar, cart icon
├── SearchPage.js     - product list, result count
├── ProductPage.js    - product name, price, add to cart
├── CartPage.js       - items, quantity, remove, total
└── RegisterPage.js   - registration form, submit, validation
```

### Test Coverage

| Suite | Scenarios |
|---|---|
| busca.spec.js | Valid search, no results, case insensitive |
| produto.spec.js | Name and price display, add to cart, custom quantity |
| carrinho.spec.js | Item in cart, remove item |
| cadastro.spec.js | Valid registration, empty fields validation |

---

## Tech Stack

| Tool | Usage |
|---|---|
| Playwright | E2E test automation |
| JavaScript | Test language |
| Page Object Model | Automation architecture |
| Docker | Isolated and reproducible test environment |
| Jira | Test case and bug management |
| Chrome DevTools | Evidence collection and network logs |

---

## Key Highlights

- Real e-commerce platform running on Docker — fully reproducible environment
- Page Object Model keeping page logic separate from test logic
- Complete QA cycle: Test Plan → Manual Tests → Bug Reports → Automation
- Bug reports include reproduction steps, evidence and technical hypothesis for the developer