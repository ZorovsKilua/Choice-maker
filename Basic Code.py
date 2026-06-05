import random

n = int(input("How many things do you want to choose from? "))

things = []

for i in range(n):
    item = input(f"Enter the thing N°{i + 1}: ")
    things.append(item)

choice = random.choice(things)

print("\nYou should do/have:")
print(choice)
