import tkinter as tk
from modules.gui import ImageCryptGUI #import GUI class from gui.py

def main():
    app = ImageCryptGUI()

    app.mainloop() #Tkinter event loop

if __name__ == "__main__":
    main()