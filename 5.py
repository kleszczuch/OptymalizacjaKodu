import argparse
import time
import imutils
import cv2
image = cv2.imread("Maklowicz.jpg")
cv2.imshow("Original", image)
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
ex1 = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 Degrees", ex1)

M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
ex2 = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -90 Degrees", ex2)

M = cv2.getRotationMatrix2D((0, 0), 30, 1.0)
ex3 = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 30 Degrees to 0,0", ex3)

x = input("Podaj kat obrotu: ")
x = int(x)
M = cv2.getRotationMatrix2D((cX, cY), x, 1.0)
ex4 = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by x Degrees", ex4)

ex5 = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 Degrees", ex5)


ex6 = imutils.rotate_bound(image, -33)
cv2.imshow("Rotated Without Cropping", ex6)

ex7a = imutils.rotate(image, 60)
M = cv2.getRotationMatrix2D((cX, cY), 60, 1.0)
ex7b = cv2.warpAffine(image, M, (w, h))
cv2.imshow("warpAffine", ex7b)
cv2.imshow("imutils", ex7a)

for _ in range (3):
    ex8 = imutils.rotate_bound(image, 30 * _)
    cv2.waitKey(1)
    cv2.imshow("Rotated Without Cropping", ex8)

ex9 = imutils.rotate(image, 75)
cv2.imwrite('rotaded75.png', ex9)


kat = 0
while True:
    M = cv2.getRotationMatrix2D((cX, cY), kat, 1.0)
    ex10 = cv2.warpAffine(image, M, (w, h))
    cv2.imshow("SPIN", ex10)
    cv2.waitKey(1) 
    kat += 5  
    time.sleep(0.01) 
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cv2.waitKey(0)