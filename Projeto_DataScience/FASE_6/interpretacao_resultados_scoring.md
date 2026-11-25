# Guia Prático de Interpretação: Resultados da Escoragem em Lote

Este documento traduz os resultados gerados pelo pipeline de produção (`notebooks/implantacao_scoring_fase6.ipynb` + `models/modelo_abstencao_enem_df.joblib`) para uma leitura gerencial e não técnica. O objetivo é demonstrar como o modelo classifica novos inscritos no ENEM no Distrito Federal e qual intervenção prática deve ser acionada para cada perfil antes do dia da prova.

---

## 1. Como Ler a Saída do Sistema (*Batch Scoring*)

Quando o modelo processa a lista de inscritos logo após o encerramento das inscrições, ele avalia simultaneamente dezenas de características e atribui a cada candidato uma probabilidade de faltar à prova (`SCORE_ABSTENCAO`, de `0.00` a `1.00`), enquadrando-o em uma das **três faixas operacionais**:

| Faixa de Risco | Regra de Corte (`Score`) | Perfil Predominante Identificado | Ação Preventiva Recomendada (Alinhada à Fase 1) |
| :--- | :---: | :--- | :--- |
| **Alto Risco** | `>= 0.65` *(65% ou mais)* | Candidatos adultos/egressos fora do fluxo escolar (`TP_ST_CONCLUSAO = 1`) e de baixa renda (`Q006` entre `A` e `C`). | **Suporte logístico/transporte e busca ativa:** divulgação prioritária de gratuidade no transporte público (Passe Livre Estudantil nos domingos de prova), mutirões de simulados gratuitos e contato institucional direto. |
| **Risco Moderado** | `0.48` a `0.64` *(48% a 64%)* | Jovens em transição escolar ou egressos recentes com renda intermediária/baixa (`Q006` entre `B` e `F`). | **Campanhas de engajamento digital:** régua automatizada de notificações via SMS, WhatsApp e e-mail (7 dias, 48 horas e véspera do exame) com confirmação de local de prova, horários e documentos obrigatórios. |
| **Baixo Risco** | `< 0.48` *(abaixo de 48%)* | Estudantes concluintes regulares (`TP_ST_CONCLUSAO = 2`) com suporte escolar ativo e maior renda familiar (`Q006` a partir de `I`). | **Comunicação padrão:** acompanhamento regular pelo cronograma oficial, sem necessidade de alocação extra de verba pública. |

---

## 2. Análise dos Casos Reais Gerados no Notebook 06

Na simulação executada na Subfase 6.1 sobre uma amostra de 10 candidatos do DF, observa-se claramente como o modelo separa os perfis de vulnerabilidade sem depender de regras manuais fixas[cite: 1]:

### Caso A — Alto Risco (`Score` entre `0.73` e `0.80`) $\rightarrow$ Ação: Suporte Logístico e Busca Ativa
* **Exemplos observados na saída:** Candidatos na faixa etária **`11`** (26 a 30 anos), situação **`1`** (já concluíram o Ensino Médio há algum tempo — egressos) e renda **`B`** ou **`C`** (até 1,5 salário mínimo) receberam escores de **`0.7318`**, **`0.7514`** e **`0.7953`**[cite: 1].
* **Por que o risco é alto:** Pessoas adultas, afastadas da rotina escolar e inseridas no mercado de trabalho informal ou de baixa remuneração enfrentam maiores barreiras de deslocamento no domingo e menor apoio preparatório.
* **Encaminhamento prático:** Como o modelo sinalizou probabilidade acima de `65%`, esses inscritos entram imediatamente na lista prioritária para **suporte logístico/transporte** (orientação sobre acesso gratuito ao metrô e ônibus no DF nos dias de exame) e ações de acolhimento pré-prova.

### Caso B — Risco Moderado (`Score` entre `0.51` e `0.65`) $\rightarrow$ Ação: Campanhas de Engajamento (SMS/Notificações)
* **Exemplos observados na saída:**
  * Um concluinte regular do Ensino Médio (`TP_ST_CONCLUSAO = 2`, idade **`4`** = 19 anos), mas de família de baixa renda (`Q006 = B`), recebeu escore **`0.5137`**[cite: 1].
  * Jovens egressos (`TP_ST_CONCLUSAO = 1`) na faixa de 19 a 23 anos (`TP_FAIXA_ETARIA` **`4`** e **`8`**) com renda baixa/intermediária (`Q006 = B` e `F`) receberam escores **`0.6264`** e **`0.6454`**[cite: 1].
* **Por que o risco é moderado:** Embora ainda tenham vínculo recente com os estudos, a restrição financeira ou o início da vida adulta aumenta o risco de esquecimento de prazos, desmotivação ou dificuldade pontual no 2.º domingo (Matemática/Natureza).
* **Encaminhamento prático:** Esses candidatos são incluídos automaticamente nas **campanhas de engajamento via SMS/notificações**, recebendo lembretes personalizados de rota até o local de aplicação, horário de fechamento dos portões e incentivo para comparecer aos dois domingos de prova.

### Caso C — Baixo Risco (`Score` entre `0.15` e `0.40`) $\rightarrow$ Ação: Sem Intervenção Extra
* **Exemplos observados na saída:** Concluintes regulares (`TP_ST_CONCLUSAO = 2`) de 17 a 18 anos (`TP_FAIXA_ETARIA` **`2`** e **`3`**) pertencentes a famílias de renda média-alta/alta (`Q006 = K` e `P`) obtiveram escores de apenas **`0.1895`** e **`0.1486`**[cite: 1].
* **Por que o risco é baixo:** Contam com acompanhamento diário da escola e estrutura familiar/financeira favorável ao deslocamento e à realização do exame.
* **Encaminhamento prático:** Ao evitar gastos desnecessários com esse público, a gestão pública concentra o orçamento de transporte e busca ativa exclusivamente nos grupos de **Alto** e **Moderado Risco**, maximizando o retorno social do projeto.
