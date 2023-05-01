#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Module 3: Individual Programming Assignment 1

Thinking Like a Programmer

This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

import string

letter = input("Enter letter:")
shift = int(input("Enter the number by which to shift the letter:")) 

def shift_letter(letter, shift):
    alphabet = list(string.ascii_uppercase)
    
    if letter == " ":
        output = " "
    else: 
        orig_index = alphabet.index(letter)
        if orig_index + shift <= 25:
            output = alphabet[orig_index + shift]
        elif orig_index + shift > 25:
            output = alphabet[orig_index + shift - 26]
    return output

print(shift_letter(letter, shift))

def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
import string

message = input("Enter message:")
shift = int(input("Enter the number by which to shift the letters:"))

def caesar_cipher(message, shift):
    alphabet = list(string.ascii_uppercase)
    alphabet.append(' ')
    index_lst = []
    new_word = ''
    for letter in message:
        index = alphabet.index(letter)
        if index == 26:
            index_lst.append(index)
        elif index + shift < 26:
            index_lst.append(index + shift)
        elif index + shift >= 26: 
            index_lst.append(index + shift - 26)
    
    for i in index_lst:
        new_word = new_word + str(alphabet[i])
    return new_word 

print(caesar_cipher(message, shift)) 

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
import string

letter = input("Enter letter:")
letter_shift = input("Enter letter shift:")

def shift_by_letter(letter, letter_shift):
    alphabet = list(string.ascii_uppercase)
    
    if letter == " ":
        output = " "
    else:     
        orig_index = alphabet.index(letter)
        shift = alphabet.index(letter_shift)
        if orig_index + shift <= 25:
            output = alphabet[orig_index + shift]
        elif orig_index + shift > 25:
            output = alphabet[orig_index + shift - 26]
    return output

print(shift_by_letter(letter, letter_shift))

def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
import string

message = input("Enter message:")
key = input("Enter key:")

def vigenere_cipher(message, key): 
    alphabet = list(string.ascii_uppercase)
    alphabet.append(' ')
    index_lst = []
    key_lst = []
    key_index_lst = []
    shift = []
    new_word = ''

    #if length of message != key
    if len(message) > len(key):
        key = (key * (int(len(message)/len(key))+1))[:len(message)]

    #split letters of key
    for letter in key:
        key_lst.append(letter)
    
    #assign index number to each letter in key
    for a in key_lst:
        key_index = alphabet.index(a)
        key_index_lst.append(key_index)
        
    #assign index number to each letter in message
    for l in message:
        index = alphabet.index(l)
        index_lst.append(index)
    
    #shift
    for i in range(len(index_lst)):
        if index_lst[i] == 26:
            shift.append(index_lst[i])
        elif index_lst[i] + key_index_lst[i] < 26:
            shift.append(index_lst[i] + key_index_lst[i])
        elif index_lst[i] + key_index_lst[i] >= 26:
            shift.append(index_lst[i] + key_index_lst[i] - 26)
    
    #converting back to letters
    for m in shift:
        new_word = new_word + str(alphabet[m])
    return new_word  

print(vigenere_cipher(message, key))


# In[ ]:




