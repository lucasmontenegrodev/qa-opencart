import os

README = """# qa-opencart - Projeto Completo de QA

Projeto completo de Quality Assurance aplicado ao OpenCart, um e-commerce open source. Cobre planejamento, testes manuais e automacao E2E com Playwright em JavaScript utilizando Page Object Model (POM).

---

## Ambiente de Testes

OpenCart rodando localmente via Docker.

### Requisitos

- Docker Desktop instalado: https://www.docker.com/products/docker-desktop

### Subir o ambiente

```bash
docker run -d \\
  --name opencart \\
  -p 8080:8080 \\
  -e OPENCART_USERNAME=admin \\
  -e OPENCART_PASSWORD=admin1234 \\
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
"""

TEST_PLAN = """# TEST-PLAN - QA OpenCart

| Campo | Valor |
|---|---|
| Projeto | qa-opencart |
| Aplicacao | OpenCart (local via Docker) |
| URL | http://localhost:8080 |
| Versao OpenCart | 4.x (Bitnami) |
| Autor | Lucas Montenegro |
| Data | 13/03/2026 |
| Status | Aprovado |

---

## 1. Objetivo

Validar os fluxos principais do frontend da loja OpenCart, garantindo que o cliente consegue buscar produtos, visualizar detalhes, adicionar ao carrinho, se cadastrar e fazer login sem erros.

---

## 2. Escopo

### Dentro do escopo

- Busca de produtos
- Pagina de detalhes do produto
- Adicionar produto ao carrinho
- Alterar quantidade no carrinho
- Remover produto do carrinho
- Cadastro de novo usuario
- Login e logout

### Fora do escopo

- Painel administrativo
- Checkout e pagamento
- Performance e carga
- Testes de seguranca

---

## 3. Tipos de Teste

| Tipo | Ferramenta | Responsavel |
|---|---|---|
| Testes manuais | Chrome + Jira | Lucas Montenegro |
| Automacao E2E | Playwright + POM (JavaScript) | Lucas Montenegro |

---

## 4. Ambiente

| Item | Valor |
|---|---|
| Plataforma | Docker local |
| Browser | Chrome |
| Sistema operacional | Windows 11 |
| URL da loja | http://localhost:8080 |

### Como subir o ambiente

```bash
docker run -d \\
  --name opencart \\
  -p 8080:8080 \\
  -e OPENCART_USERNAME=admin \\
  -e OPENCART_PASSWORD=admin1234 \\
  bitnami/opencart:latest
```

---

## 5. Criterios de Entrada

- Container Docker rodando e loja acessivel em http://localhost:8080
- Produtos cadastrados na loja
- Casos de teste revisados e aprovados

---

## 6. Criterios de Saida

- 100% dos casos de alta prioridade com PASS
- Nenhum bug critico ou blocker em aberto
- Cobertura minima de 80% dos casos com PASS
- Evidencias coletadas e salvas

---

## 7. Funcionalidades e Prioridades

| Funcionalidade | Prioridade | Tipo |
|---|---|---|
| Busca de produto | Alta | Manual + Automatizado |
| Pagina do produto | Alta | Manual + Automatizado |
| Carrinho | Alta | Manual + Automatizado |
| Cadastro | Alta | Manual + Automatizado |
| Login | Alta | Manual |
| Logout | Media | Manual |

---

## 8. Riscos

| Risco | Probabilidade | Impacto | Mitigacao |
|---|---|---|---|
| Container Docker nao sobe corretamente | Baixa | Alto | Documentar versao exata da imagem utilizada |
| Dados de teste alterados entre execucoes | Media | Medio | Resetar container antes de cada ciclo de testes |
| Seletores CSS mudam entre versoes do OpenCart | Baixa | Alto | Versionar imagem Docker utilizada |

---

## 9. Cronograma

| Atividade | Data |
|---|---|
| Setup do ambiente Docker | 10/03/2026 |
| Escrita dos test cases | 11/03/2026 |
| Execucao dos testes manuais | 12/03/2026 |
| Escrita e execucao da automacao | 13/03/2026 |
| Revisao e fechamento | 14/03/2026 |

---

## 10. Resultado Final

| Total de TCs | PASS | FAIL | Bugs Abertos | Aprovacao |
|---|---|---|---|---|
| 5 | 3 | 2 | 2 | 60% |

Observacao: Os 2 bugs encontrados sao de severidade media e nao bloqueiam o fluxo principal de compra. O fluxo critico (busca, produto, carrinho, cadastro, login) foi coberto integralmente.
"""

