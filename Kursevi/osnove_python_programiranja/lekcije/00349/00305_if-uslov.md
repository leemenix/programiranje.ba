
#### uslov if
- donosenje odluke, na osnovu uslova koji se moraju ispuniti
- krairamo program pametnijim, omogucujemo donosenje odluke
```yaml
Probudio sam se i oprao zube
ako sam gladan
  trebam doruckovati

Trebam ici u vani
ako je oblacno
  ponijecu kisobran
u suprotnom 
  ponijecu suncane naocare

U restoranu 
ako zelim meso
  narucicu stejk
ako zelim pastu
  narucicu spagete
u suprotnom
  narucicu salatu
```

```python
dobar = True

if dobar:
  print("Goku je dobar karakter")

#### 
dobar = True
zabavan = False

if dobar or smijesan:
  print("Goku je dobar karakter") # koliko god koda mozete smjestiti ovde
  print("Freza nije je zabavan")
else:
  print("Freza je los karakter")

### 
dobar = True
zabavan = True

if dobar and smijesan:
  print("Goku je dobar karakter") # koliko god koda mozete smjestiti ovde
  print("Krilin je zabavan")
else:
  print("Freza je los karakter")

#### 
dobar = True
zabavan = False

if dobar or smijesan:
  print("Goku je dobar karakter") # koliko god koda mozete smjestiti ovde
elseif dobar and not(zabavan):
  print("Freza nije je zabavan")
else:
  print("Freza je los karakter")
```

### Operatori poredjenja i uslov if (>,<, >=, <=, ==, !=)

maksimalan_broj.py
```python
def maksimalan_broj(broj_1, broj_2, broj_3):
  if broj_1  >= broj_2 and broj_1 >= broj_3:
    return broj_1
  elif broj_2 >= broj_1 and broj_2 >=broj_3:
    return broj_2
  else:
    return broj_3

print(maksimalan_broj(7, 8, 9))
```

kalkulator_nadogradjena_verzija.py

Ovo je bio osnovni_kalkulator.py

```python
broj_1 = input("Unesite prvi broj: ")
broj_2 = input("Unesite drugi broj: ")
rezultat = broj1 + broj2

print(rezultat)

broj_1 = input("Unesite prvi broj: ")
broj_2 = input("Unesite drugi broj: ")
rezultat = float(broj_1) + float(broj_2)

print(rezultat)
```

kalkulator_nadogradjena_verzija.py

```python
broj_1 = float(input("Unesite prvi broj: "))
broj_2 = float(input("Unesite drugi broj: "))
operator = input("Unesite operator: [+, -, /, *] ")

if operator == "+":
  print(broj_1 + broj_2)
elif operator == "-":
  print(broj_1 - broj_2)
elif operator == "/":
  print(broj_1 / broj_2)
elif operator == "*":
  print(broj_1 * broj_2)
else: 
  print("unijeli ste pogresan operator")
```
