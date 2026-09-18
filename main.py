name = input("What is your name? ")
print(name)

age = input("How old are you? ")
print(age)

color = input("What's your favorite color? ")
print(color)

if color.lower() == "blue":
    color_comment = "Blue is a calm and beautiful color!"
elif color.lower() == "red":
    color_comment = "Red is a bold and energetic color!"
elif color.lower() == "green":
    color_comment = "Green is a fresh and relaxing color!"
else:
    color_comment = f"{color} is a great choice!"

print("Hello", name, "you are", age, "years old and your favorite color is", color)
print(color_comment)