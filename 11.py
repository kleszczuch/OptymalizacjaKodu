import cv2
import numpy as np

image = cv2.imread('person.jpg')
h, w = image.shape[:2]

#1 
maskface = np.zeros((h, w), dtype=np.uint8)
cv2.ellipse(maskface, 
           (523, 130),  # centrum
           (100, 100),  # osie (dostosuj rozmiar)
           0, 0, 360, 
           255, -1)
ex1 = cv2.bitwise_and(image, image, mask=maskface)

cv2.imshow('1. Mask face',maskface)
cv2.imshow('1. ex1', ex1)

cv2.waitKey(0)
cv2.destroyAllWindows()

#2 
maskeyes = np.ones((h, w), dtype=np.uint8) * 255
cv2.rectangle(maskeyes, 
             (720, 230), 
             (740, 250), 
             0, -1)
cv2.rectangle(maskeyes, 
             (750, 230), 
             (770, 250), 
             0, -1)
eyeCensure = cv2.bitwise_and(image, image, mask=maskeyes)


cv2.imshow('2. eye mask', maskeyes)
cv2.imshow('2. ex2', eyeCensure)
cv2.waitKey(0)
cv2.destroyAllWindows()

#3

input = cv2.imread("input.jpg")
hsv = cv2.cvtColor(input, cv2.COLOR_BGR2HSV)

lower_blue = np.array([90, 70, 50])
upper_blue = np.array([130, 255, 255])
mask_kolor = cv2.inRange(hsv, lower_blue, upper_blue)

kolor_wyr = cv2.bitwise_and(input, input, mask=mask_kolor)
mask_inv = cv2.bitwise_not(mask_kolor)
przyciemnione = cv2.addWeighted(input, 0.2, 
                               np.zeros_like(input), 0, 0)
wynik = cv2.bitwise_or(kolor_wyr, 
                       cv2.bitwise_and(przyciemnione, przyciemnione, mask=mask_inv))

cv2.imshow('3. Maska koloru', mask_kolor)
cv2.imshow('3. Ekstrakcja niebieskiego', wynik)

cv2.waitKey(0)
cv2.destroyAllWindows()