# Cvičení 2 – Opakování
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá slovo. Spočítej, kolikrát se v něm objeví
#    písmeno "a", a výsledek vypiš.


amount = 0
word = input("Type your word: ")
for letter in word:
    if letter == "a":
        amount = amount + 1
print("In this word letter 'a'", amount, "times" )
























    
slovo = input("Zadej slovo: ")
pocet = 0
for pismeno in slovo:
    if pismeno == "a":
        pocet = pocet + 1
print("Písmeno 'a' je ve slově", pocet, "krát")
