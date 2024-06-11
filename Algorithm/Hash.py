import hashlib

# Outer class Hash that will do hashing function
class Hash:

    # Inner class depending on the type of hash algorithm used (here is SHA256)
    class SHA256:
        # Hash method, change this according to the hash algorithm used
        def hash(self, message: str):
            sha256_hash = hashlib.sha256(message.encode())
            hashed_message = sha256_hash.digest()
            
            return hashed_message

    hash_algorithm: SHA256

    # Constructor method
    def __init__(self):
        self.hash_algorithm : Hash.SHA256 = Hash.SHA256()

    # Hash method to call hash function based on inner class
    def hash(self, message: str):
        return self.hash_algorithm.hash(message)
    