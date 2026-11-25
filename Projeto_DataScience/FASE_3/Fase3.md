## Fase 3: Preparação dos Dados

### Seleção e Limpeza de Dados
- **Definição da Variável-Alvo (`ABSTENCAO`):** Classificação binária onde `1` representa ausência em pelo menos um dia de prova (`TP_PRESENCA_CH == 0` ou `TP_PRESENCA_MT == 0`) e `0` representa comparecimento nos dois domingos.
- **Remoção de Eliminados (`código 2`):** Foram excluídos **120** registros em 2023, **157** em 2024 e **126** em 2025 (< 0,2% da base) referentes a candidatos eliminados por ocorrência disciplinar, mantendo a classe positiva pura para evasão.
- **Tratamento de Nulos Estruturais (`MNAR`):** Os ~70% de valores omissos nas variáveis escolares foram convertidos na categoria explícita `0` (`Sem_Vinculo_Escolar`), preservando o sinal preditivo dos candidatos egressos.
- **Padronização Geográfica:** Os 4 casos de rede `Municipal` identificados em 2023 foram agrupados na categoria de vínculo externo e a UF da escola foi consolidada em `DF`, `GO`, `OUTRA_UF` e `SEM_VINCULO`.

### Engenharia de Atributos (*Feature Engineering*)
Foram criadas variáveis derivadas específicas para o contexto educacional e geográfico do DF:
- **`POSSUI_ESCOLA_VINCULADA` (`0/1`):** Indica se o candidato possui vínculo escolar ativo registrado no Censo Escolar.
- **`ESTUDA_FORA_DF` (`0/1`):** Captura a mobilidade pendular de estudantes matriculados fora do DF (como cidades do Entorno de Goiás) que se deslocam até Brasília para realizar a prova.
- **`EGRESSO_FORA_FLUXO` (`0/1` — Dataset B):** Sinaliza candidatos que já concluíram ou não estão cursando o Ensino Médio (`TP_ST_CONCLUSAO` em `[1, 4]`).
- **Codificação Ordinal Socioeconômica (Dataset B):** Preservação da ordem de grandeza nas variáveis `RENDA_ORDINAL` (`Q006`: `0` a `16`), `ESC_PAI_ORDINAL` (`Q001`), `ESC_MAE_ORDINAL` (`Q002`), `QTD_COMPUTADORES` (`Q024`) e `ACESSO_INTERNET` (`Q025`).

### Integração, Formatação e Particionamento
Aplicou-se *One-Hot Encoding* nas variáveis categóricas nominais, resultando em **0 valores nulos residuais** e duas matrizes prontas para a **Fase 4 (Modelagem)** em `dados_modelagem/`:

| Conjunto de Dados | Estratégia de Divisão | Base de Treino | Base de Teste | Atributos | Taxa de Abstenção (Teste) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Dataset A** *(Série Histórica 2023–2025)* | Validação Temporal (*Out-of-Time*: Treino 2023–2024 / Teste 2025) | `147.218` linhas | `82.829` linhas | `20` | **31,63%** |
| **Dataset B** *(Socioeconômico 2023)* | Divisão Estratificada (`80%` Treino / `20%` Teste) | `58.284` linhas | `14.571` linhas | `33` | **31,00%** |
