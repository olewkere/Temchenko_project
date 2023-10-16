numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
n = int(input("Введіть число n: "))
result = [x for x in numbers if x < n]
print("Числа, які менші за", n, ":", result)

strings = ("\nBlablabla 1", "tratarap 2", "blumbulum 3\n")
result = ", ".join(strings)
print(result)

library = {
    "Том Сойєр": {"Автор": "Марк Твен", "Рік видання": 1876, "Кількість сторінок": 275},
    "Робін Гуд": {"Автор": "Вальтер Скотт", "Рік видання": 1883, "Кількість сторінок": 350},
    "Айвенго": {"Автор": "Вальтер Скотт", "Рік видання": 1819, "Кількість сторінок": 400},
}
book_title = input("Введіть назву книги: ")
if book_title in library:
    book_info = library[book_title]
    print(f"Інформація про книгу '{book_title}':")
    for key, value in book_info.items():
        print(f"{key}: {value}")
else:
    print(f"\nКнига '{book_title}' не знайдена в бібліотеці.")

students = {
    "Петренко": ("Іван", 20, "Інформатика"),
    "Коваль": ("Марія", 22, "Математика"),
    "Сидоренко": ("Олександр", 19, "Фізика"),
    "Мельник": ("Юлія", 23, "Хімія"),
    "Козлов": ("Дмитро", 18, "Економіка"),
    "Шевченко": ("Оксана", 25, "Психологія"),
    "Іванов": ("Андрій", 21, "Соціологія"),
    "Мороз": ("Ольга", 27, "Історія"),
    "Савченко": ("Максим", 24, "Біологія"),
    "Бондаренко": ("Наталія", 26, "Географія"),
    "Павленко": ("Олег", 20, "Філософія"),
    "Григоренко": ("Анна", 19, "Література"),
}
surname = input("\nВведіть прізвище студента: ")
if surname in students:
    name, age, specialty = students[surname]
    print(f"Прізвище: {surname}")
    print(f"Ім'я: {name}")
    print(f"Вік: {age} років")
    print(f"Спеціальність: {specialty}")
else:
    print("\nСтудента з таким прізвищем не знайдено.\n")

phonebook = {
    "Ольга": ["123-123-123", "231-231-231"],
    "Максим": ["777-777-777", "456-456-456", "111-222-333"],
    "Оксана": ["112-223-334", "445-556-667"],
    "Андрій": ["111-333-555", "222-444-666", "135-246-789"],
    "Іван": ["123-456-789", "987-654-321"],
    "Марія": ["157-359-468", "486-624-953"],
}
def add_phone_number(contact_name, new_phone_number):
    if contact_name in phonebook:
        phonebook[contact_name].append(new_phone_number)
    else:
        phonebook[contact_name] = [new_phone_number]
def display_phonebook():
    for contact, phone_numbers in phonebook.items():
        print(f"Контакт: {contact}")
        print(f"Номери телефонів: {', '.join(phone_numbers)}")
        print()
while True:
    contact_name = input("\nВведіть ім'я контакту (або 'вийти' для завершення): ")
    if contact_name.lower() == 'вийти':
        break
    phone_number = input("\nВведіть новий номер телефону: ")
    add_phone_number(contact_name, phone_number)
display_phonebook()

