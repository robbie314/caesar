def alphabet_position(letter):
    """Find the position number of an alphabet"""
    letter = letter.lower()
    return ord(letter) - 97

#print(alphabet_position('y'))

def rotate_character(char, rot):
    """rotating char by rot numbers to the right, return a new string of length 1"""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    letter = char

    new_string = ''
    if ord(letter) != 32:

        if not char.isalpha():
            new_string = new_string + char
        else:
            if char.isupper():
                rotated_index = alphabet_position(letter) + int(rot)
                if rotated_index < 26:
                    new_string = new_string + alphabet2[rotated_index]
                else:
                    new_string = new_string + alphabet2[rotated_index % 26]
            else:
                rotated_index = alphabet_position(letter) + int(rot)
                if rotated_index < 26:
                    new_string = new_string + alphabet[rotated_index]
                else:
                    new_string = new_string + alphabet[rotated_index % 26]
    else:
        new_string += ' '

    return new_string

#print(rotate_character('6', 13))
#print(rotate_character('c', 27))

def encrypt(text, rot):
    """ return result of rotating ea ltr in text by rot places to the right"""

    new_text = ''
    for char in text:
        if char.isalpha():
            new_text +=  rotate_character(char, rot)
        else:
            new_text += char #if not alphabet, considers the space
    return new_text

#print(encrypt('LaunchCode', 1))
