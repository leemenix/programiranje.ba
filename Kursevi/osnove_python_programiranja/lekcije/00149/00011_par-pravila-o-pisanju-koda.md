
<div style="page-break-after: always;"></div>

## Par pravila o pisanju koda u Python-u

### Indentacija

Kako smo vec naveli Python je fleksibilan ali i osjetljiv na nacin kako pisemo 
kod. Dakle prilikom pisanja izvornog koda potrebno je voditi racuna o uvlacenju
linija i razmacima na pocetku linije, sto se naziva indentacija. 
Razmaci i tabovi koje koristimo na pocetku linije prilikom pisanja koda, 
odredjuju nivo indentacije (uvlacenja), sto je bitno postovati tokom ostatka
pisanja koda unutar datoteteke, jer Python na ovaj nacin odredjuje blokove koda
i na taj nacin ih grupise u logicke cjeline.

Dakle vodite racuna da komande koje pisete, a treba da idu zejedno, imaju isti
nivo uvlacenja, u suprotnom doci ce do greske prilikom izvrsavanja. 

Naravno citav ovaj koncept cete shvatiti do kraj ove sekcije ali svakako nije 
lose napomenuti ovo pravilo.

```python      
print("Zdravo Svijete!") # ispravno

 print("Zdravo Svijete!") # greska! razmak na pocetku reda
```

Prilikom izvrsenja prethodnog koda Python ce se zaliti na indetnaciju i 
dobicete sintaksnu gresku. Bez panike, samo obrisite razmak na pocetku reda 
i sve ok.

Pravilo je da za uvlacenje koda koristitie samo razmake, a u slucaju da
koristitite tabove budite sigurni da je velicina taba podesena na 4 razmaka.
Ovo je automatski regulisano u skoro svakom savremenom IDE-u.

### Eksplicitno spajanje linija

U slucaju da prlikom pisanja koda zelimo veoma dugacku liniju napisati u vise
redova i pridurzite je promjenjivoj, koristicemo obrnutu kosu crtu (backslash) 
**\\**.

```python
tekst_pjesme = "9 depresivaca \
9 depresivaca gajili su bostan \
puko lastik od bandzija, ostalo ih 8 \
8 depresivaca, k'o u dlan ih gledam \
u krivini hladnjaca, ostalo ih 7 \
... \
3 depresivca, svaki od njih vrijedan \
dvojici crk'o facebook, ostao je 1 \
1 depresivac, oprezan je bio\
onda se ozenio"
```
