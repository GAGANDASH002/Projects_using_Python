#A cipher is a method used in cryptography for performing encryption or decryption.
#Essentially, it's a set of algorithms that you apply to your data (plaintext) to 
#transform it into an unrecognizable form (ciphertext). This process helps to protect sensitive information from unauthorized access.

import random
import string

chars= " " + string.ascii_letters+string.punctuation+string.digits
chars = list(chars)
key=chars.copy()

random.shuffle(key)#shuffles the list key

#Encryption:

text=input("Enter text to be encrypted")
cipher_text=""

for letter in text:
    index=chars.index(letter)
    cipher_text += key[index]

print(f"Original Message : {text}")
print(f"Encrypted Message : {cipher_text}")

#Decryption:

cipher_text=input("Enter text to be decrypted")
text=""

for letter in cipher_text:
    index=key.index(letter)
    text += chars[index]

print(f"Encrypted Message : {cipher_text}")
print(f"Original Message :  {text}")


