from sys import argv
from helpers import alphabet_position, rotate_character

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

def user_input_is_valid(cl_args):
    if len(cl_args) < 2:
        return False
    elif not cl_args[1].isdigit():
        return False
    else:
        return True

#if user_input_is_valid(argv):

    #print("Type a message")
#    text = input()
#    while len(text) == 0:
#        text = input('you must type a message\n')
#    valid = True
#    for char in text:
#        if not char.isalpha():
#            valid = False
#            break
#    if valid:
#        print(encrypt(text,argv[1]))
    #else:
        #print("message not encrytable")
#else:
    #print("user input is not valid")

#exit()
