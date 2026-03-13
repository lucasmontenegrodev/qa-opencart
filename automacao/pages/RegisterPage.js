const BasePage = require('./BasePage');

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