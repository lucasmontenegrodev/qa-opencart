# BUG-002 - Quantidade zero no carrinho remove produto sem confirmacao

| Campo | Valor |
|---|---|
| ID | BUG-002 |
| Test Case | TC-003 - Caso 5 |
| Data | 12/03/2026 |
| Reportado por | Lucas Montenegro |
| Severidade | Media |
| Prioridade | Alta |
| Ambiente | OpenCart local Docker v4.x |
| Status | Aberto |

---

## Descricao

Ao alterar a quantidade de um produto no carrinho para 0 e clicar em "Update", o produto e removido silenciosamente sem nenhuma mensagem de confirmacao ou validacao. O comportamento esperado seria impedir a insercao de quantidade invalida com uma mensagem de erro.

---

## Passos para Reproduzir

1. Acessar http://localhost:8080
2. Adicionar qualquer produto ao carrinho
3. Acessar o carrinho
4. Alterar o campo de quantidade para 0
5. Clicar em "Update"
6. Observar o comportamento

---

## Resultado Esperado

Mensagem de validacao "A quantidade deve ser maior que zero" ou campo impedido de aceitar valores menores que 1.

---

## Resultado Obtido

Produto removido imediatamente do carrinho sem nenhuma mensagem ou confirmacao ao usuario.

---

## Evidencias

```
evidencias/BUG-002/
├── 01-quantidade-alterada-para-zero.png
├── 02-botao-update-clicado.png
└── 03-produto-removido-sem-mensagem.png
```

---

## Impacto

Usuario pode perder itens do carrinho acidentalmente ao tentar alterar a quantidade e digitar 0 por engano. Sem mensagem de feedback, o usuario pode nao entender o que ocorreu.

---

## Hipotese

O controller do carrinho interpreta quantidade 0 como remocao do item. Adicionar validacao no front-end impedindo valores menores que 1, ou no back-end retornar erro com mensagem clara antes de processar a remocao.