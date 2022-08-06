#tip, ktheje ne tkinter app. would look cool. ose thjesht app
print("Welcome to the tip calculator")

#amount of money
while True:
    try:
        bill=float(input("What was the total bill? $"))
        break                                         #if the bill is not a number,break is ignored and the loop goes directly to the except line
    except ValueError:
        print("Only numbers are accepted. Please try again!")

#tip percentage
while True:
    try:
        tip=int(input("What percentage tip would you like to give?"))
        break
    except ValueError:
        print("Only numbers are acceapted. Please try again!")

#split proccedure
while True:
    try:
        split=int(input("How many people to split the bill?"))
        break
    except ValueError:
        print("Only numbers are accepted. Please try again!")


tip_amt=bill*(tip/100)

bill_splited= round((bill+tip_amt)/split,2)

print(f"Each person should pay: ${bill_splited}")