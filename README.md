# Hash and Symmetric Encryption

## 💿 Program Description 
This program is written to implement message authentication and integrity checking technique. As we all know, MAC (Message Authentication Code) is often used to check for message authentication and integrity. But there is other technique to do message authentication and integrity checking. One of them is with conventional encryption using hash function and symmetric encryption. Here is how:

1. Hash the plain message using a hash function
2. Encrypt the hash using symmetric encryption with a key
3. Append hash encryption result to the message and send it to receiver
4. At receiver, get the encrypted hash
5. Decrypt the encrypted hash using the same symmetric encryption and key
6. Hash again the plain message using the same hash function
7. If plain message hash and decrypted hash result is identical, then we can safely conclude that message has not been tampered and the receiver is authenticated to see the message

In this program, I used SHA-256 hash function and AES symmetric encryption for easier implementation.

## 🔃 Needed Dependencies

1. Make sure you already have installed Python language on your device.
2. Install cryptography package using this command:
    ``` bash
    pip install cryptography
    ```

## ⚙️ How To Run
1. Get the latest release from this repository, or clone the repository using this command:
    ``` bash
    git clone https://github.com/GoDillonAudris512/Hash-and-Symmetric-Encryption.git
    ```
2. Run the program using this command
    ``` bash
    python Main.py
    ```
    Now you can try to embed a message with code or verify message authentication and integrity.

## Author
Created with love by Go Dillon Audris