
#### try / except (catch) - hvatanje greski
  - kada ne zelimo da nas program puca
  - ipak zelimo da nastavimo i da damo informaciju korisniku
  
```python
try:
  broj = int(input("Unesite broj: "))
  print(broj)
except:
  print("Pogresan unos")

### 


try:
  vrijednost = 10 / 0
  broj = int(input("Unesite broj: "))
  print(broj)
except ZeroDivisionErron:
  print("Dijeljenje sa nulom")
except ValueError:
  print("Pogresan unos")

### 


try:
  vrijednost = 10 / 0
  broj = int(input("Unesite broj: "))
  print(broj)
except ZeroDivisionErron as err:
  print(err)
except ValueError:
  print("Pogresan unos")
```
