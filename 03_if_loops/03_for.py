# for-ul in python e de obicei folosit in forma forEach


lista = [100, 200, 300]
# for i in lista:
#     print(i)

# for-ul clasic
# for index, value in enumerate(lista):
#    print(index, value)

# range -> inceput, final+1, pas
# for index in range(1, 5, 3):
#    print(index)

# valorile se pot repeta, cheile trebuie sa fie unice
my_dict = {
    "key1": 1,
    "key2": 2,
    "key3": 1
}

# iterarea unui dictionar
# for i in my_dict.keys():
# echivalent cu:
# for i in my_dict:
#    print(i)

# se poate itera si pe tuple cheie, valoare
for i, v in my_dict.items():
    print(i, v)


