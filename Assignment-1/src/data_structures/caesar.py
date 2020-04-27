class Caesar:

    def __init__(self):
        self.plaintext = ""
        self.ciphertext = ""
        self.shift = None

    def print_caesar(self):
        print(
            "Caesar text with:\nPlaintext: %s\nCiphertext: %s\nShift: %s" %
            (self.plaintext, self.ciphertext, self.shift))
