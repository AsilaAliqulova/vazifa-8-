from os import system
system('cls')


son = input("son kiriting:  ")

count = 0

for i in range(len(son)):
    
    if son[i] == "0":
        count += 1
    else:
        break
    

print(f"0 -> {count} ta bor ekan!")
