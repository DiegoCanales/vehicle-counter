import sys
import os.path
import cv2

def main():

    if(len(sys.argv) < 2 or not os.path.isfile(sys.argv[1])):
        print('arguments missing.\nrun: main.py [video_path]')
        exit(0)
    
    video = sys.argv[1]

    windowsName = 'highway'
    cv2.namedWindow(windowsName)

    cap = cv2.VideoCapture(video)
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