'''number = int(input("Введите число: "))
for i in range(1,number+1):
    if i % 3 == 0:
        print(i," делится на 3")'''

'''numbers = [13, 10, -5, 25, -30]
count = 0
sum = 0
for i in numbers:
    if i > 0:
        count += 1
        sum += i
if count > 0:
    total = sum / count
    print("Arithmetical mean:",total)'''

'''size=int(input('Insert the width of the Christmas tree:'))
branch=0
while branch!=2:
    num=(2*size)
    for i in range (0,size):
        for j in range (0,num):
            print(end=' ')
        num-=1
        for j in range (0,i+1):
            print('*',end=' ')
        print(' ')
    branch+=1'''

'''size = int(input("Enter the size of butterfly: "))
for i in range(1, size + 1):
    for j in range(1, 2 * size + 1):
        if j <= i or j > 2 * size - i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for i in range(size, 0, -1):
    for j in range(1, 2 * size + 1):
        if j <= i or j > 2 * size - i:
            print("*", end="")
        else:
            print(" ", end="")
    print()'''

'''white = "██"
black = "  "
figura =  ' '

for i in range(8):
    for j in range(8):

        if (i + j) % 2 == 0:
            print(white, end="")
        else:
            print(black, end="")
    print()'''

arr = [1,55,88,99,66]
for i in range(0, len(arr) - 1):
    for j in range(len(arr) - 1):
        if (arr[j] > arr[j + 1]):
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

    print(arr)
