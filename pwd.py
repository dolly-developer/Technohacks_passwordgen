# this module consist all alphabates, digits and special characters
import string  

 # this module helps to configure pasword with secuirty
import secrets


#storing values from string module

letters_choice=string.ascii_letters
numbers=string.digits
spl_char=string.punctuation

password=""
collect_char=letters_choice+numbers+spl_char

for i in range(8):
   password += ''.join(secrets.choice(collect_char)) #join method will join all random characters into one string.
print("Passowrd is ",password)
