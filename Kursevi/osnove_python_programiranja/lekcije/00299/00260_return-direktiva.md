
<div style="page-break-after: always;"></div>

## Naredba return (return direktiva)

Kada zelimo dobiti povratnu informaciju iz funkcije koristimo naredbu **return**. Sa ovom informacijom mozemo nastaviti manipulaciju kroz daljni dio koda. 
Naredba return se moze pojaviti samo unutar tijela funkcije. Takodje kada 
zelimo da funkcije mogu medjusobno komunicirati, razmjenjivati informacije 
koristimo return naredbu. 

**`Izvorni kod: kod-260_kub-broja.py`**

```python
def kub(broj):
  broj * broj * broj

cub(3)

print(kub(3))

#### 
def kub(broj):
  return broj * broj * broj # aha zelim vratiti informaciju ko god da je pozvao funkciju

print(kub(3))

#### 
def kub(broj):
  return broj * broj * broj 

rezultat = kub(3) # sacuvaj vrijednost koju si dobio od funkcije, ne i samu funkciju
print(rezultat)

#### 
def kub(broj):
  print("stampaj prije return direktive")
  return broj * broj * broj
  print("stampaj nakon return direktive")

print(cub(3))
```
