def encription(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            new_pos = ord(char.lower()) + shift  # Визначаємо нову позицію літери в алфавіті
            # Замінюємо літеру на нову літеру за її новою позицією в алфавіті
            if char.isupper():
                encrypted_text += chr((new_pos - 97) % 26 + 65)
            else:
                encrypted_text += chr((new_pos - 97) % 26 + 97)
        else:
            # Залишаємо символ без змін
            encrypted_text += char
    return encrypted_text


text = input("Enter the text that you want to encrypt: ")
while True:
    try:
        shift = int(input("Enter the step (0-25): "))
        if shift < 0 or shift > 25:
            print("Shift should be between 0 and 25")
            continue
        break
    except ValueError:
        print("Shift should be a number. Please try again.")
encrypted_text = encription(text, shift)
print("Encrypted text: ", encrypted_text)
