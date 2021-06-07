import numpy as np
import cv2
import os


os.system("clear")

def combineTwoImages(targetImg, addImg):
    tM = targetImg.shape[0]
    tN = targetImg.shape[1]
    aM = addImg.shape[0]
    aN = addImg.shape[1]

    finalImg = []
    finalImg.append(targetImg)
    finalImg.append(addImg)

    #print("tM: %d tN: %d "%(tM,tN))
    #print("aM: %d aN: %d "%(aM,aN))
    return finalImg




# cap = cv2.VideoCapture("/home/pandu/Documents/skripsi/dataset/video/s_cuci_tangan11.mp4")
cap = cv2.VideoCapture(0)

ret, frame = cap.read()
M = frame.shape[1]
N = frame.shape[0]

scaleRatio = 0.5
rM = int(scaleRatio*M)
rN = int(scaleRatio*N)


while(True):    # Capture frame-by-frame
    ret, frame = cap.read()

    frame = cv2.resize(frame,(rM,rN),interpolation = cv2.INTER_AREA)
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret,th1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    ret,th2 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
    edges = cv2.Canny(th1,90,100,5)



    # Display the resulting frame
    #cv2.imshow('RGB',frame)
    #cv2.imshow('frame-Binary',th1)
    #cv2.imshow('frame2-Inv Binary',th2)
    #cv2.imshow('frame3- Edges',edges)

    finalImg  = cv2.vconcat([th1, th2])
    finalImg2 = cv2.vconcat([th1, edges])

    #finalImg = combineTwoImages(th1, th2)
    cv2.imshow('Final Image',finalImg)
    cv2.imshow('Final Image 2',finalImg2)
    cv2.imshow('Final Image 3',cv2.vconcat([frame, frame]))


    k = cv2.waitKey(1) & 0xFF
    # press 'q' to exit
    if k == ord('q'):
        break


    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()