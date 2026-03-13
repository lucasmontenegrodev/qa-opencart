# TC-001 - Busca de Produto

| Campo | Valor |
|---|---|
| ID | TC-001 |
| Funcionalidade | Busca de Produto |
| Prioridade | Alta |
| Ambiente | http://localhost:8080 |
| Data | 12/03/2026 |
| Status | FAIL (4/5 - 1 falhou) |

---

## Pre-condicoes

- OpenCart rodando localmente via Docker
- Pelo menos 3 produtos cadastrados na loja

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Busca por termo valido | 1. Acessar http://localhost:8080. 2. Digitar "MacBook" no campo de busca. 3. Pressionar Enter. | Produtos relacionados exibidos com imagem, nome e preco | Produtos exibidos corretamente | PASS |
| 2 | Busca por termo parcial | 1. Digitar "Mac" no campo de busca. 2. Pressionar Enter. | Produtos cujo nome contenha "Mac" exibidos | Produtos exibidos corretamente | PASS |
| 3 | Busca sem resultado | 1. Digitar "produtoinexistente123" no campo de busca. 2. Pressionar Enter. | Mensagem "There is no product that matches the search criteria" | Mensagem exibida corretamente | PASS |
| 4 | Busca com campo vazio | 1. Clicar no botao de busca sem digitar nada. | Exibir validacao ou redirecionar para pagina com todos os produtos | Redireciona para pagina de busca sem mensagem clara ao usuario | FAIL |
| 5 | Busca case insensitive | 1. Digitar "macbook" em minusculo. 2. Pressionar Enter. | Mesmos resultados da busca com "MacBook" | Resultados identicos | PASS |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 5 | 4 | 1 | 80% |

---

## Bug gerado: BUG-001