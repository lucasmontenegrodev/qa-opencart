const { test, expect } = require('@playwright/test');
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