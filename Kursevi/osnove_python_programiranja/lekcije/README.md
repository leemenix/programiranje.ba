### Python 3 - Uvod u programski jezik Python
- jednostavan za ucenje

- kurs je dizajniran za sto jednostavnije ucenje

- citavo vrijeme cete biti vodjenji

#### Par rijeci o Python programskom jeziku

Python je programski jezik opste namjeni, dinamicki typed i interpretiran, objektno orjentisan programski jezik kreiran u kasnim 80-tim od strane
 Guido van Rossum.

Dizajn filozofija Python-a se svodi na jednostavnu citljivost, dakle u prvom planu ima za cilj sto lakse citanje i pisanje koda. Ovo se postize koristenjem
 white-space to deliniate code blocks umjesto vec dobro poznatog i ustaljenog nacina koristenja uglastih zagrada _{}_ i tacka zareza _;_.

##### Kako pokrenuti Python
Generalno sav python kod se pokrece koristenjem interpretera. Najpopularniji i orginalni interpreter je CPython, zato sto je implementiran u C programskom
jeziku. Takodje, postoji i par drugih interpretera, a mnogi od njih su implementirani u razlicitim jezicima od C-a, kao sto su Java ili C# (C sharp).

Najcesce koristen interpreter CPython, koristi automatski garabage koletor (sakupljac smeca :), kako bi obezbijedio nesmetano  i efikasno upravljenje 
 memorijom kompjutera. Python je siroko poznat po usvajanju ne tradicionalne, minimalne sintakse, bazirane na  white space, i dizajnu koju tezi cistom i 
 citljivom kodu.

##### Verzije Python-a
Prije samo par mjeseci (pisano Feb. 2020), ako biste htjeli instalirati Python na vasem racunaru, dosli biste u konfuznu situaciju, jer Python, za razliku
od mnogih drugih programskih jezika, ima dvije glavne (major), ne kompatibilne verzije koje su podjednako u sirokoj upotrebi

Python verzije 2.7.3, released u 2012, je zadnja verzija popularnog Python-a 2 koji je released. Ova verzija je uglavnom u potpunosti kompatibilna unazad sa svim prethodnim verzijama.

Godine 2008, kreator, Guido van Rossum odlucio je da ocisti Python bazu (codebase) i overhall dosta drugih stvari u Python 2 koje mu se nisu svidjale, s toga je kreirao Python 3.

Python 3 je prihvatan ali veoma oprezno i polako na pocetku, najvise iz razloga sto nije kompatibilan unazad sa prethodnom verzijom Python 2, i zato je 
postojao ogroman eko-sistem biblioteka napisanih za Python 2 koje nece raditi sa novom verzijom Python-a 3.

Ovih dana Python 3 eco-sistem je uveliko pohvatao i izjednacio se sa prethodnom verzijom, sto nas dovodi do zakljucka da je Python 3 logicni izbor za sve 
nove developere koji planiraju uciti ovaj programski jezik. Python 3 je verzija koju cemo ujedno obraditi u ovom kursu.

#### Priprema radnog okruzenja

##### Izbor editora teksta i **Integrisanog razvojnog okruzenja** IDE (Integrated Development Environment)

###### Izbor tekst editora
Za pocetnike, se preporucuje koristenje nekog jednostavnog tekst editora kao Notpad++, Sublime, VisualStudio Code ...

###### Izbor Interisanog razvojnog okruzenja
Vecina programera odabere pisanje Python koda, koristenjem specijalnog integrisanog razvojnog okruzenja. Trenutno tri najistaknutija za Python su 
 Eclipse, PyCharm i Netbeans.

##### Windows

- PyCharm installation (Win, Linux)

- Sublime installation, notpad ++
  - mi cemo koristiti PyCharm - IDE (Integrated Development Environment) 

- python 2 (legacy), python 3 (future)
  - razlika u sintaksi


- podesavanje PyCharm-a i nas prvi program
  - promjena teme, odredisnog direktorija, velicine fonta i sl.
  - New -> Python File ...
#### Zdravo Svijete

- pozdrav_svijete.py

```python      
print("Zdravo Svijete!")
```

- dva nacina za pokretanje Python programa i kada koji koristiti
- cmd, terminal - (ako nesto zelimo da provjerimo brzo i trenutno)
- direktno iz IDE-a (precice) - (kada pisemo vise linija koda)

- drugi program
- programiranje je davanje instrukcija kompjuteru (kroz programski jezik) 
- crtanje_oblika.py (priprema za igricu vjesala)

```python
print("_______")
print("|     ?")
print("|      ")
print("|      ")
print("|      ")
```

- u ovom slucaju python ide liniju po liniju i izvrsava kod
- sta se desava u slucaju da zamijenimo prvu i zadnju liniju?

Zadaci za samostalni rad!
- napisati program koji ispicuje vase Ime i prezime
- napisati program koji crta pravougaonik oblika
```python
__________
|         |
|         |
|_________|
```
- napisati program koji crta trougao oblika
```python
    /\
   /  \
  /    \
 /      \
/________\
```

#### komentarisanje koda
- upisavanje podsjetnika
- komentarisanje koda
- preporuka da se koristi taraba
# ovo je taraba (hash tag) simbol
# komentari su po default-u ignorisani u python-u
```python
'''
Viselinijski komentar
'''
"""
Viselinijski komentar
"""
print("Komentari su korisni")
# print("Ova linija koda nece biti ispisana")
```

#### Promjenjive i tipovi podataka

##### Promjenjive, varijable (variables) 

