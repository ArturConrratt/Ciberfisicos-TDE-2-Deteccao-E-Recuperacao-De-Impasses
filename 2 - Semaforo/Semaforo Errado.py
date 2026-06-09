import threading
import time

count = 0 

# o T é a quantidade de threads, enquanto o M é a quanidade de incrementos que cada um dos threads vai fazer.
T = 8
M = 200_000

def tarefa():
    global count       #Faz a alteração da variavel count.

    for _ in range(M):
        valor = count
        valor += 1
        count = valor
        #pega o valor, soma 1 e depois substitui pelo novo.


#Ini é inicio, tava com preguiça de escrever :P
ini = time.perf_counter()


#Cria uma lista que vai armazenar os threads.
thread = []

#Cria uma thread q vai fazer a tarefa, executa a função da thread e adiciona na lista.
for _ in range (T):
    t = threading.Thread(target=tarefa)
thread.append(t)
t.start()

#espera todas as threads terminarem pra nao dar ruim.
for t in thread:
    t.join()

#acaba o bagulho.
fim = time.perf_counter()

print (f"O que estavamos esperando:{T*M}")
print (f"Resultado que conseguimos:{count}")
print (f"Tempo que demorou:{fim - ini:.4f}s")



























