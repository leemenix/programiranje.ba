
<div style="page-break-after: always;"></div>

## Promjenjive i tipovi podataka

Promjenjive ili varijable su osnovni objekti podataka kojima se manipulise u programu. Recimo da zelimo 
imati promjenjivu **ime_korisnika** koju mozemo koristiti kroz citav program i koja sadrzi vrijednost **Goku**.
To bi smo mogli napisati kao:

```python
ime_karaktera = "Goku"
```
Ovo citamo kao: 
Deklarisana je promjenjiva, ciji je naziv (identifikator) **ime_karaktera** a cija je inicijalna (pocetna)
vrijednost **Goku**. 

Takodje iz navedenog primjera mozemo zakljuciti da je promjenjiva, ciji je naziv **ime_karaktera**, tekstualnog
tipa, niz karaktera ["G","o","k","u"] ili na engleskom tipa **string**. 

### Promjenjive, varijable (variables) 

Programiranje se uglavnom svodi na obradu podataka, stim u vezi je potrebno pohraniti podatke 
i organizovati ih na najbolji moguci nacin. Varijabla ili promjenjiva predstavlja lokaciju u memoriji
vaseg kompjutera i sluzi da pokaze na odredjenu vrijednost koju ta memorijska lokacija predstavlja.

Tri glavna faktora koji cine promjenjivu/varijablu jesu: 

- naziv, 
- operator i 
- vrijednost varijable

```text
naziv   |    operator     | vrijednost
        |  pridruzivanja  |
________|_________________|____________
ime     |       =         |   "Goku"
________|_________________|____________
godine  |       =         |     23
        |                 |
```

#### Gradjenje varijable
- naziv varijable ne smije poceti sa brojem
- naziv varijable moze poceti, malim, velikim slovima ili donjom crticom (_)
nakon cega moze ici broj
- mala i velika slova se razlikuju (a != A)


**`Izvorni kod: kod-155_naziv-varijabli.py`**

```python
ime = "Goku"
godine = 16
_nove_godine = 18
25_godine = 25 # ovde cemo dobiti gresku
a = 3
A = 4
print (ime)
print (godine)
print (_nove_godine)
print (25_godine) # ovde cemo dobiti gresku
print (a)
print (A) 
```

**`Izvorni kod: kod-156_prakticna-primjena-varijabli.py`**

```python
karakter_1 = "Son Goku"
karakter_2 = "Krilin"
godine = "17"

print("U dalekoj proslosti zivio je djecak po imenu Goku.")
print("Goku je imao 15 godina.")
print("Volio je upoznavati nove karaktere ")
print("i imao je najboljeg druga po imenu Krilin!")
print (" ")
print("U dalekoj proslosti zivio je djecak po imenu " + karakter_1)
print(karakter_1 + " je imao " + godine + " godina.")
print("Volio je upoznavati nove karaktere ")
print("i imao je najboljeg druga po imenu " + karakter_2)
# Veoma korisna funkcija type() sluzi nam da odredimo kog tipa je neka promjenjiva tokom razvoja programa. 
print(type(karakter_ime))
#godine = 17
print(type(godine))
```

### Tipovi podataka

```text
    tipovi podataka   |    python sintksa    |       objasnjenje
______________________|______________________|_________________________
     Tekstualni       |       string()       |  operacije nad znakovnim
(string - niz znakova)|                      |     tipovima podataka 
                      |                      |            
______________________|______________________|_________________________
      Brojevi         |                      |  
  cijeli, realni      |        int()         |  pretvara u cijeli broj 
 (integer, float)     |                      |     (npr. 1,10,33)
                      |______________________|_________________________
                      |       float()        |  pretvara u realni broj
                      |                      | (npr. 1.0, 3.14, 33.333)
______________________|______________________|_________________________
      Logicki         |                      |
   tacno, netacno     |        bool()        |  operacije nad logickim 
(boolean True/False)  |                      |    tipovima podataka 
                      |                      |      (True i False)
______________________|______________________|_________________________
```

#### Mijenjanje tipova promjenjive (kastovanje)

Primjenjiva moze mijenjati tip kroz izvrsavanje programa, sto se jos naziva i kastovanje (casting). 

**`Izvorni kod: kod-157_tipovi-podataka.py`**

```python
karakter_ime = "Goku"
karakter_godine = 15
karakter_visina = 168.5
karakter_osobina_dobar = True
karakter_osobina_los = False

print(karakter_ime + " ima " + karakter_godine)
print(karakter_ime + " ce za godinu dana imati " + karakter_godine + 1)
print(karakter_ime + " je visok " + karakter_visina + "cm.")
print(karakter_ime + " ce za godinu dana biti visok " + (karakter_visina + 5) + " cm.")
print(karakter_ime + " je dobar karakter" + karakter_osobina_dobar)
print(karakter_ime + " je los karakter" + karakter_osobina_los)

karakter_ime = "Goku"
karakter_godine = 15
karakter_visina = 164.5
karakter_osobina_dobar = True
karakter_osobina_los = False

print(karakter_ime + " ima " + str(karakter_godine))
print(karakter_ime + " ce za godinu dana imati " + str(karakter_godine + 1))
print(karakter_ime + " je visok " + str(karakter_visina) + " cm.")
print(karakter_ime + " ce za godinu dana biti visok " + str(karakter_visina + 5) + " cm.")
print(karakter_ime + " je dobar karakter " + str(karakter_osobina_dobar))
print(karakter_ime + " je los karakter " + str(karakter_osobina_los))
```
