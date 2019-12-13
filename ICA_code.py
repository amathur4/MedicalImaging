from sklearn.decomposition import FastICA
from matplotlib import pyplot as plt
import numpy as np
import pylab as pl
import cv2 as cv

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

window = tk.Tk()  # window is the main window which pops up when the program runs

class gui:
    input_image_list = []
    original_images, kspace_images, ica_images, kspace_output = [], [], [], []
    #components = 0
    #iterations = 0
    #tolerance = 0

    # ICA algorithm
    # made the compute_ica_output function so that it can take multiple images as input and generate their corresponding outputs
    def compute_ica_output(self, image_list, no_of_components, max_iterations, tolerance):
        original_images = []
        kspace_images = []
        ica_images = []
        kspace_output = []
        for file in image_list:    # selects one image at a time from the input and performs ICA on it
            image_name = file
            input_image = cv.imread(image_name, 0)
            original_images.append(input_image)
            input_image = np.fft.fft2(input_image)        # performing FFT to obtain K-space of input
            input_image = np.fft.fftshift(input_image)
            img = np.uint8(np.log(np.abs(input_image) + 1) * 10)
            kspace_images.append(img)

            img = np.fft.ifftshift(input_image)
            img = np.fft.ifft2(img)                       # performing IFFT to get the input back and perform ICA on it
            img = np.uint8(np.log(np.abs(img) + 1) * 10)

            # perform ICA using 3 parameters: number of components, maximum iterations to converge and 
            # tolerance of error at each iteration
            ica = FastICA(n_components = no_of_components, max_iter = max_iterations, tol = tolerance)   
            ica.fit(img)
            image_ica = ica.fit_transform(img)
            image_restored = ica.inverse_transform(image_ica)

            imagefcs = np.zeros((image_restored.shape[0], image_restored.shape[1]), np.float)
            for i in range(image_restored.shape[0]):      # performing a full contrast stretch for cler visibility of the output
                for j in range(image_restored.shape[1]):
                    imagefcs[i, j] = np.log(np.abs(image_restored[i, j]) * 10)
            ica_images.append(imagefcs)

            imagefcs = np.fft.fft2(imagefcs)
            imagefcs = np.fft.fftshift(imagefcs)

            output_kspace = np.uint8(np.log(np.abs(imagefcs) + 1) * 10)
            kspace_output.append(output_kspace)

        return original_images, kspace_images, ica_images, kspace_output

    def page1(self, window):
        self.window = window
        window.title('MRI Intelligence Scanning using ICA and K-spaces')
        window.geometry("1250x750")

        # Browse Button
        browse_button = tk.Button(window, text = "Browse", command = lambda: self.browsefunc(window))
        browse_button.grid(row = 0, column = 0, pady = 10, sticky = tk.W)

        # Heading for the input parameters
        op_label = tk.Label(window, text="""Parameters: """, padx=10, pady=5)
        op_label.grid(row=0, column=3, sticky=tk.W)

        # Exit Button
        quit_button = tk.Button(window, text="EXIT",fg='red', command=window.destroy)
        quit_button.grid(row=7, column=0)

        # Input Parameters
        # ---------------- LABELS ----------------
        # Label for Number of components
        InputLabel1 = tk.Label(window, text="Number of Components")
        InputLabel1.grid(row=1, column=3, sticky=tk.W)

        # Label for Number of Iterations
        InputLabel2 = tk.Label(window, text="Max Iterations")
        InputLabel2.grid(row=2, column=3, sticky=tk.W)

        # Label for Tolerance
        InputLabel3 = tk.Label(window, text="Tolerance")
        InputLabel3.grid(row=3, column=3, sticky=tk.W)

        # ---------------- ENTRIES ----------------
        # Entry field for Number of components
        self.InputField1 = tk.Entry(window, textvariable = "components")
        self.InputField1.grid(row = 1, column = 4, sticky = tk.E + tk.W)

        # Entry field for Number of Iterationss
        self.InputField2 = tk.Entry(window, textvariable = "iterations")
        self.InputField2.grid(row = 2, column = 4, sticky = tk.E + tk.W)

        # Entry field for Tolerance
        self.InputField3 = tk.Entry(window, textvariable = "tolerance")
        self.InputField3.grid(row = 3, column = 4, sticky = tk.E + tk.W)

        # Button for the ICA function to be applied on the input image.
        process_button = tk.Button(window, text = "Apply", command = lambda: self.apply())
        process_button.grid(row=4, column=4)

    # Displays the image as a label on the main window once the browse button is clicked
    def browsefunc(self, window):
        filename = filedialog.askopenfile()

        # storing the browsed file name for passing to compute_ica_output
        self.input_image_list.append(filename.name)

        self.image = Image.open(filename.name)
        self.image.thumbnail((256, 256))

        self.photo = ImageTk.PhotoImage(self.image)
        self.labelPhoto = Label(window, image = self.photo)
        self.labelPhoto.grid(row = 5, column = 0)
        
   # Displays the final output images after applying ICA algorithm
    def apply(self):
        self.components = int(float(self.InputField1.get()))
        self.iterations = int(float(self.InputField2.get()))
        self.tolerance = float(self.InputField3.get())
        
        self.original_images, self.kspace_images, self.ica_images, self.kspace_output = self.compute_ica_output(
            self.input_image_list, self.components, self.iterations, self.tolerance)

        # displaying K-space of input image
        self.photo1 = ImageTk.PhotoImage(Image.fromarray(self.kspace_images[0]))
        self.labelPhoto = Label(window, image = self.photo1)
        self.labelPhoto.grid(row = 6, column = 0)

        # displaying output image after performing ICA on input image
        self.photo2 = ImageTk.PhotoImage(Image.fromarray(self.ica_images[0]))
        self.labelPhoto = Label(window, image = self.photo2)
        self.labelPhoto.grid(row = 5, column = 1)

        # displaying K-space of output image
        self.photo3 = ImageTk.PhotoImage(Image.fromarray(self.kspace_output[0]))
        self.labelPhoto = Label(window, image = self.photo3)
        self.labelPhoto.grid(row = 6, column = 1)

g = gui()
g.page1(window)
window.mainloop()
