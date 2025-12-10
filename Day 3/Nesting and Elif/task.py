print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age= int(input("Enter your age: "))

# This is nested loop in if else statement.
    if age <=12:
        print("you need to pay $5. ")

        # This is elif statement inside nested loop
    elif age <= 18:
        print("You need to pay $7 ")

    else:
        print("You need to pay $12 ")

else:
    print("Sorry you have to grow taller before you can ride.")

# To calculate BMI
weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

if bmi < 18.5:
    print("Underweight")

elif bmi >= 18.5 and bmi < 25:
    print("Normal Weight")

elif bmi >= 25 and bmi < 30:
    print("overweight")

else:
    print("Invalid")
