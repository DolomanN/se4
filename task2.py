# Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность и содержащие максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]

from os import remove


list = [1, 5, 2, 3, 4, 6, 1, 7]

def excess(n):
    temp = n[0]
    for i in range(len(n)):
        if i >= temp:
            temp = i
        else:
            list.pop(n[i])
    return n

def remove_duplicate(m):
    new_list = []
    for i in m:
        if i not in new_list:
            new_list.append(i)
    return new_list

print (remove_duplicate(excess(list)))
