## Fase 5: Avaliação (Técnica vs. Critérios de Negócio)

Nesta etapa o modelo campeão (**Gradient Boosting — `HistGB`** no Dataset B) foi calibrado e avaliado sob a ótica operacional e financeira do Distrito Federal.

### Otimização do Limiar de Decisão (*Threshold Tuning*)

| Limiar (`Threshold`) | ROC-AUC | Recall (%) | Precision (%) | F1-Score | Base Acionada (%) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `0.55` | `0.7205` | 63,94% | **47,87%** | 0.5475 | 41,42% |
| `0.50` *(Padrão)* | `0.7205` | 69,59% | 46,23% | 0.5555 | 46,67% |
| **`0.48` *(Operacional)*** | **`0.7205`** | **`71,29%`** | `45,51%` | `0.5555` | `48,58%` |
| `0.45` | `0.7205` | 74,81% | 44,50% | **0.5581** | 52,12% |
| `0.42` | `0.7205` | 78,44% | 43,24% | 0.5575 | 56,25% |

- **Decisão Operacional (`Limiar = 0.48`):** Atinge **`Recall = 71,29%`**, superando a meta técnica definida na Fase 1 (`>= 70%`) sem elevar excessivamente o volume de acionamentos.
- **Matriz de Confusão (Base de Teste — `14.571` registros):** `3.221` Verdadeiros Positivos, `6.196` Verdadeiros Negativos, `3.857` Falsos Positivos e `1.297` Falsos Negativos.

### Simulação de Impacto de Negócio (Cenário DF — 82.955 Inscritos)
- **Abstentes estimados sem intervenção:** `26.238` candidatos (`31,63%`).
- **Abstentes identificados antecipadamente (`Recall 71,3%`):** `18.705` candidatos sinalizados logo após o encerramento das inscrições.
- **Retorno esperado:** Com uma ação focalizada de baixo custo (lembretes por SMS/WhatsApp e orientação de transporte) atingindo **10% de conversão** no público de risco, estima-se recuperar **+1.870 candidatos presentes** no exame, mitigando o desperdício de cadernos de prova e infraestrutura de aplicação.

### Revisão Crítica e Limitações
- O `ROC-AUC` de `0.7205` demonstra sólido poder discriminatório considerando exclusivamente dados autodeclarados na inscrição, ficando ligeiramente abaixo do teto idealizado (`0.75`) devido à ausência nos microdados públicos de variáveis geoespaciais finas (distância real entre CEP residencial e local de prova) por restrições da LGPD.
