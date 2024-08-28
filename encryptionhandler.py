import base64
import os
import cryptography
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC #derives a secure key from the user password
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet #provides symmetric encryption

class EncryptionHandler:
    def __init__(self, password: str, salt: bytes = None):
        self.password = password.encode() # convert the string to bytes
        self.salt = salt or os.urandom(16) # generates a salt (random value as an input for a cryptographic func before processing)
        self.key = self._derive_key() # gets a cryptographic key from the password

    def _derive_key(self) -> bytes:
        # uses PBKDF2 to derive a cryptographic key from the password
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32, #32 bit key required for Fernet
            salt=self.salt,
            iterations=100000, #can be a higher number for extra security at the cost of speed
            backend=default_backend()
        )
        derived_key = kdf.derive(self.password)
        return base64.urlsafe_b64encode(derived_key)
    
    def encrypt(self, message: str) -> (bytes, bytes): # type: ignore
        #encrypts the string message using the derived key and returns it (both encrypted msg and salt)
        fernet = Fernet(self.key)
        encryptedString = fernet.encrypt(message.encode())
        return encryptedString, self.salt
    
    def decrypt(self, encryptedMessage: bytes, salt: bytes) -> str:
        #decrypts the encrypted msg via the derived key, the salt must be the same as used for encryption prior
        self.salt = salt
        self.key = self._derive_key()
        fernet = Fernet(self.key)
        try:
            decryptedString = fernet.decrypt(encryptedMessage)
            return decryptedString.decode()
        except cryptography.fernet.InvalidToken:
            raise ValueError("Decryption failed. The data may be corrupted, or the password/salt may be incorrect")
    
    def getSalt(self) -> bytes:
        #returns the salt used for the key derivation
        return self.salt