from cv2 import arcLength, cv2
import numpy as np
from numpy.lib.function_base import iterable

def ordenarPuntos(puntos):
    #videos es siempre una matriz, hay que volverlas una sola
    n_puntos=np.concatenate(puntos[0],puntos[1],puntos[2],puntos[3]).tolist()
    y_order=sorted(n_puntos, key=lambda n_puntos:n_puntos[1])

    x1_order=y_order[:2]
    x1_order=sorted(x1_order, key=lambda x1_order:x1_order[0])

    x2_order=y_order[2:4]
    x2_order=sorted(x2_order, key=lambda x2_order:x2_order[0])

    return [x1_order[0],x1_order[1],x2_order[0],x2_order[1]]

def alineamiento(imagen, ancho, alto):
    imagen_alineada=None
    grises=cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    tipoUmbral, umbral=cv2.threshold(grises, 150, 255 , cv2.THRESH_BINARY)
    cv2.inshow("umbral", umbral)
    contorno, jerarquia=cv2.findContours(umbral. cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    contorno=sorted(contorno, key=cv2.contourArea, reverse=True)[:1]

    for c in contorno:
        epsilon=0.01*cv2.arcLength(c, True)
        approximacion=cv2.approxPolyDP(c,epsilon, True)
        if len(approximacion)==4:
            puntos=ordenarPuntos(approximacion)
            puntos1=np.float32(puntos)
            puntos2=np.float32([0,0], [ancho,0], [0,alto], [ancho,alto])
            M = cv2.getPerspectiveTransform(puntos1, puntos2)
            imagen_alineada=cv2.warpPerspective(imagen, M, (ancho, alto))
    return imagen_alineada

capturavideo=cv2.videoCapture(0)

while True:
    tipoCamara,Camara=capturavideo.read()
    if tipoCamara==False:
        break
    imagen_A6=alineamiento(Camara, ancho=480,alto=677)
    

    if imagen_A6 is not None:
        puntos=[]
        imagen_gris=cv2.cvtColor(imagen_A6,cv2.COLOR_BGR2GRAY)
        blur=cv2.GaussianBlur(imagen_gris,(5,5),1)
        tipoUmbral, umbral2=cv2.threshold(blur, 0, 255 , cv2.THRESH_OTSU+cv2.THRESH_BINARY_INV)
        #se trabajan dos veces los thresh, todo inverso para el umbral

        cv2.imshow("umbral", umbral2)
        contorno2, jerarquia2=cv2.findContours(umbral2, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
        cv2.drawContours(imagen_A6,umbral2, -1, (255,0,0),2)
        suma1=0.0
        suma2=0.0

        for c_2 in contorno2:
            area=cv2.contourArea(c_2)
            Momentos=cv2.moments(c_2)
            if(Momentos["m00"]==0):
                Momentos["m00"]=1.0
            x=int(Momentos["m10"]/Momentos["m00"])
            y=int(Momentos["m01"]/Momentos["m00"])

            if area<9300 and area>8000:
                font=cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(imagen_A6, "S/ . 0.20", (x,y), font, 0.75, (0,255,0),2)
                suma1=suma1+0.2

            if area<7800 and area>6500:
                font=cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(imagen_A6, "S/ . 0.10", (x,y), font, 0.75, (0,255,0),2)
            suma1=suma2+0.1

        total=suma1+suma2
        print("Sumatoria total en centimos:", round (total,2) )
        cv2.imshow("Imagen a6", imagen_A6)
        cv2.imshow("umbral", umbral2)
        

    if cv2.waitKey(1)==ord("s"):
        break
capturavideo.release()
cv2.destroyAllWindows()
    
#tomar aspect ratio del ancho/alto para los pixeles, 9/conv. unit 5