import numpy as np
import cv2
import imutils
# 1.
image = cv2.imread("img.jpg")
cv2.imshow("Orginal", image)
cv2.waitKey(0)
M = np.float32([[1, 0, 30], [0, 1, 40]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted", shifted)
cv2.waitKey(0)
# 2
image = cv2.imread("img.jpg")
M = np.float32([[1, 0, -20], [0, 1, -50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted", shifted)
cv2.waitKey(0)
# 3
image = cv2.imread("img.jpg")
M = np.float32([[1, 0, 330], [0, 1, 330]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Experimental", shifted)
cv2.waitKey(0)
# 4
image = cv2.imread("img.jpg")
shifted = imutils.translate(image, 100, 50)
cv2.imshow("Imutils", shifted)
cv2.waitKey(0)
# 5
cv2.destroyAllWindows()
image = cv2.imread("img.jpg")
print("Podaj przesuniecie Prawo lewo:")
tx = input() 
print("Podaj przesuniecie góra dół:")
ty = input()
M = np.float32([[1, 0, tx], [0, 1, ty]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Output", shifted)
cv2.waitKey(0)
