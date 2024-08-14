from os import system

system('cls')


def tartiblash (lst_items,son):
    for item in lst_items:
        item['price'] = int(item['price'])

    lst_items = sorted(lst_items, key=lambda narx: narx['price'], reverse=1)

    if son > len (lst_items):
        print("maxsulot soni ko'p kiritildi")
    else:
        for i in range(son):
            print(lst_items[i])


son  = int (input("son kiriting:  "))

maxsulot = [
    {
        "name" : "bread",
        "price": "100"
    },
    {
       "name" : "wine",
        "price": "138" 
    },
    {
        "name" : "meat",
        "price": "15"
    },
    {
        "name" : "water",
        "price": "1"
    }
]

tartiblash(maxsulot,son)
