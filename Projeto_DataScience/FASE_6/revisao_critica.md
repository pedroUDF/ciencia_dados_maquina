## Revisão Crítica do Projeto (6.4)

### O que Funcionou Bem (Pontos Fortes)
* **Auditoria de Dados antes da Limpeza:** Identificar que os valores ausentes nas variáveis escolares correspondiam a candidatos egressos (*MNAR*) evitou o descarte indevido de ~70% da base do DF.
* **Otimização de Armazenamento e Performance:** A conversão dos microdados brutos em CSV (`6,25 GB`) para formato colunar `.parquet` (`25,68 MB`) viabilizou execução rápida, leve e totalmente reproduzível em nuvem.
* **Engenharia de Atributos e Calibração:** A criação das variáveis `EGRESSO_FORA_FLUXO` e `RENDA_ORDINAL`, aliada ao ajuste do limiar operacional para `0.48`, garantiu o atingimento da meta de negócio (`Recall = 71,29%`).

### Limitações e Lições Aprendidas
* **Impacto da Anonimização (LGPD):** A partir da edição de 2024, o INEP desvinculou as tabelas `PARTICIPANTES` e `RESULTADOS`, impedindo o treinamento longitudinal com variáveis socioeconômicas de 2024 e 2025 e exigindo estratégias distintas de modelagem (Dataset A vs. Dataset B).
* **Ausência de Granularidade Geográfica Fina:** Os microdados públicos não informam o CEP residencial do inscrito, impossibilitando calcular a distância entre a residência e o local de prova — fator logisticamente relevante no Distrito Federal e Entorno.

### Próximos Passos e Trabalhos Futuros
* **Integração Institucional (SEEDF / INEP):** Em ambiente seguro sob termo de sigilo, incorporar a distância geodésica residência–local de prova e a cobertura de transporte público para elevar o poder discriminativo (`ROC-AUC > 0.75`).
