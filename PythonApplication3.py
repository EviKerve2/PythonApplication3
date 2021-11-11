print("Камень, ножницы, бумага")
name=input("Напиши своё имя ")
print(f"Привет {name}")
print("Давай сыграем?")
a=input("1 = Да, 2 = Нет => ")
if a==2:
    print("Давай начнём")
    print("Камень=>1, Ножницы=>2, Бумага=>3")
    Камень=1
    Ножницы=2
    Бумага=3
    c=""
    while type(c)!=int:
        try:
            c=int(input("Выбирай=> "))
        except:
            print("Выбери число 1,2 или 3")
    if c<=3 or c==3:
        if c==1:
            print("Вы выбрали камень")
        elif c==2:
            print("Вы выбрали ножницы")
        elif c==3:
            print("Вы выбрали бумагу")
    else:
        print("Такого варианта нет")
    from random import*
    a=randint(1,3)
    if a==1:
                print("Робот выбрал камень")
    elif a==2:
                print("Робот выбрал ножницы")
    elif a==3:
                print("Робот выбрал бумагу")
    e=0
    b=0
    if c==1 and a==1:
                    print("Ничья")
    elif c==1 and a==2:
                    print("Ты выиграл")
                    e+=1
    elif c==1 and a==3:
                    print("Робот выиграл")
                    b+=1
    elif c==2 and a==1:
                    print("Робот выиграл")
                    b+=1
    elif c==2 and a==2:
                    print("Ничья")
    elif c==2 and a==3:
                    print("Ты выиграл")
                    e+=1
    elif c==3 and a==1:
                    print("Ты выиграл")
                    e+=1
    elif c==3 and a==2:
                    print("Робот выиграл")
                    d+=1
    elif c==3 and a==3:
                    print("Ничья")
    else:
        print(f"Счёт {e} и {b}")
else:
    print("Ладно")
