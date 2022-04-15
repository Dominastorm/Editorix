# Importing all the required modules
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps

img_file = "foxy.jpg"

img = np.array(Image.open(img_file))
plt.figure(figsize=(8,8))
plt.imshow(img)
plt.show()

