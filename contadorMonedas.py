from cv2 import cv2
import numpy as np
#numpy, ciencia aplicada de manera simple

valorGauss=3
valorKernel=3
#tratar de usar numeros impares para pasar valores para el GAUSS, es complejo limpiar y aislar las imagenes de ruido
original=cv2.imread('monedas.jpg')
gris=cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)
gauss=cv2.GaussianBlur(gris, (valorGauss,valorGauss),0)
#valor de matrices gaus y kernel
#metodo gaussiano, toma valores en forma de matriz para dividir 1
#entre x.x (valores pasados por parametro), para generar un solo resultado para ese pixel, de esa manera se genra el blur (desenfoque)
#tener cuidado con los valores de la matriz para no hjacerlo demasiado borroso
canny=cv2.Canny(gauss,60,100)
kernel=np.ones((valorKernel, valorKernel), np.uint8)
#transformamos en una matriz de 8 bites
cierre=cv2.morphologyEx(canny, cv2.MORPH_CLOSE , kernel)



contornos, jerarquia=cv2.findContours(cierre.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

print("monedas encontradas: {}".format(len(contornos)))

"""
cv2.drawContours(original, contornos, -1, (0,0,255), 2)
#mostrar
cv2.imshow("grises",gris)
cv2.imshow("gauss", gauss)
cv2.imshow("canny", canny)
cv2.imshow("cierre", cierre)
cv2.imshow("resultado", original)


cv2.waitKey(0)
"""