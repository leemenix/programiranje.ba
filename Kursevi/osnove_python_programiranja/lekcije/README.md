# Python 3 - Uvod u programski jezik Python

autor: Milenko Letic - https://programiranje.ba

e-mail: milenko.letic@programiranje.ba

verzija: 0.5
- dodane igre vjesala i potapanje brojeva

verzija: 0.4
- dodani primjeri za vjezbe (lecije 1 i 2)


## O kursu

Kurs **Python 3 - Uvod u programski jezik Python** je dizajniran za sto jednostavnije ucenje. Namijenjen
je pocetnicima i kao takav pokusava da zadrzi vasu paznju, postepenim dodavanjem manjih detalja kako
bi se kreirala jasna slika sta je to Python programski jezik, gdje ga sve mozemo koristiti, kako nam moze
biti od pomoci na dnevnoj bazi ali ono sto je najvaznije kako vam moze obezbijediti buducnost u polju
informatike.

Nije tajna da je programer danas, kao i u proslosti, veoma cijenjeno zanimanje a da je potraznja na trzistu
rada veoma velika za ovim kadrovima sto ce i ostati u buducem periodu.

Ono sto cete postici na kraju ovog kursa, i sto bi trebala biti mjera da li ste uspjesno usvojili znanje,
jeste da cete biti u mogucnosti samostalno da kreirate osnovne programe, koji vam mogu biti od velike 
koristi prilikom automatizacije, ali ono najvaznije razumjecete principe programiranja i moci cete 
u potpunosti da se oslonite na svoje steceno znanje. Takodje, lakse cete moci da naucite druge programske 
jezike i da se upustite u ozbiljnije programarinje. 

Citavo vrijeme cete biti vodjeni kroz kurs na vama je samo, da u par sati koliko kurs traje, pomno pratitie sve
sto instruktor radi, odradjujete vjezbe nakon svake lekcije (rjesenja su uvijek data na pocetku sledece 
lekcije ili na kraju knjige koja dolazi sa kursom, takodje besplatno). 

Sva pitanja vezana za kurs mozete postaviti preko e-mail adrese _pitanja-python@programiranje.ba_ ili na
YouTube kanalu https://www.youtube.com/channel/UCSYrkPyht9PAXMhAbkGTbsQ (https://youtube.com/c/channel_name when it's ready).




## Par rijeci o Python programskom jeziku

Python je programski jezik opste namjeni, dinamicki typed i interpretiran, objektno orjentisan programski jezik kreiran u kasnim 80-tim od strane
 Guido van Rossum.

Dizajn filozofija Python-a se svodi na jednostavnu citljivost, dakle u prvom planu ima za cilj sto lakse citanje i pisanje koda. Ovo se postize koristenjem
 white-space to deliniate code blocks umjesto vec dobro poznatog i ustaljenog nacina koristenja uglastih zagrada _{}_ i tacka zareza _;_.

#### Kako pokrenuti Python
Generalno sav python kod se pokrece koristenjem interpretera. Najpopularniji i orginalni interpreter je CPython, zato sto je implementiran u C programskom
jeziku. Takodje, postoji i par drugih interpretera, a mnogi od njih su implementirani u razlicitim jezicima od C-a, kao sto su Java ili C# (C sharp).

Najcesce koristen interpreter CPython, koristi automatski garabage koletor (sakupljac smeca :), kako bi obezbijedio nesmetano  i efikasno upravljenje 
 memorijom kompjutera. Python je siroko poznat po usvajanju ne tradicionalne, minimalne sintakse, bazirane na  white space, i dizajnu koju tezi cistom i 
 citljivom kodu.

#### Verzije Python-a
Prije samo par mjeseci (pisano Feb. 2020), ako biste htjeli instalirati Python na vasem racunaru, dosli biste u konfuznu situaciju, jer Python, za razliku
od mnogih drugih programskih jezika, ima dvije glavne (major), ne kompatibilne verzije koje su podjednako u sirokoj upotrebi

Python verzije 2.7.3, released u 2012, je zadnja verzija popularnog Python-a 2 koji je released. Ova verzija je uglavnom u potpunosti kompatibilna unazad sa svim prethodnim verzijama.

Godine 2008, kreator, Guido van Rossum odlucio je da ocisti Python bazu (codebase) i overhall dosta drugih stvari u Python 2 koje mu se nisu svidjale, s toga je kreirao Python 3.

