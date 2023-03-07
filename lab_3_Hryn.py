import math

sigma = 1.5
x = 3
m = 4

y = (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(- ((x - m) ** 2) / (2 * sigma ** 2))

print(y, "\n")

john = 3
mary = 5
adam = 6
print(john, ",", mary, ",", adam, "\n")

totalApple = john + mary + adam
print(totalApple, "\n")
print("Загальна кількість яблук:", totalApple, "\n")

kilometers = 12.25
miles = 7.38

print(miles, "miles is", round(miles * 1.61, 2), "kilometers", "\n")
print(kilometers, "kilometers is", round(kilometers / 1.61, 2), "miles", "\n")

x = float(input("Введіть х: "))

y = 3 * x ** 3 - 2 * x ** 2 + 3 ** x - 1

print(y, "\n")

# this program computes the number of seconds in a given number of hours

a = 2 # number of hours
seconds = 3600 # number of seconds in 1 hour

print("Hours:", a) #printing the number of hours
print("Seconds in Hours:", a * seconds) # printing the number of seconds in a given number of hours
print("Goodbye\n")
#this is the end of the program that computes the number of seconds in 2 hour

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))

print("Результат додавання a та b:", round(a + b, 2))
print("Результат віднімання a та b:", round(a - b, 2))
print("Результат множення a на b:", round(a * b, 2))
print("Результат ділення a на b:", round(a / b, 2),"\n")

x = float(input("Enter value for x:"))

a = x + 1 / x
a = x + 1 / a
a = x + 1 / a
a = x + 1 / a
y = 1 / a

print("y =", y,"\n")

hour = int(input("Starting time (hours):"))
mins = int(input("Starting time (minutes):"))
dura = int(input("Event duration (minutes):"))

new_mins = (mins + dura) % 60
dura_hour = (mins + dura) // 60
new_hour = (dura_hour + hour + 24) % 24
print(str(new_hour) + ":" + str(new_mins))









