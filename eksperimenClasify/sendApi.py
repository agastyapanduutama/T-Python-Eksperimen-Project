import urllib.request
import cv2
import requests
import base64

video = "/home/pandu/Documents/eksperimen/video/s_cuci_tangan11.mp4"

cap = cv2.VideoCapture(video)

while True:
    ret, frame = cap.read()

    

    # url = 'http://localhost/skripsi/api.php'
    # myobj = {'frame': frame}

    # x = requests.post(url, data=myobj)
    # print(x.text)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
