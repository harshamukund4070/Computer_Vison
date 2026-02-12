import cv2
img = cv2.imread("image-1.png")
clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
counter_clockwise = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("Original Image", img)
cv2.imshow("Clockwise Rotation", clockwise)
cv2.imshow("Counter Clockwise Rotation", counter_clockwise)
cv2.waitKey(0)
cv2.destroyAllWindows()