TC001 = """# TC-001 - Busca de Produto

| Campo | Valor |
|---|---|
| ID | TC-001 |
| Funcionalidade | Busca de Produto |
| Prioridade | Alta |
| Ambiente | http://localhost:8080 |
| Data | 12/03/2026 |
| Status | FAIL (4/5 - 1 falhou) |

---

## Pre-condicoes

- OpenCart rodando localmente via Docker
- Pelo menos 3 produtos cadastrados na loja

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Busca por termo valido | 1. Acessar http://localhost:8080. 2. Digitar "MacBook" no campo de busca. 3. Pressionar Enter. | Produtos relacionados exibidos com imagem, nome e preco | Produtos exibidos corretamente | PASS |
| 2 | Busca por termo parcial | 1. Digitar "Mac" no campo de busca. 2. Pressionar Enter. | Produtos cujo nome contenha "Mac" exibidos | Produtos exibidos corretamente | PASS |
| 3 | Busca sem resultado | 1. Digitar "produtoinexistente123" no campo de busca. 2. Pressionar Enter. | Mensagem "There is no product that matches the search criteria" | Mensagem exibida corretamente | PASS |
| 4 | Busca com campo vazio | 1. Clicar no botao de busca sem digitar nada. | Exibir validacao ou redirecionar para pagina com todos os produtos | Redireciona para pagina de busca sem mensagem clara ao usuario | FAIL |
| 5 | Busca case insensitive | 1. Digitar "macbook" em minusculo. 2. Pressionar Enter. | Mesmos resultados da busca com "MacBook" | Resultados identicos | PASS |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 5 | 4 | 1 | 80% |

---

## Bug gerado: BUG-001
"""

TC002 = """# TC-002 - Pagina do Produto

| Campo | Valor |
|---|---|
| ID | TC-002 |
| Funcionalidade | Pagina de Detalhes do Produto |
| Prioridade | Alta |
| Ambiente | http://localhost:8080 |
| Data | 12/03/2026 |
| Status | PASS (5/5) |

---

## Pre-condicoes

- OpenCart rodando localmente via Docker
- Produto "MacBook" disponivel na loja

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Visualizar detalhes do produto | 1. Buscar "MacBook". 2. Clicar no produto. | Nome, preco, imagem, descricao e botao "Add to Cart" visiveis | Todos os elementos exibidos | PASS |
| 2 | Galeria de imagens | 1. Acessar pagina do produto. 2. Clicar nas imagens miniatura. | Imagem principal atualizada ao clicar nas miniaturas | Imagens atualizadas corretamente | PASS |
| 3 | Alterar quantidade antes de adicionar | 1. Acessar pagina do produto. 2. Alterar quantidade para 2. 3. Clicar em "Add to Cart". | Produto adicionado com quantidade 2 | Quantidade respeitada | PASS |
| 4 | Adicionar produto sem estoque | 1. Acessar produto sem estoque. | Botao "Add to Cart" desabilitado ou mensagem de indisponibilidade | Produto exibe "Out of Stock" e botao desabilitado | PASS |
| 5 | Exibicao do preco com e sem desconto | 1. Acessar produto com preco promocional. | Preco original riscado e preco promocional destacado | Precos exibidos corretamente | PASS |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 5 | 5 | 0 | 100% |
"""

