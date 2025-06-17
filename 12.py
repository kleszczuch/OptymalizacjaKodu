import cv2
import numpy as np

# 1.
image = cv2.imread("photo.jpg")
cv2.imshow("original", image)
B, G, R = cv2.split(image)
cv2.imshow("B", B)
cv2.imshow("G", G)
cv2.imshow("R", R)
cv2.imwrite("B.jpg", B)
cv2.imwrite("G.jpg", G)
cv2.imwrite("R.jpg", R)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 2. 
image = cv2.imread("photo2.jpg")
cv2.imshow("original", image)
B, G, R = cv2.split(image)
cv2.imshow("B", B)
cv2.imshow("G", G)
cv2.imshow("R", R)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 3. 
image = cv2.imread("photo3.jpg")
B, G, R = cv2.split(image)
img_rbg = cv2.merge([R, B, G])
cv2.imshow("Photo R, B, G", img_rbg)
G_zero = np.zeros_like(G)
img_no_green = cv2.merge([B, G_zero, R])
cv2.imshow("No green", img_no_green)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 4. 
image = cv2.imread("photo.jpg")
B, G, R = cv2.split(image)
R_boosted = cv2.add(R, 50)
img_boosted = cv2.merge([B, G, R_boosted])
cv2.imshow("Red BOOST", img_boosted)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 5. 
image = cv2.imread("Red.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_red1 = np.array([0, 120, 100])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 100])
upper_red2 = np.array([180, 255, 255])
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = cv2.bitwise_or(mask1, mask2)
cv2.imshow("Red Mask", mask)
B, G, R = cv2.split(image)
R_mod = cv2.add(R, 60, dst=None, mask=mask)
result = cv2.merge([B, G, R_mod])
cv2.imshow("Red BOOST", result)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 6. 
logo = cv2.imread("opencv_logo.png")
B, G, R = cv2.split(logo)
cv2.imshow("B", B)
cv2.imshow("G", G)
cv2.imshow("R", R)
cv2.waitKey(0)
logo_swap = cv2.merge([R, G, B])
cv2.imshow("red to blue", logo_swap)
cv2.waitKey(0)
G_zero = np.zeros_like(G)
logo_no_green = cv2.merge([B, G_zero, R])
cv2.imshow("No green", logo_no_green)
cv2.waitKey(0)
cv2.destroyAllWindows()