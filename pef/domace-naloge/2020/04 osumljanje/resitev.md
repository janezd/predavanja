Bilo je leta 2021. Lotila se je naloge. Mislila je, da ne bo težko. Naloga je bila [praktično enaka kot prejšnji teden](https://github.com/janezd/predavanja/blob/master/pef/domace-naloge/2020/03%20okuzbe/resitev.ipynb): morala je napisati funkcijo `osumljenci(osebe, zdravi, obiski)`, ki prejme neko množico oseb, neko množico preverjeno zdravih oseb in seznam obiskov. Funkcija je morala vrniti ... no, poenostavimo: tiste osebe iz množice `osebe`, ki se niso družile z nobeno zdravo osebo. Ja, praktično isto, oziroma še malo enostavneje, kot funkcija `osumljenci`, ki so jo pisali prejšnji teden.

In je sprogramirala.

```python
def osumljenci(osebe, zdravi, obiski):
    v_stiku_z_zdravimi = set()
    for oseba in zdravi:
        for osumljenec in osebe:
            if v_stiku(osumljenec, oseba, obiski):
                v_stiku_z_zdravimi.add(osumljenec)
    osebe -= v_stiku_z_zdravimi
    return osebe
```

(Pred to funkcijo je preprosto skopirala vse funkcije iz prejšnje domače naloge, tako da je lahko kar poklicala funkcijo `v_stiku`.)

In je pognala teste. Pa so izpisali:

```
set() != {'Berta'}

Expected :{'Berta'}
Actual   :set()

File "/Users/janez/Dropbox/Pedagosko/P1-Pef/dn04 - osumljanje/resitev.py", line 44, in test_osumljenci
    self.assertEqual({"Berta"}, osumljenci(skupinica, {"Dani", "Ema"}, obiski))
```

Očitno klic `osumljenci(skupinica, {"Dani", "Ema"}, obiski)` vrne prazno množico namesto množice `{"Berta"}`.

Pa je preverila, če je to res. V program je dopisala:

```python
skupinica = {"Ana", "Berta", "Cilka", "Dani", "Ema"}
obiski = [
    ("Ana", "kava"), ("Berta", "kava"), ("Cilka", "kava"),
    ("Cilka", "telovadba"), ("Ema", "telovadba"),
    ("Dani", "zdravnik"), ("Ana", "zdravnik")]
print(osumljenci(skupinica, {"Dani", "Ema"}, obiski))
```

In je videla, da njena funkcija `osumljenci` deluje pravilno: gornji klic vrne `{"Berta"}` in ne prazne množice, kot pravijo testi.

In mi je pisala, da je najbrž nekaj narobe s testi.

Tu torej pride naloga zate, moj(a) bodoči učitelj(ica). V priponki tokrat ni le testov, temveč tudi cela rešitev. Samo dela ne.

1. V program dopiši komentar, v katerem razložiš, zakaj funkcija, sodeč po gornjem `print`-u, deluje pravilno, testi pa pravijo, da ne. (In imajo prav!) Kaj se dogaja?!
2. Popravi funkcijo. Ne piši nove funkcije. Tvoj popravek mora biti omejen na eno vrstico. Samo eno vrstico dodaj, pobriši ali spremeni.

Oddaj tako spremenjeno datoteko.

### Rešitev

Testi sestavijo mmnožico 

```python
skupinica = {"Ana", "Berta", "Cilka", "Dani", "Ema"}
```

in potem večkrat pokličejo funkcijo s to množico. Funkcija pa v vrstici 

```python
osebe -= v_stiku_z_zdravimi
```

odstrani določene elemente te množice. Ker gre za isto množico, ki jo je funkcija dobila kot argument, na ta način dejansko spremeni množico `skupinica`. Ob naslednjem klicu zato funkcija dobi drugačne argumente.

O tem se najpreprostje prepričamo z razhroščevalnikom, ali pa tudi tako, da v teste dodamo izpis skupinice.

```python
skupinica = {"Ana", "Berta", "Cilka", "Dani", "Ema"}
print("skupinica =", skupinica)
self.assertEqual({"Dani", "Ema"}, osumljenci(skupinica, {"Berta"}, obiski))
print("skupinica =", skupinica)
self.assertEqual({"Berta"}, osumljenci(skupinica, {"Dani", "Ema"}, obiski))
```

Nauk zgodbe je, da funkcija nikoli nikoli nikoli ne sme spreminjati množic, seznamov, slovarjev ... ki jih je dobila kot argument. Razen, seveda, kadar je točno to namen te funkcije. Kako bi pogledali, če bi program 

```python
s = [1, 2, 3, 4]
print(sum(s))
print(sum(s))
```

namesto 

```
10
10
```

izpisal

```
10
6
```

ker bi funkcija `sum` iz kakega bizarnega razloga vedno odstranila zadnji element podanega ji seznama?

Popravek je preprost:

```python
osebe -= v_stiku_z_zdravimi
```

zamenjamo z


```python
osebe = osebe - v_stiku_z_zdravimi
```

To izračuna novo množico in jo priredi imenu `osebe`. Lahko pa tudi, recimo, naredimo kopijo množice oseb, tako da nekam v funkcijo vstavimo

```python
osebe = osebe.copy()
```

in potem na koncu mirno pustimo odštevanje.