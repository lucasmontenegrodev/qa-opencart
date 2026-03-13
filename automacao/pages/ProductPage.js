const BasePage = require('./BasePage');

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