import cv2
import numpy as np

windowname = "Drawing"
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow(windowname)

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_FLAG_CTRLKEY:
        cv2.circle(img, (x, y), 50, (0,255,0), -1)
cv2.setMouseCallback(windowname, draw_circle)


def main():
    while(True):
        cv2.imshow(windowname, img)
        if cv2.waitKey(20) == 27:
            break
    cv2.destroyAllWindows()
if __name__=="__main__":
    main()

