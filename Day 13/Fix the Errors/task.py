try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have entered invalid no. Enter numerical value like 20,17")
    age = int(input("How old are you ?"))
if age > 18:
    print(f"You can drive at age {age}.")
else:
    print(f"You are not eligible to drive at {age}")

