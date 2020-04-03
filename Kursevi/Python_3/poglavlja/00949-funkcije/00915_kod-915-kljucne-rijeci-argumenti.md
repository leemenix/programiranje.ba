
<a name="kod-915-kljucne-rijeci-argumenti.py"/>

**`kod-915-kljucne-rijeci-argumenti.py`**
```python
def brojevi(a, b=7, c=13):
    print('a ima vrijednost', a, 'b ima vrijednost', b, 'c ima vrijednost', c)

brojevi(4, 5)
brojevi(34, c=19)
brojevi(b=33, a=10)
```
**`Rezultat`**
```
a ima vrijednost 4 b ima vrijednost 5 c ima vrijednost 13
a ima vrijednost 34 b ima vrijednost 7 c ima vrijednost 19
a ima vrijednost 10 b ima vrijednost 33 c ima vrijednost 13
```
