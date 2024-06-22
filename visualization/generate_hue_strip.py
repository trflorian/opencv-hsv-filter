# generate a hue color strip with annotations using matplotlib

import matplotlib.pyplot as plt
import numpy as np
import cv2

hue_values = np.arange(0, 181, 1)

# create a 180x100 hsv image in one line with the hue values
hue_strip_hsv = np.array([[[hue, 255, 255] for hue in hue_values]], dtype=np.uint8)

# repeat the image 100 times in the y direction
hue_strip_hsv = np.repeat(hue_strip_hsv, 20, axis=0)

# convert the hsv image to rgb
hue_strip_rgb = cv2.cvtColor(hue_strip_hsv, cv2.COLOR_HSV2RGB)

# display the image
plt.imshow(hue_strip_rgb)
plt.title("Hue")
plt.xticks(np.arange(0, 181, 45), labels=[f"{hue}°" for hue in np.arange(0, 181, 45)])
plt.yticks([])
plt.xlim(0, 180)

plt.tight_layout()
plt.savefig("hue_strip.png", dpi=300, bbox_inches="tight")

plt.show()
