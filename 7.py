import cv2

image = cv2.imread("Maklowicz.jpg")
cv2.imshow("Original", image)

ex1 = cv2.flip(image, 1)
cv2.imshow("ex1", ex1)

ex2 = cv2.flip(image, 0)
cv2.imshow("ex2", ex2)

ex3 = cv2.flip(image, 1)
ex3 = cv2.flip(ex3, 0)
cv2.imshow("ex3", ex3)

#ex4 - porowaninie wynikow 1 2 3 

ex5 = image.copy()
wysokosc, szerokosc, channels  = ex5.shape
x1, y1 = szerokosc // 4, wysokosc // 4
x2, y2 = szerokosc // 2, wysokosc // 2 
toFlip = ex5[y1:y2, x1:x2]

flipped = cv2.flip(toFlip, 1) 

ex5[y1:y2, x1:x2] = flipped

cv2.imshow("ex5", ex5)

x = input("podaj obrót \n 0 – pionowe\n 1 – poziome \n-1 – oba") 
if x == "0":
    ex6 = cv2.flip(image, 0)
elif x == "1":
    ex6 = cv2.flip(image, 1)
elif x == "-1":
    ex6 = cv2.flip(image, -1)
else:
    print("Niepoprawny wybór")

cv2.imshow("ex6", ex6)
cv2.waitKey(0)