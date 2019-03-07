import cv2
import matplotlib.pyplot as plt

def main():
    path = "/home/raj/Documents/AI/OpenCV/standard_test_images/"

    img1_path = str(path) + "cameraman.tif"
    img2_path = str(path) + "house.tif"

    img1 = cv2.imread(img1_path, 1)
    img2 = cv2.imread(img2_path, 1)

    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

    add = img1 + img2
    sub1 = img1 - img2
    sub2 = img2 - img1
    mul = img1 * img2
    div = img1 / img2

# we can also use scalar values as operands in the above operations such as add = img1 + 50

    titles = ['Lena', 'Women blonde', 'addition', 'img1 - img2', 'img2 - img1', 'multiplication', 'division']
    images = [img1, img2, add, sub1, sub2, mul, div]

    for i in range(len(images)):
        plt.subplot(1, 7, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()

if __name__=="__main__":
    main()
