import requests
import cv2
import numpy as np

url = "http://192.168.1.2:4747/video?640x480"

cap = cv2.VideoCapture(1)


# response = requests.get(url)
# print(response.status_code)

while True:

    ret, frame = cap.read()

    cv2.imshow("a", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
