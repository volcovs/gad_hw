list1 = [1, 5, 4, 6, 8, 11, 3]

def iterare(x):
    lista_noua = []
    for i in x:
        lista_noua.append(i*2)
    return lista_noua
# print(iterare(list1))


list_2 = map(lambda x: x * 2, list1)
print(list(list_2))


def suma(n):
    return n + n


numere = (1, 2, 3, 4)
numere_map = map(lambda x: x + x, numere)
print(list(numere_map))
