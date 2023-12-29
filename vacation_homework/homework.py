# Pe siteul https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-10-decembrie-ora-13-00-2/
# sunt trecute numarul de date raportate la nivel de judet pe ziua respectiva.

# URLul utilizat este furnizat pentru data de 10 decembrie 2023, deci
# requesturile se pot automatiza. In cazul in care nu se gasesc date
# la requestul dorit intr-o zi (mai exista si exceptii in care urlul
# este format altfel la sfarsit) se vor trece de mana acele url-uri.
# Se doreste realizarea unui tabel comun pe judete pentru zilele de
# 10.12, 11.12, 12.12, 13.12, 014.012.

import requests as requests
from bs4 import BeautifulSoup
import pandas as pd

index_list = list(range(1, 43))
index_list.append('Total')

dictionar = {}

# obtinerea asincrona a paginii cu statistici
for i in range(0, 5):
    r = requests.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-1" + str(i) + "-decembrie-ora-13-00-2/")
    link = BeautifulSoup(r.text, 'html.parser')

    title = link.find_all('div', attrs={'class': 'inside-article'})
    judete = []
    numar_cazuri = []

    if title:
        tables = title[0].find_all('table')
        # iterare pe continutul tabelului cu statistici pe judet
        for index, tr_index in enumerate(tables[0].find_all('tr')):
            if index == 0:
                # numele coloanelor -> nu intereseaza
                pass
            elif index < 43:
                for index_td, td_value in enumerate(tr_index.find_all('td')):
                    # avem nevoie de index pentru a distinge intre coloana de data si restul coloanelor din tabel
                    if index_td == 1:
                        # numele judetului
                        judete.append(td_value.get_text())
                    elif index_td == 2:
                        # nr. de cazuri confirmate (total)
                        numar_cazuri.append(
                            float(td_value.get_text().strip().replace(',', '.')) if td_value.get_text().strip() != '' else '')

        judete.append('')
        numar_cazuri.append(sum(numar_cazuri))
        if len(judete) > 0:
            dictionar['Judet'] = judete
        if len(numar_cazuri) > 0:
                dictionar['1' + str(i) + '.12'] = numar_cazuri

df = pd.DataFrame(dictionar, index=index_list)
df.index.name = 'NR. CRT'
print(df)
df.to_csv('hw.csv')
