# TEST-PLAN - QA OpenCart

| Campo | Valor |
|---|---|
| Projeto | qa-opencart |
| Aplicacao | OpenCart (local via Docker) |
| URL | http://localhost:8080 |
| Versao OpenCart | 4.x (Bitnami) |
| Autor | Lucas Montenegro |
| Data | 13/03/2026 |
| Status | Aprovado |

---

## 1. Objetivo

Validar os fluxos principais do frontend da loja OpenCart, garantindo que o cliente consegue buscar produtos, visualizar detalhes, adicionar ao carrinho, se cadastrar e fazer login sem erros.

---

## 2. Escopo

### Dentro do escopo

- Busca de produtos
- Pagina de detalhes do produto
- Adicionar produto ao carrinho
- Alterar quantidade no carrinho
- Remover produto do carrinho
- Cadastro de novo usuario
- Login e logout

### Fora do escopo

- Painel administrativo
- Checkout e pagamento
- Performance e carga
- Testes de seguranca

---

## 3. Tipos de Teste

| Tipo | Ferramenta | Responsavel |
|---|---|---|
| Testes manuais | Chrome + Jira | Lucas Montenegro |
| Automacao E2E | Playwright + POM (JavaScript) | Lucas Montenegro |

---

## 4. Ambiente

| Item | Valor |
|---|---|
| Plataforma | Docker local |
| Browser | Chrome |
| Sistema operacional | Windows 11 |
| URL da loja | http://localhost:8080 |

### Como subir o ambiente

```bash
docker run -d \
  --name opencart \
  -p 8080:8080 \
  -e OPENCART_USERNAME=admin \
  -e OPENCART_PASSWORD=admin1234 \
  bitnami/opencart:latest
```

---

## 5. Criterios de Entrada

- Container Docker rodando e loja acessivel em http://localhost:8080
- Produtos cadastrados na loja
- Casos de teste revisados e aprovados

---

## 6. Criterios de Saida

- 100% dos casos de alta prioridade com PASS
- Nenhum bug critico ou blocker em aberto
- Cobertura minima de 80% dos casos com PASS
- Evidencias coletadas e salvas

---

## 7. Funcionalidades e Prioridades

| Funcionalidade | Prioridade | Tipo |
|---|---|---|
| Busca de produto | Alta | Manual + Automatizado |
| Pagina do produto | Alta | Manual + Automatizado |
| Carrinho | Alta | Manual + Automatizado |
| Cadastro | Alta | Manual + Automatizado |
| Login | Alta | Manual |
| Logout | Media | Manual |

---

## 8. Riscos

| Risco | Probabilidade | Impacto | Mitigacao |
|---|---|---|---|
| Container Docker nao sobe corretamente | Baixa | Alto | Documentar versao exata da imagem utilizada |
| Dados de teste alterados entre execucoes | Media | Medio | Resetar container antes de cada ciclo de testes |
| Seletores CSS mudam entre versoes do OpenCart | Baixa | Alto | Versionar imagem Docker utilizada |

---

## 9. Cronograma

| Atividade | Data |
|---|---|
| Setup do ambiente Docker | 10/03/2026 |
| Escrita dos test cases | 11/03/2026 |
| Execucao dos testes manuais | 12/03/2026 |
| Escrita e execucao da automacao | 13/03/2026 |
| Revisao e fechamento | 14/03/2026 |

---

## 10. Resultado Final

| Total de TCs | PASS | FAIL | Bugs Abertos | Aprovacao |
|---|---|---|---|---|
| 5 | 3 | 2 | 2 | 60% |

Observacao: Os 2 bugs encontrados sao de severidade media e nao bloqueiam o fluxo principal de compra. O fluxo critico (busca, produto, carrinho, cadastro, login) foi coberto integralmente.