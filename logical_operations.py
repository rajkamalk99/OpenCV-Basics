import cv2
import matplotlib.pyplot as plt

imgpath1 = "/home/raj/Documents/AI/OpenCV/standard_test_images/cameraman.tif"
imgpath2 = "/home/raj/Documents/AI/OpenCV/standard_test_images/house.tif"

img1 = cv2.imread(imgpath1)
img2 = cv2.imread(imgpath2)

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

img3 = cv2.bitwise_not(img1)
img4 = cv2.bitwise_and(img1, img2)
img5 = cv2.bitwise_or(img1, img2)
img6 = cv2.bitwise_xor(img1, img2)

titles = ["Image 1", "Image 2", "not", "and", "or", "xor"]
images = [img1, img2, img3, img4, img5, img6]

for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.title(titles[i])
    plt.imshow(images[i])
    plt.xticks([])
    plt.yticks([])


plt.show()