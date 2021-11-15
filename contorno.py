from cv2 import cv2

imagen2=cv2.imread('contorno.jpg')

imagenAgrises=cv2.cvtColor(imagen2,cv2.COLOR_BGR2GRAY)

tipoUmbral, umbral=cv2.threshold(imagenAgrises, 100, 255 , cv2.THRESH_BINARY)

contorno, jerarquia=cv2.findContours(umbral, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(imagen2, contorno, -1, (251,63,52), 3)
#los metodos de encontrarContorno(imagen, modo(tipo de dato devuelto), tipo de contorno(simple de ser posible))
#googlear funciones, hace de color a blanco y negro la imagen
#_ guion bajo para que la 1ra variable a devolver sea un NULL
#cv.drawContours(img, contours, -1, (0,255,0), 3) -1 es el ultimo punto de contorno en la lista, color RGB, grosor
#just color picker te da el resultado en rgb a utilizar

#mostrar
cv2.imshow('imagen',imagen2)
cv2.imshow('Hola soy una imagen',imagenAgrises)
cv2.imshow('hola soy el umbral',umbral)
cv2.waitKey(0)
#uno(1) es para videos para un valor constante durante toda la ejecucion 
cv2.destroyAllWindows()