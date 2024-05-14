Recimo, da imamo višine stopnic (ne relativne, temveč glede na podlago). 

```
(0) 1 2 3 4 7 8 10 11 13
```

Nekdo hodi po stopnicah in jih lahko tudi preskakuje, ne more pa stopiti na stopnico, ki je za več kot 3 višja od prejšnje. Gornje stopnice lahko torej prehodi takole: `(0) 1 3 4 7 10 11 13`, ali takole: `(0) 3 4 7 10 13` ali `(0) 2 4 7 8 11 13` ali `(0) 1 2 3 4 7 8 10 11 13`, ne more pa iti `(0) 1 3 7 10 13`, ker je razlika med 3 in 7 večja od 3.

Vprašanje je: na koliko različnih načinov lahko pride do stopnice 13?

Nalogo lahko rešite na različne manj učinkovite načine. Na enega kar počasnega, vendar potencialno delujočega, namiguje spodnja koda:

```
>>> from itertools import combinations
>>>
>>> s = [1, 2, 3, 4, 7, 8, 10, 11, 13]
>>>
>>> list(combinations(s, 7))
[(1, 2, 3, 4, 7, 8, 10), (1, 2, 3, 4, 7, 8, 11), (1, 2, 3, 4, 7, 8, 13), (1, 2, 3, 4, 7, 10, 11),
(1, 2, 3, 4, 7, 10, 13), (1, 2, 3, 4, 7, 11, 13), (1, 2, 3, 4, 8, 10, 11), (1, 2, 3, 4, 8, 10, 13),
(1, 2, 3, 4, 8, 11, 13), (1, 2, 3, 4, 10, 11, 13), (1, 2, 3, 7, 8, 10, 11), (1, 2, 3, 7, 8, 10, 13),
(1, 2, 3, 7, 8, 11, 13), (1, 2, 3, 7, 10, 11, 13), (1, 2, 3, 8, 10, 11, 13), (1, 2, 4, 7, 8, 10, 11),
(1, 2, 4, 7, 8, 10, 13), (1, 2, 4, 7, 8, 11, 13), (1, 2, 4, 7, 10, 11, 13), (1, 2, 4, 8, 10, 11, 13),
(1, 2, 7, 8, 10, 11, 13), (1, 3, 4, 7, 8, 10, 11), (1, 3, 4, 7, 8, 10, 13), (1, 3, 4, 7, 8, 11, 13),
(1, 3, 4, 7, 10, 11, 13), (1, 3, 4, 8, 10, 11, 13), (1, 3, 7, 8, 10, 11, 13), (1, 4, 7, 8, 10, 11, 13),
(2, 3, 4, 7, 8, 10, 11), (2, 3, 4, 7, 8, 10, 13), (2, 3, 4, 7, 8, 11, 13), (2, 3, 4, 7, 10, 11, 13),
(2, 3, 4, 8, 10, 11, 13), (2, 3, 7, 8, 10, 11, 13), (2, 4, 7, 8, 10, 11, 13), (3, 4, 7, 8, 10, 11, 13)]
>>>
>>> list(combinations(s, 8))
[(1, 2, 3, 4, 7, 8, 10, 11), (1, 2, 3, 4, 7, 8, 10, 13), (1, 2, 3, 4, 7, 8, 11, 13), (1, 2, 3, 4, 7, 10, 11, 13),
(1, 2, 3, 4, 8, 10, 11, 13), (1, 2, 3, 7, 8, 10, 11, 13), (1, 2, 4, 7, 8, 10, 11, 13), (1, 3, 4, 7, 8, 10, 11, 13),
(2, 3, 4, 7, 8, 10, 11, 13)]
```

... in tako naprej in nazaj. Ne samo za 7 in 8, temveč od 1 do `len(s)`.

Enega nič prida hitrejšega, ampak prav tako delujočega, nakazuje tole:

```
>>> from itertools import combinations_with_replacement
>>>
>>> list(combinations_with_replacement([True, False], 4))
[(True, True, True, True), (True, True, True, False),
 (True, True, False, False), (True, False, False, False),
 (False, False, False, False)]
 ````

Namesto `4` bi imeli `len(s)`, kjer je `s` seznam višin stopnic. Pa razmislite, kaj bi s toliko `True`-ji in `False`-i, kolikor je stopnic.

Na tak ali drugačen način lahko sestavite vse možne poti in preverite, koliko je legalnih.

Očitno boljši način je, da poskusite sestaviti vse možne poti.

Pri razmišljanju vam lahko pomaga, če poskusite rešiti nalogo ročno, brez računalnika. V resnici sploh ni težko. Vendar ... ne poskušajte dejansko sestavljati in šteti. Trik je v tem, da število poti do neke stopnice izračunaš iz števila poti do nekih drugih, prejšnjih stopnic.

## Branje podatkov

Lahko delate z gornjimi podatki, lahko pa jih preberete iz priloženih datotek `example.txt` (teh je malo več) in `input.txt` (teh je še veliko več). 

Pravilni odgovor za gornji seznam je (najbrž) 35, (gotovo pravilna) odgovora za `example.txt` in `input.txt` pa sta 19208 in 10578455953408. Z naivnimi rešitvami bo možno rešiti gornji primer, drugega najbrž ne, tretjega pa gotovo ne.

## Izvirna naloga

Naloga je z Advent of Code 2020, naloga [10: Adapter Array](https://adventofcode.com/2020/day/10), kjer je zgodbica sicer nekoliko drugačna. Gre za drugi del naloge; opis dobite, če rešite prvi del (za kar se morate logirati na stran s svojim računom na githubu, googlu, twitterju ali redditu). Rešitev lahko najdete na spletu ... vendar bi bilo to očitno neumno.

## Podatki