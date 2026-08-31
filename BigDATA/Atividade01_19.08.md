# Atividade Prática — Detetives dos Dados

## Ciência de Dados e Aprendizagem de Máquina — Aula 01

**Tema:** Introdução à Ciência de Dados e Big Data
**Metodologia:** Trabalho em equipe
**Tempo:** 20 minutos
**Entregável:** Mapa do Problema de Ciência de Dados

---

## 1. Identificação da equipe

| Campo             | Resposta |
| ----------------- | -------- |
| **Turma:**        | SI 7/8 Noturno |
| **Data:**         | 26/08/2026 |
| **Equipe:**       | Piratas dos Dados |
| **Integrante 1:** | Pedro Luiz Oliveira da Costa |
| **Integrante 2:** | Henrique Ribeiro Leonardo |

---

## 2. Escolha do problema

Área escolhida:

* [X] Entretenimento

**Descreva, em poucas linhas, o problema que sua equipe pretende analisar.**

> Analisaremos a fragmentação dos direitos de transmissão do futebol brasileiro após a Lei do Mandante. A divisão dos jogos em múltiplas plataformas de streaming aumentou os custos para o torcedor, gerou confusão sobre onde assistir às partidas e impulsionou a pirataria, enfraquecendo a sustentabilidade da própria indústria do entretenimento."

---

## 4. Quem possui esse problema?

**Quem possui ou enfrenta esse problema?**

> A indústria do entretenimento que perde audiência e receita para a pirataria.

### Quem é afetado pelo problema?

> O Os afetados por esse problema incluem os torcedores, expostos a altos custos e à fadiga de assinaturas. Torcedores mais leigos podem sofrer com a barreira tecnológica e a confusão sobre a grade de programação, sem saber em qual plataforma ou canal o jogo será exibido em cada rodada.

---

## 5. Por que esse problema é importante?

**Qual é o impacto do problema?**

> Aumento expressivo no custo total mensal do torcedor, levando a muitos a migrarem para serviços ilegais (IPTV clandestino e sites piratas), gerando perda bilionária de receita anual em assinaturas e direitos de imagem.

---

## 6. Qual decisão precisa ser tomada?

**Qual decisão a organização precisa tomar?**

> adequar a política de preços e usabilidade dos pacotes oficiais para reduzir o incentivo financeiro do torcedor em migrar para a pirataria.

---

# 7. Identificação dos dados

| Nº | Dado necessário | Por que esse dado é importante? |
| -: | --------------- | ------------------------------- |
| 1 | Custo total acumulado das assinaturas | Quantifica a barreira financeira do torcedor e o gatilho financeiro para a pirataria. |
| 2 | Mapeamento de distribuição dos jogos por plataforma | Mede a fricção do usuário e identifica o nível de pulverização das partidas. |
| 3 | Taxa de penetração e uso de IPTV/Pirataria | Avalia o tamanho do mercado clandestino e a perda direta de receita das emissoras. |
| 4 | Métrica de cancelamento de assinaturas (Churn Rate) | Mostra a rotatividade do torcedor que assina o streaming apenas nos meses de jogos do seu time. |
| 5 | Audiência média e engajamento por partida/plataforma | Revela o impacto da fragmentação na visibilidade do campeonato e no alcance dos patrocinadores. |
| 6 | Receita líquida dos clubes com direitos de transmissão | Permite comparar a eficiência do modelo atual com a projeção de receita em um modelo de Liga Única. |

---

# 8. Que informações queremos descobrir?

### Pergunta 1

> Qual é o custo mensal total necessário para um torcedor acompanhar 100% dos jogos oficiais do seu clube na temporada?

### Pergunta 2

> Qual é o percentual de torcedores que migrou para transmissões piratas (IPTV/sites) devido à fragmentação das plataformas?

### Pergunta 3

> Como a pulverização dos jogos entre diferentes streamings afetou as taxas de audiência e engajamento em relação ao modelo anterior?

### Pergunta 4

> Qual foi o impacto financeiro real na receita líquida dos clubes após a mudança na negociação trazida pela Lei do Mandante?

---

# 9. Quais padrões podemos procurar?

* [x] Tendências
* [x] Comparações
* [x] Grupos semelhantes
* [x] Comportamentos recorrentes
* [x] Valores fora do padrão
* [x] Relações entre variáveis
* [x] Mudanças ao longo do tempo

### Explique um padrão que vocês gostariam de encontrar

> O padrão ideal a ser buscado nos dados é uma correlação direta entre a fragmentação da oferta e a perda de eficiência do ecossistema oficial.
Buscando identificar o ponto de inflexão do consumidor: a partir de qual valor acumulado de assinaturas e de qual nível de complexidade (número de aplicativos necessários) o torcedor deixa de ser um assinante oficial e se converte em usuário de serviços piratas ou abandona o acompanhamento ao vivo.