TC003 = """# TC-003 - Carrinho

| Campo | Valor |
|---|---|
| ID | TC-003 |
| Funcionalidade | Carrinho de Compras |
| Prioridade | Alta |
| Ambiente | http://localhost:8080 |
| Data | 12/03/2026 |
| Status | FAIL (4/5 - 1 falhou) |

---

## Pre-condicoes

- OpenCart rodando localmente via Docker
- Usuario logado ou anonimo com produto disponivel

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Adicionar produto ao carrinho | 1. Acessar pagina do produto. 2. Clicar em "Add to Cart". | Notificacao de sucesso exibida, contador do carrinho atualizado | Produto adicionado corretamente | PASS |
| 2 | Visualizar carrinho | 1. Adicionar produto. 2. Clicar no icone do carrinho. | Produto listado com nome, quantidade, preco unitario e total | Carrinho exibido corretamente | PASS |
| 3 | Remover produto do carrinho | 1. Acessar carrinho. 2. Clicar no botao de remover. | Produto removido, total atualizado | Produto removido corretamente | PASS |
| 4 | Alterar quantidade no carrinho | 1. Acessar carrinho. 2. Alterar quantidade para 3. 3. Clicar em "Update". | Quantidade e total atualizados corretamente | Quantidade atualizada corretamente | PASS |
| 5 | Inserir quantidade zero ou negativa | 1. Acessar carrinho. 2. Alterar quantidade para 0. 3. Clicar em "Update". | Exibir validacao impedindo quantidade invalida | Produto removido silenciosamente sem mensagem ao usuario | FAIL |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 5 | 4 | 1 | 80% |

---

## Bug gerado: BUG-002
"""

TC004 = """# TC-004 - Cadastro de Usuario

| Campo | Valor |
|---|---|
| ID | TC-004 |
| Funcionalidade | Cadastro de Usuario |
| Prioridade | Alta |
| Ambiente | http://localhost:8080 |
| Data | 12/03/2026 |
| Status | PASS (5/5) |

---

## Pre-condicoes

- OpenCart rodando localmente via Docker
- E-mail de teste nao cadastrado anteriormente

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Cadastro com dados validos | 1. Acessar My Account > Register. 2. Preencher todos os campos. 3. Aceitar termos. 4. Clicar em Continue. | Conta criada, redirecionamento para pagina de boas vindas | Cadastro realizado com sucesso | PASS |
| 2 | Cadastro com e-mail ja existente | 1. Tentar cadastrar com e-mail ja utilizado. | Mensagem de erro informando e-mail ja cadastrado | Mensagem exibida corretamente | PASS |
| 3 | Cadastro sem aceitar os termos | 1. Preencher formulario sem marcar checkbox de termos. 2. Clicar em Continue. | Validacao exigindo aceite dos termos | Validacao exibida corretamente | PASS |
| 4 | Cadastro com senha fraca | 1. Preencher formulario com senha de 3 caracteres. | Mensagem de requisito minimo de senha | Validacao exibida corretamente | PASS |
| 5 | Campos obrigatorios vazios | 1. Clicar em Continue sem preencher nada. | Validacao em todos os campos obrigatorios | Validacoes exibidas corretamente | PASS |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 5 | 5 | 0 | 100% |
"""

TC005 = """# TC-005 - Login

| Campo | Valor |
|---|---|
| ID | TC-005 |
| Funcionalidade | Login de Usuario |
| Prioridade | Alta |
| Ambiente | http://localhost:8080 |
| Data | 12/03/2026 |
| Status | PASS (4/4) |

---

## Pre-condicoes

- OpenCart rodando localmente via Docker
- Usuario de teste cadastrado

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Login com credenciais validas | 1. Acessar My Account > Login. 2. Informar e-mail e senha corretos. 3. Clicar em Login. | Redirecionamento para area do cliente | Login realizado com sucesso | PASS |
| 2 | Login com senha incorreta | 1. Informar e-mail correto e senha errada. | Mensagem de credenciais invalidas | Mensagem exibida corretamente | PASS |
| 3 | Login com e-mail nao cadastrado | 1. Informar e-mail inexistente. | Mensagem de credenciais invalidas | Mensagem exibida corretamente | PASS |
| 4 | Logout | 1. Logar. 2. Acessar My Account > Logout. | Sessao encerrada, redirecionamento para pagina de logout | Logout realizado corretamente | PASS |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 4 | 4 | 0 | 100% |
"""

