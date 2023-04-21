# Задача 26

def sqr(a,b):
    if b > 1:
        return a * sqr(a,b - 1)
    else:
        return a

print(sqr(2,8))


# Задача 28

def sum(a,b):
    if b > 0:
        return sum(a + 1,b - 1)
    else:
        return a
print(sum(0,0))
