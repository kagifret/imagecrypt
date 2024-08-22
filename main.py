import tkinter as tk
from gui import ImageCryptGUI #import GUI class from gui.py

def main():
    root = tk.Tk() #Main Tkinter window

    app = ImageCryptGUI(root) #Instance of a ImageCryptGUI class

    root.mainloop() #Tkinter event loop

if __name__ == "__main__":
    main()