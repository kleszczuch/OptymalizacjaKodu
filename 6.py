import cv2
import imutils

image = cv2.imread("Maklowicz.jpg")
cv2.imshow("Original", image)

resized = cv2.resize(image, (150, 150), interpolation=cv2.INTER_AREA)
cv2.imshow("Resized", resized)


ex1 = image.copy()
height, width, channels = ex1.shape
halfWidth = int(width / 2)
halfHeight = int(height / 2)
ex1 = cv2.resize(ex1, (halfHeight, halfWidth), interpolation=cv2.INTER_AREA)
cv2.imshow("ex1", ex1)

ex2 = image.copy()
height, width, channels = ex1.shape
doubleWidth = int(width * 2)
ex2 = imutils.resize(ex2, doubleWidth, inter=cv2.INTER_LINEAR)
cv2.imshow("ex2", ex2)

ex3 = image.copy()
ex3 = cv2.resize(ex3, (300, 300), interpolation=cv2.INTER_AREA)
cv2.imshow("ex3", ex3)



methods = [
("ex4.INTER_NEAREST", cv2.INTER_NEAREST),
("ex4.INTER_LINEAR", cv2.INTER_LINEAR),
("ex4.INTER_AREA", cv2.INTER_AREA),
("ex4.INTER_CUBIC", cv2.INTER_CUBIC),
("ex4.INTER_LANCZOS4", cv2.INTER_LANCZOS4)]
for (name, method) in methods:
    ex4 = image.copy()
    height, width, channels = ex4.shape
    ex4 = imutils.resize(ex4, width=image.shape[1] * 3, inter=method)
    cv2.imshow(name, ex4)


ex5 = image.copy()
ex5 = imutils.resize(ex5, width = 500)
cv2.imshow("ex5", ex5)

ex6 = image.copy()
ex6 = imutils.resize(ex6, height = 400)
cv2.imshow("ex6", ex6)

ex7 = image.copy()
height, width, channels = ex7.shape
fifthWidth = int(width / 5)
ex7 = imutils.resize(ex7, fifthWidth, inter=cv2.INTER_AREA)
cv2.imshow("ex7", ex7)

ex8 = image.copy()
height, width, channels = ex8.shape
forhWidth = int(width * 4)
ex8a = imutils.resize(ex8, forhWidth, inter=cv2.INTER_CUBIC)
ex8b = imutils.resize(ex8, forhWidth, inter=cv2.INTER_LANCZOS4)
cv2.imshow("ex8a", ex8a)
cv2.imshow("ex8b", ex8b)


ex9 = image.copy()
height, width, channels = ex9.shape
for x in range(100, 301, 20):
    larger = int(height * x / 100)  
    ex9 = imutils.resize(ex9, width=larger)

    cv2.imshow("ex9", ex9)
    cv2.waitKey(500)  


ex10 = image.copy()
height, width, channels = ex10.shape
ex10 = cv2.resize(image, (800, height), interpolation=cv2.INTER_AREA)
cv2.imshow("ex10", ex10)
cv2.imwrite("resized_output.jpg", ex10)

cv2.waitKey(0)  