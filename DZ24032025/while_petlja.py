# Ispisite brojeve od 1 do 10 koristeci se petljom while.
broj = 1
while broj <= 10:
    print(broj)
    broj += 1

print('\n')

# Ispisite sve parne brojeve od 2 do 20 koristeci se petljom while.      
broj = 2
while broj <= 20:
    print(broj)
    broj = broj +2

print('\n')

# Ispisite sve neparne brojeve od 1 do 15 koristeci se petljom while.
broj = 1
while broj <= 15:
    print(broj)
    broj = broj +2

print('\n')

# Ispisite sve prirodne brojeve manje od 100 koji su djeljivi s 5 koristeci se petljom while.
broj = 5
while broj < 100:
    print(broj)
    broj = broj + 5

print('\n')

# Ispisite prvih 10 kvadrata prirodnih brojeva koristeci se petljom while.
broj = 1
while broj <= 10:
    kvadrat = broj * broj
    print(f"{broj}² = {kvadrat}")
    broj = broj + 1

print('\n')

# Ispisite sve prirodne brojeve manje od 100 koji su kvadrati nekoga drugoga prirodnog broja koristeci se petljom while.
broj = 1
while broj * broj < 100:
    print(broj * broj)
    broj = broj + 1


print('\n')

# Ispisite sve slozene brojeve manje od 50 koristeci se petljom while.
broj = 4
while broj < 50:
    broj_djelitelja = 0
    djelitelj = 1
    
    while djelitelj <= broj:
        if broj % djelitelj == 0:
            broj_djelitelja += 1
        djelitelj += 1
    
    if broj_djelitelja > 2:
        print(broj)
    broj += 1


print('\n')

# Ispisite sve troznamenkaste brojeve ciji je zbroj znamenaka veci od 10 koristeci se petljom while (Koristiti se % modulo operacijom)
broj = 100
while broj < 1000:
    jedinice = broj % 10
    desetice = (broj // 10) % 10
    stotice = broj // 100
    zbroj_znamenaka = jedinice + desetice + stotice
    
    if zbroj_znamenaka > 10:
        print(f"{broj} (zbroj znamenaka: {zbroj_znamenaka})")
    broj += 1