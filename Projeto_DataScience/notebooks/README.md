# Fase 1 e Subfase 2.1 (CRISP-DM): Entendimento do Negócio e Extração dos Microdados (DF | 2023–2025)

## 1. Entendimento do Negócio
- **Objetivo:** Predizer a abstenção de candidatos inscritos no ENEM no **Distrito Federal (DF)** utilizando exclusivamente variáveis disponíveis no ato da inscrição.
- **Critério de Recorte:** Registros com `SG_UF_PROVA == 'DF'` nas edições de **2023, 2024 e 2025**.

## 2.1 Coleta Inicial e Pipeline de Extração Local
Devido ao volume bruto dos microdados nacionais do INEP (~6,25 GB e 13,07 milhões de linhas), o processamento inicial foi executado localmente em três etapas sequenciais (armazenadas em `src/`), reduzindo os dados para **25,68 MB** em formato `.parquet` (`data/processed/`):
1. `inspecionar_pastas.py` — Mapeamento dos diretórios e tamanhos dos CSVs brutos.
2. `checar_colunas.py` — Auditoria dos esquemas e detecção da mudança estrutural do INEP em 2024.
3. `extrair_df_final.py` — Leitura otimizada em lotes (*chunks*) com filtro `SG_UF_PROVA == 'DF'` e exportação para `.parquet`.

> **Nota:** Os blocos abaixo documentam o pipeline executado localmente sobre os arquivos brutos do INEP (`data/raw/`). Para rodar as análises subsequentes diretamente na nuvem sem baixar os 6,25 GB originais, utilize os arquivos `.parquet` já disponíveis em `data/processed/`.
