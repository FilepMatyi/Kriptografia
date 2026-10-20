#!/usr/bin/env python3 -tt
from itertools import cycle
"""
File: crypto.py
---------------
Assignment 1: Cryptography
Course: CS 41
Name: Filep Matyas
SUNet: fmim2442

Replace this with a description of the program.
"""
import utils



def check_text(text):
    if not isinstance(text, str):
        raise TypeError("The message must be a string.")

    return text


def check_number(number):
    if type(number) is not int:
        raise TypeError("The key must be an integer.")

    if number <= 0:
        raise ValueError("The key must be greater than zero.")


def check_keyword(keyword):
    if not isinstance(keyword, str):
        raise TypeError("The keyword must be a string.")

    keyword = keyword.upper()

    if not keyword:
        raise ValueError("The keyword cannot be empty.")

    if any(not ("A" <= char <= "Z") for char in keyword):
        raise ValueError("The keyword must contain only letters A-Z.")

    return keyword


# Caesar Cipher

def encrypt_caesar(plaintext):
    """Encrypt plaintext using a Caesar cipher.

    ord fggv Karakter to - asci

    Add more implementation details here.
    """
    plaintext = check_text(plaintext).upper()

    caesarcode_list = []

    for karakter in plaintext:
        if 65 <= ord(karakter) <= 90:
            pos_karakter = ord(karakter) - 65
            
            shifted_char = (pos_karakter + 3) % 26
            
            caesarcode_list.append(chr(shifted_char + 65))
        else:
            caesarcode_list.append(karakter)

    caesarcode = "".join(caesarcode_list)
    #raise NotImplementedError  # Your implementation here

    return caesarcode
    #return caesarcode_list


def decrypt_caesar(ciphertext):
    """Decrypt a ciphertext using a Caesar cipher.

    Add more implementation details here.
    """
    ciphertext = check_text(ciphertext).upper()


    plaintext = []

    for karakter in ciphertext:
        if 65 <= ord(karakter) <= 90:
            pos_karakter = ord(karakter) - 65
            
            shifted_char = (pos_karakter - 3) % 26
            
            plaintext.append(chr(shifted_char + 65))
        else:
            plaintext.append(karakter)
    
    plaintext_string = "".join(plaintext)

    return plaintext_string
    #raise NotImplementedError  # Your implementation here


# Vigenere Cipher


def encrypt_vigenere(plaintext, keyword):
    plaintext = check_text(plaintext).upper()
    keyword = check_keyword(keyword)

    result = []
    k = 0

    for karakter in plaintext:
        if "A" <= karakter <= "Z":
            pos_karakter = ord(karakter) - 65
            pos_keyword = ord(keyword[k % len(keyword)]) - 65

            shifted_char = (pos_karakter + pos_keyword) % 26

            result.append(chr(shifted_char + 65))
            k += 1
        else:
            result.append(karakter)

    return "".join(result)


    #raise NotImplementedError  # Your implementation here


def decrypt_vigenere(ciphertext, keyword):
    """Decrypt ciphertext using a Vigenere cipher with a keyword.

    Add more implementation details here.
    """
    
    ciphertext = check_text(ciphertext).upper()
    keyword = check_keyword(keyword)
    
    result = []
    k = 0
    
    for karakter in ciphertext:
        if "A" <= karakter <= "Z":
            pos_karakter = ord(karakter) - 65
            pos_keyword = ord(keyword[k % len(keyword)]) - 65
    
            shifted_char = (pos_karakter - pos_keyword) % 26
    
            result.append(chr(shifted_char + 65))
            k += 1
        else:
            result.append(karakter)
    
    return "".join(result)
    
    
    #raise NotImplementedError  # Your implementation here


def encrypt_scytale(plaintext, key):
    check_text(plaintext)
    check_number(key)
   
   
    result = ""



    for row in range(key):
        for i in range(row, len(plaintext), key):
            result += plaintext[i]

    return result


