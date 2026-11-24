# Notebooks — Pipeline CRISP-DM (Abstenção ENEM DF | 2023–2025)

Esta pasta reúne os notebooks executáveis do projeto, organizados sequencialmente conforme as etapas da metodologia **CRISP-DM**. Cada notebook documenta o raciocínio analítico, as decisões metodológicas e os códigos reproduzíveis utilizados até a preparação das bases para modelagem.

---

## Mapa dos Notebooks

| Ordem | Arquivo | Fase CRISP-DM | Resumo do Conteúdo |
| :---: | :--- | :--- | :--- |
| **01** | `01_coleta_extracao_fase1_2.ipynb` | **Fase 1 & Subfase 2.1** *(Negócio e Coleta)* | Consolida os scripts de diagnóstico de arquivos brutos, verificação de mudança de esquema do INEP (2023 vs. 2024–2025) e extração em *chunks* filtrando `SG_UF_PROVA == 'DF'` para formato `.parquet` (25,68 MB). |
| **02** | `02_entendimento_dados_fase2.ipynb` | **Subfases 2.2, 2.3 & 2.4** *(Entendimento dos Dados)* | Apresenta volumetria e tipagem das bases do DF (230.450 inscritos), gráficos exploratórios (EDA) validando hipóteses de renda, rede escolar e 2.º dia de prova, além da auditoria de qualidade (nulos MNAR e consistência). |
| **03** | `03_preparacao_dados_fase3.ipynb` | **Fase 3** *(Preparação dos Dados)* | Executa a limpeza sem *data leakage*, remoção de eliminados, tratamento de nulos escolares, engenharia de atributos (`ESTUDA_FORA_DF`, `RENDA_ORDINAL`, etc.) e gera os conjuntos de treino e teste (**Dataset A** e **Dataset B**). |
