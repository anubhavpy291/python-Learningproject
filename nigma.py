import random
import string

chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

key = ['R', 'a', 'c', 'J', 'F', 'H', '2', 'S', 'm', 'd', 'G', 'D', '7', '1', '6', 'b', '5', 'q', 'T', 'Q', 'I', 'i', 'E', '8', 'j', 'O', 'l', 'Y', 'P', 'A', 'K', 'U', 't', 'f', 'g', 'w', 'n', 'u', 'B', 's', 'C', 'M', 'r', '9', 'o', 'k', 'x', 'e', 'X', 'W', 'V', 'z', 'y', 'v', 'p', '4', 'L', '0', 'N', 'Z', 'h', '3']
#random.shuffle(key)
#print(f"charcrs: {chars}")
#print(f"key: {key}")
def enc():
    enc = input("enter for encryption: ")
    l = ""

    for let in enc:
        ind = chars.index(let)
        l += key[ind]
    print(l)
def dec():
    dec = input("enter for dencryption: ")
    i = ""

    for le in dec:
        ind = key.index(le)
        i += chars[ind]
    print(i)

ins = input("welocm to nigma (enc/dec): ")
if ins == "enc" or ins == "e":
    enc()
elif ins == "dec" or ins == "d":
    dec()
else:
    print("plz enter valid input")

