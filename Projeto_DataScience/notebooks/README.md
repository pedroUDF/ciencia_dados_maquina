# Notebooks — Pipeline CRISP-DM (Abstenção ENEM DF | 2023–2025)

Esta pasta reúne os notebooks executáveis do projeto, organizados sequencialmente conforme as etapas da metodologia **CRISP-DM**. Cada notebook documenta o raciocínio analítico, as decisões metodológicas e os códigos reproduzíveis utilizados até a preparação das bases para modelagem.

---

## Mapa dos Notebooks

| Ordem | Arquivo | Fase CRISP-DM | Resumo do Conteúdo |
| :---: | :--- | :--- | :--- |
| **01** | `coleta_extracao_fase1.ipynb` | **Fase 1 & Subfase 2.1** *(Negócio e Coleta)* | Consolida os scripts locais (`inspecionar_pastas.py`, `checar_colunas.py` e `extrair_df_final.py`) de diagnóstico dos CSVs brutos, verificação da mudança de esquema do INEP (2023 vs. 2024–2025) e extração em *chunks* filtrando `SG_UF_PROVA == 'DF'` para formato `.parquet` (25,68 MB). |
| **02** | `entendimento_dados_fase2.ipynb` | **Subfases 2.2, 2.3 & 2.4** *(Entendimento dos Dados)* | Apresenta volumetria e tipagem das bases do DF (230.450 inscritos), gráficos exploratórios (EDA) validando hipóteses de renda, rede escolar e 2.º dia de prova, além da auditoria de qualidade (nulos MNAR, consistência e mobilidade do Entorno). |
| **03** | `preparacao_dados_fase3.ipynb` | **Fase 3** *(Preparação dos Dados)* | Executa a limpeza sem *data leakage*, remoção de eliminados, tratamento de nulos escolares, engenharia de atributos (`ESTUDA_FORA_DF`, `POSSUI_ESCOLA_VINCULADA`, `RENDA_ORDINAL`, etc.) e gera os conjuntos finais de treino e teste (**Dataset A** e **Dataset B**). |
| **04** | `04_modelagem_avaliacao_fase4_5.ipynb` | **Fase 4** *(Modelagem Preditiva)* | Treina e compara Regressão Logística, Random Forest e Gradient Boosting nos Datasets A e B (`ROC-AUC = 0.7205`), gera curvas ROC e identifica os principais atributos preditivos (`TP_FAIXA_ETARIA`, `EGRESSO_FORA_FLUXO`, `RENDA_ORDINAL`). |
| **05** | `05_avaliacao_resultados_fase5.ipynb` | **Fase 5** *(Avaliação)* | Calibra o limiar operacional do modelo campeão (`0.48`, atingindo `Recall = 71,29%`), gera a matriz de confusão, analisa a distribuição de probabilidades e projeta a recuperação de `+1.870` candidatos no DF. |

---

## Fluxo de Execução

1. **Notebook 01:** Referência do pipeline local executado sobre os microdados brutos (`data/raw/`), gerando os arquivos leves em `data/processed/`.
2. **Notebook 02:** Lê os arquivos `.parquet` diretamente do repositório para análise exploratória e diagnóstico de qualidade.
3. **Notebook 03:** Transforma e codifica as variáveis sem vazamento de dados, exportando as matrizes prontas para a **Fase 4 (Modelagem Preditiva)**.
4. **Notebook 04:** Treina os algoritmos candidatos, compara métricas de performance (`ROC-AUC`, `Recall`, `F1`) e analisa a importância das variáveis.
5. **Notebook 05:** Otimiza o limiar de decisão, valida os critérios de sucesso de negócio e simula o impacto operacional no DF.
  
