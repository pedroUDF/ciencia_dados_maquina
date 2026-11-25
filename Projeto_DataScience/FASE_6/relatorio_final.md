# Relatório Final — Predição de Abstenção no ENEM no Distrito Federal (2023–2025)

**Metodologia:** CRISP-DM (*Cross-Industry Standard Process for Data Mining*)  
**Escopo Geográfico e Temporal:** Distrito Federal (`SG_UF_PROVA == 'DF'`) | Edições 2023, 2024 e 2025  
**Modelo Campeão:** Gradient Boosting (`HistGradientBoostingClassifier`)  

---

## 1. Resumo Executivo

Este projeto desenvolveu uma solução completa de Ciência de Dados e Aprendizado de Máquina para identificar, logo após o encerramento das inscrições, candidatos com elevado risco de abstenção no Exame Nacional do Ensino Médio (ENEM) no Distrito Federal.

A partir da extração e auditoria de **230.450 inscrições no DF** (filtradas de um universo nacional de 13,07 milhões de registros do INEP), o modelo campeão baseado em **Gradient Boosting** atingiu **`ROC-AUC = 0.7205`** e **`Recall = 71,29%`** no ponto de corte operacional (`0.48`). Em uma projeção realista para a volumetria do DF (**82.955 inscritos** e **31,63%** de abstenção), o sistema identifica antecipadamente **18.705 potenciais abstentes**, permitindo que ações focalizadas de engajamento e apoio logístico com taxa conservadora de **10% de conversão** recuperem **+1.870 candidatos presentes** no exame.

---

## 2. Contextualização e Objetivos (Fase 1)

* **Problema de Negócio:** A abstenção recorrente de aproximadamente um terço dos inscritos no DF gera desperdício direto de recursos públicos (impressão de cadernos de prova, logística de transporte e alocação de fiscais/salas ociosas), além de representar perda de oportunidade educacional.
* **Critérios de Sucesso Definidos:**
  * *Técnicos:* Alcançar `ROC-AUC >= 0.75` (ou desempenho próximo restrito aos dados autodeclarados) e `Recall >= 70%` para a classe minoritária (abstentes).
  * *Negócio:* Viabilizar a redução de pelo menos **10%** na abstenção dentro do grupo de alto risco por meio de intervenções preventivas de baixo custo.

---

## 3. Evidências dos Dados e Preparação (Fases 2 e 3)

### 3.1 Panorama Histórico no Distrito Federal (2023–2025)

| Edição | Total Inscritos (DF) | Eliminados Removidos | Base Válida Analisada | Taxa de Abstenção Geral | Abstenção 1.º Dia (CH) | Abstenção 2.º Dia (MT) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **2023** | 72.975 | 120 | 72.855 | **31,00%** | 27,03% | 30,70% |
| **2024** | 74.520 | 157 | 74.363 | **29,78%** | 25,40% | 29,52% |
| **2025** | 82.955 | 126 | 82.829 | **31,63%** | 26,76% | 31,29% |
| **Total** | **230.450** | **403** | **230.047** | **30,83%** | **26,40%** | **30,53%** |

### 3.2 Principais Achados Exploratórios e Engenharia de Atributos
* **Impacto do Vínculo Escolar:** Estudantes regulares do 3.º ano apresentam abstenção média de ~20%, enquanto **egressos sem vínculo escolar** (`~70%` da base, inicialmente identificados com valores nulos *MNAR* nas colunas de escola) atingem **36% a 38%** de ausência.
* **Efeito Socioeconômico:** A taxa de abstenção cai de **~48%** na menor faixa de renda (`Faixa A`) para **~12%** nas faixas superiores (`Faixas P–Q`).
* **Atributos Criados (Sem *Data Leakage*):** Construção de indicadores comportamentais e estruturais como `EGRESSO_FORA_FLUXO`, `POSSUI_ESCOLA_VINCULADA`, `ESTUDA_FORA_DF` (mobilidade do Entorno GO $\rightarrow$ DF), `RENDA_ORDINAL`, `ESC_PAI_ORDINAL` e `ESC_MAE_ORDINAL`.

---

## 4. Modelagem Preditiva e Avaliação Operacional (Fases 4 e 5)

### 4.1 Comparativo de Algoritmos (Base de Teste — Dataset B Socioeconômico)

| Modelo Avaliado | Dataset | ROC-AUC | Recall (Corte 0.50) | Precision | F1-Score |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Regressão Logística *(Baseline Escolar)* | Dataset A | 0.6522 | 85,73% | 38,66% | 0.5329 |
| Regressão Logística *(Socioeconômico)* | Dataset B | 0.7137 | 66,95% | 46,46% | 0.5486 |
| Random Forest | Dataset B | 0.7195 | 70,81% | 45,80% | 0.5563 |
| **Gradient Boosting (`HistGB` — Campeão)** | **Dataset B** | **0.7205** | **69,59%** | **46,23%** | **0.5555** |

* **Ganho Informacional:** A inclusão das variáveis socioeconômicas elevou o `ROC-AUC` em **+6,83 pontos** (`0.6522` $\rightarrow$ `0.7205`), confirmando que idade (`TP_FAIXA_ETARIA`), condição de egresso (`EGRESSO_FORA_FLUXO`) e renda (`RENDA_ORDINAL`) são os principais determinantes da evasão.

### 4.2 Calibração de Limiar e Impacto no DF (`Limiar Operacional = 0.48`)
* **Métricas no Ponto de Operação:** Ao ajustar o corte de probabilidade de `0.50` para **`0.48`**, o modelo campeão alcançou **`Recall = 71,29%`**, `Precision = 45,51%` e `F1-Score = 0.5555`, acionando `48,58%` da base.
* **Matriz de Confusão (Teste — 14.571 registros):** `3.221` Verdadeiros Positivos (abstentes capturados), `6.196` Verdadeiros Negativos, `3.857` Falsos Positivos e `1.297` Falsos Negativos.
* **Simulação de Retorno (Cenário DF — 82.955 inscritos):** Dos `26.238` abstentes esperados, `18.705` são sinalizados antecipadamente. Uma ação focalizada de baixo custo com **10% de conversão** recupera **`+1.870` candidatos presentes** no exame.

---

## 5. Implantação, Limitações e Recomendações (Fase 6)

* **Operacionalização (*Batch Scoring*):** O modelo campeão foi serializado em **`models/modelo_abstencao_enem_df.joblib`** para execução em lote imediatamente após o fim das inscrições, segmentando os candidatos em **Alto Risco** (`score >= 0.65` $\rightarrow$ busca ativa e divulgação de passe livre estudantil), **Risco Moderado** (`0.48 <= score < 0.65` $\rightarrow$ régua digital SMS/WhatsApp) e **Baixo Risco** (`score < 0.48`).
* **Limitações Identificadas:** A adequação do INEP à LGPD a partir de 2024 desvinculou os microdados de `PARTICIPANTES` e `RESULTADOS` e omitiu o CEP residencial exato, impedindo o cálculo da distância entre a residência do candidato e o local de prova.
* **Recomendações Futuras:** Em ambiente institucional (SEEDF/INEP) sob termo de sigilo, incorporar a distância geodésica residência–local de prova e a malha de transporte público para elevar o `ROC-AUC` acima de `0.75`, mantendo o ciclo de re-treino anual e monitoramento de *data drift*.
* **Automação de Painel (BI):** Conectar a saída do pipeline de *batch scoring* a um painel gerencial por Região Administrativa (RA) do DF para acompanhamento em tempo real pelas equipes pedagógicas.