BUG001 = """# BUG-001 - Busca com campo vazio nao exibe mensagem clara ao usuario

| Campo | Valor |
|---|---|
| ID | BUG-001 |
| Test Case | TC-001 - Caso 4 |
| Data | 12/03/2026 |
| Reportado por | Lucas Montenegro |
| Severidade | Baixa |
| Prioridade | Media |
| Ambiente | OpenCart local Docker v4.x |
| Status | Aberto |

---

## Descricao

Ao clicar no botao de busca sem digitar nenhum termo, o sistema redireciona o usuario para a pagina de resultados de busca sem exibir nenhuma mensagem orientando o usuario. A pagina exibe todos os produtos sem filtro, o que pode confundir o usuario.

---

## Passos para Reproduzir

1. Acessar http://localhost:8080
2. Deixar o campo de busca vazio
3. Clicar no icone de busca (lupa)
4. Observar o resultado

---

## Resultado Esperado

Exibir mensagem de validacao "Digite um termo para buscar" ou impedir o envio do formulario vazio.

---

## Resultado Obtido

Usuario redirecionado para pagina de busca sem mensagem. Todos os produtos sao listados sem nenhuma indicacao de que a busca esta vazia.

---

## Evidencias

```
evidencias/BUG-001/
├── 01-campo-busca-vazio.png
├── 02-redirecionamento-sem-mensagem.png
└── 03-todos-produtos-listados.png
```

---

## Impacto

Experiencia confusa para o usuario. Sem mensagem de orientacao, o usuario pode nao entender o que aconteceu.

---

## Hipotese

O formulario de busca nao possui validacao client-side para campo vazio. Adicionar validacao no front-end antes do submit ou tratamento no controller de busca.
"""

BUG002 = """# BUG-002 - Quantidade zero no carrinho remove produto sem confirmacao

| Campo | Valor |
|---|---|
| ID | BUG-002 |
| Test Case | TC-003 - Caso 5 |
| Data | 12/03/2026 |
| Reportado por | Lucas Montenegro |
| Severidade | Media |
| Prioridade | Alta |
| Ambiente | OpenCart local Docker v4.x |
| Status | Aberto |

---

## Descricao

Ao alterar a quantidade de um produto no carrinho para 0 e clicar em "Update", o produto e removido silenciosamente sem nenhuma mensagem de confirmacao ou validacao. O comportamento esperado seria impedir a insercao de quantidade invalida com uma mensagem de erro.

---

## Passos para Reproduzir

1. Acessar http://localhost:8080
2. Adicionar qualquer produto ao carrinho
3. Acessar o carrinho
4. Alterar o campo de quantidade para 0
5. Clicar em "Update"
6. Observar o comportamento

---

## Resultado Esperado

Mensagem de validacao "A quantidade deve ser maior que zero" ou campo impedido de aceitar valores menores que 1.

---

## Resultado Obtido

Produto removido imediatamente do carrinho sem nenhuma mensagem ou confirmacao ao usuario.

---

## Evidencias

```
evidencias/BUG-002/
├── 01-quantidade-alterada-para-zero.png
├── 02-botao-update-clicado.png
└── 03-produto-removido-sem-mensagem.png
```

---

## Impacto

Usuario pode perder itens do carrinho acidentalmente ao tentar alterar a quantidade e digitar 0 por engano. Sem mensagem de feedback, o usuario pode nao entender o que ocorreu.

---

## Hipotese

O controller do carrinho interpreta quantidade 0 como remocao do item. Adicionar validacao no front-end impedindo valores menores que 1, ou no back-end retornar erro com mensagem clara antes de processar a remocao.
"""

BASE_PAGE = """class BasePage {
  constructor(page) {
    this.page = page;
    this.baseURL = 'http://localhost:8080';
  }

  async navigate(path = '') {
    await this.page.goto(`${this.baseURL}${path}`);
  }

  async getTitle() {
    return await this.page.title();
  }
}

module.exports = BasePage;
"""

