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
```

### 6.2 Plano de Monitoramento e Manutenção (*Plan Monitoring and Maintenance*)
Para evitar que o modelo perca precisão ao longo das próximas edições do ENEM, estabelece-se um protocolo anual de governança dividido em três frentes:

- **Monitoramento de *Data Drift* (Desvio nos Dados de Entrada):** Antes de rodar a escoragem em lote (*batch scoring*) de uma nova edição, auditar a distribuição das variáveis críticas (`TP_FAIXA_ETARIA`, `Q006`, proporção de `EGRESSO_FORA_FLUXO` e `REDE_ESCOLAR`) comparando-as com a base de referência de 2023. Variações superiores a **10%** nas proporções disparam alerta de recalibração.
- **Monitoramento de *Concept Drift* (Desvio na Performance):** Após a divulgação oficial dos resultados de presença pelo INEP, auditar o `ROC-AUC` e o `Recall` reais obtidos no ciclo anterior. Caso o `Recall` caia abaixo do piso operacional de **68%**, recalibrar o limiar de corte (`0.48`).
- **Ciclo de Re-treino Anual:** Re-treinar o `HistGradientBoostingClassifier` anualmente incorporando os microdados consolidados da edição mais recente, absorvendo mudanças socioeconômicas e de mobilidade urbana no Distrito Federal.
- **Conformidade Ética e LGPD:** Os escores de risco (`SCORE_ABSTENCAO`) devem ser utilizados **exclusivamente** para políticas públicas afirmativas de engajamento e apoio logístico estudantil, sendo vedado qualquer uso restritivo ou discriminatório.

### 6.3 Relatório Final (*Produce Final Report*)
- **Síntese do Problema:** Predizer a abstenção de candidatos inscritos no ENEM no Distrito Federal (`230.450` registros auditados nas edições `2023`, `2024` e `2025`) utilizando exclusivamente variáveis disponíveis no ato da inscrição.
- **Principais Evidências Empíricas:**
  - A abstenção estrutural no DF oscila entre **29,8% e 31,7%**, com salto sistemático de ~4 pontos percentuais entre o 1.º domingo (Humanas/Linguagens) e o 2.º domingo (Matemática/Natureza).
  - Candidatos **sem vínculo escolar / egressos** (`36%–38%`), de **menor faixa de renda** (`~48%` na Faixa A) e **fora do fluxo regular do Ensino Médio** (`44,1%`) concentram o maior risco de evasão.
- **Resultados do Modelo Campeão (`Gradient Boosting — HistGB`):**
  - **`ROC-AUC`:** `0.7205` (ganho de `+6,83` pontos em relação ao modelo apenas escolar).
  - **`Recall` Operacional (Limiar `0.48`):** `71,29%` (superando a meta técnica de `>= 70%`).
  - **Impacto Projetado no DF (`82.955` inscritos):** Identificação antecipada de **`18.705` potenciais abstentes** e recuperação estimada de **`+1.870` candidatos presentes** sob uma conversão conservadora de `10%` em campanhas focalizadas.

### 6.4 Revisão do Projeto (*Review Project*)
- **O que Funcionou Bem:**
  - A auditoria de qualidade (Subfase 2.4) evitou o descarte indevido de ~70% da base ao identificar os valores nulos escolares como ausência informativa (*MNAR* de egressos).
  - A conversão dos CSVs brutos (`6,25 GB`) para `.parquet` (`25,68 MB`) viabilizou execução rápida, leve e reprodutível na nuvem.
  - A engenharia de atributos (`EGRESSO_FORA_FLUXO` e `RENDA_ORDINAL`) e o ajuste fino do limiar (`0.48`) foram decisivos para atingir os critérios de sucesso.
- **Limitações e Lições Aprendidas:**
  - Por adequação à LGPD a partir de 2024, o INEP desvinculou as tabelas `PARTICIPANTES` e `RESULTADOS`, impedindo o treinamento longitudinal com variáveis socioeconômicas de 2024 e 2025.
  - Os microdados públicos não disponibilizam o CEP residencial exato, limitando o cálculo da distância entre a residência do candidato e o local de aplicação da prova.
- **Trabalhos Futuros:**
  - Em ambiente institucional (SEEDF/INEP) sob termo de confidencialidade, integrar a distância geodésica residência–local de prova e a malha de transporte público para elevar o `ROC-AUC` acima de `0.75`.
