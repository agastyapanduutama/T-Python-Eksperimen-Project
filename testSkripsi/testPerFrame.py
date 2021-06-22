import os
import cv2
import time

videoFile = "/home/pandu/Documents/eksperimen/video/s_cuci_tangan11.mp4"
cap = cv2.VideoCapture(videoFile)

frameIdx = 0
totalFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

pTime = 0
print(totalFrames)



while True:
    ret, frame = cap.read()

    frameIdxDisp = frameIdx + 10000
    frameIdxDispStr = str(frameIdxDisp)[1:]

    infoStr = "Frame No: "+frameIdxDispStr
    print(infoStr)

    frameIdx += 1

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(frame, f'FPS: {int(fps)}', (20, 70),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("RGB Video", frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
