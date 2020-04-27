class Permutation:

    def __init__(self):
        self.plaintext = ""
        self.ciphertext = ""
        self.keylength = None
        self.key = ""
        self.blocks = None

    def print_caesar(self):
        print(
            "Caesar text with:\nPlaintext: %s\nCiphertext: %s\nShift: %s" %
            (self.plaintext, self.ciphertext, self.shift))
