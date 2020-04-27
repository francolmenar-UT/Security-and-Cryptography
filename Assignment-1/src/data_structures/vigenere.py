class Vigenere:

    def __init__(self):
        self.plaintext = ""
        self.ciphertext = ""
        self.keylength = None
        self.key = ""

    def print_vigenere(self):
        print(
            "Vigenere text with:\nPlaintext: %s\nCiphertext: %s\nKeylength: %s\nKey: %s" % (
                self.plaintext, self.ciphertext, self.keylength, self.key))


