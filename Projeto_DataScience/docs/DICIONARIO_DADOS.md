# Dicionário de Dados — Abstenção ENEM DF (2023–2025)

Este documento descreve todas as variáveis utilizadas ao longo do projeto, divididas entre os **atributos originais extraídos dos microdados do INEP** e as **variáveis construídas na Fase 3 (Engenharia de Atributos)** do CRISP-DM.

---

## 1. Variável-Alvo (Target)

| Variável | Tipo | Valores / Codificação | Descrição |
| :--- | :---: | :--- | :--- |
| **`ABSTENCAO`** | Binária (`int`) | `0` = Presente nos dois dias<br>`1` = Ausente em $\ge 1$ dia | Construída a partir de `TP_PRESENCA_CH == 0` ou `TP_PRESENCA_MT == 0`. Candidatos eliminados (`código 2`) foram removidos antes da modelagem. |

---

## 2. Variáveis Construídas (Fase 3 — Feature Engineering)

| Variável | Tipo | Valores / Codificação | Descrição |
| :--- | :---: | :--- | :--- |
| **`POSSUI_ESCOLA_VINCULADA`** | Binária (`int`) | `0` = Sem vínculo (Egresso)<br>`1` = Com escola registrada | Indica se o candidato possui vínculo escolar ativo informado no Censo Escolar (`TP_DEPENDENCIA_ADM_ESC` preenchido). |
| **`ESTUDA_FORA_DF`** | Binária (`int`) | `0` = Escola no DF ou sem vínculo<br>`1` = Escola em outra UF (ex.: GO) | Identifica estudantes que residem/estudam fora do DF (como cidades do Entorno) e se deslocam para fazer a prova em Brasília. |
| **`EGRESSO_FORA_FLUXO`** | Binária (`int`) | `0` = Cursando Ensino Médio<br>`1` = Concluiu ou fora da escola | Sinaliza candidatos fora do fluxo escolar regular (`TP_ST_CONCLUSAO` igual a `1` ou `4`). |
| **`REDE_ESCOLAR`** | Categórica (`int`) | `0` = Sem vínculo<br>`1` = Federal<br>`2` = Estadual<br>`3` = Municipal<br>`4` = Privada | Padronização de `TP_DEPENDENCIA_ADM_ESC`, convertendo nulos estruturais (`MNAR`) na categoria explícita `0`. |
| **`RENDA_ORDINAL`** | Ordinal (`int`) | `0` (`A`) até `16` (`Q`) | Mapeamento numérico crescente da renda familiar (`Q006`), preservando a ordem de grandeza socioeconômica. |
| **`ESC_PAI_ORDINAL`** | Ordinal (`int`) | `-1` (`H` - Não sabe)<br>`0` (`A`) até `6` (`G`) | Mapeamento ordinal da escolaridade do pai (`Q001`), de *Nunca estudou* (`0`) até *Pós-graduação* (`6`). |
| **`ESC_MAE_ORDINAL`** | Ordinal (`int`) | `-1` (`H` - Não sabe)<br>`0` (`A`) até `6` (`G`) | Mapeamento ordinal da escolaridade da mãe (`Q002`), de *Nunca estudou* (`0`) até *Pós-graduação* (`6`). |
| **`QTD_COMPUTADORES`** | Ordinal (`int`) | `0` (`A`) até `4` (`E`) | Quantidade de computadores na residência (`Q024`), variando de *Nenhum* (`0`) até *Quatro ou mais* (`4`). |
| **`ACESSO_INTERNET`** | Binária (`int`) | `0` = Não (`A`)<br>`1` = Sim (`B`) | Indica se a residência do candidato possui acesso à internet (`Q025`). |
| **`SEXO_MASC`** | Binária (`int`) | `0` = Feminino (`F`)<br>`1` = Masculino (`M`) | Codificação binária da variável original `TP_SEXO`. |

---

## 3. Variáveis Originais dos Microdados do INEP

### 3.1 Identificação, Presença e Demografia

| Variável | Tipo | Domínio / Códigos | Descrição Oficial (INEP) |
| :--- | :---: | :--- | :--- |
| **`SG_UF_PROVA`** | Texto (`str`) | `'DF'` | Sigla da Unidade da Federação de aplicação da prova (filtro de escopo do projeto). |
| **`TP_PRESENCA_CH`** | Categórica (`int`) | `0` = Faltou<br>`1` = Presente<br>`2` = Eliminado | Presença na prova de Ciências Humanas (1.º domingo). |
| **`TP_PRESENCA_MT`** | Categórica (`int`) | `0` = Faltou<br>`1` = Presente<br>`2` = Eliminado | Presença na prova de Matemática (2.º domingo). |
| **`TP_FAIXA_ETARIA`** | Ordinal (`int`) | `1` = Menor de 17 anos<br>`2` = 17 anos \| `3` = 18 anos<br>`4` = 19 anos \| `5` = 20 anos<br>`6` a `10` = 21 a 25 anos<br>`11` = 26 a 30 anos<br>`12` = 31 a 35 anos<br>`13` = 36 a 40 anos<br>`14` a `20` = Acima de 40 anos | Faixa etária do candidato na data de inscrição. |
| **`TP_ESTADO_CIVIL`** | Categórica (`int`) | `0` = Não informado<br>`1` = Solteiro(a)<br>`2` = Casado(a) / União estável<br>`3` = Divorciado(a) / Separado(a)<br>`4` = Viúvo(a) | Estado civil autodeclarado pelo participante. |
| **`TP_COR_RACA`** | Categórica (`int`) | `0` = Não declarado<br>`1` = Branca \| `2` = Preta<br>`3` = Parda \| `4` = Amarela<br>`5` = Indígena | Cor ou raça autodeclarada pelo participante. |
| **`TP_LINGUA`** | Binária (`int`) | `0` = Inglês<br>`1` = Espanhol | Língua Estrangeira escolhida no ato da inscrição. |
| **`IN_TREINEIRO`** | Binária (`int`) | `0` = Não<br>`1` = Sim | Indica se o inscrito fez a prova apenas para autoavaliação (sem fins de acesso ao ensino superior). |

