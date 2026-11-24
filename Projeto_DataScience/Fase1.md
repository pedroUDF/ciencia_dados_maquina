## Fase 1: Entendimento do Negócio

### 1.1 Problema e Objetivos de Negócio
O ENEM registra historicamente taxas de abstenção superiores a 25%. No **Distrito Federal**, cada ausência gera desperdício direto de recursos públicos (impressão de provas, alocação de salas e contratação de fiscais) e evidencia barreiras socioeconômicas e de mobilidade urbana.

- **Objetivo Geral:** Identificar, logo após o encerramento das inscrições, candidatos do DF com alta probabilidade de ausência para viabilizar ações preventivas focalizadas.
- **Critérios de Sucesso de Negócio:**
  - Reduzir em pelo menos **10%** a abstenção no grupo classificado como alto risco mediante campanhas de engajamento (SMS/notificações) ou suporte logístico/transporte.
  - Utilizar exclusivamente variáveis disponíveis no ato da inscrição (custo zero de aquisição de novos dados).

### 1.2 Metas
- **Enquadramento:** Classificação Binária Supervisionada (`ABSTENCAO`: `1 = Ausente`, `0 = Presente`).
- **Validação Temporal (*Out-of-Time*):** Treinamento e validação com dados do DF de **2023 e 2024**, e teste final na edição de **2025**.
- **Métricas-Alvo:** `ROC-AUC >= 0.75` e `Recall >= 70%` para a classe positiva (priorizando a captura de potenciais desistentes, dado que o custo de um Falso Negativo supera o de um Falso Positivo).
