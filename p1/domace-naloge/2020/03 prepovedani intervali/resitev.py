
prepovedani = [
    (12, 18),
    (2, 5),
    (3, 8),
    (0, 4),
    (15, 19),
    (6, 9),
    (13, 17),
    (4, 8)
]

# Ogrevanje

naj = 0
for spodnja, zgornja in prepovedani:
    if zgornja > naj:
        naj = zgornja
print(naj)

# Naloga

i = 0
while i <= naj:
    for spodnja, zgornja in prepovedani:
        if spodnja <= i <= zgornja:
            break
    else:
        print(i, "je dovoljeno")
    i = i + 1

# Dodatna

i = 0
while True:
    for spodnja, zgornja in prepovedani:
        if spodnja <= i <= zgornja:
            print(i, "je vsebovan v", (spodnja, zgornja))
            break
    else:
        dovoljeno = i
        break
    i = i + 1

print("Prvo dovoljeno", dovoljeno)
