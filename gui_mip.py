import tkinter as tk
from tkinter import *
import cv2
import numpy as np
from PIL import Image, ImageTk


window = tk.Tk() # window is the main window which pops up when the program runs
window.configure()
window.title('MRI Intelligence Scanning using ICA and K-spaces')
window.geometry("750x500")


#class gui:

# Input Image

"""def showImg(self, window):
        load = Image.open('dog.jpg')
        render = ImageTk.PhotoImage(load)
        img = tk.Label(window, image=render)
        img.image = render
        img.grid(row=1, column=0)"""

# Browse Button
browse_button = tk.Button(window, text="Browse")
browse_button.grid(row=0, column=0, pady=10, sticky=tk.W)

# Displaying an image
photo = ImageTk.PhotoImage(file='P10-0001.jpg')
labelPhoto = Label(window, image=photo)
labelPhoto.grid(row=2, column=0)




# Output Image


#  Operation
# v = tk.IntVar()

# op_label = tk.Label(window, text="""Choose an Operation: """, padx=10, pady=5)
# op_label.grid(stick=tk.W)

# op_mri_button = tk.Radiobutton(window, text="mri", padx=20, variable=v, value=1)
# op_mri_button.grid(sticky=tk.W, padx=30)

# op_k_button = tk.Radiobutton(window, text="k-space", padx=20, variable=v, value=2)
# op_k_button.grid(sticky=tk.W, padx=30)


# Input Parameters

# ---------------- LABELS ----------------
# Label for Number of components
InputLabel1 = tk.Label(window, text="Number of Components")
InputLabel1.grid(row=6, column=0, sticky=tk.W)

# Label for Number of Iterations
InputLabel2 = tk.Label(window, text="Max Iterations")
InputLabel2.grid(row=7, column=0, sticky=tk.W)

# Label for Tolerance
InputLabel3 = tk.Label(window, text="Tolerance")
InputLabel3.grid(row=8, column=0, sticky=tk.W)

# ---------------- ENTRIES ----------------
# Entry field for Number of components
InputField1 = tk.Entry(window, textvariable="components")
InputField1.grid(row=6, column=1, sticky=tk.E + tk.W)

# Entry field for Number of Iterationss
InputField2 = tk.Entry(window, textvariable="iterations")
InputField2.grid(row=7, column=1, sticky=tk.E + tk.W)

# Entry field for Tolerance
InputField3 = tk.Entry(window, textvariable="tolerance")
InputField3.grid(row=8, column=1, sticky=tk.E + tk.W)

# Process Button
process_button = tk.Button(window, text="Apply")
process_button.grid(row=9, column=0)

# Exit Button

quit_button = tk.Button(window, text="EXIT", fg="red",command = window.destroy)
quit_button.grid(row=10, column=0, sticky=tk.E + tk.W)

# Creates the entire window and runs it
#main = gui(window)
window.mainloop()


# Syntax
# .Label(text="", fonts=(font,size))
# .Button(arg1,arg2,...)
# .Entry(arg1,arg2,...)
# .Text(arg1,arg2,...)
