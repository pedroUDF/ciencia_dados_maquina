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

   ### 2.3 Análise Exploratória de Dados (EDA) e Validação de Hipóteses
A análise visual realizada no notebook `entendimento_dados_fase2.ipynb` validou três hipóteses centrais para a modelagem:

1. **H1 Confirmada (Efeito Segundo Dia):** A abstenção no DF permanece estruturalmente elevada (**31,0%** em 2023, **29,8%** em 2024 e **31,7%** em 2025 considerando ausência em pelo menos um dia), com um salto sistemático de **3,7 a 4,5 pontos percentuais** entre o 1º domingo (Humanas/Linguagens) e o 2º domingo (Matemática/Natureza).
2. **H2 Confirmada (Impacto do Vínculo e Rede Escolar — 2023 a 2025):**
   - Candidatos **Sem vínculo escolar / Egressos** lideram a evasão (**~36% a 38%**).
   - Estudantes da rede **Estadual/DF** registram abstenção entre **20% e 24%**, contrastando fortemente com as redes **Federal** (**~6% a 7,5%**) e **Privada** (**~5% a 6,5%**).
3. **H3 Confirmada (Gradiente Socioeconômico e Trajetória Escolar — 2023):**
   - **Renda Familiar (`Q006`):** Curva decrescente contínua, partindo de **~48%** de abstenção na Faixa A (sem renda) até estabilizar em **~17%–20%** nas faixas de maior renda (I a Q).
   - **Situação no Ensino Médio (`TP_ST_CONCLUSAO`):** Candidatos fora do fluxo regular (*"Não concluí / Não cursando"*: **44,1%**; *"Já concluí o EM"*: **41,9%**) apresentam mais que o dobro da abstenção de concluintes regulares no ano (**18,5%**).

### 2.4 Auditoria de Qualidade dos Dados
A verificação sistemática de integridade, valores omissos e anomalias revelou:

- **Valores Omissos Estruturais (`NaN` nas variáveis escolares):** As 5 variáveis de escola (`CO_MUNICIPIO_ESC`, `SG_UF_ESC`, `TP_DEPENDENCIA_ADM_ESC`, `TP_LOCALIZACAO_ESC`, `TP_SIT_FUNC_ESC`) apresentam omissão em bloco idêntica em cada edição: **72,55%** (2023), **68,22%** (2024) e **69,29%** (2025). Trata-se de ausência informativa (*MNAR*) referente a candidatos egressos que não possuem escola vinculada ativa — será convertida na categoria explícita `"Sem_Vinculo_Escolar"` na Fase 3.
- **Integridade de Prova e Socioeconômica (`0,00%` de nulos):** As variáveis `CO_MUNICIPIO_PROVA`, `TP_LINGUA`, as 4 colunas de presença (`CN`, `CH`, `LC`, `MT`) e todas as variáveis socioeconômicas de 2023 (`TP_FAIXA_ETARIA`, `TP_SEXO`, `TP_COR_RACA`, `Q001`–`Q025`) possuem **0,00%** de valores nulos.
- **Consistência Interna:** Zero divergências de presença entre provas aplicadas no mesmo dia (`CH != LC` = 0 e `CN != MT` = 0 em todas as edições).
- **Anomalia Geográfica Identificada (`Municipal` no DF):** Foram detectados **4 registros** em 2023 (e **0** em 2024–2025) com `TP_DEPENDENCIA_ADM_ESC == 3` (Municipal), oriundos de candidatos de outros estados (`GO`: 2, `PA`: 1, `TO`: 1) que realizaram a prova no DF. Na Fase 3, serão agrupados e utilizados como sinal de mobilidade interestadual.

---

## Como Reproduzir

1. Baixe os microdados do ENEM (2023–2025) no portal do INEP e extraia-os em `data/raw/`.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
3. Execute o script de extração para gerar os recortes leves do DF em .parquet:
   ```bash
   python src/03_extrair_df.py
