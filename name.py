import random

print("Yo what's good! I'm going to try to guess your age.")
name = input("What's your name broski? ")

while True:
    age = random.randint(15, 30)
    answer = input(f"Is your age {age}? (y/n): ").lower()
    if answer == "y":
        print(f"{name} is {age} years old. IM A GENIUS")
        break
    else:
        print("Dang it I lost :(")
