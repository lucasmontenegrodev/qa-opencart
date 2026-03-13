# TC-003 - Carrinho

| Campo | Valor |
|---|---|
| ID | TC-003 |
| Funcionalidade | Carrinho de Compras |
| Prioridade | Alta |
| Ambiente | http://localhost:8080 |
| Data | 12/03/2026 |
| Status | FAIL (4/5 - 1 falhou) |

---

## Pre-condicoes

- OpenCart rodando localmente via Docker
- Usuario logado ou anonimo com produto disponivel

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Adicionar produto ao carrinho | 1. Acessar pagina do produto. 2. Clicar em "Add to Cart". | Notificacao de sucesso exibida, contador do carrinho atualizado | Produto adicionado corretamente | PASS |
| 2 | Visualizar carrinho | 1. Adicionar produto. 2. Clicar no icone do carrinho. | Produto listado com nome, quantidade, preco unitario e total | Carrinho exibido corretamente | PASS |
| 3 | Remover produto do carrinho | 1. Acessar carrinho. 2. Clicar no botao de remover. | Produto removido, total atualizado | Produto removido corretamente | PASS |
| 4 | Alterar quantidade no carrinho | 1. Acessar carrinho. 2. Alterar quantidade para 3. 3. Clicar em "Update". | Quantidade e total atualizados corretamente | Quantidade atualizada corretamente | PASS |
| 5 | Inserir quantidade zero ou negativa | 1. Acessar carrinho. 2. Alterar quantidade para 0. 3. Clicar em "Update". | Exibir validacao impedindo quantidade invalida | Produto removido silenciosamente sem mensagem ao usuario | FAIL |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 5 | 4 | 1 | 80% |

---

## Bug gerado: BUG-002