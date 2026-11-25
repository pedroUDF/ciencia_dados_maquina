# Entregáveis da Fase 6: Implementação e Monitoramento (CRISP-DM)

Esta seção detalha os artefatos concretos produzidos na **Fase 6 (*Deployment*)** do projeto, responsáveis por transformar o modelo estatístico validado em uma solução operacional pronta para uso por gestores educacionais no Distrito Federal.

---

## Mapa dos Entregáveis da Fase 6

| Subfase CRISP-DM | Entregável | Localização no Repositório | Descrição e Finalidade Operacional |
| :---: | :--- | :--- | :--- |
| **6.1** *(Implantação)* | **Modelo Serializado (`.joblib`)** | **`models/modelo_abstencao_enem_df.joblib`** *(salvo na pasta `models/` e gerado pelo Notebook 06)* | Arquivo binário de produção armazenado na pasta `models/` que encapsula o `HistGradientBoostingClassifier` treinado, o contrato exato das `32` colunas esperadas e os limiares de corte (`0.48` e `0.65`) para escoragem em lote (*batch scoring*) sem necessidade de re-treinamento. |
| **6.1** *(Implantação)* | **Pipeline de Escoragem em Lote** | `notebooks/implantacao_scoring_fase6.ipynb` | Código executável que aplica as transformações da Fase 3 em novos inscritos, exporta e carrega o artefato da pasta `models/`, calcula a probabilidade individual (`SCORE_ABSTENCAO`) e classifica cada candidato em **Alto Risco**, **Risco Moderado** ou **Baixo Risco**. |
| **6.2** *(Monitoramento)* | **Protocolo de Monitoramento e *Drift*** | `notebooks/implantacao_scoring_fase6.ipynb` , `README.md` e `Fase_6.md` | Define os gatilhos anuais de auditoria de *Data Drift* (desvio > 10% nas variáveis de entrada), *Concept Drift* (queda do `Recall` abaixo de `68%`), ciclo de re-treino e regras de conformidade ética com a LGPD. |
| **6.3 & 6.4** *(Fechamento)* | **Relatório Final e Revisão Crítica** | **`FASE_6/relatorio_final.md`**, **`FASE_6/revisao_critica.md`**, `notebooks/implantacao_scoring_fase6.ipynb`, `README.md` e `Fase_6.md` | Consolida os resultados finais do ciclo CRISP-DM no documento executivo `FASE_6/relatorio_final.md` (`ROC-AUC = 0.7205`, `Recall = 71,29%`, recuperação projetada de `+1.870` candidatos no DF), lições aprendidas (impacto da anonimização LGPD pós-2024) e trabalhos futuros. |
| **6.3** *(Fechamento)* | **Apresentação Final** *(pendente)* | — | Slides para a apresentação final do projeto, exigidos no entregável "Relatório e Apresentação Final" do Guia Prático CRISP-DM. Ainda não adicionados ao repositório. |

---

## Estrutura Interna do Artefato (`models/modelo_abstencao_enem_df.joblib`)

O principal entregável técnico da Fase 6 está disponível diretamente na pasta **`models/`** (`models/modelo_abstencao_enem_df.joblib`) e consiste em um dicionário Python serializado via `joblib`, projetado para evitar erros de esquema (*schema mismatch*) em ambiente de produção:

```python
{
    "modelo": HistGradientBoostingClassifier(...),  # Modelo campeão treinado na base socioeconômica do DF
    "colunas_esperadas": [...],                     # Lista ordenada das 32 features exigidas na entrada
    "limiar_operacional": 0.48,                     # Corte que garante Recall >= 70% (Risco Moderado)
    "limiar_alto_risco": 0.65,                      # Corte para acionamento prioritário (Busca Ativa)
    "versao": "1.0.0-enem-df"                       # Controle de versionamento do modelo
}
```
