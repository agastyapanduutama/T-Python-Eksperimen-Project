# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 16:44:27 2017
@author: sakurai
"""


import numpy as np
import cv2
import screeninfo

if __name__ == '__main__':
    screen_id = 0
    is_color = True

    # get the size of the screen
    screen = screeninfo.get_monitors()[0]


    
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    window_name = 'projector'
    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.moveWindow(window_name, screen.x - 1, screen.y - 1)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN,
                          cv2.WINDOW_FULLSCREEN)
    cv2.imshow(window_name, frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    
