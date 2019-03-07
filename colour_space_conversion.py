import cv2
import matplotlib.pyplot as plt


imgpath = "/home/raj/Documents/AI/OpenCV/standard_test_images/lena_color_256.tif"

img = cv2.imread(imgpath)

img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.title("BGR image")
plt.show()

plt.imshow(img1)
plt.title("RGB image")
plt.show()