import cv2


def get_channel_max(channel_name):
    return 180 if channel_name == "Hue" else 255


class ImageFilter:
    def __init__(
        self,
        img_path: str,
        win_name="Image Filter",
        channels=["Hue", "Saturation", "Value"],
    ):
        self.img = cv2.imread(img_path)
        self.img_hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)

        self.win_name = win_name

        # initialize the channels and their max values
        self.channels = channels
        self.channel_max_values = {c: get_channel_max(c) for c in channels}
        self.init_filter_values()

        # setup the gui
        cv2.namedWindow(self.win_name)
        self.create_trackbars()

    def init_filter_values(self) -> None:
        """
        Initialize the filter values for each channel
        """
        self.filter_values = dict()
        for channel_name, channel_max_value in self.channel_max_values.items():
            self.filter_values[f"{channel_name} Min"] = 0
            self.filter_values[f"{channel_name} Max"] = channel_max_value

    def create_trackbars(self) -> None:
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
                lambda value, name=trackbar_name_min: self.on_trackbar_value_changed(
                    name, value
                ),
            )
            cv2.createTrackbar(
                trackbar_name_max,
                self.win_name,
                channel_max_value,
                channel_max_value,
                lambda value, name=trackbar_name_max: self.on_trackbar_value_changed(
                    name, value
                ),
            )

    def validate_trackbar_value(self, trackbar_name: str, new_value: int) -> int:
        """
        Validate the new value of the trackbar to be within the min and max values.
        Adjust the trackbar value if it is out of bounds.

        Args:
            trackbar_name (str): the name of the trackbar
            new_value (int): the new value of the trackbar

        Returns:
            int: the validated value of the trackbar
        """
        is_lower_bound = "Min" in trackbar_name

        if is_lower_bound:
            opposite_bound_name = trackbar_name.replace("Min", "Max")
        else:
            opposite_bound_name = trackbar_name.replace("Max", "Min")

        opposite_bound_value = self.filter_values[opposite_bound_name]

        if is_lower_bound and opposite_bound_value < new_value:
            opposite_bound_value = new_value

        if not is_lower_bound and opposite_bound_value > new_value:
            opposite_bound_value = new_value

        # update the trackbar value
        cv2.setTrackbarPos(trackbar_name, self.win_name, new_value)
        cv2.setTrackbarPos(opposite_bound_name, self.win_name, opposite_bound_value)

        return new_value

    def on_trackbar_value_changed(self, trackbar_name: str, new_value: int) -> None:
        """
        Callback function when a trackbar value is changed
        """
        new_value = self.validate_trackbar_value(trackbar_name, new_value)
        self.filter_values[trackbar_name] = new_value

        self.show_filtered_image()

    def show_filtered_image(self) -> None:
        """
        Show the filtered image based on the trackbar values
        """
        lowerb = [self.filter_values[f"{channel} Min"] for channel in self.channels]
        upperb = [self.filter_values[f"{channel} Max"] for channel in self.channels]

        img_mask = cv2.inRange(self.img_hsv, tuple(lowerb), tuple(upperb))
        img_filtered = cv2.bitwise_and(self.img, self.img, mask=img_mask)

        cv2.imshow(self.win_name, img_filtered)

    def run(self) -> None:
        """
        Run the image filter application
        """
        self.show_filtered_image()
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    img_filter = ImageFilter(img_path="images/flower.png")
    img_filter.run()
