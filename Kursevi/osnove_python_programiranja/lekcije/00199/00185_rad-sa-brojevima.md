
<div style="page-break-after: always;"></div>

## Rad sa brojevima

Imamo dvije osnovne vrste brojeva u Python-u:

1. Cijeli brojevi (integer)
2. Decimalni ili brojevi sa pokretnim zarezom (float)

Osnovne aritmeticke operacije koje mozemo vrsiti u Python-u su

```yaml
 Operacija |    Naziv operacije   |     Primjer      |   Rezultat   
___________|______________________|__________________|____________
     +     |      Sabiranje       |  print(1 + 1)    |    2
___________|______________________|__________________|____________
     -     |      Oduzimanje      |  print(6 - 5)    |    1
___________|______________________|__________________|____________
     *     |       Mnozenje       |  print(4 * 3)    |    12
___________|______________________|__________________|____________
     /     |      Dijeljenje      |  print(4 / 2)    |    2
___________|______________________|__________________|____________
     %     |      Ostatak pri     |  print(5 % 2)    |    1
           |   dijeljenju (moduo) |                  |  
___________|______________________|__________________|____________
     **    |      Potenciranje    |  print(2 ** 3)   |    8
___________|______________________|__________________|____________
```

**`Izvorni kod: kod-185_rad-sa-brojevima.py`**
```python
print(3)
print(-4)
print(3.333)
print(7+3)
print(7+3.333)
print(8/4)
print(2*4)
print (2*(4+5))
# modulo , ostatak 9 mod 4
print(9%4)

moj_broj = 13
print(moj_broj)
print("Moj omiljeni broj" + str(moj_broj))
```

<div style="page-break-after: always;"></div>

### Funkcije nad brojevima

**`Izvorni kod: kod-186_rad-sa-brojevima.py`**
```python
# math funkcije, funkcije su vec pripremljen kod koji odradjuje posao za nas
broj = -2
print(abs(broj))
print(pow(4,2))
print(max(5,10))
print(min(3,6))
print(round(3.3333))
print(round(3.6))
print(round(3.5))

# import math modul (import math funkcije vise kada budemo pricali o modulima)
from math import *
print(floor (3.6))
print(ceil(3.6))
print(sqrt(9))
```