- programiranje se uglavnom svodi na obradu podataka, stim u vezi je potrebno pohraniti podatke 
i organizovati ih na najbolji moguci nacin. postoji nesto sto se zove CRUD (Create,Read, Update, Delete)

- tri glavna faktora koji cine promjenjivu/varijablu jesu
naziv, operator i vrijednost varijable

naziv | operator | vrijednost

ime        =        "Darko"

godine     =           23

- gradjenje varijable
- naziv varijable ne smije poceti sa brojem
- naziv varijable moze poceti, malim, velikim slovima ili donjom crticom (_)
nakon cega moze ici broj
- malo a i veliko A se razlikuju (a != A)


naziv_varijabli.py
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

- prakticna_primjena_varijabli.py - (Dragon Ball - Zmajeva Kugla)
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
```

##### Tipovi podataka

- Znakovni (string)
- string()
- Brojevi cijeli, realni (integer, float)
- int()
- float()
- Logicki tacno, netacno (boolean True/False)
- bool()

- korisna funkcija type
print(type(karakter_ime))

tipovi_podataka.py
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

##### Rad sa stringovima
- tekst, rad sa tekstom, funkcije nad stringovima

rad_sa_stringovima.py

```python
print("programiranje.ba besplatni online kursevi")

# escape karakter \
print("programiranje.ba \n besplatni online kursevi")

sajt_naziv = "programiranje.ba"
sajt_slogan = " besplatni online kursevi"
print(sajt_naziv)
print(sajt_slogan)
print(sajt_naziv + sajt_slogan)
print(sajt_naziv.upper() + sajt_slogan.upper())
print(sajt_naziv.isupper())
print(len(sajt_naziv))
# index stringa pocinje na poziciji 0
print(sajt_naziv[4])
# index funkcija i proslijedjivanje parametara
print(sajt_naziv.index('g'))
print(sajt_naziv.index('mira'))
#print(sajt_naziv.index('h'))

print(sajt_slogan.replace("kursevi","tutoriali").upper())

print("{1}, {0}".format(sajt_naziv, sajt_slogan))
print(f"{sajt_naziv} {sajt_naziv}")

### char i ord kasnije potrebni za cezarovu sifru 
```

##### Rad sa brojevima
- brojevi, rad sa brojevima, funkcije nad brojevima

```python
print(3)
print(-4)
print(3.333)
print(7+3)
print(7+3.333)
print(8/4)
print(2*4)
print (2*(4+5))
# modulo , ostatak 9 mod 4
print(9%4)

moj_broj = 13
print(moj_broj)
print("Moj omiljeni broj" + str(moj_broj))

# math funkcije, funkcije su vec pripremljen kod koji odradjuje posao za nas
broj = -2
print(abs(broj))
print(pow(4,2))
print(max(5,10))
print(min(3,6))
print(round(3.3333))
print(round(3.6))
print(round(3.5))

# import math modul (import math funkcije vise kada budemo pricali o modulima)
from math import *
print(floor (3.6))
print(ceil(3.6))
print(sqrt(9))
```

##### Ulaz/upis podataka, prihvacanje podataka od korisnika

```python
input() # hej ti, cekam da uneses neku informaciju podatak
input("Unesite vase ime: ")
korisnik_ime = input("Unesite vase ime: ")
print("Zdravo, " + korisnik_ime + " dobrodosli.")

korisnik_ime = input("Unesite vase ime: ")
korisnik_godine = input("Unesite vase godine: ")
print("Zdravo, " + korisnik_ime + ". Vi imate " + korisnik_godine + " godina.")

# vjezba ispisati preghodni program koristeci funkciju format
```

osnovni_kalkulator.py

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


interaktivni_karakter_program.py
```python
print("U dalekoj proslosti zivio je djecak po imenu Goku.")
print("Goku je imao 15 godina.")
print("Volio je upoznavati nove karaktere ")
print("i imao je najboljeg druga po imenu Krilin!")

karakter_ime = input("Unesite ime karaktera: ")
karakter_godine = input("Unesite godine karaktera: ")
karakter_prijatelj = input("Unesite ime najboljeg prijatelja: ")

print(f"U dalekoj proslosti zivio je djecak po imenu {karakter_ime}.")
print(f"{karakter_ime} je imao {karakter_godine} godina.")
print(f"Volio je upoznavati nove karaktere ")
print(f"i imao je najboljeg druga po imenu {karakter_prijatelj}!")
```

##### Liste - []
- rad sa listama, velik broj podataka (organizacija i pracenje podataka)
```python
karakteri = ["Goku", "Krilin", "Bulma", "Chi-Chi", "Yamcha", "Picolo"]
print(karakteri)

##### mozete smjestiti stringove , brojeve, boolean u liste
##### referenciranje po indexu, ako zelimo pristupiti elementu unutar liste
print(karakteri[0])
print(karakteri[4])

print(karakteri[-1])
print(karakteri[-2])

print(karakteri[1:])
print(karakteri[2:4])
print(karakteri[2:-2])

##### izmjena elemenata u listi
karakteri[4] = "Master Roshi"
print(karakteri[4])
print(karakteri)
```

##### funkcije nad listama
```python
karakteri = ["Goku", "Krilin", "Bulma", "Chi-Chi", "Yamcha", "Picolo"]
print(karakteri)
loto_brojevi = [4, 7, 3, 10, 32]
print(loto_brojevi)

karakteri.extends(loto_brojevi)
print(karakteri)

karakteri.append("Majin Buu")

print(karakteri)

