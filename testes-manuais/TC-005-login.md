# TC-005 - Login

| Campo | Valor |
|---|---|
| ID | TC-005 |
| Funcionalidade | Login de Usuario |
| Prioridade | Alta |
| Ambiente | http://localhost:8080 |
| Data | 12/03/2026 |
| Status | PASS (4/4) |

---

## Pre-condicoes

- OpenCart rodando localmente via Docker
- Usuario de teste cadastrado

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Login com credenciais validas | 1. Acessar My Account > Login. 2. Informar e-mail e senha corretos. 3. Clicar em Login. | Redirecionamento para area do cliente | Login realizado com sucesso | PASS |
| 2 | Login com senha incorreta | 1. Informar e-mail correto e senha errada. | Mensagem de credenciais invalidas | Mensagem exibida corretamente | PASS |
| 3 | Login com e-mail nao cadastrado | 1. Informar e-mail inexistente. | Mensagem de credenciais invalidas | Mensagem exibida corretamente | PASS |
| 4 | Logout | 1. Logar. 2. Acessar My Account > Logout. | Sessao encerrada, redirecionamento para pagina de logout | Logout realizado corretamente | PASS |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 4 | 4 | 0 | 100% |