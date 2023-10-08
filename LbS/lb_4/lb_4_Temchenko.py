a = int(input("Input a int number to 100 for false and 100 and more for true: "))
result = a >= 100
print(result)

num1 = float(input("\nNumber 1: "))
num2 = float(input("Number 2: "))
if num1 > num2:
    max = num1
else:
    max = num2
print("Max number:", max)

input_string = input("Input: ")
if input_string == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif input_string == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print(f"Spathiphyllum! Not {input_string}!")

income = float(input("Income: "))
if income <= 85528:
    tax = income * 0.18 - 556.02
else:
    tax = (income - 85528) * 0.32 + 14839.02
if tax < 0:
    tax = 0
round_tax = round(tax)
print("Tax is:", round_tax, "thalers")

secret_number = 777
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
user_number = int(input("Введіть ціле число: "))
while user_number != secret_number:
    print("Ха-ха! Ви застрягли у моїй петлі!")
    user_number = int(input("Спробуйте ще раз: "))
print(
"""
+===================================+
|  ██████████ ██████████ ██████████ |
| ░███░░░░███░███░░░░███░███░░░░███ | 
| ░░░    ███ ░░░    ███ ░░░    ███  |
|       ███        ███        ███   |
|      ███        ███        ███    |
|     ███        ███        ███     |
|    ███        ███        ███      |
|   ░░░        ░░░        ░░░       |
+===================================+

Молодець, магле! Тепер ти вільний.
""")

import time
for i in range(1, 6):
    print(i, "Mississippi")
    time.sleep(1)
print("Ready or not, here I come!")

while True:
    user_input = input("Word please: ")
    if user_input.lower() == "chupacabra":
        break
print(
"""
+===================================+
| ╔═╗┬ ┬┬ ┬┬ ┬┌─┐┌─┐┌─┐┌─┐┌┐ ┬─┐┌─┐ |
| ║  ├─┤│ │├─┤├─┘├─┤│  ├─┤├┴┐├┬┘├─┤ |
| ╚═╝┴ ┴└─┘┴ ┴┴  ┴ ┴└─┘┴ ┴└─┘┴└─┴ ┴ |          
+===================================+
You've successfully left the loop.
""")

user_word = input("Word please ").upper()
for letter in user_word:
    if letter in "AEIOU":
        continue
    print(letter)

blocks = int(input("How many blocks u would use: "))
height = 0
layer = 1
while layer <= blocks:
    height += 1
    blocks -= layer
    layer += 1
print(f"The height of the pyramid {height}")

c0 = int(input("Input natural number: "))
steps = 0
while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    steps += 1
    print(c0)
print(f"Steps: {steps}")
