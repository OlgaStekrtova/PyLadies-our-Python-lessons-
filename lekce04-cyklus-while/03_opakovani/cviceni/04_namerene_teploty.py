# Cvičení 4 – Opakování
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadává naměřené teploty. Po každé se zeptej
#    "Další? (ano/ne) ". Až odpoví "ne", vypiš nejvyšší teplotu.


nejvyssi = int(input("Zadej teplotu: "))
while True:
    dalsi = input("Další? (ano/ne) ")
    if dalsi == "ne":
        break
    teplota = int(input("Zadej teplotu: "))
    if teplota > nejvyssi:
        nejvyssi = teplota

print("Nejvyšší teplota byla", nejvyssi)
