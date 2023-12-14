from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

option = webdriver.ChromeOptions()
option.add_argument('start-maximized')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
driver.get("https://www.bnr.ro/files/xml/nbrfxrates2022.htm")


table = driver.find_element(by=By.XPATH, value='//*[@id="Data_table"]')
lista = table.text.split('\n')
# lista cu toate datele din tabel
# print(lista)

header_len = driver.find_element(by=By.XPATH, value='//*[@id="Data_table"]/table/thead/tr')
header = header_len.text.split('\n')
# print(header)

dictionar = {i: [] for i in header}
# print(dictionar)

# va adauga in lista fiecarei valute, fiecare valoare corespunzatoare unei date
for j in range(0, len(header)):
    for i in range(len(header) + j, len(lista), len(header)):
        # parcurgem fiecare coloana din lista cu pasul = cate coloane exista
        dictionar[header[j]].append(lista[i])

print(dictionar)
df = pd.DataFrame(dictionar)
df.to_csv("bnr_all_data.csv")


