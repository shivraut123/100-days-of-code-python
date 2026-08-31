# try:
#     number = int(input("Enter a no"))
# except ValueError:
#     print("That's not a valid no")
#

"""Write a program that:

Asks the user for two numbers (convert both to int)
Divides the first by the second
Prints the result
Catches ValueError if they type something that isn't a number
Catches ZeroDivisionError if they enter 0 as the second number
"""
# try:
#     number1 = int(input("Enter a no"))
#     number2 = int(input("Enter another no"))
#     result = number1 / number2
# except ValueError:
#     print("That's not a valid no")
# except ZeroDivisionError:
#     print("can't divide by zero")
"""
3. Exercise 3: BMI Calculator
Ask the user for their weight in kg and height in meters.
Calculate: bmi = weight / (height ** 2)
Print the BMI, rounded to something reasonable.
Catch ValueError if either input isn't a valid number.
Catch ZeroDivisionError if height is 0.
"""
try:
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))
    if height > 3:
        raise ValueError("Height seems too high")

    bmi = round(weight / (height ** 2))
    print(bmi)
except ValueError as e:
    print(e)
    print("Invalid input. Try again.")

except ZeroDivisionError:
    print("Can't divide by zero. Try again.")

