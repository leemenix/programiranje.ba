
##### Objasnjenje

Ocigledno string moze koristiti odredjene specifikacjije, a metod _format_ moze
biti pozvan upravo da zamijeni ove specifikacije odredjenim argumentima.

Primijetimo da unutar string-a koristimo _{0}_ koji odgovara vrijednosti
promjenjive _ime_ koja je ujedno prvi argument metode _format_. Slicno _{1}_
odgovara vrijednosti promjernjive _godine_ koja je drugi argument metode
_format_.

Bitno je napomenuti da Python pocinje brojati od _0_ (nule) sto znaci da prva
pozicija predstavlja _indeks 0_, druga pozicija _indeks 1_ itd.

**`Primjer`**
```python
Brojevi:  0   1   2   3   4   5   6   7   8   9   10  100  201  300  [n]

Indeks:  [0] [1] [2] [3] [4] [5] [6] [7] [8] [9] [10] [11] [12] [13] [n]
```

Prethodni string mozemo napisati i kao

```python
print(ime + ' ima ' + str(godine) + ' godina.')
```

ciji ce rezultat biti identican

```python
Petar ima 30 godina.
```

ali primijticete da ovaj nacin pisanja izgeda dosta ruznije i povecava
mogucnost greske. Takodje metod _format_ ce automatski izvrsiti konverziju
varijable _godine_ u tip string, ali dodatno mozemo izmijeniti poruku bez
izmejne vrijednosti varijable. TBD.

Takodje, koristenjem metode _format_ numerisanje unutar same poruke je opcionalno, tako
da kod moze biti napisan i kao

<a name="kod-207-metod-format.py"/>

**`Primjer: kod-207-metod-format.py`**
```python
godine = 30
ime = 'Petar'

print('{} ima {} godina.'.format(ime, godine))
print('Da li {} ide u skolu?'.format(ime))
```
**`Rezultat`**
```
Petar ima 30 godina.
Da li Petar ide u skolu?
```

Isti kod moze biti napisan i na nacin da imenujemo parametre

<a name="kod-208-metod-format.py"/>

**`Primjer: kod-208-metod-format.py`**
```python
godine = 30
ime = 'Petar'

print('{ime_osobe} ima {godine_osobe} godina.'.format(ime_osobe=ime, godine_osobe=godine))
print('Da li {ime_osobe} ide u skolu?'.format(ime_osobe=ime))
```
**`Rezultat`**
```
Petar ima 30 godina.
Da li Petar ide u skolu?
```

Sa verzijom Python 3.6 uvodi novi nacin kako mozemo imenovati parametre, skracenom
verzijom "f-strings"

<a name="kod-209-metod-format.py"/>

**`Primjer: kod-209-metod-format.py`**
```python
godine = 30
ime = 'Petar'

print(f'{ime} ima {godine} godina.') # Primijetimo 'f' prije definisanja stringa
print(f'Da li {ime} ide u skolu?') # Primijetimo 'f' prije definisanja stringa
```
**`Rezultat`**
```
Petar ima 30 godina.
Da li Petar ide u skolu?
```
