"""WEBSCRAPING WITH BEAUTIFULSOUP4 PACKAGE"""

import requests as requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get("https://www.bnr.ro/Cursul-de-schimb--7372.aspx")
link = BeautifulSoup(r.text, 'html.parser')

title = link.find_all('div', attrs={'class': 'contentDiv'})
# print(len(title)) -> o lista, nu mai trebuie iteratii

dataset = []

for tr_index in title[0].find_all('table'):
    # iterare pe continutul tabelului
    # print(tr_index)
    for td_index in tr_index.find_all('tr'):
        # datele fara prima linie (care contine denumirile coloanelor)
        # print(td_index)
        td_list = []
        # lista intermediara trebuie golita la fiecare tr
        if td_index.find_all('th'):
            header = []
            for th_index in td_index.find_all('th'):
                header.append(th_index.get_text())
            dataset.append(header)
        for index, td_value in enumerate(td_index.find_all('td')):
            # avem nevoie de index pentru a distinge intre coloana de data si restul coloanelor din tabel
            if index == 0:
                # data
                td_list.append(td_value.get_text())
            else:
                # valoarea de conversie
                td_list.append(float(td_value.get_text().strip().replace(',', '.')) if td_value.get_text().strip() != '' else '')
        if len(td_list) > 0:
            dataset.append(td_list)



print(dataset)
df = pd.DataFrame(dataset)
print(df)
df.to_csv('bnr.csv')

