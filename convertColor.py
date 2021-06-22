import numpy as np
import cv2
import os
from skimage.morphology import skeletonize
import matplotlib.pyplot as plt
from skimage import morphology, filters

os.system("clear")

# Path folder for write image
pathImage = "/home/pandu/Documents/eksperimen/image/imageframe"

#Path url Folder Video
path = "/home/pandu/Documents/eksperimen/video/"
videoFile = os.listdir(path)

# Name Video
videoFile[0] = "s_cuci_tangan15.mp4"
cap = cv2.VideoCapture(path+videoFile[0])

# Check Total Frame
totalFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(totalFrames)

frameIdx = 0
ratio = 0.3


def getCentroidOfMass(img):
    M = img.shape[0]
    N = img.shape[1]
    iC = 0
    jC = 0
    Nimg = 0
    for i in range(M):
        for j in range(N):
            if (img[i, j] == 255):
                Nimg = Nimg + 1
                iC = iC + i
                jC = jC + j

    if Nimg > 0:
        iC = int(iC/Nimg)
        jC = int(jC/Nimg)
    if Nimg == 0:
        iC = M//2
        jC = N//2

    return iC, jC


def createHbwithCent(img, iC, jC):
    M = img.shape[0]
    N = img.shape[1]
    HbC = np.zeros((M, N, 3), dtype=int)

    for i in range(M):
        for j in range(N):
            for k in range(3):
                HbC[i, j, k] = img[i, j]

    for i in range(-3, 4, 1):
        for j in range(-3, 4, 1):
            HbC[iC+i, jC+j, 0] = 0
            HbC[iC+i, jC+j, 1] = 0
            HbC[iC+i, jC+j, 2] = 255

    return HbC


def allSkel(skel):
    M = skel.shape[0]
    N = skel.shape[1]
    finVal = False
    for i in range(M):
        for j in range(N):
            finVal = finVal or skel[i, j]

    return finVal


while(True) and (frameIdx < (totalFrames-1)):
    ret, frame = cap.read()
    # frame = cv2.rotate(frame, cv2.ROTATE_180)
    # frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    pct = (frameIdx/totalFrames)*100

    M = frame.shape[0]
    N = frame.shape[1]

    # frame = cv2.resize(frame, (int(ratio*N),int(ratio*M)))
    frame = cv2.resize(frame, (200, 200))
    frameOri = cv2.resize(frame, (200, 200))

    # cv2.imshow("ori", frame)

    mm = frame.shape[0]
    nn = frame.shape[1]

    mm2 = mm // 2
    nn2 = nn // 2

    delta = min(mm2, nn2)
    delta = int(0.5*delta)
    frame = frame[mm2-delta:mm2+delta, nn2-delta:nn2+delta, :]

    # Has Resized
    labImg = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    hsvImg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # No resized
    labImgOri = cv2.cvtColor(frameOri, cv2.COLOR_BGR2LAB)
    hsvImgOri = cv2.cvtColor(frameOri, cv2.COLOR_BGR2HSV)

    [Blue, G, R] = cv2.split(frame)
    [L, A, B] = cv2.split(labImg)
    [H, S, V] = cv2.split(hsvImg)

    b, g, r = cv2.split(frameOri)
    l, a, b = cv2.split(labImgOri)
    h, s, v = cv2.split(hsvImgOri)
    cv2.imshow("try", s)

    frameIdx = frameIdx + 1
    oriMerge = np.hstack((frame, frame, frame))
    rgbMerge = np.hstack((R, G, Blue))
    labMerge = np.hstack((L, A, B))
    hsvMerge = np.hstack((H, S, V))

    finMerge = np.vstack((rgbMerge, labMerge, hsvMerge))

    cv2.imshow("all", finMerge)

    H = cv2.blur(H, (5, 5))


    Hb = cv2.inRange(H, 0, 15)
    m3 = Hb.shape[0]
    n3 = Hb.shape[1]
    rgbMs = np.zeros([m3, n3, 3], dtype="uint8")

    for ii in range(m3):
        for jj in range(n3):
            if (Hb[ii, jj] == 255):
                rgbMs[ii, jj, :] = frame[ii, jj, :]

    [iC0, jC0] = getCentroidOfMass(Hb)
    HbC = createHbwithCent(Hb, iC0, jC0)

    kernel = np.ones((2, 2), np.uint8)
    HbErd = cv2.erode(Hb, kernel)

    # # Covert To binary
    # cv2.imshow("RGB", frame)
    # cv2.imshow("Binary HUE", Hb)
    # cv2.imshow("Hb eroded", HbErd)

    # # Only to Grayscale Merge
    # cv2.imshow("RGB", rgbMerge)
    # cv2.imshow("LAB", labMerge)
    # cv2.imshow("HSV", hsvMerge)

    # cv2.imshow("All", finMerge)

    # # Select Channel Where look clear
    cv2.imshow("Only Red Channel Color", r)
    # cv2.imshow("Only A Channel Color", a)

    # Convert to Treshold with spesific channel color
    retR, tholdR = cv2.threshold(r, 50, 255, cv2.THRESH_BINARY)
    frameR = np.array(tholdR)
    cv2.imshow('Treshold Channel R color', frameR)

    if (frameIdx != 0):
        NameFile = str(10000 + frameIdx)
        NameFile = NameFile[1:]+".jpg"
        print(NameFile)

        # # Write File
        cv2.imwrite(pathImage+"/rgb/"+NameFile, frameR)
        # cv2.imwrite(pathImage+"/LAB/"+NameFile, a)
        # cv2.imwrite(pathImage+"/HSV/"+NameFile,hsvMerge)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