Python 3 je prihvatan ali veoma oprezno i polako na pocetku, najvise iz razloga sto nije kompatibilan unazad sa prethodnom verzijom Python 2, i zato je 
postojao ogroman eko-sistem biblioteka napisanih za Python 2 koje nece raditi sa novom verzijom Python-a 3.

Ovih dana Python 3 eco-sistem je uveliko pohvatao i izjednacio se sa prethodnom verzijom, sto nas dovodi do zakljucka da je Python 3 logicni izbor za sve 
nove developere koji planiraju uciti ovaj programski jezik. Python 3 je verzija koju cemo ujedno obraditi u ovom kursu.

## Priprema radnog okruzenja

### Izbor editora teksta i **Integrisanog razvojnog okruzenja** IDE (Integrated Development Environment)

#### Izbor tekst editora
Za pocetnike, se preporucuje koristenje nekog jednostavnog tekst editora kao Notpad++, Sublime, VisualStudio Code ...

#### Izbor Interisanog razvojnog okruzenja
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
## Zdravo Svijete

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

## Komentarisanje koda
- upisavanje podsjetnika
- komentarisanje koda
- preporuka da se koristi taraba
 ovo je taraba (hash tag) simbol
 komentari su po default-u ignorisani u python-u
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

## Zadaci za samostalni rad!

1. Napisati program koji ispisuje vase ime i prezime

2. Napisati program koji crta pravougaonik oblika
```python
__________
|         |
|         |
|_________|
```

3. Napisati program koji crta trougao oblika
```python
    /\
   /  \
  /    \
 /      \
/________\
```
## Promjenjive i tipovi podataka

### Promjenjive, varijable (variables) 

Programiranje se uglavnom svodi na obradu podataka, stim u vezi je potrebno pohraniti podatke 
i organizovati ih na najbolji moguci nacin. Varijable ili promjenjiva predstavlja lokaciju u memoriji
vaseg kompjutera i sluzi da pokaze na odredjenu vrijednost koju ta memorijska lokacija predstavlja.

Tri glavna faktora koji cine promjenjivu/varijablu jesu: 

- naziv, 
- operator i 
- vrijednost varijable

```python
naziv   |    operator     | vrijednost
           pridruzivanja

ime             =            "Goku"

godine          =              23
```

#### Gradjenje varijable
- naziv varijable ne smije poceti sa brojem
- naziv varijable moze poceti, malim, velikim slovima ili donjom crticom (_)
nakon cega moze ici broj
- mala i velika slova se razlikuju (a != A)


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

### Tipovi podataka

```yaml
            Tipovi podataka                  |    python sintksa    |             objasnjenje
_____________________________________________|______________________|__________________________________
Znakovni (string - predstavlja niz znakova)  |       string()       | operacije nad znakovnim tipovima
                                             |                      |             podataka
_____________________________________________|______________________|__________________________________
Brojevi cijeli, realni (integer, float)      |         int()        |int()   - pretvara u cijeli broj 
                                             |                      |            (npr. 1,10,33)
                                             |        float()       |float() - pretvara u realni broj
                                             |                      |        (npr. 1.0, 3.14, 33.3333)
_____________________________________________|______________________|__________________________________
Logicki tacno, netacno (boolean True/False)  |         bool()       |bool()  - operacije nad logickim 
                                             |                      |          tipovima podataka 
                                             |                      |            (True i False)
_____________________________________________|______________________|__________________________________
```

korisna funkcija type
```python
print(type(karakter_ime))
```
### Mijenjanje tipova promjenjive (kastovanje)
Primjenjiva moze mijenjati tip kroz izvrsavanje programa, sto se jos naziva i kastovanje (casting). 
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

## Rad sa stringovima
Stringovi predstavljaju niz karaktera (velika/mala slova, brojevi, znakovi interpunkcije, specijalni 
znakovi, ...), koji sluzi za skladistenje i rad sa tekstualni podacima. 

### Jednostavan primjer kreiranja stringa
rad_sa_stringovima.py
```python
print("programiranje.ba besplatni online kursevi")

# escape karakter \
print("programiranje.ba \n besplatni online kursevi")

sajt_naziv = "programiranje.ba"
sajt_slogan = " besplatni online kursevi"

# jos neki primjeri kreiranja string-a (kao sto smo imali slucaj sa viselinijskim komentarom)
sajt_naziv = 'https://programiranje.ba'
sajt_slogan = """besplatni online kursevi
                   za sve """
```

