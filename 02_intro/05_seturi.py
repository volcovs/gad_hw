# my_set = {}
# initial, my_set este vazut ca dictionar

my_set = {1}
# la adaugarea cel putin a unui element => vazut ca set

print(my_set)
print(type(my_set))

lista = [1, 2, 3, 2]
# conversie explicita de la lista la set de valori
print(set(lista))

# metoda pentru a lua toate valorile unice din lista
print(list(set(lista)))
