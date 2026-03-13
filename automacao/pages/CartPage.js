const BasePage = require('./BasePage');

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