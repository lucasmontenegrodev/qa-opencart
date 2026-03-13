const { test, expect } = require('@playwright/test');
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