import threading
import time

count = 0

# o T é a quantidade de threads, enquanto o M é a quanidade de incrementos que cada um dos threads vai fazer.
T = 8
M = 200_000

#Semáforo em binário (só 1 thread pode funcionar por vez)
sem = threading.Semaphore(1)


def tarefa():
    global count    #Faz a alteração da variavel count.

    for _ in range(M):

        # tenta pegar o semáforo em binario, se nao der pq um thread já estiver usando, ele espera.
        sem.acquire()

        try:
            count += 1
            # apenas uma thread por vez pode executar este trecho


        finally:
            sem.release()
        # libera o semáforo mesmo se acontecer erro

#Ini é inicio, tava com preguiça de escrever :P
ini = time.perf_counter()

#Cria uma lista que vai armazenar os threads.
threads = []


#Cria uma thread q vai fazer a tarefa, executa a função da thread e adiciona na lista.
for _ in range(T):
    t = threading.Thread(target=tarefa)
    threads.append(t)
    t.start()


#espera todas as threads terminarem pra nao dar ruim.
for t in threads:
    t.join()


#acaba o bagulho.
fim = time.perf_counter()

print (f"O que estavamos esperando:{T*M}")
print (f"Resultado que conseguimos:{count}")
print (f"Tempo que demorou:{fim - ini:.4f}s")

























