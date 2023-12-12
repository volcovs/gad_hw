import pandas as pd
import numpy as np

# din lista
lista = [10, 20, 30, 40, 50]
etichete = ['a', 'b', 'c', 'd', 'e']
# in partea stanga se pun indecsi
# serie = pd.Series(lista)
# alternativa pentru dictionar
serie = pd.Series(lista, index=etichete)
# alternativa pentru dictionar, cu specificarea in instructiune a etichetelor
# print(serie['a', 'c', 'd'])

# din vector de valori
# array_date = np.array(lista)
# serie = pd.Series(array_date)

# din dictionar
# dict_date = {'a':10, 'b':20, 'c':30, 'd':40, 'e':50}
# serie = pd.Series(dict_date)
# in partea stanga sunt puse cheile, nu indecsi
# print(serie)

# declararea unui data frame
data = {'Nume': ['Ana', 'Bogdan', 'Cristina'],
        'Varsta': [25, 30, 22],
        'Salariu': [50000, 60000, 450000]}

df = pd.DataFrame(data)
# adaugarea unei coloane similare cu introducerea unui set cheie-valoare intr-un dictionar
df['Experienta'] = [2, 5, 1]
# print(df)
# etichetele nu mai sunt indecsi, ci numele persoanei
df.set_index('Nume', inplace=True)
# metoda loc permite accesarea unei linii din DataFrame
print(df.loc['Bogdan'])

# df.to_csv('date.csv')