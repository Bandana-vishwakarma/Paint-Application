import cv2

"""...........to read and display image............."""

img = cv2.imread("logan-weaver-QoZRUI6LdKw-unsplash.jpg", 1)

scaled_img = cv2.resize(img, (500, 500))

cv2.imshow("image", scaled_img)
cv2.waitKey(10000)
cv2.destroyAllWindows()

