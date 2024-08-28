from encryptionhandler import EncryptionHandler

def main():
    password = "Hello"
    message = "Hello world!"

    # Initialize the encryption handler with the password
    encryption_handler = EncryptionHandler(password)

    # Encrypt the message
    encrypted_message, salt = encryption_handler.encrypt(message)
    print(f"Encrypted message: {encrypted_message}")
    print(f"Salt used: {salt.hex()} (Store this for decryption)")

    # Assume later or elsewhere, we want to decrypt
    # Initialize with the same password and use the stored salt
    decrypted_message = encryption_handler.decrypt(encrypted_message, salt)
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()