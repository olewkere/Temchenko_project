def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
test_data = [1900, 2000, 2016, 1987, 2003]
test_results = [False, True, True, False, True]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "-> ", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

print("\n")

def days_in_month(year, month):
    month_lengths = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year):
        month_lengths[2] = 29
    if month < 1 or month > 12:
        return None
    return month_lengths[month]
test_years = [1900, 2000, 2016, 1987, 2003]
test_months = [2, 2, 1, 11, 9]
test_results = [28, 29, 31, 30, 31]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "-> ", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

print("\n")

def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    month_lengths = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year):
        month_lengths[2] = 29
    if month < 1 or month > 12:
        return None
    return month_lengths[month]

def day_of_year(year, month, day):
    month_lengths = days_in_month(year, month)
    if month_lengths is None or day < 1 or day > month_lengths:
        return None

    day_count = day
    for i in range(1, month):
        day_count += days_in_month(year, i)

    return day_count

print(day_of_year(2000, 12, 31))
print(day_of_year(2023, 2, 29))
print(day_of_year(2032, 2, 29))

print("\n")

def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True
for i in range(1, 21):
    if is_prime(i):
        print(i, end=" ")
print()

print("\n")

def liters_100km_to_miles_gallon(liters):
    conversion_factor = 235.214583
    miles_per_gallon = conversion_factor / liters
    return miles_per_gallon

def miles_gallon_to_liters_100km(miles):
    conversion_factor = 235.214583
    liters_per_100km = conversion_factor / miles
    return liters_per_100km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

print("\n")

def is_a_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

print(is_a_triangle(3, 4, 5))
print(is_a_triangle(1, 2, 3))
print(is_a_triangle(5, 5, 5))

print("\n")

def is_a_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

def is_a_right_triangle(a, b, c):
    if is_a_triangle(a, b, c):
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return True
        else:
            return False
    else:
        return False

print(is_a_right_triangle(3, 4, 5))
print(is_a_right_triangle(1, 2, 3))
print(is_a_right_triangle(5, 5, 5))
