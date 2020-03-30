
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

### Relacijski operatori, operatori poredjenja (>,<, >=, <=, ==, !=)

```yaml
 Operacija |    Naziv operacije   |     Primjer      |   Rezultat  
           |                      |     ako su :     |
           |                      |  a=3 b=2 i c=3   |
___________|______________________|__________________|____________________
     >     |         Vece         |    print(a > b)  |    Tacno (True)
___________|______________________|__________________|____________________
     <     |         Manje        |    print(a < b)  | Nije Tacno (False)
___________|______________________|__________________|____________________
     >=    |    Vece ili jednako  |   print(a >= b)  |    Tacno (True)
           |                      |   print(a >= c)  |    Tacno (True) 
___________|______________________|__________________|____________________
     <=    |   Manje ili jednako  |   print(a <= b)  | Nije Tacno (False)
           |                      |   print(a <= c)  |    Tacno (True)             
___________|______________________|__________________|____________________
     ==    |      Jednako         |   print(a == b)  | Nije Tacno (False)
           |                      |   print(a == c)  |    Tacno (True)
___________|______________________|__________________|____________________
     !=    |     Nije jednako     |   print(a != b)  |    Tacno (True)
           |      Razlicito       |   print(a != c)  | Nije Tacno (False)    
___________|______________________|__________________|____________________
```

### Logicki operatori (and, or i not)

```yaml
 Operacija |    Naziv operacije   |       Primjer        |   Rezultat  
           |                      |       ako su :       |
           |                      |a=3 b=2 i dobar=True  |
___________|______________________|______________________|______________
     and   |         i            |if(a > 4 and b < 3):  | 
           |                      |  print("Zdravo")     |
           |                      |else:                 | Dovidjenja
           |                      |  print("Dovidjenja") |   
___________|______________________|______________________|______________
     or    |        ili           |if(a > 4 or b < 3):   | 
           |                      |  print("Zdravo")     |
           |                      |else:                 |   Zdravo
           |                      |  print("Dovidjenja") |   
___________|______________________|______________________|______________
     not   |      ne, nije        |if(not(dobar)):       | 
           |                      |  print("Nije Dobro") |
           |                      |else:                 |  Dobro je
           |                      |  print("Dobro je")   |   
___________|______________________|______________________|______________
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
