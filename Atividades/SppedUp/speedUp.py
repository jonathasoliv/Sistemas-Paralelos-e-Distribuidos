import numpy as np
import threading
import time
# import os

# função para iniciar a contagem de tempo de uma thread


def beginTimeThread():
    global start_time_thread
    start_time_thread = time.time()


# função para encerrar a contagem de tempo de uma thread
def endTimeThread():
    global end_time_thread
    end_time_thread = time.time()
    print("Tempo decorrido: ", end_time_thread - start_time_thread)


# função para iniciar a contagem de tempo de toda a função
def beginTimeFunction():
    global start_time_function
    start_time_function = time.time()


# função para encerrar a contagem de tempo de toda a função
def endTimeFunction():

    global end_time_function, endTimeFun
    end_time_function = time.time()
    endTimeFun = end_time_function - start_time_function
    print("Tempo decorrido total: ", endTimeFun)


# definir as dimensões das matrizes
linhaA = 4
colunaA = 8
linhaB = 8
colunaB = 2

# criar as matrizes com números aleatórios
A = np.random.randint(size=(linhaA, colunaA), low=0, high=100)
B = np.random.randint(size=(linhaB, colunaB), low=0, high=100)

# inicializar a matriz C com zeros
C = np.zeros((linhaA, colunaB))


# função para criar novas matrizes aleatórias
def randomMatriz():
    global A, B, C
    A = np.random.randint(size=(linhaA, colunaA), low=0, high=10)
    B = np.random.randint(size=(linhaB, colunaB), low=0, high=10)
    C = np.zeros((linhaA, colunaB))


# função para redefinir as dimensões das matrizes
def definyDimensions(newLinhaA, newColunaA, newLinhaB, newColunaB):
    global linhaA, colunaA, linhaB, colunaB
    linhaA = newLinhaA
    colunaA = newColunaA
    linhaB = newLinhaB
    colunaB = newColunaB
    randomMatriz()
    printMatriz()


# função para imprimir as matrizes e o resultado da multiplicação
def printMatriz():
    print("Matriz A:\n", A)
    print("Matriz B:\n", B)
    print("Matriz C:\n", C)


# função para multiplicação de uma matriz por uma thread
def multiply_thread(start, end):
    global A, B, C
    for i in range(start, end):
        C[i] = np.dot(A[i], B)

# função para multiplicação de uma matriz por uma única thread


def single_thread():
    global A, B, C
    # iniciar a contagem de tempo da função
    beginTimeThread()
    # multiplicar as matrizes por uma única thread
    for i in range(0, linhaA):
        C[i] = np.dot(A[i], B)
    # encerrar a contagem de tempo da função e imprimir o resultado
    endTimeThread()
    printMatriz()

# função para multiplicação de uma matriz por duas threads


