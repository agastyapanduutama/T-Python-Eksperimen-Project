from keras.preprocessing import image
from keras.models import load_model
import numpy as np
import time
import cv2
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


model = load_model("/home/pandu/Documents/eksperimen/model/31mei21.h5")


## Video Part
videoPath = "/home/pandu/Documents/eksperimen/video/"
videoFile = "s_cuci_tangan11.mp4"


cap = cv2.VideoCapture(videoPath+videoFile)
cap = cv2.VideoCapture(0)


totalFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(totalFrames)

frameIdx = 0
ratio = 0.5
pTime = 0


ret, frame0 = cap.read()

M = frame0.shape[0]
N = frame0.shape[1]

M = int(ratio*M)
N = int(ratio*N)

poseCount = np.zeros(7, dtype=int)

while True:
# while(True) and (frameIdx < (totalFrames-1)):
    ret, frame0 = cap.read()
    pct = (frameIdx/totalFrames)*100
    frame0 = frame0

    M = frame0.shape[0]
    N = frame0.shape[1]

    mR = 180
    nR = 180

    frame = cv2.resize(frame0, (int(ratio*N), int(ratio*M)))

    inFrame = cv2.resize(frame0, (nR, mR))

    b, g, r = cv2.split(inFrame)

    cv2.imshow("Only Red Channel Color", r)

    retR, tholdR = cv2.threshold(r, 50, 255, cv2.THRESH_BINARY)
    frameR = np.array(tholdR)
    cv2.imshow('Treshold Channel R color', frameR)

    rgbFrame = cv2.merge([frameR, frameR, frameR])

    test_image = image.img_to_array(rgbFrame)
    test_image = np.expand_dims(test_image, axis=0)
    result = model.predict(test_image)

    poseIdx = np.argmax(result, axis=1)
    print("Gerakan terdeteksi gerakan :" + str(poseIdx))
    poseCount[poseIdx[0]] = poseCount[poseIdx[0]] + 1

    position = (10, 40)
    frameIdxDisp = frameIdx + 10000
    frameIdxDispStr = str(frameIdxDisp)[1:]

    print("Total Frame : " + str(frameIdxDispStr))

    # infoStr = "%2.2f" % (pct)
    # infoStr = "Frame No: "+frameIdxDispStr + \
    #     " ["+infoStr+"%] Pose index: "+str(poseIdx[0])
    # print(infoStr)

    # cv2.putText(frame, infoStr, position,
    #             cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0, 0), 2)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    print("FPS : " + str(fps))
    cv2.putText(frame, f'FPS: {int(fps)}', (20, 70),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("RGB Video", frame)

    frameIdx += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
