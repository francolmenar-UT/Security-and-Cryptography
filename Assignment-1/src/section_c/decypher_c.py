from src.functions import func
from src.data_structures.vigenere import Vigenere
from src.constants import const

# Create the object
text = Vigenere()

# Obtain the key length
text.keylength = func.kasiski()

# Read the ciphertext
func.read_text(text, const.CYPHERTEXT3, const.CYPHER_MODE)

divisions = func.divide_text(text.ciphertext, text.keylength)

for i in range(0, len(divisions)):
    print("--------------------------------------")
    print(divisions[i])
