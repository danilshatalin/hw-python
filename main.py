# Задача 16
import random
N = int(input())
X = int(input())
A = [random.randint(0,10) for x in range(N)]
count = 0
for i in A:
    if i == X:
        count += 1
print(count)


    
# Задача 18
import random
N = int(input())
X = int(input())
A = [random.randint(0,N) for x in range(N)]
t = X
r = 0
for i in A:
    if ((X - i)**2)**0.5 < t:
        r = i
        t = ((X - i)**2)**0.5
print(A)
print(r)

 
# Задача 20
D = {1:'AEIOULNSTR', 2: 'DG', 3:'BCMP', 4:'FHVWY', 5:'K', 8:'JX', 10:'QZ'}
r = 0
word = input().upper()

for i in word:
    for k in D.keys():
        if i in D[k]:
            r += k
print(r)
