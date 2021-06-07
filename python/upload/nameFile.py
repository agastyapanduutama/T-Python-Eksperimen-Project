import os
import time
from skimage import io

timestamp = int(time.time())
nameFile = str(timestamp) + "detection.jpg"
save_path = '/var/www/html/objekdeteksi/objekDeteksi/objek/' + nameFile
io.imsave(
    save_path,
    plotted_img
)

print(save_path)