---

# 10. Qual análise poderia ser realizada?

* [x] Análise descritiva
* [x] Comparação entre grupos
* [x] Análise temporal
* [x] Visualização por gráficos
* [x] Identificação de padrões
* [ ] Classificação
* [ ] Previsão
* [ ] Agrupamento

### Explique

> Podemos utilizar a análise descritiva e a visualização por gráficos para resumir o cenário atual, mapeando a distribuição de jogos por plataforma, o custo total das assinaturas e a audiência média das partidas. A comparação entre grupos permite contrastar o impacto financeiro entre clubes de grande e pequeno porte, além de diferenciar o comportamento de torcedores pagantes versus usuários de pirataria. Complementarmente, a análise temporal é ideal para avaliar a variação na taxa de cancelamento (churn) e no alcance das transmissões ao longo dos meses da temporada.

A identificação de padrões conecta todas essas frentes ao correlacionar o aumento de custos com a migração para transmissões ilegais ou abandono dos jogos ao vivo. Por outro lado, técnicas mais complexas de aprendizado de máquina como classificação, previsão e agrupamento (clustering) são dispensáveis nesta etapa, pois o foco primário da atividade é diagnosticar a eficiência e as falhas do ecossistema atual com dados históricos e comportamentais, sem a necessidade de construir modelos preditivos ou segmentações avançadas.

---

# 11. Qual decisão poderia ser tomada?

> A organização deve migrar da venda pulverizada para a criação de uma Liga Única centralizada, unificando os direitos de transmissão em uma só negociação ou lançando uma plataforma oficial integrada no modelo Direct-to-Consumer (D2C). Essa medida padroniza a entrega dos jogos, reduz a quantidade de assinaturas necessárias e estabelece uma teto de preço acessível para o torcedor, eliminando a fricção de acesso ao campeonato.

---

# 12. Qual seria o benefício?

> O principal benefício é a retenção e o aumento da receita de longo prazo por meio da recuperação do público oficial e do combate direto à pirataria. A centralização aumenta o alcance de audiência, estabiliza o fluxo de caixa dos clubes com assinaturas recorrentes (anti-churn), valoriza as cotas de patrocínio para as marcas e garante a sustentabilidade financeira e competitiva do futebol brasileiro.

---

# 13. Os 5 Vs do Big Data

| V              | Pergunta                                                   | Resposta da equipe |
| -------------- | ---------------------------------------------------------- | ------------------ |
| **Volume**     | Existe uma grande quantidade de dados?                     | Sim, o volume é expressivo ao agregar bases de audiência, interações em redes sociais, logs de streaming, cancelamentos de assinaturas e registros operacionais de múltiplos clubes e transmissões.
| **Velocidade** | Os dados são gerados ou processados rapidamente?           | Sim, dados de audiência ao vivo, tráfego de streaming, interações de usuários e menções em redes sociais são gerados em tempo real durante as partidas.
| **Variedade**  | Existem diferentes tipos ou formatos de dados?             | Sim, há dados estruturados (valores de contratos, métricas de assinaturas, audiência) e não estruturados (comentários em redes sociais, logs de erro, sinal de vídeo).
| **Veracidade** | Os dados podem apresentar erros ou problemas de qualidade? | Sim, os dados podem conter inconsistências por subnotificação da pirataria, inconsistência nos critérios de medição entre plataformas e variações na qualidade de declaração dos torcedores.
| **Valor**      | Os dados podem gerar algum benefício ou apoiar decisões?   | Sim, fornecem inteligência estratégica para precificação de pacotes, identificação de padrões de churn, combate à pirataria e tomada de decisão sobre centralização de direitos em uma Liga Única. 

### Qual dos 5 Vs é mais relevante para o problema?

> Valor.

### Justifique

> Todos os outros Vs são aspectos técnicos e operacionais de infraestrutura. Coletar terabytes de dados rapidamente e em formatos variados não traz nenhum retorno prático se esses dados não forem transformados em insights acionáveis para resolver o problema. É o Valor que justifica o investimento no projeto, permitindo tomar decisões estratégicas reais, como redefinir a precificação de transmissões ou criar uma Liga Única para combater a pirataria.

---

# 14. Mapa do Problema de Ciência de Dados

```text
┌─────────────────────┐
│       PROBLEMA      │
| Fragmentação das    |
| transmissões do     |
| futebol brasileiro  |
|       após a        | 
│  Lei do Mandante    │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│        DADOS        │
│ Custo acumulado das │
|    assinaturas,     │
|distribuição de jogos|
|  por plataforma,    |
| uso de IPTV/,       |
|      taxa de        |
|   cancelamento,     |
|audiência por partida|
| e receita dos clubes│
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│     INFORMAÇÕES     │
│ Fontes de Inflexão  │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│       ANÁLISE       │
│ Descritiva, temporal│
│      padrões        │
│visualização gráfica │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│       DECISÃO       │
│     Criação da      │
|     Liga Única      |
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│      BENEFÍCIO      │
│ aumento do acesso   │
│     do público      │
└─────────────────────┘
```

