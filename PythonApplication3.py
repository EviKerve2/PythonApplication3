
##2#########################################################################
def is_year_leap(year):
    if year%4 == 0:
            if year%400==0:
                print('True')
            elif year%100!=0:
                print('True')
            else:
                print('False')
    else:
            print('False')
year=input("Введите год:  ")
while True:
    if not year.isdigit():
        print("Ошибка ввода!")
        print("Используйте только целые числа.")
        year=input("Введите год:  ")
        continue
    else:
        break

year=int(year)
while True:
    if year==0:
        print("Используйте только целые числа.")
        year=input("Введите год:  ")
        continue
    else:
        break
year=int(year)
answer=is_year_leap(year)
print(answer)
       

#4
def season(month):

    if month == 12 or month < 3:
        return "Зима"
    elif month == 3 or month < 6:
        return "Весна"
    elif month == 6 or month < 9:
        return "Лето"
    else:
        return "Осень"

month = input("Введите месяц(число):")

while True:
    if not month.isdigit():
        print("Ошибка ввода!")
        print("Используйте только целые числа.")
        month = input("Введите месяц(число):")
        continue
    else:
        break

month = int(month)
while True:
    if month == 0:
        print("Такого месяца несуществует")
        print("Используйте только целые числа.")
        month = input("Введите месяц(число):")
        continue
    else:
        break

month = int(month)
answer = season(month)
print(answer)


#8###########################################################################
def xor_uncipher(string: str, key:str)->str:
    """Kodeeritud text dekodeeritakse
    """
    result=""
    temp=[]
    for i in range(len(string)):
        temp.append(string[i])
        for j in reserved(range(len(key))):
            temp[i]=chr(ord(key[j])^ord(temr[i]))
        result+=temp[i]
    return result

#7#########################################################################
def is_year_leap(year):

    if year % 400 == 0:
        return True

    if year % 4 == 0 and year % 100 != 0:
        return True

    return False

def date(day, month, year):
    day_in_month = {1: 31,
                    2: 29 if is_year_leap(year) else 28,
                    3: 31,
                    4: 30,
                    5: 31,
                    6: 30,
                    7: 31,
                    8: 31,
                    9: 30,
                    10: 31,
                    11: 30,
                    12: 31}

    if 1 <= month <= 12 and 1 <= day <= day_in_month[month]:
        return True
    return False
year = input("Введите год(число):")
month = input("Введите месяц(число):")
day = input("Введите день(число):")
while True:
    if not month.isdigit():
        print("Ошибка ввода!")
        print("Используйте только целые числа.")
        month = input("Введите месяц(число):")
        continue
    else:
        break

month = int(month)
while True:
    if month == 0:
        print("Такого месяца несуществует")
        print("Используйте только целые числа.")
        month = input("Введите месяц(число):")
        continue
    else:
        break

while True:
    if not day.isdigit():
        print("Ошибка ввода!")
        print("Используйте только целые числа.")
        day = input("Введите день(число):")
        continue
    else:
        break

day = int(day)
while True:
    if day == 0:
        print("Такого дня несуществует")
        print("Используйте только целые числа.")
        day = input("Введите день(число):")
        continue
    else:
        break

while True:
    if not year.isdigit():
        print("Ошибка ввода!")
        print("Используйте только целые числа.")
        year = input("Введите год(число):")
        continue
    else:
        break

year = int(year)
while True:
    if year == 0:
        print("Такого года несуществует")
        print("Используйте только целые числа.")
        year = input("Введите год(число):")
        continue
    else:
        break
answer=date(day, month, year)
print(answer)

#6#######################################################################
def is_prime(number):
  from math import*  
    # Все четные числа кроме 2 непростые
    if number % 2 == 0 and number != 2:
        return False
    # 0 и 1 не являются простыми
    if number == 0 or number == 1:
        return False
    # Перебираем числа от 3 до корня из введенного, шаг - 2
    for n in range(3, int(sqrt(number).real) + 1, 2):
        if number % n == 0:  # Если число делится нацело, то оно непростое
            return False
    return True  # Остальные числа простые

n = input('Введите число: ')
while True:
    if not n.isdigit():
        print("Ошибка ввода!")
        print("Используйте только целые числа.")
        n =input('Введите число: ')
        continue
    else:
        break

n = int(n)
while True:
    if n == 0:
        print("Такого года несуществует")
        print("Используйте только целые числа.")
        n =input('Введите число: ')
        continue
    else:
        break
answer=is_prime(n)
print(answer)


##1#########################################################################
def arithmetic (x, y, z):
    if z == "+" :
        return (x + y)
    elif z == "- ":
        return (x - y)
    elif z == "*":
        return (x * y)
    elif z == "/":
        return (x / y)
    else :
        return ("Invalid operation")
x = input("Введите первое число: ")
y = input("Введите второе чиcло: ")
z = input("Введите знак: ")
while True:
    if not x.isdigit():
        print("Ошибка ввода!")
        print("Используйте только целые числа.")
        x = input("Введите первое число: ")
        continue
    else:
        break

x = int(x)
while True:
    if x == 0:
        print("Такого года несуществует")
        print("Используйте только целые числа.")
        x = input("Введите первое число: ")
        continue
    else:
        break

while True:
    if not y.isdigit():
        print("Ошибка ввода!")
        print("Используйте только целые числа.")
        y = input("Введите первое число: ")
        continue
    else:
        break

y = int(y)
while True:
    if y == 0:
        print("Такого года несуществует")
        print("Используйте только целые числа.")
        y = input("Введите первое число: ")
        continue
    else:
        break

while True:
    if not z.isdigit():
        print("Ошибка ввода!")
        print("Используйте только целые числа.")
        z = input("Введите знак: ")
        continue
    else:
        break

z = int(z)
while True:
    if z == 0:
        print("Такого года несуществует")
        print("Используйте только целые числа.")
        z = input("Введите знак: ")
        continue
    else:
        break
answer=arithmetic (x, y, z)
print(answer)
