
<div style="page-break-after: always;"></div>

## Moduli i pip alat

Moduli nisu nista drugo, nego odredjen broj funkcija koje mozete importovati, 
pozvati u vas kod. Takodje, mozete napraviti vas modul jednostavnim kreiranjem
python fajla koji sadrzi vase funkcije i kasnije ga pozvati u vas kod naredbom
**import**. 

U ovoj lekciji cete nauciti kako kako importovati standardne module, 
instalirati eksterne module sa **pip** komandom, kako ih importovati nakon 
instalacije, i konacno kako kreirati i importovati svoj modul. 

### Importovanje standardnih Python modula **import** 

Recimo da nam je potrebna informacija, prilikom pisanja naseg koda, koja nam
govori u kom se trenutno direktoriju nalazimo. Za ovo bi nam trebalo dosta 
prethodnog iskusta, vremena i poznavanja operativnog sistema, a da ne pricamo
da su strukture direktorija razlicite na razlicitim operativnim sistemima. 
U tu svrhu jednostavno mozemo da importujemo standardni Python modul **os**,
bez obzira na kom operativnom sistemu radimo nacin koriscenja je isti.

**`Izvorni kod: kod-653_standardni_moduli.py`**
```python
import os

print(help(os))

print("Trenutni radni direktorij: ")
print(os.getcwd())
```
Kada Python uspjesno importuje modul **os**, on u principu pronadje na vasem 
sistemu fajl po imenu **os.py**, u prethodno definisanom direktorijumu, 
specijalno namijenjenom za skladistenje standardnih modula. 

**`Izvorni kod: kod-653_standardni_moduli.py`**
```python
import sys

print(help(sys))

print(sys.version_info)

print("Trenutni radni direktorij: ")
print(os.getcwd())
```

### Funkcija dir() nad modulima

Ugradjena dir() funkcija vraca listu naziva definisanih unutar objekta. U slucaju da je objekt modul, dir() vraca listu funkcija, klasa i promjenjivih definisane u tom modulu. 
Moguce je proslijedjivanje argumenata funkciji dir(), na nacin da u slucaju da postoji naziv modula koji je jednak argumentu, funkcija vraca listu naziva specificnih za taj modul. 

**`Izvorni kod: kod-653_standardni_moduli.py`**
```python
import sys
# lista svih elemenata
dir()
# lista odredjenog elementa
dir(sys)

karakter = "Goku"
dir()
del karakter
dir()
```

### Selektivno importovanje **from .. import**

**`Izvorni kod: kod-654_selektivno_importovanje.py`**
```python
import math
sqrt(9)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sqrt' is not defined
math.sqrt(9)
3.0

from math import sqrt
sqrt(9)
3.0
print("Kvadratni korijen od 9 je ", sqrt(9))
```
**`Izvorni kod: kod-655_korisni-alati.py`**
```python
#
import random

def srecan_broj(broj):
    return random.randint(1, broj)

def pozdrav(tekst):
    return ("Pozdrav " + tekst)

__version__ = "0.0.1"
##
import korisni_alati

print(korisni_alati.srecan_broj(3))
print(korisni_alati.pozdrav("Goku"))

print("Verzija", korisni_alati.__version__)

##
from korisni_alati import *

print(srecan_broj(3))
print(pozdrav("Goku"))

## Import as
import korisni_alati as ka

print(ka.srecan_broj(3))
print(ka.pozdrav("Goku"))
```
