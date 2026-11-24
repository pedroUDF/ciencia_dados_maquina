# Aula 2: Algoritmos, Estruturas de Dados, Programação e Engenharia de Software

### Questão 1
* **Resposta:** C) $O(n)$
* **Evidência:** "percorre uma lista de $n$ elementos uma única vez, executando trabalho constante em cada posição."
* **Justificativa:** Como cada um dos $n$ elementos é visitado apenas uma vez e a operação realizada em cada passo leva tempo constante $O(1)$, o tempo total de execução cresce de forma diretamente proporcional ao tamanho da entrada, caracterizando uma complexidade linear $O(n)$.

### Questão 2
* **Resposta:** B) Fila
* **Evidência:** "FIFO" e "atendidas na ordem em que chegam."
* **Justificativa:** A estrutura de dados Fila (*Queue*) segue estritamente a política FIFO (*First-In, First-Out*), onde o primeiro elemento inserido é o primeiro a ser removido/atendido, garantindo o processamento por ordem de chegada.

### Questão 3
* **Resposta:** C) 10
* **Evidência:** "`total = 0`", "`para i de 1 até 4`", "`total = total + i`"
* **Justificativa:** O laço realiza um somatório acumulativo dos valores inteiros de 1 a 4. Passo a passo: $0 + 1 = 1 \rightarrow 1 + 2 = 3 \rightarrow 3 + 3 = 6 \rightarrow 6 + 4 = 10$.

### Questão 4
* **Resposta:** A) Requisito funcional
* **Evidência:** "'o usuário poderá recuperar sua senha por e-mail'."
* **Justificativa:** Requisitos funcionais definem as funcionalidades, serviços ou comportamentos específicos que o sistema deve fornecer aos seus usuários. Permitir a recuperação de senha é uma ação direta do sistema.

### Questão 5
* **Resposta:** A) Teste de regressão
* **Evidência:** "Após modificar uma função, a equipe executa novamente testes existentes para verificar se funcionalidades anteriores continuam corretas."
* **Justificativa:** O teste de regressão tem como objetivo principal garantir que alterações recentes no código (correções ou novas funcionalidades) não introduziram novos defeitos em partes do sistema que já funcionavam anteriormente.

### Questão 6
* **Resposta:** B) Validar duplicidade e testar a regra com cenários
* **Evidência:** "impedir inscrições duplicadas e fornecer mensagem clara ao estudante."
* **Justificativa:** A integridade dos dados exige uma validação lógica (no back-end/banco de dados) antes da persistência para bloquear registros duplicados, aliada a testes com diferentes cenários para assegurar que tanto o bloqueio quanto o feedback visual funcionem conforme esperado.

---

## Aplicando o C.A.L.M.A.

### 1ª Questão escolhida: Questão 1

| Etapa | Registro do estudante |
| :--- | :--- |
| **C - Comando** | Identificar a complexidade temporal do algoritmo descrito. |
| **A - Assunto** | Análise de Complexidade de Algoritmos (Notação Big-O). |
| **L - Leitura** | Um algoritmo visita $n$ elementos uma única vez com custo fixo por elemento. |
| **M - Marcação** | Palavras-chave: "lista de $n$ elementos", "uma única vez", "trabalho constante". |
| **A - Avaliação** | $O(1)$ seria independente de $n$; $O(\log n)$ dividiria o problema; $O(n^2)$ exigiria laços aninhados. Logo, a resposta correta é $O(n)$ (Alternativa C). |

### 2ª Questão escolhida: Questão 5

| Etapa | Registro do estudante |
| :--- | :--- |
| **C - Comando** | Classificar o tipo de atividade/teste realizado após a alteração de código. |
| **A - Assunto** | Engenharia de Software — Testes de Software. |
| **L - Leitura** | Reexecução de testes antigos após modificar uma função para garantir que nada quebrou. |
| **M - Marcação** | Palavras-chave: "modificar uma função", "executa novamente testes existentes", "funcionalidades anteriores continuam corretas". |
| **A - Avaliação** | Carga avalia estresse/desempenho; prototipação e elicitação são fases de requisitos. Revalidar o que já funcionava define o Teste de Regressão (Alternativa A). |

---

## Desafio integrador

**1. Estrutura de dados e justificativa:**  
Utilizaria uma **Fila (Queue)**. Como o sistema recebe solicitações em ordem de chegada, a fila garante o atendimento justo e sequencial por meio do princípio *FIFO (First-In, First-Out)*, processando primeiro a matrícula que foi solicitada há mais tempo.

**2. Regra de negócio (RN01 - Unicidade de Matrícula):**  
"O sistema não deve permitir que um mesmo estudante (identificado pelo CPF ou RA) realize mais de uma inscrição ativa na mesma disciplina/turma no mesmo período letivo. Caso uma tentativa duplicada seja detectada, o sistema deve bloquear a operação e exibir a mensagem: *'Você já possui uma solicitação de matrícula registrada para esta disciplina.'*"

**3. Casos de teste:**  
* **Caso de Teste 01 (Cenário Válido):** Um aluno regular (RA `12345`) sem inscrição prévia solicita matrícula na disciplina *Algoritmos*. **Resultado esperado:** O sistema valida que não há duplicidade, insere a solicitação no final da fila de processamento e exibe confirmação de envio.
* **Caso de Teste 02 (Cenário Inválido):** O mesmo aluno (RA `12345`) tenta enviar uma segunda solicitação de matrícula para a mesma disciplina *Algoritmos*. **Resultado esperado:** O sistema identifica a duplicidade, impede o registro e retorna a mensagem de alerta informando que a inscrição já existe.

**4. Risco da ausência de testes de regressão:**  
Ao alterar o código do sistema (por exemplo, ajustando a interface ou otimizando a fila) sem executar testes de regressão, corre-se o risco de quebrar silenciosamente a regra de validação de duplicidade ou a ordem de atendimento, permitindo inscrições repetidas em produção ou gerando falhas críticas em funcionalidades que antes operavam normalmente.

---

## Autoavaliação

| Tema | Verde | Amarelo | Vermelho |
| :--- | :---: | :---: | :---: |
| **Algoritmos** | [ ] | [X] | [ ] |
| **Estruturas de Dados** | [X] | [ ] | [ ] |
| **Programação** | [ ] | [X] | [ ] |
| **Engenharia de Software** | [X] | [ ] | [ ] |

* **Meu principal ponto de revisão:** Revisar as diferenças práticas entre os níveis de testes de software (unitário, integração, sistema e regressão) e praticar a análise de complexidade em algoritmos com laços aninhados e recursão.
