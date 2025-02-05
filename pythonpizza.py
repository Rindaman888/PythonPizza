print("Welcome to Python Pizza Deliveries!")
print("-----------------------------")
size = input("What size pizza do you want? S, M or L: ")

bill = 0
if size == 'S':
    bill = 15
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == 'Y':
        if size == 'S':
            bill += 2
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if extra_cheese == 'Y':
        bill +=1
elif size == 'M':
    bill = 20
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == 'Y':
        if size == 'M':
            bill += 3
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if extra_cheese == 'Y':
        bill +=1
elif size == 'L':
    bill +=25
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni == 'Y':
         if size == 'L':
            bill += 3
    extra_cheese = input("Do you want extra cheese? Y or N: ")
    if extra_cheese == 'Y':
        bill +=1
else:
    print("Please Enter the correct value.")
    
print("-----------------------------")
print(f"Your final bill is: ${bill}.")