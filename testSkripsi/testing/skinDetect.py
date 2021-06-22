# Required modules
import cv2
import numpy as np
import matplotlib.pyplot as plt

min_YCrCb = np.array([0, 133, 77], np.uint8)
max_YCrCb = np.array([235, 173, 127], np.uint8)

# Get pointer to video frames from primary device
image = cv2.imread("/home/pandu/Documents/eksperimen/testSkripsi/testing/image/im.png")
imageYCrCb = cv2.cvtColor(image, cv2.COLOR_BGR2YCR_CB)
skinRegionYCrCb = cv2.inRange(imageYCrCb, min_YCrCb, max_YCrCb)
skinYCrCb = cv2.bitwise_and(image, image, mask=skinRegionYCrCb)

cv2.imshow("image", image)
cv2.imshow("imageYCrCb", imageYCrCb)
cv2.imshow("skinRegionYCrCb", skinRegionYCrCb)
# cv2.imwrite("/home/pandu/Documents/eksperimen/testSkripsi/testing/image/im2.png",
            # np.hstack([image, skinYCrCb]))

# invertColor = cv2.bitwise_and(image, image, mask=skinRegionYCrCb)

imagem = (255-skinRegionYCrCb)
cv2.imshow("invertColor", imagem)


cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image
