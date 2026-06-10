import threading
import time 

Lock_A = threading.Lock()
Lock_B = threading.Lock()

def threadnumero1():
    print("O primeiro thread vai tentar adquirir o Lock A")

    with Lock_A:
        print("O primeiro thread pegou o Lock A")
        time.sleep(0.05)
        print("O primeiro thread vai tentar adquirir o Lock B")
        with Lock_B:
            print("O Primeiro thread entrou na area de situação critica")
            time.sleep(0.05)

    print("O primeiro thread concluiu a operação.")

def threadnumero2():
    print("O segundo thread vai tentar adquirir o Lock A")

    with Lock_A:
        print("O Segundo thread pegou o Lock A")
        time.sleep(0.05)
        print("O Segundo thread vai tentar adquirir o Lock B")
        with Lock_B:
            print("O segundo thread entrou na area de situação critica")
            time.sleep(0.05)

    print("O segundo thread concluiu a operação.")

T1 = threading.Thread(target=threadnumero1)
T2 = threading.Thread(target=threadnumero2)

T1.start()
T2.start()

T1.join()
T2.join()

print("O programa deu tudo certo no final.")