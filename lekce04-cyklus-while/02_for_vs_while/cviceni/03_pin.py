# Cvičení 3 – For versus while
# Nejdřív rozhodni for/while a napiš si do komentáře proč, pak úlohu naprogramuj.

# Ptej se na PIN tak dlouho, dokud uživatel nezadá "1234".
#    Pak vypiš "Odemčeno!".


while True:
    password = input ("Type ur password:")
    if int(password) == 1234:
        print("Odemčeno!") 
