
<div style="page-break-after: always;"></div>

## For petlja

For petlju (ili **for..in**) mozemo nazvati specijalni tip petlje u Python-u, 
a za razliku od while petlje, for petlju  koristimo kada zelimo da vrsimo 
iteraciju kroz tijelo petlje ako unaprijed **znamo broj potrebnih iteracija**.

Vrijednosti se uglavnom zadaju kao predefinisane ali mozemo koristiti izvore poput lista, stringova, rijecnika.

**`Izvorni kod: kod-320_rad-sa-for-petljom.py`**

```python
# operator in, za iteraciju nad listama, torkama, rijecnicima mozemo koristit kljucnu rijec in
for slovo in "programiranje.ba":
  print(slovo)

for karakter in karakteri:
  print(karakter)

karakteri = ["Goku", "Kirlin", "Yamcha"]
for indeks in range(len(karakteri)):
  print (karakteri[indeks])

loto_brojevi = [1,33,13,43,56]
for broj in loto_brojevi:
  print (broj)

for broj in range(20):
  print(broj)

for broj in range(14, 20):
  print (broj)

for indeks in range(len(karakteri)):
  print (karakter[indeks])

for broj in range(5):
    if broj == 0:
        print("prvi pokusaj")
    else:
        print("ostali")

for i in range(10):
    print (i)
    i+=1

# break naredba unutar for petlje
karakteri = ["Goku", "Kirlin", "Yamcha", "Goku", "Bulma"]
for i in range(len(karakteri)):
  if karakteri[i] == "Yamcha":
    print("Prekini izvrsenje for petlje")
    break
  print (karakteri[i])

# enumerate() funkcija - enumeracija
# ukoliko zelimo da zajedno sa vrijednostima iz liste, stringa ili rijecnika ispisujemo i njihove 
# indekse
# koristicemo funkciju enmureate()
karakteri = ["Goku", "Kirlin", "Yamcha", "Goku", "Bulma"]
for i,ime in enumerate(karakteri):
  print(str(i) + " " + ime)

### eksponencijaln funkcija - kada ne znamo koliki je eksponent
#print(2**3)

def eksponent_broja(baza, eksponent):
  rezultat = 1
  for i in range(eksponent):
    rezultat = rezultat * baza
  return rezultat

print(eksponent_broja(2,3))
```

### Primjer algoritma sortiranje mjehuricima (bubble sorting)

Prije nego napisemo kod potrebno je kratko objasnjenje algoritma. Algoritam 
sortiranje mjehuricima, ima za cilj da nad zadatim nizom nasumicnih/slucajnih 
brojeva izvrsi sortiranje od najmanjeg ka najvecem. Ovakvi tipovi zadataka 
predstavljaju osnovne koncepte teorije algoritma, a mozemo ih naci, kao 
zadatke, na intervjuima u velikim firmama poput Google-a, Amazon-a, 
Facebook-a, Microsoft-a ...

Predpostavimo da imamo niz brojeva:

```text
[4,2,1,5,3]
```

Primjenom algoritma sortiranja mjehuricima, svakom novom iteracijom, svaki 
element niza ce se uporedjivati sledecim, u slucaju da je prvi element veci od 
sledeceg, zaminijece mijesta, u suprotnom prvi element ostaje na svom mjestu. Ovaj proces se nastavlja sve dok se svi elementi konacno ne sortiraju od 
najmanjeg ka najvecem. Dakle, procedura sortiranje ce se obaviti sledecim 
redoslijedom:

```text
Pocetno stanje      |  [4,2,1,5,3]  |   Objasnjnje
____________________|_______________|____________________________________
Nakon 1. iteracije  | [(2,4),1,5,3] | (4 > 2) 4 i 2 mijenjaju mjesta 
                    | [2,(1,4),5,3] | (4 > 1) 4 i 1 mijenjaju mjesta
                    | [2,1,(4,5),3] | (4 < 5) 4 i 5 ostaju na svom mjestu
                    | [2,1,4,(3,5)] | (5 > 3) 5 i 3 mijenjaju mjesta
____________________|_______________|____________________________________
Nakon 2. iteracije  | [(1,2),4,3,5] | (2 > 1) 2 i 1 mijenjaju mjesta 
                    | [1,(2,4),3,5] | (1 < 4) 2 i 4 ostaju na svom mjestu
                    | [1,2,(3,4),5] | (4 > 3) 4 i 3 mijenjaju mjesta3
                    | [1,2,3,(4,5)] | (4 < 5) 4 i 5 ostaju na svom mjestu
____________________|_______________|____________________________________
```

**`Izvorni kod: kod-321_sortiranje-mjehuricima.py`**

```python

niz_brojeva = [4,2,1,5,3] 

# inicijalno stanje varijable, koja nam govori da li je bilo 
# zamjene brojeva prilikom iteracije kroz niz
zamjena_izvrsena = True 

zadnji_element_niza = (len(niz_brojeva) - 1)

while zamjena_izvrsena:
  # predpostavimo da je niz sortiran
  zamjena_izvrsena = False

  # isijecamo poslednji element niza, jer unutar petlje provjeravamo naredni preko indeks + 1
  for indeks,broj in enumerate(niz_brojeva[0:zadnji_element_niza]):
    if niz_brojeva[indeks] > niz_brojeva[indeks+1]:
      # mijenjamo mjesta elemenata niza
      niz_brojeva[indeks],niz_brojeva[indeks+1]=niz_brojeva[indeks+1],niz_brojeva[indeks]
      zamjena_izvrsena = True
else:
  print(niz_brojeva)
```

**`Izvorni kod: kod-322_sortiranje-mjehurica-slucajni-izbor.py`**

```python
import random
niz_brojeva=[]
for i in range (10000):
  #print (random.randint(1,100))
    niz_brojeva.append(random.randint(1,10000))

print (niz_brojeva)

# niz_brojeva = [4,2,1,5,3] 

zamjena_izvrsena = True

zadnji_element_niza = (len(niz_brojeva) - 1)

while zamjena_izvrsena:
  zamjena_izvrsena = False

  for indeks,broj in enumerate(niz_brojeva[0:zadnji_element_niza]):
    #print(str(indeks) + " -> " + str(broj))

    if niz_brojeva[indeks] > niz_brojeva[indeks+1]:
      niz_brojeva[indeks],niz_brojeva[indeks+1]=niz_brojeva[indeks+1],niz_brojeva[indeks]
      zamjena_izvrsena = True

else:
  print(niz_brojeva)
```
