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
