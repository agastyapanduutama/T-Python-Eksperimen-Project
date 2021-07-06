from tkinter import *

window = Tk()

window.title('Hasil Evaluasi Cuci Tangan')
window.geometry("600x300+300+300")

header1 = Label(window, text="Urutan Gerakan")
header2 = Label(window, text="Gerakan Cuci Tangan")
label1 = Label(window, text="Gerakan 1")
label2 = Label(window, text="Gerakan 2")
label3 = Label(window, text="Gerakan 3")
label4 = Label(window, text="Gerakan 4")
label5 = Label(window, text="Gerakan 5")
label6 = Label(window, text="Gerakan 6")

header1.grid(row=0, column=0)
header2.grid(row=0, column=1)
label1.grid(row=2, column=0)
label2.grid(row=3, column=0)
label3.grid(row=4, column=0)
label4.grid(row=5, column=0)
label5.grid(row=6, column=0)
label6.grid(row=7, column=0)


window.mainloop()
