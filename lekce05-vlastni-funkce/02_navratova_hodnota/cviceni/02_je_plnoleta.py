# Cvičení 2 – Návratová hodnota
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci je_plnoleta(vek), která vrátí True, nebo False.
#    Zeptej se uživatele na věk a podle výsledku vypiš
#    "Můžeš dál." nebo "Ještě ne.".



def je_plnoleta(vek):
    if vek > 18:
        return True
    else:
        return False
    
vek = int(input("Kolik ti je?"))
vysledek = je_plnoleta(vek)

if vysledek == True:
    print("Next")
else:
    print("No")



def je_plnotela(vek): vek >= 18 ? true : false
vek = int(input("Kolik ti jest? \r\n")
je_plnotela(vek) == true ? print(''next") : print("go")