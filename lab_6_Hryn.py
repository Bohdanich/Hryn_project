def is_year_leap(year):
    if year < 1582:
        print("Not  within the Gregorian calendar period.")
        return
    elif year % 4:
        return False
    elif year % 100:
        return True
    elif year % 400:
        return False
    else:
        return True


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
  yr = test_data[i]
  print(yr,"->",end="")
  result = is_year_leap(yr)
  if result == test_results[i]:
      print("OK")
  else:
      print("Failed")


# task 2

def days_in_month(year, month):
    if year > 1582 and month <= 12 and month > 0:
        if month == 2:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                return 29
            else:
                return 28
        elif month in [4, 6, 9, 11]:
            return 30
        else:
            return 31


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
  yr = test_years[i]
  mo = test_months[i]
  print(yr, mo, "->", end="")
  result = days_in_month(yr, mo)
  if result == test_results[i]:
      print("OK")
  else:
      print("Failed")

print(days_in_month(2000, 22))


# task 3

def day_of_year(year, month, day):
    if month < 1 or month > 12:
        return "Error: Month must be between 1 and 12"

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_month[1] = 29

    if day < 1 or day > days_in_month[month - 1]:
        return "Некоректні дані: неправильний день місяця"
        # Враховуємо високосні роки
    day_of_year = sum(days_in_month[:month - 1]) + day

    return day_of_year

print(day_of_year(2022, 2, 29))

# task 4
#
def is_prime(num):
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    return flag


for i in range(1, 20):
  if is_prime(i + 1):
          print(i + 1, end=" ")
print()


# task 5

def liters_100km_to_miles_gallon(liters):
    return 235.22 / liters

def miles_gallon_to_liters_100km(miles):
    return 235.22 / miles

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))


# task 6

def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

print(is_triangle(3, 4, 6))


#task 7
def is_right_triangle(a, b, c):
    if is_triangle(a, b, c):
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
            return True
        else:
            return False
    return False

print(is_triangle(3, 4, 2))


