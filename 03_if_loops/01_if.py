# exemplu utilizare operator ternar

salariu = 2
nivel_salariu = "Salariul este mic"

# if salariu > 4:
   # nivel_salariu = "Salariul este ok"
#print(nivel_salariu)

nivel_salariu = "Salariu este ok" if salariu > 4 else "Salariul este mic"
print(nivel_salariu)

salariu = 101
if salariu > 100 and (salariu_net := salariu - 30) and salariu_net > 70:
    nivel_salariu = "Salariu ok"
elif salariu <= 100 and (salariu_net := salariu - 20) and salariu_net < 60:
    nivel_salariu = "Salariu mic"

print(nivel_salariu)
