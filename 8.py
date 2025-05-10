import cv2
import numpy as np

image = cv2.imread('input.jpg')

#1 
ex1 = image[0:100, 0:100]
cv2.imshow('lewy gorny rog', ex1)

#2 
h, w = image.shape[:2]
ex2 = image[h//2:h, 0:w]
cv2.imshow('Dolna polowa', ex2)

#3
ex3 = image[0:h, w//2:w]
cv2.imshow('Prawa polowa', ex3)

#4
print("Podaj startX):")
startX = int(input())
print("Podaj endX):")
endX = int(input())
print("Podaj startY):")
startY = int(input())
print("Podaj endY):")
endY = int(input())
ex4= image[startY:endY, startX:endX]
cv2.imshow('Podane przez uzytkownika', ex4)

#5
ex5 = image[170:220, 120:190]
cv2.imshow('Twarz', ex5)

#6
piece = image[170:220, 120:190].copy()
ex6 = image.copy()
ex6[0:50, 0:70] = piece
cv2.imshow('Po wklejeniu fragmentu', ex6)

#7
h3, w3 = h//3, w//3
for i in range(3):
    for j in range(3):
        ex7 = image[i*h3:(i+1)*h3, j*w3:(j+1)*w3]
        cv2.imshow(f'Siatka {i},{j}', ex7)

#8
for x in range(0, w-100, 10):
    ex8 = image[0:100, x:x+100]
    cv2.imshow('Animacja ROI', ex8)
    key = cv2.waitKey(0)
    if key == 27:  
        break

#9 
ex9 = image[0:300, 0:300]
cv2.imwrite('cropped_image.jpg', ex9)
cv2.imshow('Cropped 300x300', ex9)

cv2.waitKey(0)
cv2.destroyAllWindows()
