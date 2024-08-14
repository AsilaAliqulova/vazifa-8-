from os import system
system('cls')

lst = [-1,2,3,-1,-2,6,7,9,6]

for i in range(len(lst)-1):
    if lst[i] > 0:
        if lst[i+1] - lst[i] == 1:
            print(f" {lst[i]}, {lst[i+1]}")
    if lst[i] < 0:
        if lst[i+1] - lst[i] == -1:
            print(f" {lst[i]}, {lst[i+1]}") 