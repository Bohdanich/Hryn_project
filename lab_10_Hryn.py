def check_word(word, text):
    index = -1
    for letter in word:
        index = text.find(letter, index + 1)
        if index == -1:
            return False
    return True

word = input("Введіть слово: ")
text = input("Введіть комбінацію символів: ")

if check_word(word, text):
    print("Yes")
else:
    print("No")


# Task 2

while True:
    date = input("Введіть дату народження у форматі YYYYMMDD:")
    try:
        while True:
            sum = 0
            for simbol in date:
                sum += int(simbol)

            date = str(sum)

            if len(date) == 1:
                break
        break
    except ValueError:
        print("Формат дати неправильний! Спробуйте знову.")

print(sum)