from src.constants import const
from src.data_structures.caesar import Caesar
from src.functions import func

# Create the object
text = Caesar()

# Read the ciphertext
if func.read_text(text, const.CYPHERTEXT1, const.CYPHER_MODE) == -1:
    exit(-1)

# Define the amount of places which the text is going to be shifted
text.shift = const.CAESAR_SHIFT

# Shifting the text
text.plaintext = func.shift_text(text.ciphertext, text.shift)

# Printing the result
text.print_caesar()
