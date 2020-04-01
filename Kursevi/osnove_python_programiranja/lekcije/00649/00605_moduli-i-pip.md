
## moduli i pip alat
- python fajl koji mozete importovati unutar vaseg python koda
- kako kreirati svoj modul
- kako instalirati module (list of python modules on google) pip paket manager
- build-in moduli (ugradjeni) i eksterni moduli
 
**`Izvorni kod: kod-605_korisni-alati.py`**
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

## how to install with pip
## how to import and use modules
```
