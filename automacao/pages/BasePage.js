class BasePage {
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