from cryptography.fernet import Fernet
import base64

# Outer class Encryption that will do ciphering
class Encryption:

    # Inner class depending on the type of encryption algorithm used (here is AES using Fernet)
    class AES:
        cipher: Fernet

        def __init__(self, key: str):
            encoded_key = base64.urlsafe_b64encode(key.encode())
            self.cipher : Fernet = Fernet(encoded_key)

        # Encrypt method, change this according to the encryption algorithm used
        def encrypt(self, message: bytes):
            return self.cipher.encrypt(message)
        
        # Decrypt method, change this according to the encryption algorithm used
        def decrypt(self, message: bytes):
            return self.cipher.decrypt(message)

    key: str
    encryption_algorithm: AES

    # Constructor method
    def __init__(self, key: str):
        self.key : str = key
        self.encryption_algorithm : Encryption.AES = Encryption.AES(self.key)

    # Change key used for encryption
    def change_key(self, key: str):
        self.key = key
        self.encryption_algorithm = Encryption.AES(self.key)

    # Encrypt method
    def encrypt(self, message: bytes):
        return self.encryption_algorithm.encrypt(message)
    
    # Decrypt method
    def decrypt(self, message: bytes):
        return self.encryption_algorithm.decrypt(message)
    
    