HOME_PAGE = """const BasePage = require('./BasePage');

class HomePage extends BasePage {
  constructor(page) {
    super(page);
    this.searchInput = page.locator('input[name="search"]');
    this.searchButton = page.locator('button.btn-light.btn-lg');
    this.cartIcon = page.locator('#cart');
  }

  async goto() {
    await this.navigate('/');
  }

  async search(term) {
    await this.searchInput.fill(term);
    await this.searchButton.click();
  }

  async getCartCount() {
    return await this.cartIcon.textContent();
  }
}

module.exports = HomePage;
"""

SEARCH_PAGE = """const BasePage = require('./BasePage');

class SearchPage extends BasePage {
  constructor(page) {
    super(page);
    this.productList = page.locator('.product-thumb');
    this.noResultsMessage = page.locator('.col p');
  }

  async getProductCount() {
    return await this.productList.count();
  }

  async clickFirstProduct() {
    await this.productList.first().locator('h4 a').click();
  }

  async getNoResultsMessage() {
    return await this.noResultsMessage.textContent();
  }
}

module.exports = SearchPage;
"""

PRODUCT_PAGE = """const BasePage = require('./BasePage');

class ProductPage extends BasePage {
  constructor(page) {
    super(page);
    this.productName = page.locator('h1');
    this.productPrice = page.locator('.price-new, .price');
    this.quantityInput = page.locator('#input-quantity');
    this.addToCartButton = page.locator('#button-cart');
    this.successAlert = page.locator('.alert-success');
  }

  async getProductName() {
    return await this.productName.textContent();
  }

  async getProductPrice() {
    return await this.productPrice.first().textContent();
  }

  async setQuantity(qty) {
    await this.quantityInput.fill(String(qty));
  }

  async addToCart() {
    await this.addToCartButton.click();
  }

  async getSuccessMessage() {
    await this.successAlert.waitFor({ timeout: 5000 });
    return await this.successAlert.textContent();
  }
}

module.exports = ProductPage;
"""

CART_PAGE = """const BasePage = require('./BasePage');

class CartPage extends BasePage {
  constructor(page) {
    super(page);
    this.cartItems = page.locator('table tbody tr');
    this.removeButtons = page.locator('button.btn-danger');
    this.updateButtons = page.locator('button.btn-primary');
    this.totalPrice = page.locator('tfoot tr:last-child td:last-child');
  }

  async goto() {
    await this.navigate('/index.php?route=checkout/cart');
  }

  async getItemCount() {
    return await this.cartItems.count();
  }

  async updateQuantity(index, qty) {
    const qtyInput = this.cartItems.nth(index).locator('input.form-control');
    await qtyInput.fill(String(qty));
    await this.updateButtons.nth(index).click();
  }

  async removeItem(index) {
    await this.removeButtons.nth(index).click();
  }

  async getTotal() {
    return await this.totalPrice.textContent();
  }
}

module.exports = CartPage;
"""

REGISTER_PAGE = """const BasePage = require('./BasePage');

class RegisterPage extends BasePage {
  constructor(page) {
    super(page);
    this.firstNameInput = page.locator('#input-firstname');
    this.lastNameInput = page.locator('#input-lastname');
    this.emailInput = page.locator('#input-email');
    this.passwordInput = page.locator('#input-password');
    this.privacyCheckbox = page.locator('input[name="agree"]');
    this.submitButton = page.locator('button[type="submit"]');
    this.successMessage = page.locator('#content h1');
    this.errorAlert = page.locator('.alert-danger');
  }

  async goto() {
    await this.navigate('/index.php?route=account/register');
  }

  async fillForm({ firstName, lastName, email, password }) {
    await this.firstNameInput.fill(firstName);
    await this.lastNameInput.fill(lastName);
    await this.emailInput.fill(email);
    await this.passwordInput.fill(password);
  }

  async acceptPrivacy() {
    await this.privacyCheckbox.check();
  }

  async submit() {
    await this.submitButton.click();
  }

  async getSuccessHeading() {
    return await this.successMessage.textContent();
  }

  async getErrorMessage() {
    return await this.errorAlert.textContent();
  }
}

module.exports = RegisterPage;
"""

