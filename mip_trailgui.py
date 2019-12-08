import tkinter as tk
from tkinter import *
from tkinter import filedialog

import cv2
import numpy as np
from PIL import Image, ImageTk
from matplotlib import pyplot as plt

<<<<<<< HEAD

window = tk.Tk() # window is the main window which pops up when the program runs
#window.configure()
#window.title('MRI Intelligence Scanning using ICA and K-spaces')
#window.geometry("1250x750")

=======
window = tk.Tk() # window is the main window which pops up when the program runs
>>>>>>> 696dd3b1628979b82f710ac265c1de271bd91661

class gui:

    # Input Image

    """def showImg(self, window):

        load = Image.open('dog.jpg')
        render = ImageTk.PhotoImage(load)

        img = tk.Label(window, image=render)
        img.image = render
        img.grid(row=1, column=0)"""
    def page1(self, window):
        self.window = window
        window.title('MRI Intelligence Scanning using ICA and K-spaces')
        window.geometry("1250x750")


        # Browse Button
        browse_button = tk.Button(window, text="Browse", command=lambda: self.browsefunc(window))
        browse_button.grid(row=0, column=0, pady=10, sticky=tk.W)


<<<<<<< HEAD
         # Output Image
=======
        # Output Image
>>>>>>> 696dd3b1628979b82f710ac265c1de271bd91661


        #  Operation


        op_label = tk.Label(window, text="""Parameters: """, padx=10, pady=5)
        op_label.grid(row=0, column=3, sticky=tk.W)


        # Input Parameters

        # ---------------- LABELS ----------------
        # Label for Number of components
        InputLabel1 = tk.Label(window, text="Number of Components")
        InputLabel1.grid(row=1, column=3, sticky=tk.W)

        # Label for Number of Iterations
        InputLabel2 = tk.Label(window, text="MAx Iterations")
        InputLabel2.grid(row=2, column=3, sticky=tk.W)

        # Label for Tolerance
        InputLabel3 = tk.Label(window, text="Tolerance")
        InputLabel3.grid(row=3, column=3, sticky=tk.W)

        # ---------------- ENTRIES ----------------
        # Entry field for Number of components
        InputField1 = tk.Entry(window, textvariable="components")
        InputField1.grid(row=1, column=4, sticky=tk.E + tk.W)

        # Entry field for Number of Iterationss
        InputField2 = tk.Entry(window, textvariable="iterations")
        InputField2.grid(row=2, column=4, sticky=tk.E + tk.W)

        # Entry field for Tolerance
        InputField3 = tk.Entry(window, textvariable="tolerance")
        InputField3.grid(row=3, column=4, sticky=tk.E + tk.W)

        # Process Button
        process_button = tk.Button(window, text="Apply")
        process_button.grid(row=4, column=4)


    def browsefunc(self, window):
        filename = filedialog.askopenfile()

        print(filename)
        print(filename.name)

        self.image = Image.open(filename.name)
        self.image.thumbnail((256, 256))
        
        self.photo = ImageTk.PhotoImage(self.image)
        self.labelPhoto = Label(window, image=self.photo)
        self.labelPhoto.grid(row=5, column=0)

        self.labelPhoto = Label(window, image=self.photo)
        self.labelPhoto.grid(row=5, column=1)

        self.labelPhoto = Label(window, image=self.photo)
        self.labelPhoto.grid(row=6, column=0)

        self.labelPhoto = Label(window, image=self.photo)
        self.labelPhoto.grid(row=6, column=1)

g = gui()
g.page1(window)
window.mainloop()
<<<<<<< HEAD
#browsebutton = Button(window1, text="Browse", command=lambda: self.browsefunc(window1))
#browsebutton.place(relx=.2, rely=.8, anchor="c")

# Displaying an image
#photo = PhotoImage(file='lana.png')
#labelPhoto = Label(window, image=photo)
#labelPhoto.grid(row=2, column=0)


# Creates the entire window and runs it
#main = gui(window)
#window.mainloop()


# Syntax
# .Label(text="", fonts=(font,size))
# .Button(arg1,arg2,...)
# .Entry(arg1,arg2,...)
# .Text(arg1,arg2,...)
=======
>>>>>>> 696dd3b1628979b82f710ac265c1de271bd91661
