
## Naredba return (return direktiva)

Kada zelimo dobiti povratnu informaciju iz funkcije koristimo naredbu return. Sa ovom informacijom
mozemo nastaviti manipulaciju kroz dajlni dio koda. Naredba return se moze pojaviti samo unutar tijela
funkcije. Takodje kada zelimo da funkcije mogu medjusobno komunicirati. 

2 na n-tu
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

rezultat - kub(3) # sacuvaj vrijednost koju si dobio od funkcije, ne i samu funkciju
print(rezultat)

#### 
def kub(broj):
  print("stampaj prije return direktive")
  return broj * broj * broj
  print("stampaj nakon return direktive")

print(cub(3))
```

### Funkcija ne mijenja sadrzaj promjenjive
```python
def brojac(broj):
  broj = broj + 1
  return broj

broj=3
brojac(broj) # vrijednost koju promjenjiva pokazuje, ali ne i samu promjenjivu, sto obezbjedjje da funkcija ne moze mijenjati promjenjivu, samo kopiju vrijednosti koja je proslijedjena
print(broj) # 

# funkcije unutar sebe mogu imati lokalne (local) i globalne (global) promjenjive
# ako lokalna i globalna promjenjiva unutar funkcije nose isti naziv, Pyhon ce koristiti lokalnu
# lokalne promjenjive su definisane po default-u ako se ne navede drugacije
def brojac():
	global broj
	broj = broj + 1
	return broj

broj = 3
brojac()
print(broj)

# nepoznati broj argumenta
# u slucaju da nismo sigurni koji je tacno broj argumenate koje zelimo proslijediti funkciji
# parametru funkcije dodamo * i time postizemo n broj elemenata koji mozemo proslijediti funkciji

def srecni_brojevi(*brojevi):
	print("Loto brojevi za ovu sedmicu: " + str(brojevi))

srecni_brojevi(8,13,22,12,54)
```

