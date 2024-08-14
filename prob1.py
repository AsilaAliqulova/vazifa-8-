from os import system
from json import dumps

system ('cls')

son = int(input("son kiriting:  "))

son = str(son)

count = {}

for i in son:
    if i.isdigit():
        if i in count:
            count[i] += 1
        else:
            count[i] = 1


for i ,count in count.items():
    print(f"{i} -> {count}")

 
