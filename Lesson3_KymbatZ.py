'''a = int(input("Введите оценку:"))
b = int(input("Введите оценку:"))
c = int(input("Введите оценку:"))
print("Среднее значение:", (a+b+c)/3)'''

'''your_name = input("Введите своё имя:")
print(f"Добро пожаловать,{your_name}!")'''

literature_a = int(input('Введите оценку по литературе:'))
literature_b = int(input('Введите оценку по литературе:'))
literature_c = int(input('Введите оценку по литературе:'))
literature_avg = (literature_a+literature_b+literature_c)//3
math_a = int(input('Введите оценку по математике:'))
math_b = int(input('Введите оценку по математике:'))
math_c = int(input('Введите оценку по математике:'))
math_avg = (math_a+math_b+math_c)//3
biology_a = int(input('Введите оценку по биологии:'))
biology_b = int(input('Введите оценку по биологии:'))
biology_c = int(input('Введите оценку по биологии:'))
biology_avg = (biology_a+biology_b+biology_c)//3
if literature_avg > math_avg and biology_avg:
    print(f'Предмет литература имеет высшее среднее значение:{literature_avg}')
elif math_avg > literature_avg and biology_avg:
    print(f'Предмет математика имеет высшее среднее значение:{math_avg}')
elif biology_avg > literature_avg and math_avg:
    print(f'Предмет биология имеет высшее среднее значение:{biology_avg}')

'''last_name = input("Введите фамилию: ")
first_name = input("Введите имя: ")
birth_date = input("Введите дату рождения(день,месяц,год): ")
permanent_address = input("Введите место проживания: ")
card = (f'{last_name} {first_name}
{birth_date}
{permanent_address}')'''
