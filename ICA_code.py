from sklearn.decomposition import FastICA
from sklearn.preprocessing import Normalizer
from matplotlib import pyplot as plt
import numpy as np
import pylab as pl
import glob
import cv2
import os

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

def compute_ica_output(image_list, no_of_components, max_iterations, tolerance):
    original_images = []
    kspace_images = []
    ica_images = []
    kspace_output = []
    for file in image_list:
        image_name = file
        input_image = cv2.imread(image_name, 0)
        original_images.append(input_image)
        input_image = np.fft.fft2(input_image)
        input_image = np.fft.fftshift(input_image)
        img = np.uint8(np.log(np.abs(input_image) + 1) * 10)
        kspace_images.append(img)

        img = np.fft.ifftshift(input_image)
        img = np.fft.ifft2(img)
        img = np.uint8(np.log(np.abs(img) + 1) * 10)

        ica = FastICA(n_components = no_of_components, max_iter = max_iterations, tol = tolerance)
        ica.fit(img)
        image_ica = ica.fit_transform(img)
        image_restored = ica.inverse_transform(image_ica)

        imagefcs = np.zeros((image_restored.shape[0], image_restored.shape[1]), np.float)
        for i in range(image_restored.shape[0]):
            for j in range(image_restored.shape[1]):
                imagefcs[i, j] = np.log(np.abs(image_restored[i, j]) * 10)
        ica_images.append(imagefcs)

        imagefcs = np.fft.fft2(imagefcs)
        imagefcs = np.fft.fftshift(imagefcs)
        output_kspace = np.uint8(np.log(np.abs(imagefcs) + 1) * 10)
        kspace_output.append(output_kspace)
    return original_images, kspace_images, ica_images, kspace_output

input_image_list = ['P10-0001.jpg', 'P10-0002.jpg', 'P10-0003.jpg', 'P10-0004.jpg', 'P10-0005.jpg']
original_images, kspace_images, ica_images, kspace_output = compute_ica_output(input_image_list, 15, 100000, 0.000001)

plt.subplot(141),plt.imshow(original_images[1], cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(142),plt.imshow(kspace_images[1], cmap = 'gray')
plt.title('K-space Input'), plt.xticks([]), plt.yticks([])
plt.subplot(143),plt.imshow(ica_images[1], cmap = 'gray')
plt.title('ICA Output'), plt.xticks([]), plt.yticks([])
plt.subplot(144),plt.imshow(kspace_output[1], cmap = 'gray')
plt.title('K-space Output'), plt.xticks([]), plt.yticks([])

plt.show()

window = tk.Tk() # window is the main window which pops up when the program runs
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


        # Output Image


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
