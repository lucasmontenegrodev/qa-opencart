const BasePage = require('./BasePage');

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