karakteri.insert(2, "Vegeta")
print(karakteri)

karakteri.remove("Majin Buu")
print(karakteri)

karakteri.pop()
print(karakteri)

karakteri.clear("")
print(karakteri)

##### provjeri da li je odredjeni element u listi

karakteri = ["Goku", "Krilin", "Bulma", "Chi-Chi", "Yamcha", "Picolo", "Bulma"]
print(karakteri)

print(len(karakteri))

print(karakteri.index("Bulma"))

print(karakteri.count("Bulma"))

karakteri.sort()
print(karakteri)

karakteri.reverse()
print(karakteri)

karakteri_novi = karakteri.copy()

print(karakteri_novi)

karakteri_novi.sort()
print(karakteri_novi)
```

#### - Tuples (tip podaktovne strukture, veoma slican listama) - ()
- razlike od liste
- immutable (ne mogu se mijenjati) za razliku od listi

koorinate.py

koordinate = (4, 5)
print(type(koordinate))
print (len(koordinate))
print(koordinate.index(5))
print(koordinate[0])
print(koordinate[1])

koordinate[1] = 10 # dobicemo gresku

##### list of tuples
koordinate = [(4,5), (6,3), (7.4)]
print(type(koordinate))

print(len(koordinate))

#### Rijecnik - Dictionaries - {}
- standardni rijecnik koji imamo ima strukturu rijec i detaljno objasnjenje rijece
  gdje rijec predstavlja kljuc (key), vrijednost (value) predstavlja definiciju
  key mora biti jedinstven

Jan -> Januar
Mar -> Mart

konverzijaMjeseci = {
    "Jan": "Januar",
    "Feb": "Februar",
    "Mar": "Mart"
}

print(konverzijaMjeseci["Jan"])
print(konverzijaMjeseci["Feb"])
print(konverzijaMjeseci["Mar"])

print(konverzijaMjeseci.get("Jan"))
print(konverzijaMjeseci.get("Dec"))
print(konverzijaMjeseci.get("Dec","Nije validan kljuc"))
Funkcije
skup kodova koje odradjuju odredjene zadatke
dobri su za organizaciju koda

kako kreirati funkcije

zdravo_svijete_funkcija.py

# kad god se pojavi def na pocetku, python zna da korisnik zeli kreirati funkciju
```python
def zdravo_svijete():
  print("Zdravo Svijete.")

# moramo pozvati funkciju ako zelimo da je izvrsimo
zdravo_svijete()

def zdravo_svijete():
  print("Zdravo Svijete.")

print("Prije funkcije")
zdravo_svijete()
print("Nakon funkcije")

# prosledjivanje parametara funkciji

def zdravo_svijete(ime):
  print("Zdravo " + ime)

# moramo pozvati funkciju ako zelimo da je izvrsimo
zdravo_svijete("Goku")
zdravo_svijete("Krilin")

def zdravo_svijete(ime,godine):
  print("Zdravo " + ime + " vi imate " + str(godine))

# moramo pozvati funkciju ako zelimo da je izvrsimo
zdravo_svijete("Goku", "15")
zdravo_svijete("Krilin", "16")

# primjer funkcije sa korisnickim unosom
korisnik_ime = input("Unesite ime : ")
def pozdrav(ime):
    print ("Zdravo " + ime)

pozdrav(korisnik_ime)
```

#### - Return izraz/direktiva statement  
- kada zelimo dobiti povratnu informaciju iz funkcije koristimo return direktivu
- kada zelimo da funkcije mogu medjusobno komunicirati

2 na trecu
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

##### - operatori poredjenja i uslov if (>,<, >=, <=, ==, !=)

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

##### kalkulator_nadogradjena_verzija.py
osnovni_kalkulator.py
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

#### while petlja 
- struktura u python koja nam omogucava da prolazimo kroz isti kod vise puta, onoliko puta
koliko smo to zadali inicijalnim uslovom
- kroz svaku od iteracija kroz kod while ce da izvrsi sve sto je unutar while petlje

while_brojac.py
```python
i = 1
while i <= 10:
  print("Vrijednost i je : " + i)
  #i = i + 1
  i += 1

print("Kraj brojaca")
```

igra_pogadjanja.py - primjenimo sve do sad nauceno
```python
tajna_rijec = "python"

pokusaj = ""

while guess != tajna_rijec:
  pokusaj = input("Pokusajte pogoditi tajnu rijec: ")

print("Cestitamo, pogodili ste")

# limitiraj broj pogresnih pokusaja
tajna_rijec = "python"
pokusaj = ""
pokusaj_broj = 0
pokusaj_limit = 4
kraj_igre=False

while pokusaj != tajna_rijec and not(kraj_igre):
if pokusaj_broj < pokusaj_limit:
    pokusaj = input("Pokusajte pogoditi tajnu rijec: ")
    pokusaj_broj += 1
else:
    kraj_igre = True

if kraj_igre:
    print("Iskoristili ste sve pokusaje. Kraj igre")
else:
    print("Cestitamo, pogodili ste")
```

### for petlja
- specijalni tip petlje u python-u
```python
for slovo in "programiranje.ba":
  print(slovo)

for karakter in karakteri:
  print(karakter)

karakteri = ["Goku", "Kirlin", "Yamcha"]
for indeks in range(len(karakteri)):
  print (karakteri[indeks])

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

### eksponencijaln funkcija - kada ne znamo koliko je eksponent
print(2**3)

def eksponent_broja(baza, eksponent):
  rezultat = 1
  for index in range(exponent):
    rezultat = rezultat * baza
  return rezultat

