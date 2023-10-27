import cv2
import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
nprocs = comm.Get_size()
myrank = comm.Get_rank()

newimage = None
image = None
n = 0
largura = 0

if myrank == 0:
    image = cv2.imread("maspcomruido.jpg", 0)
    altura, largura = image.shape
    n = int (altura/nprocs)
    newimage = np.zeros((altura,largura), dtype = 'uint8')

(n, largura) = comm.bcast((n,largura), root=0)
localimage = np.zeros((n, largura), dtype='uint8')
newlocalimage = np.zeros((n, largura), dtype='uint8')
comm.Scatterv(image, localimage, root= 0)

#Distribuindo entre os processos

for y in range(1, n - 1):  #colocar esse for no comentario - processamento distribuido- do slide MPI 
    for x in range(1, largura - 1):
        media = int(localimage[y - 1][x - 1]) + int(localimage[y - 1][x]) + int(localimage[y - 1][x + 1]) #1º linha
        media += int(localimage[y][x - 1]) + int(localimage[y][x]) + int(localimage[y][x + 1])             #2º linha
        media += int(localimage[y + 1][x - 1]) + int(localimage[y + 1][x]) + int(localimage[y + 1][x + 1]) #3º linha

        media = int(media / 9)
        newlocalimage[y][x] = media
        
cv2.imshow("imagem cortada", newlocalimage) #imagens partidas

#recolhendo entre os processos
comm.Gatherv(newlocalimage, newimage, root=0)
if myrank == 0:
    cv2.imshow("imagem original", image)
    cv2.imshow("imagem filtrada", newimage)
    cv2.waitKey(0)

cv2.destroyAllWindows

