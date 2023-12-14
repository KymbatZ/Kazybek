'''x = int(input("Введите число:"))
if x > 0:
    print("Положительное число")
elif x == 0:
    print("Чисдо является нулём")
else:
    print("Отрицательное число")'''

'''year = int(input('Введите год: '))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
     print(f'{year} Високосный')
else:
     print(f'{year} Не високосный')'''

age = int(input('Insert your age: '))
health = True
if age >= 18 and age <= 45 and health == True:
    print('Yes')
else:
    print('No')
