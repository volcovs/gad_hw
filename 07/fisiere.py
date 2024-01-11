"""
r -> read only, este valoare default cu care vine funcia open, daca fisierul nu exista,
da eroare
w -> write, daca fisierul nu exista, il adaugam, daca exista informatie in fisiere, e suprascrisa
a -> scriere, daca exista info, scrie in continuare
r* -> sciere, citire, eroare daca nu exista deja fisierul
"""
import csv

file = open('data.txt')