### 3.2 Trajetória e Vínculo Escolar

| Variável | Tipo | Domínio / Códigos | Descrição Oficial (INEP) |
| :--- | :---: | :--- | :--- |
| **`TP_ST_CONCLUSAO`** | Categórica (`int`) | `1` = Já concluí o Ensino Médio<br>`2` = Concluirei no ano do exame<br>`3` = Concluirei após o ano do exame<br>`4` = Não concluí e não estou cursando | Situação de conclusão do Ensino Médio no momento da inscrição. |
| **`TP_DEPENDENCIA_ADM_ESC`** | Categórica (`float`) | `1` = Federal \| `2` = Estadual<br>`3` = Municipal \| `4` = Privada<br>`NaN` = Sem vínculo escolar | Dependência administrativa da escola de origem (disponível apenas para concluintes regulares). |
| **`TP_LOCALIZACAO_ESC`** | Categórica (`float`) | `1` = Urbana<br>`2` = Rural<br>`NaN` = Sem vínculo escolar | Localização geográfica da escola do candidato. |
| **`TP_SIT_FUNC_ESC`** | Categórica (`float`) | `1` = Em atividade<br>`2` = Paralisada<br>`3` = Extinta<br>`NaN` = Sem vínculo escolar | Situação de funcionamento da escola no Censo Escolar. |
| **`SG_UF_ESC`** | Texto (`str`) | `'DF'`, `'GO'`, outras UFs ou `NaN` | Unidade da Federação onde se localiza a escola do candidato. |

### 3.3 Questionário Socioeconômico (Dataset B — Edição 2023)

| Variável | Tipo | Domínio / Códigos | Descrição Oficial (INEP) |
| :--- | :---: | :--- | :--- |
| **`Q001` / `Q002`** | Categórica (`str`) | `A` = Nunca estudou<br>`B` = Não completou 4.ª série/5.º ano<br>`C` = Completou 4.ª série, mas não 8.ª<br>`D` = Completou 8.ª série, mas não EM<br>`E` = Completou o Ensino Médio<br>`F` = Completou a Faculdade<br>`G` = Completou a Pós-graduação<br>`H` = Não sei | Grau máximo de escolaridade do pai (`Q001`) e da mãe (`Q002`). |
| **`Q006`** | Categórica (`str`) | `A` = Nenhuma renda<br>`B` = Até R$ 1.320,00<br>`C` = R$ 1.320,01 a R$ 1.980,00<br>`D` = R$ 1.980,01 a R$ 2.640,00<br>`E` = R$ 2.640,01 a R$ 3.300,00<br>`F` = R$ 3.300,01 a R$ 3.960,00<br>`G` = R$ 3.960,01 a R$ 5.280,00<br>`H` = R$ 5.280,01 a R$ 6.600,00<br>`I` = R$ 6.600,01 a R$ 7.920,00<br>`J` = R$ 7.920,01 a R$ 9.240,00<br>`K` = R$ 9.240,01 a R$ 10.560,00<br>`L` = R$ 10.560,01 a R$ 11.880,00<br>`M` = R$ 11.880,01 a R$ 13.200,00<br>`N` = R$ 13.200,01 a R$ 15.840,00<br>`O` = R$ 15.840,01 a R$ 19.800,00<br>`P` = R$ 19.800,01 a R$ 26.400,00<br>`Q` = Acima de R$ 26.400,00 | Renda mensal bruta familiar autodeclarada (valores de referência do ENEM 2023 baseados no salário mínimo de R$ 1.320,00). |
| **`Q024`** | Categórica (`str`) | `A` = Não \| `B` = Sim, um<br>`C` = Sim, dois \| `D` = Sim, três<br>`E` = Sim, quatro ou mais | Presença e quantidade de computadores na residência. |
| **`Q025`** | Categórica (`str`) | `A` = Não<br>`B` = Sim | Disponibilidade de acesso à internet na residência. |

---

## 4. Saídas do Pipeline de Escoragem (Fase 6 — Produção)

| Variável | Tipo | Domínio / Faixas | Descrição |
| :--- | :---: | :--- | :--- |
| **`SCORE_ABSTENCAO`** | Contínua (`float`) | `0.0000` a `1.0000` | Probabilidade estimada de abstenção calculada pelo modelo campeão (`Gradient Boosting — HistGB`). |
| **`FAIXA_RISCO`** | Categórica (`str`) | `Baixo Risco` (`< 0.48`)<br>`Risco Moderado` (`0.48` a `0.64`)<br>`Alto Risco` (`>= 0.65`) | Classificação operacional utilizada para direcionar a régua de comunicação e busca ativa antes da prova. |
