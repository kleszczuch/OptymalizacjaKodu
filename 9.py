import cv2
import numpy as np

image = cv2.imread('input.jpg')

#1
ex1_cv2 = cv2.add(image, 50)
ex1_np = image.astype(int) + 50
ex1_np = np.clip(ex1_np, 0, 255).astype(np.uint8)

cv2.imshow('oryginalny', image)
cv2.imshow('OpenCV +50', ex1_cv2)
cv2.imshow('NumPy +50', ex1_np)
cv2.waitKey(0)
cv2.destroyAllWindows()

#2
ex2_np = (image.astype(int) + 150) % 256
ex2_np = ex2_np.astype(np.uint8)
ex2_cv2 = cv2.add(image, 150)

cv2.imshow('Przepalenie NumPy', ex2_np)
cv2.imshow('Przepalenie OpenCV', ex2_cv2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#3
ex3_np = image.astype(int) - 80
ex3_np = np.clip(ex3_np, 0, 255).astype(np.uint8)
ex3_cv2 = cv2.subtract(image, 80)

cv2.imshow('Ciemniej NumPy', ex3_np)
cv2.imshow('Ciemniej OpenCV', ex3_cv2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#4
b, g, r = cv2.split(image)
r = cv2.add(r, 30)    
g = cv2.subtract(g, 20) 
b = cv2.add(b, 10)   
ex4 = cv2.merge([b, g, r])

cv2.imshow('Wlasny filtr', ex4)
cv2.imwrite('input2.jpg', ex4)
cv2.waitKey(0)
cv2.destroyAllWindows()

#5 
ex5_1 = cv2.imread('input.jpg')
ex5_2 = cv2.imread('input2.jpg')
diff = cv2.absdiff(ex5_1, ex5_2)

cv2.imshow('Roznice miedzy obrazami', diff)
cv2.waitKey(0)
cv2.destroyAllWindows()
