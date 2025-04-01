import numpy as np
import cv2
blue = (255, 0, 0)
green = (0, 255, 0)
red = (0, 0, 255)
white = (255, 255, 255)
#1
canvas = np.zeros((300, 300, 3), dtype="uint8")
cv2.line(canvas, (150, 150), (300, 300), blue, 2)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
#2
canvas = np.zeros((400, 400, 3), dtype="uint8")
blue = (255, 0, 0)
cv2.rectangle(canvas, (0, 0), (150, 50), green)
cv2.rectangle(canvas, (250, 350), (400, 400), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#3
canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
cv2.circle(canvas, (centerX-100, centerY-100),40,blue)
cv2.circle(canvas, (centerX+50, centerY+50),60,red)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#4
canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
cv2.rectangle(canvas, (centerX-50, centerY-50), (centerX+50, centerY+50), green)
cv2.circle(canvas, (centerX, centerY),30,red)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#5
canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
for i in range(0, 300, 20):
    cv2.rectangle(canvas, (centerX -i, centerY -i), (centerX +i, centerY +i), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

#6
canvas = cv2.imread('18.03/zadanie6.jpg')
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
oczy_lewy = (300, 125)  
oczy_prawy = (355, 125) 
usta_gora_lewo = (290, 160)  
usta_dol_prawo = (380, 175)  
srodek_twarzy = (325, 120) 
promien_twarzy = 100 
cv2.circle(canvas, oczy_lewy, 30, (0, 0, 255), -1)  
cv2.circle(canvas, oczy_prawy, 30, (0, 0, 255), -1)
cv2.rectangle(canvas, usta_gora_lewo, usta_dol_prawo, (0, 255, 0), -1)
cv2.circle(canvas, srodek_twarzy, promien_twarzy, (255, 0, 0), 2)
cv2.imshow("Canvas", canvas)


cv2.waitKey(0)
