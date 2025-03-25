import cv2
image = cv2.imread("Podsiadlo.png")
(h, w, c) = image.shape[:3]
cv2.namedWindow("Wyświetlony obraz", cv2.WINDOW_NORMAL)
cv2.imshow("Wyświetlony obraz", image) 
print("kolor:")
print(f'width: {w} pixels')
print(f'height: {h} pixels')
print(f'channels: {c}')

image_gray = cv2.imread("Podsiadlo.png",cv2.IMREAD_GRAYSCALE)
(h, w) = image_gray.shape[:3]
cv2.namedWindow("Obraz w skali szarości", cv2.WINDOW_NORMAL)
cv2.imshow("Obraz w skali szarości", image_gray)
print("Czarno bialy:")
print(f'width: {w} pixels')
print(f'height: {h} pixels')
print(f'channels: NONE')
save = cv2.imwrite('output.jpg', image_gray)

if save:
        print("Obraz zapisany pomyślnie!")
else:
        print("Wystąpił problem podczas zapisywania obrazu.")
while True:
    if cv2.getWindowProperty("Wyświetlony obraz", cv2.WND_PROP_VISIBLE) < 1 and \
       cv2.getWindowProperty("Obraz w skali szarości", cv2.WND_PROP_VISIBLE) < 1:
        break
    cv2.waitKey(100)

cv2.destroyAllWindows()

 