### Resuma cada etapa

**Problema:**

> Fragmentação das transmissões do futebol brasileiro após a Lei do Mandante, gerando custos elevados, confusão para o torcedor e aumento da pirataria.

**Dados:**

> Custo acumulado das assinaturas, distribuição dos jogos por plataforma, uso de IPTV/pirataria, taxa de cancelamento, audiência por partida e receita dos clubes.

**Informação:**

> Ponto de inflexão em que o custo e a pulverização levam à pirataria, picos de cancelamento ao longo do campeonato e impacto da fragmentação na audiência e receitas.

**Análise:**

> Análise descritiva e temporal, comparação entre grupos de clubes e torcedores, identificação de padrões de consumo e visualização gráfica dos impactos.

**Decisão:**

> Unificar os direitos de transmissão por meio de uma Liga Única centralizada ou criar uma plataforma oficial integrada (D2C) com precificação acessível.

**Benefício:**

> Aumento do engajamento e alcance do público, retenção de receita de longo prazo com assinaturas recorrentes, redução da pirataria e sustentabilidade financeira do setor.
---

# 15. Preparação para apresentação

### 1. Nosso problema

> A fragmentação das transmissões do futebol brasileiro pós-Lei do Mandante, que gera custos altos, confusão ao torcedor e impulsiona a pirataria.

### 2. Precisamos destes dados

> Custo acumulado de assinaturas, grade de jogos por plataforma, uso de IPTV/pirataria, taxa de cancelamento (churn), audiência e receita dos clubes.

### 3. Queremos descobrir

> Em que ponto o custo e a pulverização levam o torcedor à pirataria, além de como o cancelamento e a perda de audiência afetam as receitas.

### 4. Pretendemos analisar

> O cenário geral (descritiva e gráficos), a variação ao longo do campeonato (temporal), o contraste entre clubes/torcedores e a identificação de padrões de consumo.

### 5. A decisão poderia ser

> Migrar para uma Liga Única com direitos centralizados ou criar uma plataforma integrada com pacotes e preços acessíveis.

### 6. O benefício esperado é

> Recuperação e engajamento do público oficial, redução da pirataria, receita estável e previsível com assinaturas e sustentabilidade do futebol nacional.

---

# 16. Checklist da equipe

* [x] Definimos um problema real.
* [x] Identificamos quem é afetado pelo problema.
* [x] Explicamos por que o problema é importante.
* [x] Identificamos pelo menos 5 dados necessários.
* [x] Definimos perguntas que queremos responder.
* [x] Identificamos possíveis padrões.
* [x] Indicamos como os dados poderiam ser analisados.
* [x] Definimos uma possível decisão.
* [x] Identificamos o benefício esperado.
* [x] Analisamos os 5 Vs do Big Data.
* [x] Preenchemos o Mapa do Problema.
* [x] Estamos preparados para apresentar em 2 minutos.

---

# 17. Reflexão final

> **Ter muitos dados significa necessariamente tomar boas decisões? Por quê?**

**Resposta:**

> Não. Ter um grande volume de dados não garante boas decisões, pois dados brutos não geram valor por si sós. A abundância de informações frequentemente leva à "paralisia por análise" e ao excesso de ruído, dificultando a identificação do que é realmente relevante para o negócio. Além disso, existe o risco da ilusão de certeza: ter muitos dados pode criar uma falsa sensação de segurança, levando a decisões equivocadas se as informações forem imprecisas, desatualizadas ou interpretadas sob o viés de confirmação de quem as analisa.

---

## Entrega

### Produto final

**Mapa do Problema de Ciência de Dados**

```text
Problema: fragmentação das transmissões do futebol brasileiro pós-Lei do Mandante
↓
Dados necessários: custo de assinaturas, grade por plataforma, uso de IPTV/pirataria, churn, audiência e receita dos clubes
↓
Informações desejadas: ponto de inflexão para a pirataria, picos de cancelamento e impactos da pulverização na audiência e receita
↓
Análise: descritiva, visualização por gráficos, temporal, comparação entre grupos e identificação de padrões
↓
Decisão: centralização dos direitos em uma Liga Única ou plataforma oficial integrada (D2C) com preço acessível
↓
Benefício esperado: recuperação do torcedor oficial, redução da pirataria, receitas previsíveis e sustentabilidade do futebol nacional
```

**Formato:** Markdown.
**Apresentação:** 2 minutos por equipe..
