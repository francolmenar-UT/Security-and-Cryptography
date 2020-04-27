from src.constants import const
from itertools import permutations


def read_text(text_object, filename, mode):
    """
    Read a given plain text and store it into the field "plaintext" of the text_object
    :param mode: Flag representing if what is going to be read is a ciphertext or a plaintext
    :param text_object: Object which is going to save the read plaintext
    :param filename: Name of the file which is going to be read
    :return: 0 if it has not happened no error. Otherwise -1 is returned
    """
    f = open(filename, "r")
    if f.mode == 'r':
        contents = f.read()
        if mode == const.CYPHER_MODE:
            text_object.ciphertext = contents
            return 0
        elif mode == const.PLAINTEXT_MODE:
            text_object.plaintext = contents
            return 0
        else:
            print("Error while reading the text [Incorrect mode code]")
            return -1
    else:
        print("Error while reading the text")
        return -1


def shift_text(origin, shift):
    """
    Shifts each of the letters of the given text the amount of positions given
    :param origin: The text which is going to be shifted
    :param shift: The amount of positions the original text os shifted
    :return: The resulting text from the shifting of letter positions
    """
    # Defining the variable which will store the resulting text
    result = ""
    for letter in origin:
        # The space is not shifted
        if letter == const.SPACE:
            result += const.SPACE
        # Shift the letter
        else:
            pos = ord(letter)
            pos = (pos - 65 + shift) % 26 + 65
            result += chr(pos)
    return result


def divide_text_blocks(text, keylength):
    # Length of the text
    div_number = int(len(text) / keylength)
    # Calculate the number of letters per division of the text
    if len(text) % keylength != 0:
        div_number += 1

    # List with all the divisions of the text
    divisions = []

    # Add padding to the text
    if len(text) % keylength != 0:
        for i in range(len(text), len(text) + len(text) % keylength):
            text += " "

    # Iterate through the different divisions of the cipher text
    for i in range(0, 1):
        aux = ""
        # Iterate through the ciphertext and add letters to each division
        for j in range(0, keylength):
            # Add the correct letter to the string
            aux += text[j + keylength * i]
        # Add the string to the array of divisions
        divisions.append(aux)
    return divisions


def permute(text):
    perms = [''.join(p) for p in permutations(text)]
    aux = set(perms)
    for i in range(0, len(aux)):
        elem = aux.pop()
        length = len(elem)
        if elem[length - 1] == "X" and elem[length - 2] == "X" and elem[length - 3] == "X":
            print(elem)


def kasiski():
    return 9


def divide_text(text, keylength):
    # Length of the text
    div_number = int(len(text) / keylength)
    # Calculate the number of letters per division of the text
    if len(text) % keylength != 0:
        div_number += 1

    # List with all the divisions of the text
    divisions = []

    # Add padding to the text
    if len(text) % keylength != 0:
        for i in range(len(text), len(text) + len(text) % keylength):
            text += " "

    # Iterate through the different divisions of the cipher text
    for i in range(0, keylength):
        aux = ""
        # Iterate through the ciphertext and add letters to each division
        for j in range(0, div_number):
            # Add the correct letter to the string
            aux += text[j * keylength + i]
        # Add the string to the array of divisions
        divisions.append(aux)
    return divisions
