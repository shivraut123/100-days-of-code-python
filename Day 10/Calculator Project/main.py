import art
print(art.logo)
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 -n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
continue_working = True
while continue_working:

    # print(operations["*"](2,2))
    n1 = float(input("Type the first no:\n"))
    for symbol in operations:
        print(symbol)
    operator = input("Type a mathematical operator\n ")
    n2 = float(input("Type the second no: \n"))
    answer = operations[operator](n1, n2)
    print(f"{n1} {operator} {n2} = {answer}")
    choice = input(f"Type yes or no to continue calculating\n").lower()
    if choice == "yes":
        continue_working = True
    else:
        continue_working = False
