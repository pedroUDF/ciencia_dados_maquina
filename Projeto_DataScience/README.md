Metodologia: https://www.ibm.com/docs/pt-br/SS3RA7_18.5.0/nl/pt/BR/pdf/ModelerCRISPDM.pdf 

# Predição de Abstenção no ENEM (Distrito Federal | 2023–2025)

Projeto de Ciência de Dados e Aprendizagem de Máquina estruturado sob a metodologia **CRISP-DM** (*Cross-Industry Standard Process for Data Mining*), com o objetivo de prever a probabilidade de abstenção de candidatos inscritos no Exame Nacional do Ensino Médio (ENEM) no **Distrito Federal (DF)**.

- **Disciplina:** Ciência de Dados e Aprendizagem de Máquina | IA
- **Docente:** Profa. Kadidja Valéria
- **Status Atual:** Fase 2 concluída até a Subfase 2.2 (Descrição de Quantidade e Qualidade)

---

## Status do Ciclo CRISP-DM

- [x] **Fase 1:** Entendimento do Negócio
- [x] **Fase 2.1:** Coleta de Dados Iniciais e Extração do Escopo (DF)
- [x] **Fase 2.2:** Descrição de Quantidade, Tipagem e Qualidade dos Dados
- [ ] **Fase 2.3:** Análise Exploratória de Dados (EDA) e Validação de Hipóteses
- [ ] **Fase 2.4:** Auditoria de Qualidade (Nulos, Anomalias e Inconsistências)
- [ ] **Fase 3:** Preparação dos Dados (Limpeza, Engenharia de Atributos e Integração)
- [ ] **Fase 4:** Modelagem Preditiva
- [ ] **Fase 5:** Avaliação (Métricas Técnicas vs. Critérios de Negócio)
- [ ] **Fase 6:** Plano de Implementação e Monitoramento

---

## Fase 1: Entendimento do Negócio

### 1.1 Problema e Objetivos de Negócio
O ENEM registra historicamente taxas de abstenção superiores a 25%. No **Distrito Federal**, cada ausência gera desperdício direto de recursos públicos (impressão de provas, alocação de salas e contratação de fiscais) e evidencia barreiras socioeconômicas e de mobilidade urbana.

- **Objetivo Geral:** Identificar, logo após o encerramento das inscrições, candidatos do DF com alta probabilidade de ausência para viabilizar ações preventivas focalizadas.
- **Critérios de Sucesso de Negócio:**
  - Reduzir em pelo menos **10%** a abstenção no grupo classificado como alto risco mediante campanhas de engajamento (SMS/notificações) ou suporte logístico/transporte.
  - Utilizar exclusivamente variáveis disponíveis no ato da inscrição (custo zero de aquisição de novos dados).

### 1.2 Metas Técnicas
- **Enquadramento:** Classificação Binária Supervisionada (`ABSTENCAO`: `1 = Ausente`, `0 = Presente`).
- **Validação Temporal (*Out-of-Time*):** Treinamento e validação com dados do DF de **2023 e 2024**, e teste final na edição de **2025**.
- **Métricas-Alvo:** `ROC-AUC >= 0.75` e `Recall >= 70%` para a classe positiva (priorizando a captura de potenciais desistentes, dado que o custo de um Falso Negativo supera o de um Falso Positivo).

---

## Fase 2: Entendimento dos Dados

### 2.1 Coleta Inicial e Extração do Recorte (DF)
Os microdados oficiais foram obtidos no Portal de Dados Abertos do **INEP** (edições 2023, 2024 e 2025). Devido ao volume nacional (~4 a 4,8 milhões de linhas por edição), os arquivos CSV originais foram processados localmente em lotes (*chunks* de 100.000 linhas) filtrando `SG_UF_PROVA == 'DF'` e convertidos para o formato colunar `.parquet` (totalizando **25,68 MB**):

| Base Extraída | Total Brasil | Total DF | Participação DF (%) | Colunas | Tamanho `.parquet` |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2023_completo` | 3.933.955 | 72.975 | 1,86% | 76 | 7,62 MB |
| `2024_participantes` | 4.332.944 | 74.520 | 1,72% | 38 | 1,11 MB |
| `2024_resultados` | 4.332.944 | 74.520 | 1,72% | 42 | 7,19 MB |
| `2025_participantes` | 4.810.772 | 82.955 | 1,72% | 38 | 1,23 MB |
| `2025_resultados` | 4.810.772 | 82.955 | 1,72% | 70 | 8,53 MB |
| **Total Consolidado (DF)** | **13.077.671** | **230.450** | **1,76%** | — | **25,68 MB** |

### 2.2 Descrição de Quantidade, Tipagem e Qualidade
Durante a inspeção estrutural dos esquemas do INEP, identificou-se uma mudança metodológica relevante a partir de 2024:
- **2023:** Tabela única (`76 colunas`: `37 object`, `21 float64`, `18 int64`) unindo dados socioeconômicos (`Q001`–`Q025`) e presença (`TP_PRESENCA_*`).
- **2024 e 2025:** Por adequação à LGPD/anonimização, o INEP separou os dados em duas tabelas sem chave primária comum: `PARTICIPANTES` (perfil demográfico e socioeconômico) e `RESULTADOS` (dados da escola, município de prova, língua estrangeira, notas e presença).

#### Comportamento das Variáveis de Presença no DF (`TP_PRESENCA_CH` e `TP_PRESENCA_MT`)
As colunas de presença não possuem valores nulos (`NaN`) em nenhuma edição e revelam um padrão consistente de **evasão entre o 1º e o 2º domingo**:

| Edição | Inscritos DF | Faltas Dia 1 (CH/LC) | Taxa Abstenção Dia 1 | Faltas Dia 2 (MT/CN) | Taxa Abstenção Dia 2 | Eliminados (Dia 1 / Dia 2) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **2023** | 72.975 | 19.725 | **27,03%** | 22.403 | **30,70%** | 81 / 39 |
| **2024** | 74.520 | 18.927 | **25,40%** | 22.002 | **29,52%** | 108 / 49 |
| **2025** | 82.955 | 22.198 | **26,76%** | 25.955 | **31,29%** | 84 / 42 |

---

## Como Reproduzir

1. Baixe os microdados do ENEM (2023–2025) no portal do INEP e extraia-os em `data/raw/`.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
