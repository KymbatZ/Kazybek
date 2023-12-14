'''for i in range(0, 21, 2):
     print(i)'''

'''number = int(input("Введите число: "))
sum = 0
for i in range(1, number + 1):
     sum += i
     print(sum)'''

'''name = 'Python'
for i in name:
     print(i)'''

'''sum = 0
number = 1
while number<=100:
     sum += number
     number +=2
print ("сумма нечетных чисел:", sum)'''

'''for i in range(6):
    for j in range(1, i + 1):
        print('*', end='')
    print()'''

'''for i in range(1, 6):
     for j in range(0, 11):
         print(i, '*', j, '=', i * j)'''

num = int(input("Число: "))
if num <= 1:
    print(f"{num} не является простым числом")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
         if num % i == 0:
             is_prime = False
             break
    if is_prime:
        print(f"{num} является простым числом")
    else:
        print(f"{num} не является простым числом")
