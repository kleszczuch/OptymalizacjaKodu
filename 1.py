import cv2
image = cv2.imread('guy.jpg')
(h, w) = image.shape[:2]
cv2.imshow("Original", image)

(b, g, r) = image[0, 0]
print("1: Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

image2 = image.copy()
image2[h-1, w-1] = (0, 0, 255) 
cv2.imshow("Changed2", image2)

(cX, cY) = (w // 2, h // 2)
(b, g, r) = image[cY, cX]
print("3: Pixel at center: Red: {}, Green: {}, Blue: {}".format(r, g, b))

x = input("Enter x: ")
x = int(x)
y = input("Enter y: ")
y = int(y)
if (x <0 or y<0 or x > w or y > h):
    print("Invalid input")
else:
    image4 = image.copy()
    image4[x, y] = (0, 0, 0)
    cv2.imshow("Changed4", image4)

image5 = image.copy()
image5[0:cY, 0:cX] = (255,0,0)
cv2.imshow("Changed5", image5)

image6 = image.copy()
image6[cY-50:cY+50, cX-50:cX+50] = (0,0,255)
cv2.imshow("Changed6", image6)

thirdH = h//3
thirdW = w//3
one = image[0:thirdH, 0:thirdW]
two = image[0:thirdH, thirdW:2*thirdW]
three = image[0:thirdH, 2*thirdW:w]
four = image[thirdH:2*thirdH, 0:thirdW]
five = image[thirdH:2*thirdH, thirdW:2*thirdW]
six = image[thirdH:2*thirdH, 2*thirdW:w]
seven = image[2*thirdH:h, 0:thirdW]
eight = image[2*thirdH:h, thirdW:2*thirdW]
nine = image[2*thirdH:h, 2*thirdW:w]
cv2.imshow("Changed7", five)

image8 = image.copy()
image8[100,:] = (0, 0, 255)
cv2.imshow("Changed8", image8)

image9 = image.copy()
image9[50:100, 50:100] = (255,255,255)
cv2.imshow("Changed9-before", image)
cv2.imshow("Changed9-after", image9)

image10 = image.copy()
px1 = image10[100, 100].astype(int)  # Convert to int
px2 = image10[50, 50].astype(int)    # Convert to int
roznicaB = abs(px1[0] - px2[0])
roznicaG = abs(px1[1] - px2[1])
roznicaR = abs(px1[2] - px2[2])
print("Difference in Blue: {}, Green: {}, Red: {}".format(roznicaB, roznicaG, roznicaR))


brightest = 0
brightestPixel = (0, 0)
for i in range(h):
    for j in range(w):
        (b, g, r) = image[i, j].astype(int)  
        if (b + g + r) > brightest:
            brightest = b + g + r
            brightestPixel = (i, j)
print("Brightest pixel at: {}, {}".format(brightestPixel[0], brightestPixel[1]))

cv2.waitKey(0)
cv2.destroyAllWindows()
