
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


```python
import os

print(help(os))

print("Trenutni radni direktorij: ")
print(os.getcwd())
```

Kada Python uspjesno importuje modul **os**, on u principu pronadje na vasem 
sistemu fajl po imenu **os.py**, u prethodno definisanom direktorijumu, 
specijalno namijenjenom za skladistenje standardnih modula. 

### Djelimicno importovanje **from .. import**

```python

```

tbd.
```text 
{## how to install with pip
## how to import and use modules
}


tbd.
```text 
{## how to install with pip
## how to import and use modules
}
```
**`Izvorni kod: kod-655_korisni-alati.py`**
```python
#
import random

def srecan_broj(broj):
    return random.randint(1, broj)

def pozdrav(tekst):
    return ("Pozdrav " + tekst)

##
import korisni_alati

print(korisni_alati.srecan_broj(3))
print(korisni_alati.pozdrav("Goku"))

##
from korisni_alati import *

print(srecan_broj(3))
print(pozdrav("Goku"))

##
import korisni_alati as ka

print(ka.srecan_broj(3))
print(ka.pozdrav("Goku"))

```
