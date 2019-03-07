import cv2
import numpy as np
import matplotlib.pyplot as plt

imgpath = "/home/raj/Documents/AI/OpenCV/standard_test_images/lena_color_256.tif"
img = cv2.imread(imgpath, 0)

plt.imshow(img, cmap='gray')
plt.title("Gray scale image")
plt.xticks([])
plt.yticks([])
plt.show()


plt.imshow(img)
plt.title("Default scale image")
plt.xticks([])
plt.yticks([])
plt.show()