def two_threads():

    # iniciar a contagem de tempo da função
    beginTimeThread()
    # Dividir o cálculo em duas threads
    thread1 = threading.Thread(target=multiply_thread, args=(0, linhaA//2))
    thread2 = threading.Thread(
        target=multiply_thread, args=(linhaA//2, linhaA))

    # Iniciar as threads
    thread1.start()
    thread2.start()

    # Esperar as threads terminarem
    thread1.join()
    thread2.join()

    endTimeThread()
    # Printar a matriz
    printMatriz()


def four_threads():
    # Dividir o cálculo em quatro threads
    beginTimeThread()
    thread1 = threading.Thread(target=multiply_thread, args=(0, linhaA//4))
    thread2 = threading.Thread(
        target=multiply_thread, args=(linhaA//4, linhaA//2))
    thread3 = threading.Thread(
        target=multiply_thread, args=(linhaA//2, 3*linhaA//4))
    thread4 = threading.Thread(
        target=multiply_thread, args=(3*linhaA//4, linhaA))

    # Iniciar as threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    # Esperar as threads terminarem
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    endTimeThread()

    # Printar a matriz
    printMatriz()


def octa_threads():
    beginTimeThread()
    # Dividir o cálculo em oito threads
    thread1 = threading.Thread(target=multiply_thread, args=(0, linhaA//8))
    thread2 = threading.Thread(
        target=multiply_thread, args=(linhaA//8, linhaA//4))
    thread3 = threading.Thread(
        target=multiply_thread, args=(linhaA//4, 3*linhaA//8))
    thread4 = threading.Thread(
        target=multiply_thread, args=(3*linhaA//8, linhaA//2))
    thread5 = threading.Thread(
        target=multiply_thread, args=(linhaA//2, 5*linhaA//8))
    thread6 = threading.Thread(
        target=multiply_thread, args=(5*linhaA//8, 3*linhaA//4))
    thread7 = threading.Thread(
        target=multiply_thread, args=(3*linhaA//4, 7*linhaA//8))
    thread8 = threading.Thread(
        target=multiply_thread, args=(7*linhaA//8, linhaA))

    # Iniciar as threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()

    # Esperar as threads terminarem
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()

    endTimeThread()

    # Imprimir a matriz resultante
    printMatriz()


# A (8x4) x B (2x8)
def typeOfMatriz1():
    definyDimensions(4, 8, 8, 2)


# A (16x16) x B (4 x 16)
def typeOfMatriz2():
    definyDimensions(16, 16, 16, 4)


# A (64 x 32) x B (16 x 64)
def typeOfMatriz3():
    definyDimensions(32, 64, 64, 16)


# A (512 x 512) x B (64 x 512)
def typeOfMatriz4():
    definyDimensions(512, 512, 512, 64)


def menu():
    while True:
        print("Escolha uma opção:")
        print("1: Matriz (4x8)x(2x8)")
        print("2: Matriz (16x16)x(16x4)")
        print("3: Matriz (32x64)x(64x16)")
        print("4: Matriz (512x512)x(512x64)")
        print("-----------------------------------")
        print("5: Rodar Single-Thread")
        print("6: Rodar Dual-Thread")
        print("7: Rodar Quad-Thread")
        print("8: Rodar Octa-Thread")
        print("9: Sair")

        opcao = input("Opção escolhida: ")

        if opcao == "1":
            print("Você escolheu a opção 1.")
            typeOfMatriz1()
        elif opcao == "2":
            print("Você escolheu a opção 2.")
            typeOfMatriz2()
        elif opcao == "3":
            print("Você escolheu a opção 3.")
            typeOfMatriz3()
        elif opcao == "4":
            print("Você escolheu a opção 4.")
            typeOfMatriz4()
        elif opcao == "5":
            print("Você escolheu a opção 5.")
            print("Digite quantas vezes você quer que rode: ")
            timesRuns = int(input())
            beginTimeFunction()
            runs = 0
            for i in range(timesRuns):
                single_thread()
                runs += 1
            endTimeFunction()

            # adicionar informaçoes no arquivo texto
            with open("Resposta5.txt", "a") as arquivo:
                arquivo.write(str("\nO Tempo medio das vezes na opcao 5 eh: " +
                                  str(endTimeFun / runs)))
            arquivo.close()

        elif opcao == "6":
            print("Você escolheu a opção 6.")

            print("Digite quantas vezes você quer que rode: ")

            timesRuns = int(input())
            beginTimeFunction()
            runs = 0
            for i in range(timesRuns):
                two_threads()
                runs += 1
            endTimeFunction()

            # adicionar informaçoes no arquivo texto
            with open("Resposta6.txt", "a") as arquivo:
                arquivo.write(str("\nO Tempo medio das vezes na opcao 6 eh: " +
                                  str(endTimeFun / runs)))
            arquivo.close()

            # print("O Tempo medio das vezes na opcao 6 eh: " +
            # str(endTimeFun / runs))

        elif opcao == "7":
            print("Você escolheu a opção 7.")

            print("Digite quantas vezes você quer que rode: ")
            timesRuns = int(input())
            beginTimeFunction()
            runs = 0
            for i in range(timesRuns):
                four_threads()
                runs += 1
            endTimeFunction()

            # adicionar informaçoes no arquivo texto
            with open("Resposta7.txt", "a") as arquivo:
                arquivo.write(str("\nO Tempo medio das vezes na opcao 7 eh: " +
                                  str(endTimeFun / runs)))
            arquivo.close()

        elif opcao == "8":
            print("Você escolheu a opção 8.")
            print("Digite quantas vezes você quer que rode: ")
            timesRuns = int(input())
            beginTimeFunction()
            runs = 0
            for i in range(timesRuns):
                octa_threads()
                runs += 1
            endTimeFunction()

            # adicionar informaçoes no arquivo texto
            with open("Respostas8.txt", "a") as arquivo:
                arquivo.write(str("\nO Tempo medio das vezes na opcao 8 eh: " +
                              str(endTimeFun / runs)))
            arquivo.close()

        elif opcao == "9":
            print("Finalizando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()
