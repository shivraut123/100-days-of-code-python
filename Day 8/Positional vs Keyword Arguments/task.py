# # Functions with input
#
# def greet_with_name(name,location):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#     print(f"What is it like in {location}")

# greet_with_name("Shiv","Nepal")
#
#
#
# def greet_with(name,location):
#     print(f"Hello, {name}")
#     print(f"How's in {location}")
#
# greet_with(location="Nepal", name="Shiv")

##################################Love Calculator ######################################################################
def calculate_love_score():
    print("Welcome to The LOVE Calculator! ❤️")

    #Get user input:
    name1 =input("What is your name: ")
    name2 = input("What is their name: ")
    combined = (name1 + name2).lower()

    # count no of times TRUE occurs
    t = combined.count("t")
    r = combined.count("r")
    u = combined.count("u")
    e = combined.count("e")

    true_total = t + r + u + e

    # count no of times LOVE occurs
    l = combined.count("l")
    o = combined.count("o")
    v = combined.count("v")
    e1 = combined.count("e")

    love_total = l + o + v + e1

    love_score = int(str(true_total) + str(love_total))

    print(f"Your love score is: {love_score}")
    if love_score < 10 or love_score > 90:
        print("🔥 Wow! You go together like coke and mentos!")
    elif 40 <= love_score <= 50:
        print("💖 You are alright together!")
    else:
        print("😊 You two have potential!")
calculate_love_score()
