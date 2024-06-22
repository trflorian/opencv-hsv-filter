import cv2

img = cv2.imread("flower.png")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

win_name = "Image Filter"
cv2.namedWindow(win_name)

# [name, default_value, max_value]
sliders = [
    ["Hue Min", 0, 180],
    ["Hue Max", 180, 180],
    ["Sat Min", 0, 255],
    ["Sat Max", 255, 255],
    ["Val Min", 0, 255],
    ["Val Max", 255, 255],
]

for slider in sliders:
    cv2.createTrackbar(slider[0], win_name, slider[1], slider[2], lambda _: None)

while True:
    hue_min, hue_max, sat_min, sat_max, val_min, val_max = [
        cv2.getTrackbarPos(slider[0], win_name) for slider in sliders
    ]

    # make sure the min values are less than the max values
    hue_min, hue_max = min(hue_min, hue_max), max(hue_min, hue_max)
    sat_min, sat_max = min(sat_min, sat_max), max(sat_min, sat_max)
    val_min, val_max = min(val_min, val_max), max(val_min, val_max)

    sldier_values = [hue_min, hue_max, sat_min, sat_max, val_min, val_max]

    # adjust trackbar positions
    for slider, value in zip(sliders, sldier_values):
        cv2.setTrackbarPos(slider[0], win_name, value)

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
