import base64
import tkinter as tk
from tkinter import filedialog, messagebox
from controller import Controller
#from controller import [classes]

class ImageCryptGUI(tk.Tk): #GUI class definitions
    def __init__(self): #main window init
        super().__init__()
        self.title("ImageCrypt")
        self.geometry("800x600")
        self.controller = Controller(self) # creates the controller
        self.mode = tk.StringVar(value="encrypt") # toggle mode between encryption and decryption (as a var)
        self.create_widgets() # creating widgets (GUI methods)

    def create_widgets(self):

        self.mode_label = tk.Label(self, text="Mode:") # Mode selection (Encrypt or Decrypt)
        self.mode_label.pack(pady=5)

        self.encrypt_radio = tk.Radiobutton(self, text="Encrypt", variable=self.mode, value="encrypt", command=self.toggle_mode) # button for encryption mode
        self.encrypt_radio.pack(pady=5)
        self.decrypt_radio = tk.Radiobutton(self, text="Decrypt", variable=self.mode, value="decrypt", command=self.toggle_mode) # button for decryption mode
        self.decrypt_radio.pack(pady=5)

        self.image_path_label = tk.Label(self, text="Image Path:") # image path label + entry
        self.image_path_label.pack(pady=5)
        self.image_path_entry = tk.Entry(self, width=50) 
        self.image_path_entry.pack(pady=5)
        
        self.load_image_button = tk.Button(self, text="Load Image", command=self.load_image) # image button loading
        self.load_image_button.pack(pady=5)
        
        self.message_label = tk.Label(self, text="Hidden message to Embed:") # message input (encryption mode)
        self.message_label.pack(pady=5)
        self.message_entry = tk.Entry(self, width=50)
        self.message_entry.pack(pady=5)

        self.password_label = tk.Label(self, text="Password:") # password input (both modes)
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self, show="*", width=50)
        self.password_entry.pack(pady=5)

        self.salt_label = tk.Label(self, text="Salt value (don't forget it! Use for decryption):") # salt value output and input (both modes)
        self.salt_label.pack(pady=5)
        self.salt_entry = tk.Entry(self, width=50)
        self.salt_entry.pack(pady=5)
        
        self.process_button = tk.Button(self, text="Proceed", command=self.process_message) # to embed the message onto image button or to decrypt (both modes)
        self.process_button.pack(pady=5)
        
        self.output_text = tk.Text(self, height=10, width=70) # output area
        self.output_text.pack(pady=5)
        
        self.status_label = tk.Label(self, text="", fg="green") # status area
        self.status_label.pack(pady=5)

        self.toggle_mode() # init the toggle modes

    def load_image(self):
        image_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")]) # accepts PNG images
        if image_path:
            self.image_path_entry.delete(0, tk.END) # refreshes the path variable
            self.image_path_entry.insert(0, image_path)
            self.controller.load_image(image_path) # loads an image for imagehandler

    def process_message(self): #used for processs differentiation between the modes (encrypt or decrypt)
        if self.mode.get() == "encrypt": 
            self.embed_message()
        else:
            self.extract_message()
    
    def embed_message(self): 
        image_path = self.image_path_entry.get()
        message = self.message_entry.get()
        password = self.password_entry.get()
        
        if not image_path or not message or not password:
            messagebox.showwarning("Input Error", "Please provide all inputs: image path, message, and password") # error handling for encryption process
            return
        
        output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if output_path:
            self.controller.embed_message(message, password, output_path)
    
    def extract_message(self):
        password = self.password_entry.get()
        salt = self.salt_entry.get().encode() # converts the salt value to bytes
        
        if not password or not salt:
            messagebox.showwarning("Input Error", "Please provide the password and the salt value") # error handling for decryption process
            return
        
        self.controller.extract_message(password, salt)

    def update_status(self, message):
        self.status_label.config(text=message)

    def show_salt(self, salt):
        self.salt_label.pack(pady=5)
        self.salt_entry.pack(pady=5)
        self.salt_entry.delete(0, tk.END)
        self.salt_entry.insert(0, base64.urlsafe_b64encode(salt).decode())  # displays the salt value
    
    def display_extracted_text(self, text):
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, text)

    def toggle_mode(self): # toggle mode specific configs
        if self.mode.get() == "encrypt":
            self.process_button.config(text="Embed the hidden message")
            self.message_label.pack(pady=5)
            self.message_entry.pack(pady=5)
            self.salt_label.pack_forget()
            self.salt_entry.pack_forget()
            self.output_text.pack_forget()
        else:
            self.process_button.config(text="Decrypt image")
            self.message_label.pack_forget()
            self.message_entry.pack_forget()
            self.salt_label.config(text="Salt value (Required for decryption):")
            self.salt_label.pack(pady=5)
            self.salt_entry.pack(pady=5)
            self.output_text.pack(pady=5)