### Funkcije nad stringovima
rad_sa_stringovima.py
```python
print("programiranje.ba besplatni online kursevi")

# escape karakter \
print("programiranje.ba \n besplatni online kursevi")
# takodje se koristi kada trebamo ispisati specijalne karaktere
#print("\")
print("\\")

sajt_naziv = "programiranje.ba"
sajt_slogan = " besplatni online kursevi"
print(sajt_naziv)
print(sajt_slogan)
print(sajt_naziv + sajt_slogan)
print(sajt_naziv.upper() + sajt_slogan.upper())
print(sajt_naziv.isupper())
print(len(sajt_naziv))
print(sajt_naziv * 3)

# index stringa pocinje na poziciji 0
print(sajt_naziv[4])
print(sajt_naziv[-4])
print(sajt_naziv[1:4])
# index funkcija i proslijedjivanje parametara
print(sajt_naziv.index('g'))
print(sajt_naziv.index('mira'))
#print(sajt_naziv.index('h'))
# find funkcija i proslijedjivanje parametara
print(sajt_naziv.find('g'))
print(sajt_naziv.find('mira'))
# razlika izmedju find i index, u slucaju da ne postoji trazeni patern
# index() vraca gresku, dok find vraca -1

# replace funkija
print(sajt_slogan.replace("kursevi","tutoriali").upper())

print("{1}, {0}".format(sajt_naziv, sajt_slogan))
print(f"{sajt_naziv} {sajt_naziv}")

# jos neki primjeri funkcija nad stringovima
sajt_naziv = "programiranje.ba"
sajt_godina = "2020"
sajt_kratki_slogan = "kursevi"

print(sajt_naziv.isalpha())
print(sajt_godina.isdigit())
print(sajt_kratki_slogan.isalpha())
### funkcije chr() i ord() kasnije potrebni za cezarovu sifru 
# funkcija ord() daje cjelobrojnu vrijednost karaktera prema ASCII tabli
print(ord('A'))
print(ord('a'))
print(ord('b'))
print(ord('z'))

# funkcija chr() konvertuje cjelobrojnu vrijednost u odgovarajuci karakter 
print(chr(64))
print(chr(33))
print(chr(97))
print(chr(100))

# kombinacija chr() i ord()
print(ord('b') + 3)
print(chr(ord('b') + 3))
```

## Rad sa brojevima
brojevi, rad sa brojevima, funkcije nad brojevima. 
Osnovne aritmeticke operacije koje mozemo vrsiti u Python-u su

```yaml
 Operacija |    Naziv operacije   |     Primjer      |   Rezultat   
___________|______________________|__________________|____________
     +     |      Sabiranje       |  print(1 + 1)    |    2
___________|______________________|__________________|____________
     -     |      Oduzimanje      |  print(6 - 5)    |    1
___________|______________________|__________________|____________
     *     |       Mnozenje       |  print(4 * 3)    |    12
___________|______________________|__________________|____________
     /     |      Dijeljenje      |  print(4 / 2)    |    2
___________|______________________|__________________|____________
     %     |      Ostatak pri     |  print(5 % 2)    |    1
           |   dijeljenju (moduo) |                  |  
___________|______________________|__________________|____________
     **    |      Potenciranje    |  print(2 ** 3)   |    8
___________|______________________|__________________|____________
```


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

## Ulaz/upis podataka, prihvatanje podataka od korisnika ili interakcija sa programom

Slozicete se da je programiranje dosadno, ako nemamo interakciju, nekakav vid komunikacije
sa nasim programom. Kako bi omogucili interakciju sa programom, Python nam na raspolaganje nudi
funkciju input(). 

```python

input() 
# hej ti, cekam da uneses neku informaciju podatak, naravno korisnik nije siguran sta se desava

input("Unesite vase ime: ")
# aha ovo sad vec ima smisla

# <naziv varijable> <tip podatka>
korisnik_ime = input("Unesite vase ime: ")
# naravno, posto nam je korisnicki unos vazan mi zelimo sacuvati isti taj unos u neku varijablu
# kako bi smo kasnije mogli koristiti
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


## Zadaci za samostalni rad!

1. Napisati program koji trazi da upisete vase ime, a on automatski ispisuje vase ime pet puta, sa
razmakom izmedju imena.
```yaml
Unesite vase ime: Goku
Goku Goku Goku Goku Goku 
```

2. Napisati program koji trazi da unesete dvije rijeci, a zatim ih ispise u istom redu sa razmakom od 
tri space karaktera izmedju izmedju.
```yaml
Unesite prvu rijec: Dobar
Unesite drugu rijec: Dan
Dobar   Dan
```

3. Napisati program koji racuna aritmeticku sredinu za tri unesena broja. Pomoc: Aritmeticka sredina za a,b,c se izracunava po formuli (a + b + c)/3 
```yaml
Unesite prvi broj: 1
Unesite drugi broj: 2
Unesite treci broj: 3
Aritmeticka sredina je: 2.0
```
4. Napisati program koji za uneseni karakter sa tastaure ispisuje vrijednost iz ASCII tabele
```yaml
Unesite znak sa tastature: }
Vrijednost znaka '}' u ASCII tabeli je 125
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

