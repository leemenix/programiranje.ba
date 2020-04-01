
<div style="page-break-after: always;"></div>

## Moduli i pip alat

Moduli nisu nista drugo, nego odredjen broj funkcija koje mozete importovati, 
pozvati u vas kod. Takodje, mozete napraviti vas modul jednostavnim kreiranjem
python fajla koji sadrzi vase funkcije i kasnije ga pozvati u vas kod naredbom
**import**. 
U ovoj lekciji cete nauciti kako instalirati eksterne module sa **pip** 
komandom, kako ih importovati nakon instalacije, kako importovati standardne 
module i konacno kako kreirati i importovati svoj modul. 
 
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
tbd.
```text 
{## how to install with pip
## how to import and use modules
}
```