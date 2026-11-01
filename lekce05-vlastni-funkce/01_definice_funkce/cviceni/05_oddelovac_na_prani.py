# Cvičení 5 – Definice funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Předělej oddělovač z prvního úkolu tak, aby šlo při volání vybrat
#    znak a délku řádku. Když se nevybere nic, ať vypíše 30 hvězdiček
#    jako dřív.
#    Funkce musí zvládnout všechna tři volání:
#        oddelovac()
#        oddelovac("=")
#        oddelovac("-", 10)


def oddelovac (znak="*", delka_radku=30):
    print(znak * delka_radku)

for radek in range(3):
    oddelovac()
    oddelovac("=")
    oddelovac("-", 10)


znak = str(input("ur sign?"))
delka_radku = int(input("from 1 to 50?"))

def oddelovac (znak, delka_radku):
    print(znak * delka_radku)

oddelovac(znak, delka_radku) 

# for radek in range(3):
#     oddelovac()
#     oddelovac("=")
#     oddelovac("-", 10)