## Tuples - torka (tip podaktovne strukture, veoma slican listama) - ()
Tuples predstavlja niz nepromjenjivih clanova. Clanovi unutar Tuple-a mogu biti istih ili razlicitih
tipova. Tuple definisemo nabrajanjem objekata odvojenih zarezom, cak i ako je u pitanju jedan jedini
clan moramo imati zaraz, u suprotnom se gubi osobina Tuple-a.

Razlikuju se od liste po tome sto su nepromjenjive (immutable -ne mogu se mijenjati).

```python
karakteri = (1,2,3,4,"a","d","-")
print(karakteri)
type(karakteri)

karakteri = (1,)
print(karakteri)
type(karakteri)

karakteri = (1)
print(karakteri)
type(karakteri)
```

koorinate.py
```python
koordinate = (4, 5)
print(type(koordinate))
print (len(koordinate))
print(koordinate.index(5))
print(koordinate[0])
print(koordinate[1])

koordinate[1] = 10 # dobicemo gresku
```
### list of tuples
```python
koordinate = [(4,5), (6,3), (7.4)]
print(type(koordinate))

print(len(koordinate))
```

#### Rijecnik - Dictionaries - {}
- standardni rijecnik koji imamo ima strukturu rijec i detaljno objasnjenje rijece
  gdje rijec predstavlja kljuc (key), vrijednost (value) predstavlja definiciju
  key mora biti jedinstven
```python
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
```
## Funkcije

Skup kodova koje odradjuju odredjene zadatke, dobri su za organizaciju koda. 

Funkcije se definisu pomocu kljucne rijeci def, kad god se pojavi def na pocetku linije, python zna da korisnik zeli kreirati funkciju i stim u vezi se i ponasa.

```yaml
def naziv_funkcije(parametri): # parametri su opcioni, ali ako postoje moraju biti definisani/proslijedjeni
  blok naredbi # argumenti

naziv_funkcije(argumenti) # poziv funkcije
```

zdravo_svijete_funkcija.py
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


#### Naredbe za kontrolu toka (if, elif, else)

Ako zelimo da donosenje odluke prepustimo nasem programu, na osnovu uslova koji se moraju ispuniti, a
samim tim krairamo nas program pametnijim, uvescemo novi uslov if (naredbu if), koja se jos zove
i naredba kontrole toka. Ukoliko je uslov ispunjen (Tacan - True), izvrsava se naredba ili blok naredbi
pod tim uslovom, u suprotnom izvrsava se drugi blok naredbi ili se nastavlja ispitivanje.

Primjer iz realnog zivota
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

### Logicki operatori (and, or i not) ili bitski operatori

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

## while petlja 
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

## for petlja
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
## dvodimenzionalne liste i ugnijezdene petlje (nested)

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

## try / except (catch) - hvatanje greski
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

## citanje iz eksternog fajla
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

## upisivanje u eksterni fajl
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

## moduli i pip alat
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

## Klase i objekti
Znamo od pocetka da je Python objektno orijentisani programski jezik, sto znaci da su svi podaci
predstavljeni kao objekti. Prihvatanjem objektno orijentisanog nacina programiranja, nasi programi,
ali sam kod, postaju ekstremno korisni, organizovaniji i mocniji.
Kada programiramo susrecemo se sa razlicitim tipovima podataka, takodje susrecemo se sa razlicitim strukturama podataka, ali sta u slucaju kad ne mozemo predstaviti neku pojavu iz prirode sa vec postojecim tipovima ili strukturama podataka?
Upravo su nam za to korisne klase. U Python-u mozemo krairati klase (definise vas licni tip podatka, ponasa se kao template, patern kako nesto treba da izgleda). Objekat je podatak u memoriji, pravi podatak kreiran iz klase. 

Posto ne postoji student tip podaka, kreiracemo klasu Student

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

