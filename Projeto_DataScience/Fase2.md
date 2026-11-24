## Fase 2: Entendimento dos Dados

### 2.1 Coleta Inicial e Extração do Recorte (DF)
Os microdados oficiais foram obtidos no Portal de Dados Abertos do **INEP** (edições 2023, 2024 e 2025). Devido ao volume nacional (~4 a 4,8 milhões de linhas por edição), os arquivos CSV originais foram processados localmente em lotes (*chunks* de 100.000 linhas) filtrando `SG_UF_PROVA == 'DF'` e convertidos para o formato colunar `.parquet` (totalizando **25,68 MB**):

| Base Extraída | Total Brasil | Total DF | Participação DF (%) | Colunas | Tamanho `.parquet` |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2023_completo` | 3.933.955 | 72.975 | 1,86% | 76 | 7,62 MB |
| `2024_participantes` | 4.332.944 | 74.520 | 1,72% | 38 | 1,11 MB |
| `2024_resultados` | 4.332.944 | 74.520 | 1,72% | 42 | 7,19 MB |
| `2025_participantes` | 4.810.772 | 82.955 | 1,72% | 38 | 1,23 MB |
| `2025_resultados` | 4.810.772 | 82.955 | 1,72% | 70 | 8,53 MB |
| **Total Consolidado (DF)** | **13.077.671** | **230.450** | **1,76%** | — | **25,68 MB** |

### 2.2 Descrição de Quantidade, Tipagem e Qualidade
Durante a inspeção estrutural dos esquemas do INEP, identificou-se uma mudança metodológica relevante a partir de 2024:
- **2023:** Tabela única (`76 colunas`: `37 object`, `21 float64`, `18 int64`) unindo dados socioeconômicos (`Q001`–`Q025`) e presença (`TP_PRESENCA_*`).
- **2024 e 2025:** Por adequação à LGPD/anonimização, o INEP separou os dados em duas tabelas sem chave primária comum: `PARTICIPANTES` (perfil demográfico e socioeconômico) e `RESULTADOS` (dados da escola, município de prova, língua estrangeira, notas e presença).

#### Comportamento das Variáveis de Presença no DF (`TP_PRESENCA_CH` e `TP_PRESENCA_MT`)
As colunas de presença não possuem valores nulos (`NaN`) em nenhuma edição e revelam um padrão consistente de **evasão entre o 1º e o 2º domingo**:

| Edição | Inscritos DF | Faltas Dia 1 (CH/LC) | Taxa Abstenção Dia 1 | Faltas Dia 2 (MT/CN) | Taxa Abstenção Dia 2 | Eliminados (Dia 1 / Dia 2) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **2023** | 72.975 | 19.725 | **27,03%** | 22.403 | **30,70%** | 81 / 39 |
| **2024** | 74.520 | 18.927 | **25,40%** | 22.002 | **29,52%** | 108 / 49 |
| **2025** | 82.955 | 22.198 | **26,76%** | 25.955 | **31,29%** | 84 / 42 |

---

## Como Reproduzir

1. Baixe os microdados do ENEM (2023–2025) no portal do INEP e extraia-os em `data/raw/`.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
