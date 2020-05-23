import cv2

def main():
    windowsName = 'highway'
    cv2.namedWindow(windowsName)
    
    cap = cv2.VideoCapture('./highway.mp4')
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
    
    while ret:
        ret, frame = cap.read()
        cv2.imshow(windowsName,frame)

        if cv2.waitKey(1) == 27: # si la tecla ESC es presionada
            break
    
    cv2.destroyWindow(windowsName)
    cap.release()

if __name__ == "__main__":
    main()