
<a name="kod-917-varargs-parametri.py"/>

**`kod-917-varargs-parametri.py`**
```python
def ispis(a=4, *broj, **imenik):
    print('a', a)

    # prodji kroz sve elemente tuple-a
    for element in broj:
        print('element', element)

    # prodji kroz sve elemente rijecnika
    for prvi_element, drugi_element in imenik.items():
        print(prvi_element, drugi_element)

ispis(10,13,32,15,Petar=166,Marko=165,Ogi=164)
```
**`Rezultat`**
```
a 10
element 13
element 32
element 15
Petar 166
Marko 165
Ogi 164
```
