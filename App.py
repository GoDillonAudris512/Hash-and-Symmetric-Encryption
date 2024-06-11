from Algorithm.Hash import Hash
from Algorithm.Encryption import Encryption
import base64

# Class that will embed signature of a message and verify a message with signature
# This will act as a message authentication and message integrity checker
# Serving as another technique besides usinG MAC (Message Authentication Code) Algorithm
class App:
    CODE_LENGTH = 188
    hash: Hash
    encryption: Encryption

    # Constructor method
    def __init__(self, key: str):
        self.hash : Hash = Hash()
        self.encryption : Encryption = Encryption(key)
    
    # Embed a "code" to message before delivery using hash and symmetric encryption
    def embed(self, message: str):
        raw_message = message

        # Hash the message first
        hashed_message = self.hash.hash(raw_message)

        # Encrypt the hash
        encrypted_hash_message = self.encryption.encrypt(hashed_message)

        # Encode encryption result using base64 and turn it to string
        encoded_code = base64.b64encode(encrypted_hash_message)
        encoded_code = encoded_code.decode()

        # Embed the code to the raw message, return it
        return raw_message + encoded_code
    
    # Verify a message with code with a key. This will check for message authentication and integrity
    def verify(self, message: str):
        message_with_code = message

        if len(message_with_code) <= self.CODE_LENGTH:
            raise Exception("No code found on message")
        
        try:
            raw_message = message_with_code[:(len(message_with_code)-self.CODE_LENGTH)]
            code = message_with_code[(len(message_with_code)-self.CODE_LENGTH):]

            # Decode the code from base64
            decoded_code = code.encode()
            decoded_code = base64.b64decode(decoded_code)

            # Decrypt the code using encryption algorithm
            decrypted_hash_message = self.encryption.decrypt(decoded_code)

            # Hash the raw message
            hashed_message = self.hash.hash(raw_message)

            # Compare decrypted hash with hashed message
            if decrypted_hash_message == hashed_message:
                return True
            else:
                return False
        except:
            # Catch all exception, either when decoding or decrypting
            # All this indicate message has been tampered or key is wrong
            return False
