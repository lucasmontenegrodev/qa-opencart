# TC-004 - Cadastro de Usuario

| Campo | Valor |
|---|---|
| ID | TC-004 |
| Funcionalidade | Cadastro de Usuario |
| Prioridade | Alta |
| Ambiente | http://localhost:8080 |
| Data | 12/03/2026 |
| Status | PASS (5/5) |

---

## Pre-condicoes

- OpenCart rodando localmente via Docker
- E-mail de teste nao cadastrado anteriormente

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Cadastro com dados validos | 1. Acessar My Account > Register. 2. Preencher todos os campos. 3. Aceitar termos. 4. Clicar em Continue. | Conta criada, redirecionamento para pagina de boas vindas | Cadastro realizado com sucesso | PASS |
| 2 | Cadastro com e-mail ja existente | 1. Tentar cadastrar com e-mail ja utilizado. | Mensagem de erro informando e-mail ja cadastrado | Mensagem exibida corretamente | PASS |
| 3 | Cadastro sem aceitar os termos | 1. Preencher formulario sem marcar checkbox de termos. 2. Clicar em Continue. | Validacao exigindo aceite dos termos | Validacao exibida corretamente | PASS |
| 4 | Cadastro com senha fraca | 1. Preencher formulario com senha de 3 caracteres. | Mensagem de requisito minimo de senha | Validacao exibida corretamente | PASS |
| 5 | Campos obrigatorios vazios | 1. Clicar em Continue sem preencher nada. | Validacao em todos os campos obrigatorios | Validacoes exibidas corretamente | PASS |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 5 | 5 | 0 | 100% |