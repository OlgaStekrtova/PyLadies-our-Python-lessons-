# Cvičení 3 – Definice funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci ohodnot_znamku, která má na vstupu celé číslo a vypíše:
#    1 → "Výborně", 2 → "Chvalitebně", 3 → "Dobře",
#    cokoliv jiného → "Ještě zabereme".
#    Zavolej ji v cyklu for pro známky 1 až 5.


def ohodnot_znamku(znamka):
    if znamka == 1:
        return "Výborně"
    elif znamka == 2:
        return "Chvalitebně"
    elif znamka == 3:
        return "Dobře"
    else:
        return "Ještě zabereme"


for znamka in range(1, 6):
    print(ohodnot_znamku(znamka))