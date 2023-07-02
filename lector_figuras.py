import cv2
#Leemos la imagen primero
image = cv2.imread('figurasColores.png')
#La transformamos a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#Obtener una imagen binarizada para eso necesitamos detectar
#bordes de nuestra imagen
canny =cv2.Canny(gray,10,150)
#Aplicamos dilatación y eroción para mejorar imagen binaria
canny = cv2.dilate(canny, None, iterations=1)
canny = cv2.erode(canny, None, iterations=1)
th = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
#Encontramos contornos
cnts,_=cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)#oPENcv 

#PAra analizar los contornos hacemos lo siguiente
for c in cnts:
    #etermino epsilon(determina la precisión de aproximación
    # Caluclo de perimetro del contorno o la longitud de curva)
    epsilon = 0.01*cv2.arcLength(c,True)
    #Explicamos contorno
    approx = cv2.approxPolyDP(c,epsilon,True)
    #print(len(approx))
    x,y,w,h = cv2.boundingRect(approx)
    if len(approx)==3:
        cv2.putText(image,'Triangulo',(x,y-5),1,1.5,(0,255,0),2)
    if len(approx)==4:
        aspect_ratio = float(w)/h
        print('aspect_ratio= ', aspect_ratio)
        if aspect_ratio == 1:
            cv2.putText(image,'Cuadrado', (x,y-5),1,1.5,(0,255,0),2)
        else:
            cv2.putText(image,'Rectangulo', (x,y-5),1,1.5,(0,255,0),2)
    if len(approx)==5:
        cv2.putText(image,'Pentagono',(x,y-5),1,1.5,(0,255,0),2)
    if len(approx)==6:
        cv2.putText(image,'Hexagono', (x,y-5),1,1.5,(0,255,0),2)
    if len(approx)>10:
        cv2.putText(image,'Circulo', (x,y-5),1,1.5,(0,255,0),2)

    cv2.drawContours(image, [approx], 0, (0,255,0),2)
    cv2.imshow('image',image)
    cv2.waitKey(0)
#Cerrar ventanas abiertas
cv2.destroyAllWindows()