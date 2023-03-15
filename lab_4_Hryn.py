# task 1
c = 0
while c < 3 :
    n = int(input("Enter the number:"))
    print(n >= 100)
    c += 1


# task 2
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
if a > b :
    larger = a
else:
    larger = b
print("Large number is:", larger)


# task 3
n = 0
while n < 3 :
    text = input("Enter \"Spathiphyllum\": ")
    if "Spathiphyllum" in text:
        print("Yes - Spathiphyllum is the best plant ever!")
    elif "spathiphyllum" in text:
        print("No, I want a big Spathiphyllum!")
    else:
        print("Spathiphyllum! Not", text, "!")
n += 1


# task 4
n = 0
while n < 4:
    income = float(input("Enter the annual income: "))

    if income <= 85528:
        tax = income * 0.18 - 556.02
    else:
        tax = 14839.02 + (income - 85528) * 0.32
    if tax <= 0:
        tax = 0.0

    tax = round(tax)
    print("The tax is:", tax, "thalers")
    n += 1


# task 5
n = 0
while n < 5:
    year = int(input("Enter year:"))

    if year < 1582:
        print("Not  within the Gregorian calendar period.")
    elif year % 4:
        print("Common year")
    elif year % 100:
        print("Leap year")
    elif year % 400:
        print("Common year")
    else:
        print("Leap year")
    n += 1


# task 6
secret_number = 777
num = int(input(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
"""))
n = 0
while secret_number != num:
    num = int(input("Ха-ха! Ви застрягли у моїй петлі! Спробуйте ще раз:"))
else:
    print("Молодець, магле! Тепер ти вільний")


# task 7
import time

for i in range(1, 6):
    print(i, "Mississippi")
    time.sleep(1)
print("Ready or not, here I come!")


# task 8
key = "chupacabra"
while True:
    text = input("Enter code word:")
    if text == key:
        break
print("You've successfully left the loop.")


# task 9
a = ["A", "E", "I", "O", "U"]
user_word = input("Enter the word:")
user_word = user_word.upper()
for letter in user_word:
    if letter in a:
        continue
    print(letter)


# task 10
word_without_vowels = ""
a = ["A", "E", "I", "O", "U"]
user_word = input("Enter the word:")
user_word = user_word.upper()
for letter in user_word:
    if letter in a:
        continue
    word_without_vowels += letter
print(word_without_vowels)


# task 11

for m in range(4):
    count = 0
    total = 0
    i = 1
    number = int(input("Введіть число: "))
    while total < number:
        count += 1
        total += i
        if total > number:
            count -= 1
            break
        i += 1
    print("Кількість ітерацій циклу: ", count)


# task 12
c0 = int(input("Enter the positive number:"))
count = 0
while c0 <= 0:
    c0 = int(input("Wrong number, enter correct number!"))
while c0 != 1:
    if c0 % 2 == 0:
        c0 /= 2
    else:
        c0 = 3 * c0 + 1
    count += 1
    print("c0:", round(c0))
print("Steps:", count)


