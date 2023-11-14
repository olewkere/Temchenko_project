
# def mysplit(string):
#     string = string.lstrip() # метод strip() не змінює об'єкт, а створює копію!

#     list_split = []

#     if string.isspace() or string == "": # якщо рядок пустий, або з одних пробілів
#         return list_split

#     if string.find(' ') == -1: # якщо з одного слова
#         list_split.append(string)
#         return list_split

#     fnd_1 = 0
#     fnd_2 = string.find(' ')

#     while fnd_2 != -1:
#         list_split.append(string[fnd_1:fnd_2])
#         fnd_1 = fnd_2
#         fnd_2 = string.find(' ', fnd_2 + 1)

#     return list_split

# ІІ варіант (красивий, але не факт, що оптимальний)

def mysplit(string):
    list_split = []
    word = ""
    for char in string:
        if char == " ":
            if word:
                list_split.append(word)
            word = ""
        else:
            word += char
    if word:
        list_split.append(word)
    return list_split


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

# number_input = input('Введіть ціле число: ')
# number_list = [str(i) for i in range(0, 10)]
number_dict = {'1' : ('  #', '  #', '  #', '  #', '  #'),
               '2' : ('###', '  #', '###', '#  ', '###'),
               '3' : ('###', '  #', '###', '  #', '###'),
               '4' : ('# #', '# #', '###', '  #', '  #'),
               '5' : ('###', '#  ', '###', '  #', '###'),
               '6' : ('###', '#  ', '###', '# #', '###'),
               '7' : ('###', '  #', '  #', '  #', '  #'),
               '8' : ('###', '# #', '###', '# #', '###'),
               '9' : ('###', '# #', '###', '  #', '###'),
               '0' : ('###', '# #', '# #', '# #', '###')
               }
def display_number(num):
    if num < 0:
        print("Число має бути невід'ємним.")
        return

    num_str = str(num)

    for level in range(5):
        for simbol in num_str:
            print(number_dict[simbol][level], end=' ')
        print()

display_number(12345)

# Caesar cipher.
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)

# Caesar cipher - decrypting a message.
cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)

def caesar_cipher(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()
            code = ord(char) + shift
            if code > ord('Z'):
                code -= 26
            encrypted_text += chr(code) if is_upper else chr(code).lower()
        else:
            encrypted_text += char
    return encrypted_text

def get_valid_shift():
    while True:
        try:
            shift = int(input('Enter the shift value (1-25): '))
            if 1 <= shift <= 25:
                return shift
            else:
                print('Shift value must be between 1 and 25.')
        except ValueError:
            print('Please enter a valid integer.')

if __name__ == "__main__":
    cipher_text = input('Enter the text to encrypt: ')
    shift_value = get_valid_shift()

    encrypted_text = caesar_cipher(cipher_text, shift_value)

    print('Encrypted Text:', encrypted_text)
