## Fase 4: Modelagem Preditiva

Nesta etapa, foram treinados e comparados três algoritmos de classificação supervisionada — **Regressão Logística** (*baseline* linear), **Random Forest** (*bagging*) e **Gradient Boosting (`HistGradientBoostingClassifier`)** — utilizando `class_weight="balanced"` para compensar o desbalanceamento entre presentes (~69%) e abstentes (~31%).

### Resultados Comparativos dos Modelos

| Cenário | Modelo | ROC-AUC | Recall (%) | Precision (%) | F1-Score | Acurácia (%) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Dataset A** *(Série 2023–2025 \| Teste OOT 2025)* | Regressão Logística (*Baseline*) | `0.6522` | **85,73%** | 38,66% | 0.5329 | 52,47% |
| **Dataset A** *(Série 2023–2025 \| Teste OOT 2025)* | Random Forest | `0.6521` | 85,69% | 38,66% | 0.5328 | 52,48% |
| **Dataset A** *(Série 2023–2025 \| Teste OOT 2025)* | Gradient Boosting (`HistGB`) | `0.6522` | 85,70% | 38,67% | 0.5329 | 52,49% |
| **Dataset B** *(Socioeconômico 2023 \| Teste 20%)* | Regressão Logística (*Baseline*) | `0.7137` | 66,95% | **46,46%** | 0.5486 | **65,83%** |
| **Dataset B** *(Socioeconômico 2023 \| Teste 20%)* | Random Forest | `0.7195` | **70,81%** | 45,80% | **0.5563** | 64,97% |
| **Dataset B** *(Socioeconômico 2023 \| Teste 20%)* | **Gradient Boosting (`HistGB`)** | **`0.7205`** | 69,59% | 46,23% | 0.5555 | 65,47% |

### Principais Achados da Modelagem
- **Impacto das Variáveis Socioeconômicas:** A inclusão do perfil sociofamiliar e demográfico (**Dataset B**) elevou a capacidade discriminatória (`ROC-AUC`) de **`0.6522`** para **`0.7205`** (+6,83 pontos), comprovando que dados puramente escolares capturam parte relevante da evasão, mas o contexto socioeconômico é determinante para ranquear o risco individual.
- **Atributos Mais Relevantes:** A análise de importância relativa (*Gini Importance*) apontou **`TP_FAIXA_ETARIA`** (~29%) como principal preditor, seguida pelas variáveis criadas na Fase 3 **`EGRESSO_FORA_FLUXO`** (~10%) e **`RENDA_ORDINAL`** (~9%).
- **Seleção para a Fase 5:** O **`Gradient Boosting (HistGB)`** obteve a maior área sob a curva ROC (`0.7205`), avançando para a etapa de **Avaliação** para ajuste fino do limiar de decisão (*threshold tuning*) visando superar a meta operacional de `Recall >= 70%`.
