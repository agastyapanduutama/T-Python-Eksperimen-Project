import time
import cv2
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model
from keras.preprocessing import image


# from tkinter import *
# window = Tk()


# def summariseTheResult(poseCount, totalFrames):
#   window.title('Summary of Handwashing')
#   window.geometry("400x300+300+300")

#   secondPerFrame = 1/30
#   posePctAcc = 0

#   poseDurationAcc = 0
#   for idx in range(7):
#     poseDuration = poseCount[idx]*secondPerFrame
#     posePct = (poseCount[idx]/totalFrames)*100
#     idxStr = "{:2d}".format(idx)

#     if poseCount[idx] >= 10:
#       textColour = "black"
#     else:
#       textColour = "red"

#     text = ("Pose %s: %3.2f  sec    Pct: %3.2f %%") % (
#         idxStr, poseDuration, posePct)
#     lb0 = Label(window, text=text, fg=textColour, font=("Helvetica", 12))
#     yPost = 20 + idx*25
#     lb0.place(x=20, y=yPost)

#     poseDurationAcc = poseDurationAcc + poseDuration
#     posePctAcc = posePctAcc + posePct

#   posePctAcc = round(posePctAcc)
#   text = ("Total Pose Duration: %3.2f  sec    Pct: %3.2f %%") % (
#       poseDurationAcc, posePctAcc)
#   lb0 = Label(window, text=text, fg='black', font=("Helvetica", 12))
#   yPost = 35 + yPost
#   lb0.place(x=20, y=yPost)


# saveVideo = False

# rootPath = "C:\\Users\\INKOM06\\Pictures\\handwash\\mod1\\trdataset\\"

model = load_model("/home/pandu/Documents/eksperimen/model/31mei21.h5")
# model.summary()

## Video Part
videoPath = "/home/pandu/Documents/eksperimen/video/"
videoFile = "s_cuci_tangan02.mp4"

cap = cv2.VideoCapture(videoPath+videoFile)
# cap = cv2.VideoCapture(0)


totalFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(totalFrames)

frameIdx = 0
ratio = 0.5
pTime = 0

# ret, frame0 = cap.read()
# M = frame0.shape[0]
# N = frame0.shape[1]

# M = int(ratio*M)
# N = int(ratio*N)
# videoPathToSave = "/home/pandu/Documents/eksperimen/video"
# if saveVideo == True:
#   out = cv2.VideoWriter(videoPathToSave+"output.avi",
#                         cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 30, (N, M))


poseCount = np.zeros(7, dtype=int)

while True:
# while(True) and (frameIdx < (totalFrames-1)):
    ret, frameNA = cap.read()
    pct = (frameIdx/totalFrames)*100
    frame0 = frameNA
    frame = frameNA
    # cv2.imshow("kamera", frame0)

    # frame0 = cv2.rotate(frameNA, cv2.ROTATE_180)
    # cv2.imshow("kamera rotate 180", frame0)

    # frame0 = cv2.rotate(frameNA, cv2.ROTATE_90_CLOCKWISE)
    # cv2.imshow("kamera rotate 90", frame1)

    # frame0 = cv2.rotate(frameNA, cv2.ROTATE_90_COUNTERCLOCKWISE)
    # cv2.imshow("kamera rotate 270", frame2)

    # M = frame0.shape[0]
    # N = frame0.shape[1]

    mR = 180
    nR = 180

    # frame = cv2.resize(frame0, (int(ratio*N), int(ratio*M)))

    #out.write(frame)

    inFrame = cv2.resize(frame0, (nR, mR))

    b, g, r = cv2.split(inFrame)
    
    [H, S, V] = cv2.split(inFrame)
    retR, tholdR = cv2.threshold(r, 50, 255, cv2.THRESH_BINARY)
    frameR = np.array(tholdR)
    # cv2.imshow('Treshold Channel R color', frameR)

    # [B, G, R] = cv2.split(inFrame)
    # ret3, inFrameR = cv2.threshold(R, 50, 255, cv2.THRESH_BINARY)
    # cv2.namedWindow("Input frames", cv2.WINDOW_NORMAL)
    # cv2.imshow("Input frames", inFrameR)

    rgbFrame = cv2.merge([frameR, frameR, frameR])

    test_image = image.img_to_array(rgbFrame)
    test_image = np.expand_dims(test_image, axis=0)
    result = model.predict(test_image)

    poseIdx = np.argmax(result, axis=1)
    print(poseIdx)
    poseCount[poseIdx[0]] = poseCount[poseIdx[0]] + 1

    # position = (10, 40)
    # frameIdxDisp = frameIdx + 10000
    # frameIdxDispStr = str(frameIdxDisp)[1:]

    # infoStr = "%2.2f" % (pct)
    # infoStr = "Frame No: "+frameIdxDispStr + \
    #     " ["+infoStr+"%] Pose index: "+str(poseIdx[0])
    # print(infoStr)

    # cv2.putText(frame, infoStr, position,cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0, 0), 2)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    print(int(fps))

    # cv2.putText(frame, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN,3, (255, 0, 0), 3)
    # cv2.imshow("RGB Video", frame)

    # if saveVideo == True:
    #   out.write(frame)

    # frameIdx += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

# summariseTheResult(poseCount, totalFrames)


# window.title('Summary of Handwashing')
# window.geometry("400x300+300+300")


# secondPerFrame = 1/30
# posePctAcc = 0

# poseDurationAcc = 0
# for idx in range(7):
#   poseDuration = poseCount[idx]*secondPerFrame
#   posePct = (poseCount[idx]/totalFrames)*100
#   idxStr = "{:2d}".format(idx)


#   if poseCount[idx] >= 10:
#     textColour = "black"
#   else:
#     textColour = "red"

#   text = ("Pose %s: %3.2f  sec    Pct: %3.2f %%")%(idxStr,poseDuration,posePct)
#   lb0=Label(window, text=text, fg=textColour, font=("Helvetica", 12))
#   yPost = 20 + idx*25
#   lb0.place(x=20, y=yPost)

#   poseDurationAcc = poseDurationAcc + poseDuration
#   posePctAcc = posePctAcc + posePct


# posePctAcc = round(posePctAcc)
# text = ("Total Pose Duration: %3.2f  sec    Pct: %3.2f %%")%(poseDurationAcc,posePctAcc)
# lb0=Label(window, text=text, fg='black', font=("Helvetica", 12))
# yPost = 20 + idx*25
# lb0.place(x=20, y=yPost)


# textVal = str(frameIdx)

# lbl=Label(window, text=textVal, fg='red', font=("Helvetica", 16))
# lbl.place(x=60, y=50)

# window.mainloop()
# cv2.destroyAllWindows()
