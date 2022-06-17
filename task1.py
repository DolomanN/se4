import random
my_file = open("numbers.txt", "w")
list = []
for x in range(1, 10):
    list.append(random.randint(1, 100))
print(list)
list.sort()
my_file.write(str(list))
my_file.close()

my_file = open("numbers.txt", "r")
result = my_file.read()
print(result)
my_file.close()