# kreiranje instance Student student_prvi objetka
student_prvi = Student("Goku", "Programiranje", 8, False)
print(student_prvi)
print(student_prvi.ime)
print(student_prvi.ocjena)

student_drugi = Student("Krilin", "Ekonomija", 8.3, True) 
print(student_drugi.brucos) 
```

### funkcije unutar klase (funkcije objekta)
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
## naslijedjivanje
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

```python
#potapanje brodova
```
```python
# Vjesala

import random

fajl = "rijecnik.txt"

def ucitaj_rijeci():
    """
    Vraca listu validnih rijeci. Rijeci su tipa string, napisane malim slovima

    U zavisnosti od duzine liste rijeci, ova funkcija moze potrajati.
    """
    print("Ucitavanje rijeci iz fajla 'rijecnik.txt'...")
    # otvori_fajl: fajl
    otvori_fajl = open(fajl, 'r')
    # linija: string (procitaj liniju u fajlu - citav fajl je napisan kao jedna linija)
    linija = otvori_fajl.readline()
    # lista_rijeci: lista rijeci (rijec po rijec)
    lista_rijeci = linija.split()
    print("  ", len(lista_rijeci), "rijeci ucitano.")
    return lista_rijeci

# listarijeci_pomoc = ucitaj_rijeci.__doc__
# print(listarijeci_pomoc)
# print(listarijeci)
# lista_rijeci = ucitaj_rijeci()
# print(lista_rijeci)

def izbor_rijeci(lista_rijeci):
    """
    fajl (lista): lista rijeci (string)

    Funkcija vraca slucajnu rijec iz liste lista_rijeci
    """
    return random.choice(lista_rijeci)

# izabrana_rijec = izbor_rijeci(lista_rijeci)
# print(izabrana_rijec)

# kraj pomocnog koda
# -----------------------------------

# Ucitaj listu rijeci u varijablu lista_rijeci
# kako bi smo mogli pristupiti listi bilo gdje iz programa
lista_rijeci = ucitaj_rijeci()

def da_li_je_rijec_pogodjena(tajna_rijec, pogodjena_slova):
    '''
    tajna_rijec: string, rijec koju igrac pogadja
    pogodjena_slova: lista, koja slova su pogodjena
    Funkcija vraca: boolean, Tacno (True) ako su sva koja se nalaze u tajna_rijec rijeci takodje 
    u pogodjena_slova, u suprotnom Netacno (False)
    '''
    brojac=0
    for slovo in tajna_rijec:
        if slovo in pogodjena_slova:
            brojac+=1
    if brojac==len(tajna_rijec):
        return True
    else:
        return False

def dohvati_pogodjenu_rijec(tajna_rijec, pogodjena_slova):
    '''
    tajna_rijec: string, rijec koju igrac pogadja
    pogodjena_slova: lista, koja slova su pogodjena
    Funkcija vraca: string, kombinaciju slova i donjih crtica koji predstavljaju pogodjena slova i
      slova koja jos nisu pogodjena, respektivno.
    '''
    lista=[]
    rijec=""
    for key in tajna_rijec:
        if key in pogodjena_slova:
            rijec+=key
        else:
            rijec+="_ "
    return rijec

# tajna_rijec="asa"
# pogodjena_slova=["a"]
# rijecica=dohvati_pogodjenu_rijec(tajna_rijec,pogodjena_slova)
# print(rijecica)

def dohvati_raspoloziva_slova(pogodjena_slova):
    '''
    pogodjena_slova: lista, koja slova su pogodjena
    Funkcija vraca: string, listu slova koji sacinjavaju slova koja jos trebaju biti pogodjena.
    '''
    rijec=""
    brojac=0
    slova='abcdefghijklmnopqrstuvwxyz'
    for slovo in slova:
        if slovo in pogodjena_slova:
            brojac+=1
        else:
            rijec+=slovo
    return rijec

# pogodjena_slova=["a"]
# rijecica=dohvati_raspoloziva_slova(pogodjena_slova)
# print(rijecica)
    

