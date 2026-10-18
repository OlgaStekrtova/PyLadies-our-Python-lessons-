# Cvičení 5 – For versus while
# Nejdřív rozhodni for/while a napiš si do komentáře proč, pak úlohu naprogramuj.

# Načítej od uživatele čísla tak dlouho, dokud nezadá záporné číslo.
#    Pak vypiš, kolik čísel stihl zadat.


pocet = 0
cislo = int(input("Your number is?"))
while cislo >= 0:
    pocet = pocet + 1
    cislo = int(input("Your number is?"))
print("Amount of ur numbers before negative ones", pocet)