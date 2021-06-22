import cv2
import os
import numpy as np

gambar = cv2.imread("/home/pandu/Documents/eksperimen/image/0.jpg")

labImg = cv2.cvtColor(gambar, cv2.COLOR_BGR2LAB)
hsvImg = cv2.cvtColor(gambar, cv2.COLOR_BGR2HSV)

[Blue, G, R] = cv2.split(gambar)
[L, A, B] = cv2.split(labImg)
[H, S, V] = cv2.split(hsvImg)

rgbMerge = np.hstack((R, G, Blue))
labMerge = np.hstack((L, A, B))
hsvMerge = np.hstack((H, S, V))

finMerge = np.vstack((rgbMerge, labMerge, hsvMerge))

cv2.imshow("all", finMerge)

retR, tholdR = cv2.threshold(finMerge, 50, 255, cv2.THRESH_BINARY)
frameR = np.array(tholdR)
cv2.imshow("image", frameR)

cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image
