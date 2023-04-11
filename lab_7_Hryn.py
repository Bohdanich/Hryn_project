numbers = (5, 10, 3, 11, 4, 6, 9)
result = []
while True:
    try:
        n = int(input("Enter the number n:"))
        for num in numbers:
            if num < n:
                result.append(num)
        print(result)
        break
    except:
        print("Enter correct number!")


# task 2

tuple = ("occasion", "knowledge", "scar")

result = ", ".join(tuple)

print(result)


# task 3

library = {
    "The Lion, the Witch and the Wardrobe": {
        "Author": "C. S. Lewis",
        "First published": "1950",
        "Pages": "172"
    },
    "The Da Vinci Code": {
        "Author": "Dan Brown",
        "First published": "2003",
        "Pages": "689"
    },
    "Black Beauty": {
        "Author": "Anna Sewell",
        "First published": "1877",
        "Pages": "255"
    }
}

book = input("Enter book's title: ")

if book in library:
    print("Author:", library[book]["Author"])
    print("First published:", library[book]["First published"])
    print("Pages:", library[book]["Pages"])
else:
    print("This book is not in the library.")

# task 4

while True:
    students = {
        'Гринь': ('Богдан', 2002, 'Інформатика'),
        'Грицюк': ('Вадим', 2001, 'Математика'),
        'Мєдова': ('Ірина', 2003, 'Історія')
    }

    student_name = input('Введіть прізвище студента: ')

    if student_name in students:
        # якщо студент існує, виводимо його дані
        student_data = students[student_name]
        print(f'Студент: {student_data[0]} \nРік народження: {student_data[1]} \nФакультет: {student_data[2]}')
        break
    else:
        print('Студента з таким прізвищем не знайдено.')

# task 5


phone_book = {
    "Богдан": ["0982032155", "0975554142"],
    "Вадим": ["0662123635", "0984562812"],
    "Ірина": ["0972566622", "0992226666"]
}

def add_phone_number(name, number):
    if name in phone_book:
        phone_book[name].append(number)
    else:
        print("Такого контакта не існує")

# Додати новий номер телефону до списку номерів певного контакту
add_phone_number("Богдан", "0972115656")

# Вивести список номерів телефонів для всіх контактів
for name, numbers in phone_book.items():
    print(f"{name}: {', '.join(numbers)}")

