from tkinter import *
import tkinter as tk

root = Tk()
root.title("Test Chrono")

counter = 9


def counter_label(label):
    button1 = Button(root, text="Recommencer", command=counter_label).grid()
    button2 = Button(root, text="Commencer", command=counter_label).grid()

    def count():
        global counter

        counter -= 1
        print(counter)
        label.config(text=str(counter), font="Arial 20")
        label.after(1000, count)

        if counter < 0:
            label.config(text="Fini")

    count()


label = tk.Label(root, fg="green")
label.grid(row=5, column=0)
counter_label(label)

mainloop()
