print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?$ "))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
total_tip=tip/100
total=bill+ (bill * total_tip)
each_person= total/people
print(f"The bill was ${bill}, split between {people} people, with {tip}% tip")
final_amt=round(each_person,2)
print("The total amount each person should pay is: $",final_amt)