def vjesala(tajna_rijec):
    '''
    tajna_rijec: string, rijec koju igrac pogadja
    pogodjena_slova: lista, koja slova su pogodjena
    Funkcija vraca: string, kombinaciju slova i donjih crtica koji predstavljaju pogodjena slova i
      slova koja jos nisu pogodjena, respektivno.
    
    Startuje interaktivnu igricu vjesala.

    * Na pocetku igre, daje informaciju igracu koliko 
      slova ima tajnoj rijeci.

    * Pitaj igraca da proslijedi jedno slovo po pokusaju.

    * Igrac bi trebao dobiti informaciju odmah nakon pokusaja
      gdje se u rijeci nalazi slovo u slucaju da je pogodio.

    * Nakon svakog pokusaja, igrac bi trebao vidjeti djelimicno
      pogodjenu rijec, ali i slova koja nedostaju u rijeci.

    '''
    # main funkcija
    duzina_tajne_rijeci=len(tajna_rijec)
    print("Dobrodosli u igricu, Vjesala!")
    print("Razmisljam o rijeci duzine " + str(duzina_tajne_rijeci) + " karaktera.")
    dozvoljen_broj_pokusaja=2*len(tajna_rijec)
    i=0
    pogodjena_slova=[]
    while (dozvoljen_broj_pokusaja != 0):
        print("------------")
        if tajna_rijec != dohvati_pogodjenu_rijec(tajna_rijec, pogodjena_slova):
            print("Imate jos " + str(dozvoljen_broj_pokusaja) + " pokusaja.")
            print("Raspoloziva slova: ",dohvati_raspoloziva_slova(pogodjena_slova))
            pokusaj=input("Molimo pokusajte slovo: ")
            pokusaj_mala_slova = pokusaj.lower()
            
            if pokusaj_mala_slova  in pogodjena_slova:
                print("Ups! Vec ste pokusali to slovo: ",dohvati_pogodjenu_rijec(tajna_rijec, pogodjena_slova))
            
            elif pokusaj_mala_slova not in tajna_rijec: 
                print("Ups! Slovo se ne nalazi u rijeci koju sam zamislio:",dohvati_pogodjenu_rijec(tajna_rijec, pogodjena_slova))
                dozvoljen_broj_pokusaja-=1
            else:
                pogodjena_slova.append(pokusaj_mala_slova)
                print("Pogodili ste: ",dohvati_pogodjenu_rijec(tajna_rijec, pogodjena_slova))
                #chances+=1
            pogodjena_slova.append(pokusaj_mala_slova)
        elif tajna_rijec==dohvati_pogodjenu_rijec(tajna_rijec, pogodjena_slova):
            print("Cestitamo!")
            break
    else:
        print("----------")
        print("Nazalost, nemate vise pokusaja. Tajna rijec je bila "+ tajna_rijec +".")




# Kada zavrsite funkciju vjesala, mozete testirati vas kod definisanjem
# tajne rijeci tajna_rijec="tajna"

#tajna_rijec= izbor_rijeci(lista_rijeci).lower()
#tajna_rijec="tajna"
tajna_rijec=izbor_rijeci(lista_rijeci)

vjesala(tajna_rijec)
``````python
from random import randint
mreza=[]

for i in range(0,7):
    mreza.append(["#"] * 7)
def stampaj_mrezu (board):
    for red in mreza:
        print (" ".join(red))

print ('Igra Potapanje brodova moze da pocne!')
stampaj_mrezu(mreza)

#Slučajnim odabirom u mrežu ubacujemo oba broda
def nasumicni_red(mreza):
    return randint(0, len(mreza)-1)

def nasumicna_kolona(mreza):
    return randint(0, len(mreza[0])-1)

#brod 1
red_1 = nasumicni_red(mreza)
kol_1 = nasumicna_kolona(mreza)
#brod 2
red_2 = nasumicni_red(mreza)
kol_2 = nasumicna_kolona(mreza)
#Da se brodovi ne bi preklapali, potrebno je da nemaju zajednička polja
#To se obezbeđuje funkcijom razliciti()
def razliciti(r,c):
    while r == red_1 and c == kol_1:
        r = nasumicni_red(mreza)
        c = nasumicna_kolona(mreza)
        red_2 = r
        kol_2 = c
razliciti(red_2,kol_2)
#Kada izaberete jedno polje, preostala dva mogu biti horizontalno(levo ili desno) ili vertikalno(gore ili dole)
#Zato se definišu sledeći pravci
def nasumicni_pravac():
    n = randint(1,4)
    if n == 1:
        return "gore"
    elif n == 2:
        return "desno"
    elif n == 3:
        return "dole"
    elif n == 4:
        return "levo"
