# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()
#
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# writing file
# with open("my_file.txt", "w") as file:
#     file.write("Hello World")

# /Users/shivraut/Desktop/my_file.txt


with open("/Users/shivraut/Desktop/my_file.txt") as file:
    # file.write("My name is Shiv Kumar Raut")
    content = file.read()
    print(content)