const { test, expect } = require('@playwright/test');
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