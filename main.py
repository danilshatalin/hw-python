# Задача 34

def counter(phrase:str) -> int:
    voewls = 'аиеёоуыэюя'
    num = 0
    for l in phrase:
        if l in voewls:
            num = num + 1
    return num

def parse_poem(poem: str) -> str:
    num_phrase = poem.lower().split()
    num_l = counter(poem[0])
    for p in num_phrase[1:]:
        if num_l != counter(p):
            return "Пам парам"
    return "Парам пам-пам"


# Задача 36

def print_operation_table(operation,num_rows,num_colums):
    for i in range(1,num_rows):
        k = ""
        for j in range(1,num_colums):
            k = k + operation(i,j) + " "
        print(k)
 print_operation_table((lambda x,y: str(x*y)),7,7)
