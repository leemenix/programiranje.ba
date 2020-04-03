
<a name="kod-911-globalne-promjenjive.py"/>

**`kod-911-globalne-promjenjive.py`**
```python
promjenjiva = 32


def funkcija():
  global promjenjiva
  print('promjenjiva ima vrijednost', promjenjiva)

  promjenjiva = 23
  print('promjenjiva ima novu vrijednost', promjenjiva)

funkcija()
print('vrijednost promjenjive na kraju programa je', promjenjiva)
```
**`Rezultat`**
```
promjenjiva ima vrijednost 32
promjenjiva ima novu vrijednost 23
vrijednost promjenjive na kraju programa je 23
```