#Nasumično se odredi pravac, i na osnovu njega sledeća dva polja
while True:
    d = nasumicni_pravac() 
    if d == "gore":
        if red_1 >= 2:
            
            red_1_2 = red_1 - 1
            kol_1_2 = kol_1
            red_1_3 = red_1 - 2
            kol_1_3 = kol_1
            break
    if d == "desno":
        if kol_1 <= len(mreza[0])-3:
            
            red_1_2 = red_1
            kol_1_2 = kol_1 + 1
            red_1_3 = red_1
            kol_1_3 = kol_1 + 2
            break
    if d == "dole":
        if red_1 <= len(mreza)-3:
            
            red_1_2 = red_1 + 1
            kol_1_2 = kol_1
            red_1_3 = red_1 + 2
            kol_1_3 = kol_1
            break
    if d == "levo":
        if kol_1 >= 2:
            
            red_1_2 = red_1
            kol_1_2 = kol_1 - 1
            red_1_3 = red_1
            kol_1_3 = kol_1 - 2
            break
brod_1 = [(red_1 ,kol_1 ),(red_1_2 ,kol_1_2 ),(red_1_3 ,kol_1_3 )]



#drugi brod:
while True:
#Nasumično se odredi pravac, i na osnovu njega sledeća dva polja
#Uslov je da se ne preklapaju sa poljima prvog broda
    d = nasumicni_pravac() 
    if d == "gore":
        if red_2 >= 2:
            if (red_2 - 1,kol_2) not in brod_1 and (red_2 - 2,kol_2) not in brod_1:
                
                red_2_2 = red_2 - 1
                kol_2_2 = kol_2
                red_2_3 = red_2 - 2
                kol_2_3 = kol_2
                break
    if d == "desno":
        if kol_2 <= len(mreza[0])-3:
             if (red_2 ,kol_2 + 1) not in brod_1 and (red_2,kol_2 + 2) not in brod_1:
                
                red_2_2 = red_2
                kol_2_2 = kol_2 + 1
                red_2_3 = red_2
                kol_2_3 = kol_2 + 2
                break
    if d == "dole":
        if red_2 <= len(mreza)-3:
            if (red_2 + 1 ,kol_2) not in brod_1 and (red_2 + 2,kol_2) not in brod_1:
                
                red_2_2 = red_2 + 1
                kol_2_2 = kol_2
                red_2_3 = red_2 + 2
                kol_2_3 = kol_2
                break
    if d == "levo":
        if kol_2 >= 2:
            if (red_2 ,kol_2 - 1) not in brod_1 and (red_2,kol_2 - 2) not in brod_1:
                
                red_2_2 = red_2
                kol_2_2 = kol_2 - 1
                red_2_3 = red_2
                kol_2_3 = kol_2 - 2
                break



tacan = 0 #U ovoj promenljivoj smešta se ukupan broj pogođenih polja oba broda
prvi_brod = 0 #U ovoj promenljivoj smešta se broj pogođenih polja prvog broda
drugi_brod = 0 #U ovoj promenljivoj smešta se broj pogođenih polja drugog broda
#Na početku nemamo nijedno pogođeno polje, pa sve promenljive postavljamo na 0
#U ovoj promenljivoj smešta se ukupan broj pogođenih polja oba broda
tacan = 0 
#U ovoj promenljivoj smešta se broj pogođenih polja prvog broda
prvi_brod = 0 
#U ovoj promenljivoj smešta se broj pogođenih polja drugog broda
drugi_brod = 0 

#Dozvoljeno je 15 pokušaja da se potope oba broda
for pokusaj in range(1,16):
    print (str(pokusaj ) + '. pokusaj:')

    nagadjanje_reda  = int(input('Pogodite red:'))
    nagadjanje_kolone  = int(input('Pogodite kolonu:'))
#Ispituje se da li je korisnik pogodio neko polje prvog broda
#Ako jeste, broj pogođenih polja se povećava za jedan
    if ((nagadjanje_reda -1  == red_1 ) and (nagadjanje_kolone -1  == kol_1)) or ((nagadjanje_reda -1 == red_1_2 ) and (nagadjanje_kolone -1 == kol_1_2)) or((nagadjanje_reda -1 == red_1_3 ) and (nagadjanje_kolone -1 == kol_1_3)) and mreza[nagadjanje_reda -1 ][nagadjanje_kolone -1] != 'X' :
   

        tacan = tacan+1
        prvi_brod = prvi_brod + 1

        if (tacan != 6) and (prvi_brod != 3) :
            
           
            print ('Bravo, pogodak!')
            mreza[nagadjanje_reda -1 ][nagadjanje_kolone -1] = 'X'
