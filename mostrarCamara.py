import cv2 as cv

capturaVideo=cv.VideoCapture(0)#cero porque esta dentro de la pc

if not capturaVideo.isOpened():
    print("no se encontro la camara")
    exit()

while True:
    tipoCamara,Camara=capturaVideo.read()
    grises=cv.cvtColor(Camara, cv.COLOR_BGR2GRAY)

    cv.imshow("camara en vivo", grises)
    if cv.waitKey(1)==ord("q"):
        break

#siempre ponerle condicion para que se detenga el video, el estado siempre es en 1
capturaVideo.release()
cv.destroyAllWindows()
