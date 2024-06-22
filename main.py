import cv2

win_name = "Image Filter"
cv2.namedWindow(win_name)

cv2.createTrackbar("Hue Min", win_name, 45, 180, lambda x: None)
cv2.createTrackbar("Hue Max", win_name, 80, 180, lambda x: None)

cv2.createTrackbar("Sat Min", win_name, 0, 255, lambda x: None)
cv2.createTrackbar("Sat Max", win_name, 255, 255, lambda x: None)

cv2.createTrackbar("Val Min", win_name, 0, 255, lambda x: None)
cv2.createTrackbar("Val Max", win_name, 100, 255, lambda x: None)


img = cv2.imread("flower.png")

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

while True:
    hue_min = cv2.getTrackbarPos("Hue Min", win_name)
    hue_max = cv2.getTrackbarPos("Hue Max", win_name)

    sat_min = cv2.getTrackbarPos("Sat Min", win_name)
    sat_max = cv2.getTrackbarPos("Sat Max", win_name)

    val_min = cv2.getTrackbarPos("Val Min", win_name)
    val_max = cv2.getTrackbarPos("Val Max", win_name)

    img_mask = cv2.inRange(
        img_hsv, lowerb=(hue_min, sat_min, val_min), upperb=(hue_max, sat_max, val_max)
    )

    img_filtered = cv2.bitwise_and(img, img, mask=img_mask)

    cv2.imshow("Image Filtered", img_filtered)
    cv2.imshow("Mask", img_mask)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cv2.destroyAllWindows()
