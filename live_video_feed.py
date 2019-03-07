import cv2

def main():
    windowname = "Live Feed"
    cv2.namedWindow(windowname)

    cap = cv2.VideoCapture(0)

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
    
    while ret:
        ret, frame = cap.read()

        output1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        output2 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow(windowname, frame)
        cv2.imshow("gray", output1)
        cv2.imshow("RGB", output2)

        if cv2.waitKey(1) == 27:
            break
    
    cv2.destroyAllWindows()
    cap.release()
    

if __name__=="__main__":
    main()
    
