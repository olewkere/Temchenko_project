a = 16
b = 63
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

import math

def gaus_func(x, m, s):
    gaus = (1 / (s * math.sqrt(2 * math.pi))) * (math.e**(-((x - m)**2) / (2 * s**2)))
    return gaus

x = 16
m = 63
s = 23
result1 = gaus_func(x, m, s)
print(result1)

john = 3
mary = 5
adam = 6
total_apples = john+mary+adam
print("\nJohn has", john, "apples, Mary has", mary, "apples, Adam has", adam, "apples.\nTotal apples:", total_apples, "\n")

kilometers = 12.25
miles = 7.38
miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61
print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

x = [0, 1, -1]
for x in x:
    y = 3 * x**3 - 2 * x**2 + 3 * x - 1
    print(f"For x = {x}, y = {y}")

# this program computes the number of seconds in a given number of hours
hours = 2
seconds = 3600
print("Hours: ", hours)
print("Seconds in Hours: ", hours * seconds)
print("Goodbye")

a = float(input("Enter a float value for 'a': "))
b = float(input("Enter a float value for 'b': "))
add = a + b
print("Addition result:", add)
sub = a - b
print("Subtraction result:", sub)
multi = a * b
print("Multiplication result:", multi)
if b != 0:
    div = a / b
    print("Division result:", div)
else:
    print("Division by zero is not allowed!")

print("\nThat's all, folks!")

x = float(input("\nEnter a float value for 'x': "))
if x != 0:
    y = 1 / (x + (1 / (x + (1 / (x + (1 / (x + 1/x)))))))
    print("Result:", y)
else:
    print("X can't be a zero!")

hour = int(input("\nStarting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
end_hour = (hour + (mins + dura) // 60) % 24
end_mins = (mins + dura) % 60
print(f"End time: {end_hour:02d}:{end_mins:02d}")