SPEC_BUSCA = """const { test, expect } = require('@playwright/test');
const HomePage = require('../pages/HomePage');
const SearchPage = require('../pages/SearchPage');

test.describe('Busca de Produto', () => {
  test('busca por termo valido retorna resultados', async ({ page }) => {
    const home = new HomePage(page);
    const search = new SearchPage(page);

    await home.goto();
    await home.search('MacBook');

    const count = await search.getProductCount();
    expect(count).toBeGreaterThan(0);
  });

  test('busca sem resultado exibe mensagem', async ({ page }) => {
    const home = new HomePage(page);
    const search = new SearchPage(page);

    await home.goto();
    await home.search('produtoinexistente999');

    const message = await search.getNoResultsMessage();
    expect(message).toContain('There is no product that matches');
  });

  test('busca case insensitive retorna os mesmos resultados', async ({ page }) => {
    const home = new HomePage(page);
    const search = new SearchPage(page);

    await home.goto();
    await home.search('macbook');

    const count = await search.getProductCount();
    expect(count).toBeGreaterThan(0);
  });
});
"""

SPEC_PRODUTO = """const { test, expect } = require('@playwright/test');
const HomePage = require('../pages/HomePage');
const SearchPage = require('../pages/SearchPage');
const ProductPage = require('../pages/ProductPage');

test.describe('Pagina do Produto', () => {
  test.beforeEach(async ({ page }) => {
    const home = new HomePage(page);
    const search = new SearchPage(page);

    await home.goto();
    await home.search('MacBook');
    await search.clickFirstProduct();
  });

  test('exibe nome e preco do produto', async ({ page }) => {
    const product = new ProductPage(page);

    const name = await product.getProductName();
    const price = await product.getProductPrice();

    expect(name).toBeTruthy();
    expect(price).toContain('$');
  });

  test('adicionar produto ao carrinho', async ({ page }) => {
    const product = new ProductPage(page);

    await product.addToCart();
    const message = await product.getSuccessMessage();

    expect(message).toContain('Success');
  });

  test('adicionar produto com quantidade personalizada', async ({ page }) => {
    const product = new ProductPage(page);

    await product.setQuantity(2);
    await product.addToCart();
    const message = await product.getSuccessMessage();

    expect(message).toContain('Success');
  });
});
"""

SPEC_CARRINHO = """const { test, expect } = require('@playwright/test');
const HomePage = require('../pages/HomePage');
const SearchPage = require('../pages/SearchPage');
const ProductPage = require('../pages/ProductPage');
const CartPage = require('../pages/CartPage');

test.describe('Carrinho', () => {
  test.beforeEach(async ({ page }) => {
    const home = new HomePage(page);
    const search = new SearchPage(page);
    const product = new ProductPage(page);

    await home.goto();
    await home.search('MacBook');
    await search.clickFirstProduct();
    await product.addToCart();
    await product.getSuccessMessage();
  });

  test('produto adicionado aparece no carrinho', async ({ page }) => {
    const cart = new CartPage(page);
    await cart.goto();

    const count = await cart.getItemCount();
    expect(count).toBeGreaterThan(0);
  });

  test('remover produto do carrinho', async ({ page }) => {
    const cart = new CartPage(page);
    await cart.goto();

    await cart.removeItem(0);
    await page.waitForTimeout(1000);

    const count = await cart.getItemCount();
    expect(count).toBe(0);
  });
});
"""

