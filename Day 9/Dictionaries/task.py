# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

# person = {
#     "name":"Alice",
#     "age":25
# }
# # Add a new key value pair
# person["city"] = "London"
# #Change an existing value
# person["age"] = 26
# # Remove a key
# # del person["age"]
# person.get("name")
# # print(person)

# d = {
#     "x":1,
#     "y":2
# }
# d["z"] = 3
# print(d)
#
# # problem- 2
# scores = {"Alice": 90, "Bob": 85}
# scores["Bob"] = 95
# print(scores)
#
# # problem-3
# inventory = {"apples": 10, "bananas": 5}
# del inventory["bananas"]
# print(inventory)
#
# # problem-4
# student = {"name": "John", "grade": "A"}
# student["grade"] ="B"
# student["age"] = 17
# print(student)

#################### GRADING PROGRAM #################################

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {}

for student,score in student_scores.items():
    if 91 <= score <= 100:
        student_grades[student] = "Outstanding"
    elif 81 <= score <= 90:
        student_grades[student] = "Exceeds Expectations"
    elif 71 <= score <= 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)



