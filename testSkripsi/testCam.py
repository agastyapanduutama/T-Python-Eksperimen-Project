# Required modules
import cv2
import numpy as np
import matplotlib.pyplot as plt
import time


min_YCrCb = np.array([0, 133, 77], np.uint8)
max_YCrCb = np.array([235, 173, 127], np.uint8)


# url = "http://192.168.1.3:4747/video?640x480"
url = "/home/pandu/Documents/eksperimen/video/s_cuci_tangan12.mp4"
cap = cv2.VideoCapture(url)

# cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    time.sleep(00.03)

    frame = cv2.resize(frame, (200, 200))

    cv2.imshow("RGB Video", frame)

    b, g, r = cv2.split(frame)
    h, s, l = cv2.split(frame)

    # cv2.imshow("Only Red Channel Color", r)


    retR, tholdR = cv2.threshold(r, 50, 255, cv2.THRESH_BINARY)
    frameR = np.array(tholdR)
    # cv2.imshow('Treshold Channel R color', frameR)

    labImg = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    hsvImg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    [Blue, G, R] = cv2.split(frame)
    [L, A, B] = cv2.split(labImg)
    [H, S, V] = cv2.split(hsvImg)

    rgbMerge = np.hstack((R, G, Blue))
    labMerge = np.hstack((L, A, B))
    hsvMerge = np.hstack((H, S, V))

    finMerge = np.vstack((rgbMerge, labMerge, hsvMerge))

    cv2.imshow("all", finMerge)

    all, all1 = cv2.threshold(finMerge, 50, 255, cv2.THRESH_BINARY)
    frame1 = np.array(all1)
    cv2.imshow('All Treshold', frame1)

    
    imageYCrCb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)
    frameRa = np.array(tholdR)

    convertColor = (255-frame1)
    cv2.imshow("Treshold Invert", convertColor)

    imageYCrCb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)
    skinRegionYCrCb = cv2.inRange(imageYCrCb, min_YCrCb, max_YCrCb)
    skinYCrCb = cv2.bitwise_and(frame, frame, mask=skinRegionYCrCb)
    
    retSkin, treshSkin = cv2.threshold(skinYCrCb, 50, 255, cv2.THRESH_BINARY)
    frameSkinTresh = np.array(treshSkin)
    cv2.imshow('SKin Treshold', frameSkinTresh)

    cv2.imshow("skin Color", skinYCrCb)
    # cv2.imshow('Treshold Channel R color', frameRa)


    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
