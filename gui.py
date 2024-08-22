import tkinter as tk
from tkinter import filedialog, messagebox
#from controller import [classes]

class ImageCryptGUI: #GUI class definitions
    def __init__(self, master): #main window init
        self.master = master
        self.master.title("ImageCrypt")
        self.master.geometry("800x600")
        self.create_widgets()

    def create_widgets(self): #methods
        self.test = tk.Button(self.master, text="Test input text", command=self.testclick)
        self.test.pack(pady=20)

        self.message_test = tk.Entry(self.master, width=30)
        self.message_test.pack(pady=20)

    def testclick(self): #action
        messagebox.showinfo("GUI test success", self.message_test.get())