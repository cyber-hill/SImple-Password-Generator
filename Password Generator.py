import random

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
while True:
    print("""
    {1} Գեներացնել գաղտնաբառ
    {2} Դուրս գալ
    """)
    menu=input("Գրեք ID! ")
    try:
        menu=int(menu)
        if menu == 1:
            number = input('Գաղտնաբառերի քանակը? ')
            length = input('Գաղտնաբառի երկարությունը? ')
            try:
                number = int(number)
                length = int(length)
                print("==========================================")
                for n in range(number):
                    password =''
                    for i in range(length):
                        password += random.choice(chars)
                    print(password)
                print("==========================================")
            except:
                print('Սխալ')
        elif menu == 2:
            break
        else:
            print('Սխալ մենյուի համար')

    except:
        print('Սխալ')
        continue