# Ciberfisicos-TDE-2-Deteccao-E-Recuperacao-De-Impasses
Nome dos integrantes: Artur Conratt, André Felipe, Eduardo Guilherme, Gabriel Moreno
Linguagem escolhida: Python
Link do video do YouTube:



PARTE 1 - JANTAR DOS FILÓSOFOS

Instruções de compilação e execução: 

Essa primeira parte foi implementada em código Python usando a biblioteca padrão threading e time. Para executar basta ter Python instalado na máquina; para ver a versão incorreta, basta executar o arquivo "TDEzao filosofo errado.py". Para executar a versão otimizada, basta executar o arquivo "TDEzao filosofo certo.py".


Relátorio Técnico:

O problema do jantar dos filósofos simula cinco filósofos que estão sentados em uma mesa. Cada filósofo alterna entre pensar e comer. Para comer, ele precisa de dois garfos; o da esquerda e o da direita.

Na versão incorreta, cada filósofo tenta pegar primeiro um garfo e depois o outro sem uma regra de ordenação. O deadlock pode ser gerado quando todos os filósofos pegam um garfo juntos, e ficam esperando o segundo ser liberado. Por consequência ninguém consegue prosseguir, pois todos estão segurando um dos recursos enquanto esperam o outro.

As quatro condições de Coffman são representadas nessa situação:
- cada garfo só pode ser usado por um filósofo por vez
- o filósofo segura o garfo enquanto espera o outro
- o garfo não pode ser tomado
- cada filósofo espera um garfo que está com outro filósofo eternamente

Na versão funcional, usamos hierarquia de recursos. Cada filósofo verifica os dois garfos que precisa utilizar e opta por pegar o garfo com menor índice e outro garfo com maior índice. Com isso, todos conseguem seguir a mesma ordem global de adquirir um recurso e por consequência todos conseguem pegar dois garfos e comer. Isso evita o deadlock porque quebra a condição de espera circular. Já que todos os filósofos seguem uma ordem para pegar seus garfos, não é possível formar um ciclo de espera entre ele.

Fluxograma da lógica do código:

Para cada filósofo:
- Primeiro se define o primeiro garfo necessário, nesse caso: garfo1 = g
- Então se define o segundo garfo necessário: garfo2 = (g+1) % filósofo
- Então se calcula a ordem certa:
- primeiramao = menor valor entre garfo1 e garfo2
- segundamao = maior valor entre garfo1 e garfo2
- e então executa as ações de cada filósofo:
- filósofo pensa
- filósofo fica com fome
- filósofo adquire o garfo de menor índice
- filósofo adquire o garfo de maior índice
- filósofo come
- filósofo devolve o garfo de maior índice
- filósofo devolve o garfo de menor índice
- filósofo volta a pensar

Prints e Logs:

Versão incorreta:
<img width="886" height="340" alt="image" src="https://github.com/user-attachments/assets/23a828cb-ecde-460c-a883-356555d2ffea" />
<img width="886" height="578" alt="image" src="https://github.com/user-attachments/assets/56f8831d-ae2a-4e10-80d6-282526df5c2a" />

Versão funcional:
<img width="886" height="566" alt="image" src="https://github.com/user-attachments/assets/90c19197-8b7e-46e7-9516-ec0472e99fe3" />
<img width="736" height="1191" alt="image" src="https://github.com/user-attachments/assets/0e324966-6340-4c22-8b1f-82f823dfdd1f" />


PARTE 2 - THREADS E SEMÁFOROS

Nesta seção, analisamos o impacto da falta de sincronização em sistemas concorrentes  e como um semáforo binário resolve esse problema, garantindo a consistência dos dados.

Pergunta -
Por que a versão sem sincronização perde incrementos?
Resposta -
Ela perde incrementos porque é burra? não ela perde incrementos porque elas começam lendo o mesmo valor na contagem “count” e sobrescrevem os valores uma da outra, fazendo isso elas perdem uma atualização.
Pergunta -
Por que a versão com semáforo é correta?
Resposta -
Esta versão é a correta, pois o semáforo começa com um tipo de permissão, quando a thread excuta a função “sem.acquire()” e ela se torna a única lá dentro, como se fosse uma pessoa em uma roupa, cada thread só pode ser executada em seguida caso a próxima “roupa” esteja liberada, e tem também “sem.release()” que impede que as threads se sobrescrevam, para não dar erro.

O trade-off de Throughput 
Podemos começar analisando os tempos de demora dos diferentes tipos de semáforo, sendo que um deles elimina o paralelismo real em parte do código fazendo com que as threads precisem esperar uma por uma, como uma fila, e isso reduz o throughput mas pelo menos garante que está tratando de dados corretos.

Conceito de Visibilidade e Ordenação 
Para ententer este conceito vamos analisar que em Python o uso de “acquire()” e “release()” do módulo “threading” atua como uma barreira de memória implícita, que faz isso funcionar como um farol para as próximas threads que vão adquirir o semáforo, na ordem correta.



Versão incorreta:


<img width="393" height="155" alt="image" src="https://github.com/user-attachments/assets/3271ab11-b50f-4cc6-9d3f-df673bff44bb" />



Versão Correta:


<img width="384" height="168" alt="image" src="https://github.com/user-attachments/assets/4d8dc72f-03e7-461a-afbc-a9592bbd72d5" />


PARTE 3 - DEADLOCKS

O dealock ocorre na versão incorreta pois a Thread 1 tenta pegar o Lock A e depois o Lock B enquanto a Thread 2 tenta pegar o Lock B e depois o Lock A. Devido a concorrencia e ao atraso time.sleep, a Thread 1 segura o Lock A e a Thread 2 segura o Lock B, fazendo com que ambas fiquem esperando juntas de forma infinita pelos recursos retidos pela outra.

As 4 condiçoes de Coffman presentes:
1. Exclusao mutua: Cada lock (A ou B) só pode ser retido por uma thread por vez.
2. Posse e espera: A Thread 1 segura o Lock A enquanto espera pelo Lock B (e a Thread 2 segura o Lock B esperando pelo Lock A).
3. Prioridade/preferencia: Um lock não pode ser retirado de uma thread à força.
4. Espera circular: A Thread 1 espera pela Thread 2 que por sua vez espera pela Thread 1.

Na versão funcional, é definido uma hierarquia de locks . Ambas as threads adquirem primeiro o Lock A e depois o Lock B, quebrando a condição de espera circular.

Pergunta - 
Como identificar visualmente que o programa entrou em deadlock?
Resposta - 
O terminal para de produzir novos logs e a execução nunca é encerrada, permanecendo travada nas chamadas do método `.join()`.

Pergunta - 
Qual é a principal diferença na logica concorrente das duas versoes?
Resposta - 
A ordem de aquisição dos recursos. A versão incorreta adquire lock de espera circular, enquanto a correta adquire locks na mesma sequencia exata em todas as theads.

Prints e Logs:
Versao incorreta:


<img width="600" height="200" alt="image"  alt="image" src="https://github.com/user-attachments/assets/407c56e4-a5ea-48c5-a260-58ab602e944f" />


Versao Correta:



<img width="600" height="200" alt="image" src="https://github.com/user-attachments/assets/894fe696-c2c3-436b-ade3-16df7731b52a" />


Tabelas de resultados:

| Versao    | sequencia thread 1    | sequencia thread 2  | comportamento do programa |

| incorreto | lock A -> lock B      | lock B -> lock A    | travamento infinito       |
| correto   | lock A -> lock B      | lock A -> lock B    | finaliza com sucesso      |