def decrypt_scytale(ciphertext, key):

    check_text(ciphertext)
    check_number(key)

    result = [""] * len(ciphertext)
    index = 0

    for row in range(key):
        for i in range(row, len(ciphertext), key):
            result[i] = ciphertext[index]
            index += 1

    return "".join(result)



def encrypt_railfence(plaintext, num_rows):
    check_text(plaintext)
    check_number(num_rows)

    if num_rows == 1:
        return plaintext

    rows = [""] * num_rows

    row = 0
    direction = 1

    for char in plaintext:
        rows[row] += char

        if row == 0:
            direction = 1
        elif row == num_rows - 1:
            direction = -1

        row += direction

    return "".join(rows)


def decrypt_railfence(ciphertext, num_rows):
    check_text(ciphertext)
    check_number(num_rows)

    if num_rows == 1:
        return ciphertext

    pattern = []
    row = 0
    direction = 1

    for char in ciphertext:
        pattern.append(row)

        if row == 0:
            direction = 1
        elif row == num_rows - 1:
            direction = -1

        row += direction

    result = [""] * len(ciphertext)
    index = 0

    for rail in range(num_rows):
        for i in range(len(ciphertext)):
            if pattern[i] == rail:
                result[i] = ciphertext[index]
                index += 1

    return "".join(result)



# Merkle-Hellman Knapsack Cryptosystem

def generate_private_key(n=8):
    """Generate a private key for use in the Merkle-Hellman Knapsack Cryptosystem.

    Following the instructions in the handout, construct the private key components
    of the MH Cryptosystem. This consistutes 3 tasks:

    1. Build a superincreasing sequence `w` of length n
        (Note: you can check if a sequence is superincreasing with `utils.is_superincreasing(seq)`)
    2. Choose some integer `q` greater than the sum of all elements in `w`
    3. Discover an integer `r` between 2 and q that is coprime to `q` (you can use utils.coprime)

    You'll need to use the random module for this function, which has been imported already

    Somehow, you'll have to return all of these values out of this function! Can we do that in Python?!

    @param n bitsize of message to send (default 8)
    @type n int

    @return 3-tuple `(w, q, r)`, with `w` a n-tuple, and q and r ints.
    """
    raise NotImplementedError  # Your implementation here

def create_public_key(private_key):
    """Create a public key corresponding to the given private key.

    To accomplish this, you only need to build and return `beta` as described in the handout.

        beta = (b_1, b_2, ..., b_n) where b_i = r × w_i mod q

    Hint: this can be written in one line using a list comprehension

    @param private_key The private key
    @type private_key 3-tuple `(w, q, r)`, with `w` a n-tuple, and q and r ints.

    @return n-tuple public key
    """
    raise NotImplementedError  # Your implementation here


def encrypt_mh(message, public_key):
    """Encrypt an outgoing message using a public key.

    1. Separate the message into chunks the size of the public key (in our case, fixed at 8)
    2. For each byte, determine the 8 bits (the `a_i`s) using `utils.byte_to_bits`
    3. Encrypt the 8 message bits by computing
         c = sum of a_i * b_i for i = 1 to n
    4. Return a list of the encrypted ciphertexts for each chunk in the message

    Hint: think about using `zip` at some point

    @param message The message to be encrypted
    @type message bytes
    @param public_key The public key of the desired recipient
    @type public_key n-tuple of ints

    @return list of ints representing encrypted bytes
    """
    raise NotImplementedError  # Your implementation here

def decrypt_mh(message, private_key):
    """Decrypt an incoming message using a private key

    1. Extract w, q, and r from the private key
    2. Compute s, the modular inverse of r mod q, using the
        Extended Euclidean algorithm (implemented at `utils.modinv(r, q)`)
    3. For each byte-sized chunk, compute
         c' = cs (mod q)
    4. Solve the superincreasing subset sum using c' and w to recover the original byte
    5. Reconsitite the encrypted bytes to get the original message back

    @param message Encrypted message chunks
    @type message list of ints
    @param private_key The private key of the recipient
    @type private_key 3-tuple of w, q, and r

    @return bytearray or str of decrypted characters
    """
    raise NotImplementedError  # Your implementation here

