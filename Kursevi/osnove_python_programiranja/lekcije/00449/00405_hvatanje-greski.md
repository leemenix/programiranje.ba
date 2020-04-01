
## Hvatanje greski - try / except (catch)

Kada imamo situaciju da bez obzira na gresku u nasem programu, ipak zelimo
da nastavimo sa izvrsenjem programa i damo smislenu povratnu informaciju 
korisniku, tada koristimo **`try/except`** za hvatanje greske.

**`Izvorni kod: kod-405_hvatanje-greski.py`**
  
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
