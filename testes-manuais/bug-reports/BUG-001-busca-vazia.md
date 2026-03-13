# BUG-001 - Busca com campo vazio nao exibe mensagem clara ao usuario

| Campo | Valor |
|---|---|
| ID | BUG-001 |
| Test Case | TC-001 - Caso 4 |
| Data | 12/03/2026 |
| Reportado por | Lucas Montenegro |
| Severidade | Baixa |
| Prioridade | Media |
| Ambiente | OpenCart local Docker v4.x |
| Status | Aberto |

---

## Descricao

Ao clicar no botao de busca sem digitar nenhum termo, o sistema redireciona o usuario para a pagina de resultados de busca sem exibir nenhuma mensagem orientando o usuario. A pagina exibe todos os produtos sem filtro, o que pode confundir o usuario.

---

## Passos para Reproduzir

1. Acessar http://localhost:8080
2. Deixar o campo de busca vazio
3. Clicar no icone de busca (lupa)
4. Observar o resultado

---

## Resultado Esperado

Exibir mensagem de validacao "Digite um termo para buscar" ou impedir o envio do formulario vazio.

---

## Resultado Obtido

Usuario redirecionado para pagina de busca sem mensagem. Todos os produtos sao listados sem nenhuma indicacao de que a busca esta vazia.

---

## Evidencias

```
evidencias/BUG-001/
├── 01-campo-busca-vazio.png
├── 02-redirecionamento-sem-mensagem.png
└── 03-todos-produtos-listados.png
```

---

## Impacto

Experiencia confusa para o usuario. Sem mensagem de orientacao, o usuario pode nao entender o que aconteceu.

---

## Hipotese

O formulario de busca nao possui validacao client-side para campo vazio. Adicionar validacao no front-end antes do submit ou tratamento no controller de busca.