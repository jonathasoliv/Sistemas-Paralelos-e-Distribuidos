import cv2
import numpy as np


image = cv2.imread("maspcomruido.jpg", 0) #trabalhando com imagem de um canal 0 (escala de cinza)

altura, largura = image.shape
newimage = np.zeros((altura, largura),dtype = 'uint8')  

#print(image.dtype.type) mostra o tipo da imagem do uint8, no caso do exemplo é inteiro de 8 bits

# Filtro média 3x3
for y in range(1, altura - 1):  #colocar esse for no comentario - processamento distribuido- do slide MPI 
    for x in range(1, largura - 1):
        media = int(image[y - 1][x - 1]) + int(image[y - 1][x]) + int(image[y - 1][x + 1]) #1º linha
        media += int(image[y][x - 1]) + int(image[y][x]) + int(image[y][x + 1])             #2º linha
        media += int(image[y + 1][x - 1]) + int(image[y + 1][x]) + int(image[y + 1][x + 1]) #3º linha

        media = int(media / 9)

        newimage[y][x] = media

cv2.imshow("original image", image)
cv2.imshow("filtered image", newimage)

cv2.waitKey(0) #aguarda até clicar qualquer tecla para fechar a imagem. 
cv2.destroyAllWindows()


#recolhendo entre processos colocar o nome localnewimage no lugar de localimage