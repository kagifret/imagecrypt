import base64
import cryptography
from cryptography.fernet import Fernet

class EncryptionHandler:
    def __init__(self, password: str):
        self.password = password.encode()  # convert the string to bytes
        self.key = self._derive_key()

    def _derive_key(self) -> bytes: # derives a key from the password input
        derived_key = base64.urlsafe_b64encode(self.password.ljust(32)[:32]) # hashes the password in base64
        return derived_key

    def encrypt(self, message: str) -> bytes:
        fernet = Fernet(self.key)
        encrypted_message = fernet.encrypt(message.encode())
        return encrypted_message

    def decrypt(self, encrypted_message: bytes) -> str:
        fernet = Fernet(self.key)
        try:
            decrypted_message = fernet.decrypt(encrypted_message)
            return decrypted_message.decode()
        except cryptography.fernet.InvalidToken:
            raise ValueError("Decryption failed. The data may be corrupted, or the password may be incorrect")
