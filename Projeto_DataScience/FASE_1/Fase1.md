## Fase 1: Entendimento do Negócio

### 1.1 Problema e Objetivos de Negócio
O ENEM registra historicamente taxas de abstenção superiores a 25%. No **Distrito Federal**, cada ausência gera desperdício direto de recursos públicos (impressão de provas, alocação de salas e contratação de fiscais) e evidencia barreiras socioeconômicas e de mobilidade urbana.

- **Objetivo Geral:** Identificar, logo após o encerramento das inscrições, candidatos do DF com alta probabilidade de ausência para viabilizar ações preventivas focalizadas.
- **Critérios de Sucesso de Negócio:**
  - Reduzir em pelo menos **10%** a abstenção no grupo classificado como alto risco mediante campanhas de engajamento (SMS/notificações) ou suporte logístico/transporte.
  - Utilizar exclusivamente variáveis disponíveis no ato da inscrição (custo zero de aquisição de novos dados).

### 1.2 Avaliação da Situação

**Recursos disponíveis**
- **Dados:** microdados públicos do ENEM 2023, 2024 e 2025, do Portal de Dados Abertos do INEP (sem custo de aquisição).
- **Ferramentas:** Python com `pandas`, `pyarrow`, `scikit-learn`, `matplotlib` e `seaborn` (ver `requirements.txt`), notebooks Jupyter e execução em nuvem.
- **Versionamento e documentação:** repositório no GitHub, com uma pasta por fase do CRISP-DM.
- **Equipe:** dupla de estudantes (ver 1.4).

**Riscos e contingências**

| Risco | Impacto | Contingência adotada |
| :--- | :--- | :--- |
| Volume dos CSVs brutos (~6,25 GB) inviável para processar de uma vez | Alto | Leitura em lotes de 100.000 linhas, filtro do DF e conversão para Parquet |
| Mudança de esquema do INEP a partir de 2024 (tabelas `PARTICIPANTES` e `RESULTADOS` separadas, sem chave comum, por causa da LGPD) | Alto | Dois conjuntos de modelagem: Dataset A (série escolar 2023–2025) e Dataset B (socioeconômico 2023) |
| Muitos valores ausentes nas variáveis de escola | Médio | Auditoria antes da limpeza para separar erro de ausência informativa |
| Falta de variáveis geográficas finas (CEP residencial) | Médio | Assumido como limitação; registrado para trabalhos futuros |
| Uso indevido dos escores de risco | Alto | Uso restrito a ações de apoio e engajamento, em conformidade com a LGPD |

**Custos e benefícios**
- **Custos:** nenhum gasto com dados (fonte pública e só variáveis da inscrição) e baixo custo de execução (lote anual, sem servidor dedicado). O custo operacional fica nas ações preventivas (SMS, contato e apoio de transporte).
- **Benefícios:** menos provas impressas, salas e fiscais ociosos e mais candidatos presentes. O retorno é estimado por simulação na Fase 5.

### 1.3 Metas Técnicas de Mineração de Dados
- **Enquadramento:** Classificação Binária Supervisionada (`ABSTENCAO`: `1 = Ausente`, `0 = Presente`).
- **Validação Temporal (*Out-of-Time*):** Treinamento e validação com dados do DF de **2023 e 2024**, e teste final na edição de **2025**.
- **Métricas-Alvo:** `ROC-AUC >= 0.75` e `Recall >= 70%` para a classe positiva (priorizando a captura de potenciais desistentes, dado que o custo de um Falso Negativo supera o de um Falso Positivo).

### 1.4 Plano de Projeto

**Responsáveis**
- **Pedro Luiz Oliveira da Costa:** coleta e extração dos microdados, entendimento e preparação dos dados, modelagem, avaliação e notebooks.
- **Henrique Ribeiro Leonardo:** revisão técnica, correção e consolidação da documentação, apresentação final e checklist de entrega.

**Etapas e entregáveis**

| Etapa (CRISP-DM) | Entregável no repositório | Responsável principal |
| :--- | :--- | :--- |
| Fase 1 — Entendimento do Negócio | `FASE_1/Fase1.md` | Pedro e Henrique |
| Fase 2 — Entendimento dos Dados | `FASE_2/Fase2.md`, notebooks 01 e 02 | Pedro |
| Fase 3 — Preparação dos Dados | `FASE_3/Fase3.md`, notebook 03, `docs/DICIONARIO_DADOS.md` | Pedro |
| Fase 4 — Modelagem | `FASE_4/Fase4.md`, notebook de modelagem | Pedro |
| Fase 5 — Avaliação | `FASE_5/Fase5.md`, notebook de avaliação | Pedro |
| Fase 6 — Implementação | `FASE_6/` (plano, relatório, apresentação e revisão) | Pedro e Henrique |

**Prazos (calendário da disciplina)**
- **29/10/2026:** apresentação da metodologia CRISP-DM e início do projeto.
- **04, 11 e 18/11/2026:** aulas de desenvolvimento do projeto, registrado no GitHub.
- **25/11/2026:** entrega da Avaliação A1 (projeto no GitHub e checklist CRISP-DM).
