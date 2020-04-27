
<div style="page-break-after: always;"></div>

### Parametri funkcije

Vrijednosti (argumenti) koje proslijedjujemo funkciji se nazivaju parametrima 
funkcije. Sama funkcija bez parametara je prilicno staticna, dok se uvodjenjem
parametara postize dinamicnost i fleksibilnost, kao i sira upotreba funkcije.

**Parametre** funkcije definisemo prilikom inicijalnog kreiranja funkcije, 
stavljamo ih u zagrade i odvajamo zarezom, u slucaju da imamo vise od jednog 
parametra. 

Prilikom pozivanja funkcije, definisemo vrijednost koje proslijedjujemo 
funkciji, takodje unutar zagrada, a proslijedjenje parametre jednom rijeci
nazivamo **argumentima**.

```text
def brojac(broj): <- (broj) predstavlja parametar funkcije
  broj = broj + 1
  return broj

brojac(3)         <- (3) predstavlja argument, vrijednost koju proslijedjujemo
                         parametru (broj)
```

#### Lokalne i globalne promjenjive.

Promjenjiva koja se nalazi unutar bloka funkcije, ima odredjen opseg djelovanja
ili *scope* i nikako nije povezana sa promjenjivim van tijela funkcije. Ovaj 
tip promjenjivih koje se nalaze unutar bloka funkcije se nazivaju jos i 
**lokalne promjenjive**.

U slucaju da ipak zelimo definisati vrijednost promjenjive koja djeluje izvan
tijela funkcije, uvodimo komandu **global** i na taj nacin nasa promjenjiva
djeluje globalno, cak iako se nalazi unutar tijela funkcije. 

Ako lokalna i globalna promjenjiva unutar funkcije nose isti naziv, Pyhon ce 
koristiti lokalnu promjenjivu, ali ovo se ne preporucuje zbog zbunjivanja i 
konfuzije prilikom citanja koda.

<div style="page-break-after: always;"></div>

**`Izvorni kod: kod-265_parametri-funkcijama.py`**

```python
# funkcija ne mijenja sadrzaj promjenjive
broj_1 = 3
broj_2 = 10
def brojac(broj_1):
  broj_2 = 30
  print("Broj 2 iz funkcije ima vrijednost: " + str(broj_2))
  broj_1 = broj_1 + 1
  return broj_1

# vrijednost koju promjenjiva pokazuje, ali ne i samu promjenjivu, sto 
# obezbjedjje da funkcija ne moze mijenjati promjenjivu, samo kopiju 
# vrijednosti koja je proslijedjena
brojac(broj_1)
print(broj_1) 

brojac(broj_2)
print(broj_2) 

# funkcije unutar sebe mogu imati lokalne (local) i globalne (global) 
# promjenjive
# lokalne promjenjive su definisane po default-u ako se ne navede drugacije
broj_3 = 3

def brojac():
	global broj_3
	broj_3 = broj_3 + 1
	return broj_3

brojac()
print(broj)

```

<div style="page-break-after: always;"></div>

#### Nepoznati broj argumenta (**VarArgs**)

U slucaju da nismo sigurni koji je tacno broj argumenata koji zelimo 
proslijediti funkciji, tada parametru funkcije dodamo **\*** i time postizemo n-broj elemenata koji mozemo proslijediti funkciji.

**`Izvorni kod: kod-266_srecni-brojevi.py`**

```python
def srecni_brojevi(*brojevi):
	print("Loto brojevi za ovu sedmicu: " + str(brojevi))

srecni_brojevi(8,13,22,12,54)

# poziv funkcije iz druge funkcije
def kub(broj):
  return broj * broj * broj

def ispis_kubnog_broja(broj):
  kubni_broj = kub(broj)
  print("Kub broja " + str(broj) + " je " + str(kubni_broj))

ispis_kubnog_broja(2)

# docstring - dokumentacijski string,  predstavlja dokumentaciju same funkcije koja moze da se pozove funkcijom
# help()
def kub(broj):
  '''Funkcije izracunava kub unesenog broja, po formuli broj * broj * broj.
              Primjer koristenja funkcije: print(kub(2))
                                           daje vrijednost 8
  '''
  return broj * broj * broj

print(kub(2))
help(kub)

# neke od standardnih, ugradjenih, funkcija koje dolaze sa Python-om
print(abs(-1))
print(len("Goku"))
print(max(2,3))
print(min(2,3))
print(str(2))
print(type(kub))
print(type(print))
print(type(type))
```

**`Izvorni kod: kod-267_dva-i-vise-parametara.py`**

```python
def zbir(*brojevi_1,**brojevi_2):
  broj = 0
  for broj_1 in brojevi_1:
    broj += broj_1
    print(broj_1)
  for broj_2 in brojevi_2:
    broj += broj_2
    print(broj_2)

  return broj
  
print(zbir(1,2,3,30,3))
```

#### Podrazumijevana vrijednost argumenta 

U slucaju da zelimo koristiti podrazumijevanu vrijdnost argumenta ili 
jednostavno znamo da je ta vrijednost konstantna tokom izvrsavanja koda,
onda unutar definisanja parametara funkcije pomocu operatora dodjele **=** 
definisemo podrazumijevanu vrijednost.

**`Izvorni kod: kod-268_podrazumijevana-vrijednost-argumenta.py`**

```python
def obim_kruga(poluprecnik, pi=3.14):
  obim = 2 * (poluprecnik * pi)
  return obim

print(obim_kruga(2))
```

#### Argumenti definisani pomocu kljucnih rijeci

U slucaju da nismo sigurni koji je tacno broj argumenata koji zelimo 
proslijediti funkciji, tada parametru funkcije dodamo **\*** i time postizemo n-broj elemenata koji mozemo proslijediti funkciji.

**`Izvorni kod: kod-269_argumenti-definisani-pomocu-kljucnih-rijeci.py`**

```python
#### 
def pozdrav_svijete(rijec="Pozdrav Svijete \n", broj=2):
  print((rijec) * broj)

print(pozdrav_svijete(rijec="Zdravo \n", broj=10))
```

Ako zelimo definisati parametre dostupne samo preko kljucnih rijeci bez
obzira na poziciju na kojoj se nalaze, to mozemo uraditi definisanjem 
paramatara posle prvog parametra sa **\***.

**`Izvorni kod: kod-270_vrijednost-parametra-bez-obzira-na-poziciju.py`**

```python
def zbir(*brojevi_1,broj_2):
  broj = 0
  for broj_1 in brojevi_1:
    broj += broj_1
    print(broj_1)
  broj += broj_2

  return broj
  
print(zbir(1,2,3,30,3,broj_2=2222))
```

