import tkinter as tk
import cv2

window = tk.Tk()
max_amount = 0
label1 = None  # just so it is defined

def fun():
    global max_amount, label1
    max_amount += 100
    label1.configure(text='Balance :$' + str(max_amount))

btn = tk.Button(window, text='Change', command=fun)
btn.grid()
t1 = str(max_amount)
label1 = tk.Label(window, text='Balance :$' + t1)
label1.grid()


cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     cv2.imshow("image", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()



window.mainloop()



