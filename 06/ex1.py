# print("mesaj")
# nr1 = input("Introdu numar")

# def my_function():
# pass

# def suma(c:int, a=2, b=5) -> (int, int):
#   return a+b+c, a-b-c

# suma_1, diferenta_1 = suma(c=10, b=4)
# print(f"Suma este: {suma_1} si diferenta {diferenta_1}")

def suma(a, b, *args, **kwargs):
    """
    :param a: primul parametru
    :param b: al doilea parametru
    :param args:
    :param kwargs:
    :return:
    """
    # print(type(args)) -> tuple
    # print(type(kwargs)) -> dict

    total = a + b
    for i in args:
        total += i
    for j in kwargs.values():
        total += j
    return total

suma_1 = suma(1, 2, 3, 4, 5, d=7, e=8)
print(suma_1)
