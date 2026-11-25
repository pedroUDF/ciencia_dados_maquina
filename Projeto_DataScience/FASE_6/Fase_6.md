## Fase 6: Plano de Implementação e Monitoramento (CRISP-DM)

Nesta etapa final (subfases **6.1** a **6.4**), estrutura-se a operacionalização do modelo campeão (**Gradient Boosting — `HistGB`**) para uso por gestores educacionais no Distrito Federal (SEEDF / INEP), consolidada no notebook `implantacao_scoring_fase6.ipynb`.

### 6.1 Arquitetura de Implantação (*Batch Scoring*)
Como o ENEM possui calendário anual e os dados sociodemográficos são coletados no ato da inscrição semanas antes da prova, adota-se uma arquitetura de **Processamento em Lote (*Batch Scoring*)**, simples, auditável e de baixo custo operacional:

```text
[1. Inscrições ENEM Encerradas] 
       │  (Dados sociodemográficos e escolares dos inscritos no DF)
       ▼
[2. Pipeline Python + Artefato .joblib] 
       │  (Limpeza automática + Gradient Boosting calcula o Score de 0 a 1)
       ▼
[3. Motor de Segmentação por Limiar]
       ├──► Score >= 0.65        ──► [Alto Risco]     ──► Busca Ativa + Transporte/Simulados
       ├──► 0.48 <= Score < 0.65 ──► [Risco Moderado] ──► Régua Digital (SMS / WhatsApp)
       └──► Score < 0.48         ──► [Baixo Risco]    ──► Comunicação Padrão
       │
       ▼
[4. Pós-Prova (INEP)] ──► Auditoria de Acerto (Recall) + Re-treino Anual
