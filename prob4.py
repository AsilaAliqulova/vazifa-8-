from os import system
system('cls')

right_lst = [
            '6','7','8','9','0','y','u','i','o','p',
            'h','j','k','l','n','m',',','.','/',"'",';',
            ']','[','=','-'
            ]

left_lst = [
            '1','2','3','4','5','q','w','e','r','t',
            'a','s','d','f','g','z','x','c','c','v','b'
            ]

count1 = 0
count2 = 0

gapcha  =  input("gap yozing: ")

for i in range(len(gapcha)):
    if gapcha[i] in right_lst:
        count1 += 1

    if gapcha[i] in left_lst:
        count2 += 1

print(f"o'ng qo'lda {count1}ta belgi yozilgan, chap qo'lda {count2}ta belgi yozilgan ")
