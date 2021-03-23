Se je lotila naloge. Je mislila, da ne bo težko. Naloga je bila praktično enaka kot prejšnji teden: morala je napisati funkcijo `osumljenci(osebe, zdravi, obiski)`, ki prejme neko množico oseb, neko množico preverjeno zdravih oseb in seznam obiskov. Funkcija je morala vrniti ... no, poenostavimo: tiste osebe iz množice `osebe`, ki se niso družile z nobeno zdravo osebo. Ja, praktično isto, oziroma še malo enostavneje, kot funkcija `osumljenci`, ki smo jo pisali prejšnji teden.

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
