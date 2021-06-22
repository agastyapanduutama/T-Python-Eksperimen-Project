import socket
import sys
import cv2
import pickle
import numpy as np
import struct  # new
import zlib
import os
import time

os.system("clear")

# Set Connection
HOST = '192.168.1.17'
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
s.bind((HOST, PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')


while s.listen(10) :
    print("hello")
    time.sleep(2)
    s.close()
