#If Statement = a block of code that will execute if it's condition is true

age = int(input("How old are you: "))

if age == 100:
    print("Wow, you are century old!!")
elif age > 18:
    print("Wow, you are an Adult!")
elif age < 0:
    print("Wow, you haven't been born!")
else:
    print("Wow, you are a child!")
#Remember the order is very important !