#Ako je pogođeno polje treće polje prvog broda, korisnik se obaveštava da je potopio ceo brod
        elif (tacan != 6) and (prvi_brod == 3):
            
            mreza[nagadjanje_reda -1 ][nagadjanje_kolone -1] = 'X'

            print ('Bravo, potopili ste ceo brod! Ostao vam je jos jedan!')
#Ako je reč o šestom pogođenom polju, korisnik se obaveštava da je potopio oba broda
        if (tacan == 6):
            mreza[nagadjanje_reda -1][nagadjanje_kolone -1] = 'X'
            print ('Svaka cast, potopili ste oba broda!')
           
            break
#Ispituje se da li je korisnik pogodio neko polje drugog broda 
#Ako jeste, broj pogođenih polja se povećava za jedan

    elif   ((nagadjanje_reda -1  == red_2 ) and (nagadjanje_kolone -1  == kol_2)) or ((nagadjanje_reda -1  == red_2_2 ) and (nagadjanje_kolone -1  == kol_2_2)) or ((nagadjanje_reda -1  == red_2_3 ) and (nagadjanje_kolone -1  == kol_2_3)) 	 and mreza[nagadjanje_reda -1 ][nagadjanje_kolone -1] != 'Y'  :
        tacan = tacan+1
        drugi_brod = drugi_brod + 1
        if (tacan != 6) and (drugi_brod != 3):
            
            print ('Bravo, pogodak!')
            mreza[nagadjanje_reda -1 ][nagadjanje_kolone -1] = 'Y'
        elif (tacan != 6) and (drugi_brod ==3):
           
            mreza[nagadjanje_reda -1 ][nagadjanje_kolone -1] = 'Y'
#Ako je pogođeno polje, treće polje prvog broda, korisnik se obaveštava da je potopio ceo brod

            print ('Bravo, potopili ste ceo brod! Ostao vam je jos jedan!')
#Ako je reč o šestom pogođenom polju, korisnik se obaveštava da je potopio oba broda

        if (tacan == 6):
            mreza[nagadjanje_reda -1][nagadjanje_kolone -1] = 'Y'
            print ('Svaka cast, potopili ste oba broda!')
            break
    else:
        if (nagadjanje_reda < 1 or nagadjanje_reda > 7) or (nagadjanje_kolone < 1 or nagadjanje_kolone > 7):
            print ('Ups, izvan opsega ste!')
        elif (mreza[nagadjanje_reda -1 ][nagadjanje_kolone -1]=='X'):
            print ('Vec ste pronasli ovaj deo broda!')
        elif (mreza[nagadjanje_reda -1 ][nagadjanje_kolone -1]=='O'):
            print ('Vec ste pogadjali isto polje!')
        else:
            print ('Promasili ste!')
            mreza[nagadjanje_reda -1 ][nagadjanje_kolone -1] = 'O'


    stampaj_mrezu(mreza)
    if (pokusaj == 15):
            print ('Igra je zavrsena!')

if (mreza[red_1 ][kol_1 ] != "X" or mreza[red_1_2 ][kol_1_2 ] != "X" or
mreza[red_1_3 ][kol_1_3 ] != "X") or (mreza[red_2 ][kol_2 ] != "Y" or mreza[red_2_2 ][kol_2_2 ] != "Y" or
mreza[red_2_3 ][kol_2_3 ] != "Y"):
    print ('Brodovi su se nalazili na ovim pozicijama! Vise srece drugi put!')
    mreza[red_1 ][kol_1 ] = "X"
    mreza[red_1_2 ][kol_1_2 ] = "X"
    mreza[red_1_3][kol_1_3] = "X"
    mreza[red_2][kol_2 ] = "Y"
    mreza[red_2_2 ][kol_2_2] = "Y"
    mreza[red_2_3][kol_2_3 ] = "Y"


stampaj_mrezu(mreza)
```
```python
ime = input("Unesite vase ime: ")
pet_puta=(ime+" ")*5
print(pet_puta)
```

```python
a=input("Unesite znak sa tastature: ")
b=ord(a)

print("Vrijednost znaka '" + a + "' u ASCII tabeli je " + str(b))
```

```python
a=input("Unesite prvi broj: ")
b=input("Unesite drugi broj: ")
c=input("Unesite treci broj: ")
asredina=(int(a)+int(b)+int(c))/3
print("Aritmeticka sredina je: " + str(asredina))
```
```python
prva_rijec  = input("Unesite prvu rijec: ")
druga_rijec = input("Unesite drugu rijec: ")

print(prva_rijec + '   ' + druga_rijec)
```
