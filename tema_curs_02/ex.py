a = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# ordonare crescatoare a listei in alta lista
b = a.copy()
b.sort()
print(b)

# ordonare descrescatoarea a listei in alta lista
c = a.copy()
c.sort(reverse=True)
print(c)

# doar elemente pare
print(b[1::2])

# doar elemente impare
print(b[::2])

# elemente multiple de 3
print(b[2::3])
