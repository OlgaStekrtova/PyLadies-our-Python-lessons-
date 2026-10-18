# Cvičení 6 – For versus while
# Nejdřív rozhodni for/while a napiš si do komentáře proč, pak úlohu naprogramuj.

# V nádrži je 45 litrů vody a každou minutu z ní uteče 3 litry.
#    Po každé minutě vypiš, kolik vody zbývá, a nakonec vypiš,
#    po kolika minutách je nádrž prázdná.


Water= 45
Minutes = 0
while Water > 0:
    Water = Water - 3
    Minutes = Minutes + 1
    print("After", Minutes, "minutes there r", Water, "liters left")
print("Tank is empty after", Minutes, "minutes.")
