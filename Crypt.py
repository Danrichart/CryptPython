import random

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "XPMGTDHLYONZBWEARKJUFSCIQV"


def encode(no_encode):
    encoding = no_encode.upper()
    encoded = ""
    for x in range(len(encoding)):
        match = alpha.find(encoding[x])
        if match != -1:
            encoded = encoded + key[match]
        else:
            encoded = encoded + encoding[x]
    return encoded


def decode(no_decode):
    decoding = no_decode.upper()
    decoded = ""
    for x in range(len(decoding)):
        match = key.find(decoding[x])
        if match != -1:
            decoded = decoded + alpha[match]
        else:
            decoded = decoded + decoding[x]
    return decoded



def ran_key():
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        global key
        new_key = ""
        ran = 0
        for x in range(0, 26):
            ran = random.randrange(0, 26)
            while new_key.find(alphabet[ran]) != -1:
                ran = random.randrange(0,26)
                
            new_key = new_key + alphabet[ran]
            key = new_key
        return 

def menu():
    option = raw_input("\nSECRET DECODED MENU\n\n0)Quit \n1)Encocde \n2)Decode \n3)Random\n \nWhat do you want to do? ")
    return option
    
def main():
  keepGoing = True
  while keepGoing:
    response = menu()
    if response == "1":
      plain = raw_input("text to be encoded: ")
      print encode(plain)
    elif response == "2":
      coded = raw_input("code to be decyphered: ")
      print decode(coded)
    elif response == "3":
      ran_key()
      print "You randomized the key"
    elif response == "0":
      print "Thanks for doing secret spy stuff with me."
      keepGoing = False
    else:
      print "I don't know what you want to do..."

main()
