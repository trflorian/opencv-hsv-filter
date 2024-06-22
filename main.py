import cv2

img = cv2.imread("flower.png")

win_name = "Image Filter"
cv2.namedWindow(win_name)


class ImageFilter:
    def __init__(self, image, win_name) -> None:
        self.image = image
        self.image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        self.win_name = win_name

        self.hue_min, self.sat_min, self.val_min = 0, 0, 0
        self.hue_max, self.sat_max, self.val_max = 180, 255, 255

    def show_filtered_image(self):
        img_mask = cv2.inRange(
            self.image_hsv,
            lowerb=(self.hue_min, self.sat_min, self.val_min),
            upperb=(self.hue_max, self.sat_max, self.val_max),
        )

        img_filtered = cv2.bitwise_and(self.image, self.image, mask=img_mask)

        cv2.imshow(self.win_name, img_filtered)

    def on_hue_min_change(self, value):
        self.hue_min = value
        self.show_filtered_image()
    
    def on_hue_max_change(self, value):
        self.hue_max = value
        self.show_filtered_image()
    
    def on_sat_min_change(self, value):
        self.sat_min = value
        self.show_filtered_image()
    
    def on_sat_max_change(self, value):
        self.sat_max = value
        self.show_filtered_image()
    
    def on_val_min_change(self, value):
        self.val_min = value
        self.show_filtered_image()
    
    def on_val_max_change(self, value):
        self.val_max = value
        self.show_filtered_image()


img_filter = ImageFilter(img, win_name)

cv2.createTrackbar("Hue Min", win_name, img_filter.hue_min, 180, img_filter.on_hue_min_change)
cv2.createTrackbar("Hue Max", win_name, img_filter.hue_max, 180, img_filter.on_hue_max_change)

cv2.createTrackbar("Sat Min", win_name, img_filter.sat_min, 255, img_filter.on_sat_min_change)
cv2.createTrackbar("Sat Max", win_name, img_filter.sat_max, 255, img_filter.on_sat_max_change)

cv2.createTrackbar("Val Min", win_name, img_filter.val_min, 255, img_filter.on_val_min_change)
cv2.createTrackbar("Val Max", win_name, img_filter.val_max, 255, img_filter.on_val_max_change)


while True:
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cv2.destroyAllWindows()
