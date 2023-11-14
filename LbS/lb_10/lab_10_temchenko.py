def are_characters_hidden(word, combination):
    for char in word:
        index = combination.find(char)
        if index == -1:
            return "No"
    return "Yes"
word_test_1 = "dog"
combination_test_1 = "vcxzxdsobywuefgasuybfd"
print(combination_test_1, are_characters_hidden(word_test_1, combination_test_1))
word_test_2 = "dog"
combination_test_2 = "vcxzxduybfdsobywuefaas"
print(combination_test_2, are_characters_hidden(word_test_2, combination_test_2))

def calculate_life_number(date):
    digits = ''.join(filter(str.isdigit, date))
    if len(digits) != 8:
        raise ValueError("Некоректний формат дати. Введіть дату у форматі РРРРММДД, РРРРДДММ або ММДДРРРР.")
    digit_sum = sum(int(d) for d in digits)
    while digit_sum > 9:
        digit_sum = sum(int(d) for d in str(digit_sum))
    return digit_sum
while True:
    try:
        date = input("Введіть дату народження у форматі РРРРММДД, РРРРДДММ або ММДДРРРР: ")
        life_number = calculate_life_number(date)
        print("Цифра життя для дати {}: {}".format(date, life_number))
        break
    except ValueError as e:
        print(str(e))

def get_integer_input(prompt, min_value, max_value):
    while True:
        try:
            user_input = int(input(prompt))
            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(f"Error: the value is not within permitted range ({min_value}..{max_value})")
        except ValueError:
            print("Error: wrong input. Please enter an integer.")
min_range = 1
max_range = 100
user_number = get_integer_input(f"Enter an integer between {min_range} and {max_range}: ", min_range, max_range)
print(f"You entered: {user_number}")
