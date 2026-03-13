# TC-002 - Pagina do Produto

| Campo | Valor |
|---|---|
| ID | TC-002 |
| Funcionalidade | Pagina de Detalhes do Produto |
| Prioridade | Alta |
| Ambiente | http://localhost:8080 |
| Data | 12/03/2026 |
| Status | PASS (5/5) |

---

## Pre-condicoes

- OpenCart rodando localmente via Docker
- Produto "MacBook" disponivel na loja

---

## Casos de Teste

| # | Cenario | Passos | Resultado Esperado | Resultado Real | Status |
|---|---|---|---|---|---|
| 1 | Visualizar detalhes do produto | 1. Buscar "MacBook". 2. Clicar no produto. | Nome, preco, imagem, descricao e botao "Add to Cart" visiveis | Todos os elementos exibidos | PASS |
| 2 | Galeria de imagens | 1. Acessar pagina do produto. 2. Clicar nas imagens miniatura. | Imagem principal atualizada ao clicar nas miniaturas | Imagens atualizadas corretamente | PASS |
| 3 | Alterar quantidade antes de adicionar | 1. Acessar pagina do produto. 2. Alterar quantidade para 2. 3. Clicar em "Add to Cart". | Produto adicionado com quantidade 2 | Quantidade respeitada | PASS |
| 4 | Adicionar produto sem estoque | 1. Acessar produto sem estoque. | Botao "Add to Cart" desabilitado ou mensagem de indisponibilidade | Produto exibe "Out of Stock" e botao desabilitado | PASS |
| 5 | Exibicao do preco com e sem desconto | 1. Acessar produto com preco promocional. | Preco original riscado e preco promocional destacado | Precos exibidos corretamente | PASS |

---

## Resumo

| Total | PASS | FAIL | Aprovacao |
|---|---|---|---|
| 5 | 5 | 0 | 100% |