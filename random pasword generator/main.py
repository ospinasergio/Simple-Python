#Password Generator Project
import random
import string
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
mode=(input("Do you want easy or hard password,Press e or h\n"))
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pass_length= nr_letters+nr_numbers+nr_symbols
password=""
possibilities=["a","b","c"]
if(mode=="e"):
    for i in range(0,pass_length):
        if(nr_letters!=0):
            password+=str(random.choice(letters))
            nr_letters-=1
        elif (nr_symbols != 0):
            password += str(random.choice(symbols))
            nr_symbols -= 1
        elif (nr_numbers != 0):
            password += str(random.choice(numbers))
            nr_numbers -= 1
    print(password)





#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#HARD MODE
if(mode=="h"):
    for i in range(0,pass_length):
        if len(possibilities)!=0:
            selector=random.choice(possibilities)

        if(selector=="a"):
            if(nr_letters!=0):
                password+=str(random.choice(letters))
                nr_letters-=1
                if(nr_letters==0):
                    possibilities.remove("a")

        elif (selector =="b"):
            if (nr_symbols != 0):
                password += str(random.choice(symbols))
                nr_symbols -= 1
                if(nr_symbols==0):
                    possibilities.remove("b")

        elif (selector == "c"):
            if (nr_numbers != 0):
                password += str(random.choice(numbers))
                nr_numbers -= 1
                if(nr_numbers==0):
                    possibilities.remove("c")
    print(password)