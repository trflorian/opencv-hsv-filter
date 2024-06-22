import cv2


def get_channel_limit(channel_name):
    return 180 if channel_name == "Hue" else 255


class ImageFilter:
    def __init__(
        self,
        img_path,
        win_name="Image Filter",
        channels=["Hue", "Saturation", "Value"],
    ):
        self.img = cv2.imread(img_path)
        self.img_hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)

        self.win_name = win_name

        self.channels = channels
        self.channel_max_values = {c: get_channel_limit(c) for c in channels}
        self.init_filter_values()

        cv2.namedWindow(self.win_name)
        self.create_trackbars()

        self.show_filtered_image()

    def init_filter_values(self):
        """
        Initialize the filter values for each channel
        """
        self.filter_values = dict()
        for channel_name, channel_max_value in self.channel_max_values.items():
            self.filter_values[f"{channel_name} Min"] = 0
            self.filter_values[f"{channel_name} Max"] = channel_max_value

    def create_trackbars(self):
        """
        Create trackbars for each channel and its min and max values
        """
        for channel_name, channel_max_value in self.channel_max_values.items():
            trackbar_name_min = f"{channel_name} Min"
            trackbar_name_max = f"{channel_name} Max"

            cv2.createTrackbar(
                trackbar_name_min,
                self.win_name,
                0,
                channel_max_value,
                lambda value, name=trackbar_name_min: self.on_filter_value_changed(
                    name, value
                ),
            )
            cv2.createTrackbar(
                trackbar_name_max,
                self.win_name,
                channel_max_value,
                channel_max_value,
                lambda value, name=trackbar_name_max: self.on_filter_value_changed(
                    name, value
                ),
            )

    def on_filter_value_changed(self, trackbar_name, new_value):
        self.filter_values[trackbar_name] = new_value
        self.show_filtered_image()

    def show_filtered_image(self):
        lowerb = [
            self.filter_values[f"{channel} Min"] for channel in self.channels
        ]
        upperb = [
            self.filter_values[f"{channel} Max"] for channel in self.channels
        ]

        img_mask = cv2.inRange(self.img_hsv, tuple(lowerb), tuple(upperb))
        img_filtered = cv2.bitwise_and(self.img, self.img, mask=img_mask)

        cv2.imshow(self.win_name, img_filtered)

    def run(self):
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    img_filter = ImageFilter("flower.png")
    img_filter.run()