print(exponent_broja(2,4))
```
#### dvodimenzionalne liste i ugnijezdene petlje (nested)
```python
resetka = [
    [1, 2, 3],
    [4, 5, 6],
    [7 ,8 ,9],
    [0]
]

print(resetka[0][2])
print(resetka[2][1])
print(resetka[3][0])

# nested for loop

# resetka = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7 ,8 ,9],
#     [0]
# ]

for row in resetka:
  for col in row:
    print(col)

for col in resetka:
    for row in col:
        print(row)
    
# cezarova sifra u python
def enkripcija(tekst, pomak):
  rezultat = ""

  for broj in range(len(tekst)):
    slovo = tekst[broj]
    
  if(slovo.isupper()):
    rezultat += chr((ord(slovo) + pomak - 65) % 26 + 65)
  else: 
    rezultat += chr((ord(slovo) + pomak - 97) % 26 + 65)
  return rezultat

tekst = input("Unesite tekst: ")
pomak = 2

print("Unijeli ste: " + tekst)
print("Pomak: " + str(pomak))
print("Sifrovan tekst: " + enkripcija(tekst, pomak))
```

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

#### citanje iz eksternog fajla
- dosta puta imamo potrebu za citanjem sadrzaja iz drugih fajlova
- parsiranje teksta ...
- apsolutni, relativna lokacija

karakteri_porijeklo.txt
```python
Goku - Sayan
Krilin - Zemlja
Piccolo - Namek
Frieza - Universe 7

# r - read; w - write; a - append to end of file; r+ - read and write
# otvoren fajl
karakteri_fajl = open("karakteri_porijeklo.txt", "r")

# provjeri da li je fajl citljiv
print(karakteri_fajl.readable())

# citanje informacija iz fajla
print(karakteri_fajl.read())

# citanje linije u fajlu
print(karakteri_fajl.readline())
print(karakteri_fajl.readline())
print(karakteri_fajl.readline())
print(karakteri_fajl.readline())

# citanje linije po liniju, citaj svaku liniju i pohrani u niz
print(karakteri_fajl.readlines())

# koristenjem for petlje
for karakter in karakteri_fajl.readlines():
  print(karakter)

karakteri_fajl.close()
```

### upisivanje u eksterni fajl
```python
karakteri_fajl = open("karakteri_porijeklo.txt", "a")

karakteri_fajl.write("Bulma - Zemlja")
karakteri_fajl.write("\n Chi-Chi - Zemlja")

karakteri_fajl.close()

### upisivanje u eksterni fajl

karakteri_fajl = open("karakteri_porijeklo_novi.txt", "w")

karakteri_fajl.write("Bulma - Zemlja")
karakteri_fajl.write("\n Chi-Chi - Zemlja")

karakteri_fajl.close()
```

#### modules and pip 
- python fajl koji mozete importovati unutar vaseg python koda
- kako kreirati svoj modul
- kako instalirati module (list of python modules on google) pip paket manager
- build-in moduli (ugradjeni) i eksterni moduli
 
korisni_alati.py
```python
#
import random

def srecan_broj(broj):
    return random.randint(1, broj)

def pozdrav(tekst):
    return ("Pozdrav " + tekst)

##
import korisni_alati

print(korisni_alati.srecan_broj(3))
print(korisni_alati.pozdrav("Goku"))

##
from korisni_alati import *

print(srecan_broj(3))
print(pozdrav("Goku"))

##
import korisni_alati as ka

print(ka.srecan_broj(3))
print(ka.pozdrav("Goku"))

## how to install with pip
## how to import and use modules
```

#### klase i objekti
- ekstremno korisni , organizovan i mocniji
- kada radimo sa programiranjem susrecemo se sa razlicitim tipovima podataka
- takodje susrecemo se sa razlicitim strukturama podataka
- sta u slucaju kad ne mozemo predstaviti neku pojavu iz prirode sa vec postojecim tipovima 
  ili strukturama podataka
- u python-u mozemo krairati klase (definise vas licni tip podatka, ponasa se kao template, patern
  kako nesto treba da izgleda)
- objekat je podatak u memoriji, pravi podatak kreiran iz klase

student.py
# posto ne postoji student tip podaka, kreiracemo klasu student
Student.py
```python
class Student:
  # inicijalizacija klase (inicijalna funkcija)  
  def __init__(self, ime, smjer, ocjena, brucos):
    self.ime = ime
    self.smjer = smjer
    self.ocjena = ocjena
    self.brucos = brucos
```

main.py
```python
from Student import Student

# kreiranje student_prvi objetka
student_prvi = Student("Darko", "Programiranje", 8, False)
print(student_prvi)
print(student_prvi.ime)
print(student_prvi.ocjena)

student_drugi = Student("Dragan", "Ekonomija", 8.3, True) 
print(student_drugi.brucos) 
```

##### funkcije unutar klase (funkcije objekta)
```python
class Student:
  def __init__(self, ime, smjer, ocjena, brucos):
    self.ime = ime
    self.smjer = smjer
    self.ocjena = ocjena
    self.brucos = brucos

  def dobar(self):
    if self.ocjena >= 7:
      return True
    else:
      return False
```
#### naslijedjivanje
- u slucaju da imamo klasu, kada kreiramo novu klasu mozemo naslijediti staru klasu
- nova klasa ce imati sve osobine stare klase sa novim opcijama

Kuvar.py
```python
class Kuvar:
    def priprema_mesa(self):
        print ("Priprema pileceg mesa.")

    def priprema_salate(self):
        print("Pirprema Cezar salata")

    def priprema_specijalnog_jela(self):
        print("Priprema rebarcadi")
