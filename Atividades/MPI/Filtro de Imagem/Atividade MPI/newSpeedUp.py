import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
myrank = comm.Get_rank()
nprocs = comm.Get_size()

linhaA = None
colunaA = None
linhaB = None
colunaB = None
A = None
B = None
C = None
D = None

if myrank == 0:
    linhaA = 4
    colunaA = 8
    linhaB = 8
    colunaB = 2
    A = np.random.randint(low=0, high=100, size=(linhaA, colunaA))
    B = np.random.randint(low=0, high=100, size=(linhaB, colunaB))
    C = np.zeros((linhaA, colunaB))
    n = linhaA // nprocs

n = comm.bcast(n, root=0)
D = np.zeros((n, colunaA))

# Scatter matriz A para todos os processos
comm.Scatter(A, D, root=0)

# Broadcast matriz B para todos os processos
B = comm.bcast(B, root=0)

# Multiplicação de matrizes localmente
F = np.dot(D, B)

# Gather resultados parciais de volta para o processo 0
comm.Gather(F, C, root=0)

if myrank == 0:
    print("Resultado da multiplicação:")
    print(C)