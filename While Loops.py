# while loop = a statement that will execute it's block of code, as long as
#             as it's condition remains true

#if 1 == 1:
#    name = input("What is your name: ")
#    print("Hello, " + name)

name = ""

while len(name) == 0:
    name = input("What is your name: ")

print("Hello, " + name)

age = ""
while len(age) == 0:
    age = input("What is your age: ")

print("You are " + age + " years old")

