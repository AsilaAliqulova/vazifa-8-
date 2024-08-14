from os import system
system ('cls')

def bellashuv(dic):
    maks = max(dic.values())
    print(maks)
    for key, value in dic.items():

        if value == maks:
            print(key)
    



royxat = {
    "Anvar": 1,
    "Lobar": 1,
    "Asror": 0,
    "Vali": 1,
    "Surayyo": 0,
    "Baxtiyor": 1
}
bellashuv(royxat)