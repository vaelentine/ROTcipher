import string
from time import sleep

# ROT CIPHER (UPPERCASE ONLY)
alpha_list = list(string.ascii_uppercase)


def encrypt(my_str, rot):
    encrypted = ''  # empty string for the converted word
    for i in range(len(my_str)):  # find letter in the alpha list
        try:
            encrypted += (alpha_list[(((alpha_list.index(my_str[i].upper())) + rot) % 26)])  # rotate by amt
        except ValueError: #skip over non ascii
            encrypted += my_str[i]
    return encrypted


def decrypt(encr, rota):
    rota = -int(rota)
    return encrypt(encr, rota)