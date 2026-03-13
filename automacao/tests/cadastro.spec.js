const { test, expect } = require('@playwright/test');
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