'''RANDOM PASSWORD GENERATOR'''
import random
import string#collection of string constants

pass_len=10

charValues=string.ascii_letters+string.punctuation+string.digits#returns any random choice 

#list comprehension for i in range(n):
password="".join([random.choice(charValues) for i in range(pass_len)])#concatenates the strings in the list
print("Your random password is:",password)

#password=""
#for i in range(pass_len):
#   password+=(random.choice(charValues))

#print("Your random password is:",password)