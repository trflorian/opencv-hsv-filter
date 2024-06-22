import cv2

img = cv2.imread("flower.png")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

win_name = "Image Filter"
cv2.namedWindow(win_name)

def emtpy_callback(_):
    pass

tb_hue_min = "Hue Min"
tb_hue_max = "Hue Max"
cv2.createTrackbar(tb_hue_min, win_name, 0, 180, emtpy_callback)
cv2.createTrackbar(tb_hue_max, win_name, 180, 180, emtpy_callback)

tb_sat_min = "Saturation Min"
tb_sat_max = "Saturation Max"
cv2.createTrackbar(tb_sat_min, win_name, 0, 255, emtpy_callback)
cv2.createTrackbar(tb_sat_max, win_name, 255, 255, emtpy_callback)

tb_val_min = "Value Min"
tb_val_max = "Value Max"
cv2.createTrackbar(tb_val_min, win_name, 0, 255, emtpy_callback)
cv2.createTrackbar(tb_val_max, win_name, 255, 255, emtpy_callback)

while True:
    hue_min = cv2.getTrackbarPos(tb_hue_min, win_name)
    hue_max = cv2.getTrackbarPos(tb_hue_max, win_name)
    sat_min = cv2.getTrackbarPos(tb_sat_min, win_name)
    sat_max = cv2.getTrackbarPos(tb_sat_max, win_name)
    val_min = cv2.getTrackbarPos(tb_val_min, win_name)
    val_max = cv2.getTrackbarPos(tb_val_max, win_name)

    # make sure the min values are less than the max values
    hue_min, hue_max = min(hue_min, hue_max), max(hue_min, hue_max)
    sat_min, sat_max = min(sat_min, sat_max), max(sat_min, sat_max)
    val_min, val_max = min(val_min, val_max), max(val_min, val_max)

    # adjust trackbar positions
    cv2.setTrackbarPos(tb_hue_min, win_name, hue_min)
    cv2.setTrackbarPos(tb_hue_max, win_name, hue_max)
    cv2.setTrackbarPos(tb_sat_min, win_name, sat_min)
    cv2.setTrackbarPos(tb_sat_max, win_name, sat_max)
    cv2.setTrackbarPos(tb_val_min, win_name, val_min)
    cv2.setTrackbarPos(tb_val_max, win_name, val_max)

    img_mask = cv2.inRange(
        img_hsv,
        (hue_min, sat_min, val_min),
        (hue_max, sat_max, val_max),
    )

    img_filtered = cv2.bitwise_and(img, img, mask=img_mask)

    cv2.imshow(win_name, img_filtered)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
