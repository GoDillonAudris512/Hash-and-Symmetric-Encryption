from App import App

# Main class to start program
class Main:
    # Ask key from user
    def ask_for_key(self):
        key = ""
        keyIsValid = False

        while not keyIsValid:
            key = input("Input a key: ")

            if len(key) != 32:
                print("Please input a key with length of 32")
            else:
                keyIsValid = True

        return key
    
    # Ask message from user
    def ask_for_message(self):
        message = ""
        messageIsValid = False

        while not messageIsValid:
            message = input("Input a message: ")

            if message.isspace():
                print("Please input a message that contains characters")
            else:
                messageIsValid = True

        return message

    # Embed message from user
    def embed_message(self):
        key = self.ask_for_key()
        app = App(key)
        print()

        message = self.ask_for_message()
        print()

        message_with_code = app.embed(message)
        print("Embed message:")
        print(message_with_code)
        
    # Verify a message with code from user
    def verify_message(self):
        key = self.ask_for_key()
        app = App(key)
        print()

        message_with_code = self.ask_for_message()
        print()

        try:
            print("Result:")
            message_valid = app.verify(message_with_code)
            
            if message_valid:
                print("Message has not been tampered and key is right")
            else:
                print("Either key is wrong or message has been tampered")

        except Exception as e:
            print(e)

    # Run the main program
    def run(self):
        while True:
            print("===============================")
            print("Choose program functionality (1-3):")
            print("1. Embed a message")
            print("2. Verify a message with code")
            print("3. Exit program")
            print("===============================")

            command = input("> ")

            if command == "1":
                self.embed_message()
            elif command == "2":
                self.verify_message()
            elif command == "3":
                print("Program exited...")
                exit()
            else:
                print("Invalid command")

if __name__ == "__main__":
    Main().run()