const BasePage = require('./BasePage');

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