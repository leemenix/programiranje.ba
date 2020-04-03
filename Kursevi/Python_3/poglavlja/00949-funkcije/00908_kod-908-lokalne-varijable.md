
<a name="kod-908-lokalne-varijable.py"/>

**`kod-908-lokalne-varijable.py`**
```python
promjenjiva = 32


def funkcija(promjenjiva):
  print('promjenjiva ima vrijednost', promjenjiva)
  promjenjiva = 23
  print('promjenjiva ima novu vrijednost', promjenjiva)

funkcija(promjenjiva)
print('vrijednost promjenjive na kraju programa je', promjenjiva)
```
**`Rezultat`**
```
promjenjiva ima vrijednost 32
promjenjiva ima novu vrijednost 23
vrijednost promjenjive na kraju programa je 32
```
