import cv2

img = cv2.imread("flower.png")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

win_name = "Image Filter"
cv2.namedWindow(win_name)

channel_max_values = {
    "Hue": 180,
    "Saturation": 255,
    "Value": 255,
}

filter_values = {
    "Hue Min": 0,
    "Hue Max": 180,
    "Saturation Min": 0,
    "Saturation Max": 255,
    "Value Min": 0,
    "Value Max": 255,
}

def show_filtered_image():
    img_mask = cv2.inRange(
        img_hsv,
        lowerb=(filter_values["Hue Min"], filter_values["Saturation Min"], filter_values["Value Min"]),
        upperb=(filter_values["Hue Max"], filter_values["Saturation Max"], filter_values["Value Max"]),
    )

    img_filtered = cv2.bitwise_and(img, img, mask=img_mask)

    cv2.imshow(win_name, img_filtered)

def on_filter_value_changed(trackbar_name, new_value):
    global filter_values
    filter_values[trackbar_name] = new_value
    show_filtered_image()

for channel_name, channel_max_value in channel_max_values.items():
    trackbar_name_min = f"{channel_name} Min"
    trackbar_name_max = f"{channel_name} Max"

    filter_values[trackbar_name_min] = 0
    filter_values[trackbar_name_max] = channel_max_value

    cv2.createTrackbar(trackbar_name_min, win_name, 0, channel_max_value, lambda value, trackbar_name=trackbar_name_min: on_filter_value_changed(trackbar_name, value))
    cv2.createTrackbar(trackbar_name_max, win_name, channel_max_value, channel_max_value, lambda value, trackbar_name=trackbar_name_max: on_filter_value_changed(trackbar_name, value))


while True:
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cv2.destroyAllWindows()