SPEC_CADASTRO = """const { test, expect } = require('@playwright/test');
const RegisterPage = require('../pages/RegisterPage');

test.describe('Cadastro de Usuario', () => {
  test('cadastro com dados validos', async ({ page }) => {
    const register = new RegisterPage(page);
    await register.goto();

    const timestamp = Date.now();
    await register.fillForm({
      firstName: 'Lucas',
      lastName: 'Montenegro',
      email: `qa.teste.${timestamp}@email.com`,
      password: 'Teste@1234',
    });

    await register.acceptPrivacy();
    await register.submit();

    const heading = await register.getSuccessHeading();
    expect(heading).toContain('Your Account Has Been Created');
  });

  test('campos obrigatorios vazios exibem validacao', async ({ page }) => {
    const register = new RegisterPage(page);
    await register.goto();

    await register.submit();

    await expect(page.locator('.text-danger').first()).toBeVisible();
  });
});
"""

PACKAGE_JSON = """{
  "name": "qa-opencart-automacao",
  "version": "1.0.0",
  "description": "Testes E2E com Playwright e POM para OpenCart",
  "scripts": {
    "test": "npx playwright test",
    "test:ui": "npx playwright test --ui",
    "test:report": "npx playwright show-report"
  },
  "devDependencies": {
    "@playwright/test": "^1.42.0"
  }
}
"""

PLAYWRIGHT_CONFIG = """const { defineConfig } = require('@playwright/test');

module.exports = defineConfig({
  testDir: './tests',
  timeout: 30000,
  retries: 1,
  use: {
    baseURL: 'http://localhost:8080',
    headless: true,
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },
  reporter: [['html', { open: 'never' }]],
});
"""

EVIDENCIAS = """# Evidencias

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
"""

arquivos = {
    "README.md":                                            README,
    "TEST-PLAN.md":                                         TEST_PLAN,
    "testes-manuais/TC-001-busca-produto.md":               TC001,
    "testes-manuais/TC-002-pagina-produto.md":              TC002,
    "testes-manuais/TC-003-carrinho.md":                    TC003,
    "testes-manuais/TC-004-cadastro.md":                    TC004,
    "testes-manuais/TC-005-login.md":                       TC005,
    "testes-manuais/bug-reports/BUG-001-busca-vazia.md":    BUG001,
    "testes-manuais/bug-reports/BUG-002-quantidade-carrinho.md": BUG002,
    "automacao/package.json":                               PACKAGE_JSON,
    "automacao/playwright.config.js":                       PLAYWRIGHT_CONFIG,
    "automacao/pages/BasePage.js":                          BASE_PAGE,
    "automacao/pages/HomePage.js":                          HOME_PAGE,
    "automacao/pages/SearchPage.js":                        SEARCH_PAGE,
    "automacao/pages/ProductPage.js":                       PRODUCT_PAGE,
    "automacao/pages/CartPage.js":                          CART_PAGE,
    "automacao/pages/RegisterPage.js":                      REGISTER_PAGE,
    "automacao/tests/busca.spec.js":                        SPEC_BUSCA,
    "automacao/tests/produto.spec.js":                      SPEC_PRODUTO,
    "automacao/tests/carrinho.spec.js":                     SPEC_CARRINHO,
    "automacao/tests/cadastro.spec.js":                     SPEC_CADASTRO,
    "evidencias/README.md":                                 EVIDENCIAS,
}

print("Criando repositorio qa-opencart...")

for caminho, conteudo in arquivos.items():
    pasta = os.path.dirname(caminho)
    if pasta:
        os.makedirs(pasta, exist_ok=True)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo.strip())
    print(f"  OK: {caminho}")

print(f"\nPronto. {len(arquivos)} arquivos criados.")
print("\nProximos passos:")
print("  1. Crie o repositorio 'qa-opencart' no GitHub")
print("  2. git clone https://github.com/lucasmontenegrodev/qa-opencart.git")
print("  3. cd qa-opencart")
print("  4. Coloque este script aqui e rode: python setup_opencart.py")
print("  5. git add .")
print('  6. git commit -m "feat: projeto completo qa-opencart com POM"')
print("  7. git push origin main --force")
print("\nPara rodar os testes:")
print("  docker run -d --name opencart -p 8080:8080 -e OPENCART_USERNAME=admin -e OPENCART_PASSWORD=admin1234 bitnami/opencart:latest")
print("  cd automacao")
print("  npm install")
print("  npx playwright install chromium")
print("  npx playwright test")
