import cv2
import io
import socket
import struct
import time
import pickle
import zlib
import numpy as np

from tkinter import *
window = Tk()

def summariseTheResult(poseCount, totalFrames):
  window.title('Hasil Evaluasi Cuci Tangan')
  window.geometry("600x300+300+300")

  secondPerFrame = 1/30
  posePctAcc = 0
  poseDurationAcc = 0

  for idx in range(6):
    poseDuration = poseCount[idx]*secondPerFrame
    posePct = (poseCount[idx]/totalFrames)*100
    # print(posePct)

    idxStr = "{:2d}".format(idx)

    # if poseCount[idx] >= 10:
    if poseDuration >= 5:
      textColour = "black"
    else:
      textColour = "red"

    # print(idxStr)
    # if idxStr >= 6:
    #       print("he")

    text = ("Gerakan %s: Dilakukan selama : %3.2f detik | Persentasi : %3.2f %% \n") % (
        idxStr, poseDuration, posePct)
    lb0 = Label(window, text=text, fg=textColour, font=("Helvetica", 12))
    yPost = 20 + idx*25
    lb0.place(x=20, y=yPost)

    poseDurationAcc = poseDurationAcc + poseDuration
    posePctAcc = posePctAcc + posePct

  posePctAcc = round(posePctAcc)

  if poseDurationAcc >= 40:
      textColour = "black"
      # text = ("Durasi Cuci Tangan: %3.2f  sec | Persentasi : %3.2f %% \n dilakukan dengan benar") % (poseDurationAcc, posePctAcc)
      text = ("Durasi Cuci Tangan: %3.2f  sec |  \n dilakukan dengan benar") % (
          poseDurationAcc)
  elif poseDurationAcc < 40:
      textColour = "red"
      text = ("Durasi Cuci Tangan: %3.2f  sec |  \n dilakukan teralu Singkat Minimal 40 Detik \n dan setiap gerakan dilakukan minimal 8 Detik ") % (poseDurationAcc)

  lb0 = Label(window, text=text, fg=textColour, font=("Helvetica", 12))
  yPost = 35 + yPost
  lb0.place(x=20, y=yPost)


# Set Connection
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect(('35.219.90.227', 8080))
client_socket.connect(('192.168.1.17', 8080))
connection = client_socket.makefile('wb')

# Load Video
videoFile = "/home/pandu/Documents/eksperimen/video/s_cuci_tangan11.mp4"


cam = cv2.VideoCapture(1)
cam.set(3, 320)
cam.set(4, 240)

img_counter = 0


frameVideo = cam.get(cv2.CAP_PROP_FRAME_COUNT)
print(frameVideo)

frameIdx = 0

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

# while True:
while(True) and (frameIdx < (frameVideo-1)):
    ret, frame = cam.read()

    if ret:
        # Resize image
        mR = 96
        nR = 96
        inFrame = cv2.resize(frame, (nR, mR))

        # RGB Color Treshold
        b, g, r = cv2.split(inFrame)
        retR, tholdR = cv2.threshold(r, 50, 255, cv2.THRESH_BINARY)
        frameR = np.array(tholdR)
        cv2.imshow('Treshold Channel R color', frameR)
        frame = cv2.merge([frameR, frameR, frameR])

        result, frame = cv2.imencode('.jpg', frame, encode_param)
        # data = zlib.compress(pickle.dumps(frame, 0))
        data = pickle.dumps(frame, 0)
        size = len(data)

        print("{}: {}".format(img_counter, size))
        client_socket.sendall(struct.pack(">L", size) + data)
        img_counter += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
          break 
    

cam.release()
cv2.destroyAllWindows()
