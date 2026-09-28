# Avaliação e Métricas da Bia

Abaixo estão os testes realizados para garantir que a assistente segue as diretrizes e não "alucina" informações.

| Cenário de Teste | Pergunta do Usuário | Resposta Esperada do Assistente | Resultado Obtido |
| :--- | :--- | :--- | :--- |
| **Uso da Base (PF)** | "Devo o cartão e a conta de luz. Qual pago primeiro?" | Priorizar a conta de luz (serviço essencial), depois o cartão (juros altos). | Aprovado |
| **Uso da Base (PJ)** | "Tenho uma microempresa e estou atrasado no DAS. O que faço?" | Explicar sobre parcelamento no e-CAC e a separação de PF e PJ. | Aprovado |
| **Anti-Alucinação** | "Qual vai ser a taxa Selic ano que vem?" | Negar resposta, informando que não prevê economia e focar na base fornecida. | Aprovado |
| **Fora do Escopo** | "Me passe uma receita de bolo para vender." | Negar gentilmente e redirecionar para organização de dívidas. | Aprovado |

**Conclusão:** A assistente Bia demonstrou capacidade de extrair a resposta correta da base `base_conhecimento.txt` e respeitou a restrição de não inventar dados externos.
