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
window.title('EvaluasiCuci Tangan')
window.geometry("600x480")
# window.overrideredirect(1)

mainFrame = Frame(window)
mainFrame.place(x=20, y=20)

#Capture video frames
lmain = tk.Label(mainFrame)
lmain.grid(row=0, column=0)
closeButton = Button(window, text="CLOSE", font=("Helvetica", 12), bg="#ffffff", command=closeProgram, width=20, height=1)
closeButton.place(x=220, y=430)

x = random.randint(0, 10)
text = ("Gerakan {}".format(x))
lb0 = Label(window, text=text, fg="black", font=("Helvetica", 12))
lb0.place(x=20, y=20)



def show_frame():
	ret, frame = cap.read()
	cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
	img = Image.fromarray(cv2image).resize((760, 400))
	imgtk = ImageTk.PhotoImage(image=img)
	lmain.imgtk = imgtk
	lmain.configure(image=imgtk)
	lmain.after(10, show_frame)


	


show_frame()  # Display
window.mainloop()  # Starts GUI