```
KineskiKuvar.py
```python
from Kuvar import Kuvar

class KineskiKuvar(Kuvar):
    def priprema_rize(self):
        print("Priprema rize na kineski nacin")

    def priprema_specijalnog_jela(self):
        print ("Pekinska patka")
```
main.py
```python
from Kuvar import Kuvar
from KineskiKuvar import KineskiKuvar

novi_kuvar = Kuvar()

novi_kuvar.priprema_mesa()
novi_kuvar.priprema_specijalnog_jela()

novi_kineski_kuvar = KineskiKuvar()

novi_kineski_kuvar.priprema_rize()
novi_kineski_kuvar.priprema_mesa()
novi_kineski_kuvar.priprema_specijalnog_jela()
```

devet_depresivaca.py - (Rambo Amadeus - Devet depresivaca)

```python
print("9 depresivaca gajili su bostan")
print("Puko lastik od bandzija, ostalo ih 8")

print("8 depresivaca, k'o u dlan ih gledam")
print("u krivini hladnjaca, ostalo ih 7")

print("7 depresivaca, opet losa vijest")
print("Neuzemljen bojler, ostalo ih 6")

print("6 depresivaca, turbulentan let")
print("Dnevno kilo vinjaka, ostalo ih 5")

print("5 depresivaca bez mrlje na jetri")
print("Moca od pecenja, ostalo ih 4")

print("4 depresivca, veseli su svi")
print("Droga jeftinija od viskija, ostalo ih 3")

print("3 depresivca, svaki od njih vrijedan")
print("Dvojici crko facebook, ostao je 1")

