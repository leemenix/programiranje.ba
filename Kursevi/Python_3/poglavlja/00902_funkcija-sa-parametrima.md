
<a name="funkcija-sa-parametrima"/>

### program-xx - funkcija-sa-parametrima

```python
def uporedi(a,b):
  if a > b:
    print(a, 'je vece od', b)
  elif a == b:
    print(a, 'je jednako', b)
  else:
    print(a, 'je manje od', b)

# direktno prosljedivnje parametara funkciji
uporedi(3,5)
uporedi(5,5)
uporedi(6,2)
```

Output:
```
(3, 'je manje od', 5)
(5, 'je jednako', 5)
(6, 'je vece od', 2)
```