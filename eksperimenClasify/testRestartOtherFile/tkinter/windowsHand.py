import os
# from keras.preprocessing import image
# from keras.models import load_model
import cv2
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import Frame
from PIL import Image, ImageTk
import sys
import time
import random
import datetime
from tkinter import messagebox
window = tk.Tk()

os.system("clear")

# model = load_model("/home/pandu/Documents/eksperimen/model/16jun21.h5")
video = "/home/pandu/Documents/eksperimen/video/s_cuci_tangan11.mp4"

cap = cv2.VideoCapture(0)


def closeProgram():
    messagebox.showinfo("Informasi", "Aplikasi di tutup")
    sys.exit()


lab = Label(window)
lab.pack()


def clock():
    time = datetime.datetime.now().strftime("Waktu: %H:%M:%S")
    lab.config(text=time)
    window.after(1000, clock)  # run itself again after 1000 ms

clock()

#Graphics window
window.title('Evaluasi Cuci Tangan')
window.geometry("800x800")
# window.overrideredirect(1)

mainFrame = Frame(window)
mainFrame.place(x=20, y=20)

#Capture video frames
window = tk.Label(mainFrame)
window.grid(row=0, column=0)
closeButton = Button(window, text="CLOSE", font=(
    "Helvetica", 12), bg="#ffffff", command=closeProgram, width=20, height=1)
closeButton.place(x=220, y=430)


def textna():
    x = random.randint(0,5)
    x = 1
    print("wait")
    # time.sleep(1)
    for item in range(5):
        print(x)
        if x == item:
            color = "green"
        else:
            color = "black"
        text = ("Gerakan {}".format(item))
        lb0 = Label(window, text=text, fg=color, font=("Helvetica", 12))
        yPost = 20 + item*25
        lb0.place(x=20, y=yPost) 

    window.after(1000, textna)

textna()

    # time = datetime.datetime.now().strftime("Waktu: %H:%M:%S")
    # lab.config(text=time)
    # window.after(1000, clock)



def show_frame():
	ret, frame = cap.read()
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

	img = Image.fromarray(frame).resize((760, 400))
	imgtk = ImageTk.PhotoImage(image=img)
	window.imgtk = imgtk
	window.configure(image=imgtk)
	window.after(10, show_frame)
    

show_frame()  # Display
window.mainloop()  # Starts GUI