print("1 depresivac, oprezan je bio")
print("Onda se ozenio")
```
# import turtle
# # from turtle import Tkinter
# import tk as Tkinter


# fred = turtle.Pen()
# fred.shape("turtle")
# fred.forward(100)
# fred.circle(100)
# fred.color("blue")
# fred.circle(-100)
# fred.forward(100)
# Tkinter.mainloop()


import time
import turtle
import tk as Tkinter
from turtle import Turtle # specijalna funkcija Turtle (Kornjaca)
from random import randint # random integer (slucajni cijeli broj)

# kreiranje prozora
window = turtle.Screen()
window.title=("Trke Kornjaca")


turtle.bgcolor("forestgreen")
turtle.color("white")
turtle.speed(0) # prikazi odmah
turtle.penup() # kretanje kornjace u drugim pozicijama, trenutno je kornjaca na poziciji x,y = [0,0]
turtle.setpos(-140, 200) # x lijevo, y gore
turtle.write("Trke Kornjaca", font=("Arial", 30, "bold"))
turtle.penup()

# zemlja oko staze, dekoracija
turtle.setpos(-400, -180)
turtle.color("chocolate")
turtle.begin_fill() # popuni oblik bojom
turtle.pendown()
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.end_fill()

# finish linija
stamp_size = 20
square_size = 15
finish_line = 200

turtle.color("black")
turtle.shape("square")
turtle.shapesize(square_size / stamp_size)
turtle.penup()

for i in range (10):
    turtle.setpos(finish_line, (150 - (i * square_size * 2)))
    turtle.stamp()

for j in range (10):
    turtle.setpos(finish_line + square_size, ((150 - square_size) - (j * square_size * 2)))
    turtle.stamp()

turtle.hideturtle()

# class nova_kornjaca:
# 	def __init__(self,speed,color,shape,penup,goto):
# 		self.speed = speed
# 		self.color = color
# 		self.shape = shape
# 		self.penup = penup
# 		self.goto = goto
		

kornjaca1 = Turtle()
kornjaca1.speed(0)
kornjaca1.color("black")
kornjaca1.shape("circle")
kornjaca1.penup()
kornjaca1.goto(-250, 100)
kornjaca1.penup()
# kornjaca1 = nova_kornjaca(0,"black","turtle","","-250, 100")


# kornjaca 2
kornjaca2 = Turtle()
kornjaca2.speed(0)
kornjaca2.color("cyan")
kornjaca2.shape("turtle")
kornjaca2.penup()
kornjaca2.goto(-250, 50)
kornjaca2.penup()


# kornjaca 3
kornjaca3 = Turtle()
kornjaca3.speed(0)
kornjaca3.color("yellow")
kornjaca3.shape("turtle")
kornjaca3.penup()
kornjaca3.goto(-250, 0)
kornjaca3.penup()


# kornjaca 4
kornjaca4 = Turtle()
kornjaca4.speed(0)
kornjaca4.color("magenta")
kornjaca4.shape("turtle")
kornjaca4.penup()
kornjaca4.goto(-250, -50)
kornjaca4.penup()

# kornjaca 5
kornjaca5 = Turtle()
kornjaca5.speed(0)
kornjaca5.color("blue")
kornjaca5.shape("turtle")
kornjaca5.penup()
kornjaca5.goto(-250, -100)
kornjaca5.penup()

time.sleep(1)

# pokreni kornjace
for i in range(145):
    kornjaca1.forward(randint(1,5))
    kornjaca2.forward(randint(1,5))
    kornjaca3.forward(randint(1,5))
    kornjaca4.forward(randint(1,5))
    kornjaca5.forward(randint(1,5))

turtle.exitonclick()

Tkinter.mainloop()from random import *
import time
import sys
 
reel_1 = ''
reel_2 = ''
reel_3 = ''
bank = 0
current_bet = 0
spin_count = 0 # For Testing Purposes
total_won = 0
total_lost = 0
def slow_reel(reel1, reel2, reel3):
    for symbol in (reel_1,reel_2,reel_3):
        sys.stdout.write(symbol)
        sys.stdout.flush()
        time.sleep(0.1)
slow_reel(reel_1, reel_2, reel_3)
def game_loop():
    global reel_1, reel_2, reel_3, bank, current_bet, spin_count, total_lost, total_won
    if bank <= 0:
        print("GAME OVER LOSER!")
    while bank > 0:
        if current_bet > 0 and bank >= current_bet:
            bet_r = input("\n[ENTER] TO REPEAT BET, 'NO' TO PLACE NEW ONE: ")
            if bet_r == "" or bet_r == "Y":
                bet = current_bet
            else:
                current_bet = 0
                bet = 0
                game_loop()
        else:
            try:
                bet = int(input("PLACE YOUR BET!: "))
            except ValueError:
                return game_loop()
 
        if bet >= 0 and bank >= bet:
            bank -= bet
            total_lost += bet
            current_bet = bet
            try:
                reel1 = ['!', '@', '@', '#', '#', '#', '&', '&', '&', '&', '%', '%', '%',
                '%', '%']
                reel2 = ['!', '@', '@', '#', '#', '#', '&', '&', '&', '&', '%', '%', '%',
                '%', '%']
                reel3 = ['!', '@', '@', '#', '#', '#', '&', '&', '&', '&', '%', '%', '%',
                '%', '%']
                reel_1 = choice(reel1)
                reel_2 = choice(reel2)
                reel_3 = choice(reel3)
                print("\n-----SPINNING FOR: ${}-----\n".format(current_bet))
                for c in reel_1:
                    time.sleep(0.4)
                    print(" (","<",c,">", end=" | ", flush=True)
                for c in reel_2:
                    time.sleep(0.8)
                    print("<",c,">", end=' | ', flush=True)
                for c in reel_3:
                    time.sleep(1.0)
                    print("<",c,">", end=' )', flush=True)
                    time.sleep(1.5)
                print("\n")
                print("----------------------------")
                spin_count += 1
 
                if reel_1 == '!' and reel_2 == '!' and reel_3 == '!':
                    bank += 100 * current_bet
                    total_won += 100 * current_bet
                    print("YOU WON THE JACKPOT!!!: $",100 * current_bet)
                    print(spin_count) # Testing Odds
                    exit(0) # So I Can Easily Tell When JACKPOT Is Won
                elif reel_1 == '@' and reel_2 == '@' and reel_3 == '@':
                    bank += 50 * current_bet
                    total_won += 50 * current_bet
                    print("YOU WON!!: $",50 * current_bet)
                elif reel_1 == '#' and reel_2 == '#' and reel_3 == '#':
                    bank += 20 * current_bet
                    total_won += 20 * current_bet
                    print("YOU WON!!: $",20 * current_bet)
                elif reel_1 == '&' and reel_2 == '&' and reel_3 == '&':
                    bank += 10 * current_bet
                    total_won += 10 * current_bet
                    print("YOU WON!!: $",10 * current_bet)
                elif reel_1 == '%' and reel_2 == '%' and reel_3 == '%':
                    bank += 5 * current_bet
                    total_won += 5 * current_bet
                    print("YOU WON!!: $",5 * current_bet)
                elif reel_1 == '%' and reel_2 == '%':
                    bank += current_bet
                    total_won += current_bet
                    print("YOU WON!!: $",current_bet)
                elif reel_1 == '%' and reel_3 == "%":
                    bank += current_bet
                    total_won += current_bet
                    print("YOU WON!!: $", current_bet)
                else:
                    pass
                print("\nYour Statistics")
                print("Won: $", total_won, "Spent: $", total_lost, "\nCurrent Balance: $", bank)
            except (Exception):
                pass
def start():
    global bank
    print("\nWelcome to Python Slots")
    command = input("YOU START WITH $10,000! \n\nPRESS [ENTER] TO BEGIN ")
    if command == "":
        bank = 10000
        game_loop()
    else:
        print("ALL YOU HAD TO DO WAS PRESS ENTER")
        start()
 
start()RIFF¦  WAVEfmt      D¬  ˆX     fact       data0  
 öÿíÿrÿ°ÿÜÿŸÿÒÿ±ÿÆÿšÿ’ÿ«ÿœÿÂÿÒÿáÿ¦ÿ£ÿÒÿµÿÏÿ¼ÿ¹ÿèÿšÿíÿåÿÁÿÊÿ¹ÿúÿ×ÿØÿ×ÿåÿËÿ¾ÿÜÿİÿ ´ÿÏÿ 
 3 wé ¹üdşw:1`:h†DrsÊ‡¨ÆŸì£s¬1´ø·«´\¬Ò¦±©s±|µ±±S«ì©È®õ³u³·®k«V­²N´Q±g­7­¹°¡³á²»¯®á¯ä²å³Ê±¯ú¯²Õ³ş²K±^° ±é³´~²O±ä±j³?´Ñ³‘²h²”³©´½´­³ø²Œ³Ò´mµ¹´û³Ô³ö´µMµÑ´²´<µàµ-¶êµwµ[µ!¶±¶¶úµ
¶e¶ ·^·Ğ¶£¶Û¶9·˜·ƒ·¦·…·ã·'¸¸¸¸G¸‡¸Ô¸¸¸¥¸ì¸0¹!¹9¹J¹D¹l¹«¹Ş¹Ç¹Ï¹Ì¹ºHº7ºoº»¼6½á½¡½R¾ÈæEşUÛ}è~#b`FFñ\Xp¶lY1MyUOfNk_èQ÷Q_>hdcõV—QY˜c·dÓ[·SMU^Èb{^_V&T»Yú_’_YYUÓV\_A["VIULYô\ß[»W;U6W²Z[ªX‘UÂU‹XtZXYV'UºV­XÑX¼VİT`UXW8X!WSUÃT÷U WÄVhUqTÀT÷U>VzU*TæSúT‹UûT4TuS¸SUT‚T²SîRêRYSÆS}S±R,R‰RSïRƒRëQìQR[RRvQ.QlQ¯Q€Q:QÔPûPCQ&QGP6OçM1MLM M[Fñ.z YÄâ“ş†¥°¾VÈ]µŸ?šÕ«©¼¨¹±¨¬º¦-¶Çºç¯Á£¤y°'¹µò©*¥¬·µõ¶ê®ó§÷©ÿ±Ä¶Ñ²Š«Ö©C¯(µÒ´4¯a«»­0³µZ²û­°­©±µ4´š°•®¶°"´µµ²ç¯A°4³,µo´²±“²½´µP³²±{²¤´Ÿµ´:³³V´±µ…µb´»³l´ÖµI¶„µÆ´Ö´¼µ½¶h¶¡µVµúµ·(·¶¶7¶è¶§·Œ·Ú¶­¶@·¸,¸Î·q·“·Z¸•¸y¸,¸_¸Ê¸C¹¹´¸¹}¹’ºU»)¼u¼Ÿ¼¨ÀÒåøP1ÅfÿtZUCC¹L!d’oªdKRœMBZßg¹fôXÍOUafÇ]gSmRb[ôbL`WgRWé^m`8ZTßTíZ_,\üUÁS¢WX\`\ÛW-T‡U²Y›[éX!UbT7WêY@Y.V0TdUXÒX¿VƒT]TkVÃWüVãTÑSËT©VáV!U¦SáS6UÜU&UÛS>STõTÇT”SÙRSÛSDTtSŸR^RÇRYSS1RšQµQrR›RàQgQZQôQRÃQ"Q²PÕP"QQ®P1PPmP‹PeP¹OºOóOÖOwOÅNÁM§LãK/LKi@¯ îé­ÿˆÔŒp¬¿ÅâÁ©š—É†³½Ö±2¡æi¬¹v¶¬¨7¡È§´°·×®&¥Í¥a¯‚¶	³ ªU¦ÿ«õ³Å´M®‘¨ª±µÙ±ó«ÊªÙ®®³™³1¯*¬ı­x²E´‰±®Ï­è°Ş³³P°§®U°-³ì³Ö±ì¯m°³ µ?´©²W²ù³êµ7¶@µ[´ÿ´¸¶Ö·p·p¶’¶ã·%¹m¹Ø¸‹¸l¹[ºşº»º‘º¥º»›¼¼¼x¼~¼&½¾•¾w¾¾¾„¿á¿À8ÀHÀÌÀÆÁÕÁ·ÁÿÁiÂÃdÃÃÖÃoÄ?Å Æ3Ç6È@ÈIÈeÎÚãÌ©>âbh7R:}6&GõWWÙG¼<`AnN½SuK'@»>¡G.O¤L'Cİ=IBJK?Ej>Î>ÜDşHF@—=Ô@BE4Eï@?=Ô=ÖA’CŞ@à<¶;>W@Ö?Ÿ<b:~;š=1>O<É9h9Ş:$<_;d98•8Ç9²9:8Î6Â6Ÿ7&8O7Ë55§5666Û4Ö3ù3>4i4g3¢2822¡2q2±1À0Ö01Û0/0t////é.-.ã--m-r-¿,*,,ü+Í++Ø*˜*^*@*å)z)7)â(—(u((‹'Ï&Ê%—%%X#¤·éZÒ€Ê¡Óúáè–áã×ÕoÛ2ãWãGİ”ØÛ\áòãúàWÜÜ=à6äÓãàëİCàöã+åìâlàáüãæfå7ãtâWäˆæüæ‡å:äåç0è·ç`æXæ‘çÖè8éJè¯ç„è¼é/êıéLéŒé”êVëeëíêësëìí´ììÚìíîîîNî¬îïxï[ïaïĞï,ğ’ğ¦ğ–ğêğñüñ)òIòXòÆò#ófó˜ó®óôqôÅôõ=õPõ±õğõ5ötö¥öÖöäöW÷÷£÷øWøwøÊøÿøzù¬ùÿùEú€úÏúàú~û;ıi9…Sx
“ö©
d-
áCû	]	AsˆÙÈgÆ‘‡AÂ„00¤?ãpA‹—’¥Ï¬x—«ÁiKv¼˜‹yd³ŠİY^{Q|{]‰WpidpZMZ+Hk¨’^’°šn`‰,simp_3M/V6j–FBCL3WSFdZ<HkCèZ’H6 $'155\&!D8HHc$)O\nTBKIKI/î%VşGkC!	5ıêB078*h@Y->e--5XX='/!úèòõô 2C2	ü"ÿø"0ú!õMşñ$+$âóáÛàññáñşíôîï	+şàÇÆÛÅõŞÒÑ	ïïËÌêîäÇäêÂæÆÜ¼¼éÀ¦¯ìô»ÄÙİ¶˜Õê“—µ±¼›½Ğ«¼¼™ƒ¡ ¶h »©ÎÑ¬¨á½‰©š•¨{š«ÖÍŒlvŸyl}xtnx›•Î„ˆ{¡™ÊÄ·®º˜Š¶ººpµt_¨—™¬º\emš¡Œ{‡~¡·gZ›—¨šÂ’X:…j>5K=A4@Rtyc¥pNlbULbnPZ]TLb•AaXFhe{W`Še`LNx“lks±——\PjwU9qeZ[cEcZZ_[lQIDe(]2G`„ŒqN`NNNNR"Lx38NU62U!K?$-ûü#==JIc*"/@!Qg!X-ëô¿9=4N;/'õøıäõúD>65:ı>Kæ 	"'k@şşı	#>A (òá4íñ%éíñ	ÓğÖçëŞâ>ôÑâËáÂºòÏñêÜÂÃúÆ¯ííààßõ¿ß³¯É¸¡·º˜µ³Í¤Ù¤ÔŞå÷ïÊ¾ËÔ¾ÊåŒØéàÊ½¼¸ÛäÓÊ³¿·ºÕ¸Ğâ¾á	ÈåáÊ¬¹¹Ï¹½ûÏÀ¸ÅñÉ³ÎÍÀÖ¼Í¼Ñ¿¡³ÃÕÃ©z¡²áËÔÜàØÆ¾±öåÂ´Î¬£™•õ¦Ñı³¿³¸º·ÈÑÕÑ®º©º±¨¾¨“·’¨ÂÂ ½éÀÅÉØÎÎÀ¼ÄÄ¤ÀÈ¤È—¿¡~Ê¿†²º±­w±…œ´¬éˆŒ´’Œ`«Œn¦‡‹v¦ÚºÄ—©œ¤­˜µ’¨µÂµ||€¨§¸‘¬¢¢à¢¢™¦¿‡­“††qkth¤’†’b~]Y£yoopvTcbfw]€–‘ev‡¬qd`~Gv•²Äip_k†©MMy~›Â¯wYHTf€eGj>L[e„j˜‘q¢`lv²©•[qpzœ‹uk‹©kYY…79oXT]0B29T€dvd„d[•dWhh‹zkB~~©t®­¤¨…¹Š›¸kCYj{w]B1j9FbeJ=‚„JXN0_AWn=".f.RIU%clukoU6Cò ò GbT7]#(>#GO8"G['0IB5.IR0107*d[<%<M^36cY?I**- +1;CTù 2'Lo9(5,,;5qe[A'8B8_JA_AW?&.AY&.WHN;k222L- 67YC(ş ç è ô ó è ı 09=5=9û 	+ö 6ø ö î î 	û ="õ &ğ 8D2*.2;%->%OC>X(	 S1ı 6ï â ê 9S+58A+3&"Ó D2&H.?U<1. -1LGf6ı ê ô #ô #ô 156"ó 9"ö ÿ í î ú û ä å ö é ì %.!&ã × ä õ  
Ö Ş  2ı  	Ù Ñ Ì ï ì Ö â Ş  ï ö =6ø å 	é ö ö ö &ú û ÿ á ÿ +2.ä !ß Á ş É è ú É Ş ã ğ ê ô È ì  · Ö Ğ 	õ 
ı Ö - ø ÿ î ı Ó ö ï û &&N+í ö å Æ é é ş ş É ÿ <MÒ ô !?ı ù Ò À (ù ø ,,	ó +â ö İ î î ò ò ä ä Ö Æ ä í Å í ö õ !-Lô ı ù 
#ş ï Ù ± Ş Ù Ğ ¿ â Ì ¶ Ç â ¿ £ ê Ø å é Ø º İ Ù µ é Ø Â ÿ î é á è Æ Ø É Æ ä î ì Ü ş Ú ğ ù è Ò ø Ô ã 
ô ı ı ó ¿ ² ¶ Ş Ù ¶ Ã Ã ² Ñ   Ğ § x ¿ Ğ ò ± ú Ü Ø å Ğ ÿ ä î Ø Ü Ü Æ ¼ é Î ´ µ À ¼  ‘ ¦ œ Ú Å ‹ Ü Ò Í ğ ç Ñ Ş Ú ª ø Å ê ï  â ı ê ï ± “ ç ­ Ì Ù ± Ô Ù Ø ± Ã ¿ Ğ … Ÿ Î µ Î Ÿ Ğ Ë ˆ ¤ Ç § ¸ § ‰ • i £ a Ÿ Î Æ ¸ Ÿ É ½ ¸ Á ¸ Ö ·  ƒ ƒ ƒ ¯ ´ œ ¯ ˆ ~ ­ Ñ È … ” Í ² Â ­ Ã   ¥ Æ Š q Ç º Ş  ‘ Ğ Ó ê º ¤ § l b ˆ ¸ µ ä í ° Î ò é ğ × è Ò Å Å ­ ‹ ‹ £ Ã ” ”  ƒ ‹ › » ¡ » Ç ­ “ x ¿ ¯  » á å º Ø Ô µ Ğ Ó › € Ë Ü Ø ò é Ë š Ü Ğ Ò  ˆ ‰ • À ¸ ¦ À ¯ ” Ò ¸ · À Ã ¥ ¯ ™ ˆ À « ¿ ç Ì À ± ª ©   Ç Ù ‡ ~  Ç İ   } ¶ Š œ ² « ¯ « Ë ª ª ¶ ¯  ¯ r g ƒ › ^ Z ‚ \ @ R  a L  : 6 òÿ ñÿ  üÿîÿsmpl<           “X  <                                            