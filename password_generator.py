import random
import string

print("Welcome To Your Password Generator")
print("==================================")

chars = string.ascii_lowercase+string.ascii_uppercase+'!@$%^&*(),?'+'0123456789'

number_of_pws = input('Number of passwords to generate: ')
number_of_pws = int(number_of_pws)

length_of_pw = input('Input password length: ')
length_of_pw = int(length_of_pw)

print('\nhere are your passwords: ')

for pwd in range(number_of_pws):
    passwords = ""
    for c in range(length_of_pw):
        passwords += random.choice(chars)
    print(passwords)
