import threading
import time

filosofoes = 5
garfos = [threading.Lock() for _ in range(filosofoes)]

def filosofosos(g):
    garfo1 = g
    garfo2 = (g+1) % filosofoes
    primeiramao = min(garfo1, garfo2)
    segundamao = max(garfo1, garfo2)

    pensa(g)

    print(f"Filósofo {g} está com fominha")
    print(f"\n")

    garfos[primeiramao].acquire()
    print(f"Filósofo {g} pegou o garfo {primeiramao} e está resenhando")
    print(f"\n")

    pensa(g)

    garfos[segundamao].acquire()
    print(f"Filósofo {g} pegou o garfo {segundamao} e ainda está resenhando")
    print(f"\n")

    come(g)

    garfos[segundamao].release()
    garfos[primeiramao].release()
    print(f"Filósofo {g} terminou de comer e voltou a resenhar")
    print(f"\n")

def pensa(g):
    print(f"Filósofo {g} está pensando...")
    print(f"\n")
    time.sleep(0.1)

def come(g):
    print(f"Filósofo {g} parou de resenhar e começou a comer...")
    print(f"\n")
    time.sleep(0.1)

threads = []

for i in range(filosofoes):
    t = threading.Thread(target=filosofosos, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()