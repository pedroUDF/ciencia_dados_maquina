### **1. Determinar os Objetivos de Negócio e Critérios de Sucesso**

- **Contexto e Dor de Negócio:** O Exame Nacional do Ensino Médio (ENEM) registra historicamente taxas de abstenção entre 25% e 30%. No **Distrito Federal (DF)**, cada candidato ausente representa um desperdício direto de recursos públicos (impressão de cadernos de prova, alocação de salas na rede pública/privada e pagamento de fiscais locais), além de sinalizar barreiras socioeconômicas ou de mobilidade urbana (como deslocamentos entre Regiões Administrativas) que impedem o acesso ao ensino superior.
- **Objetivo Geral de Negócio:** Identificar, logo após o encerramento das inscrições e antes da aplicação das provas no **Distrito Federal**, os candidatos com alta probabilidade de desistência (abstenção), permitindo ações preventivas.
- **Objetivos Específicos:**
  - Mapear os principais fatores socioeconômicos, demográficos e de deslocamento intraestadual associados à ausência nos dias de prova no DF entre **2023 e 2025**.
  - Fornecer subsídios para que o INEP e a Secretaria de Estado de Educação do DF (SEEDF) direcionem campanhas de engajamento ou otimizem a alocação de locais de exame.
- **Critérios de Sucesso de Negócio (Impacto Real):**
  - Reduzir a taxa de abstenção no DF em **pelo menos 10%** no grupo de candidatos classificados como "alto risco" que receberem ações de engajamento ou suporte logístico.
  - Gerar um ranking acionável de perfis vulneráveis no DF sem exigir a coleta de novos dados além do formulário de inscrição já existente.

### **2. Avaliar a Situação (Recursos, Riscos e Custo-Benefício)**

- **Inventário de Recursos:**
  - **Dados:** Microdados públicos oficiais do INEP referentes às edições de **2023, 2024 e 2025**, filtrados exclusivamente para os candidatos com local de prova no **Distrito Federal (`SG_UF_PROVA == 'DF'`)**, contendo variáveis demográficas, escolares, geográficas e questionário socioeconômico (Q001 a Q025), além dos registros de presença (`TP_PRESENCA_*`).
  - **Ferramentas e Hardware:** Ambiente de desenvolvimento em Python (Pandas, Scikit-learn, LightGBM/XGBoost) executado em máquina local / Google Colab.
- **Delimitação de Escopo e Justificativa:**
  - A restrição ao **DF** garante viabilidade computacional (reduzindo milhões de registros nacionais para uma amostra local de dezenas de milhares de inscritos por ano, sem perda de profundidade histórica nos 3 anos) e homogeneidade regional nas condições socioeconômicas e de transporte.
- **Análise de Riscos e Contingências:**
  - **Leitura inicial de arquivos brutos (Risco Computacional):** Os arquivos CSV originais do INEP vêm consolidados em nível nacional (arquivos de ~1,5 GB a 2 GB por ano). *Contingência:* Aplicar leitura em lotes (*chunks* no Pandas) filtrando imediatamente `SG_UF_PROVA == 'DF'` antes de armazenar os dados em memória.
  - **Mudanças de esquema entre anos (Risco de Consistência):** O dicionário de dados do INEP pode sofrer alterações pontuais de nomenclatura ou faixas entre 2023 e 2025. *Contingência:* Padronizar os esquemas antes de concatenar as quatro edições.
  - **Vazamento de Dados (*Data Leakage*):** Utilizar variáveis pós-prova (como notas ou status da redação) invalida o modelo preditivo. *Contingência:* Restringir estritamente as *features* às informações disponíveis no ato da inscrição.
- **Análise de Custo-Benefício:**
  - Como os dados são públicos, gratuitos e já coletados no ato da inscrição, o custo de aquisição é zero. Em contrapartida, o custo de um **Falso Negativo** (não identificar um candidato do DF que vai faltar) é a perda da oportunidade de intervir, enquanto o custo de um **Falso Positivo** (enviar um lembrete ou oferecer auxílio a alguém que já iria fazer a prova) é baixíssimo.

### **3. Determinar Metas Técnicas de Mineração de Dados**

- **Enquadramento Técnico:** Problema de **Aprendizagem Supervisionada — Classificação Binária**.
- **Definição da Variável Alvo (*Target*):** Criação da variável `ABSTENCAO` para os inscritos do DF, onde `1` representa o candidato ausente e `0` representa o candidato presente.
- **Estratégia Temporal (Treino vs. Teste):** Utilizar o histórico do DF de **2023 e 2024** para treinamento e validação cruzada, e reservar a edição de **2025 (DF)** como conjunto de teste fora do tempo (*out-of-time*), simulando o cenário real de prever uma edição futura a partir de anos anteriores.
- **Critérios de Sucesso Técnico:**
  - Atingir **ROC-AUC $\geq 0,75$** no conjunto de teste do DF (2025).
  - Priorizar o **Recall (Sensibilidade) $\geq 70\%$** para a classe positiva (`ABSTENCAO = 1`), garantindo que a maioria dos potenciais desistentes do DF seja capturada, mantendo uma **Precisão** aceitável para não pulverizar recursos de intervenção.
  - Extrair a interpretabilidade do modelo (*Feature Importance* / SHAP) para explicar quais variáveis mais impulsionam a desistência no Distrito Federal.

### **4. Produzir o Plano de Projeto**

| Fase CRISP-DM | Atividades Principais (Escopo DF 2023–2025) | Entregável / Marco |
| :--- | :--- | :--- |
| **1. Entendimento do Negócio** | Definição do problema no DF, critérios de negócio/técnicos, análise de riscos e plano de projeto. | Documento da Fase 1 |
| **2. Entendimento dos Dados** | Leitura dos dicionários (2023–2025), análise de volumetria no DF, taxa histórica de abstenção por ano e verificação de nulos/inconsistências. | Relatório de Exploração Inicial (EDA) |
| **3. Preparação dos Dados** | Filtragem (`SG_UF_PROVA == 'DF'`), remoção de variáveis pós-prova (*leakage*), engenharia de atributos e integração dos 4 anos. | Dataset unificado e limpo do DF (`.parquet`/`.csv`) |
| **4. Modelagem** | Treinamento de baseline (Regressão Logística) e modelos baseados em árvores (Random Forest, LightGBM) com dados do DF de 2023–2024. | Modelos treinados e tunados |
| **5. Avaliação** | Teste na base do DF de 2025, análise de matriz de confusão, *Feature Importance* e verificação frente aos critérios de negócio da Fase 1. | Relatório de Avaliação de Impacto |
| **6. Implementação** | Proposta de arquitetura para escoragem pós-inscrição no DF, plano de monitoramento de *drift* anual e apresentação final. | Apresentação e Código Final |
