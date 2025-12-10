print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
bill = 0
if size == "S":
    bill= 15
    print(f"Small Pizza:${bill}")
elif size == "M":
    bill = 20
    print(f"Medium Pizza: ${bill}")
elif size == "L":
    bill = 25
    print(f"Large Pizza: ${bill}")

if pepperoni == "Y":
    if size == "S":
        bill +=2
        print(f"with extra pepperoni:$2")
    else:
        bill +=3
        print(f"with extra pepperoni: $3")

if extra_cheese == "Y":
    bill +=1
    print(f"With extra Cheese: $1")
print("_________________________________________________")

print(f"Your final bill is ${bill}\n")
print("Thank You Shopping With Us. Enjoy Your Meal🍕")






