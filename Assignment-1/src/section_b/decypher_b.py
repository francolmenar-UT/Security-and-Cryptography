from src.functions import func
from src.data_structures.permutation import Permutation
from src.constants import const

from nltk import everygrams
import enchant

# Create the object
text = Permutation()

text.keylength = 7

# Read the ciphertext
# if func.read_text(text, const.CYPHERTEXT2, const.CYPHER_MODE) == -1:
# exit(-1)

# text.blocks = func.divide_text_blocks(text.ciphertext, text.keylength)

func.permute("XSXDXIE")

# d = enchant.Dict("en_US")

# aux = [''.join(_ngram) for _ngram in everygrams(text.blocks[0]) if
      # d.check(''.join(_ngram)) and len(_ngram) == text.keylength]

# print(text.blocks[0])

# list(everygrams(text.blocks[0]))
# print(aux)
for i in range(0, len(div)):
    print(div[i])
