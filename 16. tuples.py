#tuple = collection which is ordered and unchangeable
#         use to group togather related data

student = ("Alfred",20,"male")

print(student.index("Alfred"))
print(student.count("male"))

for x in student:
    print(x)

if "Alfred" in student:
    print("Alfred is here")

