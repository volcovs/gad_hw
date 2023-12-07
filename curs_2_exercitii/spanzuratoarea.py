cuvant = 'onomatopee' # o _ o _ _ _ o _ e e
cuvant_de_ghicit = list(cuvant)
prima_litera = cuvant[0]
ultima_litera = cuvant[-1]

for i, value in enumerate(cuvant):
    if value != prima_litera and value != ultima_litera:
        cuvant_de_ghicit[i] = '_'

cuvant_de_ghicit = ' '.join(cuvant_de_ghicit)
print(cuvant_de_ghicit)
litere_incercate = set()

vieti = 7
while vieti > 0 and '_' in cuvant_de_ghicit:
    litera = input("Alege o litera: ").lower()
    if not litera.isalpha() or len(litera) > 1:
        # daca caracterul nu e o litera, se trece la urmatoarea iteratie din while
        print("Introduceti o litera!")
        continue
    else:
        print(litera)
        cuvant_de_ghicit = list(cuvant_de_ghicit)
        for i in cuvant_de_ghicit:
            if i == ' ':
                cuvant_de_ghicit.remove(' ')

        if litera in cuvant:
            for i, value in enumerate(cuvant):
                if value == litera:
                    cuvant_de_ghicit[i] = litera
        else:
            if litera not in litere_incercate:
                vieti = vieti - 1
            litere_incercate.add(litera)

        if vieti == 0:
            print("Ai pierdut!")
            print(f"Cuvantul era {cuvant}")
            break
        print(f'Mai ai {vieti} vieti!')

        if len(list(litere_incercate)) > 0:
            print(f"Literele incercate sunt: {','.join(litere_incercate)}")
        cuvant_de_ghicit = ' '.join(cuvant_de_ghicit)
        print(cuvant_de_ghicit)

if vieti > 0:
    print("Ai castigat!")
