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

# Caesar Cipher

def encrypt_caesar(plaintext):
    """Encrypt plaintext using a Caesar cipher.

    ord fggv Karakter to - asci

    Add more implementation details here.
    """

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
    """Encrypt plaintext using a Vigenere cipher with a keyword.

    Add more implementation details here.
    """

    vigenere_code = []

    for karakter, karakter2 in zip(plaintext, cycle(keyword)):
        if 65 <= ord(karakter) <= 90:
            pos_karakter = ord(karakter) - 65
            pos_keyword = ord(karakter2) - 65 # 0-25 kozti szamokka alakitjuk
            
            shifted_char = (pos_karakter + pos_keyword) % 26
            
            vigenere_code.append(chr(shifted_char + 65))
        else:
            vigenere_code.append(karakter)

    vigenere = "".join(vigenere_code)

    return vigenere

    #raise NotImplementedError  # Your implementation here


def decrypt_vigenere(ciphertext, keyword):
    """Decrypt ciphertext using a Vigenere cipher with a keyword.

    Add more implementation details here.
    """
    
    vigenere_decode = []
   
    for karakter, karakter2 in zip(ciphertext, cycle(keyword)):
        if 65 <= ord(karakter) <= 90:
            pos_karakter = ord(karakter) - 65
            pos_keyword = ord(karakter2) - 65 # 0-25 kozti szamokka alakitjuk
               
            shifted_char = (pos_karakter - pos_keyword) % 26
               
            vigenere_decode.append(chr(shifted_char + 65))
        else:
            vigenere_decode.append(karakter)
   
    vigenere = "".join(vigenere_decode)
   
    return vigenere
    
    #raise NotImplementedError  # Your implementation here


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

