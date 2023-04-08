# Задача 1
num = int(input('Введите трехзначное число: '))
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

print(f'Сумма чисел равна {sum}')

# Задача 2
sum = int(input('Введите кол-во журавликов, которое сделали дети: '))

print(f'Петя сделал {sum // 6}, Катя сделала {round(sum // 1.5)}, Сережа сделал {sum //6}')

# Задача 3 
num = int(input('Введите номер билета: '))
num1 = num // 1000
num2 = num % 1000
sum1 = 0
sum2 = 0 

while num1 > 0:
    digit = num1 % 10
    sum1 = sum1 + digit
    num1 = num1 // 10

while num2 > 0:
    digit = num2 % 10
    sum2 = sum2 + digit
    num2 = num2 // 10

if num1 == num2:
    print('Yes')
else:
    print('No')
    
# Задача 4
n = int(input())
m = int(input())
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('Yes')
else:
    print('No')
