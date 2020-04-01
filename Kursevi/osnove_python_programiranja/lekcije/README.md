
# Python 3 - Uvod u programski jezik Python

**autor:** Milenko Letic - https://programiranje.ba

**e-mail:** milenko.letic@programiranje.ba

**godina:** 2020

**izmjene:**
verzija: 0.5
- izvorni kod za igre vjesala i potapanje brodova
- rad sa datotekama

verzija: 0.4
- zadaci za vjezbanje (lecije 1 i 2)


<a name="o-kursu"/>

## O kursu

Kurs **Python 3 - Uvod u programski jezik Python** je dizajniran za sto jednostavnije ucenje. Namijenjen
je pocetnicima i kao takav pokusava da zadrzi vasu paznju, postepenim dodavanjem manjih detalja kako
bi se kreirala jasna slika sta je to Python programski jezik, gdje ga sve mozemo koristiti, kako nam moze
biti od pomoci na dnevnoj bazi ali ono sto je najvaznije kako vam moze obezbijediti buducnost na polju
informacionih tehnologija.

Nije tajna da je programer danas, kao i u proslosti, veoma cijenjeno zanimanje a da je potraznja na trzistu
rada veoma velika za ovim kadrovima sto ce i ostati u buducem periodu.

Ono sto cete postici na kraju ovog kursa, i sto bi trebala biti mjera da li ste uspjesno usvojili znanje,
jeste da cete biti u mogucnosti samostalno da kreirate osnovne programe, koji vam mogu biti od velike 
koristi prilikom automatizacije, ali ono najvaznije razumjecete principe programiranja i moci cete 
u potpunosti da se oslonite na svoje steceno znanje. Takodje, lakse cete moci da naucite druge programske 
jezike i da se upustite u ozbiljnije programiranje. 

Citavo vrijeme cete biti vodjeni kroz kurs na vama je samo, da u par sati koliko kurs traje, pomno pratitie sve
sto instruktor radi, odradjujete vjezbe nakon svake lekcije (rjesenja su uvijek data na pocetku sledece 
lekcije ili na kraju knjige koja dolazi sa kursom, takodje besplatno). 

Primijeticete da nazivi Python fajlova imaju malo cudnu konvenciju, ali na nacin kako su fajlovi nazvani
autor je olaksao organizaciju izvornog koda kao i referisanje studenata na odredjeni kod.

Prilikom kreiranja kursa i primjera mahom su koristeni karakteri iz poznate anime serije Zmajeva Kugla
(Dragon Ball). Ponekad su dijelovi teksta uzeti iz pjesama Miladina Sobica, Tome Zdravkovica, Dubioze Kolektiv
 i Ramba Amadeusa. Takodje, postoje dijelovi teksta iz pjesmica za djecu, sve u cilju da se koncepti programiranja 
 usvoje sto je lakse i prirodnije moguce ali i da predavanje drzi paznju te da bude zanimljivo tokom cijelog kursa. 

tbd. Igrice vjesala i potapanje brodova.
tbd. python mozete koristiti na svim poljima, automatizaciju, obradu ogromne kolicine podataka, web, igrice ...

Sva pitanja vezana za kurs mozete postaviti preko e-mail adrese

_pitanja-python@programiranje.ba_ 

ili na YouTube kanalu 

https://www.youtube.com/channel/UCSYrkPyht9PAXMhAbkGTbsQ (https://youtube.com/c/channel_name kada bude spreman tbd.)

<a name="istorija-pythona"/>

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

**`Izvorni kod: kod-10_zdravo-svijete.py`**

```python      
print("Zdravo Svijete!")
```

Imamo dva nacina za pokretanje Python programa, ovo je preporuka kada koji koristiti:
- cmd, terminal - (ako nesto zelimo da provjerimo brzo i trenutno)
- direktno iz IDE-a (precice) - (kada pisemo vise linija koda)

Programiranje predstavlja davanje instrukcija kompjuteru (kroz programski jezik) i na osnovu ovih instrukcija
kompjuter donosi odluke. 

**`Izvorni kod: kod-11_crtanje-oblika.py`**

```python
print("*")
print("**")
print("***")
print("****")
print("*****")
print("******")
```

- u ovom slucaju python ide liniju po liniju i izvrsava kod
- sta se desava u slucaju da zamijenimo prvu i zadnju liniju?

## Komentarisanje koda

Komentare koristimo kada zelimo da zapisemo neki podsjetinik unutar koda, komentarisemo kod, objasnimo drugima
i sebi sta odredjena linija koda radi. Praksa i preporuka je da se koristi simbol taraba (hash tag) _#_. 
Komentari su po default-u ignorisani u Python-u, preciznije ignorisani od strane Python interpretera.  

**`Izvorni kod: kod-12_demonstracija-komentara.py`**
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
```text
Ime i Prezime
```

2. Napisati program koji crta pravougaonik oblika
```text
__________
|         |
|         |
|_________|
```

3. Napisati program koji crta trougao oblika
```text
    /\
   /  \
  /    \
 /      \
/________\
```
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
    tipovi podataka       |    python sintksa    |          objasnjenje
__________________________|______________________|_____________________________
       Tekstualni         |       string()       |  operacije nad znakovnim
  (string - niz znakova)  |                      |     tipovima podataka 
                          |                      |            
__________________________|______________________|_____________________________
 Brojevi cijeli, realni   |                      |  
   (integer, float)       |        int()         |  pretvara u cijeli broj 
                          |                      |     (npr. 1,10,33)
                          |______________________|_____________________________
                          |       float()        |  pretvara u realni broj
                          |                      | (npr. 1.0, 3.14, 33.333)
__________________________|______________________|_____________________________
  Logicki tacno, netacno  |                      |
   (boolean True/False)   |        bool()        |  operacije nad logickim 
                          |                      |    tipovima podataka 
                          |                      |      (True i False)
__________________________|______________________|_____________________________
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

## Rad sa stringovima
Stringovi predstavljaju niz karaktera (velika/mala slova, brojevi, znakovi interpunkcije, specijalni 
znakovi, ...), koji sluzi za skladistenje i rad sa tekstualni podacima. Mozemo reci da su stringovi 
uredjeni i smisleni niz karaktera. 

### Jednostavan primjer kreiranja stringa
**`Izvorni kod: kod-165_rad_sa_stringovima.py`**
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

**`Izvorni kod: kod-166_rad_sa_stringovima.py`**
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

**`Izvorni kod: kod-185_rad-sa-brojevima.py`**
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

**`Izvorni kod: kod-190_interakcija-sa-korisnikom.py`**
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

**`Izvorni kod: kod-191_interaktivni_karakter_program.py`**
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

**`Izvorni kod: kod-192_osnovni_kalkulator.py`**

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

Liste predstavljaju niz objekata, gdje svaki clan liste ima svoj indeks. Ovi clanovi se nazivaju elementima
lista. Slicne su stringovima, s tim da svaki elemnent liste moze biti razlicitog tipa. Elementi liste su
smjesteni u uglaste zagrade _[]_ i razdvojeni zarezom _,_. 

```text
lista   |  [ 1, 4, 6.33, 10, "Goku" ]
indeks  |    0  1     2   3    4  
```

Rad sa listama, nam pomaze pri organizaciji i boljem pracenju toka podataka.

**`Izvorni kod: kod-210_rad-sa-listama.py`**
```python
prazna_lista = []
print(prazna_lista)
pritn(type(prazna_lista))

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
**`Izvorni kod: kod-211_rad-sa_listama.py`**
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

del(karakteri[3]) # funkcija del
print(karakteri)

izbrisan_karakter = karakteri.pop(4) # metoda pop, u slucaju da hocemo da sacuvamo izbrisani element
print(karakteri)


karakteri.clear("")
print(karakteri)

##### provjeri da li je odredjeni element u listi

karakteri = ["Goku", "Krilin", "Bulma", "Chi-Chi", "Yamcha", "Picolo", "Bulma"]
print(karakteri)

print(len(karakteri)) # funkcija len

print(karakteri.index("Bulma")) # metoda index

print(karakteri.count("Bulma")) # metoda count, prebrojavanje koliko se trazeni element pojavljuje u listi

karakteri.sort() # metoda sort
print(karakteri)

karakteri.reverse() # metoda reverse
print(karakteri)

karakteri_novi = karakteri.copy() # metoda copy

print(karakteri_novi)

karakteri_novi.sort()
print(karakteri_novi)

print list(string_karakter)
# funkcije min i max, vracaju najmanji ili najveci element liste respektivno
karakteri = ["Goku", "Krilin", "Bulma", "Chi-Chi", "Yamcha", "Picolo", "Bulma"]
print(karakteri)
print min(karakteri) # funkcija min
print max(karakteri) # funkcija max

# konverzija stringa u listu
string_karakter = "Goku"
type(string_karakter)
print(string_karakter)
```

## Tuples - torke (tip podaktovne strukture, veoma slican listama) - ()
Tuples predstavlja niz nepromjenjivih clanova. Clanovi unutar tuple-a mogu biti istih ili razlicitih
tipova. Tuple definisemo nabrajanjem objekata odvojenih zarezom, cak i ako je u pitanju jedan jedini
clan moramo imati zaraz, u suprotnom se gubi osobina tuple-a.

Razlikuju se od liste po tome sto su **nepromjenjive (immutable -ne mogu se mijenjati).**

Tuple mozemo prevosti kao torke, a izraz dolazi iz matematike od pojma _n-torka_ (eng.tuple) koji predstavlja
konacni niz (poznat kao uredjena lista) od n objekata, od kojih je svaki specifincnog tipa.

Clanovi torke su smjesteni u obicne zagrade _()_ i razdvojeni zarezom _,_. Clanovi torke mogu biti same 
torke.

**`Izvorni kod: kod-220_rad-sa-torkama.py`**
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

### list of tuples
koordinate = [(4,5), (6,3), (7.4)]
print(type(koordinate))
print(len(koordinate))

## tuple su nepromjenjive strukture
koordinate = (4, 5)
print(type(koordinate)) # funkijca type()
print (len(koordinate)) # funkcija len()
print(koordinate.index(5)) # metod index
print(koordinate[0]) 
print(koordinate[1])

koordinate[1] = 10 # dobicemo gresku

### pristupanje elementima torki slicno je kao i kad pristupamo listama
karakteri = (1,2,3,4,"a","d","-") # pristupanje elementima tuple-a 
print(karakteri[1])
print(karakteri[2:4])
print(karakteri[-2:]
print(karakteri[::2]) # pristupanje svakom drugom elementu

# konverzija drugih tipova u tuple
karakter_ime = "Goku"
type(karakter_ime)
karakter_godine = 15
type(karakter_godine)

karakter_ime = tuple(karakter_ime)
type(karakter_ime)
print(karakter_ime)
karakter_godine = tuple(karakter_godine) 
karakter_godine = tuple(str(karakter_godine))
type(karakter_godine)
print(karakter_godine)

karakter = karakter_ime + karakter_godine
type(karakter)
print(karakter)

# brisanje tuple-a
del(karakter[3]) # brisanje elemenata tuple-a nije moguce
del(karakter)
```

#### Rijecnici - Dictionaries - { }

Rijecnici su tipovi podataka, opet slicni listama, ali za razliku od listi indeksiranje se obavlja kljucevima.

Za lakse razumijevanje ih mozemo uporediti sa klasicnim rijecnikom za prevodjenje rijeci sa jednog jezika na 
drugi, gdje imamo strukturu strana rijec na lijevoj strani i detaljno objasnjenje rijeci na desnoj strani.
Ako navedenu analogiju primijenimo rijecnicima, kao tipovima podataka u Python-u, onda rijec predstavlja kljuc
(key), dok detaljno objasnjenj predstavlja vrijednost (value). 

Elementi rijecnika su smjesteni u viticaste zagrade **{ }** a parovi elemenata su razdvojeni zarezom **,**. 

```text{kljuc:vrijednost} ({key:value})```

Bitno je napomenti da kljuc (key), mora biti jedinstven, ne mozemo imati dva ista kljuca. 
```text
{"kljuc_1:vrijednost_1", "kljuc_2:vrijednost_2", "kljuc_3:vrijednost_1"} - ispravno
{"kljuc_1:vrijednost_1", "kljuc_1:vrijednost_2", "kljuc_3:vrijednost_1"} - nije ispravno 
```

**`Izvorni kod: kod-230_rad-sa-rijecnicima`**
```python
karakteri={} # prazan rijecnik
print(karakteri)

karakteri_osobine={"Goku":"Vegeta", "Picolo":"Namek", "Krilin":"Zemlja"}
print(karakteri_planete)
print(type(karakteri_planete))

karakteri_planete["Bulma"]="Zemlja"
print(karakteri_planete)
karakteri_planete["Goku"]="Namek" # prepisace trenutnu vrijednost ako postoji

del(karakteri_planete["Goku"]) # brisanje elementa

print(len(karakteri_planete)) # primijetimo da se broje parovi

print(karakteri_planete.keys()) # metoda keys() nad rijecnicima, ispisuje sve kljuceve (keys), nema argumente
print(karakteri_planete.values()) # metoda values() ispisuje vrijednosti elementa, nema argumente
print(karakteri_planete.items()) # metoda items() ispisuje kljuc: vrijednost elementa, nema argumente

# metode get i setdefault
karakteri_planete={'Goku':'Vegeta', 'Krilin':'Zemlja', 'Bulma':''}
print(karakteri_planete.get('Goku','Karakter ne postoji u bazi'))
print(karakteri_planete.get('Pikolo','Karakter ne postoji u bazi')) # metoda get() nad rijecnikom vrsi pretragu po zadatom kljucu, u slucaju da kljuc ne postoji vraca default-nu vrijednost, vrijednost koja je proslijedjena kao drugi parametar

print(karakteri_planete.setdefault('Pikolo','Karakter nema definisanu planetu')) # kljuc ce biti kreiran u slucaju da ne postoji, a vrijednost ce biti podesena na vrijdnost drugog proslijednjenog parametra
print(karakteri_planete.setdefault('Bulma','Zemlja')) # obzirom da kljuc postoji, nece doci do promjena

# metode pop i update
karakteri_planete={'Goku':'Vegeta', 'Krilin':'Zemlja', 'Bulma':'Zemlja'}
obrisan_karakter=(karakteri_planete.pop('Goku')) # pop() metoda prilikom brisanja key:value, zadrzava vrijednost (value)
print (karakteri_planete)
print (obrisan_karakter)

# spajanje rijecnika mozemo izvesti upotrebom metode update()
karakteri_1_planete={'Goku':'Vegeta', 'Krilin':'Zemlja', 'Bulma':'Zemlja'}
karakteri_2_planete={'Chi-Chi':'Zemlja', 'Vegeta':'Vegeta', 'Bulma':'Namek'}
karakteri_1_planete.update(karakteri_2_planete) # update() metod nad rijecnicima prosiruje prvi rijecnik vrijednostima iz drugog, u slucaju da imamo dva ista kljuca, kljuc iz prvog rijecnika bice zamijenjena kljucem iz drugog rijecnika
karakteri_1_planete={'Goku':'Vegeta', 'Krilin':'Zemlja', 'Bulma':'Zemlja'}
karakteri_2_planete={'Chi-Chi':'Zemlja', 'Vegeta':'Vegeta', 'Bulma':'Namek'}
karakteri_2_planete.update(karakteri_1_planete)
```

**`Izvorni kod: kod-231_konverzija_mjeseci.py`**
```python
# recimo da zelimo konvertovati kratke nazive mjeseca u standardne
# Jan -> Januar
# Mar -> Mart

konverzijaMjeseci = {
    "Jan": "Januar",
    "Feb": "Februar",
    "Mar": "Mart",
    "Apr": "April",
    "Maj": "Maj",
    "Jun": "Juni",
    "Jul": "Juli",
    "Avg": "Avgust",
    "Sep": "Septermbar",
    "Okt": "Oktobar",
    "Nov": "Novembar",
    "Dec": "Decembar"
}

print(konverzijaMjeseci["Jan"])
print(konverzijaMjeseci["Feb"])
print(konverzijaMjeseci["Mar"])

print(konverzijaMjeseci.get("Jan")) 
print(konverzijaMjeseci.get("Dec"))
print(konverzijaMjeseci.get("Dese","Nije validan kljuc")) # ako koristimo get necemo dobit gresku vec empty
```
## Funkcije

Skup naredbi koje po pozivu izvrsavaju odredjene zadatke. Funkcije sluze takodje za bolju organizaciju koda.

Funkcije se definisu pomocu kljucne rijeci **def**, kad god se pojavi def na pocetku linije, python zna da korisnik zeli kreirati funkciju i stim u vezi se i ponasa.

Sintaksa funkcije:

```text
def naziv_funkcije(parametri): # parametri su opcioni, ali ako postoje moraju biti definisani/proslijedjeni
  blok naredbi # argumenti (poznat jos kao tijelo funkcije)

naziv_funkcije(argumenti) # poziv funkcije
```

Iz sintakse mozemo zakljuciti da je naziv_funkcije identifikator kojim pozivamo funkciju, dok parametri sluze
da bi se definisale vrijednosti koje se mogu proslijediti kao parametri naredbama unutar tijela funkcije.

**`Izvorni kod: kod-255_rad-sa-funkcijama.py`**

```python
def zdravo_svijete(): # funkcija bez parametara
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

Kada zelimo dobiti povratnu informaciju iz funkcije koristimo naredbu **return**. Sa ovom informacijom
mozemo nastaviti manipulaciju kroz daljni dio koda. Naredba return se moze pojaviti samo unutar tijela
funkcije. Takodje kada zelimo da funkcije mogu medjusobno komunicirati, razmjenjivati informacije koristimo
return naredbu. 

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

### Funkcija ne mijenja sadrzaj promjenjive
**`Izvorni kod: kod-261_rad-sa-funkcijama.py`**
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

## While petlja - (Izvrsavaj blok koda sve dok je ispunjen uslov ...)

While petlja predstavlja strukturu u Python-u koja nam omogucava da prolazimo 
kroz isti blok koda vise puta, onoliko puta koliko smo to zadali inicijalnim 
uslovom, odnosno sve dok uslov ima vrijednost Tacno (True) ili dok nasilno ne 
prekinemo uslov naredbom prekida (**break**).

Dakle svakom iteracijom kroz blok koda, while petlja ce da izvrsi sve sto se 
nalazi u tijelu petlje. Naravno, uz while petlju mozemo kombinovati i uslove
 cime dobijamo na brzini koda i vecoj efikasnosti.

Ono sto je bitno napomenti kod while petlje, ona se koristi uglavnom kada 
unaprijed nemamo definisan broj iteracija. 

**``Izvorni kod: kod-310_while_brojac.py``**
```python
i = 1
while i <= 10:
  print("Vrijednost i je : " + i)
  #i = i + 1
  i += 1

print("Kraj brojaca")
```

**`Izvorni kod: kod-311_igra_pogadjanja.py`** 

```python
# primjenimo do sad nauceno
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

### Naredba prekida (**break**)

**`Izvorni kod: kod-312_demonstracija-naredbe-break.py`**

```python
karakter_opis = {}

brojac=0
limit=10

while brojac <= limit:
	karakter_ime = input("Unesi ime karaktera: ")
	karakter_godine = input("Unesi godine karaktera :")

	if int(karakter_godine) <= 0:
		print("Godine ne mogu biti manje od 1!")
		break
	else:
		karakter_opis[(karakter_ime)] = (karakter_godine)
		brojac+=1 

print(karakter_opis)
```

### else kod While petlje

Kao sto smo vidjeli sa uslovom **if**, takodje mozemo koristiti granu else 
prilikom konstrukcije while petlje, ali trebamo imati na umu da se else izvrsava
 samo jednom, ako i samo ako je glavni uslov while petlje netacan (False). 
 Naravno ukoliko unutar while petlje imamo naredbu **break** koja je izvrsena, 
 else naredba ce biti preskocena.

**`Izvorni kod: kod-313_demonstracija-grane-else.py`**

```python
karakter_opis = {}

brojac=0
limit=2

while brojac <= limit:
	karakter_ime = input("Unesi ime karaktera: ")
	karakter_godine = input("Unesi godine karaktera :")

	if int(karakter_godine) <= 0:
		print("Godine ne mogu biti manje od 1!")
		break
	else:
		karakter_opis[(karakter_ime)] = (karakter_godine)
		brojac+=1 
else:
	# sadrzaj rijecnika ce biti ispisan samo ako se 
	# kompletan program izvrsi bez okidanja/trigerovanja naredbe break
	print(karakter_opis) 
```



## For petlja

For petlju mozemo nazvati specijalni tip petlje u Python-u, a za razliku od while petlje, for petlju
 koristimo kada zelimo da vrsimo iteraciju kroz tijelo petlje ako unaprijed znamo koliko puta je to 
 potrebno.

Vrijednosti se uglavnom zadaju kao predefinisane ali mozemo koristiti izvore poput lista, stringova,
 rijecnika.

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

Prije nego napisemo kod potrebno je kratko objasnjenje algoritma. Algoritam sortiranje mjehuricima, 
ima za cilj da nad zadatim nizom nasumicnih/slucajnih brojeva izvrsi sortiranje od najmanjeg ka 
najvecem. Ovakvi tipovi zadataka predstavljaju osnovne koncepte teorije algoritma, a mozemo ih naci,
kao zadatke, na intervjuima u velikim firmama poput Google-a, Amazon-a, Facebook-a, Microsoft-a ...

Predpostavimo da imamo niz brojeva:

```text
[4,2,1,5,3]
```
Primjenom algoritma sortiranja mjehuricima, svakom novom iteracijom, svaki element niza ce se 
uporedjivati sledecim, u slucaju da je prvi element veci od sledeceg, zaminijece mijesta, u 
suprotnom prvi element ostaje na svom mjestu. Ovaj proces se nastavlja sve dok se svi elementi 
konacno ne sortiraju od najmanjeg ka najvecem. Dakle, procedura sortiranje ce se obaviti sledecim 
redosledom:

```text
tbd.
[2, 4, 1, 5, 3]
[2, 1, 4, 5, 3]
[2, 1, 4, 3, 5]
[1, 2, 4, 3, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]

Pocetno stanje         |   [4,2,1,5,3]   |   Objasnjnje
_______________________|_________________|_________________________________________________
Nakon prve iteracije   |   [(2,4),1,5,3] | 4 i 2 mijenjaju mjesta jer je 4 vece od 2
                       |   [2,(1,4),5,3] | 4 i 1 mijenjaju mjesta jer je 4 vece od 1
                       |   [2,1,(4,5),3] | 4 i 5 ostaju na svom mjestu jer je 4 manje od 5
                       |   [2,1,4,(3,5)] | 5 i 3 mijenjaju mjesta jer je 5 vece od 3
_______________________|_________________|_________________________________________________                    
Nakon druge iteracije  |   [(1,2),4,3,5] | 2 i 1 mijenjaju mjesta jer je 2 vece od 1
                       |   [1,(2,4),3,5] | 2 i 4 ostaju na svom mjestu jer je 2 manje od 4
                       |   [1,2,(3,4),5] | 4 i 3 mijenjaju mjesta jer je 4 vece od 3
                       |   [1,2,3,(4,5)] | 4 i 5 ostaju na svom mjestu jer je 4 manje od 5
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

## Klase i objekti

Znamo od pocetka da je Python objektno orijentisani programski jezik, sto znaci da su svi podaci predstavljeni kao objekti. Prihvatanjem objektno orijentisanog nacina programiranja, nasi programi, ali sam kod, postaju ekstremno korisni, organizovaniji i mocniji.

Kada programiramo susrecemo se sa razlicitim tipovima podataka, takodje susrecemo se sa razlicitim  strukturama podataka, ali sta u slucaju kad ne mozemo predstaviti neku pojavu iz prirode sa vec postojecim tipovima ili strukturama podataka?

Upravo su nam za to korisne klase i objekti. U Python-u mozemo krairati klase (definise vas licni tip podatka, ponasa se kao template, patern kako nesto treba da izgleda). Objekat je podatak u memoriji, pravi podatak kreiran iz klase, sto se jos naziva instanciranje objekta.

Metode su funkcije unutar klase, koje se koriste da izvrse neku akciju nad odredjenim tipom objekta. 

Sintaksa klase:

```text
class naziv_klase():                 # kljucna rijec class
  def__init__(self,param_1,param_2): # konstruktor/funkija __init__
    self.param_1 = param_1           
    self.param_2 = param_2

klasa = naziv_klase()                # instanciranje objekta
```

Iz sintakse vidimo da u slucaju pojave kljucne rijeci **class** Python automatski prepoznaje da je rijec o novoj klasi. Takodje, primijetimo da je za instanciranje objekta, potrebno da imamo funkciju ** __init__ ** zaduzenu za instanciranje, koja se jos naziva konstruktorom i uvijek prihvata minimalno jedan element **self**. Taj prvi element, koji prima svaka funkcija unutar klase, se uzima kao licni, prisvojni, sebi svojstven, element i sve sto se radi nad samim objektom se referncira pomocu ovog elementa. 

Prazan objekat:

```text
class prazna_klasa():
  pass

klasa = prazna_klasa()
```
Primijetimo da prethodni objekat nema funkciju inicijalizacije, postoji podrazumijevana funckija, koju ne vidimo, ali moramo znati da je ovaj objekat prazan objekat.

Posto ne postoji student tip podaka, kreiracemo klasu **Student**.

**`Izvorni kod: kod-555_student.py`**
```python
class Student:
  # inicijalizacija klase (inicijalna funkcija)  
  def __init__(self, ime, smjer, ocjena, brucos):
    self.ime = ime
    self.smjer = smjer
    self.ocjena = ocjena
    self.brucos = brucos
```

**`Izvorni kod: kod-556-main.py`**

```python
from student import Student

# kreiranje instance Student student_prvi objetka
student_prvi = Student("Goku", "Programiranje", 8, False)
print(student_prvi)
print(student_prvi.ime) # pritstup objektu ime unutar objekta student_prvi
print(student_prvi.ocjena)
# student_prvi.ocjena znaci da imamo pristup ocjeni instance student_prvi

student_drugi = Student("Krilin", "Ekonomija", 8.3, True) 
print(student_drugi.brucos) # pritstup objektu brucos unutar objekta student_drugi
```

```text
      Student                  <= naziv klase
______________________________
ime      |    "Goku"           <= objekat ime unutar objekta Student
_________|____________________
smjer    |    "Programiranje"  <= objekat smjer unutar objekta Student
_________|____________________
ocjena   |    8                <= objekat ocjena unutar objekta Student
_________|____________________
brucos   |    False            <= objekat brucos unutar objekta Student
         |
```

### metode - funkcije unutar klase (funkcije objekta)

**`Izvorni kod: kod-557_funkcija-unutar-klase.py`**

```python
class Student:
  naziv_fakulteta = "Elektrotehnicki" # podrazumijevana/defaultna vrijednost
  def __init__(self, ime, smjer, ocjena, brucos):
    self.ime = ime
    self.smjer = smjer
    self.ocjena = ocjena
    self.brucos = brucos

  def dobar(self):
    if self.ocjena > 8:
      return True
    else:
      return False
```

**`Izvorni kod: kod-558_main.py`**

```python
from student import Student

student_prvi = Student("Goku", "programiranje", 7.9, False)
print(student_prvi.naziv_fakulteta)
#student_prvi.ime = "Goku"
#student_prvi.ocjena = 7.9

print(student_prvi.ime)
print(student_prvi.dobar())
student_prvi.naziv_fakulteta = "Prirodno Matematicki"
student_prvi.smjer = "Fizika"
student_prvi.ocjena = 9.0

print(student_prvi.ime)
print(student_prvi.naziv_fakulteta)
print(student_prvi.dobar())
```

U prethodnom primjeru smo vidjeli jednu od metoda **dobar()**, ali ajde da 
pogledamo malo detaljnije o cemu se radi.

Recimo da zelimo funkciju u nasoj klasi **Student** koja nam ispisuje 
kompletan sadrzaj instanciranog objekta **Student**, ali i omiljenog pisca tog
studenta. Za ovo su nam potrebne dvije metode unutar klase **Studnet** koje 
cemo nazvati **student_opis** i **student_pisac**.

**` Izvorni kod: kod-559-metode.py`**

```python
class Student:
  naziv_fakulteta = "Elektrotehnicki"
  pisac = "nije definisan"
  def __init__(self,ime,smjer,ocjena,brucos):
    self.ime = ime
    self.smjer = smjer
    self.ocjena = ocjena
    self.brucos = brucos

  def dobar(self):
    if self.ocjena > 8:
      return True
    else:
      return False

  def student_opis(self):
    print(f"Ime studenta: {self.ime}, Naziv fakulteta: {self.naziv_fakulteta}, Smjer: {self.smjer}, Ocjena: {self.ocjena}, Brucos: {self.brucos}, Pisac: {self.pisac}")

  def student_pisac(self):
    print(self.pisac)
```

**`Izvorni kod: kod-560_main.py`**

```python
from student import Student

novi_student = Student("Goku", "programiranje", 7.9, False)
print(novi_student.naziv_fakulteta)
#novi_student.ime = "Goku"
#novi_student.ocjena = 7.9

print(novi_student.ime)
print(novi_student.dobar())
novi_student.naziv_fakulteta = "Prirodno Matematicki"
novi_student.smjer = "Fizika"
novi_student.ocjena = 9.0

print(novi_student.ime)
print(novi_student.naziv_fakulteta)
print(novi_student.dobar())
print(novi_student.student_opis())
print(novi_student.student_pisac())
```

### Naslijedjivanje - podklase

U slucaju da planiramo kreirati novu klasu, a vec unaprijed znamo da imamo ili
da vec postoji klasa koja sadrzi vecinu metoda koje trebamo koristiti, medjutim
mi trebamo definisati jos par novih objekata ili novih metoda, u tom slucaju 
koristimo naslijedjivanje ili podklase, tako sto kreiramo novu klasu koja 
naslijedjuje staru klasu.

Nova klasa ce imati sve osobine stare klase sa novim opcijama. 

**`Izvorni kod: kod-565_kuvar.py`**

```python
class Kuvar:
    def priprema_mesa(self):
        print ("Priprema pileceg mesa.")

    def priprema_salate(self):
        print("Pirprema Cezar salata")

    def priprema_specijalnog_jela(self):
        print("Priprema rebarcadi")
```
**`Izvorni kod: kod-566_kineski_kuvar.py`**

```python
from kuvar import Kuvar

class KineskiKuvar(Kuvar):
    def priprema_rize(self):
        print("Priprema rize na kineski nacin")

    def priprema_specijalnog_jela(self):
        print ("Pekinska patka")
```

Dakle, sve metode koje su definisane u klasi **Kuvar** , koja se jos naziva nadklasa, mogu se koristiti u novoj klasi **KineskiKuvar** , koja se jos naziva podklasa.
Mozemo primijetiti redefinisanje metode **priprema_specijalnog_jela** u novoj
klasi **KineskiKuvar**. U slucaju redefinisanja metode, prilikom pozivanja 
metode **priprema_specijalnog_jela**, koristi se nova redefinisana metoda. 

**`Izvorni kod: kod-567_main.py`**

```python
from kuvar import Kuvar
from kineski_kuvar import KineskiKuvar

novi_kuvar = Kuvar()

novi_kuvar.priprema_mesa()
novi_kuvar.priprema_specijalnog_jela()

novi_kineski_kuvar = KineskiKuvar()

novi_kineski_kuvar.priprema_rize()
novi_kineski_kuvar.priprema_mesa()
novi_kineski_kuvar.priprema_specijalnog_jela()
```

## Rad sa datotekama (fajlovima)

Fajl ili datoteka, predstavlja kontejner, mjesto gdje skladistimo, pohranjujemo
podatke. Na ovaj nacin podaci su trajno sacuvani na disku, za razliku od radne
memorije i moze im se naknadno pristupiti iz drugih programa, ali se moze 
vrsiti i razmjena izmedju razlicitih sistema.

### Citanje iz eksternog fajla
- dosta puta imamo potrebu za citanjem sadrzaja iz drugih fajlova
- parsiranje teksta ...
- apsolutni, relativna lokacija

```text
access_mode | rezim rada nad fajlom nakon otvaranja 
____________|________________________________________________
r - read    |otavara datoteku samo za citanje, ovo je default  
(citanje)   |rezim, ako nije navedeno drugacije, uzima se 
            |ovaj rezim
____________|________________________________________________
r+          |otvara datoteku za citanje i pisanje 
____________|________________________________________________
w - write   |otvara datoteku samo za pisanje, ako datoteka    
(pisanje)   |vec postoji snima se nova datoteka preko nje, 
            |ako ne postoji kreira novu datoteku. 
____________|________________________________________________
w+          |otvara datoteku za pisanje i citanje, ako 
            |datoteka vec postoji snima se nova datoteka 
            |preko nje, ako ne postoji kreira novu datoteku
____________|________________________________________________
a - append  |otvara datoteku za dodavanje i citanje, dodaje
(dodavanje) |liniju na kraju datoteke, u slucaju da datoteka
            |ne postoji kreira se nova
____________|________________________________________________
a+          |otvara datoteku za dodavanje i citanje, dodaje
            |liniju na kraju datoteke, u slucaju da datoteka
            |ne postoji kreira se nova
```


**`Sadrzaj fajla: fajl-605_karakteri_porijeklo.txt`**
```text
Goku - Vegeta
Krilin - Zemlja
Piccolo - Namek
Frieza - Universe 7
```

**`Izvorni kod: kod-606_rad-sa-fajlovima.py`**
```python

# otvoren fajl
# funkcija open()
karakteri_fajl = open("fajl-605_karakteri_porijeklo.txt", "r")

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

# obzirom da se tokom rada sa fajlovima koristi pomocna memorija (buffer), 
# nakon rada sa fajlom potrebno je da se pozove funkcija close(), kako bi se 
# podaci upisali u fajl
# cak i ako koristimo funkciju write() ali na kraju ne pozovemo close()
# podaci ce biti izgubljeni
# moguce je zadati velicinu pomocne memorije kao treci parametar u funkciji
# open() reda bajta.
karakteri_fajl.close()
```

## moduli i pip alat
- python fajl koji mozete importovati unutar vaseg python koda
- kako kreirati svoj modul
- kako instalirati module (list of python modules on google) pip paket manager
- build-in moduli (ugradjeni) i eksterni moduli
 
**`Izvorni kod: kod-655_korisni-alati.py`**
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

### upisivanje u eksterni fajl

**`Izvorni kod: kod-607_rad-sa-fajlovima.py`**

```python
# dodavanje na vec postojeci fajl
karakteri_fajl = open("fajl-605_karakteri_porijeklo.txt", "a")

karakteri_fajl.write("Bulma - Zemlja")
karakteri_fajl.write("\n Chi-Chi - Zemlja")

karakteri_fajl.close()

# upisivanje u novi fajl
karakteri_fajl = open("fajl-608_karakteri_porijeklo.txt", "w")

karakteri_fajl.write("Bulma - Zemlja")
karakteri_fajl.write("\n Chi-Chi - Zemlja")

karakteri_fajl.close()
```

## moduli i pip alat
- python fajl koji mozete importovati unutar vaseg python koda
- kako kreirati svoj modul
- kako instalirati module (list of python modules on google) pip paket manager
- build-in moduli (ugradjeni) i eksterni moduli
 
**`Izvorni kod: kod-655_korisni-alati.py`**
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
%PDF-1.4
%����
1 0 obj
<</Creator (Chromium)
/Producer (Skia/PDF m80)
/CreationDate (D:20200401085019+00'00')
/ModDate (D:20200401085019+00'00')>>
endobj
3 0 obj
<</ca 1
/BM /Normal>>
endobj
7 0 obj
<</Filter /FlateDecode
/Length 5574>> stream
x��]���q����� ��3	�;��v0@��Xv�HQGJ�Ţ�W������n�d�X�Ձ�N�4�y���_��Ѫ.����O�~�ۗ����ק���������n;��a|��_��z���������?��_�ox_H桔��uZ��������_~��}���?Ӌ���	]�J��6��~���7������������A:��!ai0���;�����G��`Ǘ~��|�N�N������D�:Q�����2��4P�#��1��?N}����G�n�7�^���>?�O�����R����}�LX�A5��;V&5]f����i��)�j��dT����;���an4������L;�A����+'���/�>�{e�oFj(�i�{;�h⼑,4�c��J07ҟ��t�{W�����i~>��w�fd��'���	����i_u�:1)�?aƍ�R���c1�4�֍6����%��G��y�.����ō[O�]�#� �1Ӣ�c���� ��ڵ;�Qe;O<��AHi��L*���Rwv�2�z�Y3t�,$�sʨ�]_�'lAgV�4��:���2+�M��of��K�������[��6�,����NR�YRL�KjϪL�sj�%�R���p�K.��p"�iH�้���\�>V:������@}ߑ~��v�L�0�'K,��Iκ�ʚ���^Y��2}5}������n�����ݞE|�z��6G�Ћ�?ȇ�,�/3K��4/��DuW3m?������G5�Y��ѥ�*�11m�5�R����/b�y�n����t��(���z�?����o7=aI�beъOr�X�`��oZv��
��N��%����7t�X�+�*Ġ3�ݯ�u��v�	��/e�,�f1EP��j�<ܖ����lxB��,��j;t*����TMnπX�Y��i��԰��kp��#�j��*����soν�㼷g����iL���p����;x��Q�n��c�ͽ��U7�5�8��O�8y�auog�j|��;���ڋ̯�%#�ʘ�P��<�nt{,�ò4M�F�R�@1%�L)��M<h�'[�-�K�����RgҒ�������a�	nӿ�Fv������-�V�mȂ9�2���O��`���Z	�*���/=m�mZ{�7�f��Jm���p��,�ܘ������n�a��š-����02���<^��'�Om){m~U���OC4�d����Dc�$�{ƚm�Dc,��:
1V9~׹�Bt���L�i���#�b2��#�vZ[���#�Їa�j�b�����&�Sn��ݼ��_���I��y�:nff��a|z��h���/W��az\���v�\%;.�W{Y�ܼ���`�%cj䱅���|���`�bv+/t(X~�W�9V��hY�b�-+�������w����[Q� �� B7X"����E.�\��^�`�%6��x�P��q �<g:��!c���ޠ�Iq���!\G|m��Q7 iL)��f
�4��7���sf��<��Y^��� ȁ�HF��.�#�e�����#r��,�c)��-�Aj��:P[~�+��-�|U�z�����A����@���Ew��X�\�۪�q�js��`˙��x�ɪ�Wڭ�}���b�q=̈��>O���#v��<K�y��ti�?�j����"j>n������}���?Ԙ��J���m��м���`�'cnƱ� u�<��
n^�Pp�?�����NZ֠�p�@�
�F~v;�}���f�,D�c=+K�啪�6қ�x.�'��TN��{�xيO�[���Μ�R2��(%��^)妽R�mG�DRi���PJ�mo��6���F)�ֽ=���J)���(�ܺWJC۬����T|9����������b\�8.ƿ��L_�dQ�����^��p�z�G�D�8(�ܶ7hs[���(%��!�
����J)��Rn*�Rn��JWj;(�ܸWJ�����Jil^V}p哲���ֱ����y��rv+7�tX�~�׺?Jʮ;i]�uík��|�����w|S��`���0��,%�;8���[����ɍL�b!��_X�i(T��# ��;��;��$�-�#Ƅd��	��D�����`����}Lj:�73���I�� �:�i��WȪ9�Q�^�I^��[,���I\�)�ٜ���j��!AITreeN1�.�P�"�ܻ�d*6�Og&�!�X�"�j*,~Ur��!���(�������i-���s� �tǈ���a"~>�	>��W1\�D��	Y0�0/�y���{�} �	�@"J�@�um��"�n�EWȨm~�AFcW��Y�� ��B��A��p�� ���[�Rl� '`�.��z��:����òDpg <��";W�Z�OO=i��c���f�R��<Q���)�ސ>V5��p��-f"�*H��>^"I3�aG�8&��7��9�8~h��Cʕ��`����%�\�
4����Y����X�Uy����P�F��r�\ ��J�Յ�7����%7�쩩Vgu��F��!b�	��b�Z�/u�6;���ir�	_J�:�T�|�T*���ʶ<�R�1QJ���]�EuOm�ѫ�<�����<���Qr/�����I���hU3;�K�$��bGt�ш �����1�^pT��;�Br
3�L�vi�?��>;݊C͘"�| �P�}?7�IU@�2,��f�m͆�p�||��{�zeO��5[�b�Z&���`_0��w��'ƖɻR�U��4;$�}驡p@Z�U�'8��Hce��ʣ�ʥ���!����l0ٰ�p�'��K�R���r�V�4�91b����Wn`�	�~?���L�9�v�/7��ݻ�1�&����V嬽��}R��w}����4�;|��V�|�i�_�S����xc��(5���y��'�  t�����W��c��N��Q���~̵!��Լun�'	���J�'e�Ӈ�� ra{p$Ϸ�$�e�4�3�E&��0�`9;���dIR�`E��G�$��qy']����b7d�4XE g�"�y�<���rir�����S�E�X��lj�ސT�`KA�������A	
x��lR%B�^%7�����`r�H։���&	?�Ɨ�5��K�g��O:2ή���7�Y�g��/�<�ݏ�Rޮb����;f�I��B<��B_�j�H;�v�a�
�������<;�Ҥ�ْ��s���l)J��P��'�:��k�9��.w���٠|��p��K>B_U=�N��Eb{��'�C��W���U��[2����U�.��t�����c�+m�<��m'��S�������r��w1a��5��w#-�����(���?[S�}��Ǚ`x���ZN��e^��UhR0Z�O��!@ny��;�	�n|

���0)�P2�}�ٳ2�x�yP�|Gѩ��F��i�X��V`X ���GP$�I�Dv�&�|���%�s3~��/KA_�o���+��+'�x�9k�s�Tz������9��ʝ�D�-�#�-�߉]��ც��'w�9e;�~GMn>�Qu����i;�ݞ�a��88tq:��e�@� �2����UUѽ� ��p����NnHP��Rc�/����J��U��n>�!|K�|q7�iX�+^C?����~������ש�|av�W��yD�I!���|���`�fW�	ӛ����^?+�yb�m�B����2��g��8���"�+H�)��� �����Թ*ao�syr9���<@9�߸��&���ﾚX"�GxŬ*
)f%4�E䙫��5���o��1kև������������_oь_�Ǡ���S�>cŚ@\��V���'E�����j�sן3����6\���Quy�ܕgR�Z̿3�'z
��ڿ�<-DE�f��-dA�w��n����ߔ��r)|n+,2~�5쬆� "��Yx���RC� �f��p~\Qn���g9C/A�=�P���ۯX��b��i0�B���*��8�� Sr܃~ WЏ�ֻ�?&��$ �I�c�Mw&��W҇Xs�v��}�P	N��3���Hޅ(x� �C9T��+�+BΨ����|e^H�9̜m4�`�� ���y�_-I�D�&���wOd�f[7�K���Y�[����v�<(�c�,D���r���%m�G۸{������]�g#�6P�]����[�h���W
�ao׉/�FU*
��?x[�Kspo��ͩ,%�9g�>�	��#�&X��^���bw8�p��*@Xӟ*N����]��k�߹�P�D�5�\n�Q�Ϻ�6�^�շD����v8��ܹ�:.)���dב�'4�ٯj�AU��� �-�+�y�6��bH9 ��!Ne�S�am$����Qnv�5��D_�Y ��C0�P�T�F!� ;���vV�<��w�����_�> �G�U9>�j�q]b_2�`B�$X���tÅ��0�^7��,��/z�gQ9o�$x�ȡyT����.��Y���bptx�3z��2�\Z?|�+{�*cb�vn�}M�AC�ST�>4,/����<_����9��|�	m��􏗇D��{C��{�|<�!�$�(�|��E#蚼r�y�{	ND�&B���O��|p���פ!��` L��H]�ٌ��{O�J�����g@kƄ0+h?�33��,RM/�T�F��U����ذ]K�tv>j�G�,���U��U�;�������}h`7=-�"p��T!��|��L��K�]r%�R�����)�2~z�Zb^d>l<���Щ��a�n�2S�Xԕ����V��m����SS.x��N-���E��9���4d�%���_<��jTY�a��������
���3�<8��!>���W�A�W��d��ԝG[���I��_U
Xۉ�tށ��Tw����U�`ߟ������Wfa�⒳�цS}"�O�Ap^g�ັ���R؞~�D���[����֤�`P��`�`s� �G�`���N/�L�Kr��Al|��g��.\���i�~����5�NU]�O]�r���ޑ��[#���Z���A���dJ��_b�/��Σﭧ�/��O�{�ޙs�P4�]�Y�j�Jc��W�]̱��H09T��U`c�37!���%��n��\pqK��7�q/�iN�K2bE:l�j�5�잤��{������JL|kF���-%�؋��ܷ e���a�:��1��1������R���p������qR��y�T{���
�K��>�Tߙes2_f�|��w�#����r4�_���	%K�q�������r�%���mT4���f!?T�J֥�C=x��A�Z��b^p����J<~�>ov��ĥٱA#�pqs�2F�0?�a�A�w1��sm0���ʂo��d-�IF=-n�G���>�.u
endstream
endobj
10 0 obj
<</Type /XObject
/Subtype /Image
/Width 64
/Height 64
/ColorSpace /DeviceRGB
/SMask 11 0 R
/BitsPerComponent 8
/Filter /FlateDecode
/Length 5354>> stream
x��XTW�}˖ٙY��c>Ԩ��{��bA�ŀD���c�F�S�5�����AQPD@P�� R�������
~ƴs�'�sg������{����[��?\KqkC�:�t;rˎ�K2��{��x��bS ��:���kC\;��^R�4�Cn�%�Ǒ�q�	2S~���4�тF��#u�?�6��*g�%��ȝ	$k�잓<g����G�G��0�� �@ d��HA����$~ I*9"���$��,g���&w)�x�:���:e�����3�H��4�тF�CR�,��Һ1Z2�L�L��w�?���.c�ת��p��x_C�ۧ:�~e����s ���4�тF�CR�,�a��w�ɑ���m{�G���ܓL�V��MY�(!�C���&�^�����%#�S愁 �hA#�!)BⰀџ[SZ�����1��ײ�sTy+��h���L;��1�K̍ň#ća�P	C_:�����F�CR�,�a��L���^_�{q���]���}�^S��՝j+\Y*f���Ĝ �/��M�,��1�"�� d!.=�q��S�?�� rk<��N���+�ė쭡i�<!����Q���3�%*3�ϡ"�� d!���:�+���3���5��5��	�sĻ��,7�u��=%!��`��:	)BⰀ�2+.���ʧWE����m�cMW���}� �s��V��7��vH�9Y��F�3]���eO���YS�]�;��!q�<@o�w��J��F�� A�f��`SX#�W��?M���+�n�;\�p�Q��A�7ь�nUB�N�`����`u d�T4i�o��`SX# b�AE'w��rb�X��B��i.b�/��uH����	�O�V���f�<7�22]@-h|n��:�Ki.��)� 1�����c��ɣy������5��-�k�Ĕb�r�
��i����9��m��Ɋ��
�hz�����@F��l���a!][SX# b ��߳��ǐgy��xO��u1#����h�zc�3�,4�-^4�z�Gdڗ��mH�4s�s���\
h ��h��s��0��!����<�u���T����Q]��Rw����BLp�ͤI�Ӥ��z%�͹�=ar{fao����vd�c+zs.M~�fo�4�тF�C�9Z�d;��a	�^�F���'��1V[��!���8�&:ҫS_D�tߍ=� k1���R��W�8Α^w��|�	S �2ZЈv�TANt�)� 1�^��$71S��Rw����H�J�L�W&҄�p�a���gt�m�v�^�_�ܕ���'WA�>S �2ZЈv�TA�ݕɰF �@DB0�{u"��5�V��Zz7+�߻4Ζ^C�GW���]�i6������-��-�¾|�M[9i,�@ d����Z�q���H�x��$;�Gs��Z��������4n(�R5F��o���|��֑�_�0�:����D�l� '�b
�@F��j��" b "!�"�u�1Y��T]��F�	+�W���Gc����������՘�Pƹ�Y��/�Ձ4�:S �2ZЈv�T���a	�!��_���X<k��_k��E߷ihz����"��g���zV��Lטּ��c߅Fu�Q�iT;#�K��]0��!��шv���U��a	�!�����TSl4/=TG8�@�kLC�C����ƿ�+��@�Kv�h����|�ff�`��Zӈwh�5nZ	� �@ ʹ~Јv�HROe�3j� ��0��`����ե�f��+�juG�<Ҁ&�ox�i>�Ұ�4Ԇ�4�盻�|kN�i������>�}��Z�?�PkL� �i����� Y���]x[�1�	� �!BV���8��Y��RZ��o�@�}nFClhhKڂ��+�>��<n��]��2���z+׌��m��*�)@-hD;D*]f3�F��)�
l�0��!�E���)��ͻ���d}�Oc،�`]�"�6�k�x����e�zNg���������r~^�4�тF�C��;�i`3�A$C<��.��I��lў����E��b`31к�f���K-��7���lQw�����4��/!����4����l��J�)����xY]~���b���,s�o�n,X�Mhj5!�!MK[�Z\�0M�9������[	���d���Ϥ�ʒK�	�O�0��`�������,o��xwͲSo��6�7� #�q9(ؘU �MiFے�ҫ-h��4�q1 \m!�3�J���t��r��	M���a	�!_�~���vY���+x�7�5���H��D��b��� #��jHC��FbHC1T��Y�HFK�BP%q���h���o#�o#�ѝ��`����sc���p�Fw���QW�����~V4�����hp]1��RW��ZG�#��#��C_F��)�5�B'D��8�Gì��`��{K�c% ��"����B���'��=Z�(�ʖ����|kK�m��ؽ��2�k;��~�4ƒ^0�����"a!FZ�Q��@�������yKkI�,�xX�w1�X�-�i������?@j���*=�E0�C���ۚ=\ /pU����Xޖz_K�����3U�����o���b���R���l�/G#9��˜�+�7"Έ��#��0q���¸\O���m�z� �6��e�,e�y*��},�^�zw��C��Mj�C����Crf������ܵ��V���4Z�s�z`]��MeíHK�ݒ�o@ƶ"�����)�V�U^ޣ�yR��z�z�*�P�F�J�Ta�� �_՝3��#���J��}Ίն
�Nf��Hwҿ&S�L���2����psX�Z�K[vZ[|��wa!�+��I��,�eѯ��M#x��B O�y���эdΟ�X�0d��W�tk>�m�A��uȗ��%�R�t�Ez�E[�d�{��C2�2�2�}2�aC4&=둮5I����bIz[���2v�u����Ƀ�cjK��we'Y�	��\�2ם��c����$�����j�INסּ�!�����Q�ĩw+wO/� OO�3�nG�m޹~�ƥ�/s8wT��?w��jb�c>���ֶ�f�;Ԇ��|�Z�OjL��ةo��o�e�[�sw�,?~p��Ӟ^�^~A���k�M�(+ai0+�F�ѝ�
w���ak��X^�M�;��=��Cx�E�N_��i��uWPphHHhTTtܥ�	W���Sn������e�JMMIN�|-�BR�	�I���A�&_OLMKK��q#����ԫI���v�]����4�5�B0/�k��4�#\�Vu�ByD���TKڑ�YfO\�-�?+��a���v�,U{+2eLO///�^���JLLLNNNOO������~��ѓ'Eť�2� RS����?��y� ++���۩�iIIIW�\�t)�bܥ��GԩY�F$lCcYC�G���w���l`�^]Z%I�Z�,ڣ֝�_�΋xW�7α�[˻4'_}�h���}��EFF���e��ʾ�s�>�=��{��ɓ��"�Ng0����%%%��Orsssrr��ݿ�}����kI��~�.?=�o��-�5#N=X��a=�0Vr�.5"!�����TG������-��('xk����(�^��;�Ƶ���|ٜ|���y�I#{�]����c�#�rr�V�j
���ݻ)))��>�vm^2w��_ty����H���1�&?�AM�"<��x����(W��ɝ'G�שf$�A����x�Z�3j����M�fvR,�\�S��En��ۚtjN�7'��p}�7���i��-�=i��i�V��vѦ5��,��l���������^�Yuj�l���.ؖ�oO��X�S9��b�0e�U��g�H�&��271�W+	�^��̕�J����-��+��p4����.��6D�c��u�r� �~�ٽ�N]e:������>-I�����oKҫ%��5���ԑL�&��[���r�`�aʝ��\�E�����dɋ!�KSz�+�� ��׻���P����^��.(�zA������ɬ�8l�:9^ub�꨽��8�^;�����#�.��uÕ?S��\i�j\�0i��-#�;GK�C���%������T˺*����/�L���p�!@�?��V�-W "����1��^��^U|��{b+i��<���.?]��ȸP�Ĝq`<ϩ��T�#s֑qwP�vP�}�:5��H�?�:� �@�Z@���W��<�Jm���Db;�W|�E �@�7(��f���;����"x�:�ȹ�=J7�>C�a�����'�ә����U%T~�xΌ�4��T��x����'a�9�4[��Q�>��+m�r�x��Ɗ'�["/���N�z�Ëx����j��̮��?Auz�9�����*��K0����=�1�9����Z;Bt��K���tQx��+���.��V����)��Ɵ�e����.�h�x\O�y1O{�S���i��0V�t�s�=��~`�*����x�dܜ���T.#���Sc�)�_��y1
����$�;SX�������ա��`��]�΍�p�H�xQ#^�iO�����:1��T{&1ǾeN�`��b<g�=���,�m:sd*��^��N���=5��7M�pC�C�F���.�^����S
:�&��J�����P�B�<M�i�� �">���:n�t��I�{f�f�Df�f�xf�=�u
�g빍�����7�.?޸�c4B�o���Ҳ��I����jnA.��r�6����ܱ8l4��U�Y����9ͳ(ʶ�-I����4�:��|�S.h�ݰ�b�i�{~Mz����w
��̍-ޯ�8,.�����˦�:5�,{���ji;�S�yr�@N��U�5�EOohh��f��Z�Ȉ-�kNoiL�<�y^���ᶫ�d!qX�%�+��#rm����.ʢ}L�	���x�܊6]��5D���J��ei
�a�P�O����E{HA�����=}I��2���7(����KN�e�l�?�����	Ѽc"�AL�P���`�R�!�"�� d��j�!{��dGك�fy+��XE�����KN�������C�Sd>�4�т�dD �~��G��M���Az"�W)��D�WU�f#\U8� �@ d���W�_Tx�����݈����e�_�Re�J�N1�)@�{Wʿ�o������k
endstream
endobj
11 0 obj
<</Type /XObject
/Subtype /Image
/Width 64
/Height 64
/ColorSpace /DeviceGray
/BitsPerComponent 8
/Filter /FlateDecode
/Length 825>> stream
x����K*Qpό:�Lj��&�cA*���^�H�eA�]��hѮ�� "�E��jע�]��6eTX�����6u�8��|͜���?�9��y�d��+��
�\]����,&	����g��糅 VS��7���� %F˃��8�렼(���d���>�>���.����� ��s�r UQ1�h��,"�C)�. ����g�ω���( p�ȏ���Q ��Χ��`�Ii�I�����T/�5 '��r����S��T�� ��αދ孛�9�"�C�B�v��^��K�R� �j{A�/m*�8=��!���? W/��E�0 J�.���*��G�_����� Ue��*UIO�������=F�Q��߯Fm5)��9F��)�b����?����U��O�4��6+��[�O����B������ߴ������@�60�%��-���a�:+?6`�i	I�������<J�=����o�܀P��� T�zΥ���*��58&%͡ĤÐ~�Ϛ���m�w_<��6����&Ǩ�S�r�a�e�!���8~;�dH�ϨY���~��ͪ��L�������c�:]�_ ����E~cb}�w�.���~�O�H���.V��14�wd�!�~X�:,�7�s��7�{��ﱥ1���\�_�!��v�hf'���_�;3C~��VO�� �F���78<�Go��o������`��n3�"�qr���̹{}Ã����������5[���ϧT���6�r]N7g�����i�:��K&��ʲ��d(�������I�!	E�^����
endstream
endobj
12 0 obj
<</Filter /FlateDecode
/Length 5260>> stream
x��]َ�}���� �Eq	�f?;�@��8���R������P���ɵ_��H܊U�������S+�~�d��i�I)������O�����d}�N���o:�[~w�	�������i���?����ǯO��hO����{}�'c�n��/Ͽ�ß��C���ק�p�t���|�y��d�����Ξ����綵�/���z
����'�����������m����<�`/?��+��;����{���>��闃t�A�r��X�����/�D��NQ6x����ǩ������-���-����ڟ���?ɿ�?�0��N��M;��뼐i'��KWR��@6�@���^�ζ��?wq�h;!��m������ړiݴ0���8ק��+Q��h
�]�ˍl+�Yn���+��f�:?�M�|�͕�ݧ���~����q��a���{�?�7�r	S�^��(X�yGB�I����%!���/|_�ɦ>���'K�?徠����z?��ke�p%�IuNtQ��3k3]#T$��ލ�J}J��tNqJ��(�k��<����>%͆�_�V��[R���Fw�T�K�Zŵ���6F��sRH���77f��-4�5��R��rV���c�3U	F�2]g�6�6Ѻ��r?�b'�=�U�W����~��&i�6������ϻo�|&��q��)�~b���!����&����Aod������_���TL��l���\���4nS�ٷ���QD��Տ�lq�l�AH�E��ם'e��U9�vu�ֻ~�c���:�݇�C��CΏ.j�v��W�4�#��$�qbL
� 4)L��ɩ����r~6�l�m��݋M4e����4�v!c�A�i�n�=�A(������!e�����^o�AZ�BhRa���QA~ү.�!%�����E`�|�&�Q%Z�d���n��M8�'����ʅ+���x�"��x��0�V#M�P��X�P�=�i\��#M�A�F_x]�~��a�_JMdpf���Q�2z�녟E#_j50)g9��~Biζ<����ls�mv6,�^/c��v�~�vj�&��22��!��lsx��m��D�7�a�a���>��$-�@���A�uk�>B��P�u����tl��� ~�b��:f:?���9���B�4Do���L3`�3�� '�x����R�a��R�&��b���k��;z�u�+���.㕮�c?�K1�.V�5H���<d��o�)��ؼq�zTƓ܎�mY:��F��u@���hxj?-(�3+��.J�(0e�6�井EE� �Aq��QtP�R��
�&
O���0�o�*��
ӥ|��	)���|�b.I�PQ��ʄ���lwْ�f���\wQĆ�w�W�. ކ9��ֹ��d䆲Fsm �l$���˄'O�?E�d�8��c�/�\��&��?��s���[�w[��-C�����W���-�I0V���L��/����S�;�����C~��@��o���l;�*��c�b�iYŀ��$�!Z����$ذ���^��b�ѡ��B�C�hj:�X����z>�L��G>aץ��:�AOWM��Zcr��N]����d�#B�{~�>wC���B��?����J��pu!�OEg%�B�c�z"s���l�o7�i�9��������ITO��C=�<��M(.Zw�;���-u�-Hه���8G�� ��!>�2 �(5�w@!��� ��������X� 4�	0Ù�Rq�P+PHx��
zت�����aF�*p�#oxє�gyh�����2\�m�P."~�@w���}mM7��1":5):�y�P�<�|�4�V�9�4�q{q�F���5P��^��#` K-�������}4L��׌�Qf�4�ǜ�mU�l΃��ê-4��pC.�P�<8DN��ή�����	� �U�ʁ�4}��VH���qhПrZp��]��T5oo!1���x i���6/���Hυ/�Z���;�~�W�?�sb-��;�[�6�T��}a��׼Ih��o#_��Q��a"�zyR�A��������@$;�Pϑb����B����CѮ2�N��G�h@_ ޡV�f(M5y��5H:���9��S�ӡ� ��
J�y�VQ��»@��.����b�E�쾀��>;'z�����t�f�1)��
I�W���Uyy�}&��V1+��Ży�T����Ln�G*DA(}���ve���e�s��9S�I�>:�O��d�z��w��x.��Ft�2~�<�4��6��UF������(0�\��1�֕�/�>F���nWho�5kzY�PY%��:����{*8�rtW$��4���!��]y�����r���@��/��aSإ鯻�I���k�Qv�B��D��B;�to�PE�|Z���F�H�o��:/��n�����7�֧3�����3�7z��m��`���A?q:3��tq������=�S��T}��d�nC��Y7���&���+���N�#(T��i�:jA$*�T�gy1�}V�(4�:����!��5��Tf�;X�� �}�ZM\�[P��{w���gA(L)�aSc�Yۘ�9�7P�
� "�圹v�0͚v�£�Tu:��b�@Ax��)�b����{����g��j���G`8��-����G�����hܡJdn�����zC�tf�+|�MA:?m0���0 o�,Ǡ����BT�,A�<���V��٦ �S��
CC(PPUؤ�G��!>�������� ���A�[�H������7hXA3,�PVT�tת����rcx1꙰hw^EG�t��7@w<%��B��
&u6d�`
G�t�W�g��u���9��>]��),?�k���Q
�t��1:	��D�CS���	��Y/S�;�Ś�����j0�D�Y�A����#XP�r
��i�!���� �n���U��@��8����W�m�(��G	�* \{�F?'XM���bb�͊7o���1:�ix���n0��-����ِ��RiIfO���&�Bs�`N|�od��(�6k���3�:o��h��lYE��6Ys���J�P��C��3 z���5�K'��4�Ȇ�����������?�/�{	��nc���[�9��
�J9<Sۛ�	|ioMv�wS�h.�;�`{��L���������� ��*V�A�κ!�Ƚl���f�SP�,�Fy����ƓJ)��7���F5+;P�^�
�!�f��UD��x���Q���k{��C����``IW��X/�*t=]��5��HֽJ�J��^Š���h���ꇼ��hk��0u��W��b�L��xH�P����t�#_ϽbE�;l�wRl�էC¼>�VEU�"�?V9K+�r/�����h��%�������QV�&t3����z��논���EpK�{yu,���zw]����Ղ�KT�{,:`^��iAN�HὈ�)8�=/�`�זɍ�p?�A�&W`��k#Hc;|<���h���_�q	JCS�uMɛzCpa��̛���c������m0��4�L��֊�<����;��/_/�>�n� �e�Y�����?���P7���槔�E%��+#*��x'T�dz<+h����oPU-� �������J[��O�m�|��3i+װ�"�����]R���A�ұ5��j�V���s8z���zH~�1�ʳ��9 {Џ�t�j��;*4򣚅�*N�vڤ�ch������Zz�m��7�Œ|�	��6CwH�}Ky��'mC���k�M���v��<�@�|���;�}�m�s��?ٙ=HY���c���|���;�u�������Lҗ���_>| t�)H���(�fK�;�yD��j��BU�́��í�2���3�h��9��k�J�軕��Ծw� ���Z��� ^�5j�j1[��ϥ�g�Z)�-��O��@tЄ�W�����{��2��Xq�,�o�b)�jm�ӇUP�-_~���u
\&�Nx�M��z�>��
r�f�QC�q��9��ҽ�;�ʛV��%�p��hҗWk�gM%�e��Q���&J�)�U��p�0a�o�V`���,�~W�>�KT�]E���@��'oK�x4����v�m�L:m��M����G�^���H�^�خ	�~�9vy�>d�����Rő���� �I�F-l�T���P���H�瓚�F?����q���S*s,�L%\�{X/_D�"t�1)��}O0��r�v�ܝ�(0�7�5S�*1ˀНGy�6 w/��ڸ8=�Gt2�S���k7�el/ͤi�@��i{�l%o�7��'?L�6���gEW!�n����u*��d��Z�2�rT��E���{��5S���7�Jad�ƴ]��fp4�=�	T�J]B��S}<��Z��j%M��L�G4t<��(��1xB���TK���,�/\m*S��s�/\Uj�d�J��������y�o�SN���bB3v� s%4|�swi�T���z)�n+hpȻ���E¿��{x	v<ܷQip{�)^QZWC�t^D�H�G�=������ԋ��A7�cN�xqh�(L>��m�+�l��"]�q�F�VZ����L�z�PJ�B�@�AWvB��_yA�y=�`=;]K��hLuȔ�6ۮ:W`��
lCi~vM &V���=��WH�	��@���w)��
 �7��Pt�R3k��d���}2K��&B@%2�}_A�1���a�G��f�U6���<��/W�!sA���rŕ�\��"Ya��\�-p��~���|�VA�_>��6���33T�I_(^��ۣf��;I��٣�1�nJV�;_ՁD��U DQ+��$7y8*f��-|`3X��
L�����C[��ټwX�qr�	��N7�cZyW	�|�����{	�����y�\���)(����pl��sI�!Q��
^9]��Ϯ�;��ٱ�����f��ճ�j�ӭ�Y��
�C�+zVY3Û�������h�/ ���j�����$�����p��Ĥ�v�/�����^�D�6}�+�|�Sg����������}r�.���0W��|cM����[>eCL��|�c��
���j�e}���mR�����(�"v���~k$����3�S�yQ��3�Ru+ޘ3��4i�ΑV��|�f�q�o2���Y�0�]M��]O
endstream
endobj
14 0 obj
<</CA 1
/ca 1
/LC 0
/LJ 0
/LW 1
/ML 4
/SA true
/BM /Normal>>
endobj
17 0 obj
<</Filter /FlateDecode
/Length 7219>> stream
x��=ێ%�m������u� A ���X����?RWJ*�)u��5fחӬ*�")�DI��1�s��O�3yDc�����'|�L7mE������ ����>�0�������������o��Ԟ��&�R���D�����?~4�x��7h(a(o�>HeoJ�>}y�7!���ۧ�}r���_o Pa���7�	�6�L � 6��F�t����P2x���s'j�DΘ�ọ�z0op��`n\pt/�yY��]q�o�=��B��������$�;�cn���7�1U@n-uQ��v����7ݡL���V���(���CS��m(q �}p�/�7<���ι� xϝ6Zf�6� �E��{��ۯ�q�^�Ԛ>�v_��H�������.0��c�O�
�q�����aA:�'v�B�0b�X!Z֗7]�o�ƇCI/�~}r��?>���Ҵ7�Б4��h��C�.�C9�i("�j��a�y���DIC��0T 4D��EJl�"\I0��!�CXao�����};8����V����=�����g�H��U��ø?]�Z�P�͍@вH0�!��1����Q"8��+]~��Q_�T��ֻ�BY%�[�Ce���L�B:e*�������r�����>�}��	������NZ�j�&��	~h�}M��x��(UՀ"2��5�PQՀ�Y5 I8�լ4��-�!F��h��S�!l��uC�%ݐݐ�tC�k�A%�n(�oC!s���L�F�>���,�uCc��}E ���x�0��tC�ͺ�n�	6�Zt@��8Q	MB�$���%�!��nH�P~S��_����F;�2��l��G�e���M�F�>e:����Ӱs�O���>�7�����*��
��U�_NR_�H9{��^�x�c�D�|M��)7b#�$��s����*ӓ)&���^�V�VA��?(����p�LYp�}���L(-Ic�sK�l���QH�$8�ڵ�)�7 krN��� Z�F*����rށu�*:����w�8�jT9�MY7�I��p8,{@|e�%��� ��D�Q+Ŭ��?�^z��_��v�l��mC�hD�ڨ �LKP�y�ՅaTъZHi�}t_"h	�ax#�H=Λ(\TD�cy�A?/`�̑�ζ�Ky �4�	�f���a��9.s�����gIU�T'���(G^��󇛬��.�<g�̴*�F��},~.sW����;o��`�l�}��*,�Z�]Y|U3�w͙�,��>�D�,�����Js��%�9��kO�"�l���{��wE;y���Ib�G*��33����JO�ř|NLxz�c|<�Vc->�F�,��/���@��sU���#bR����):-gz���ы����
x@�Y�ڂ�[3��'6ęN�:7ĬVgG��"\r��t�W�)���H�}{�"M�д����OA�"��A8a����՚C�c�s3���(7b(.�yE'�4���^� �q$��T>X|�����/�Zmdr
�a�<'`@?�~(�ZԝJ���l@��Es�}���)_��ӣO�^-����}�V)0�z�H�		w��vaCs������	��*$�2�f�>:VrX�6�4f���oVjG��� ���"	�_��LB��NAQ���������<'�tx�"�#;��zF�Dq�	�ǈ5�~8i�Ck���.	Y�nq�X�f}�yAx�n�em�ZFc��ҙ%c����qp�b�b�b��YF�8$��#���t_�!�=�S��<��v��+C���i��6Ϳ\�W��8qE{[C9{a���P�/W�X����=�1'�����Q���q|𦸮��1cvY{�\�w]�03�]��}[Y)g��ŰJ�]�U<V���~ �b�CL|�$߃�y�D�/��3����I{�����N�u�U��)�S�V�����dY�}>��{�m���9n7����L���@�D���3��� F0;˛�!��F��b�\���l�ƩR�:s�%ۋfv��;�I�m+X��z��x\Կ�L����!���pv��?T�gAS�4*瘘�K�����>3��s�w��Kb5D�>�>V|<tIzN#���&K��؟W%|t���Ql亭��Ri�jY}Yw6w�L�%�4d0��8=P<�����a���ف��^���4��K��$���~�AҀSv�X�J�&n�x��CnT�hԕ���!�L"���ז�C���׳��(X:�.�l�|ۙ�kI�K������/��9+�b�m�5��!�Xi��7:xC��<�;��lS��c��*�+x�������k�$2w2������q����X^��,o)9��
���N����=UV�/E��Ӵ��p�f)��d�L��xӶ�g� �Ŧ�8QN�Z�R_���*��QH%Nj�0��F���-)��ڞo�N�A;}y2!eN�K�C9x�0Uy�
!�xԲ	�A�o���8�BA�$��`�(�44J����[x�p� B����B�~J0�+WՃ��+� �� P��V1C�N3)W�D���Mj
k�i4}�L�;ڈCY�t�Н=b �DR��S7����v�=�RVR�X����F:{H���#�-LS�אּ�S���"�8Hw�8H5�/p�&����G�pk��c1��w����cI�Oo6ZZ7U&mڂA�@@��(��-��?1�17=��o�I!��j��kh)%$��HA����ΏN\:�*�|�슕����<�p�`B�=�w���kY/6�bZ�����#]QΛ��,A�]Q���5K�Rl;e9�	�h�"��j�o�n���P�v�,����Uf�%��j�2�, ���a�K�F�j���C�l���8��6a��C`aF����%X�q�*Ԫ=�Ӧd{#]����u���-j��(ݶT�uDIܭUg����+gdf�ߥa��wb�L㴷�4N5�͞X9��Va��C�!+�@@8�>��@;Z���H@���J�J�]�\G�ʩ=�r�T�+��q'V���ιʮX�������ck/��K�.���%�6�6n�Dx3K�'�.U�de+�XCM+�	��0Yu�8n�6V��
e���0��V`I[�<1q5^y
�im�ߐ'�΀��C�R�yȚÚMj?d�B�%��.ʠbGBQZ
��BQk�v)�*�J/dm�#}���U���]�{˪)�V�ז�O4;h��S�[!;ղM�~�n�>������fn���ʮ�Њ�!�П�jv�K�c�_��d��*~��L_�����HeY������6Y�)� tn�"�["8�*a*��.�}xD�+��Wz�y�)KgT�A8�U������V�юI����}"/X��t�+�}��o�g|;�[��/���Nn)J�(��JQi%Lو$�u7fX��;o��y��a,�9k����<�p�vn�d��8Ӫ	G��K�Esk�<V\M����$v�e�b�~���-� �U�v.e�gե�^ɰ-ۋn�C�1EFmL���, l\@�Ƿ�Is� K�`'	�.	�-	��$H �N"���#QN������Ɠ�H���"���>q��@I����$%
�H���9
#,�S��&G�홖 6/ �$9����y	 a'��&��
�A��(U�?I� pI���W��19�Sa���["'�"Q"ym"�d�D�)��7���Β#�t�����x'9�cS���tz�]��Za��r=*M]Ϊ>�~�=6s�m��辺��=H�%���`����]��=����q�����k˛����옚���A؜�A��XvH�X�z"��v�.B��B�G�3��%���&g:%g�&g��cr�?�ـ�HO��z�����nY�@{r��'A:�z��R�'V:/�	�l�萞��,�����������A؜�A��N�s��t��t�'�������1=���sz�vBe��Ce���e����^�3�^t����L�A8�U������"�bJ�=��ow����|EQ"��^q������@� U��% ,��,���ak�b]"�Y�=��xK�"�H���s���9xA�Z���)xI���C(�_ܟ6�����l�Yw�;Z�q���Dڃ�N�4t�����"���+�Q��&���� �ڸ��"l^�E�� t^�Eؼ�����	�s�2�TÔt	�k�H�]k�:�DN�YS'��F2:G�j�:�#5L��/0��9��|���f��;�^<���+��{��m��l�yߦ��vVHްi�ũ`����}/;���jq)E?EJѯ�R�k���"6�Ҹ���q!'qRk��'Ō�'Ű�I1�8)FN������⿓ވ���"AC�02Pe4��h�P�D-��$�i|0'����c��%�4h;��΢�h�()�5J��,J����QR�k��Y��%!���)JJ�<�%J"�P	�k����kO��F*�v��e錪<'����ע$t����]���:Ƕ�|�Q�'н�Hl;���^q0�F�Y�Ś �!�Gv� llJ�Us�~!�~��+6)n���փ�Q��H���vC�]���߸"{�X����mo���(2��ը�d�0 �ț��YEmBV�)1�`H�f�R2��!t.$D�TH���� 6���@�s��Wcޟv��������ot��gB�}�N���T�u��R�{O��W6sr������9O���s��ȟb�e��!������s�a����Ǡ̐>g<(�`������]ڷ]lH'D�:D�M^��X7:�o���$�x`��W�r��oD���vpQ�T?	��&��V4su��k^�U3U;XN��k6Lm/E��a�e;�sn<��.{�^�����	�z�zB]�| Q�8`ߒ;�'
��T�b7!F��1G O!�����Yz�u���A7�����ͤ�xf���/���)B�-��x�o�px�a�&��m�����0��
�>��Ʌ�G�1!��'�p���'0����%���m!�1����Y��ƶ�p�����H����+�o�x���9�T�c�����0_�s�s��z�Y�ǽ�B�s�~��H�?3x/ZN��ˠ�(��
:I�A	���
��xI�)}^\���?�P��"e� �]�����0��R�#�����0y��)c`���
m��<BATUn���@�X�Q��P��k��w�	ĭ�����6��Q���r�\k4nP������N䠍�L��f��)-�4�v1[e�@t]dl�B�{�Q��	���=�-(��QƼ�Y8�� t��}��4��EP�:WR7�0$��U�*Ẹ"L�h�+o��C?ʃÔ֋(Bʣ������d�����<!F��B�>?��Bo(&<j?F�(�&}����n4޸|##4:���6ZX§ӭA�N��}cD��"�9�Ѧ�R�w"AU�~{J?)���h���le0M����s���ୁhF�t�\�96x;�m����Y��Z.5Shs ��	�E�n�f�"�uP�z��8�����-�!~ߐ�@1N@c?b6޷s��""�fG�ү�W�c���:t����ꓝ|�p�@��<l�p{��'�}��w��������������a�7p�rI�K���S;שׂ��o;�C8�ۇj>���K�P��	���>��~c�:�ެ�Õx���9�����"���������}A7%ة�1ص�a�,����������e!lݗ�й�asi#��}Y�J��6;�6��������hg�T���K�:�=�M��;Iz9a']/<�D�%����*�Q
�]66"�)���`���6��B�Z؈�yg��Y[vf!pޙL.lf*l�:�۷DRH'D�:D��DJ�Yac'�{��F�Kg�Z���+_.l�6�W��֜�����_Ű_��8��K�?p�:���Nm��S�#����҃�����xz����w��=cC�-��K~�;�Q�F�k~9wb��6�S����~I{�߾���|p�<����� #��q܃�� �ޞ��1���)D�zLa�fڅ���������&��R��M�=S�M-^��ޛ���x{�N�^{ڽ���JHg�ih?��O<"2P�;5����b���kk���W����y�z{^�ޞo������r���<���\�� l�Ƃ�e�m,x�{������_.�Xh'T�*:T�䲍��ʳ\��F2:?:q�LR����+�x{��� ��`���˛��AB�aº��6�� m���A����.����^q��W9Cm�a��ڿ��u��]y�
��U0���������,Gw�xyS�z>x�J�� ��}��6�.=R�˜�?[��^Qn�=�����w����F�v{�Ɋ�l2����u��\�mk1�K����o��^Bcir����>Y�W��x�,C/׭���X����ȼk��5�/���Z�]�x������{��{EV�ݻ����]��{]%���:��p������?L�5���p�e�d�a͛¿z
�G6-��SzYn���m�b�}���޹Νл-������t �����;�+m`u�)m��մ���
׏�l�{�N�j�2�頡�Zb�+ܵ�S��; 掀u
�f`��a�� P��	��`��
���w��Сt�C��������b�w t��N�>FkԠ;:�>�P��ҝ �����c�t��?�t���~K̚�1"����F�w:t(��п'�h����D���h�� ̈U�T�2~
�Iw: LJH��AK�M9�t�8�t��l&J���0�ӡC�N�}�-@�i�
���z۩@���4tbН�pt��vR�k�� 0��7�b� K�2�N��A�ΛE���<�5��u�P�ׁ|�Xѻ�<�u�vԉĴ!�Hѷ�� /�w��@:����A���i�����mA«�}}��D*�߉T��F���+����N�u\кD����k��u4��a$�=�%�A��?6��?2���
endstream
endobj
19 0 obj
<</Filter /FlateDecode
/Length 5976>> stream
x��][���~?���pE��X 3����� �X�	����ԅ�T-wU����۞�L��%�7QK�ތ���E�?6�19�e�s�|���/��qI]�W�򯿾��]���t�[c�a�����.��_������S���^�6��[A�Z/��_����˗�AG�B}�q�I1��巗W����|�� ��� �f��@,@$���uZ��k�L���~�r�p��ft��r�A�4��)��1s��,�Xj��$�@����������c�������[�����a��]4
�x0P�����`p�z%�}�.��r�Z�wʺ��#�$��� �a��/V��^����'[B�A�\��`����,de�}�Ys������+�f�6�3g�r!���Im�m\dl����Vc�7FA?K:D�g-劅�Kc�t���z�	����6ޮ�����W��Y�݉@��f�bه��CN�	EB$"�-�� C�a�9����NH1�L2DȪ2I��u6x#�R��+5M}�5��FM�/|7({�^�{1|�@}�B'�e�/�N�@���ehR�4n8�.,ɂA�Nȼ`@D�k��@�5X!�`Tq���6�_���a��l@�'[��m��$�en��%�4H><eX�<���y�fx��yj}�/t
�R�E_Я�=�y���+x������'�c��N�7XgF� ��7D�%��)g�� �}C�@�V���7 X&T��`0��b;�P��7T}C����}���A���;a�b`a�D��|bE����L$�s$C19���4&���N�k� L�5?8 v���9 �sAgB����9 �w,dv�����s@ȵ�;�j��;�b��;���;���Salbxa�D([/�#�\p��KH���_B�b&�nČ%��>)<���<�����bd����=Ē��b�F�`5�|F�g�д�(��;D��}D��}D�����;�x�zռC�0x�
	�k�yi�e`�~����;+b���l"��k2�rvVa�ޡ�e����P��P�w  E��w@,0��b�z�1��F1oM8�e���=�T����1�[ROe~��= :����{�O�=���=��҆��=��'�@�
���H;g�ń�"��RN0����];r�v-��>-<���<��O��2�A��N��d��	���b��D��7�!|��C.�� ���6;����A�8�z�D�08�
	����Q����1M�bB�txޑ��S��"�<��T09���  ��&)h9>b ?8���n7�ش�@h�����v�ͻ	���	D��c��=������faA�Oajbpa�D&�.q#�\�ͳ��G���]B�b�f�|%��>+<}��<}������h��)�� @��C�&�P��s 4L;�Miǂ�t �9�X�)�X�гjZB6���shW�9��94����c;��E3�l��
��3O&��9�!ON)m�Ƭ�����s(����y'Q�)�X�y'`y�f�s(ش�(��; �D���D�v;���ޡB9��O�;�k��faB�Oakbpa�D&/q#�\��Ӂ$f	R�/!q1I7bƒyv���������>z���`f3YT��Ct���@� Hƫ��Ѭt*h� ��97m���|�9����Zg�1�AV�%�}t
 #4E`� kq��u���b���@�l������e凱 ͛�*O��0��6 �pK�9�*�Ҿ�M��B�E��)�*]H�g��L\e�Q�D�)G�1u>C(X�+t��\SZ�-�a-p߬1A떩e+`�v�&��e�!�?�ڭ�<��U�,�A�m2h�~SIg<��7��[��=fm�S} ����Qq�|@_su�a�y�L�9x-ٔRE�!w{ m)�OH��L��r/00qAy$�Dph^��j32��I�uÚ�^_���[�@<�E�꒗���l̝�F9��f��7b�)<A]�$��bHXjH��m����4Cd!�f���t��7�ms��A��ш�&��\�`�n8����D=��a�z�������@����!��Q�5��^��f�S�x1��A��鯧���L;|2��p|�J#��*;7�7�����dG]����'E�Cޔ`�0�l[ 8�#@h)��	�T{S�Q���Z7����#��~{q�.� Ix�P��д�6o04�����}�"��[G �C`i��"���isVY]1�ܖ��m(j�Ve��M�b�y#�f}�P��7�H���� ��2Q�D��0Ru�����oaY�9�	nf\�z�Mh���������\%�Y��$'XԤP���F��T*��7��.d�kk0�X9Au�}R[�C��,�.C+�l���|��?Sb���Sl�O���)׵5K��˝,-���Q���U)� ����LS��*g���z[i+<���N���N��SfPZt���.29CX�r.u5�9�Օ�1�Q|��]E@O��sֺ?����\��؜-�Mo,�ĵj>��-�)^i`<��zB�B��@;�!�Q�^t�[�u��=��s�#� �a���w�`P�{r��A�kn�f���������F���_Բ@�������Q�X�\�$���`���g<�A_�F���1�[���bM��7����O��r�3i� ����NL���F��{��o�����ȥ7���n+��A��c���f�S��J�d]�;�����pC� f`����F�	��&��5!+���bp�Ǩ	�9jBl��*�5!:GM�Q�)g~�j��Ң͝��.��8�	�x���B��1�c�.:�i��9���RS�C��L9�6�L��1�)����Q�)fBl���k7�L��1bs̄�����C��eВk�sc�T���m��� Ҧ�.fb���2�Ҟ�.fb�����L�9�<�LU�ߎ���T�*Y/ԫ��P���zz�^~ȳbj���^���p����KlL�vW�P�|p�6���˚����:l��E@����ʠ�br��Xh�b$-㔥�R��3�c�)�Mʼ�ܖ�3�������t鰌T�n>u[�f~�ٚ��_�ag�0vRy�W5>Mٛ03~ͤ�0����S� ��f�M�k���R�@B�,��տ������K��Fv���o���5!�O}x�M���+�o��߄��d�Mz�����G���k�����'����ha�
EA�A�ܿ!�%�˱���|��������|�����"�������]c�Ւ}���"bNr�=&*��_/��uv5�`��Z~>^8�������b�T9���<�#\
q�����*`X�n�dp�-sY��3ݘ�����q��p(�;M��u3�R��1g2̃�M����o�Cc��X�ί�j���}��q�Wa�2����g��S[O���쑵㭉��-<n�Gf�V&}Z�k�,]��$�M�w�?�yʙun,���������t�/��Gu���yrWa��gh�5���u��r�=�+�½u�~^V���uW��c�G����o<����j�\�8�:����Kg�\��ެ�/o�3����fu��|H��j-�<�_;��gp:ܚg9����BZ�۲����hXsҁ��ϒ}` ��'�N?�uy%��W��գӮ$�R�¦�jƮ��y�ێ��&�Ң�*{-س���=��1�)���jH��-㫤�` �-Lpx�x:-���r}��ɶ`w��d5�MG�n? p[)�E��������r>���?W���D�0����R�H4y�_�vl���>K�)�b�{��ȡ���Z.4��Ŕ�e�����T�v �]ՁS=l���#�ͨVU꫰�
k���-^�]">^���}�熹�JU�봂*�Z�vˡ׭����3����v�}����{;��%K>^�4wk�x��ʻ�1��vra/�a����+�t[��Ra���"���n�r��N+J��V\�L���&P�u�e�b.��Zk��k���z�+�]p�#6��W�$7�$(�|���$�6U~*�YD��\�E�!Y�M���&P(�����v��wW�g_ܭ��ʹh<UKP��1���j`m\ڬ	Έ�a ���g{Y������T�`)�����ojIe�r ��i��kI7UiK���d!K�Ij��['�7��(����$%|�(�Cy
^�:/��C��k#X����%zqK�ےx֕$���dK!���sG������%�xܾ� ~��k�����GJz]��W�r]
p�@��>+*��KD���~I��T�����I�1�s8+!l浗U�^V��h}�F<y���e*���RBo���R�͏�8灐ks+jj*�T�T�Y��=B��1�jo����C���}� &L�a!=3���h(kʘ6�\�T�55�EA�]����m;V�K-n��cE1��uQ�n}y)��Y��><�ޏ�Եj��6��A�r���瑱D}8ݻ8��<A�r/yKY�F����8%�:	����Q�8ޒ�X��һ��㄄����0	u�A��a�E{�q����0|���y,{�/���Ε�X�f~~`�XV����7���#��4˼��d��8}�}�\=-�;��?�H��nN�9Z��骾G�-���q��7~�T�ء�e��ݬߙ�&��/�{:������f����^�<
l�ai��i/|�ۦ��BC��퓜�i��x5H��#�sK�
NB1���b���H�W2] �2]�aʨd)�[�KfHua��PA��
LMu!�+�.e��[��(BI��N�\���]$�}�İ�vz�Db�o(/��I��=ʐ�'� �����, *����1`�ud��$S]�\7�t��K1��dS�J�G9�.��"y�<��5�E���0
�[RKn|�!�u�PQ� K5�Gb��,W�d��Z��{V�$���$� ��6�^�2�~x�Ď���l�I��d��}76���x<̏yI�:�N�S����[����{yF����ثck>�r������8�r���%K��|رR���Q��	ҳ5Q���JS�O9�x��*-"#�/�wi�=��0�{X�2�����+|s�b��%,�<ϯ�x��;�9p절/i�
jD�Jt�ؖ�0���"{����!2NIo֌�q�y7G�)�Ɍ�qJu��qŦȸ�CdL��h�-A��+Q.�O^��+�qj�9����B�z����|C��!4�)0�-��
Ch썇��{3���L!�7S8\pD�}r�)�(���h�����B���s���u�{�(Ƀ���/`��������Nc,� �B�
�p��@�5#As׬I�ɕ����[�{��)�'����Ϳ�b���^��S�������޷��ϷȀl{�ƽ"&����ޏc� 戂Nc�ϔ�go����۸Q�P~���~�ބ{y�M�{���{�UW�����K�������~��X?�ʭ���cC 5��S��rZʽ`	�d�{@#ߔ{��tD� �7 P�����X\R�Q;���=�7`�Ua�Os �[o}�QsNr_ X�\}q���'��� 0�徠b㶠crW�m��i�'A��(�-4O�M6s�g<X�����FJ����� `v+���0��0�݀U�B-w���DhG䞠cr[@-)��S$>�?��$��0k��>�vPDI?��=�_?�]`��4�+8��4�
 M��+ �? x~|������EJ�I�<kHúd��et�Fky�����~ǿM{+Ф�mCG��^h����c��cke6\ �W�dwGFOj]�|���3��K��/�J�
endstream
endobj
21 0 obj
<</Filter /FlateDecode
/Length 7085>> stream
x��][��6r~�_q�X���c{�� ?��n����RE�d�T��nu�=����9��H֕E�Tڔ���C��m�k0r�2����ק<�ue�xh+���������;�f�~�s�7�Q>����#��ߞ��g������|�)������?��?|~������
�ʇ��RهҏϿ>��������>9���� �0f||�H@�ې2�6�+`r�?}>��vS2x2r��N�ЉG>�b�^�`~�T���}���GA~,�8�q��o�=��ğ������IJ�9�c���}Uʂ�*`�������;ʟ���I���~��
�<D�k�=4E��AhC��>�6�������?��������N-3�M���(T��0�?~����ҥ���s���H2d��%����;���f�W��q�C�=�)cA��޴
1c8
�YḬ�	��K��a�P��O�<��˗/�e�Z��K�:����9�u�bؔSѐ!"f5�!� 杇O�f#艒�p1T <DH��b�mD�vV�$�g����o�%���5X���[E̡��.Ƚ�<P�2!w�Ӄ��0PB9b���|�y$=���Ax��-)��Q䮫|��>�cY��W�|��DT����Pi���hefS�J�rBw3�� b5��ľǉ%V���2l������_��?t�s�$ )p%���|x�?�7��B��G��tqZ�Aˤ^���F��0��Z&��; 4z��C켃��w@l���c��Cwȟvt�!CD�jsDOI�D����WR����5U�4��y��uff+�{�*b�U|�C@�V� �w@l��M�A1y�F���t�xuAӮc:`8��9 �å���5��5�ϝk�U��U��1U�2D��;!T���
k��R�j��&X�BM�H���J���>����f���Ã�+~��*t~�[��n!m���Gl�TB��"�tcB�_@l��D�GR����Cl���~!a�/�O�_�_:��!�x�9���c��u�D�+)�:�Ď*w��U�$�&\�B,��o�(��P�[  9`�[@lt�Mn!�0�ĬV��|��[�*Nk�Ƶb���a퐠�v�o�3�ϝg�?&T�$�F:'JY��t�RC���ݬ�2�Me$1/�qb�U6�^��m�����|��o��4P�F�����		 ���!a�s pZ@$lX@$lr	�C��9쟲sؿP�CM�ZsMOi�M����7R��P��55�T�k<l�I��̸I��{�^�I��9$�S���~H��6: ��6�69@��	��J�sĴ��!��o�P�������7�*mM#����l�[�!*N�n�P�CL�����7��*b�U�ͲO��	><�7�	�������tSQ:����-��W�~']� �~�8&M8�)e�.�B����\:f�
� ��S(#��+��I�E28���6�oAm�>����h6��0�9��J�h �NEaig �MI��)-�àW�b����4wh�Pjc�?�P��M&^��44`a����@��!���AT��/wj��w�4�]��P�daxC�dZ?M�tDM�m�M7�Gڅz���&�9��Mռ�~'�o�Gq#6|08W�8��(1�]y�ТP�ʢ�~����j�Q����U�9ҏ�'�`�J�zEQ�Xt��||�Kߊ�f���]�ʃ�WI���)>�J��|D�mO����M��oL�����X�L2�қ�p�:0mp�����N���M�r�<��ۤ|�3C�Y��PO�9���tS�H�SE��M4��w�]E���`P���1�ꑶ�J)m0=�AӤ6���*�9L�����?wrssR�͉�͞ܖF��Z#0'�G�rj�mo��Gy�������pd���)��hI��9�0KfrA�[4�x�[���)�@%�y�?��8A�5er�$FЖU�)Y:VGk�y[��qsKbS<����.&��:�O;ao�~�12z·[Qn4�|�FsH"x���k�{��Q�{V��=Ɣ���"z�s������+��B;aRyP�N�a�7����v3G{���t�	b��8Q���c��`�9�h�k;*<��^h�sa��_aAe�y�%%�s#��va~�/��l�`a���f�)f4�� ϥď�e!ׇ)�O`�'��e�Z�KI C�Ǌ���i'��j�!�t4ѝ�U�u=`��%�la��8�(�k��]%Ç�{����3���9�rm��Ņ;:ʻ��@Lʜ��ÅM��`G�����x;#�����7�>��>L����Y
\S���c	�:G�1�w��Q�/����(i`�5���+K_y�	���u�c������\7EL������D�Η�/�wB4�+�ҩJ;qa�?%���З��^�n�V������Cփ ��`�Hu^vk��ᣄ�t��'��f$���7�*� �q� �p�(j�X�Y�0�Go&nM�-~��8��1Y�q;u��W�ݨм�(��`�����n^O��=��S �}$��<�W���5����+���Wˮ�F����'΍����]�9��+����Lr���m���ə-�Y��^L{I1�Ux��ōKv]�I|4KU��W��+k���D��A�Fh,�܊�� �vv�{6�;���	JeS�@
��_���	����O�ÃU����wK�pa��{�M�7���R ��@Y�B���Yp�)��ݸI�����<�����v�;g�!,���hpS�E���d��a6�"�AhP4�v,���p�Ԋ �椔�dV ���RF�*J�*�Z?-u���%9���d�F#�
7h2E�ܗ����ڏ8LoB$CP_��]:�
h�GڅL �!dT$���}F�iJi���t֤��	��4�Q{�QsZ�gն��d��TA�N���r�`5d��� >(�-���A)�RzЪ�g�;o) ���i����@���
݀jJzM} $�$���:�GS'`���N@��9�A #���nۥNĀ�Z�z�:C�[�ԉ�������"�M�N�,6іJށ}��	$�-�C1rۓ~B/�Aa��[��S*0ۢ�U��0��^�N$; �J�WG}�S��{@�E�ī� �$#� �~�-� Q�U��t��������;�#�	�G�{鱸��BCNY��r1�}��/��V�I^H�{�[̸\f��<�(����C�u_��=z^_��[�%{�����n_����0� �p�=Ģ,����ݾ`ݙ����v/&�$@�,����a��A��*����0�lS�8�����)����N��8���tF/�������IP���r��sv���:�P������č��kNR�7YMDz�p������ƞ�%s�u��r�hh�򂝖���4�pΐd������;�@�Ҿ�QN���<���G�� ��.9�%�퍛8
 ���m��uڋ�+{�8ɺ0%����2���Z>�<]+0Ǎ׳�IW����#/I�Y_�,��~#�	��v�[uUMA.�"���х���PqWV�w�������M���|�2�.?���e<�X��|^��?��-(!"�L0iAY��Y�ض��_2��מ�X�w�t�ۖ['���!k,���α�l�,����R�������'v.+捡��iwS�_ �-J�"��Qa��8�,�c���P�� !꧹R�u�
�F*�_vL���|���K+�.&>~(��c��>8������|಺�~ѧ��l|�=�Ig�����.���DW���$��I)��'�:�y���O��4��	E�|t�b�tP#1І4�{f]�w8<�?8�2��!L��b3Q�Q#�&�	�M����B�y�4����+��ºD�]�~����
�}DM�.@�R�৹�<a	�s�rD�D3�Y� !m���}�6㜈��9`C�m�Є�b*N��xs�w�����9<޷���1����o���-�Yo����9�}Կ�)n鱜j��P��9��j�b���c��Bה��c7>�;���ɶ������|r��Wv=�{��]��� �����k�ˏ�iR?��pܰ[�%�^�aY��Τ.����JP�re��Xv_�^N�Ӵ�Xio���;����)B-��
�1����;I��p�������sc���c�e�~6�t���dYo�`5sV����eC��b�����֯�ڼV��|�|�a��^��/-I;ʗ���rGwT{:7��BY/�t-#���a��<X+X/�t�绯�益��]9�u��Z.�³�=�X-o�U�:o,��8G7�s��^Z�\�J�����ɗ3���ڥ(��'����؋�}��UV޴H�䱼���L�g���w}�H��Go.E��`P���WN�8y\yDÙ8>��Lbz_�Bj>?_�s��Hq5ں�֦�����Н��mu_ ��v�>�{uiU�v��u0�1[���k�ō5�y�O����(]g��5h��>���ףK���b&��G��6l�x< H����_�^o�r
Q|��45UF8c
�-f��z?	3R�w�U��E�J�Rhm�����#�چ�,�w{��*f4�C�)�+>�dRS�B&�/�3��H��̀�:��$�8-���LE��n�k|� !�n6XlO*(z�v����	��&�RF�l�`��gJ�8,�V��~����X���%�̾y��Tn��c=��R�ǗeQ� ��&�]��1q.�S��n:�b'���H� ���Ąm��o�x�n����KT�tB���(_6QSB Q��
���e�Ds�)�R�W������"�Rrq�\��VG�F �NO����2��`�#��~�ُxa&?���G�ϲ�#��]��ĠI�1G�G��R?�Ev!>��"��.T�m�65��4�h�i�ӆ�L�،���mcY3o����,�Q��{/R�]
ɴ}�
�4���B"��эX��Ğ6y�>ʹ��[X$�8᫜������o�>�"w9��	ե2�se�T;��h���^XF-�1�ZP��"�X�����<�h`����	�o	r��\\���E)�Z��`�@���GNJ��I69)�}8;)@�`�1�A,��28)��/�wRʵ`ǧ�R3�W���F�Y��ցC��&��L!N�2���f�x�@,�X�R�w�Smw��4*ڃ9�w��S���� v� �`��lvXJ�K�]�zpX��=;,�	�+=;�:l����aUVP��S�C�K���]W,R<qX�Ś�,��[�^U�Yy��4v]1g�o��`���3�r{+I-g|�*�Bmŀ���Jەr|$NX��p��Ȯ-�\AZǹ��r��L��i��[�F]�e6�"Εa_:P�E�΀��J{:/���UW����jG
8'$�I��s]��
����n"���j9�~��@w�����e�Zu , ���h��> B��0`b^:Z�YI\��I�f�ensg]�j�h��
Ҋ���Z���Q�#w����ɰk�eB^-�\�@�5W��r� �wA;R�����n<.⻥M�
6��BmH�f��˪=)ؼc���\AZ���]E�:i���iRm�zR�u��k��ս��3�(r���1�����{��DW�k:'�ο��`��O8��6���H��:��/�Ɨ�c��ȸ�j� l���)�Hi�ϟ��4�X��)2���a���I/�:���J���w�#1g���w��31z�9#���\#��z�g�<��뎯iD��lUq�`��SљF�5z�������<ja
��.x��̈́��� t��U�ZG~�Pp$/�O������^���z�<.X������z��^x�����C�t[Ia���ȃUd�u��ȃ�F+
����.V����2�r̫�+��v�^ZW�g�{W�やu�	���n'����a'.a�N\B����;q	��:;fl߉�/��#�Z��H#u����,���(B@ݫ�H��Z�)u��0��ul�;jU�J+��p8;�ǎ	�����'��ԝ 潢�p��~�q�q�i�q��	��v�p�B݄k��M8�Iۄk�i�pm�m�����*�\c5��XjF�#T,�{v�w?r\y��7�vG��}E-^P��]^��%��|$a=Kn���z��I=�2W+=��j:�O�pn�0�fk�N�u7[�ف������`LJ�4[�y�8[+s4[+3�ֈ��Z�a��W�l]!�5���u`d���ٚ�Jf��2[W�锰�̻U �J,)�R�|��4_+5�*�c���f	���:�	%lHJ�8c'p���%؟���
L��]'T��&D�M����������:�RsRӜ]��O�l�?�������g��r�Y>$Y-���R?��]~Q��`�G��d�>t�$� �f*�w����w+�?x����L����w�Ae��s�N���P�c�b�_/ �s[����O�]z)���޶�g+�l�>^�"��.W��Ƈ���&� ���F�+8��v�R��KK�K�H}��B���
��qe��t�j�u�
#�q]�q���2S>b¦u�qG�*��u�qd]e���2c>"i����;�P0S>"!�,=�d�R�B3�yd�c��8,�V�RVUƌ��	ҧ6�O������	;XV�)1a�Fh�`�c�e�I��[V�P�*��eU���J�jՔ�H�M�� ���j�ӧ;�R[2c�4W,R<YW�'T�Cߣ`�W�C��@,W����ݻT�]O�g巉�-�ZJ�%�Ж�!L!tkJ�"<	��)��������c�Vu{�XT~s���,�YX_Y�p���-�)��,�=�*%9|���)�dO��?` ISd�S&�A����-�l,�q�NƤ��*�x���H���
endstream
endobj
23 0 obj
<</Filter /FlateDecode
/Length 4058>> stream
x��\َ�|߯�gj�} ��z�M�@[2�� ��8����z��+�إ(��tWfE��U�����,���������u�i�����ܸ��U^~���?���J�[u�Kca~G7�����������/�-��l����~.��K����?�%/�~����z�q�I��|���g������?�>��υ ����� q V ]C���zK���~�t^q��jt����[!f#Do5?�b;{m���+.)j�[�t��/�
.Vv��V]uC6��>��m���������-:���'5Ɠ��;�H�ve�aA�����Y1�n;�!7OY7�]s����t�)Hc���;��/�Viy�׎c.1I�DB�묮�uY3�2�:���oN:�PFk�!�9S�Tȅ`�)�����o��i���=�/�6��*�t��'3)W,�\n6����JR�󕤾��a����燐c��oVk�W2���c,��$8䴚`��~`*����9�Lnb�v��$��!�r�H6��o�*#�9�cͼ��f���� f��PGe,��(�1"A����Nk��,0Ƽ5'��ԍ�F��dQ�`�!MT"�Y�B�]����,P��`�������c\��O���CMq�>pq��� Bf��|C�@�Jd~�7焴��8��%���(��f��L�	��L��;��Va����@��S��$50�M�)g��\pġ���]<��腛r���ј#3��b���F���`%7�W-7�7Sn�z_�T�Gw���T0Dd�L����!���a�������A���Sr �$90�M��$��٫u���y���3v��?Im�c�������P���]O������A}Lp5N9����YK0z f�]�7���밠��=e�k.x������O-��a$�L�N�!s��I�m�c'k��2׿rC�	yc�d�U:YC0�]C0v��憂��P_��P�L��B�|c8pS=T�S��9C,v$�����mnf�h�k���sC1<�� 7�<Ё��e�r�q�
��;��&'ɡ`4��v�
:'�
��P޵��^cr��ŅƘ�k(\�R��+�/�y�p�$j�H	/d\Ql#+6�ྣRxM���5|������|,�>ДV�5U�Z�=OW~ؓ?D�c$.;J.W���Y�J'�ªc�N�h$����M�=��:q�Ks^�eg�!ѕ���3��I�Nd9Wd��>S-��0Aٺ9�^G��0r��<�!�"Q�<id�"J���	��
,g���F���@����J�TFm�$��2(E y��&��?�P���>Q�fN�
ѝ@��z�kB���~�bbj���L��W��������Pt���w��XLQs�G'�ٷ)���8�(rh(�8R :��D4#�!R��s��qÎ+��m�k`l���e���<��+��R�$�İ:öE���xmPuC/5'�b�"�Q�n��� ��V�;�1���63�&�(Ә��:b�<�sЊ�s���D���x���}o��>�a�����:ò��x�L�u�c'���Y��8�r�4#��*�ѴL$�����v~tmCڽ�}�7�N6=�h��	 �r=�0���NEP�;�	���!	�����cZ�iG�7��=�$�~j�u�b#D_$$E���*�LB�U�����kP���C��%|6����0x�S`F��
��$K��HM��UHz�g*��r:��5P��G]`��&Ź3J6E4�U;��{~�R��bM <��6z^)iRr��C%jxZ�\��99����l��n������z�9�z�_<��5?�ڵy�{���t����s���5��o���r��s�t/��B��B�p���b�/3�+��6�jq���������<C�Ǒ����������Tz��\����I���M�1��A|�(��	j*CiG���������q�We��U��|�ʯe.��9�|�f�e��|����ܳ��1B���?`Y�ȹ'��sOv3�� �|�������đ�5&Z��!���uZO��r؟�D�xZ����i}_��D�o�ؽ��Ī~Sm��xA�Rx7�k׶��+c�z�dZ�޷h�kr}ݯ+׸�+�u�ݓ�05X�-͊0�W��V��47khXl���lBء�ѮQg�+�fu�36��t�k*�$�
�]V���
0�)E�4Q1��$�S*ӝ@i�<h|��\z��i56inRFP�0S��S��P[Z��f%�t�"tY�� ��*w�ID�X�C���2�3u�Z5�4���Y5اFXq-'FoU�D:D������C���t9��]ՙ&�7�U����S���+�+�%-V���Xa��d5Фxp�MV=�!4Y	��]	:F��B۬�rg MmV�����Ȁ��:@���� b�mRf��F���;��?��J�y i�C 5�ԇ�a�WMs�b�W��?Tlh�5��=GG�B�ך }O���|g��8j���x�~����x����A�.�l_��у|"7д��M�u���G����52�������r~ZS~���*���V�9�Ƕ��d�(�R%RC����5W�E�����������Z09��@"�����|o��aiF K��Zޒ+�-��l�/�&���tv�kk�λ[��XWo��hK�����o���tM&���=f��2�P3��zmA7��Pa���(��F�Xta�m�r}!x��ծ;�l�J��4o�QY�;ݵ�h�r��X�A�ê�L�L�k�*�C����W����-�+^��Qn=!�Iy�K�w�z�v��z�����������+/{ώe�j]��Ћ��Bo�-U�	Ô{Y���vf���������I�]��!��q߂�N�+��{Չ���ۭZ�UTk[8�h�+K�C��A�1?��s�p4�3�o><��m9����p����$%�]q0�;�8�k�����ͤo��;�h&=�����t-�|��DI��p�i�6�m�J��O��4�uU>�-�t# �i{�؇���ک���jۋP9$��'X�F��u���Q�>��W+oD�up|0u#�z~[���0�+ö�4�=?,��D#��toýˉ|�3v��<���a]h���>N����y�m�٪�g��Մhuh���D���mo�z\��c�d�� .��ᖛ��e��~����C��⍧���Ɂ���ۺ��ʑ��">Wg�VmS��߼m7KkB���3���5�z@<�F���)���5FJ	�ɁM�@B�pGK��e9����~��Ji���o��>\�ݓ�=bp��v�!�CZ���㪌�p��0O�mp�✿�������^ �nu�޻�}R٥��O*��~l��]�!��6p�����&�Ҁ�a�3V�t��
�ŵ<�D>vC��_V�;
�r��+�,��B���
��
r��@���P��h.֗����
Ηo����/ �tX�@M/u��
��ʞ��)[ެT9�G�����
�k;�(�Ƀ!e�~�,[�"C�2rl@Ԗ�2=9��y��	�1<��|�k�,�������h��6��t����W}��e0���gNr�pww��a�I�aUP�dL��w���	y>F{�_E�X=��
��vR�]�<��VR�8o�tv���)�_8/����8v#��̮:*�9�~���cU�]�����ה�6K���e/��ǾMk�C�G�z���H��{L��Ov��~@����L�+�C�{��K G��#L��!ҍ��[ H����j�/�Z�bl��>eo{��{#��M�k�N@���M�E�%s�HEf[��7�}�m�x���Қ�*p�t�ͽg���.<�j;�V���k�A�>Ec���{���FB�+��C|���v�@��E�����4�j��A{��V[��Z��������C���Paosl�S=/��ʕ��F�θ���)�i�91����|��
endstream
endobj
25 0 obj
<</Filter /FlateDecode
/Length 3725>> stream
x��\�n%�}�_���͝, ��������A�1`���Tq���lM_�K3��=M����ŭ�F�!~�}��`� _�^~��se��0���?�2����â>�0}��@����^�������c{� �R��/T4����/?<���_�����}��J�_/Bۿ���8|���
s��_-"�ې2�6U�
������V�Q�����υ��9�|Yb�{���F�-EU0C@���7��
=�n��ؑ���d/��\j���~�ҍ��� �Xe�A��z$�!���I��a�ʻުп��#xl���zK�Pb����_�k�"�'zmh�*���i�e´I��J9a���*饣��^;Mpp$�8%qL+�3�/�*K|�R�@u�ڣy����� 	sbeEjY�K��D<�o|��x~�����7O�f�Z�Z� g��a`���¨��T$�j�b]!�;��x����Z�a2��8$HpP�V6W6�Y��14�a�#,�7Uʆ��� ��Ո9CO����NMEE�H��C�O�,Z��<b�Rf�G����и��-�C-R�b����C�a� ���;�K�����\�n.T�l�ƅ7�ljV�m�i^��]�C#���Fd^��6�mڀm6l������S4(�c AKa$���#�)��O�y��
����9\#�耀�G��͢C���A9��E��ͣ���d�!b8��a8H�$:DԒ�����_�������!�|�5��iph2ǯ=aC�u��JNs�B68�lW���^���Y�Ćhv�ǆ��bC��A5��ņ�-b�z"6��"�Il���ֲ�����kZ��A���k\|�ʦhu�֟���u84�ڨiT���9o�Y��f�6�,>��G0�������᷋$@:7H����W�}rƍt��TAC .��@�!���^���(~�������"��Y��	i<����E	�q
�Pt���t�B���� ����� :�!��u)`����D7�@P�DQ��0��g���4�<6�m�C�� ���:!��㐕��Y�ͨ82^�i��ah� h#ǅ���
��Z�Ь6Q�Y�)�|�uq�I��cJ�I��O�N>ְON�	hp��@�E�@&R��^rx\N���)�0"�G(���'�q/�%i��#��@#-o( *����<�A񰄑�yA�Ie���n*Fy7�k�<F9+�D{�:j'�̠o���,�=]Zm�h�O���	�6L'�ѻ�i�S�G�&�Ҏ���8���J2u��U��,���\N��T�je�?w��Ӆ7?�?��Ȯ��B.-��H�DŃe����h��4)��'��?an���qV1�o�ok��C*g ��U�ۤ������C�\>��ni{�����%m�@����S��F��ŭNDE�P� �~GeC�KJ��Lt�D|fS�H�]�J�|�´�S��i���^O�z۟�Ge�拱g<�W�at���c��o�Lf�[��ڥoq�Ӕ�8M�5٧����VQGЈc����!����#<*.��^��E �t)���w�%o=XpV{��R�@��e���^��#A�u>�ܧ(�Sq���w�o��Zm8��=��=M'Mh��}��S�|��C�,�o�-�CM�� Sͧce^5P�Pbi���$p�L���D��y*P�ԇ6e1T����T�3���i�%|k�^���螗w���9{dYVmQ-�Χx_�W�g>w�o�ԑ�|ӦOym�Tss��;�Lٶ,�b����+�l���L�S5^ݗ2�sp�ܧ�W*�8P��<n�DΛQ�������t/���ܝ&��F�9k�K.F�����1��[�v/Ě�f����C��4%P(a5'K5Z�4���ɧq��[�S.rQpHqMA�����^�݆R6����5���-�J�x�L՜ʋ�%�Sau�`,Jв=P�n�:�@�V +�~�����R�-]>Zje���A��U�7�g��ܻ���֯%4z�7U|Β!h�ey��,p8X�:<�e���._�~cG@�6�Y~`����O�*�\]u��eVJplHT/3h ��Ҥ{ J�y�E�Z9�²J�G��Nk�dC ��v���U��P��%��A.=Mi����`�t5O9����Q�Wf��/�����`}��:b���}m�{~��9�CiSF�~l��=�[�`���7{��ԦGo+[�2�@�D#��0k�d�f����U��	��ָ�e8{�i�Iρ?(E�	L���.H�m�{{`nU���`�?g������0Z��a���e�Ӧ�7����mZ�(0��(ئ�#��j�o����˽D�q�	�����u�g�2J��A*���\�t�wx�f��c����pB2	�^
�A��f��H�&�|<U�/�('t�u�ο�9���P޷30y���|gEG�7y'�q�Fe���d���K՗dj\Ŏz�z(qJ\�"hGix�!Bzt����A�n�L��M+Y�!b"*�2�
�s+�s+�2����Ǵay�Uo�0X�7��Ɇ���)�F�G`Ɇ����k�k�X�N5I5�Έ}ñLÈ9ex�aƦɆ�	��v3A�Ҍ��ifm�7����2�%d�b9ca%�P���r�c>{MX��k�3sKj[�8�K|�R��Ұ$�����R��絶[&W�%�5u[v`�UK"+���'�Z����ߎ�*BCƼ�L��((5��"���6��"F��*L�4��`<���-�3�@e�)���7j�����	�*��%��[�{Qs#�D���G�t�N+iI*����_������/t�6$F���>�[%u�}3G㔒������{�Puæ��¸A8/��O%��Qx���|��v��tLS����$���u�� �ޯ9F��:aU�H�_hȹ4���n}��>�9B�J�E��SM���,�ub�5cNSl�O��� 5�8�3]��Ϥ������s�����3�����G�:tKL�ܬّ����A���9��
MKa�ű����31��$���^<���8\����{���{0bղ�5i��-�\��f�-(���3�m�iNa��� q���%���������瞾���qF�n�n�Ք����qi�����եy�[=�5�in���L1fL�8�ϭ�N���O�&��p�GEZ՝հ"i�A�	#�2�e��BxZ�<=��x{U�7J�!�s�^Οw�������
�I���ɳ�@$�3��V�R�n-��3�-��I`�v�@�ڭvh�pҘ�'y���z��78қ�kS��^sO�s��@�)��v/��^���]�P�=���'�}>Q�\���f�u|�ӟ���`ڝ��g�K �˼�5�q���Qǵ�u�6�q�ˤuP�TG��ǺL�+����� a��X��X�u�U�u��>�8B�[;�e�_�X��������ֱ.���ǺLR���GB=e����	��u�D�戾��N77�Ǽk,��z'�V�����=�r���%]g&��k�rsr�Q���ݴ�z��Z��������μ��P�����\�o����㙧J�@w��ӏ�A�b.lw�!_oL���۠߃�}�0��N�y��2�B]�D�D�8�?���
endstream
endobj
27 0 obj
<</Filter /FlateDecode
/Length 4534>> stream
x��]ێ�q}���g[��0�;K=�"�X[2� ���D�"�jr��l�D���̸gdTti36�?7��~������u����/O�x���%u�^��?������w�n���:�������?���������_�/f{����/Qtk��[�|��w˷��D�B}�q�I3���W��?�>��)�����0i�=`U�z�`��< W'���˄{�7�S��_���{ʏw��v,�Xj��%�������7+��nO���6lO�}�� �?��?��[�?�I���@0���`h��I��k�f1���xʺ��#���b��Fm����R?� ��D�y["���p=XguŬ˚�����)go?�णe6�E,ݘ3��B.�t3N����Pǖ1�n�6B?K�1e1�r�Bʞ�|lwzZ�P�bj�x���Sȱ�D_6k�w��y�V��C�c�\�I�	&;A!a�����b�!�n��a:�$DH�U9d)k����sBy�5��AMퟞ�n n<k�������އ6U���t�1;�б`�`���ت��ڍ���EY0̭��fU�Kw��Y_�SuX��V����'6��-�'e[�˳U2��x��r��p{���Kʜ����Zd����),�[�E����
��-���`�/�|!GhyF� "�j�!z��� @�Ep(�u)H�	S��):DL��ѡ@��P�}t �hLѡ`�,5FX�R�[B�?(�������E��	��	K�$
��/<�a�2�)�-<y�Ex|W_���H�Sx p���a��)���a��@�1<D
xJ��@��(��	;FB��ZF���\�}���~��C�W�ϘRX�X\�� �M�3#L\p;0�#\f�Q8���pá�C���W�H�	�"��9|n���J#4$p>�����Q���`�#@�;Bh;���,lw�(��Q������B%2��P�I-�fU!a{}6a�bYa΃@a����c�IC6�pC��3����a(E��P^)���ed �$�Ed(�.2��ed ����`��P�O�!k�DT���VE!��Y�P���b-*�/-*��2*�{�txJ62�8�#�9��0-�.�baOa�KI9��F�IYs��r�� � ���1 ���Ӎ�ߟ4.��NCY��t?�H$D��Ьt��޲K>�o��OA톔�7��*�-��lʐ�N��X���Z
#q��z���lH�bCH�9l^�0�
���O� ��!�M�*R��9 �am���V��	8d%�66�x��J�r��(r��F~#>�3���k��a�U�Xy+��fe	"X�L-[ su�2?2+��Q.y�Ͷ�C?�~ځ�\p*D���+(��a���bVtB
\7,M>B0�Q�ñ5��&՛鱝#�Ж�JՇy$�e5��+"8$��Lt�'yL��6�%�I3��k33bb&���tC#˧L�@���&��:m�ij�j���ߨ/'��i㳘W���Ӑ��Ґ��"����zd����مG����V��(K�ь���<YƩ�*�-;*pn�����|7O���]��{S�q� �@v ��i����̴U�����t5��G1}_ϯ���Q!W�u�G��� n��/�3��0(�0~���Vn{3�;�8σ�d@��wѹv���tͥ��6FU�a�7�⾤r��Ws���)-����Pyrr�h�)r�"��\V=)S⨌�5���͂�OXK�q3�X��d,�}�2�|�X>�h]#IT�;
���HnO���r�_��H�K�|r֬�E��f6��؅�M���j+��A#i�^��x���h�4p�m��UN���|��k�3��r}._�J0q��|����Q�����j�Ѣ�Nw��l5F��W4��Yf�NΖ;�Ȇ2���_{��#����&{��%��ؕ[%!$��%Es�~/)�!;�����$t9#�߉
�ZO����g�|�.��B؋)n
Dѹ��ڽ��h��lض�qP��ߚ��O#�T.�����������m��jw����d�����D�VQzxb�O/�o-ە���3���%�O+.V����j��>�bI����ŗ���-�y7)�7�Eaҟ�ە��4	g���H��kͶ���-<Y-��j�%�nA�!��$�O����%2$�q��%�u�՗@����x�Z׷�W#���Px���
�F�Ւ�eĽ����Y�1��{�6�S�*+��r;��\*��(��I��>�:_�gi��R�C�;��7H�f�ZF������H��?��a�(d�'�q��7�����ӗÈ�����Ӡ��{�^O�cn��$� S0�;��r�粫<s��-2�e�4-�����[&�gR�i�*�_�������p�.�
�r�u�|]���?C��m������S�ʝ֢Z��Ճ�zX���p�˭A�1��`'�~�į���u;�y�x���/�*Kz5����-�X�w��UFw.K9%��mb�_���H�V	�gL%=0��z-��9�T�JG�~��:U�n#K�^?>./��,MaJNmًc����2�>U�W�&�N�91��V��!āHNǰ�A,N5���&vMu��M;�B8��>o���U�k0o6+��!f`=:�q38*��Bh��J��3�'*P���M�^j�������Fp[�o��M�|6���J۔����6��M�p�>�X*c����f�Gq,�X�����LW5���b���.��u�J�L�ߵ��������n$�BBʅ�R}�{ ��ݗ]Lݣ�A�3yD{ �ۃ����oO���5���t�6U����}j<���C�wm������*��x�9���8����ScG�*������h�Y��D�@�%"�nJ�w��E3%����|�M��=���C1)�)NpK� �{[X��}�CP�&P�MӮ�� 3p'Gʵ}��o0� :'�ˢs�as�� e%�f��*�!I+s�Jg�^��c%�[׌I���jL3	F�K��`�{jgD#@��e%�O(�D%@���0: $�'(�'y�h=���.ř���(i�����!��!�&��d�$@!�(�&��j�VR��}S�o.�&)��8/�&�A�|#�&N�Z]�,\;��K��$1�Y&[�Jg�h?�Y礿�H7����o�K;E^+���+��;�#J��Q|����AQ��]ce��/{Hk�*c�g��D��}�Ib�j�Ie_J��<�}
;72׽�3��zӕ����_�~ڐ=d��C�ƈ�=�
4m�/�R��I޵���Y�����H�`���e�NI)�_���B��z��^�~< �-�l�$��� ���b�t��Gّ�>7S�"s5!.b�UdF=�?�S/�-��L�C��!m�أZc���L]~M�A��Nb�3�8���KW3�2Zj����~s{N�>���C������n�.���edUl��l*yѴݱ�X��{��c�'�+�.��]���b��78�,��;�HS����F�1ο��&[��)!�н���Y�ok}G��8�쑩�(Ɣ�ct��7��L��p��Llj�C����c�Gć�k�#h?%q羕�̤T��nt�#!����Sb�{>�߇��<��.V¾��<H����tL���^
>���^m����xxfaMQ�pxv{��^��/��KZU���o��<1�*7�g0�z;���&�^<����O>����7X�Tu#?�mcG�VT7����h%*��UdA�P����S=���b�rv�J�B���%]+~�=j�%ⱆ(&jD�y�-�Ӄ�	��[��>�`�_Aɷ*^ZSj��`���c�((��F���$�$6�(��<�u����$=�W�����`=��v�M?��=��O3�����Q5�!X��6���� k� =�C�\}%L���WY�.�,g��,�u�i�Qad�J�`g��y_u�!!Y���:60�	�@���H�uS;h�7__�xd�KU� 
6W�$��bd�6�?�22�'H��Y;Z�oV���g�_�����ְ�.԰Ũ3	u�Ǫ��٧o��-�;%�%��հ'i��a�!��v�ܫ<2�/貙�D�pZ�*���:���ާrZ�c�\�y�q���Z%����z}�U龟$zw8�i��̲����9����c'e_]ţ[,Թ�x�&M��}���螬S��W�%�7Pvd|��|$u�d��7RX�|��|$gDOo8|��6�������)//z�F�?�ƕ�ܥ3��G.��9B]z�0w/�ys�I��0��x����y+U����Yt{���
�k�ߝ�n�eS���焓��3Ҡ/a�D��&i+�;����^w�A�'��B��M�3%�7���u������K�؏i�Jq��_�hz������U��Ĩ�}W�3���
endstream
endobj
29 0 obj
<</Filter /FlateDecode
/Length 3607>> stream
x��\ێ�}�W�s ��N�h4��� � ov��^`7����bK-Q65Y[3Ru�.�.,�[�*�g����>#W� a�������+Ģ�������7��U:<�'�'(������_?���_��yЋ�J�_"EЩ����z���,�������r�~�A*�(��~:�Um����������T�̖�#�W���yH	�l�`���eŭ����3ͥ�
Q!r���[��v��ST�8�x�~2v��[���1���3|�����R��яY��+� ���
�vȩ��^)lHPz��S�Xs�_Z�a@�]�#+�ǝ���]@��|J�}n�H��\ ����ǝ6Z&�6 ��@�r�0z�@����Enf��i: s$���aQS[)�i�h�ģ.��4F҉^{�R���(E�T�Ds1���Բ>�iI�"��D���}88���G��j-M=��
���:�;�ª��$����!�w޻�b�A��a�M�D���̓�vV1�D:�0�-{7�n�xhg��"�Hs�i`�̬��HA���i}�,�4�θ%�@J�4�#��iZ�4�x&R���[�}��IK�bl����E=��Ncق�o��ԬQi�ͭ�)�`i���k)�qn��<Ғ�y�%�ÿ��%��
P������� |/ ��7[ ~����Db`�.���" !|� D�6\L{�a�v��+kkZA�$�/��o/Htۂi��ig!RQ]�*B�QE��RE�xE�$w��P&��rU��{5�%���PE�eZŐ�d��n�
���\ȹ� �׻�����@�mA b�K%nS��-D÷��`��	ŋ����M��)
D��H+E�>����wE���§�d�Ƅ���j��-ưgV�T�𰌩0��bx�$��a�Z=������{�^�ׁo��tߦ���-ZH�h�Z-Z�߁p+m���l����:��� d�D�&��!ѬR���B�jBDƖ�&�\C�@����zKD�z��1&i���= ���12�0k�w�QG�C"�e؜��)-�G��H�QX5�#h"�L�0~��m���,	iv���L)Bw%e�5�԰JDci�F��2�Θd��H�*��W�n��K���=�OstӼED��BDQhR�)A���>+tG�F|���֑q�Ӛ�9H�$:��YJ �Q*4�qE?�	{hO	�Tlڅ��SҪ@gz��G�.���:���j�L��xa:�c�#8\��n5�"��
!Z����@y cmgk&z�Kd��Ï��@�VCsi���:SkJ!��:�Xf��jWp��N�a�xX!�4+d��Q�
4]���T�u�T'3�Y�Tϣ��;��_-��`j�zJ[K��d��m(��6�����a�'Q,���o���V�A�Eu3[G��0G!��+�
��)�-�H����_&���ώN<�qy~�}N�1&�s���;&b���� qK���`B���eF�)B��D3�YØ�T����RS�1����zK�7'�We�z�O�	g�U	-5�L��X)L6f[R�O�mS%���]� 8�1|�'��ke%��(W����i�8?OS�<h!V�Jl`�X��<!_Gf#�Nڈ���`�ؐ��6%ݴ����<�y/�ܐy����Nt���Wd}<�Op�ј�6VCc(-LJ@)w����qE��O�h����|%������}������p��"B'�8�.�6<.�"૶|��c��9N��5M!Mֈ46��ym����ǹ+Gu�;d<�G��M��^ķ]�➕#�3$FR�h;3��q��̉]+���ܺ�+lG(阄��'.�6�5_�U���<�>tl���!���k#gV=�����T~f%�ԗ:VR��	���㕖�%�-%%�"�lx����y�RTJY�P�[���b[)��M)+�Qi�#�j�3}�>�)��*��8�}���)���L�f������3*��t���`�CV�K!�K_,D�Y�ΐ3�u]���|V�^�E��	Fc�n^��khk���TJ����l�TagD��*2�/_h�6�=�p�VT�g"�/����JL�c�e�c�eF�֔[�����PP��f����_��/����E�������	�t��p���\ziOJ`�Y����T��H񱵃��C�u�و/�po��&��l���q�J�ۉ�[ɫ�t�$�p4�A� �4]}Oku�ה���l3�7W���j���9]�3g���[Cț�2��5p�um[h�k���څ�\��� �7em,��l�;s�J�����F��D��Kiu��F,�l_�v�eo����^D,�e�6%�~�nӠ�`Z� .��y�:9ֈ�
�'m���)8�J�Zx!��tb���M�6��0����围�l��$���Zlx=��@9�%7�O9�G�T��Դ3�~�.�^*v�c1̎���e����43�_o����4��EYڠm�O��=t;��uk�.k~����M|7�����x���3�<�[���l�L�m-���R62���g�"���>7A�m4Ҽ��[�u0�%�,���s�S�v���B<���uP���v�{v�ֆ`�'���O��^e�/�"/�'Tjgp�q]�Pr���7�9�K�L��V�v�y�D���E7f9{�N���U���b6�&b9{WS����#WeF��#�k"Ƒ�w��n޻4�*3^�z~rM�8rpWG
�#����Ϙ�v��Sv�̝|����[�}uLiH�f��b�ȼ�����Λ5/+�������{�̻Ïr�I�0�UC_Bpq���#\��{���!ݭ%�CQ�ҥ��l+��Qtw�iC����`�tIWu��t�bp��b�g����E&�.��Y7�ّ����!�#�� z��fv,3��+ ��q�L��P�r�L�����޼�e2��rwq�Be���T8:s�v�/�������v���Ӡ���mD�����T��.�1Q�.a2YS�"~C �[�k���Ym~����ᐝ܄�Ҕ�#?6OR
С=e-_㣯	:�
�S��#�Z��~P�=�ͬ�
�=Y�&_ ��@_��-e���{�m:V���:$ XͬL_p�+�/�m�IO����� V����H����1�˼�3eXE��.��yuAW�2�bFx�&�m14x�����S F�F�o�(���㤆"���W�0�lm>g�ol�T� ح[1޴�"���(yLW�D���s@�e�0�/��u��2vY}]�(!�V�n��n[~����Xm�13�e�9e/J��(�Ê �m���v?v����oS�L��1����m�o�c�r��CKL�J���ַ#].�.:�0!,�P�	�m�e���٬un�.&�o�|:� ��#�xdO�]^�)���<m5���X]X��,�;�o�.�{yT��ٶ&Dl=��=HƄ���?Y:=b�]�笯VA�%���}�ww��U��l�o}v���=UoK�%֝��ǻ�c��1F�eU�e�=�A����{���)��
����[�-���ј3
endstream
endobj
31 0 obj
<</Filter /FlateDecode
/Length 4137>> stream
x��َ���}�B�,�} A �����6q�`׀��B�E�ԇz�Z��z<j�T�Y,V����ע��w+���^��9-�������7.��z�������?,� ܭ:����0�������R/~����?���.��l����~.������Ǘ�?�%/��
�z�q�I��|���G������_/~��o L�� �U����u����< ����e½���)2�u�"1$zK���-��nW�F�IzI �F㎂;O�R�ie��n�W����pbv{ӟ�3���E��r��~�2��x�[�0ٮ]юQ�bgRx��o��>e��x�������@è�/�'�|i����3^;t�������Ka!+�oS�,��٤�e0��ޘ3�L��`<�n�m0�p���߆�l�g4�m%UX� c �5)WXH bx� Y��v'���G�]L��߮>������a�@Ÿ�+��p�>�8!9�&�����+�!�0�r+1�1� L'��dU���o�V
��Hyjʭ�4�~a7 �6(�v��t����0n�Aǜo��ehRk�	���� :p�#̪T�A���*�i��`)��>l��������g��!g&9�$���0g\�+�0�bd���͜ph���� ����bDHK�A�.1�A�5�Ɓ�8�~z 3h�E@+d�G�`7�!X4��#�����E�����E��Ȁ0��#C��N���S`@�>0 t
��z�C�0�
b�7�cV�3{$2��0�`3O�!�d�I�f.<t�\����Tm�U�<0�62T H���
���f����֘P��PaB-}Z�Q��р-F�O-H�<J��dLl\���2QF�d�L~�p&-r"&Wr�I�L]��L����^�k�x���Ǌ�//���	�D`r5�����q�J;�-Ѯ&�� ��N �k^�l�6�D�/oQC35|��V�������#h��<:�9�M0�����8�����#�``XYy�`y5Z�"c�}�`�[x�G�(O7(����̐0i��*[F�Fل�M��6�uOF�|,�^�o"��\�������.j6�p��&�Hь���E�B�D�3
K¡�҇ap���,\2%�xPA�J"Ľ�,.�!k��-BtE�G'�(>J!AlY���d�Whۥ5`���*�Ek�D���*�z��ݬΠb=&&d�p�\�S� ��JR���>�ɩ�0<:�%z�YE:�5%�M�x��a��Q�R��g(�6Ҁ�.���.4b(��"�Mt���r:������������1��!�+Eit7���볚���?��Y!店1}�[��<� +�lTk��I\��~:�������� ?W0�Rސ�DC��g�� չ��3̿�%|��Y	�
޿���Y���Ӵc�	L<�I��L(	pc��s#�kJ��Vܚ,d�9�ktK�{��ڦ�'�5�0���`{�xs��B����n�D>\s��c�����P��������� K>]0�=OW����D��a�%a�����c��^c?>���a���!��]e�d|R Ja�� ���3�����H'��`"�E�����>���k����8B�I�Y������*�u����/��3��S�z3�<9��*��4��g���}��sg![��+��Ї�>Xv��e[k���Ld31��W�T�E�VBޯ�ތi�	Ѯ$U�odr��gU
Z�ژ��������y�ʐ�|%�S�1�V���y�O��@#���`@6_���b]�j�:%g�;䧧+����ʆ�t�h���H�x��xLWdݜ�+��KW��$������gKWd]��+�(�LWH��'�0\���y�J�+N�3�6�;�t�D�y�Bh�ӕ[1bԘ�\&D�r�tF}���vC�u�vC�|H$,���h���H��K²��|�	+��%_qv+z�|ŖxI�� ��ld,��荹�',u�v����["]Qyc1�?�TX�x=�5e�OYH��RgNMY��Z�O���G���4�)�D+,��D�Nf��	���Z���aM�
˖�
��􄥥u��
����
�Ez�*,���'�Qaa$WX�9�T�E؅X��.�Q��pA��+�+C��ҕt�I������ OW�#|JW�Y'bo1 ����|r����O'q��x;��$wH6�zT�)b��T�m&?ϢxH֠xhC�`��7Y��w�2���2�l0�e�K�J����2y�F��e�+�$X�u�^�G�d�4*qB��<��x+���4t�����:��M�=^`��M�X�{�տ�(JbR�umE����Cp�e�1B��ݳ96��*kG|V�
�8�wJ��K�y�kQB�z?%��g_�l|�v=F�;&ho�ۻ�����˻K�%�=2�7��'�o�}5��{�t��q�Njxcn�U.�#����j��j��֙���j��!Ȣ�O5\m����3K��n޶��rs�L���{Oӝ~w��.]Y�4���2��}{)��Ő�Ð;!n~�R��Fo�J�SKkK� 35�Ж��������7�5� �]�Xl�A=��k��RX����Q���(�J(�i@@���yWfmk���b���ס�:���s~����L]!���!����),-��SO����(XO��^G�����b y;z��AXHs�R2QN�@^��}#k!_�f��緼�Gl���ѱ&�xȪxC��	s3��� ,��(�XCN� <5�`CPS��0LtQ��uu`�R˚jxH���  )���B ,�!Q �'l��N?"*�j��2YG��� �w����>������dF6����ޚ~�6!ڛ�,��>�z[�Jv��u�2c�KC�J��c����CG��oo��!�������ȾQu珆? ��%Ξ:"����������3H�n�}	��{�����"(�¾JC��<�����Q.�l]�+�P�kی�	{ꐲ]���(�=�>G�D�)����}�M��0�p�U�3t?PRBJ�4�9C�4����=�߾>���*WL�+{��M{&e����rAe���&�Qv�W�Vo!����z�f�}.(��oG
���QE�>��7B"ci���d�7�h�zkó4�gCW�(��p�=�2�mG.����`�'����� ჋u��x�v�S���VX�lܕnX��y+��
���?��v?V�K�n9:S����5t{�H�}빂Pj���)8������Q.=W0��+�S���K��@��n���fǦ���� x�������] ��bH*X�}\뮴�j8�U��>��q�������ɉ	�k�l%��|wn�om�"1��֦VF!���pш�����氶	�c=�/{���SX���6��7M��C�u��;���v��.�~�+�u���uj4m�c�I8}~G�3�c�a�z�JN���m��S��+�.����`=��8�`�a�D؂ܧG-�p��<6�A�fS2!.�f��}��i�#R�*���{B4���k6N��Gy�D{;#c6���:%M��V(��?[}�#{���14\�Ē�M�^��ݣ�L���Bc���&0�ˬ�&c�eD������:1p4ظy��{/[��̛�F0Ћmm����2"^�������@|d���K�63��Lvю2�"�׷>�l$������Ѧ���GIx���2�2�,b�cA�Q��rRjC�A�����T�f��'2�q�����5�l����B��W�0nk��t�g+G���,)/UJ�f��cZv��`�޾$t�ؐ,����M�?��e"�%����Ȳ�Oc[����V���ӻA�@S�_f~(�p2ƶ:�X.+Y����0�.Z����V ��F{��&7���G��P�Y�fڕ�Ko�QɔS$<O1���)�/=zL���z˵����r�nN��XaT�I��fO�A���K,:6�$�A�̖���c\h
�a�����V�y
endstream
endobj
33 0 obj
<</Filter /FlateDecode
/Length 4762>> stream
x��]ێ�}���s��,�	vgf��d�|�&v����@�x-R͖4�3�Nf}k�d]�"��J�E�_\٥װ�/_���zG���bQF������/��,>�R�6�����K����w?������sA- RRw?EDУ�>��������?aGQBX�[�i���_��$�2^>�������X�~���
(?� �&5	Щ��ϗ7`V	�1�����a%�>1jj&O����2n$��[�S[k�FqG��ua��\���>����~����?zgV| ������h�=��U+��>��T<���Q,1�}��kp��7�ۂ؇+������"X�'��)=ErݶJ+H��.b6YZ._��6v�����C��I���/uSR���gM����֮$ "N9tR��k��ı�1����V�T���$JK�G�v>c��ӗ;\�x��U)��I�*���������ʠ�����&9��4�!`�H��6����Y� %���je�d>��N7��]���?ݵ�#B��u�@��f$� ��(*�A� ��TJ�A?3���m�]��@��4{&<Xf�*��/%X+�ܔ|�A�O���*Ɗ�Ow-H��-�X�-�:Z�2yk$7�Z�w&����Ւ�ٵ�[炖��]-��cY���Q�_����s$t��;A��;A����N���=Q����BYt�������A�E��0�����	�Oqj�,�/�[t�C7���=2��z?�G��R0��O�l|�UV�U+�H� <骱XvV��Dn��9_]�١���y��	D�&�lل@�C/����M\`7lB�6	@Y';6!��ل@%��&k�m�&�lBW�M�E�&�q]�_�L�U^�E/��,g��xrU��<d.�9[�œ�:�q��r�<���<�Ƀ�ǳK���M�5��7lB؆Mܲ	�6!l�&n�$X�e7lB��~d��T����&�ca�tճIº�,}vq���b���%GѪK�f�.銱xv�v�\���|qU�٧�?�il�cB6l��M"�aDDtlA�@q#DС�{6A�r&�k�;vX=�-�Dxd�&�W�I�E�$�qY�_�\�M��Q'� \��+�J,��=Y�qӳ\mnbI��8�L	�N��N����à`�E@��Y@=�Dld�nXQ?�H�F���Eu���"�.d"<.dY$�,��:����'�a6>��*+O��O f �l�X,+�Qy7��\���P|Zx���X�X3�"[!p�"nY��mX�Dp\�D������Y��,B�!x|����"tUY$]�,R�U��Q�d�[�e�M:�`��\�V�IU��󏙞�juO��P��J�w�x'�w�x'�Tzl�$�#�UAe�?�"�rE����t������6ҟ�,������F:[���`B;�d�i��.��5~Vʌ�"���0*���Q��ղ���Y0(;�d���re8��WoD����zǇ`T;̓P]�kn�����@�8�3m#��0�g�|�L���u��:rX�3A��P6�>���,�x��,���{&�/2;t��������c�9���{�I1ݝi����aM�}5���A`�.���}ܕ����^hI��Q��:kq~���5�p&��w�S�I�D�Q��Nt]xM�5M��>��N�N#������X�P���;���/���E�#���4ݱ����]��],,'��j��dn<�X2�T#A�Y#H9��Xr9�.V����f�e�ɬE9��B�]���Fq�K��55��N�T���~��z��꼂j"U�B4"阶�c��	��9�1N��x��4U���ķ�?c(�*Cov_��S��l8���!&�uC�t%�5�M���i!�D(����A E������ctjh&U��\x!xf�Λ�x�3M:�r�ȃ=̨�G���u�ǳ�ȋ���/���^�
^�|�$WZ4�&�ܐ4c_$�A�Y��ug�<���v%��,F��*r�!<���Cq&sOq潰hۊ������t�)��޴}��{����E�&\�`j��y�Ij��uׅ������i�e��xc��y�v�R��9��I�g��R���&Y��%��x��X�_d��s�[�!����NA]����yF�6or�PQ�$���}	�Em]"�J�D��YE���QsEf�-����n7ȼ���0�y�NctFW|l#�^P�e��u�t�1+���)��P��/��3�0����c�z(���؛���$�0�e�ci��n$��j����T���^.��R/�6>A؀�`R`��%xyO��H
J(J\���G�K�v(��LЗ��{�) �djK}G����:��6��	��d����ܧ{E�z�Ƥ�U����_~�/W��)5��wn��@� ��Z?UT/N��H+�B��0�=҉DL� �bv�J:3 ެJK�� ��������)i�щ��WG9�P�A�8�?��A°q+��I$�p��Mv�`:�StdX�Fl��j����"�6brEm1��:=)�EG��^�*F�J[gcd�E��U�\V�Z7G�Q�˸<͹M�M�1D{�^R��С)p�^t������U��R���� ��tDYȅNTI�x ����#8�P|)I>�Ջ��Z�Y
P%�*Fv�!WE)�m;��K���6��HgWL���#��{Lp$@��p3�)b�V�=ݵ��	�W��0��]O�y���K��"9�s �Q�1���L)��4)V� �S��'�!��:a�[��<R�z��)�u�FV����/:�B3E�gP��������~�����=O�q��:S�4#��4�苲L
5d}�v�16,��E/�)DG�΄Y�(��<�}L��γ]��H�O����ӬE�Q�]�EWȳ�m�������b�l'�ga�gM6c��=eӸ6�9c�;q��Ԏ�ⳙ��Qfk��/k���7뱐1��WQ�C6c�H��[��g.(&�*���#�0�Q�	/	I�*�A՜?�|pW�����pb��Se��\�@��)��Hlj���V�EC�lTn����U�����V6�71�w(���)aX��Й4JD�VN��):�!}J�Έ,��uNJ��VQ��(.����8�t&�U�i�`N�ĸ�!�!1h�U�6�L����~2wSMy3��X�c���M�c&v�����.�DKE)D7�ܔ48�51�;�P��ʙ^�=�P���҃��6̃�������2�UF)m���q�Ŏ��sߗ)e��aü+X�<^L�������ϵ�U.����D���z(��*�ꞙw������UGi|��6[�V+3��b{�֪�����<K�Sq�4,
;���"��^}N@��1����Ąۗ=m�H`i:����M�	p�zax���X5~��S�Fɰ^�K��c0�$X�:KҔ ����vu�d��1�6f�ñ���sW�U~�st�{����g�h��ϼ�g|������p��?]��	�l�M���'1M+�3�w���8kv̕��{_{�`�:�-&	�����$��rq��P�	V��[�\���J���^�~�{4�^]+�j���j��B���E�����lw7�}u�͎�g_gUF��ê,�r:�rr�w��y\�TZ��Ȫ&�>WJ�J,�J�d*/��s�-e����r��KeS^�5���fu�qy�:�⬛�Yk��g]�I�Q�dk����^^w�-��x��F�Ö��K�-���.'R�
�9�J����v�ws��H�v�+�7�+���+����l��I�����l����ae���dO=�#� l�cZ��W�{��AB�{M��[A߽��3�w�3&���
���ֺ���Ҽ��i~m�7�7/D�v�Z�T,�)���?-&7���r*�m���l?g����#�e㔬���l�:b��6l���u��uk���m�������m﹩�6�U��o`�߹Fm�e;׈�U1a��U���&��8�ٶ5b@;��[g�u����֬u�?�:����H�#�����o�kM�癷Y+���z���}�:=lK��2����^���'���	�/}]�ֶ�F�%򸪏�(�R5�7�7���&��L{ŢQ����)��m��F"��6������?brm�~�ʝ8--׹�o^@�ov�ʽ�+T��+�u�B�Ī��<4s_گ�At�,W���.{EZOr=w߳@]O�f�g�[9��w]�!\r^v��K����l���ce��'>6�k �#��r*����
�n�@�_L�s�;�Z��\����R�[��fby_:������{S�<�@a�[y�C�Pg��_�3����o�^/Vo���j캗Ve���|��	�r>/{���ҧV�����V�)���Iޣ��o	ƩR�r5w�_\
��7;f{L���N��D�F����υґ.�n�}<?}Z�3�t0����
q'¥��u��V�u��a��h��FJax�:��5|*�χW�H��Ƚ���r��&3�2l�w��׹F�Z(����9�E��įo�Ρ�Ti�n�KW3��_@����y�c��o����T����y�,U^B0k��#��.��r��p��8���q�>k_s�Y���e{d=Uu��� �^c�ri+5C~���� ��gcf[��p�c�
endstream
endobj
35 0 obj
<</Filter /FlateDecode
/Length 5563>> stream
x��]ٮ#��}�_���� �u��l�����20�����Dp=L^^eJ�Ű����GI2[��LjS:�.���f��`�e���˯/�|��	⢭����������&��s������_���巿ח��_��G}�R)��	|k�@����巟�%^>��*Jʋ��RًҗϿ���������/�����*��||�H@X�!etl.`r�?�-��vS2x�\�}#j׈�K>߱��{`q�JP�%��������d�^Z轸{����h�P�Ia?���?�|��m��1ɚV�<V���ѽVo�A�D��~���nc;]�_E�,�EOU���RJlܦu��k��R\���� ��HB���Ѳ`�Ǡ�B��Q�_�x�^�T�����1R��8CuJ�u�t���v���b�o�ړ�
$iI)jQ��B�\^�t��z/��F�n*�P?���oW_�j�$L��g��X'��:���]��8�ʠ����A�w�\$U
%*�AT@�2Fzwq�?�F;��T	$��)c��Xu�//x?!�y��t&�B0����"/��"�;Ơ%�J`Г��¬��*]S��`�4��vk1l��֪FM =a���*9�n_^�a���Y�^�B�=����}� ��C�4-aP5}b���1V��0��A!���>�%��Y�~N	��F�4�I�4�I�ƟN�9ʸ��@��,�Hcq�NY��)�08g�ÔE���sqA�Y��)�0�B�g�-���)��H�X�H��H��/[����>�{����
��֔Qٔ������L�Y�ڴ�WB/6��!sa�42
� id�E��sa�j�%0�F�IخU�������Y��)�$�e�jY$_�Y�ގ���E/�c�����' �:�J�U�'��c��	��r����3i<��3i<��}C�ht�"��]	FOY��)�08g�`ԔE���sI��>�08eߘ�0<M`��H�X�H��H��/[����>�{����
��֔Qٔ������L�Y�ڴ��z�"�c�\�>�08M`��H4f�"N��>�DCR�!�06eߘ�0<e��L�W-��1���ѻZ�� zm�ܻ�T 1Ӵ����q&��m���n��\pj�L���L����案���MYz�&��}6I�>�$p�&Jȸ�&	�g�Nل�0e��I�l��}6�`�&�c�&�j�&��u�c���]V��+$T ]WV�ήTd�?�|7d�fӒ?��[6I1dF�l��}6I�ĥRG)D�$��	M�	�r�M&I���'5	�g��l��j6)C6i��w�z�A��&/�w�� b�i����L�1�̅�����P�<���<��cH�E��˺JF��&4ؙ�	cS6ap�&2�)�06e�v�&2**��l�`�v�&��j���js6�k6�Wc6������]6��O٤�:G��H]C�UeatV����/w٤�j�Ŧ-Dلb�&��ل�)�08g��e��'6	�'6�)�06e�M��6n�&	lل�Z6�c6���w�z��S6i�{�~a �
 f��0��^1���\�Ͱ�NE���<���<0y�����?^�ƛ���Ṉ�d�!i�n�/���2Q�	�40gPo��hH��l$
�U2#h�M�2�����)mS��8����T2�ۘ�vF8!���H���6�F����[�����q�����@�!豋���/+*�2@v3ކT_i$R�h9j���7����Et�c�tc��t���B�+"Z�tZ���l���^����M�Rtkvy��{�&�a�cWR���ax��Zy.U���YW�Q�'�x�n"H��S��0FRH�ي����J�P�b�EZ��!
4����K]=([K�X�'7�<�� jLx�Y�6�ǁi;6�<e/+���Lɠw�`�u9�-X�̗�^4R��:P��MDŝ)5Ua�"K�(t������[��,����R�h��X~>WU��i*��U��D3� L3��}�wo��qNl������Η<6�>�J�HN�[&m��GH~��X!,�U����*~��M�'���7�{I����	��}�V�;�wX���*�,��b�� � Qt����+��|��$1X䘿K"�!_3.�G4����ȼ%�0���F)k6@�]��b�>*���~k�4q����"2]�����X��H]ܫFr<l5:�Ŏ��b��{���Zz��h�c���Z(�&>.��WdQ&hP�c0�_�������P�5{�����g�������`�GO� �$Ŏه��?P���[$A�L�b��D]�%	���~'?�����
����.T������[���\��1�O����)�EM��5�"�&4M�t��nyD�d����\�2�2څh�>R��W�7��D���&됆񒦟�K�HVĠ�\���hf�+(�_�U���F沮�U޹����g4�մ���e+6+2P�ы#͛OE]���i���͐V'��v�"��ǚ?fޥK3Ĉ�B19�������>�~{y%��#1��+�S5N�hY;&#u̺}�]�Z��(��}d�Ww��ƨ���Ф���o����ҽ��ۨ/��sDǨ�uq���fIE�d������������i�?���e?�Ǣ�(�u𳥸�UݠÕ9n��k醍T"�;�2~别��մ�����C*���[�5��J��K	Avr�9���HI6!���J�ξn�d7^`��:�0hs��7���%;��������nt�{;�H���u�(���:�ջ$3Wu$:��ê�;�m�j��uR<��C�Qu�T���e�YU����m\�}�p:��-ue���WN�)�Þ���:=d�eX�t�:�zୟ��p^=�o��yq����g6T�����z�f���1�?/k%�ªťcͻ@�V����Z�^���cM��ʮĕc]���
k��+�ǽX=F�`����Ľ�(��㦸/#�7G�@�2wt^+����y<\B&�S猳��L`Z��h����r2k��r(�w ܡw�o�W��-K�ú�n{�l*�����,��$�3
��5���֖���/.k�΢�����34�2�b}�*�+̓}�d�k�л�ج���ڮ�^�����wm�2y�V�	���[�aə`�wb��5g��V�+�+���V�i��d�F��QZg��~��|h\�=��n�Bv:`�?$�=]��a��b7����ə[��ݔ�i5�W�~*������ S"x��K ��b^���qJz�.,|E��%�n�_*z8����w2��|���7���z_�(y��+)��/<���~�*F95*���X&y����U�����ii��Z�W󤥟�����ҫ	�rF�=Y�B�t�J鏤��G�|q�qS�nE�>��NU�#<�y�}=".���y��<�i~.b�Wd܏�=���+��|���1���en8��k��Y�c!���a�fx�z��#M��ki�uU�e�+)���`Pu���鵎�%%����kWm,��%�6�?��7�������o�@�pX!��J8H��q} Pw��ͪ���� �F��au��4��w��Ձ
�v��D<H�}���ڽjkT���=7{���F�����EqE@I-6��k��L�VT*�k�z��w�$ݖM�n�޳����?uQ��)k���u2�A[
��O��W�~���VT��H����Nb��) �C�P�dg�{��dGA:�E�w�j�����d����'@m6�?al���F!ͯ�"�Oh�(yX`���(2�%𦂂�����U��H3� N3&��Q;8z�����G�~x��V�l�N{�y�;��3�������K�vR�j�/�-��ؽ���A���0�Ow��8�u���umQ�ҪUu+��"U��į����6�[��}z(Nz�����E2�(������@>F��~�ܫy��O����O�Vs��t��������q����N��z���?�0z ��V�j���8��>��9�1x��s���v��캍Ӻ2va�֜�2]��������,�>Zw����*l�k���F��P�XӬ#(s�+����f��K!�Ne-7۟��2�=~i���.�CE�ON�
C�e0/�<}=�8��H�����I��o+�0�]ת�'G���:}.4h��Ef��c=1h-��I��b�@9�ZQ�T�,�;��e,=��e�}X����1��DR9��6���V�iw1�J�r���ڱ��:av��-o��vf�Z��)>AJ��:a|�"P�@N�@Ȩ��V7�� ��U\`�[���-������v��g25�dOX�-t52�ސ�4�AF�1o"��؎S���8�f+Zom�}@0d���7��ĺ�j��+��v�I���ll���E��뼭��u-�!�Z',��|��C�����q��n�;S���6
���.vg�{�:�^�0��Y[��%+d$�)�0�6�%��v�'E�v�^	v�_"�
��EPl/����Bq�I���!��{��n;Ilo����C���w�6QC������������ ���߁�D�ah��p'���77R�7�-I@��Xg����
Y}�Ê���#4�����@�ܫ1)�W��������J�ڇ���y1 iЁ�=I�����s]����q��y������>6�2B~���J�&�ښϘ�߱��<6�t����o�O}���}�?�~�pd��7� {�����W�\@8Mv��;ȿ��%�佈����r��_�`�+}}��p���Cq�*W:�HZ��*�w�uy��F��[�9L>mqW�F�MK��4[,4 �.��<ޏ,[�nb`٢H��X�H���F����h��<[���`�Y����I��"]�z6`��kPQӗ2{��0�'�s3�Fh�m	�m���!���v��6��P�n�.w�y���-3Ѧeak�E���D�P�#��ڼy���
��*�H�y�z�?�F�{ �`��LT+�	��F��P�N�u�;Yֻ�9�؎ҨP��l��cG�i�a��F��i6�?뱣�t�U��f��KM_��J�+���F��q�EAp������|?����(	�ڧ��c�ַ)~�����4S��_��;�V��Y��ߩ�E90ju�0YA��t�G�~�R�� �"�3��
����n#�3����[�<����ܖ~p(��j�^�OlF��$O�9�tP�#%�]����C��P��\�њf�Mڽ�0�%yp��w��s����=���:/9�T�S��y.����G���|�f�99�<Bj^�5���D����Z�y��L=;b��H�=���Yq:�]�Nj�S1�t#��:Ҕ��]&�$��G �^�4R�O���T(��d�3b7�R�CS�ǫm�(�GC��y�8���T�2���Y����d|�
endstream
endobj
37 0 obj
<</Filter /FlateDecode
/Length 4694>> stream
x���n��]_�����l��s� �IQ���?��f����J+�dG��Y^��rx�*ӟE��V��\��1,_���~��	b�V�����/�o 7�t����'�(�������_�~�I/��/��^�T
��%A6�����w?~2K\>�%���TvQz����Bh��������� *lf�	�@��1�L � 6w�`�?#n�]��a.�v��Dn1߷�R/�0h1BT�`p�q��{�7�z�Ew��x-Gfǰ�������wR����H䴲��
8�`�Z�������V����
�=DY�w����~{ ����J�|�F���_H(�8��3L��.
�
#�/�=H/]P��kk�i�`1f���`�J�
�O�Kx�J� ݜĦ^{�R�c*�Q�Ѕh�����-��" 2��Q���/w.���O�d�1B�:�1-r���Ű*���"�j�éB�w޻�.�L_�,ʠBc��	�Et��_��F;���dj�LV���U�x�������D�!��hm��kA���y�J-H�c�+\��RC�̯�Y�� ]'jr���6�ml��E�OIyt{x��JS�s�j�rM�8$��6|�zW��!00�i������퐉��l7�&X�����HX��=���x@x�yޜǛ�xso���y�|")qLx�ț8 ��&N��7A�Λ p�M��;o�0�L�M��&N�n�7A ���&<�&�y���$��$?��$øn�1U�M��a�M��8Uܐ��5f1�lL农���&MT�;T�V��Ro�$)D�M��&	��&	��& ���y��Zj΄� �ޛ �pO��0v�I ��$���$�'IOՓ��Γ��L�h\����$�/�v�� '�l��Č���쏳��*��5	���3!ț�xsoN��i</�0V��2�ދ �l�H�m�H�@�֋$�֋$���v^�j��$�6�I�b�\�Nϕ"�)�)O�)0��y�>�)�oE��c 7��,f����7���މ���S�"�nCKN$�C�D�s"	�u"	�s" �;��:���n�H�d� ���s$	X��	,���$�#IOՑ��Α��L�h\�����/iw���g�q���!3Y�m,sg"�7���;�|Ǜ����c�p��%l�W	�c5����I}������Ι�}>�Z��1�d�0���U �|TeW|t�^�P�
��v{���cd/l~d���SKk��-��9G9�<�&N�X6�)s�J����z�Ȱ�T
�(	�a��6�0R��aC�Oh�o�q���?F��
qb
Uyn�u2v؁,�����Q#�붇��3�!a���]em�@�����	3}��C�*g�U�0����~��
��Q�6�T��XoM�s���rma�ټ��R
����ܹ�B��duZnrd8IG��v�
nZF/���b���
�
G[ǈ���vJ2���$[v3ڣ3K$,�h�~`P@��mM����E�������dH9_��c�Gs�-�s^i��$r����.C5��c~���<V�p�����y~�\�]�:�0��kWF2F�~����#�c��Q�i��C���M�U�k3���q�����Y�ᐇ�C}>O�8j.�C�_;�^pҽ;LG�{��dyv��/[�y�?U���T�^d�S�q�����\�=�3�9���	�~/��i.��lI�M����ذ��AF���"�,F�?C���UU*�_}��'��f��)�Х�������Pc�Lm���IN�d�D�O��F�.�����U3�g���{£m�q1����p��-�:�P�V�R[X�ҽ.\�q�ǕD ���x�o¡lp�k���~�a�)�7�x21�Q>�zz��B�<z1���!7���B�\�N���WJU=�W����NZ~��V�s��Ph����ΰ�3 Kd0k:�2 L�0^��",@X�|��`oF��Ʋvూ��{ap%�	���PG�z�*#�]zj�%���W%E��PZ�8� �x�e�9��X��Cs��2�W�p���k<�l�8 �G]&���X�L��8�9�N"2�&�VfUʨ����i�ǆ�Ix�ԉ����I(�x!kÜ�E�f
졃����®"@0�;bn� _�%�Vr�� ���X��������']����.�g��V�ɭ����p>��n5
��O�<Z�TEX(��I)0�HN}�Z_���@s�Ղ�fU�� �V\�b�����6>�,�9LB�*��G�;�4��n��l�&��&5�.i��ӌ�3ӗ#W�������X��C6G��m}�I�Z�m���`���.���~���c�Wb���}��}�j�ip��_�V����{,f���{�5h]�N�m����e�C-9H$K�p�+h�c�����}��ͳ;h���[���vF8ݡN�^����kL<��&�S��1����;��r��U�vGa�y��Ps:��ۅ{�"��1����Üwȑ��eƖɷ�f�1N{�o��1�]o�.�:�?�&�Ré��������u�O���O<��d�'u�O7u���Mѡ�NH�+����.��[��9��뷵��BD-��h�nm����ܗ��c	� 2�`"G65�3e�{���?���%?m��)i:�~)F�i:Hr�4=z�J�di:���A��X
!�7�4=B��4�,O��P�ԳBx�^a<O�0Jxi|J�9&�DΔlm�y��ʫ�����%� �L터����D���ĦQ0�r������y�iL�
���Gx�������s!պI�a�+��afU��j����\,�<��+�'�H7��<�K��3O�3���OKtٸ-%�h�3C�%ٌ���W�y�^Y�t�AP�E34�P�A3l�!h;x��p^[������8P`}�ހ<Og�+��$M::M�q�����|�T�i_]4y���e��j��ë���L��m��{�u.��,K��؈�O���ƼJ�����z{���H%d��}~��O#`�k �*<��v3���L{/�W��ڞȨk�ǂv v���"�Vv�)�4n��^��PU���8�jsM�c�!��t�8��H��1�Q��B^E�/D�_7��f� 55~���>��&�=���A���K聀�c`�<���g�u��*	Aj�RY�F�b=���O��K(r��'�\�V=�s�z=�N��[ˇ�0�(��)'Q�r�~�D� �J%9"���Gt5��k�)����
�����Bvz�B�wuE��[;߳֔���:^=s0�����]��6�T/���uY���j�����2gdj
m��i	�JG꫋�h�;ܰ��Ϊn�}�C�K�w\}+�C��62ic�"�@*_yg+�ʽ���|}��C�V�΋��L$P��3��EO��h�x%R�5}_��H�읐���}�X�O#�j2���U?�8�v��w�ᆜ�s��|���\f̹�(����;�HC.mI�+��7D���Ăg Ҧ��p�(:��������{5���4���cs��6<�n�B�]������ �>�e#�c.7�Q|�e��u��a�T�Mpł�ˎ-�=�J�:���:�N|��ѐ�\;h����*�N�xR7���m�9�~�_����<���z�ʓӲ�X��������䑶���S���qbw�J���:)����K�Gٞ4�7��������=�i��R"KI���W�A�q���9��[�7���2�.N���g�0�u������̆ ���JF!�:��Ѷ"EKY��ɗl�b���7-�Gx��0�eSƴQ
m�ޅ6�_2t�f'�G{p�Q[��J�V�{Q����
�ּ+g�-��gŚ+ˋ�oG��Z	����͹`M8�޴-�rār(���iV��%~S�Mtk�X��J�]E�UeLZ��\\Z�TNnGeL�S�k˘\ܗ1)Ϯ����ڊbuL �`�]���{�� Yi��1X�ʘ,-T���MV�����T +	js��!�+3�h�j�F��[>�~Qܗ2��J��w�b*���R1���9ڗ2��2������^4�J�hLvǈ���5<��F�^O��})�
�U�q�N���	`b��Z&��֔o��e5Ax�jV�0�.�f�^�Ta������ ���8"ToD(S]�F�K�ݭ��/jX��1��QL�A>�[G1W���Q��F��Q�UIݽ�xP�Ԁ��#�ݮ�9��G�n�\?*y;��F%M��T��
Q�Q�§��eK�+�\M+D�R�
�(�S��([:^��jzX!ʆ��*D��"V����
Q�+�*D�xN�J_q�}*�)'Q�m{��9���
7�KÕ���՛4�F���~������}A�ig�c��\C���_}.� C�\T�� /�/�<�[B^�.:0�%^o�p��w�=騑>�\�͝ͳNg�0�M>�l<UD����D �[���+eb���K0�N$���i��KM9��=u𭵗gf
���x�����D�?�H����������Z�Q�i^,aݺ-����
endstream
endobj
39 0 obj
<</Filter /FlateDecode
/Length 2650>> stream
x��[�n$�}ﯨ� ���;X{�}Nb 0�� ������ԍU�=�˝���t�%�vH�R�
&�E��U<F�פS�˗���'�lT�q*-���?-�A�]�ǡ!��}z���y�������f��^Hf�����)���8����Ë]���+.��ń5Dn�������qY^�}����/ �	vOL�`��5�f�i���F�y���˂;�V�1�u�3����|�^{m��+#�	
Q/\d<���j:��Vf/�^~�ua�)̙������OZ���/�h�48D,��=��QkVB�ȟĴ�=D���/ �c��k
8I���Ή��yZ��/FG��у� �L�(TXh�7��B360�'m��z�Bӣ�����44%��B���4�:��D0��|�_�2p��44��~*ĨiM@�b*D#��.�P�:2;=f�+��~�r�)��7zZ�Ѷ&�wʤ������:��k�<$+e%�3�KjE��C�[��V~m����c3��L3*���_f[�HO1]j�K�V���U<���x��5�"Vf��i#�s�,��E*j�UfX�b�3�H01x����L��0,�0͇��h���Øl����k&�u&cǴ����L.���@�2�vy;��^"�	z�tk���va(] B��K�vw�H_N��,����G��y����{���;����<w�}����I��&�\���d%PU~��%��)���X(%|X�Xɣ$HD��D�F���C���֐��Sh�`HC�1c3�L�d����F~M~u:�qHA%���HKXgc�"%�E"���HԔ��ToC�ت�f��-Ѯ�)�Yx ͯ�� -���l֮ȍT�#KY�j�4��`Y�b�Bsl�j�F$OU������K������K�}�5��
�~��*�� >X�x�L�1F��[U$?!���Kyl?���#�ŖS��R�j]¥м;y(���j�T5�OU�� `<Ee7�!`2!�HF�j��%e��	�i��!��n�i!�l�Z�jo�>�DuІYHCgf�.Ґ�+ت�#-�����@���Um������,&�,Ͷbf��`м��9V-pҔ;�N�ՁVm�V1�E9�ʧ-�7o�ijں6�&Ň1Im{�ڙ^��)�ƿsJ�'�W��!����ǖ�l~��l����^�oc�rPD������]k����e�+�5y����2 =���9���p�# ����?��k+'���mZ.�^��VK���H��j�|}iа]� c���B��������BD�D�p3m-����rP���w�)� ��_� ��E |��T#U$����@���<H��F�Hy�L�N�;!��:�A-���Zj4lbb6�v��y],�
�:�e�}NG�Ũ%��4�5�"l%�~F"jkAE �z�aǋ��8=�Ў6�S+�y6���Ū>[�#Ԗ13���l��K3ߨ�a�Xa�ұ*��Z�*dt'T�Er�V�S�*N�LI�fj�c����p�����#2q�i�/=5f5��V�3d�Z��l豲1�K���/��%?[�w���\�>��kqZ��>��<v������4���$18M��*)�-�>�q1�_ձ���C�.������`g9(b8V�t�x���h��7�����D]���YMS�
��7�BeZU(�������Y��η��ϼnP2q�L7Ik>~ک�O�/�^�*ӓpmhxN]k(mu�CY�]�4|�9,�=o[�4c.��ʊ��p�e����1���U{���?W=���Dp
vSB�C�K�<w�5��Y�&t�FF�k���ҥO�w��~��&�s=|��x�R��)�p�wl�+�1O��U�Yr&}�F�c\Ө�\XB�L����p�d6���a�r.�p�8�
֐|.n:O�nUZ�z?kp��w��;�A���9F{K�Z?�#*N�Ob�O�ȇ�t�3r��0ϧcB�!�'u��N0����?�t�=Nh`�c����\.p�g�O���897�Mب
8!���C��g:֎�;�uL\�^��?p^�%3ד��B����g͌�xKoLv)�Z�>�S�x���ز9u��e}�(s��ߚ꾨v��?����]�As�C��V�/����B�dp��Q!����F�����4�KQ�k�]�	��"�C�U���S���P27�I�y+�˾�窘S�?)՘�ӽ/��1�>T`Xm�ѵ�[�@w�q��2��'`O�l���E�R�a�S 'D�;��Z�g�)w��7�������1(v<�I�:�I^R���y@�.Ơ�0c��w��b��mi�{8��Ӌ	qG����C2y�,��{�#o0�4{P�/؈2���B4�����(R�x��f��{��B�C�0��7�O����'y����͜���W���Y���qQ����
 [j-L|-KYA�T,ű9�Դ�h! �pd[��+5!�=��$��Wj{M�t�6[#q����Wjӵ�+��w�R����R�iu�+���+��Fw�R�h4r�&'̸R����S^�	��Ԥ�c�����,��&�O/F;��
���ܼk���\�u��"��wE
{WԢ��?cv�0��卥������mr|�
endstream
endobj
41 0 obj
<</Filter /FlateDecode
/Length 5101>> stream
x��=ێ\���������~�춝����d�X�H����:�P���.u�ڞ�t�$�II,֦tL.�������-����ߟ��ϕ	⢭��������w��M:x��g�_�@y��������?���?����?�磾H�N�[�|�������?|3�x��L�0��7���/���������=9x��/ �p�#�'�� - �sH� ��>$V��'���:�V�M��	��Q�E���;��K}0��UA^08�x� �Bm��>�{�_�FFE�91�s�g���')�����H䴲��
8�`���zC�%��Ȱ_�	Fo0���*P�e��-z�����@�C��44���B�`//� ��1�����6Zf�6>]��Qy����'"�5���d2�8.J��+�Piaq���.W0�I|��Ĕ�A�
V�*�t!��
��֗�Z�: 8
����듋��z�W��Ҵ7#�Y�c�S��h�;e���6�T4WZ(U��{�3�Ÿ��KC��@*S�I0-����y���**��"R���Ê>�<��#�!/d�t&v8$`�V��vt
�9�/��J@���<H@��L��J`�� /BH@-�>�
,��6�B�Ӥed�]_�<��o'���%�Hq J��m�]�"v@Y�L�q��V�+1C*b�M\Ķ�`�+���ы���:��{�; <p<���w|���q��=���,f��FX�8�E�L "��$���$O��w�'�A�q�g"O����L��L��L��Lv`r&���L�Ιd��:'�c�>���+5�J5$� jt�Y�:+S�!7�S����ޡȴ��z�&I!:o���7I��7I��7�:y�<z����	�5�$���'I@-���$�ѓ���Iҫ�I�ΓԷ�j�-�8=I÷�v�� %��J�1��Ob���V���Q7�0��|8����4>�FN=O_.�4ZE	[�a��	��Ho~�P���@+ ����	���42c��OZ���d�sA�ʁ�28�+@n�r�2� ���D��(=��x�۬�N @Ч(,]
�`�R�-�U�(�%���Sb{�Η4>Cw��tXQYP���ő1`[���.,��̸[�F���;3�v?
k�� doaZ��
s3����ݤE�h�m�6ht���J	<zF3�R%�j�^V��<�� )�	2&����e)� ;e�V��*��K��AA(��x
&����d-0sS�]r�ŪP;6ʃ��0�@�a#��P�^�2l���s�#i;3�v��������jBH�U@'���R���*�oi���Egda�qiDZ�[���2�@��v�R�ZG�髜:D�H	�DG*i�)�4~D��	��:TL�zH�n�n�A�;�6[�������O���'���&?��=	7�e^�sa�
�V�O���o����?���������ǘO�y�s~������{�Q�F:2���l���Y��
$%=3�5��I��Q�Ծ��tWս�I����P�,�>��HK#7�
Ι������>?�y���;?��y�|g}�����A�c�!Bt)z��;�ٺ
Rw�4���n�:�M�	<����H�{3)7iEԱ]ZfK��Ky`}���B���.:��'UH ,��,�u �����/Ka.!?>^��- bA�Y�_�B2�! �;�a��Gȸ�U)	1ZMвe��`BH����4�7@#����I	���B�1F��E�y��м�	�vϖ|�}M����������E� C�e2��qD_%������`���ƒ�X3��⩁�E ���$��ڋ��� 9���{�V�r��v3�4T{NF��f��x�D��z2�L��W}-^�:�!U��+=��TYn ܱ^_3bH�����x�!;7�)��RH�h��(	:Z��Y{��)����4�\O�Dk� q6:�!9Y���p'.����{�� m�2��su�ex#!V����n#	r���sSqXe��4Ã~أx���e[<{ x #\4�Y�%��[Gu2r�lх�>]a��.�l1�%�L���t��%X�O�/�C�5�H�,Y�82ؙX���F��yD��&`�z�� uS�u�S��n���C0�:}@��5�n��b?��EO^郍B ��./�<H\M�G�^I'?���{v��X�#�߉�PN��J,��.���Ca��P�#��d��F��'�u�#1����e����CXw�
vZ��5h4���/��*:�<VDG����#���:o4�Es�2w�ub�}Wg,�8"�w`��|`^
ng����Y)y����J~zΛ�B/���3.)峚1Wx>���̂u�|��N5�ϧs�,�Y���X�s�+�b9rw�2����cwS1+n�S܁�<đ@��R���lИN�x:�Z�-ǫZ��p��o,(�V��8���"��؛wx��gT�2�_cZ���~~��S��K�+��i&��t��w���Ǵ����)�	�:^�b�����"w�C�r~ȋ�?��<H��_|:'�O��)-�M����ټ|�ȏ��͟Γ��]=o��{�?W���x�N��CN��C����[U��z}�?�� ��㒰!g��&��Ƃ�̡��!�2o_�;�Rgx��bgt�!�����+R�3s������:O�}Vb�.T*�����ٽ�Ylul̩Pؤ�e�9��Xx��d��F+��`l̼8�H`��DݿdO��T)�H�d0=���������S�}^�
�Iy�9�C�~���>��3�Ɠ��]�T*�ky�ǂMXF�ُ,*�Ah˒`@�G��Bv���԰�4Z"�WB2�tO���*�;&^��nӡ�Ɂ�T��M�Ӝ�k�$ϝ��,h��+ � .�e$���I������l�4n�@��ʓ�u�(�A�}$g_��}�Q��g!,g� �t��H^	g�������6+��c&���=�)��g��y�»mn�Wq�V4w���ma�"��T����+άY�l���o{^��CO�p�0&
����8�e�\ݕ\K
�>Fw�����S�39�]��{���"Es;�c�
)b�HO#�uC9�6������'w^�_u�^ኃ?۽}���P}/��J�\�>U����men��䬺|�iZF���M�t�Ə��em���f3�S�2�XV�~h���uf��&y>]����H[C>K5퀇No��q_q���(��t��\��+RC6�.�X�Ηė�W�.��`j�+"ye���e�b�)VE�: ���1�Ϭ��C�Z����Q�إ����ᱏ<��>ve����Mb��<�Y}	43�ʏ"��A\��N�jY��|&>�!�;|�|u�PI9�@�wƑZ���0�*��C�p磢Z�t�K|7��q'���w�d�j�����?�~��v��x�b�?r3�6� ��������Gq'L,/?������;��7��<�A��;�J%VwV���@]hI��CP��e.��a�tֶJ��� J	��6B_Dj��ja-l+�,�F[�_��~7G��gy�Ԃ(?ǶE�:���:�e��ϱ��>���5M�miSF@ooDD{2Pn:�l����(��h]� 6/�1]OF {�
-(Ck���bk.XA�!c�~��:�EZ����'� �*2;��ڌ����^���cXi�XQ��Ա����JR�~�	��-3�o�X��-c��Vi2��4�6̛4
�hѹ9��Y�hFiU�
�!��.�0-��$6O�;Kj�?��d���g��+�|���g`H�,k������g�#k�C�@���R�&R�kEJam�XyA{3V���� L�i�h��R� ��E���:KZҞ1�"�7^ ��Θ �5#UxO&�R�Ш%S)�����g�֋q�[\q�{����� �����fĀ3�����7�Z��B������7Q��Nb����[��8�S1��	�+�J0�����y=�ܭ�<b��So�;�X&���+)�[
�V��R��6۲���dE�c�s��~�����<$G�F�1�\�70{��)Y�^_M�Tk�6�4�Z)ôr��PD�S���%�P��|�f����Ȳm���������Bd�hy�lS�o�jRj���1�:�ޚܖD��w�dn�}�8�=6}���d��jM&SߗAK��1��J���b�� �־�������E<6��-��ϕ���;�^��{j����-�bUZ���S��$�"ƛ�ʡ�oJ�$��GX]k�D��%�w�t��d��۞�N�⾢�����%�?�`�֏bs���;2�t\�Mzy�����T�"^��L���A�!�a��&}�ϭ�XC�a��Ɉ�[�x�AO�坐�ő!�4OP��l��o��ŧ˷@�}iAeu�&ߖbє��	s��Q��2�*�2�/g�4��+�[W�߰�s���b���:l�(y�˅���ӕ�rV'r�ڰZKE7���$��GR��]��SA��6��^"���[h���p�5����dN����[�j�b7�����]6W����;N0d�@C���ح�Q��6jHrrDH�lR!D8x� �Ǥ�27r�8�k)	�l5?�M�H�_⚒`��[2�z�����'��n���k'L�Ş��Ji�f��2�4A/R�ui�*���I�(l���F��u��w��o>�i��g�t�o�Q�t�z��=.�҅6h��jn���L0W�]��H�5�7&%}����!/<h�!�UIY��I:J�/I@���TSvߎ���Oe��o���S\�Ӎ���AͶo�K���K-�z��]�9y5dZ��3������	�����綃-�(�4����U��˳�^B�]��ԭ$r���;�M�� ,}��n�F�o���oS.Dq_Z.�F��r!���r�����Q�ז]G��r!:��-ż�1_^.��V.t��-ʅ�+w����L�{���i���W�-�#놂��+��Wf��2�!�&~�W�ylW.�k��������E��
endstream
endobj
43 0 obj
<</Filter /FlateDecode
/Length 4597>> stream
x��]Y��~�_1���} A �V�sb�J� ����@�x{�vșޕ��ʒw�i�u�x4�)��I���6�1�Ec8}����~�L'mE<��χ����+�f������'��O���y��G}��?�>�IJ����"���<������O������T����㗇?��_N�������8��0{�'�7@��)�`s�� �+}��2�V�M��	���Q�F���'��K��'8BU�� .4�Q�/J�ޓ��_<O��s&��Z����)���ǜ$JZY�X�wPG�Z��a�7R�;0r7��گ�Qޢ���P��:�ؠM�<})L���A	@�?�N�>c���(T{Py��Ń�ҥ
Uܼ6�|�`��xR|])]A�����v�x�bN�^{�S��P���
��.�T^u����E�� *�PAt���}��?mZ��!�Б։`�(��}æ���Ҋ���C�B�;��( ��/�JR�"�Etq�?�F;���:5D��U��b� >?��Aq��9��ā�Fkku�^@D�c	�Zj*�z�}�b���"U�u�
����e��l�q'��Fj-�G�����ǉe�z���b;�ݴO�(��W���Suy���'���D��+�ĀO���N�?���p@iqނ�[�xoA���r�����v�E��� �I�H´	�r�@Ň(� aZEfh�1�����Q�YI�>�$�<�$xE2��H��D��i�"#v��$6L�'��i%Nѹ"D@���{e*q`"��]U$*4�����ޢH2�!� �CI �5�`�f�"�ʳ(��}I�y4-$�$	�A�A�G��#Ik$I�j$)�H����꥖Hh�V��%�]���@D@|�I�:W�+�ì�}4����Kb�J
�<ނ�[�xC�9����3��MN��	b �1� �E#�iM;�&]41R�GA-c4AЅ��&�E��h���$�Iƨm�:�����7Z�s4��#P�k�"�لJ�˟�|S�U�5~��[4I1DD6�i,I�3�R��h�I ��ƑY)�	��(�Q�D���rO��>
nN�G�b��#}�ѣ|�G{�XS��!��h���r�<ḻFq�*A�kD��-�N��V�__I5ނ�[px�g��ٵ�ӯ��ME�PK�~!�w@b��*f��,�`2d*�D>mR�O��"2��*p	��&5���t ,�ޤ
�<Lm���<"J�ATft����� ��DaiC �MIG�� I��;��aF_Z*��`MY+���y��K��`@L&���[!��-=NU�d��?���PUA�VyU�U[�.�^W��+��ܕ�9�Y��~�,���I|�B�E��0���d4	��aX�*KY�@$7&�@ek�@��*�������� �͖2����jLEk7�A����fACSʻͨdM�(�!�Y����Ȫ8-�o"I������� ,�,M ���[(� �^i)d6S�.������*������@N/)]�@i���4����T�F۩&��Լ�Rw��(�E#�GNi�\�*İVnp��@w��-���B�w�	�0����_S�3�3~Դ������E' 9����j����]�*	z7
<} �lJ�&��N��Jk~:�t�%p=4� �#G�ӪAB�6D\(
���T��Qp�N��ZG#�9�Bb�t3T����&f�+��,�VtR��"�L��]�ш<D�h�ND���ES�m�BB����/�bld�=�LZ�U#�a;i�,Q2��0OY��y|&(�ו�3>ׅ�����P�%��em� aڒ�P�,�
{�������o�u��,2,�k������eY���|ї.��^Ά�L�c��2֐7:��(aoN̦���Ȫ�'��)1��`����?�����ŧN����&R��C�n%P����T��Ȣ�$��P�������$�0�]Pl�t�a�*���݉�@�<�ho׫���{���q&�V�ɘ$[Ƶ�u���/����:铬Z���7=I��;�Z%7e:�w�O���Nsb�n�p؜�F��91xi^I-	���m�4��R@�lN�E�o!�v2&ɶ���t����2I�_��|��K���B�_({Qt��ٚC�C��8�F��?�mMҦ���Nɼ{s������Yp�����}'.�/�M�{1�Ӧ�>�"�is6�r�]�-�^���|8 eu1MΥ��71��#篬�D�tGL^���]�GϨ�,����"r\0#n:$=�Eγ�V���OT%����G����yi��M��ё��E���pt��BR�����K�PV�m9�df�@�d#��.�Y�a�u�/���ג1�l�e�RBAE^��s1��77h��")��@i�Q]/Q�B�b����ʹ��^$���iuU�V!��7!��#���&UeE�-
�ʨ�<p��9p��Kܾ/�ʨq!�j7.�KF�hg���
t�3Y����ڛ��/B�wP�m�m����: #�3;��W[��Ii#!��N�וg�e���|Q�S`Nv���mF.���˨}�l�AM�Ư6�3�M�k�v�rB"\	���+!>����g|3��`�eo��L�"(P����}�%v�&ޕ�� �^�j�D9z�̮�i���"�!�^�B�����9d�9iᩪ	�v43lpԶ����s�A�l���F�ҒNz�fF���@������4����w4�mKFR|X�q'�6�s
���6��T���T>@��m��c�*��,'�ʹ���$�����;)i�H�����z��}� +N�HX�[����+�����Tك���D���.�/|��%|A]����M�j?`$J�j������,���,��+���T�����
��$�:{�%�٤2"���Y��S˙�� ��NvT��l9���{���|���n|n4��@�7�2���Ő��aQ�����{fdH��[dr`��� +�+��ۂ։�ֳ�u�J����� q"�����ZVQ���PKD'�t���45f������KM�l^�\���˃�q���Γ�M��K�&�C�x`�45�E��5�!�&��m���`{=�_��m��RO�4<n�k�=K�-�������M�:nb�/�<��>O��;�åˬf��Z[���d򏗗�����+	�J^���:��G�z����V97<n*@FNg���~�䲡m��֟1��O�k��C�C�r�s\��hv�}9����J�&�2�יB^]�>r$�5��W�/39�����!�Y��d�ܮ<:h�^v����I=V����/˛t���N�]��,X��̠���t��N�s�{��'���	��K�S�n�f������r�x�6H��ⷼ���DS��z�c��_�i�,��Ld����wL볦��p	7߷���F��un^�1Qr*���tߤ��f��v,�tdR�<�Z�ߝ�^ö�U�����z.r�J�t�j�zg�����q��>3�8��!>��d\����%�k��6�ߔ����N����� �(c������N[���`5|�w�3o�7֍gYT˯���:?��W/���M��~�������ݻ��/��X��#����Ǵ-o\�F֧S׳�P���Wx���_�':�׈Էok�r���S1f	�s���4/�|�wx O-'Avw�`��|�����H'1>�΢�&|: ���i��CP����f�K�g�s'?b́^�^e̿[|����O��ŏG[�a�t���:,���� ��=xA:�ԇm����W�?��C)�^�g����v4����ŷ.�ӡ6�?p��z�[���M�
�_��bS���n7��>�������~�W��S˲��x���;�7���v��o�aQ�]{Y�H�2���&V_�\ =�x�d�_֗R��B^[+��q.�7��&�-פh��7���o���e(�3B��U)�A�-�C����@�:+�E)
o�Hg�k?D�Ii �&������F���R�/0�t��N:�.�h`���XA�I�"Ԟ���{��-��r@��t`e0a��@nJ)�xUJ�])�t�Ao�k�����)���^���+S�0�V�W�T
J�Q�F�.� )hv����@l	�� �ϐV�KST�֦����=7�U/�W��b�Rw��d �]aB�mW���}(�zIJ��(@@R;rQ
`��(M��÷z�)P�c�M)	K-u)h�2�[R@oH!���I�M7M��`j��s[�jפ@�ЎƓ6��!*�����^��2��e��\�����B��CmJv�k�e8�� g"٩1��g"�[����P-�~c�3�lg�:�h��ޯn���[C��&���|�B&ڠG˒�^����)�!t]��ұ��PU�*����^с�E��a��4
����,��3?��{�qDMN�C�����
endstream
endobj
45 0 obj
<</Filter /FlateDecode
/Length 3672>> stream
x��َ#��]_����} A��9��d�|�&v����@�x���^�������n�}��UH~~X�[����n�����	?ʱEj���q���\���R�о������_����ǟ��������B��~�K�X�����Z���3�(`�iW�Ћ�������O���N>�� �z��6 lH ��=8 Y :^�@ś��o#��^w�`�m���6�=��+z��V\BT8�8`p�����W�P��L�������H&(2g����3���ĹY���[���=�$4� ��S�]���F���ͅU����{�yR��[���;�=[5bi��%�1����(4C ��q.0RI�`Rn 4����)�|�������J#q��`9	���{r�x!d���s�ؤ�%2��R+-�3�����4�k�^ v���@ CY��h������w��\��1�I�@�����ƻU���Z��
��XkZ�AuW�Y�N8�T�I�o��P%�TT2UD��R��e��8��v,�d������+ 0c!$��R`֘Ľ�(�2$���p_�� ��Ff��j!��0�N����D��,'�TnK� @t4cZU9�B�P\M����P� �5�ib�E&�|�舭>�݄[�����X@D�Y�;����s��tݗ�@*�\��/�Z�ڿ��W3t
|�����a�q���)gaKɼ����S�!7�C�`Tt����x���w�%
w�0�|��%P��7�斮�g���3�6B2�&h�`��T��p"\���k-Ԭ����0�j���� s�x�1ah�xV&
�g�ʋ󁻙o����W9�}��(FU�����-BmD�;>c>�W����!<U(��g`}��^ܘ��`�K��t��`�O��'�s�@-��V�N>*X�!�O
V��``����"H�5���#�Y�`�EThPP����qT�f���2��T�����0Y�`�Ak5�`PO*�q�]�*�iX4��r���ʢb
��(�6EfBE�u�1��-���[�$����������,T�>�piM�B���
W��WAA��o|�!R(�`��P� 7�V���[�ǃ� W}@���F�9\��b2PK�	���Ѳ�_�o�>Kx����2� {-���n��u٢��X�Z�k�*��le��XΞo���b� ��l9�"����uǵl�i�k�oEX��6))���+��ռ�"!&C@�c��xJ�"ba3�A�5kjݎ��K�U���b?%����)�H��Y��X���#��D�L��U�-��BO(of�Fa�<@GO&���^g��0�>B0
���`�+�۷j�S�(pN�ݒ���ƆdR8�yK�a��`��X�g���PCbz�s�J�$���U�p^w3���}�	 �����sB��$j�0��٭T�H3���Ze��z�<yo��>�c(j�#�8��f(��Q	7&�R[<gK̡AB�yNР:(�m�vEh� �L�U}.��V�U>L�d��t�vH����nV��͔{���U�K
�놠H&i�Lq"��Q��^�5~�2�kr=b�ڢ��V��\�^փ6�$5r�BPHD�y� 9!ňt��U��K�UK+l-/k�A��J��+r������Y��=���,y�­N����sC�!U�-�p��i&�Ԫ��x�,�����K�^������vF��F��	�c��%�V�L��*�s�ى2��o%��-?'��PJ�P��d�*]K�vV���\�fI��~�/%�����W Xo��q���R�d⽧���겑Ҋ>��V�%��E�d"G��7���ʝ��Xhz
�p�[�[[ИX~��$�x��Ö���++�v5S�k�P�<W���ae֖�������*[TdI%q�%�e*}`��k�ݑʏ9�b���$�(�M4o*��Uݪ����)c�ե����%�XEz�H+巟�u�P��%����k(��3�M�Kqڳ�٘(��$�ˀmO����t�������I�J�+و6eM Ӫ�=4#���`r���hgx2�#���P�|q��O�qV���F-�4�we��3Ζ��3���'�t����ʥQ�z�s�l茳�ͥ��Z�/�����\�hs�1�2�(:�l	���g͍o�1�w�Li%�g̳�[S�i@���\��VI8����l�v��¬"����L��P�	m�����Sm=�RX��{�LyC�iz�i�{X��0�-$���ἲ����;Hd׻��Ro���R`����ٕ���,���m̎!�l�F���Kv��l��+�Iiq�3цȐ�-э�*߬��K�?�ܶ{l��>o����p��Sͤ�v���uP�)�-�w��'�3D��7pc�}�8�m�zI���m��_㤔pl��Ju� c��}�u��p�avXdj�s^��*1ul԰"|��?	B� +̮��enƑ衶�P�aB�%�B��1V1p����j˘yv�쉰M��r>�����������=���3NnKa����r$��;=�si��S��a�T�w����}&�4��𙮬��v�<�#��� `���je>d��ec$�#l�deE/n�wl�D�%����xjS�kQ������_�*6#͕�me� ��#�;�nQ��wh?Jz��t˻���.���+�b='f�o�G�H�ɉsz�)׃�ٹ�;��#�Z�{���nk7�l6�&$䵤�ʰ3��X���z�.O��;c�=�T'�,��׀�ʶ�p��C/���,猾�z�\��W%
�T��Ԑ� ��!�n搫��1C.���!W/���fʆ�z�<h�5[:d��K��!�Lѐ!�#EC��#��y��b;�we��db�ȴ����NM�i��;�u�����ü�� H���n7=;�:w��6��ta ���A�&��^�v�G2F�!3���|�õC��z��<�XrK�F׺����-�ã�[��3��?�b��ܖ�����4d��P���Շ-�������yǾ{��3���#�%�y�cFAy^�t�LUm����(��%K�Gbn�P<Gx>�^�!�EN�>��\�]+�6��Lg$/��4�!��r;&�U8�:��y\��X�9<������<����҉T8d�)œ�(:�x�[�p�$]��;����g�x4ԃ�W<��9>=S2��#��'�r�n{�n2z�i
C�s���u���p��9��ɧ�Z7}?���i��n�
��nRt�ZI�jЎ�9�عK�ZB�8[6���G�5���3}צ��㙍.�W2!�g��*�=�$��]����c
%Ư���]������=�CN[��C�����o��P*�s�G��3��5���Z�\���Ó�B0MIAaL���.�����[���u�j^�Iay�x���l�W.j��8�|ge�T��r�Zݲ��V�׼:�N��]��gWs�d�ߐ��4_��R�i�k�;�r�W��ǃ*{�arO�ꑝ�,�������p� W==��h>��Q����h�xX{�l;�����Q퍉�!�N<�joLiot�yD{c�db{�B�퍺������o�_ 2
endstream
endobj
47 0 obj
<</Filter /FlateDecode
/Length 4758>> stream
x��]ێ��}ﯨ�&��0���g���k���8�I2���Lu��j��H�<�ɸLV�bl.�.�~���erz�:�t�����?���%u�^��?������7�ݢ���+zP_��~wY��_�~�;{��?�x1ۋ���p.��[����_�~��.����4P�P_l\b��_��|���JY���/����/�`�p[  v����Z�v�����u��/���/F���%b6D����;��k�&w�5I_)��x���o?MF���ݲ��_}��2s�������ߟ�K�__h�L,O~kH��Fߵ�Z����eE���^l��S�Ս�i(����i��\F}��^���+_8�Tb;�����b���`����������n�6X�5g�����hLMo�m ]8~^�ǡ>n鱠��h#鳂��!�2E�rCʞ�7̝��^�j'��p15�à���Sȱ_}��Z��fF�'s�fB釜Lv�+���/���b�B��:F;T�:��Je̪�F�ޠ�
H6u`Sƚ��ǚC|}��!u\`����e�8Xy%А2. R���(}�bU{UQ�m��k�^ ��j�f��:�.`����zU�����O�$�v�>,80 >�8W.��Ã�]5BM�k�i�n�f:������i"]��8;��Kb!Qf�H��#9�[&�?XC�u�:B"��l��c� ��o0[̺4��rzL�zҠ�\Q F�1f�(s;+ڀ��Gk1Fa:f��z��/XI�ǚ$�Ր$*�؆D_��ԍMt�&�Hc��"�iCS�A�,���,ز۸�b�!70��j�2P�������P�Mn(�Un(h.��UI���]凂n�Ê��P�Z~�C~跃�a����Ʃxp�<$���*��i���C0v�@�6B�Y@|������-R��/���l�c� �msD�69�`W9�P��r�!j�1�������1Z�&c�*It�$V�$��cM�jHC7lC��
q���&F@cE�ƨj��kz� �c87�`�7���V�,�0f	B�Y��m�`�*Kx;m�4���CMU�H�Θ&|ͬM�t�*g�X��F�9�`=G�U��Ř#���FmXt8a ]��
�Ҡ���M96M�`�m�f�j>��C�����>������coM.{⥇ɚ�i2���'���&�K�`W`�`��Y�r����V$E�U@�*S�p&N�!t�ɯ�j���+����a\�A]��������gOke�@r��<#0/F�eƌU�\r)�@��Q���)TX��Q6^�1^��3��d�iW��EGr�U�*��j�f�PURg�aS��R*�u�uӠ�l¦ly^�"tĀȑ�Zx�oy�'{�Q�R�SQ�'�OVY�'���biP�d!W@���>a��xS�H.��\��>��y���d���TnuՄ�C�:\�!7��0;ez���0��=�g fbXH3y×��9nQ3��i+Q3e�
��>�6siiba������q��#g�ɮV�"�i��EĤ0!H�ۚF*Vl+���隆�E�L��Ӎ,\��t�nxS�/�~-��ř�WS#"5Vy�M�>0��v%ժP_l�W�C�x���מf�*�L��_����[}F����������Xy�켞���!�k���)l�O4| 2�W���p�>u�;44#M�"�5~ �_�)�D"�R��R_VŞ"��}��,��=|�<��'��U�	�,y��W��6.кU�B�W��s~,GrF�'Rn=�����h��]S���X#��i���gI�)����r�潆�Z/z;j����JU{��%	M/9���dPwl�i��[>흇V���'m�WK�{��������}Z����6-�W��zy�j���*�i_�O�7\��	�_�"�7�Ucސ~<�uZ�(oV���e�>ͪ{�rS�u��y��L�أ�#��^�=��@���^�埿K�CYF�e*멡,����"E��e$��\�����
|�\J2�¢IX��_ؔrB0���rLP)f���=ȑH»R"#b��T4�uD3ł�B�X�7,-��#�	\�ƍwBKy��aT5Ŕ�1A�Tl!t�jȑ�Wx?o��u!F����X��'��
|��{�`!��]X�*HE:C	F�n+0�� �/x�0@�:C�"�{�$�+@+��/B�5��!��x�#�|LC�e,M�!j/�GQ�ګay�����o� 2�dCݸ�:�K�}O��}ȴ	�eI�S��W���:��5���3gn��
f�r_��e���7�b�3��8y�_�lm�L�dfic��f3K��d�\�k?���u��g���̼ȸ|]�B}�YY����伡c�𼥃��x����ŴBxٵJ�:���MV�{V�+��wU��z�>����N���?��eD�e@^��@�o͟ad�o�ZW�﭅lX�|]��'�D>{K{��ZC)�Rh�]n���@(��ڮ�Y:� �ǹ�T��
ڌD�:�f�n���	�{���Nw�N�N0���sD�r��w�H���WݾAk�~����
;�͏���:��s1���v�8bJ�x7�y�(����<��/����N��`1xk��p u7�9e$��p��~��B]?���G,��L?�,��N�@�@�Gk�~T���P ���+�����?�1�rG���e��m}��f̼�<�����?�'ٞ9��GJ@4�7�*=��O�u˃O����:��b�������.m,;Zvd�[8�����G��P`}��r�UR����b*Fyy�+�� zdg ���	ܣw	��_�m���=n�p.F?�t�#�]���B�z������ѻ�@���(���Cx�n�\�_�±@Z:�=~�H��E&���C��V��FK�z�I��9�\�O\�z�~�+��!~Wx�X��D����n���~� F脎�*���f�����`�N�¡z9�x��J*�_�h|�ت��5b̋�����l�B����瞖��+�9>��6Z��6"�C�Jh ��'�lj��G�Ɔ�06�0Lc�$��%���Cro�b0��V4]��\R=նA�Qj�ڷ2�����j=4	l^����;�%��*�q�~�{{l��k;�Տ������b��t_����\��>�x"�oP<�3e[ӃϾ*9��e�ro��}�9���p ����x2�-�L.i�D��𓦯~=1��B�g�|�g���6��>{'�L](��%���V����*G��^&�x�����d|���J7R�S����H��o�Vnt�ub�m�i�����,�7���[=]��܌��2;rR�V踐d�*N�r~��s��;�3�:wŨ�
|�:}�M��sFn_&$�b�U8S���w��s��_��>�-R��@��@4���]��k|Jb�Ԝ�̥|�CG�t흊��Oc��SG8��������o˝����k��Ci�;�PC໼�8N3'��N�Vz��r̞�g�y��P�D�|�G��K��S�SM�*ַ�7}�8�����^erj��,���ܧ�n�7,���qz�O$C4&����[.�L��}LMM>u+�b��&E�ubxL��ΘsŀF�z�`�s{�cJ|��>5�{w܏�i8횅��$�A���
��ܙ�5��Y������^ر�Ĕ睿��S޾U�tmqx��)&C�Oϵ�P�\MG{V[31�/_�.c����V�5[	�~|�9��f��eޜי���ഔ:��1���lW�ص�NjeKErE� �I'Vo�J������Ɉ��h뾰��_�n�]~2�f�<���oI*�U��%��a>���E���hjm�uT�m�����8oXG������g)t:���c?����s`�๭F<w?��5��q�+SD`(�����r�x�0_�/���0�Z�e�Zu�^��yn��9�j���{ή
6�'`�OW߱�:��t���4�p���/���؏�|��S?\#��n�~�;־�w���*M�@�6d��ޤ�]��)`��1݃{WAo�������>w��z���n��N�?Tn�F�4���6T��Y�a*�˻p��6T&��xS�-�6EِR֖D��Q6��m�%��.TRk��K�c؅JP�B%(trjd���͡:��D�K�X�6��}Р��&T���s�l�0K�%=4�"��!�@���"4�j�؄JPlB%ϋ%���9�
��"�-/������&T&��<l@-�p��e�y�@cK#ʓ$��؅��H"8]�����K�)u�P	�]��yi�$t��2$�ui#%"Jé����/t�������d��K�m�qhCE�S�M*B��І���f�P5llC%(����)�L����4��c��7���pr*�M,���p�f��ɬ�����z����������f9`S��9��찷���\k'������eV=WW�}��No����o��3O�Pыڞd�q���zs�2�rߙ'g���z����|��lSgLՎ�#[������-����n��X������'VE������toU����!��{ڗX�H��jY4���b/��~�ρsč��䳻�pO���o\s�zv�3;d�R;d���ޥ���P���}��sD��'4OL���� �PlE
endstream
endobj
49 0 obj
<</Filter /FlateDecode
/Length 3842>> stream
x��][�ܶ~�_��Qx� E��>�s[�n���$��@g(^F�Ί<G�9n�q��;9Wr>��xV:��I���f�59Gc�>��z���1i+��ۿ.������,���ߠ�����~����|��G=���ԟ�z�R)��Dx��n}����G3���O�Q�PN��>He'��O_/BۿL��sqp��?' ��%�-�'��-!�}H����$V�Y:}�t]p+�d�Dr�LԆ��J��c���[s'�
r
`�,�N���[�S[k���n����BQav{WZ���z����$����")q���zj��g�#d�|"����7+㎣XA܇(s��CW�oh�'BJ��3j`�5	N��~18C�*Lx��F�L�&�\��'��>c� �tK0\��;c�q�I��II�J�B��������A��y����$���*�Ls�	+�*Z_��E��ƇB��/?_\����6k-M�)΂I�H��9�b�b��S piV�Qi�y��.F�%��dP�XIZDW�F���*�D�1K�xi��K���/r?R�
�6�\�6�h����")-Za"
%�7�̓L�ݲ���&bG�S�'�~q]qM��d����S��eU�~�r!�Qo'AT�%�F �Y$m�t!!N4nc����jB2����0�^!õ8���ϗ���?���4���`&y��&����1��
��x"A �׬!��@�:d� �AwTD�aAG��t�[���  �m-\n��P����X(�c����FGzZ�B,�m̂=�)� ۅ'�/T�- FO���[0����|F���W�1ڽ	5���1�C0��M�tH��o܆�c����?p~��j�3`��R�Fׂ5H^Q�]�c��]q�?#��!�
����a�]�J&x�*w�����lu�p$�Z9�D]z!dH�^��>�۰[�Ս�cF⃄��+V�U�F�����_e��qudm�G	�P�C>��q�<b�2>�X]�zo�y�dc��Y��f\x4K�r�uE\�pG߼Nmś�уs�����J%JV1������8�����8ψ~��&�{G�ܨN��%�y���0G���*X6�t�DF�g�l�u5�$NĔ}��t�N��9F�4ƪ�"D��������BX�{�ήG��Z�L�J��S�P�3��O{=~(Έ��a�\=3	�ٓ�I]�$��Y~��Z>�`�C�7�A���9��m\uN>~���+rMxՇq+߂��a+��������T�L�P����7�\`M���9�>5�.(3Ͱ�]�Av�r�/�]�E����,	�
�fE��� Ň+4�����_��0�]H���g�|B���[x��=V�{%Έ�[�ȇ���_.2�YE����a�N_	��0K���J5@u,�ُB��f�$<u0�~��g/���h�笍r�j6ǅxV�9�x9�|d��Ļ��x'��cp6*��G�(��@��{��Z��q%�����h�V<ёҊ5R�Lm�����}?5>@�z*�T�bv^�E�,;PA���L��45�C�f�FC�5*z�ظQ�/��5*Q�o���A��Z��Ƙ����k>�c�
"��T�@��`�� &�Yk����,�Xĳ���$��G��9@��x�V�\o�H���X���]�!V�bE:C�+��V|Ƌ���Ơ�TTtH
���*f�'�H�3��˥�*��N�|������h0[�!]�3�T�W�#��#t�W�L�F��S�j�F���I��
¦�l%P�.�FLQ�J�x�f�<��|�
Jf��6'd�m�Ig�V�MLK5�b����p
A&kJ�=����J�aў[�AD��9�a�;"��{�����1��%-�T�R�[�����ӭ�9:�-݂��gz
iK�e��&��Z�w����*�V��M�+��uNsN��A�X\u�Kmh7�Q!?V���e�p���=6�!���o�@��J?��F�y/�>��2`���7��d�mQZQ���ጦL�׫�7b	RZA�'��L��,���h	{F Z3\⪉��(@��Yr�����Rl�cΪu�&O���uO �G���]`u�3{�|�D�O�J�/}�P�f�]۞1>u���Wb�.Wy@W/���3&7@ ,pqŲSD�DS_N��/��;'���>ɴ����)Q��d�:J�לp3.�{x� <_[� ���j��a��1�C�ށUVѤqJ�!�V��-���8XäaF�:���ŌU�>;����g$�ƲSD�
n��  ��'\?�����`]��u`�-��~�9��
9Q��-�N�b߲��Sg$.m��dm�e��q���'��l�{������+�=D�w২<��ݱ:B�^1[gZ�p Dx �Sf�e�z�{"���oۉek�v�el��K�L��n'׷5�z�LL��(�y1$z�� t"�G��Ex�9l���(�����m�gc�r�y���8��OdP����WCh����C�����	P#
/�5��@���T�-��h,3�o�y���*�!Ѣ.����fE�hBy>�l��C*����2��NF�$���̯g)�]z@HV�4���Sĳ�1Q� ����=q��N��E��B��Ш��\e^�/~2zh�<�vϘ& Yk"��p�9xQ�@����X�"i�%ν�(q������)�Ҏ6�h�gi|����a�D�n�(a�@<c�W�lg~�l	8۹���e����t�Ӊ�ij��x������/�H���V����������2^�PI	���ӫ�$�H��&f�K��F��b��xρT0ò�L�:��f��	�)kͻ�	���	[�����y�>��I�V�{�1�!\>5'�w�zɏ�]���pp���{R�Q�UN������
��̋A�*ZߏX��'/�
=ko���6�uI[��hB�	�x˓$�8��S�rl����޳Hຄ����W��d��fV�>b����B� ���F�Sy�K�<y�4o�I���U��2t�����6���
���ӊ��ly���ؽYv�S�K~��/8��8O:n�ʲ�߰*7|��F;C�Ƿut�� x�A�*T{ �׹�Jl��R�����E�b�� �������af��z�S* 7Gհ�ɟW�`����{�'֜�+�A��.�p��G�b��,���6R��-����� `jj�����zS�*��?��|;x5f�+u����@��mۇW�.�4��<[ca���3/��W���Jk`�ǵ��]��Z��"{Hٖ�}�������xK"�{�ت����nfb3�f.��&r)��
I���]��10	y�����|�* j�2�siO���	�ǆ��=��m��.9^��t%@o'�6��T�|L���RX,�*�r(�U��8.;�;J%v�_
��u�JX���J��ǋfv��UB쪬X���,�f��*��mX*����٢a@|F�EN\���d�>އ+��J�]9hUt���x?=���[���Y0�Sq3I��6t�n�Kj��p_��jF��۰g����dg���S��߶f�X���b�<?�^�f�TiǼ���@U���}7VqvW��L@�7<8��F���eA3��W0[ſ�UFU�
��݈���;d��/�b�ܮM�������3���_��6����x���u������n+���\f7z��|�6�v/<q;\|V�X�<���i5c#��by�)�����R�X+je�R�zM��Q�}�
endstream
endobj
51 0 obj
<</Filter /FlateDecode
/Length 3442>> stream
x��َ��B�L�xdgf��x�|�;f�� U�����8Hvƽ�*���Y�26��E��7J\&*C�i������7.��z����~���_��
�N��~���R�����������z1��Z��4�~��>]��薼|�	*�b��	�_�]>}��Qk���|��%��O?.0ipk@,�8 V@��@��uJ W}�t�p^HQPq�Ĭ�����k���wF�#�$X
�Ѹw6*�gk�&wM�~{9��$�J`���������W�zF��G�5(��+��ZEvD��71�����"<�b�v�243V9�R�_�w�5�Vh��|���w�+]8r�T �J�Yh0�
,dm�8�\�� B�����9��4�ÛȞ�����x3��r���Fe�%��"�&��'$+��G"�4�w1u����%�8�^�JY�$xT�X�`ه'�!'e��N�I0o�G�C�b�!g�NH�`�Lr$��9�I�u6x#tS`�C'tH���:�����a�e+(� ���m[�PJ@���T�7Yp^a1�&�*#��QU���� �cU]SM��"����ev�"�;.^/l<����es��aJ��V^��%��X4�3C��\R�솬vס:��?\�Aa!-�?��{	$�"�$_���`�5�_��w��Ψ+���G�E���6G�
[G���C9r[!9�+��ț�"u@�98T�:8T�l1�v�J��ؗ���ȥQw2��wv����/u���R����N�5#}�k�G��E�Sl �*6Ph�6
��$
̣����)8 ���@״��x�!	st(P$VF�
�ѡ\���.��0�+�
{���n�����p��!
���8�"��Ox��b�k8������p������r�L�@�j�*��,����1����E�[����f�c�(�9�`�Qg�&�R�G����f�-������	��F>������^sP��0��������FA���iAҎ0 ��C	�(s���:C�!�X�vZEm$=�x����
�Ev,zK��e�a�ȷˍ���.a�Ϛ`<�3Ik�ig`o�Y#��T@�HE���%�yؗ�dQk��7A	qN���/w3�
Ut9}j�w�\�v��ܘ�ɐ�"�y�!�#�܅ڡd`�vr��H�E�11(g�BA-�x0�t�5�,
a����z��ёu6e��5�QP8�Z]s�N�)�'$��b&21�F��@Ȓ�P�H�x�gU4Bg� ��A�����+��coc0|
�:w�5��ORe��;ܴ��ʓ9����s�K��}{��X�?�	����k��ч
�{���	K���W��"�g�q^߽h�?��qIOe�딧�5�> G�!�0�����=#�� ����$�Ӊ��yndu�p�:o_?W��y��z zF�+6�l¾����m��x��{d\�Ls9���llw�e��9�D��f��ԏ����wO������"r(���i�
��P����ODN�5R�����5�u��]�|�2V�Q~��I]�@_7�>϶l�&��N#��4"X89�N�%�0�]i��ߴ��4r�}-$7P�8�j�!]	����X:&+��TDX��z7�r��P�ҵn����h�้�Uq�{�oY��s�+����>�Ej(�_���ύ�خ#��
=,+����f�1ɼd� ���h'07��J������r���,�}UQ��{�bF|*���b1s��u�tD*N޽K*Nў���9�X�pr*��K*f|�R�-��iٜ�����♥�S�+Iآ��o��k���J)�GN�Ċ�"ݞ�E�b	�1)��:/]��Q�/�3S�+#�z)ۊ�n-�"z�UJ�%��:���W;��ATO���ٸSU�FB���6ڵ��;/�}����N��b�f���_��L���F:CzP=���Յ􍰯��X~ByAFޡ�@<�1���B�8���X8���8y��B��Q^���6��T^�s��^�Yqy�a��&��#��|�y����E��S��g�'S���r[��2�0|�P�[���M�6�6),�s�A��=��5K�s`�a?ʞ3�MH��]�qnqh׭��n���2���I{�w�A�)��8W?(;N:y���l�-�y�E��o�e�9�x�KK���!${��ƚ(4��/��ˢ~�����Q
�q��p/m) ���񍪓���:�7�0��2�;^-]�]��-��-�7ʬ���1��9p.���T_�|�H��x���>�GI�����{�P{�1�`}�o������B����"b݂�kwY��)2}E�[4z���،�M|9YH��^)�E"�������
8b��J���f��'=N������������(~2�����Fɥ�~H��o>��\�BK%#���=������'�X�q|�SO��6���(6*gr�vs���O]�u�<�Y@�h�0��P��P�Z�шDA��V�������uYȮH���

����4�����d��Ȁ�W(T�Y`9˂a�)���)�����*��r�v6���-����n_���߉��V��&�i�Q"���7��G-��шg}�u��=�	��zt���9�SO$��B���� �Udҹ��Y���!�ɂ�=��� K@j�x���l�a@�SO$B#R��DX��Y'z";l�d���*������]A�����+�={"17ē{"%�s����ߺ�}�Ӈ`�}�qh �=��J��Q�;B���qsk��eR�ɠTfq�����-ɤJwW��t8{s�Q�����ҮM�i?V��I�7z�?z
��g�aV����N����F��;�fl���<^��̇��|�K�-�^���Yl�91޴�	��`ku~X��m��<�gH�Gw�(�[7f�a��]/�B���Tq�W�ї�� `jD{�D�UM�'�0��A�h�ۣ�����8|�H�^���&~7�&���*�e��un��h!��LF�$��^����|��K��.p��4�m��[���z�v�ֆ#� ��XX۸Z�dn��q����=l��nX�o�B1r/�\�!��4����wd&��8��r-bD��>&�-�j{����X�θ����X�"��ժ��G����(a�u�ܪ��l�']�Cz29�I�oX�&�aP&�uX�4zAC�n����Ҿ]��4�4��ݤfo�Q���5�[�a�Pq�Av��X�MQ
2駪����$2���1��i�l��f,M`Z��>�'h,��fޫ.{�~@7�'7K�lu�c�C��ᨭ��Q��������L���2��
endstream
endobj
53 0 obj
<</Filter /FlateDecode
/Length 2991>> stream
x��\Y��~���s���>� ����I��d7z����*^EI��4y�t�{�2Y��b%�t��I�慄�F�Q��/_/�]�se���q�����a�7��,��C�&�	���.~�����z��?��G=I����(����~���Lqz���r�~�A*;)=���Qm�4��������O@PaI0K�'��-����l�+�$���ۊ[ig%�g�K��B�R�����R/	WF\ST9pp�q5�ܞAm��^���_�VFŕY9���3��v����$���{���*�N�zF��t�&rF�Lt�(V��e��=��aޚ<���z1}�o �f��7�a ���j�N-3M��(T'����� �t����682FX7�d�ɰܕ҅���>sy*$�hp��<�iAM�,�B�4W0Y�V��2Ң��
�_.�\\��������F��E�i�:�;�.�Y9�
W5�f5�0s������b�(i��&�
̋H�"����F;�Xd�c�&Ei%�iV	�ǅ�G
xabl��2۬ Ѣ��U���01��f!��r�y�)�-��jb~��Ș{�h�B�]�QAىE0�"*]桲J�7��:����exc
0dVU��rfs[�9l�T'��ż�b�[�%|lu��C����5�����G:���O��_�W�\kf�s����Yp�WF��3�⣒��알jBb21�2Z�L��]�a��e��v�$��m���b����8p����Ĵ���}���1���Vz�Y ��e���Z�I�ZJp- �� D�k�sc;bq1���ŏ�
�2!ZEr�U�i4����֬?Pͬ#!�
4����O
-���X|�淘49-|\��{�D�qS�Ně��9�2V�[�~
&V�q�����A� #�ʢ��b�u�U*�p��-�
鸆�fc�p�3jh(�9/ie�
�LLps����n��0t��t� �(��K��Zu6(@�Ĥ�4��B�3�9��� �aLI�,	h�!mJi�`��:e��
񓸟WC���L@��ZJ��­PA��k6�Ą������f�s�7U�vG36cK��`.�j�����:J	�7]Oi�uߣB	���o&��Bb�����5_�!.�ĸ���z�*������*q��+�$�"܌$��,�k�7�^��[~s Ѿ��rFX��AH�E�.74L4�����k@�A��x�1��0m۱�>W��:l9b�q���\��5��RȆ�my���-?��Cw�$�w��aM@+][�,���r�K΃> �l��ҏ>O�z�h ���V�sL/|A�Ψ|F$&d��U|v�Ѱ
G�4���@�^~����-��z�_S�:]��HP'��K��d:��Z*�16��xE��f̐��i.t
�_�w��`@pxi��hՎ�4�@=+�g��mc��+�[��$;h�o0$�Է���3l�-��5�L��;>t�˜W�+�`���T(��1�)�9Ʊ9{�������n4̅>�d3x��}�U�'JȞY�����K�G�<�� &o@����u��=8@�]���;����px����
��B��if�/?X�$����yq�x���խ��`�+�m6���.(C�Wġb��'�炬�;���ؚ1ұ��!�0X�{���j�� ߋ�����^���+Q��^{�]�TsS�q移�����I*�}�_��:���l�*}�m�9UP�{Π
�Ԝ��q�!�&����tj-�%[�\�����*5C�u�
�^��}�`���١����,$�a���ڏ�>�j��o��5?�����`�]��)�+hob0z���=<�����I�k?K/����Vϥ�=G�f�=�?��<�}`e-����h�1KT�m7j�Ǜ�hWk.i#�wT��}��r�8�ދ^�]�5��{̄��J{\��GL̒�(�l��7<�[�I'72�n��U�Q���sU�y����7i�������2�A*����H!?�N|�8yu3��nnB9��jź�ۉ%ӭ:��B�V>8+/P3�Σ���f.�2ٌ�M�إ����U��-'6盎��IOb�
��s�O�x�L�A��[��9�oTR�ffi�`�(���ݢu����<�>�k5~�C�c���1���h	M��6�t�����<�b�n������F��^>GL;!�Y��`��0-i
���X�ρ^ߧ�[�+;�&�m#U�#/�x�I�[���։��#{7�+m�̋c�t�Ki�^�*I/o_���9����"�A�HsGcŐ=ay��<�z{��7��('��g��M�9�$3��f�[�=�E&�fq��71�DWT=X%�&����^�3�r�����;�Q�w&YMVǅ����y�n{�z]�*�Y�[K��4���pCwM��EX/��{_��٢��Z�Ɣ�����+;�/�^�>��?��y���f6����rӃ.�_��f�=��[���BJ�<y��=�t.r��K��$q@*n!cH��s�agL�w98[����:�#�r]���K�8�/�+�AM�!M>��cno��C>Ob3ǜhk)�Qrv��1��T���un-�_��Ѡ᷀�*��d��$o��֐-��r�����|ϧ�,�m��on�[O]-�{�:����\ڴ�#PO9���t�m�#�>~?��27��H��vMN=�ģGy�zؖ�����jx6u̓*�y��s�P:��rȞ����ٞ��S��i;�Ƶ�t0���7����'W�9	0�yjw5��5��؊�s]���Ը����#c�u�� Py�����h��w_3`�ۃ@w�h�C��{���%�9�D+�}.St.cV%爆�Q�'���A�^�V�Ɛ}�o�M��[)�:�\���H�W�!5�K��@�n<���_b��
endstream
endobj
55 0 obj
<</Filter /FlateDecode
/Length 5741>> stream
x��=َ$�m���l@���0���ֳ��cK�1#@��&#�`���bv/�=�u�2$�W0ٓ����)����|LNOY�n�����7.���*����/��/���M:��qư����ǟo������lo���/f{��D��Q���<�˷�?��[�}�+ *ꛍSL�����o?_�U)�����_|��n 0ipk@,��V@�qh] ��<$w�����m�p��dt��rד��$zM���5�ڮ��&�[W7���Ѱ�c��kr�����Xe(1���F�;��ǋ�a
���4J�x�X��ch��P�p��'2�!Z?C��OYW�r�A�_��&�M�p�Y?������� S�($�묮0�
,de�s���w�tԡ�Ky����9��T�~C7�6�#���]�C�q�\�V�����&�
)�`Teۓg1@}r15�}���Kȱ���&k�#$x�k�DX�!���!��Snd"�[�C�AX1�v�yk׎�a:�D�� �r�y#���Y�˳��
"���<�-���<B@
7���BE[	(���3� � �ᧀ�ɔ��@�,�*�E�#�X��*���._[�uEH}gX����(c��/DA��D�:Z�r� ���ԡÝ#���a]H�v�,���s�C̶-"���/���!����Wh?����)|:�O��r
9�3Լ�b6u/���K���D�D�Y� L9�� u FG�D��D������K��KXHy�%
t�%fX����%꧅��0��%U�19U�F&5��5��6��&b{M��H���9���V�V��\��%p��^ k/��P�6��_z�`3Ja�&�a�)�ۺ	���Dp
�/�� ���K �!�E,��%�S�󇥗h�SEjh���rVJ�
7~��ΉM4Q�i��F6dNͱ�5ۺ���O��N��)|:�߇S��N�����n�b����C��ع��k��Ð2�\r�����~.�x\���(¸�V����[W� c������}��j���z�_��sIh��<����r��Ai`Ќ9L#7�������q>G=ꉾ�&0Y����ý�/����"s$fr^V�N����ɛHr�1<!]�K�\{�@��2j�����I3�V�u�@ �����ɉ�7H�D�cz�I}YV��C �5;�Z#O�tѬU v:`�ح�`.옪�6��mM��2��F���d�krMF���Q�/b�sQ^����~;��y�ͫ�>��~GT�+
'���7�0��l�c+Yn���,��_n�X^��jwG���k&p��V˭P��r��,��a�]���KPFL�]�	�:�R������,��>2��,�<Y�V*sFFYwjf��cD<��#�E�����QqaW����R��b�ڿȕ*�zz@$,��^�8OB����1�煻��4���������:m�<���尬���)�J}�S/��Avr���6��Y�Ӟ�J�A��L�O�ĆW�7D">SQE�� �L�74�@�I�'�4*���M�ع9uL��T�F����]�Ex����rZ�.�V����'�D�,�O�U��x��C:��^�73�|�4a]���q��?0�9R{!d�YT���&�%�%��/�l��28��w���B0��<�k�_��7Nɜ��nB.�����;��^��+k~`�'<�y-�܆��}J9�V5�<]Cd`l4=�zp���F���q���l�њ����&;s�� 4y�QY��X�r�d)�l��Ppu���א��wh�����,�y9L,w=�<�������	�Á�r���Ȍ�
���d��V�\���#�Q��BX��h[��r
>�f���p�3�K�tl�e�M�B)X����9>4�M��3�H�G�u�3��hYj9P�c����6��|�Ǻu6y���8]�|���3{X���ٷ���£"ȃ$֚V7e�,�u�����b���U'�J��BM��'\������}7��9��?mCg �9wΕR�9�QO9�#��������=!���!�~l����q�|
ȉ�P�n���P� �|R�/ࡍU�ZixC;K�M^�n��qc���7lW�����λ$���s�'�8���~��sf�d�qo�-��}���Nf2Y�p�)���s?	0:;E�o  P4�h8���	aj��~�0in���Z��;Ɩ|4@Ӥ���	��"��"K(��|ƻ�Mw3�3���B�3�KS��X��Z(�*�aׄT i�>	GV/#+���&��6� P�@	xqv�R�^~�x�sV`�8l�o�W�/�lb�@\�&�1z�|�2V��3��>V{�)�O�Jd��"��|�J4���f%� ����|?��!���N�k���a��xТ`�b��~@���1(�D�+�
���y��Y�*rU�
CU�f�I�1�DF��M�3�L��(��$�-"o��Va�I���.�/c,,��r���m�����j &0�c%��!�}���Ph�\��M�:5]X�t���M�d��D�����h�����4U:�	���0�>/x�ϫ[zs��ᵪ�p��b>��Lx�kwG~u·j���m�t	i/_�Χ�����,z����o�P�h}�p�s�'Iw�B�Ҥ�Z��ʓՠ�99����\K�}��m�(�/���ڡ����EO$T�@P�N�4�c�g�o���j����]c��z9�bqj6�O�4�1��Xe�Zb�r����k��O��W��ʅ1s�#��ˑ8��?/�8�C����̚����"�V$#JG��V�F����`*[Q�m��.g2R2(�0����Uk�S���=��Բ^�eʲ����~Km�d�F^$�f~��(ɘ�D��s7Me}Wӌ�:4�)$C!��P�&1�@��bi-������e�I�14m�<�̲�WŦ�����ij[�*Û��E�Kt�h2e��ίӌ���I��xC��E��)� 8�!ٓ=l�:t�Y$�X~��#����yMb��:����F���[a��k�=��S�xH�dD�M)a�1b����=>�jc��Q���=A-�q֖�#��r2vC�|���GR�٫kd
�D�`�Ϳ�֐)��;S=��L,5�5���t��K�]��WU������t�Z�"�(#�e��[]�8���.�U��u��۝K�,ت�����wY��Y_fz�{�^���B	c	K=65S<"k�/%Io�j�t����]��
�\��'��I�)/��L���V�Y��k~�=M�ǀ.��"�M^X�Y��]�	�����<A��B ]B�5f!�����E�; <����Jas��Mڦ�ɀ��p�|A�ۼ�n;33A��4��)���NT۾�>x�y=�VH�Qo�����*Ԇ��VA�"^�?@;�v[8���{ݣ�3yplsܽaj*�7�<v$�(?/Y]� /d������W�j��7���12���Mm��u_Ӝ&m�����(vr���`���E%8�ru�//�L��BoiԴ�6��FMH���V�� T��ِVM�B�B�̀ ��Bٰh�h�����jl&j�!vm��@ڳف�r�1Z%)5����=Z/w�,ڸ��c	��Ø`�1li)��-��,:7
��E�f��X޺�Qa������c�X�1�X,J�X�A�X����l[7���C[7a��H] �dRё��03�X��uLa��͛�C���YҼ	�����+��nV��l�z$��[%D��JBno�$l�.��?m�쒢�� ܐ���M9"����0X?���N9@��$�I�f��wY�O��MkW]�dT9A��fAF_EB0Ջ��VW��M�.�b�<���ߵ	�݅'���}qek�Ǚp?�-�O5^)A.4,��*A�m/�ܜ
mR�W�IL~۟~��,rpe��Z�֨���HmDN�bXs"��1��Y��Z��� 	ڽ^��z��*�8��^�'�7���I�)��[����P��F�,ɘ�,Ec�Aa��}�%G�7�O��f���p�b�.㣃�ps��_�����>��w�%���Q ��هX3)�����`�Y��S3�VyƟ��G�`��/�=@�ne5�}D����M��Ƕ��ʿ^��KܸP�F:�Ͼ~�����a���uDh���m& I��ę��!cg��(��tJ��87���=�:i�2Qت�F�D�(�M�!c��=�����%�ڬzk�LJo|=�~G�J�_z�ש��w�y�r��	�4��sv�~ک;5o)?��6r���w�ԚX���*����d�Z�BI�vKە�<�{��Y߯�1��9Q��L��Ok.���[< Y��]�*���ֿ]k?���}P4d(r��4�c��KҠ�ȦiP�E:�C�uiP����b�M�6�W$�N$b8�K���9��`��9I��iPGzE�D;�I$��$�q�S�K���,�dI$>Z�,E�r*���פmX���g��؞��m���b.%�p"y�3y���-�GH�W&o�ѽ�9>cG�`��g�N�."������*���D���pa -.�\��H,u�<�.u;��������i/vQ�$7�D
<�5��^R`���D[߲�A���/��m�y6���ڤ���ɒ�*|I��i(�h��%�_�t-r��U�K�j�o����ݼ�H���{@T)/]����k��K�q���wAk������_ �����k����F ڬ�O4��%jY�M�Bݑ��7�m�5F"ଔE,������K;�͆}���V�=-��Ґ���BN�m�#�5�1���Yjy�Rː����^�����_�K-���|g�|oa��g�v���c��@�T[��bX������|�eTr4�b�J�/�̽�+���\���R�Qh|������޲�F��2[1gY
.�$%I1��v��dK.fm�R)����X�MR��q��9q��O�������D2���������I�!�N���__�����kDo`�#jD� 5���jD>�O�t;��Ո:R� YkD��QGzE�ȋ��xԈdU�Ԉ���	���)˨��P#��mՌ���D�v?o�}X�(��jf�W�v`S�vĐ.X;�]5�'u�5�_Z��7�1&���-�L��z����ri��wl���w,�KʼK����B���Ҡe���K��g�/pC%��坠��ܱԉk�v�?%���R��6���D�.x�]O{L�i� ��
cr��[������ F�c�����}
����@*#炇$Ž�1�^P�Xk�T�CX�G��3q��ǘ�₇����������;o���w.���ް���R���K�r��1�p��B�k�6��'�)���l�FG�@zmφ��5�p1z���&���=���7��Ӿ!�O�}�'4�7$)�����7�#Ծ!��}�"7_r���%~�\m5�L�F^z2��n�@^�������Mܚs<`K��_�ܘɶ_��U�_�^=�*M�h�̔��^[��-Bv� �٥_�z1o��;�u>$B�QHEC��4$"�Q�He�;�,�-��R��oK
�~���T�ˑ� 奲�\��
�k5��뛥Z__����GI�^-�X���/�}V�NT��W?�?¯
endstream
endobj
57 0 obj
<</Filter /FlateDecode
/Length 4001>> stream
x��][��~ׯ����~��ڛ�6��M�b ��z���DY��k��5����3Y���ga�燕\:�WϽw��/�?��P�-R3�����?����Z��[m졽��|�?��y�������r���?��¹�ݯaxk� �~x9������

�"�jzry�r�+cR�my�����/�Z �T� �H ����б�/���~z9N��z�YB9�� ����o���v��#T8�8p�q�ڜnJ�������g���LPb6��[���q�ܬ��Q�B��
���>���-���H�,�ƭ����
0x�y���[��� �!؊��/�Bp���B�s�|��T�'L���D��)�|�֎[nbj�R�ރ�$H�~.���#���IM%�Qx���0�0��'��'h,�*�m�S�(�W�e�>�|0ޖ�W�Z��ތ��Lz�%b^c���w�0	.d"�%�v��ZC�6ޯ��\� ƝpD�I�o䍨�F���y���D,�8���=��),�[�L�6���:u�(5ң�b�L9G���e�(Z��Q:o���d6���Q�T���an����j �vjH�[jr� j��Rbj�s�YD�u�(��U�Sw�ڡn��H|���?��è�?������
���
�UP�傜!���!+*Q��E	�0�D	Ĥ2-����(�*�R�(�P%룄�f%�bƹ.J �G���(?�(��(��S������Nd6��i|%��8U���$��I��wN�i�>i���k��o�"]�P%�G	 e%�E��m�D@�(��D�6Q"�]��X��*G�t�D�r;1��-19B 1�Li5��1u�y��""�:E��Ɉ̉;���J$>~I��
���
�IP����)V���ͷ&J ��(�n���P�E� uQ"`]����>J���,0�E��-�|��D�j�D�3L]6[o,;��x@b���v�TI>���'Ey�Q"i��E�%.A������6J �G	�6Q7��(��V���uQ�)���(�t�H�m�@�+a�J��m�ȷSK��R��P�̤#�Qc����B�Γ�IݬJ�:d�uܤF��%�����𽄅_����4!��腛b̵�;�N��c�s<6[AKL^��1���G�B���PZC���O�ȼ���x�
f�9�C��S[K���壨�ZϘ=O�������.}��r��@���V�;��zȥ�qZ��$k^�;ąl�xr������ �<�$�
��G���s+'��HbBIOZ\��=��z�����')�N[����cO;���V��a���ۿ޳㝎vY���7�(��E�/�J�=Co���w������ Y>��B ��Ý�S�����<�1���t��� P�wx"!_��L�����qh 
!	�r�Qa؄`V��jQS�97R����g�v�_g��C�s�|�)ŀ����(%�&�G�4�YAu6�L# �V�q��� s�<���ln$̡`�3f� �F�*�� �,�����PI�*|2L�SCRU)!��0�YN�hL71�� f1�� ĸdLs�e8��z��K������ uJ�;!���R9L=$� �
�~��� �pLm�%y��U2%��%��T�1U�	�V�}k�TВ(�B�����
�/M�J�-쇶	2z=Ԇ @b���:e Q�NB����3{Lt� ����2w ��(7�%��eEZ��Li�,{:N�RKSQ(���Gᴵ�lJ��ˬ��N�U\r�H�g�^�Ai��0ŶR��A]r��1om���b����)�D�*�J�
��qF�D�6�~,3;����<��<^�4ǘ��3�U*?WאL�%�(ND<
_���~/V;�@WS/�[�f��9Cr���K��g�V$L:�b4ݦ��Yո]�'ۗ��z�!)�fкX�J�ܮ����>�4���B3��Ґ���\K��襽l���I��pуix

vWF�=5�i�['��6�3L�#�03�����P��79O�
��(�g7���J��y28c&2-w����S�V�m�W�g����U^�6TI�2����!����喧�oe��o��SfĔN�:]?�mԫJi�N��6+~��ѾGD��"�!Qz�MN��v/����=cRnu���F�cjr��ܳ�+�י��`���\3_���!8�a�TW��?՝�du��e�R�E�j9�K�B�fO�,�RTai��a��V���#C]ρcM��Ϡչ���{�z�Іg�+�'��3>=xfI�z?�3|\1�r�7Vu��/������u!?�pe��P>m���|-�F�^v����
�;E�S��]C��Z��Z���q~����D��k��2~��m����g-�Ӥ�u27����gI�}x�S�9���ǔ��Lܧ���>���8͐(��E��v����ǹjiA��i�%�s�߈?����5"�!��J}Ā�$�tK�9c֐`g�1�������K�*�15y�n����K����em�G��36���3�S�Ȏ���w*d4u�3�g-/%$��urC��U�b��n���u=�QѼ��>�SV�)��[]���.�J�JI�J5�BUn�x
Ÿj�.e\��]LYY�u�g�,->M�[Ȅ�%[�׬���J�M�cqq�!~xmy���E��{���חT4C�T_sd��ח���:έ+�)�5ߐ�ͷxN9b�w]XR1��=�,�`aY�>�&�3���^1�9�����,	��,O�^��7ZM�gf�C�B)73�̙]K�̇5��L�.&�Y�����-����(!�O�J��H#���<R+��,53��N2�nOAˏ�bᙤ.k�$KmD3$J�=���]�Aio���ʦ7�R�\��#��"k��8��j#�!����%��הHJk�4e�ήm�$@z�V-����[�kj�\�h�I@��Vs�z�X�F��je[���m��0׶�j��?-L����L3-vL�5�]��,��aX�H�$`
fZg	-���*�hj$a8oH�$`_:@+$�H&��G֖�6��@�X	-�޵PM�bw[k�VGb��T�Y��
A �Wϱ$���YfW���������ƷB�=�0�����|��Z:R�!Z#Y@Z%Y�z�:F-M���*�Jv-w��՚�(Z&��E+%�Ţk�R�	]1�5q�h�8۔I
�¼ U����+Z$���H���H��.��u�Z�Jɩ%��pj!���ռU���eJ:����l�čq�>&��O�O^̒q�&^n��૖V.�&�e5�j���N��`��9:�Q�ha�tR�#
=[�^K׀Mw#R����׵[ԂȘ����X��J�]���8ޟ�K�e���8#�(�ӌ��3�������{�҈��8�����j�l�u��;c��s����$�!��1ƫeo��跍du�A�������9��D�B:�^ux���k��i�A�d"�vCaFt��2����C�$v�,P��� y8�c+T*�vG)�K�ԳX(ڏ��M�C���m��O`d��4���&�.��`*����!M
\U����M%�A�,�p6+[�Z̎�\�����)p�I�h[6:������7�:��A]���"�#{���ɹh���K�E�*�$�͵x��o�;u�pe	��O`����(g�����٘�6��-��y��{N�k�,��/�@*�!e��$�JM�g$��b�(cܚ�L���M��8�R�o�������j+���_�{�X��M���]~���b~j�-k���LF���qhy�������~B�m�~2����S�2W}����������Ւg��&�²j�z8�����J�9uf�����(e��٠���g�d�����/��pG�a�m�|#o��O��U�e�_G�m�_ǩ���,���*
endstream
endobj
59 0 obj
<</Filter /FlateDecode
/Length 4582>> stream
x��]ێ�}߯�� n�~� �J��$�J� X���@�H��ޞ����{�ؚ9�$���!���˟E�?߭�krz�:�|�|���n\R��*/����Z~ܭ:����0~��z����R?�����?������b����`w?D��\�����n��ǟ��"�^l\c��/�.?��Y)���|��]��?�s��p3;`U�~Z�v��&��v���ӂ{�W�S��8b�A�,���Y{mg`�=AM�K77�/�i���Z�Y�Y~uY��fc�w����ϯwZ�5��h����,��Z�b���h�]�1��B��k �S�-���+�_h���V�����`<��	�
�Q�/�Y�0�b!+ӯSN/��u�Q�ڟZ�5xeΐ1r�.p���X� ����Bm�3�qx<԰�30�5)7,�'hl@��#]�q�'a����]ȱ{�o����ň�l]"�}q<䴚`P�.&b���b1���!��];a�t2IX!�r�do�[cg�7�3�\�.t���k+r�㝼��"�E(�Y� �e�[WMR��`�E*��/��Ő���F�l�H["�VG̪X������n�^,XF��
ll��x'#�.��D�ʘcdt��"�I#쬻�
2�L2�L3��LH�L��F�����"-�X�s))�-�)oe�,���?XY���6��=8�^'RS�H٣�:����� ��2��3Y&r�mi9���X'R��(u��N R���s�(X��#Չ�m��u9Dl|�U�0�	RgȖ���W�B2���<�2��f����^@�^'���:��T'
4Չ��u�i��:Q��NlS' ղF���FDkDA]1P�`�|��s���P!&"�w)bM.�����[4.��T��(rKXZ$a��HVr���[�o������u)��i��SmpF�6 ���D���D�6�	�!F"�ńE0���D���`i�ä��f9QЩ6Tl1�g���P6�_�r��>��M�!�:C���C*5�ȌkV�����IL���N�j�>�ڀ�k sm@h��mj��vS�kb���j|��Ķ�ѹ6 F��~n��~kC�dQ�2�xp�$�^�D8�+2�#�(S�--��|"���Nd�Mӄ�R�V
�J��|�4!�H�6x����U����,! ��@��`�@���MK��m��kC�jm��6�ocm���?�RFj|�U̱6�:2CXo�Kd!�rdG��lq���52�ɃT��\��cm d�͵�MmH�ljb��AsĶ�!�
Bv��ڀض6 :׆��X���P��Ձ.�QD��xcdd��"�Q嬳H2��2��/��LD�L��>��7M���[9x+��r����&�_�@��d���~�,��7���x�+h^Ě^�J���4�&(L��)(h�`
�����&��
�Kpu �xQ<�� �u�`qM
��n��p�:
}���uC�B,e�� �I;20�l��4L=jh�p���#Z-Tzh(��q�0[UBʑF���f-������5�]��re���O�J�|�5ُ0�!Y�۲Ox����}�rsT�~ۘ¨�h3
ϒյ�j���R�m#�ר��>��s���lp�@��ЬD����w�ޝ��� #�����ָ�gR�X�>d�Pі�M��Kr5M��JFRnlm",>�4�H&Bq75ФX&Bك֣&f�؏
74
�Jf|���!�
D[,9}��=���iRa�4 S]y���'ʕMW�r�ct�@-,e���A�n]ц� �����⊈�jm����3`+�A�������T9��xHXy��!��j���{����7X����8� �<�� �������˂n��vt]�xxӆs0d��Sꀦ{�D52�۳IΛ���wY��.p#OU����U������|��AA4�z|��Gw9ho�;���3.�N��pޟ�6V�U0[�04P�bA���¥E�~��nط��>��B�"���EqpxVW���Zn<P`r=C<|�d]��)[��1a�C���;5O73�{�^O�K�}����5g�$��j�v�~<3r��XQo�.S�0�%��E���{����kc�G�j!Laٮ=�Dȕ����r�i�3�T����K�a��p���M�����k
d{(�<-[�p���|Z�>�y*��kl�/Ɏ�>C��(��+���#���'r1f���c�:(�%6B�C�U.}vJy�i�3��|Ŭ�*n=wb���c�}�j���,'77;�x�x�c^��!�Z������`E
�o�@iܗ}FE�=��6�<E��=�b������^�OE<F5X��a���8�q6G��N�j����٘����Fh}%}h��sZiU��แiҦ3?��|���B<j��M�au�@;0z��P��������1L��X"oIR�����1`vN�o�ع���¤��T#fk�6�>Z'�M��^�\��A�E��$�I�H2�0I��$��t�����.2�g������1��㈁�g/�7 3xo �4�#�J��]p�5�X�Q�o ���LFh���$����E��Av%��.�m�e˼rsb�2���mAE��e� eC�"'+<�c��[V���QtF(�"SF�L[�$�F�:C%��\� Dg����ju-w��12�d�
��l��\� Q�ʳ$�qM1e=�k ��*�(�5��Sk2D���uPm�9�_��5��}*�A�5�DΗ�mgi�l��rm~p�y:�C�y�A��($�J���L��/kb��6E#�A,���Be��g��&A�5�lӨ��y�*�ƹ�C��=����{��g��A �&��ά$S�u�Ÿsy�W�� �$q�)�nP`׹m� �Q�}�`�ӟ�F8��0pץ��qK\�B8s�R�r�CQҴ�;5�dx����-V��(��`�ʞŨ��ֿb�)��Y4���>�	��3�5;�?j����؝�����-qj2GE+�ۍ�<�z �@��:Y,Fz�,�Tz��ǳx��E��,C��
�,�\@��&g0�!�9�Z!�Gz�Tz:�o	A��!��-x�zX�5�<I�>g50��^�D��Bh����'z��`8O~�V�>a���Y�HJ��?ֵ�$��&�D����GXp�h�_6��4�ӎd��o�w���C�LhG"���A�v��]�z��e�wm�8�=j�!�
� �~�ػ�{�G08���z��/�����[�[O�x9&�j���}���x�nĥԊ����Hȧ����W�5���X�������jo�g�Viw�to�l/.{GPY��a6l\�Bv�#|7�v6�� �ҭ���ھL��p�q���k7�ty��qb�N㻅<>�!����	(7l�
�h���`q��v��v��v{_�o�M&�j]^��FjP�^n�u3=�`9p�Ħ�	�h��B��7Þ���[v�ՇĮ]��}�ʝ;n͖�Q�GR�&K�Ng����֝	��ܻ�R��Q��;��=N*yG(�tV�����w�`l2>��{L�纗�{Q���<n��`<o�Iaxw���m����5#��n-��`9[�`���0<�o�����z�_l�V��w��$w�DK2��{i��S-ピ���W;#��D�%���IZ�F�rZ)��$dqpqmS[S�Ah:�J���Z����j���r�!%!XWhBҫ�3X�Қ]4;DL�z���k���s�?������)���Z����^uR��g)�s��G�<1������f+�߇�߯q���/�tP���.]oa�w�.�f�k��Q����cgy[�[(�,η^���A{�F��}�(�,��E��R�m{��(~I̪�7�_:�r?�[��#&H�Pm�u�7n%�7�\�'z�2�ؖ�Z̰K��~c�ߘ�W�l*�\�v�����HJ�T|,�3,i*%�D��7�]���[�]H���� IyuP�^�QCMBAI�؂���X~���\�#�V�r�``ot2��y$6�iն��iW�X�wBf��Hz&9/n���1�QR�(�͞g�6Q�e����u�Lb�P�~�`�$���r�Υ$|iK��K��{��%�e�-��-&x�n1�QKf��旤 �D���X�jLm%~�H��$�ec�[sJ���^_Ѥ��̠�4�]�z0G�l����$�eE�usY�gݪ�5_ҽ4���)���c���]�w��,��f�/������)X!淹�Pi�!ꑣ
���lzh�샾e�՜���fׇ儾e=���0�y�{�:S�O��w�K6^c5_�� ��#�vErr��Ж��q|N�6�Ya�3;�U���h���Q��/�F^�2��#~���^��\�(�o�r��e��M�x��oT�	0>��:ƅ����|�ݣ�37L�'^&rJHn^:���Q^?2ő[!�o��,����R��4�"��?.G��ٰ���|�-���X�z�
endstream
endobj
61 0 obj
<</Filter /FlateDecode
/Length 5203>> stream
x��َ$��}���lY���s����A�k���!uRU�iU�f6�g���f�ě"%{S:�?�l�m0r�2�p������\� .ڊx�������M:x���w0P^��_~������Ï����|>ꋔJ�t?%��G�x���>�K�|�	&Jʋ��Rًҗ���(���|�׃��?�� � ����E~)@7��Cb�<����	��nJO(�~�D��=��'��K�0Op�� /\h<������B����/'FE�9�]�g��냔ns��\$JZY�X�w0G�Z��!���{�=u�vX{���=LC��@�C�͢'iy�V�X._�A�	� x8m���A.
�F_��� �ty:�y����Y
�8Q|\)]a�K�Е�9|�k��.� H��̅��զM��>	��@�������/.���+�۴��?�g��dJ�E�o�c�)lʩh��0��aa�y��]���4DB�A"Gi]$�P��U]5	4D��:΃���>��R��Y�L�#,Z[�*��P
��,`��#̻P�Ve�.Gx�G��u�t�P��5�`���X�ۛ��:��Ԋ���:�2+�Ā�j�g�U8�k��uiSG�z�[�G����?10�K��A}�B	h	b�k8x���w�z"O(�F��j�フʍ� �Lg�*	&�@�А �@?�K0��� 0��	��	v�	����CyY�Cy7ć#6ئ$�J��nd�o�/�lwj��^פHܓț8r�������[|H��Bv�!���S�E��� @4mȪ80�0�4&����·A��!"A�&h�Ȱ"һ"ʛ!D�ǩ!�i��u�qVR�W���wމST!Q�)��N�eNݱj��mQ"��3I�kPx
�A�w�O"�N-Jh�wQB[w��ƌ Lh�����k$b�0��%�5[2[���Q��(�`9J�5J�wc�Ȱ�˔��6�i2(����ܪH�:_��4	<��DV��DUa֓0���@�aA�0��C�������aa޹]�@�>LDaa�0��}�H�&�]��&��Ԓ���:�:+�Ĉ+G��;��-����YR/�2��X�C��(�8����5*�F�ר�;�
�=��� �T�@��n��o��H��WAA�+��QȐ�0k�7 4�T���S���]`����ó�RZ@���B ��� L
 3�|���P�@����� D]K� 0nJ�8��� Q�Q��c��{�� Tź*���� �ͨ!����:Rz �29�t�9�4��£ÜU��&��I�Uf�*���c�:��0JM�m��A��h?h�hYJ��0�$�e��{��ϞI@0���"�f
( "�u� Ti�yGP���E j�oRܒ�tV��(�eP�RW�ҍV�\,���"�����+K�E��یB�hR�p��Gd����I��
��Ck=V�:-H,�<��Za*9�t�ғ�G@�&�
M	�C_Z-M�ddUA��5��4K�&�Ҙ;XO����\Xo �c����r�����)�FK�if8����x�<H� ?���=��z��u�pD4B����T��X���Gg��¿��n�3�2��3�͠@a1߭��T`��S�������F�T����p�� X��M0�DscXVd)]�I���ge�x�m��X��Qx	#�I�k�T��[,��Ԏ5aN裌��ٰ|_��d �k-�M~�2�h�,��-3��2	AK-3؝eZ��[f�"?L� VhT���iW��=��%,�B�o'j9d<��?�.��q��7��2�:CQ���L9�
��=���n)$'�I��Fs<�}&݈��^C|��P_C,e��M ��|���O2ǐ�C����8������Q� ԩ��r��pE
fVĠ��F�?�*E�����|�*`#�a��'��"&�NB�n,�J�A6q����c���JDǮ�|���$a0�� q�H+Vz!���'��D�C��Ѻ2�vP�p�w��#d�Xxyqf�b,�xN�V�!!F����GJ�1�ׇh���a��4c�z]0��	����Q?Z;�<����0�x��ӓ(~���Lsj��~�(;+Vr���0���x��)b���������=Y�1aVu��Er��,$g��'>ح�����
�߭PzC���n���&��*�m%��1*���ނ��^��&���CoJk�b���a���Tey�݃���D}�0�XT���e}���E�,[,�sS���Q<��yXi��yQQ�f��aq� ��,��#C����4j��t5)g!����"@��Ө����pXqqw0F�Y��5����,�l2�qy�=:��5A^��p�ذ���3 ��9� ;U��~����/;���Jp�$�c�n��A<�"�GcB �y�!�EM�(	�r����n�r��6LEFp�����W,�����$�����Yi�R>|�8�ǩx�3��A%��	�W����N}�NY�3�>���a���2�L:A՞R�̒I%N�^ɐ�<�:>��R�^�y�:�r�Os�=��&�su
G�Ѹ��h<�!�V�\�F�Uol�~��P8�U�#�r6��r�������˧�8ˑ[�J8�9��-h�E=l'�I���f����*���9��x>X�x��;�Ö�4va��rwL*���XK\����A����X;��"ѥ�Ć\8����2�ŉ��q#/͖c��u�[!��x�U�����߭a���v��/uWө�@�*n3�O/�������<Φ��yX�|��*���i����*W"�ڞYL$G�6�Z����h~:6���dN�6�xF�l�w�u[	��I����*���oE�p�Dl,؜��({��J�{��`c�${�-��^,�
dL��x�qA9����z�U�;�͇G�wl�Xw�Ŗ��!�j���)���&[y�*z;���l g\W�	{�ĦBt�vb_�G=�Uz}-xr�r~{�����r�-�����#���z�Q��+7'�v��7ӟt>K�Y����ӌ/\���Ým��/�����KlO�.<q��oX��f���ө�؝ߗ�G�> �cۂJ�	���#�����<��������5��(a��8��3����!����<�e�n���p5����N����;��u�ϭ���4Ҫ&�(n ,,�<������~ۋ5�ugd�w&�
:ND�;r�;v�ץ��9�is;7l�]�����/|�z��K���:���i������>�>ř"��\��b��m4�/5�̬��;�]xlfςOԫꪥ0����o�,�>2�OeOw����g?�a�qv��|�¦Uws�ebO����J៶��f#��,\�_y�_�x�۾���W�o�
M_l�c�;�x~�^y���:8�{�\���ܑ���[��6-���j�trx>����:�ceas��nd���<�?9�dq�,z�!���*��=9�փ�褨_E��g�����z��%Rg��n|m���H�ܑD�g8�[LW��/E��C���C�D�Q�~����uJ��	�['m��{��
#,i\'�k�,�nlo�0�it}� �7�YJҷ����_+ ڲ��hǺ�-���;�@Ho$�i��s���k�&��#���cX 7Ѵ]�^���vu ��J�	�	<�glr(��_]҆u}t��5E��:�w�w�Xαc�Ũ:PZ�K�A
��R
ڳNZ�*�=� �l�5�YP�l��ڪ�rh���v�k@ڱ�nM�(��n��������s��֜���6�kr�� ��L�T� b��ޕ�"�y��� a0�4�K�����/�vu	@�ՑQU�d�'JE�(!��He�h7g��M4׹ݨ�BDnK�h��Hc��bRX0��YRO�=p���U��nM�(��&Xϵ��I�s/��i]+�����Kj���p� ͋�f�Y[�(:��f��]��To=�%����8��_��n�CJ,���\�s�g�t��~��^4		7{]a��+��hDI?h�{�u�t��坼q�9s"u�K$n\���1	O�mc���޷٣4�vr���FiüF
�r?��w���;���А�H�1�;�����3\c�R2࿫�>n�[G���웈ͷ�\<cK���o���Z���L��0�%�,�k��]�	_y��4���:P����Z@A�bi^]j( ���V�q��F�Q�_�`i�`����F���U@�$�TR-aoU�Aj/B��ݤ�k�QXKL;Д����l��<c$� ��bZԢ�7�9l�EP!��0ZVX|����Rҕ�H�:���X������h%3�MhG�>�	(<s�Y�	�	�V} ���YM�>�eQ�
FUQ�2GUQ�r���ES��WW��^�u�{��Y녝j�r&I�J P ��H�0�=PZ���PTa�MP�,�R`���z6v'o@Z��U�I��@N�&!��Fep������R���OGIR�C>.z�[�{j�Z{[�����5%wN�c�e�5�^�7���G�2#k��ݖ���kԕ��]-��,M�zr��O��Ԣ7-a��wei��ra=D��Թ"Ϙ@sAU�@�fjk$��U�#�:E�N�Xt���0�=�GǑ��m��@[�A�^ĝq��-҉wSRf�n����p�I���sK6"�m�9!�!!���]�gS����ҷu�U�/ܿ�I��_j4�w�2!��c�֔vձjz�y�_�*�RUꈻP���~z\�ls�%M�!1y"���g���:&6�
����'�1�y�>���K��[��u�o����*f�֍�*�5���)Q-�5N��%3�uNb2�|�ґ>O�B���Iۮ��?�Y�ĳٲ��	[s��e�}�IY?+�+Q�Y��@��_!�����d��;_�6�۟=l��:qd�j�U,�W~���dR&��(�4�^t3����2�����۞�
נ���"��yQo=�\q-n��y�x?Q��
����p��?mNi
endstream
endobj
63 0 obj
<</Filter /FlateDecode
/Length 4672>> stream
x��][o�~ׯ��f8�(
Ē��6��&E!H�����:�=��J+�IeG�9��%�s�8.O��1�Y$�}'��`@D�1,����zG�+䢭��o������_7^�s�;������⷟��A/?�'��^ ���~J��K�������>�%.�~���h/| e��O_��,��Y>������� ��0k�'�7@��y 	����� ������P<�����֒o�X���\1TX*�ȸ�;>}7��-�Zܵ��ia�T\����׻���p��� iZY�X��w�F�Z-ȃ������.�z���*���8��o���}[�PR�l6j�|�o���#�1�!!I��.p�h(�6�0�j�I��tw .�g��ta�01_ƹR�bJE��CWn5x����h��@L	i�
�`.�Y�T��z%�KW:$*F~__~�sѷw��Nh�_L��RG�$a�:��]B9E71	������n��Q`��a"�
M�*AZF����F;��i\��lh�		�F�wU�?���A5,�Y�\i�
@X��4U$�Ȍ*_W�C��Q��Q����#B��.�|�N���~�>����nń��}t�������z9���,��. ��**s�:"��}�,,��x�]�(�:��X������?�%�G�P_'FAc!����+����+�x"k(�Gn�il�҄���@��5M$L�� &�4�(��0�H�� �K��M &�4��M$̅8�DBW4��D�e���n���17lM2�e�3�nb�h�a�҇͢���^�"R�o��2,�/$7�H�X��K$h�	[��q�	Z�D�6,ጔ�!�=�;� -�H	5I?�~	���U�(o�h�s��ro�p�,�2辰p�#f�PU�#�h��V�4�j��t,��doT�FoT����g�	it�l\�&٬&��8 �rr�GjcN��BZsa�����D���@�f9��59$,�C~Y�!��!c�k��Y{�ܫ�����px��q�h�b1W�ȃ�k��q���j��d��I�;�b��B:E��Ekv@А8=$�j�CO�wa�D-�zOs�'E�!�(,燌U~H�*?�7?�˙�f�+������!�y9r��5M�,���Y$6�����c�}&Wx�7>x�?>�xt?d��5.T�����x�����4WC��k�%�1��� �D�����P�F9@8�Hu�t�C=X�Aԝ!���br�&-���7����n�;~3�Tᑖw� �d�^4��tJaA����`��
T�=� e��t���u���M�	�L����0�#L,�ȘM��������m������t�v����m}����JI�&
2��ػ���8J�(J0�d�Hf�4�@�$���,y�OU�y�A�)8� �᥀�fUH����R"��X}���T� H�nV��1t��9�J.��Q�HʂdW�t@,�GY@�u�n-@U��]�3 ��t��t�s� ���&M��GBI4�G�h �>� ��3U	�eԪ��,M��Ϊ~�A3� J�)�{H��k�?�شE�E6'V_p�9%Zc}�����-�|��S��C�z6��Ӷ��K�������/l�uu��s �y�Da�Ga7�w���qj��p��-�<�{���{?�!���7N�0l�oEՠ��W��ܖ5g=�yJT�?J���P�Yd����!�C'������\�
�$!��\DT�~B,�ڄ��ߗ߾k�~�k<�r{	�őr{Ƒ�j��eR�Dq0�~�b��	ae�C���鼡g�,?ThڈN�b�R��q�R���<h�&ly��:8HO*!�GT�Y?���L�q��:�E�e7tq����o;fQZ�ܶh��]Y�Ă�1r�g<� �g�R��>�"MsG�:8�3�7�_�X�?��ԛ?j�]����:=�7�H��"�f�+fH{�S�@ݗ�����u�:���4	V������-$�B�����8��%sf��z������(�L�z{�_�F{/�h��v̗iE��}�uJ��&���܄2A�K�� Wy��ׯ�E�k��L�=_��C���_�aP�^�˜����$"I&_iO�ǆi�#qA	��c���Q��?W\����?)[� ���6G�u�����I��q]�=2X���IC����M�9.�t����z�%�����Pr�nȦK\���h�*�:F�V��`�^K)��ҫ�n��S��i�Ճ�=j��L.(̭L�����n2!I��P�.M�yZ�S"�V��:Uߗ3��R����%�(4Ri(�`��6:�\2��ԯ�Sbj��&�/*�g&�uy� ��h*�A��( �ǆ)B��H�
�$D�^pCL���N*��	$rj�����h�xq�b���:��A�^��r��&� z1�F��GcȢG�N�
 �Ҽ6�ơ1j��"���6�� ��#�ś"
6Gȫ���n��K7����K���Gx�w��Q�:]ܪ��*�X0�F(�[5A/<��"hE�2X^!EԠ	$�	��P:���
iy����
���V��i�K.{�s�Q��h���6��")�蘠+�"����f!��:ER-�eER��V$M�X$-/��;�X�V�(ͬLh�'up[�yN��@ֶ_!u��r1mc�¼5Y�����ڞ�}�wrou�)*�������N]�uV��:9�&��kR�e9빟�zA���$`��A�Z�UA�p���F�������4P����:0�R�q�j�]�k.󞭷�X�7�����ם�Vz�n΅"�SeaUO�\�Ik�u�>�4���,���@3]���+H:�4�V{�L��!��w�kyw�>8�8�L}�L;fE�_b��N|-cb���a�S&~B�#�N��p�f��f�ւ{�m1���o�*��Z{���~Y��)�<���۱��BϾ_s�e��䱔�� .�d�v1�T��ɬ�3n�Ó�ޫ����)�b��du�aY=A�k�강:��|�Y�����}$�!J1Wщu�mw�I��蹽e��;hߗ�Ɛ"�����+�Q�G��Rnl�^ș���͖!��N6@�W^9����z�A<g=�?� ���8�)��'���^!_'slԴ���n���� �]O�g��쩏�q*&�(b�rQ��e}��Fw���ޞ��ܻ��`"��l�9z��r�l{�cن2�q����SYt�*û]�}��&�	��dU��"�Xv��f]���@ϝ6���)m <�=����D��=�B��d˗� �;c�ݗ�a2�0����.���T5P�6:��g�hI�:X[�*�1�nt���Qo��	et�*��L� :x�.2�R��Ω}I�(D�J�E���T�Q��+c�5���J��:��4~�w�~��U55���P�[���b2�f�t4ѭu�3z���ƛ�{5��`s#��3h��F8�GF,㷂mcL�Wͽ)Yǎk�������9z6���
�:ڮC�ֻ��A��؋@/��|�y(��4ne���0�O��<�&���VاÍ��M��c>��kF��8� `B���t���s�m�$4��I���S��^����L�B��3�^�	7����ޭ�pX�-��'�}tq��?��[�I����ٰ��ƭmI>%�-1
$k�}e��|N��8şj�CS!L���i*�y����o`p�p4�I}c]M�s�SB�3�OI��9k:=L���u݌2�.�3�:<=�L3���^7	}�	p�U5?�Hl>�%�l�4�����DFw`��8f'�i:iMy�`��)sNn��s��E���3��Y�t~1�� ����okܯ���4o������c�x�o��0�,?�[��I��9U�&n�%;�*>B�b�����Z�� �u~8w���N#�����x f�TOg�ڶf68}�	���ղh��7�9��������J�#>R@����ʍ�r��px���Ns'	�������Χ�'�/��S��e=�N��E�y�Ʃ��[(�΂��^+ۙ����Y��|�;]yO��� �F�r"��z��X}#��d!n6��[�67hϣ�ޜ��4F��<�'��j�s_=��p��.D�Dp��qv��V�ώ�%���/����{�T��n��$����g�DL�v�!���fO����������'|�y���m_xQn�'{���:�k��/8�zja8ҫ}K�7���E�.�ψ�h���y5B;	�8/b�ze�S�V��;��g�g�$�m��m#c��:z0��z�/b 0�PLĴ �r�9^DQf���5�Zu��-?�� ~t7]Ͻ�n�{7]�����g��C����4TQ�'vP�$s���QI�$���Y���?�K����F���X���<�?��@~Z���O��>��X.L?E���m����ܨ�s�UQ��.b��B	��E���(�DQ�xL��4(z����U�cn�2�s�j���uь4�����Q���owN��otN�w}��U��}�zW��s�������� ��N_�n��8_2j6�;	���d�gt�����;�����gty��4l��S���]&���.���ݍ�J^�_��;�
endstream
endobj
65 0 obj
<</Filter /FlateDecode
/Length 4450>> stream
x��َ��B�V�} A��9��x�|�&v����@�x�f����Y�n�Zd�)�<�����ϧ�\:�gϽw��o��.��P�MR3?����?�2�
p5s��8C{�����?���������|�ˉs!p����������75����0Q��O���q�'!�/�.eL�M_�{1���M n	PK� [ �����y ��q�/ '}�r�p��,���rn�H�	_R��c�=�K@����Ɂ����O�G�R�h&��.�g���LPbV��G���v�����Q�B��
���9���-Q�Od�''��3 7�W��;ϓ���� �7�[a�f ��ӷta���;^(�? ��	o0HS�I`�3Q�c�O_q�㖛8���x���0	���p'��&D��K��*��F+��8��̔�'�q �k��ԈF �NY�ah���׋���;^�RrUoF���X�a^c�ƻY�2�%�vf�����x?��sE$�0�#rD�d��F�U�hAt`�'r���Gex���b�ȴd@.�� �Z��"� T(��0`MX0k���� �'"H�Ɖ��H����	P v"*�0�D�qH�����Ḅ�N�(M�\"�Fkͦ�H��f����;��)2$�E�M<���xl�qﯗ�`dpS�B�b	(	���x�=|��x�ӎJ!Uq�����B)���e�0�* �)���""�"��l���jl�8�Ƈ ]ć�!}L�!]5�!��	�)��V�Ԭ3���3;�I
�ԛ�|��e)R��~�5C�=k0�q	A�Mx@�"<�IQ'`^�&< �jht A�0`��&:��\D	01s��L2�F� UR�a9B��!�E!��Đʴ���8�ՆG��	��)����dY'#2'�X�C�6+������{P���?IP�it�c�����`8�1lr|#�O2��^�
� {͜��w�f'� T0� (cJI����*L	��<+k�^��@] :�<�ZT��A`)���V �*eͭ��V䙦� �g��m���8��( ��u��� �P����{o`����~�h��g)������B���I��ĥ���A�Y���R�0TZo�U-����(%U���j�����m	����pɶ*��,�V� �0��9��P��A����L�vZ���^�M>�P�S�8z�p"�e@�\�b,���lV�������f��P��4�BhR-�B`�\4t�E�p����"O�,��K�%�-�SE�%(J��}��K��JP"�K�#�=ܙ����PD�����"()B%����EM!E���j#����d�ߒ�qG8��A��R�MaC�C0S͖�8���5�ߘF����W�U�v��_�ָ$t	&��	>���<~��� ��p���s��o=+�0h�ǧ�u~�f�,]��%]%C��>�q��MVU��� �B��*z:��!��y������m�+���X��~���~�u����b�]�y	�sm��|�dvԅ��2��,ʔO,0Xރ��̉�e/�{�`����ö��g@BxPP޺������H.��Ԑ���a��`�ˎ9�4��L��)�RoFn8���W�<�Fhh>�t�S�d��2����/��}!��`?R�Q�DB��V�m��l	�+}m�W�A�>78�v� F�3qٍ%�Z�
�A�qf�,���R~sGp���	����9,�m�+Wx�)+(��#�M��r��;��sr��kK�Ǔ�V���zR�RLb�P��-��P������"��9~�s��t��A;��`�+Aܰc|���ܵa�p��g9/	˦��z��Q�����4�Ҭa��q�6�D�ݤ�i�1�d��8_��)	�d�F|��iHֆ��Ww�4n�DN�ȅ@�}_�{\#��c��>d�kB��$�^ ��:����tY�[
�v!DI��S���A������E\J�:+^$?� K�.�ǭ"�b O5@Z�zL��rpwin��᥇�bf�NeGy7�m�Vؿ^UߗL�*h�0�՜+�}gY�{�Ի���h������ q�zR�cz���ײ��ӱ^w3�bu�/��td.Y�2�+2$E����kA�؄E)�-��2�[�"����K��-��-镒�H�oEbgP�t��n�yo�RzVLzK��v+��Ky�L
$��Rvv���6�0�z��RFp��Ra��{Q��]�ͤ�F˲�n�5_
��ނ�TpD��@�P�m�XɼO-��^2��E�q|M-�uo	��a������2�l�D�P@�p���S�S���6U]��r޳®6�d�l��z�-�sש�$z�v��v����Bf���#�ñ�2�g4�TKN&9����3���9�>x��SQ�U�^7J.g)kp(��f�*p3�yc��+�KÂ'T�1���Uo�>�Yu]�������[OW�*g�����)W�ް+��.�=��������c�Oq�a�cn}����J0(zwV0C�����C�6��I?�Ќ�D�.�ݩ�ʡۥ,gy����&_wyϗ�#��tw�;�X7�x�p�.��އp�ő#�mn��=��v\q�{a�����6<�%ā��X���@��?<3�Sw���Y`�ݭr��^O��S����ҭW����XR�~��[JGj����O}�������%h��� $HD,�I�B뉤�7]/�=�=��R�z�7
4�w��O�X#�2#����s�ޮMw��Y�b]��Su
���Vmj Td�c�G'�V�{%���e��9������ɺ{Gx(�6>��cz#�S4tl��{����f?�vq����jom�d��mG?gh��?���c�v��s��ѭ}��I|�'���*eiq\}�bw��@c���7�#��ڻ�&�+U&��	;���_=�w�6R�����C������gj�sl�bg뜘�p6vV���
XNtt$���iAO���
<E��)�4xڄ�\��|'g�dF>����G��"xx>��O���VN��ܡQ�&��k��m���� �`V1M�� �g �:ҳ@6kǤh���~�&Mv �e�&vB�2���eX�O#j+[CL�z#���8�bl남�[���Іt�������`~V<�g�5�P HW�8�,O��"���0�WW�V�WUK����Jw�|�oa/�:���3����K�Z���J� � 'W���r��9M�� ʁ{�m�����[����+@�UW��4��t����f7J{銣\��� �O�ct�Cw�s�4�-�IB
����k�� � ����,7hf!m�+@�QWg�EO1E��lj���b��<��Qg��ũUABn>�hkH��I�-�!���T2^�Ð!t���X>x�O��C��%��!t���{n��Mt�1�=F���uS[\9��G��G=Zȭ�Ya���DX��ު�2;E�Wح**5��g���,�]2t����t��L�+G^�Y�X��%��V^�W��&�A4�����v�լ��<���פ��&�[D��b��m����^=Xף�\GV��_bU����^��jH[�,���5D���j�Je����b���8$l����Ҳ��!�MF˧���1�&���Ms.=F�!*ݮ&ZXB(��L;���A�XQ��i�}M����9:](����7�$�Zp�J�[��c8r�,�h�h9��$ea��|dj��
G�m�&�Z:䪼N��@^QВ]%�n`���T�V��ߍg7�5Nj�
13�r������"4��2��!g(@*ф��4`X-<+�uF9BL\�5�e�;�{F:��2��,g4J��̮�d���O���ȴ���d�����fdB����d���8�m��������Y�cF�w�,(WGQ.m^��C�����Q�C,O����>�e�x�=�,�~�F�7������+�O�<]I/�ف/D�uEM�:�D�H��Ψ����&a������ܝ��+������Whd�%u�7�IS^{_��n��9��*��s;��nײt�0?�����c��*	��P`�lhRa���M`���������˟�6��5pE�q.F�:��Z�>��*�P��H����m���ꌄ���+���	,��R�*t��<}���8�~X��h�@���^o���OK+���#ܝ��ײ��o�Qr�����]��� m����{�T-K��[`ᛇ�pi+N�ZQ|\�B�:�^iY��z�"�G�����u㐊cȘ���!���`:���F֦��~9u|�_QR���{Qg�z����	n#�!+0˥a����PSZ��#��C�w��B����CR�{��^9!g3��g�T�����Ԧ��
endstream
endobj
67 0 obj
<</Filter /FlateDecode
/Length 4903>> stream
x��َ��}�b���� � ����I���A�2`���T�y{��ٳ���h��f��d�U,����1�\��n!_��K�1�˗��<�ue��h+���=��O��n��V���������e���O���/?�7�磾H�v�c��u� �~����'s���?BG	Cy�~�A*{Q����ß���/���ypp��?/ Pa0[�O _Z$@���2tصI� �v��yq+�d�s鷃�� r���[���;8DU�� �8^���zkjk-��-��ud�P�+�Ud�
~y��-�E"���U�y}4��j�~";�[PN���@�C�Y���+�/��BJ,�[0����Ńj\^��A	�����2ô	sQ�z�0��[�[�s���,&���%�Е��m%\s���6��ڃ�2,H�)K�3��'h� �h}���(
�ƇC�/�<�����h-M�!�
I���9��bX�S�pEaV�!a�y�(�.��]��ɠ�"���.v�F���*"��1c�JaE�k�"��r?B��m�>R,ڂ��) A��}���*R�̃��l�,JPT:�J��E�@��`Zd��$(�ąq��K;l�t���@��N�vKT� @����t�RDt��ތ�2��N�%12�sb�U:�l���y�7��pY��W(��Ca�G���9�oN���)��Dΐ�܃��Kgb�% �^"���	@ؕ� ��x��x��x���S��z��x�s!�^"A7^b�%/�?f/��u^"è�.�¶��j4�	r��T��U��+\�F��M͹H�Z}�`�(��%P��� ��K �e�S@X���^^y	Y�2%aޅ���Ru�C�����8��ğ&���U�~�D���P�j[C��eƔh/�B5�QLL���ZL� 5��ij�E&�X��e�J���o���+�#����7.??�%�� l��+~'m���
5	
l�"�B��a��%(��T���D|�>,�[9���>��X�����+4x6&��)X�1��G�	E������JQ�n4��EI7�)-���N% �hx�����J=dhe�Ktr�B�K
`���X-�i Ѩ��L@W�n��`N�DjfK������
D1f��M,m�&B�Owü)F�pG�P5Q���o�1J��r���P��VP2&Ay`�Z�8\�lR9�[#�T�J�,N&���P�'�g�4.k��U۲�A�:ӷT�a3��0T��Q��Z�T=�G����f�'�I=dh���C� ���S�y(��U����D����$ T-A�4x&`���,,Ya�<JWE[a�Me1i[dA��b됩"&hS�)�]�RQ�U����?�1�!m>�����teg�3uᾔ��o)9��8����,�mae�z�A<I%�H&��'!���u���Q$ģuՁ�"����^+�.�:KǇ�v�o��v�v�k�����?�0!jII�1�C��W(��D�,�Ʊj�,�c��i[�	�V*,�cd���)9��Ro7�hHn���Q)�~mY�213m��� �+���I�H��i�ی�j�${b�H�lVM6V[&��Q,+��/�9�z��WF��R���� � ǰG)z�����(3��׫wr�m�k�3E%��P���Y������xi���d�m��qb�
�TeŴ�����E*J�"̔���y.̷�_cFR���FK�.��f
9�<gۗ���5�ދ�t=d�-�ཀྵ��d[T4�>�PO�r�f�F���1ô"��gBjfAB54�B2����~~k@�.��]}XY�p�985L B?ܧN�n#E�l?�%��+ٖ���̡(�{Q��a(ҏYO��t�c6�i/�F̲�C��K�8�c�����fb�X���#<�U�f өIm������6�=�ZB�]�ڞ���6��������8�V&�����@�Y�$8��6Re�	�l�'`��:�#Z�]���p�к�s��U.Z(\m��7�/�F&�Ou"���A��e���,�T�I���}kq(��mr8����X�ˠ��tRt]M�c�������#�:�;c�b��w�od��̗�$rK�`$�<�a���ц��'�&�A�:�-K:A�ZӨG�Gb��<g'��m<O:�8�o7��h���~+��y�R���O���4I�kƓIrƽ�)���.�8rolڰw-�>���������?��F�?�?����Qn��4馬R?�����"��T�\v��sh�:�?���S��cf_,aeO��\X�[X��4^���m�-�u"{�*����ac"�K�|orSj/qq�K鞼1���o�����{�^�p�k/[Jީ�2�"R{�P�^������{h[���&��^���C�z������K��$�����!jh#�F��H�:�#4M+���A���h���ꊳ#�
������t�c�����y��{��<;��ݥZ�L;U��?�L����Tŋ��خ��63�*����b�W�y]���Vɻ6S����ӗ���TA�Z�H����Fs��)I-�в�����)��|Z���[��(Z�O���VN���(3�:�Q&��APW�[�.(�z�Հ	�
�Q�r�()]7�~��;͋	�E]e.��2�Az��ƸZ�k�[�vO��*�
���n��$We���9Ѽ�tf�0���ɦ��z=�U��1���6��t.�+�����U.Jô�-�=��ِu�,z�X^+�=�*n��{�W��[笎�s�
Eu��`�nu���
I��e7$�����f-/���0ֈsi�Q�Z¸)�GW1s{eZ%�Rf���2I�=��F[���<�M�6���m/E1���1��@�V����Z�~��-�x>��'R�S]#�+Nq�&DJ]��}�{o-�����&��"u����&�H��"V�к2O�-r-<.��!�x��:��{���Eٕ�x��]��#�a�C��d0�v��|����v�W�,�;��i�����ڮ��>
�*XlY�X~0D�xE��ܬ,;�)��X�5RzI�*:~С��";'������k-!�N��J�]0#�Dض荶�
wL6ۂ���䐸�P������y�M̰�\�˶��~�*%�w��b��������Օ��\��AY���f��:Fr!� -��]	ﺧ�h��2�g�b$T��䡵��K�]8�A�D�YFe�r�X��1y�(�"����������Ө p}�S~��5}<9�pCd����Go���`����g�<5ϲ��)�n����+ea�)����&��2{�,�y^Q:��]۰��KGƠ���y]��b	�q	��1��;f“:%�C��S޿�t��tb�7�8�>��q��.���Y�k(�+�pX�>M�/K!���w��W4�� 9���=l�B��)"�b��X���)Qaئ��������檫�\��-��>^�Ev��yNG�P�e1l^7/C�!���I����V.�A����P�%��a�w��5�������^v�o��P�8���Rl�;�-���JwLgݼ���g�|����{��6��)��,4���^{��ؚ�������a����C'�!V�bǦ+��6x>��Ȭ.��r=s���x&�0fe��b���DqcVd�Ca(�>?Kӫ&J�,���8,V"|WC�KWvjܐ�֦�� r�������iZǎ�U�nH�Y�/�q����!�r'5�D{v��3��L
��K�Y~U<�5�t9~^����l�I��A(gQ���r���8~�����o�˻�Z�gG�60UBv�F�/9�ϗ�'N�nȟN��n����5��Z���C!���x�g���f�hR����r.lQ׊[��P�0�>�g�q�l�~k�u,�:�*�9��׬Wg]�3�+�k_��tH���6����Suz�m����IՍ"�b�Q�p��.�+��"�����i/Ů5�R�*Iw��#߅�j�b���4_8eY��j�R�o�a^�3k���Ud�D��uzꔜT<9]��v�Rŗ�*��1��%]x=%p�ݾ�|�ഋ~�r���y~�ҼЙI�D
o_kܖ�xʇ��H8=������홦[�5��d��O�5Q!�es���||��(r�	�@V��0�ǄT��8���RHr�	��)&j{��ڞ]� �ď�'9��NN)h��F*5�RMO*��y���hwR	��-�'� ����z �;�`؝T�a�I%HO*i���(M6�&Ćyv�pGS�O*�"?6BO*QQ�esN	��_��jGX �Igp��.B��%�r��b`��x�P;<#�Cn����S��0�zjGm��hc�c@(2����v;X���N �l���T~�SI �+z*��]�OG�t �
�SI 
��F�SI ��;�d����=���-�'CTAu�T�������7;�$�P>���'��{>�������������7Ǵ���q���׷�M|�;��@h��)�_��x�<rp�}�3�l�{��Vc���w�"��^��2QqٽXl���c7�*��M5�������m'a�e�6W��K����c&ZǾa|���Χ6�tʓ�l���w�s;Now�7�����b���ua�nX�9����-��7E�ג�;S�\�շQp.�t�i^y��P��N�·��ǐi�q�mqڹ�*�0�%��ݢ}�-L3k�6>ܴ6�~LU��=\��o��:j�}`6��q�4��c�#�q���"}>s:�ox��G:�o?��[Q��/���~0��s�Gސa��Zm	zƆ��w8w�1A
���7�c��*`�
endstream
endobj
69 0 obj
<</Filter /FlateDecode
/Length 3668>> stream
x��\ێ�}���� n�~� ޛ��(��`e����⭊=�m�4��ᕼ�̙&yX7ɚ]����"��w+{�\��1,?]~�����h+����/����+�f�����4���ǏK~��/����/�K���)���~N��G�x�����'������Qb(�W����ˇO��
��ߖ��8��ÿ T�f��h��0�C����$6��N?��ҮJϘK�Dm�[��Olg/�<1"��\�p�j}�rkP*�zKw�_�LF��\	쮶�;���"�[�1�DI+�@�� ��+Z�_�f߅�Z��*��e1�5z���A�C	�]E���	����t����|�i�e��I��B�焎�Gl��.�'W�>#�K��Ӌ���J�)�㇮��F�ڃ�
$`0��*Ă��1Ҋ��'-���bh���ǋ���{�w����È8��.��9��bX�SH��D�j�æ��w޻n�.��]&!�dP��!-����5�Y�t����CĪ�s�j ��<" ��u� ra�-]e� z��&�0�fSO��������vǄ	X�ι�������I��faZ�X갶C�J�7�f!�qfI�[fs� ��ʔl�͇;�9yEs�&J�fL��!�v��V%2/�x�����0.��)��� ��������da�yC�=Rf�[����.N "�q"a�8�0ad'  F��D�~�D���]��VFh�x�H�&L$�*L$t&2��DyY�Dyׅ��q3�]r����eW���t���is���a�W�ȝ���ݹj�{}�`���%��y�HH%2�J��@Ƣ�<J hVe��i��F���Q1�G�m�DF�(Q�%�%�%�q2$�L� �lL�	�|���̛O���uH��d\�䎤rۦD��'�����ރ%(��sbVR�t�b�Xw2#0����O����^[:�z�G4���Q>jPN�$H�jȆf��Ӵ �������k|��n��4_��{R�'!:C��GE�22�p<�1�,�Ct��⡌m<�pzc��y��4�_,-���P{��
?-��z�a_���v5�S�P����D��V�~0���ld,D]�a@"�΢�-7=�נ	��TZQ(�n�ޗ����2B�pܢ#�㮸�����������D�ӕ �8i�U�:{C��l1��;��b��)�[��Z��@�ob"������mD2b5��un3�҅c���	>!F��1����v1f�����nhWC���(j��X�� �-v\$������V���t�2���kF}?�_�jO��;�+�~a��a7��I��d8�����	���әU�_��/��n�C��ݍ���d�0s�9%��j=Hr��f��"ǋ�TL�K�N'�o�##�X�gd�CE�.M��l6t�q�7��p�s�b��áQi����@���+�C�-&�p�_/2�UE���J���0����3���`nrA�݀�Zu��U*��\hO�d��6����
��a�(;�4�_����a�'�Ѭ�X1<`�`A��s������=@qURĎ��B�FK��t����8�%���J������b0�&���*]Tyr�6�f�ٴ�%,�4! f�8���ک¤V$sꝴ�y��1�fvm+x�V��[u�"�tŊpqY�*�ĳi`�30�(��<h���vM'�@D:�G�R���� �/At5���],6�!4!�´fʛՂx��;�4!NBy�I�8]��8/˧U0ߦ������Bm���ږ1 CU�؀>�}1��PЎ��69�ri��AxԮ��4�R�*v6D�OG�i���Q�we-Վ��W,I���A>^������h,���l�<���[�]�h�m�����z��P�FT�V�>b]'����*�k�^��Cq0t�B�xWǆ��g숞P�"zƞ�fp��멞�׆��4��)��E��pS�"l	g蹱���c�M�S�M��&�q�y�t4�s��b"�c��C�֕�c2n�s��я}��'��T�UQVW�nzЏ*���rč8���2!p��Ҙ��oW���~p��R?_�3%��o"�CG��@��9�zX���l|�1;^2V����&G1�ŉB�,�s�s�=�w�iЉ���XTx������CsS�)���3, �>h^�}�@�w0�/L����uy���!LԐ��l��zDN�X��<,�ï��J��sǬ�[��0ߠE�S� ��E�S�ϥ22��l-?�cn`�1cLn\ÝH�zz&��k�;VRے����x.kS��Q�2v;iMg)Gi��h�IzZ|#�Ғ�;Jb��\
[��{�F��H�P�d�4a�l�pgB�;�ýg�g��n�Y��;�k�VS,)�KT�8JTѢS�������du��ָb٢S"_�b�%o���X�H���PӉꩴ����a�Z��ӑ�-�����7��p�Ni�齴�oʎҒ�4��%4�$����W6���fgs���UZrbG�%;�	#䫤%��$��ՍE�֝��qG�%;�	�rGC����=�� e��ؐoͮ����n�b4��V��<0-�"�b5%Jk;���և�h��Ծ|I��ܱ-�s�-%={O)Uՙ�Cw���IAw�:�]^)�t��e7�:�U���RB�m0��.^��j-tW)��.KV*�_y�Dx�D�x�D�X�A�U&0����e�m^VnrY�D���U�k1F�X1�y�`Z��PP����,�A,x�%
�K4�LPkV��Fa�,�+|i�Y�L���\WL�XJLxɄ2�Ąc^by
]��_`CEѕ��
H��K& ���I7�F����/�h /���T�@cP�'CeD��hzT&aj�	/�hEI��":�Zj^;�#DY�4���n�O��䠚��Dȕ�0�R~��G��'��&X�V�B�SU�A�/D�[G�ص�|���h���Y�g/��l�m����%j�R�Y�c�/w%��~U�����嵗�Q�9#��n�ʅ'u]j�o��������_���F���r#vs�JJ`�ܕ��[��{�w��k�~��jk��č�_β���?8�	
V[S�%�� �A"���1�c��g��u�m�mij����0I}�5�����as?�P����m��v�n��1%�,�n�6�P?1��1��S�?#w��F>��xu6�K��^�W.����T0L���ve,��䖖�X�I�� ^&�9��v�0Y�����٬�3�"�4,��hj~j}� a���M6�q����)�\�,tn��B�(�x���EA�|6)�('٨ڤ7��SZ[�ߟJ���m@���\��n�.�l�6Y�kq��L2����"�,���Ȳ�z���Z������[��D�1^�����
2�|�)1Ǩ�lv"嶙�6�E(��sʘ\���ԥ��1��[gN7�2�h�������͕�&RJ����,cr�ZOҗw�CM�2��H
B����!x��sR�cz��NPז��{a��:�a���K[��t�����4w6���������h�w���v���j���j���N�yd�n<���M<�%�&�Zc�2H�������%
endstream
endobj
71 0 obj
<</Filter /FlateDecode
/Length 3686>> stream
x��\Y��~�_����} A �����(��`e���Rū���;'�]y��&���HI�J�����ie���5������~�L��".�����?-�ݬ���>��?AC���������r��G���ԟ�z�R)���D�j� �>��~x1K\^����r�~�A*�(��~=�Ym���������,@PaK0[�O�Z$B8�C�DЍ`s��&w��z^p+�d�Lr�LԆ��J�c���[��G�� � .2�+[�S���[q�����Bqav{���
~;I�V�?f�hie�
,�B�^A�"b�>E-|Hԋ�U��e�=4�C�=�Pb����z��T�o�`0 C�Hj��6Z�6��P�=a��[�����k�o�SH���J�J<B[	߹�TFh��=�=�YhABw
xib��������M��t�|�4�}����oOo��j-��g���K�E�V�T4LL�Y?L�y��j�W�vi�}�&�
̊H�"����F;��g<h��V}�[U�����D+,�m&��m Ӣ��'I�hVe�B
e�U�i�id�v�6�TD�i:gF�$���L5�HՉ��:����J����^' Q�9. ��I� L�Թ�-&�D:dJ
2ns
G��ms"��/�azK��B��
�
2�GR�H
I�J
?]1g(�܃�k��� �<K Ţ�N,�i��$�'	��I�[�A��'�L��%��7Y"��,�i>�,��}�(�E��K��O<KTZ��e�ƼCv����N+M�.���x�%;�>J���4Q\c�҅}qaK�Q�H���RV0.����$d�.O q�'m�'m�'u�'����������V�Dz�y�<ty��ΠԺe�c0xVI	�M�v�9�E3��fJg��, �wX�6/�0�f��>��G^�~��O�e����tUQ��^�ʞ?�So�h�b��(dHD���QѬR�4B�@Y�$��j����CX� D�����S�����#JOD�itГw�9BQX��qUR�^(a^��@LSv�U��(�y!�d$��V���§��X=���{>sJm�� X��6@+7�
-[�UH�j�B"�S��(.���%�^=js�%%�ҋ�H�ʞ?y�$c�#g�q�)��� ��׸Pn��kĒ��,�HC���*�)@ ̬
�U�I�*������bER�!�<�� L�Xy�V�E�F��J@�)0��Ru�+�����,DOI���v��ުՆ��"B�P��]�*L�۰��ECo!��)���$i�4������.`,��:a�_��%M�9OWTdW��0��t���Z)��[ (yI��*<X�JԼ��8^,0��`K�{��� �]*�3&
a���f@����7�з����ϐ��|��7�7OU�0QBKݫ�D����j�g�zZ�W�g�`�[t�(�k���]���s6:�j�@����[��F�&8��`#q��:�]?M�}��)��F,�}����wv�>���v{2�`)M���7[9G��uy�#��\ ���)$N���:
�Um�s�1�|�q�=�_1����d06#���qn�s�@��q�@���c��YD�ia�u��o�bB��.vL�qt�͢���Ԕ��������+�l(=����H���0��Ƙ#ƏR��>�(}L�o2���I�)��F�Q�m���m���<�l��5�<����C���Qβ���}I)ӌ,���9C.��4K�RPI/���w����I�����W��h
7���@�I�l��+J��JN��������cCik6�qt��x��2�~�y��i�x�7L�W!��ڋp߃<|I���^$���:p��\ �v!��|�9$,����Z��jmB�V����L6�]���N�� +j���� Mb�2�R���%��jL�7Bq�Pw�_�~��1��氀�`]��y)\�.����P�H�VĠ�e.�J�b�A��� \��M��l8������>�w#v��C`�{:��_E0(E�t�э��[���l5@K��1 V�`t����",�����mf���ޕ\����n��:զ��w���X��� զaL_��X;:s>k}�� ʃ��%ţ�"Q�R�FC��}�J�Z=�OU}.	��If�' �8m��Pm��������b�.�pg0�n��`���4��qk)�m�D�
�o3PK�<q qYț$5y���#f�ۀ���%��3�b��uA�K�����`"ɭ�v �W#-�8̭p��U��3�e���Pڴ*=���;Z埉�v�Jm!��Y�&�@k����h���"�t|�� T ����. #��5Z��Ј|���FgL�w:q���U�V�_{�T��T�I�����E�}�ăX�E$���|_�a�;�\�i�R����/S���xN��N�6��;+�������vk�\	�W'�]�A��#���q�~6ZI����ğQ���z7�	�$���������7�VV{�3Z�8�y6Z{%^�V�a:Z�&?�����V*.^��++jW��Z�Ӕmp�V��ra\���D�)9�k�v��"��t�+��ؘkv��}W�8����9'�a�'Rx�TS�-��:M�剢úO�^�)s�hk���(��T��EP�"(�TsL�A�:�'(H���N��@��`א��7
�j�"%��:�#(��Sr���*PP�AP�}����-�_�Vy�`�$p�3z�����s����<�V׿Ѹ�r�d&٘��~0�B�o-4�8���n��~����.�0+�����/#�/���s���6#�>��?.0��ǫxY=�K�	s~{܋�݀n�q����M�'��OHh�{z��=��牪��4�J�7�tl��Q�x�-��nG��7��z���}~+�q�X��L8dw��p���������~>?����Z�拝�/�R�Y�5$��6�d����;,�,E*M�R�"�T���=�I�l��8���HE��6��xna:MC�w&ۂ}�2�k4�u����b��ӳռ�e �f_�� qn79��]�V#�#����c	����䇇�^���.��r]V��@�9�X0�+�m5xhau`���c��T�礟N�+��A�(��H�9tn��-��(���1c�䫄\�˩#�3�X<�Z��ϖPo���rk�z�ogc���qe����&�19�5�i�0���A�u�F��i�V�b����~�d�y�δ1��R�R��Y�hwc�1�N�?��{�h�{�=�! ٣-�4��R`�</��9]��^K�T�Qڷ��3$�?��:>���8F{���|�8e<�
��,�E�s�-�N�����T��_n�S���� ���x&����I_�B���,��,}��XD�G��/�R��EF�J��E�{���ٸ���Bה;]줓F�ջg;�<��#�sz����CV�r�W(���w&#�o��C(�F>h�Bq��]R��RR3n�L9 ץ$��� %�.wII=^H���$�kR������>�J�
endstream
endobj
73 0 obj
<</Filter /FlateDecode
/Length 4137>> stream
x��]Y�$�~�_Q�\�} A��c��x���u� �5`��!uRU�i��z<YϬw��]ɏ�X*��
������w+y�_=��-_��~;��B9�H�����N����+���\j��;�������_N�� �_��^.����(/�/�һ�����◧�a� !_�]��B/B.O_OeL�-O�9����m	jK��`A�@p�98Y:�⤏O��\��;K$�v�Dl����+��s�%t��	*_ �d4�����`�:�ɭ�[����H&�0;����ß�N�����Z8"-4x� ��Q�V��A�"�"þ�TXa�E�����俫�0���0�`�^$gJ._�ƼY����s�R��F*�Mj$�D�g��������j��+��xI$
a.��4x��9|h�X	�^h�%��
 Ef��D3�
�U*�m���+Aze]����_N����߭RrU/F��Lz2%Ҽ6�6̍w� �)"&Ҵ��Ҭ��4z�W�v�BH�N���
$	6�q�+i�ȦL��	���Ge�?���HY܅�hFi*A�y�%��t�qp�(д�T�@��$�J��~G����)�$���
TP*f��0a�f��y>)�W*��#�̒V'.�o'�װ(��)P�8#���,�!�[�H����ߘ!���Đ_��Ƃ��>��G^���'*�T}��~Ή���D��xǢ�&�@�J5 �I�f
��kH�(E�@�4!|�(���B-��M�4�\�(u�("-$��2%���I�F�0OI=�2���Ť!�ա�R��a�"ї`�QZ��-C�>[0g�q�h�6O Ph���2� H�Z�i�b�3M�@�6K m�%�������Y��,h%K໒%�6K�˩�i��U�o&I�g}��W�ILd�h�$$i�U�i0f�РM&$>U;|������)�������s���6}�оB���BT�`Y�v��w�hV���Z���@t+7�f����H�rP�rg 
"1����J�5�pzn��ͪ�5t 1���,��W��o�P[��y#:9�*���ϩ3n��S3'���r�:!='Y�T��G���(�LZ"�Y�y�`i:`��44X����6�<���4ղU��U�����g	�[�1!��Y�P¼AІbI�����q�#�fN!��ą�%@�%̄b#ծ� !�p�R�:���:V S
�s%*:�����j&"piX	kV%��������h4֣���5mE%O���6���C�l�0!�!a�Z�$P>�m�L�2i�4V���+HE�ƪ�@K�d����!�]���S�Z;��~5�E��q�+�G-��6�f�H5[�
oɝ�e˚nJ�zK.!�N.2����܆�c��К1��7`�]|�ya9�Q���L"^[�
χ�S}��������yC���zaT ֻ���(�(�z��&�GM��	��=�eB?/�֐���}|�ԼA�Wü��0@O��/�h�$c@����!9�>���EA�p�h�`w��#�ƌ�X6*(�eP�j���7�L4�{�0k����r�G��3d�d�2� ��]5(No=�KqC��R���(pS�?���GM��C}S`Ś}����?����biT܁L;d�Qx#N�gB�P������kÚb��E��]'z�G�wv��8�>g@�	��~��ʧu��i��o���b'���a�H�A�!��������ȵv�	W��mD���tZ�a��B�P�����V/y}�}��a���MJ�O��vs�ǁsqo��1X;e�5�c�'p��n�v2��2�q�A�\EN��.�y'�ğ2.�ת~�u����V�pѱS��x�y�)��ϫ��Ǧ����`��#���2���Y\%�����D���r��a��셃���0(�4#��l`i���������	�8�ޑ}��ąwR)-��**7p����5z�1���ʁ��X;plܥ�Hkq7n�H�ea!�z������u�
)��z���V�{Q��f�s��c���7
��>F�b�ȅ�R�}�g�)p��`Y2�ˑ ^=�n�q�����N��P�}shYݛʥ�X�R���@w~�L�&��L{m�e}��dWAN��<"i��>���L��"uFZ
�sk�[�TN��N��n1@q��<�G�Έ�F��]ͻ�/���t���PŽ�&ܭ�������^��I?���G?<z�t���U��S��8�vd��
:��5Ɩ���X��1͏�f}���Tp;U	���V�ǡHà�z7��Q��KWO4�ޏ���ӵmo5���.|�l�e1�zt���uh�x;��<��y�b�L�.�-\{)�[�u��隲�n�Q�݆B?��kܪ[��^��r�OFY?��L�����±���11��~m����C�
�f��ۮ���tauyY�Y��⏵GW����;�Ήe5��U���;b�A�-�ʩ�Ў.�iK_��W�F�K��.m�g��u;Vڸ=�~~����/�wi�u࿦Sь<�x�#z�r��K׭���Q	*txթ�T�椱ҳ������qKx*�Yy�z<F�"�[�~x>���ߑ�7�]���pǨO��7�8'��9��P^�2'���O�i���Ѷ�qlg�B1MZ�(!�0�H��$(Ӵ�aH���ܤe.tx�֯��Y��r�oi"��gF&�-i� �{�[�܈Z1�O{�
P�����H��Ī��D"�IPH��I�ze<t;e���F�B��]r�H����{�RMD�֬�W�W��̾ON2��;U"�Gw�4��M9��O����\��
�
tbN�>9�4`x�4sq�Zk�W!�&�B�=rupi2�LJ?Z+Oi]���7�ei��p����"�`�!r@�O��D"�t�G�-�r@J�9��tll�`D�n��2�vʑ���E1W#L�,��JVo�?W����]n��]MR��럛�����͆�~������kS�����|V�C����g�7iA�$��p�g[���=�P�(<ш5�k 5��*�GOur�ˍy�w��1�%������K񕭟Q~��k�WX�t�TnC�3Q:Sɸ1�HΆ���@�̀�'�ڕ~��'�K(E�Q�=Ҧo�hD��G�A,��P�����Uk.��"�|sC���x*9�k�_y J$!.cښ�>3쭿E�b�{����Y��1��P�`�5XK��m��m�.������.�@'�4��,}���.�@5�
��8B��H��9�a���3D��T��f�
��y��3�ϡ)ѽe1S�!R2婌��	5�~gI��Օv1�
0n���D���k"�SWH����2���X&���L|L���ǩ�C�)�RL�td]��+���i33��"ם��
��R�RC�*��;�l�����4S�S�������[o_�.c������n�F�㖷*�+����H�ʆ�Q�W�nQ��j߰�'j]�S�Lm���切'½���5[�S�����j���ϑ)Ѳ��{*��
��Р�>ksD
�$��r��"Z]\3���3ӌ�*��*鲛�ҖB9�ʾ��*z~�&�9e1d:c�LwdqNx��✈4S�S�&�>�>��d9͚N`b�w��7��z�Rx�w��ΝL��� �������oO��	*�GV���O��O�Ct&gQ��{��C�=6udkv��ׄ��.�-�n�n�%��r��A����'3�Fs��	p���4@B<��Un��~ӌ����絇�@;T�����#f��|\��az=�W4O�?�o0�V�N!�G�
_��������b�;T�^選�|,rwzm������&�Yz���ӏ]��w��>�xE�vcs��P�TCŖ��`��)�?�v�h��GQ���Sm�Kf�ʜ?K8]mW���%D��?j
��͔s�c9����ӿ�-C�U���49�uNB���	�^�կ��׿�Js�Nx�̗z~�J���^���1&�_"�w��=�KZ��[��~�_�ҍ@Z����+RR�

���TCQ�
endstream
endobj
75 0 obj
<</Filter /FlateDecode
/Length 5715>> stream
x��=َ$�������ú`a�������]���1������AE$+�HuV�LuO�T2C/Q�(2����&���1�Dc����˿^�{e��i+����y�����f��[�'h(o��?�z�~���?�U�~���?�MJ�������n���?|y��_�-޾�:Z1�7���7�o_~y�w!�����?^|��o Pa0{�_� �X��C���nMb����_�#n�]��`.�~�D�1?>��^�=�y�CTy��������Z[�Gw��x-E���r�����z��-���DN+�����Z�� b��4�C��዆֧��@�C�I���+�/�;�%hi�n��ҋ�W�`p��H�>��2��E��B�Ǆѷ��q�^��;�>#L�2�0ϕ����/]j롑��� �� Gq0b����Z����'_|�7>d�}���}��?-ZKSF��BG�%¢uΗ�����T4MwC������0�w�.����pa2�P�hV����q��ʢV��",yk�����>`Ív� ��� ,Z��J�j�7J�,���0�Bb\f��F	������o�+�A�YT%����:}B\�.��P�ȏS-��R}�P�L��EZ��W��lȬ��&��N��k:�T�|M�#�����E�n�h��%�)������>������i��2�<X�v��
�Lc�7�
۴��j�Y��pA'.an�~Au�B@��< l��T�ݛ������l�O�y�`Ts�TY��T�3�T�39t���d��!s.s�N��o:��d�l��� e\���� �[9��n�x����8 hov44Z5a�w�t�-B�b������>�"?N)wKU�"@�3�Jt8SDu��N&Ef�;/[3�1}o&6�f"I�L�!���*|X���;�
ם�hb5ޛ���^�ۛ	���Z3�>R+��d�9���ڨ�J ,H݈aǭB�Vb�mVb�5[��Sk%6U��%U�u�(wV"�I�@&�N�B6�U�?d�%&�9Z�Mgs���Y~�,����@�F ����~�m0@��JD+eCc&f�o(G�wng&��_����Ez�paZ؝�@��L����ܮ���Ck&��T�r�T�*T;3�D�3ET�+�dVd&ѹ��IgY�:��Y>t�f9�Y>�=|����a~/f�owBl�MXC/�BkB9�e�9�b>o��%
�"��-���@��� nl��F��_� �b����cA8�c�������m�ZA.Q���'��m�l�6��atA�/~LHY#a��UHcm��4D l=��33�8֦/LO������jpO���>��y�G5���'�SlO��9Lğ3J�a��aL��RG�]�NG4x勘��Q��}��6��2џc�N%^��F�h�S�@�JeX��D!㤧90�Xg c���sB)�(��7l�yf[\���`�nn𳉝4���i3q�a+ɛ0f��/��_Y6��~��q�ׅltm����KJPJ�c.Xy��K=�c�x	�6�E��?��p!jV(v!'�]�x
�<�f��2����r�k�8��,�ԋqdq� ��6��{�#���<R�<�X�5��_�[P)�Vͼm(�Z\pK�I���S��";A�!��PC�d�#\"���@^�q��S�����M��Jv�ǘ�vM�+G�xt�8���n)��� �X/x����=!��7�nv����y���?(cm*����g�_�����-��(fw��ָ��f�bͱ�wN}$�r�X�qovx���%���:O3=i�	��8��Gi{gd��vH�Ƕ#o���U@OHt����6Q���t��s|گ��[���̘�5�B��f�=5v��~�{�{�o�&}8�ߓ��(-,$7P��2%t>wכ,���4~t�+$f�ی'U�o~��������=NWMjϝ|��]�2����Y�NV����/gΰXΰt��}��a7=g��r��o������OYm-N��ф~H��[߈���݆��Yd �>�g�U~;5|&:�E�ó��CbU5�Ϯ�I��>:ߵ7��L��Oi�G��}��}f�������d������w��;�Wm�>_�v�&��'zç���u�2��ؾ��pb�І��w=s"R����ϙ��N����%������jܨ^8Rg=��#�q���ٮ
���^C;Cq��)�RC��|b��ۇM�X^��=b?�^�Xu��7�v��u���c��i�Vh<�q�R��ݦ�̼�����'���e��Y��/�N��;�t���)��<\vݺ����Lg:��%��<��'��15�Rl�l^��ݙw�������#,�Ha���Z�'xO�v�'_DIY�Vem�x�kz�"�&�����׳"���QUN�ˮ��8<���w�X��=?n�U���R���N��s�2�d��[K��j(��؂�����/��{_k���[���H�m�&Z�]z6r�W,�wq�wk����"W�#Q�p�p�ߢKg|v�\��X�#��y��&F���]�?fQt���E��(���\R�
J.X�k�E�(@� �E: P�f���@���'h���,� ����-A�Z�1��:xa�h�f� �6J�@�'Oo�K`\��EHi!p�@q�Īw�� 7v��303�k�r�0����c�X�8Y��4,��ҙ��Z�B��+�v��,!W8b��la�qmN�Q"��H!W�:TR�hVuAES_��e��a6E#@X���5@��దV#2��XS�ݱp^�T5���a�\��K��b�]��%�/��^K;K]�Lo��r1+�����W�f�p�D۹�n1jU0���hťjpk��ن���k����B��ktz��e �k���H�Z	���L��jS�j_�4o�a�+p+(T��`�Re-i\d@F��j0��%�Su)tu(����|_��V-��c-dWsH���f�� ����w4�h���q�J�qyC���p�h�7�aXm���ោC�GtM7\3^+�v��7���݁�f�?��j�(��(kvo��XY�6��7>��Y�e���pd]f�rĝ3zk	}��/��9���DAXiՆ����]��9}VL��n��3asb��t����\
Ql�&��b7�����g�F)O�ߡֶ'����௭Y���ܒ�E��3ȶ�d���S`�a�ޡ�EJc��XBa;۳���5�V}j'�:�L��a���j��Ć}���l��]��Z��E����}=����k͸��+�v����x�;�����4/��b��a<Icbe��e
�x*����CR�3�YF�t�����ċ3])�]G��%��3�>͉�CcY�8X�ԑl�$�8��㎚x��R������g>�z���U���U�&o�	�t��4v���4�������ANCy�q�Y�|�*k�i;�6�k�ƸO,�_����LN\�f1�3!/��Qw�U�����*���Ux��_yvo��xWVcO]�w�.q������F˾M.ąD����^��.���j^�������y�,Ƀ��ِ�2y�׿���g��/;5<2�竑�S��MW%��pׅ �����<��a�8�SZ���[���(��x��fΙϷ/i?xV_@����������Xu��E�F��B���L��.35�--�%�<���x��M�?rG-e4m�}�i��mu]g�y��B2 �'Nts�Q㲜�� ~��PH���َW�e���o�����0��೎��x^*�++vp�'*�4~k�,��ws�)���p��̓�`�A�b,�T��뎕KQs:�3�8�z�D�����Y����T%��=f��W�e���
�T3i�Ov��yFEYޕ��.�&ෑ�8�œS��p�޴���	�Ĭ3�?e_���5](?3��V��/�W	��N��8�F4g8�Ϙ|a|c�&��b� ?�ˣǕ��|���m��6�|�I͸��$μY:|:~�t�y]Or�/��r�p���{(���}�g_(d����[~���Pg�g�|y�
�ěY�C>xj�SJ�)+�c��&䃤r��J<Z��Z�#�V��-������R�a�74]	LE����H&���IgК��<t�n)�$`�4��i�H����q�1j�7Ŧ&��ky���S�þ�@�h+�@�fC�1�Bc��s���D�}���*��Sҕ	�L��&��@��2����4�M$_���7Ǥse��Ѥs%�1��[Z6�9ؖ�Mr���zӌs�eM
�$�`m�yЄ��	�Y��&}�����N�-�ℬ�W^���S4��x�D;�k� <�o�1
����4�NK�WX��景��4�|�sҪ��v^eCѨR�S�Ȅu��˭g��9y;%k��ͻɚF��f�����2i��T���3�$�e�ۓCjĖc�	1g#�0�|����}�� �l�UT�>��Y�;��#>#�sb�д�/�����ޓ5��N|y��wM>�"�K�M��򭢉�pb8(��#��M����]�S���۷�~!?%+��8м^v6���9���p�˧�*�	l��1��X�Ms�ym�x$n��'�\_?rs>���F��$6�2���T�|�����������[���{�'�S|�^��
���9]eW��]~�,���xI3��8��vR�$8�\ٞ�>�i���4�f^eO�\�ߗ1\F��b�����ĲRë̅[��MO�w�A`������x@y⋮�]�=��Uk!ObS]�Hb�ts�0�1Q���Y?���G^ͦk���g��F��-[Z�r+MP���b�->r ��s:6gV+Ku�t$��VS��\I�Vl�j���k����Ke� Jڵ(��uAm9޿��Ƃ�v��Xj��g~q&D܎¡���Fa���nG���n#L���j���D�3�D��$�L�!��7	P�X�^��c_[ֹ�4��U��DF��6N�lb��\B�4�0���v��vѸvU�׾��(U��*�J�Q_�Amm���.�u�N���Z��DC������Q���n&� kT�oc�Q5�v��v��A��>k�^������԰u��Ʋ3�h(``�u��l�9P�@��G����l��"�P�ޮ���*Be�&�4
+I��q2HM�N"A�jE&�)W"�V{}�`��������A6�]ֈ� :3PLǨk.P8��$�B���|�`tL��:�f��	���XR��:�i�^����a��7��B����-����W��xJ�����R��}^���BϹJ��!i�_?�o
����zß�M������t`�u�+�&�:��_��q����i�������I��6�"�U`����=��RA�8���L�9��s�[	�΋��	�ZA!Js�e�w*�c�.�m�ϊ�&�|aG��<����Vj-�[�;�D���ҩ���.�V���%��S�g&3�RM�݅j0��1�it��z���҃z�wn��:����Ϝ�`��P��P#o�`�U�����������<R�R
endstream
endobj
77 0 obj
<</Filter /FlateDecode
/Length 4378>> stream
x��\َ�}���� ns_� �4��s� 9v��� U$�Ud���$��W�>�����d�zVcs��(���*.��k�9����_�{�Z�Wy��������n�n����
����K�ᷟ���.?����]�6��� 
o�?���?>|�얼|�	*���5&m�b�����_���o���>��� &̀��X���
�N��ul|}$w��F�>��_�NQH��܉�:ѳ��;f��w��$�$0p�1�O��O�S�iegqg��ya�2R���������>hրܢ�_��XY�����%�]�baG�'��wbĸ5gs9�~ʺ��#�%��� �a��A����.bt�^8�� �J����a�,de�}���>�tԡ�g�h�Ɯ�q��a�c	���G5|ړ��P��԰��9�*gM�)����>ҝ .�	»���?=���^��j�7#<��M"�}�dȺ��V��BLļ�?B�b�1H�C�+F;a�t2����U9��ڈ:�~)��	�!F�O��_����`�E��Xp~� ��I�&i�j5�>L
!�M4G,���F6B4�H[f�W�`uĬj���A�Y�H/��H��S����!t��$jV� ��DAL�`g�Ũ #ɱCƔ���.�#�G�[���������\(���Fo��F2Z��놶��-@�����#O �f�(��C�<�C:A���`Q f��䊂%��
�!��NDQ�B��F�j ���@�M������b�A��Å��ۇ�_�����3Qtǈ��ب���E��@��DQ��(
6�a&��MDQ�Q �I��khx08B ���8�b��8�]�o�AD��pcd`6IE��.2�Yc1�4rȐ	��b[�aH^�Õ�'�-��76xc�76�����(^�X�L� ���b3= ��T j�MEAfv@lf������m�љ
V١�H�P�Fv���y����y���0F�;�}��v`k�8oف��� Kv@�� ��Xh��m���b���V�#�eo��p=�B��DAgv(Xg���P/Fv��eQ�2�X �MR���q�X�2�1dB9���r�W�h%}�Z�������d���B��:;3���6�b۝D0f�I ��Ki;�fzf��,ؔ�,ؖ��`��D�j�����&e����dS�>�#IW[�&��tdE9:��r�g�x'#�����#? ��J 6o%�i-!j�v��@l�J ��D�$`n�@lK��$Q�Nx�I�^�$A��P�feб 2<ITŤ��v�]2�=dL9���rD���%?�q~Ӳ�ވ��<� K���Y`�@ �Χ�����C��9Ԇ`F��j5�yT��O������V�=bY������?�` ��>�^Cʹ�����1K���B�����d���C0'���,`��[D_:� ?� �G,����H�6�a8������Z�#�<D��=�Sm��;���3���u��J�C6��:
�5��c�1
�������<Hd�t ����!���������
ӽpЫV	��=���Ud,�vM��j���g��H�d��f�`l@���֢	v���7ƮJpLuw�
G��QXHʗ�-���B�&$��#M��Y�&��f�Bڄ��()�
��$8�"x�/��c膐[�u.�$���&u�eD7�u�M�c"��F
nbF�T�aQ��<�Pa��n `0BԾ��zg#�\څ��A�jtei��0��|��� ?�X�LB`��O� X7�l�<"����n�:�����E��-�p0���sP?�36Oa�\9ʀ9�N.7�7���z�ڿ��d�шP��}<��U��>|�L>�)ĥ:M ƕ��*y�w�aV9h�X��2�t��Z��6mԵ'��.w����0�/<U�
����{�lX}���	�A'촂���� ��jU����_�*^�kkr~�'�=�-u9p�iN�u-C뗲N�,K��	�?�����Cu��:������ �l�^��:���R�=\��i[��Ǐy�,�T�V��!���lɝ=!�:=,�E�FK�E]މ�Ug��]�Ņ�l�Q���=n�`B�6J�pύXpl5F��Z���?請��Z���Ln[��:n\:@�w����0��t~槮�ZS5=�Ώeྂ.I[&�",w~����>VX�y&.C�����8�M�f�A�8
�������=}&#�m{V�����Ϸ���>���T�хu�o�@1?�f����X�c�;:�9��T�����J�� ��&&lo̧y��Q]�����a�ʡ��M]tf}����r��XQ3�5��]�u2c���}�s!���	�Vܜڱ�C�b&��C�h��/�J���^�n��ݽv�iǀ�}�~y�=��
z$������������1�ն(���(��;'�=j(k/�Т9�Ή�/�Y�CW:��x���[��ۖ�B���ҫ	��c	Z���S	m�L1�� �U���8��V'X�Y��Db��Յ�d��C:q4 e�Ej�ʣ N�[q^"����>w&��`�؀��� �i���eD�YUh]�0�T���Gf<� � ߕ�2i
�]u9h�FaLN0*�&e�p?�@)��e�`��j{*aT3�p(���#n��i�� �\��r���U�;y0�'Q@���`q�j<��<��<��Mpz��ⓀA*>5���Е�"�.򈂍(O( �	)jy@�B-c � �(�:���VN�N`&�a�8� ,g�ʣ	�<�Dtӝ7��,D��C*�Dԫ%����8��F���>���G|�3��i{�[�2�f�|���SS*�����퍽qv�}v+3�W�\ڌ��j�E�R�@��9�����;�nF���_�����W�ɵ��J��pC4�ɿ]4��2�Ny�Tly����u����Sr~����Q�ԖMy����D�z�j��>�$��En���.Eչ��7�,X��T��l�+���&��myK�(oyn�}.��Gb_6���
Y�40�sa�9��B��������/�����+��J��O��Ѝ�j��v�K��H��P�Y�9�B�_��<ͻh|���iOtr�������٫p��eek�����t׭)k,�����$�v!G�;�k���"���>�{���n��������ɍ�o��s&|l�j�
�?��o5��J�~���cpX�ޅrMmo����',{�O���f��WtL��5��a�v.�W�3��QQ�ߏo·���1�py��S�־gc���8��̖�#��k�����BsáE���*!��W��v�K�W�p����m�	��[<��\ې�63�*�!Am`]K��S�%��R��M��
�wCr�`�v�Y��T܊�4c23ͨLL3*Һ�� �Tq�]��IE	�-dF���2�n5�ʚy�CX�*�/�@��ل4d�-�ɵ�,yW�`X},2҄�iFeF��gWp?�4)��e�(`��h���X��"Ldm��!!�Y�NQ�Skͫ���	3iHF6sI&��'"͘LE3*3��yN�r?��qr�K�9dV����2�f�9h�z؉'r��5v���7�5&�d�3_s�V�-�Pf9h��4�2-�'O�n����o��"^��;1��C��.D.��q|��Ї8.��VMQ�6lv�n	AV�Ƃ;����C��og�ܣ�pi���c�`��{D�uۛ��i^.��.�d���~����:��J�&k�
\�ǝoݢ����2�D�S[�R��]��;��wV#�`{!Fؼ%@�[��;9�,��X(��8�ՆC��)Y�T'�T��^��?k\��ޑ��&�A�Q�����(�]{׫4A�dъF�v�Qtw��C!<��y���~�P\˦���
�P(���p��|怀�;���NV"Q�&^0`�.?�<���.J����d�M���'�f��;�����(I�,�3����|)%m�1�TG�]��^!����!����
��5�XE-�ar&��Cf�����89�Xɘ���/@����ğv�!%�Q�~��@���m��q��`_���V-��]^v��٧W���쐟��M�0�=����6�à�ͬ������c#�!���,�C�]�3��>)Dn,�Iaޗ}�Pgv���5�^��{v�Α���v*m�g��:�px���7�%Q���>'�.�=��=�{/�SgNT�둲�_y@p�_c@�"�c�p��_<�?����
endstream
endobj
79 0 obj
<</Filter /FlateDecode
/Length 4344>> stream
x��َ���}���L�} A iw��$���A�2`���T�YM����"ǻҬfj�]���.j҇�����f��)>{>��z��rl����^����������O0�O��o?L��o?_��AN?�'�g��8��)@^���_/�R��^���|�v��=	9�~���1��2���b���' ��%��- �����< d�8������n���w�P���X �K��W,��r	�\�#T8>9p��,G_gS�R�h&��.�g׉�LPbV��G���z����ĭ�[���`��o`�j�rF;BD��g�+6n��X��;ϓ���\�7�[a�f=I%�����fz�
���m܄��'�Tf<�:&��G;n����J��{�E�(R���B���X_�4T� �ZiAQ	�8�'f��p>��s8X U^�|%ЋW�ʺC��o?_����~���^����:%¼6�6ȍw�0�+B&´��¬��4|��ZWDB�N�*F�H�o�P%�D3TD��:�����.�z���D�0��M�W��H) �,t�01`Zr�z�Yc�����#��uk��L����� �_Qc���8%d��v!&R.'�T�%FG �YH�V\8"�Nx�~Q�D�����:�Ȣ�E���?_��!�M�/F��>PD������.0�}�vH�G��ȑBi�� A;S4RH�� a�H�E��E�0P [� [� =��"@�"�B�HoS�H��@�`���b#�E�(dR��Po)lS���!ޗ�H��J��s�����P�5N��@���m��[�	P�*N LC8��#l'��`��8��u�@��M��&�S	�C&��ԐҬ��*zj��Pbj�s�YD�s�(��U�So�ڡ^��H||�|x
�A�=(�1���91��
5�J�V�Z:���'�e�ð�y�J<1�����%���SO�u��D�i����K�� �9 �T�����0N?ݴ�3�r+��� ~.-�K�� 6@�
���\P>�<�0�|iA0jF? �{)1p��(0�yP���Õ0;׸��A�;w`�*��0e�^��(�*����(��Ș&x �g��o( :0eNi�x2���F'(�[����U0q�8z���( �Yk�E�4�`���P耙Q B��	$�d` �
��Q{Y�d�����!���0Qm���iU�mhr��f�	_jYL���F��(ay�у���`�-��q��͸[!=�!$p9+7 n���u�Yt�2ʫ�P�G�V(��P蘢ㅅUH����;PmC� a�%\��x�����Dat���]� ֳ�&L kb-!
����H��si8�*0��``4�[IF�+��Sd�P\Ew-]E͔j<��-���6�[y�7�:�9,a�D`��@a��p���)��r������f2D�B�m���R��XE�`��^�:��)D��&V�e������(Ȇ˧��B:��Ξ�-���ҭؕ]v�#SZ�*�R�;��ZABC��������e��5�w8��ˍ�Y�c�+�x;��|E�Ҧ�k�\T���ʑ����3��l(@d���	Q@#n�G-��!��2*�SO�3�g�Q���
�d��d[f�a��X�Ct�9���x��A�۲�?��?��䂇���§��St �N`GK���=����~m�ǂ��9$K�|t���
���9���*�,ym�]����v���X���O���l+.e�g�$��]3Z��3��5�� '��$^^^Wi�7�o�)�45�d5Q�N�N�U�{|y~`�]�=t����F�{�I�U%� �P�>�|���ӈ�s��#�`-"po��w�5�m�����I;�����
ʹ�&�D*��vH��~~Jn��ʩS�9&)�[��ǔ%�=�2��U�J�O�"H%3�DB�� Muz%H������r7B�V��wW�y"�'�G�Z�y9VQ��+d�}D!ss���$ߛ�sV�?Ʈ��[�v����C�"�]��������ظЀ�_r����|,x�E�C��7��������RϊIo��r�5�� A��i��[]�P��쭨Ti��k�)
�#��/����݉Ҿ30���S�J+����ΐ�p{ص�I��t�o1����o�Ol00�Ȫ��qQ�Oi�0����q�a˥�sl�(�V��4��}����JttHvr��^�{�R*��z'Wf���:�@��S�WC_��4HXnX���X=K�tgD�̂ޭ�'��z �*���ɩ8�'�M-����nA�&++,[0�����F���G�BE�I���yO�!�T��{��C�P�=���v88t�83$�}}�x�q�[B�����y�"r?Eg��2�%���f�X�;�uٌ�VR��d��7��-��Z�ZNOK�m�:wJ.z�`�E��	�R�xx�'���ćD
��dr&�~����Kbۃ9ku�^��e�&�㮛I�U/�����e44�W�tKFa�l��q~�x�
P��pp�׊Z�_��Ty���Rk�
���*�I��Yy�S��3P�y��o�1�f:�`�G����J���8°��D�.㣥�x}�3��}��b��y�s�Ɲ)���]��m	t��
ݰ�cҕt����1T��߃��U@�Z���G�Bt���%����ְG��٪��P�j��NBV�6߾��|��#�k�D]��#���ww�b|gd<-���x	A7�_B�����K�\7�ot��:�`��J��|Ψ�6��k-�u����xS��I��Gn�X'�u�� ���Y��5�I��ɎT�$��i���&���Q59��������2�/�����pR�V�h��۳�~���S�l�uϰ�J�C$�	'�p� �9���u��n�.�����U����];�U��9������C[�MN;���BoE׿%ݝ���o݅��̹f���u�(����5r%�%�}y��d�UQ�j�|�	{f�5��G/�� �x��_��4�/��M%+����Վ�0���
�޹9��|��Yi�����9��Ӷ^����m�*�Q6��ܧ�ئ��b6���f��;ٴƂ{�A鴵���(<im0lJ$��F[�+��6W(i.xH1��4�Igr᱁%i���*���My�66�iR�ה�"�	�f<�9��^xX�ѐ��sMOs�Җ�:���Z�U�VګT��h����d�P0h�m��B��Jz���g� �� ����^f<�<���9��H3s��f�
���d|�&xJ�pCP�1&��fd�b�[� ��Up���Ϭ,��׮i�����Ps�	q�t2K<�$��ط��jkw�����Bi3_��+��N	���tj1��+��/C8�53����a_C�;N�;�� G�ҘB��iW���=�O'�*��^�;����tO�b��M����6e�-Q\U��'���h��V�A����$	5��XV��9�c-'N���Î��9��ic��B�2I�$���Ó�RRf��dYY�.���Y�:�Ő���mdWȹ�1�͸�NWQT���(��Q�x�^T�6��{{�B�IϏ ܥv��Գ���4�.�U#�'�o��9t�u�	>o��{z� m/%�{��qjK�WZ�E0(Aa!�k-���&�.O�!R� �z����;4��7J�!ҝ!�@���5{,(���t��䈙�\����5��b@�u#[��+��=%�!��%�m�;/�����ft?#��
��t��/>[m�Ӄffئ_�dn��JS(�ΰ��F��o���Q��jEX�O"�)!1��G��MČ-��].�b*�L�,��1����L��H��4��V/���A��U1HK��O�i"�#W�밇�~�����q΋a,����[@�pDn�ۯ���p��c�bx�#�B��d���ʕc����봊��:����:�"�}<��A�5���J��BHX����^�!��e��3*N�I�H��t��IV�W5����=��]��R��o�35,?7������[�a�x`�w�(a].�wH�^�H�]�]����JJ���v�!=�gV`p�.�x[I�m�;k�C���W���g�v���ײ#t����5CcU��'��B��v|�C�.�M�P�em�%8J�r��vU��e?���4KB�)�Y��Eik�L���#�plE�1˱-�٣+����
����
�"8����ۑ���i5F8~X�[�د ۣ�dG#W��6(�=����?��4�R2�!���	�
endstream
endobj
81 0 obj
<</Filter /FlateDecode
/Length 4825>> stream
x��]ێ$7r}ﯨg���0��g��� � �wc����p���Ū��i�3*��T��;��dhQ:�?A���e0r�2�p���������q�V��?������7��"��s�5�����/������/��ԟ��"�R��_"����n������K�|�u�(�����/_y�W!������}q���?_Pa�5���E¼)�`s�� �;���:�V�E���r�׃�� rM���5�R���3BU��@.4�u�p�5)��zM�~q�-��O����߿�H���Ez�A�rQʒ�*���������ߠ���ҺEuߌ~����=����v[��Pb�mbt�_����/�aH�M$�N-�M�\��'t��̭�������5�#�"#ƑT$��R�bd��T�o����F�}^{�S�����"�V!���+"*Z_�$r�NG��P1�����}���W�����q���]2�s�ROaQNEd2Fߵv��{�l��V�4 �dP��-����5�YzI�π��έ�����,$��˘3v���h*�RR�ln\b�*?pΘw�ȭʈQ&eIF�H��3�E�_��&��*1A��ڌ)�.������ѐJ�hq}x��J(�p�M�s>QE��SE�>�e��X��^[�>����px��G��=RE����>���*(�灜���K�Т�dC� D�1J$L����m��b�	YE�����&VWM$,H�:KXvTPnBWQ"c)J��%J��!J��u	�
��e72�;�+�mp�&��{U�� m��������[�H��#$�Q"a��[)`,Z=D	=K�D¬��m��#_Sǃ�"
� �P�F�����j�(C�h���n��:h��R0_�M�s�PE�SE���e�^X���Z��}$e���#����S�@�x���Utp^l�c�E����\\EF�с�ut�1����	�FF��!a9:�5:�1:dM�v���G��d��Wv�G��LU>�sE��]���U/��U5��{t`�с���"a�E��
�zA��Ղ"a����jAA�[G����q=�� ���|1�z;�Q����Y��ܠ�w��#���o� �ú���n�g���%!�#$|���CHx8mpҊ#��u���֋
ƶ��H��#Y���1"j�YT0�^T0����cD�r��_k��Wc��a�͵�v]�D��젧4�ѥ�|���C��ї�^���jT`���?�F֋���	[/*��EE�V���mbDBW1�0�އL�f2���E�j�HW5J��!J����Z�`s@ Xg#�q��x�^ф�ӄ	^Rl��mz/?�:|�����~7a������*sY�)>l��>��9���6��C�D*��9ԫ��>�>�>�>R��/��?gܐ���L��(��Va�a��>�/IK��ׇ^����tQQ���$^�w��n跆����!�3�P��",�DW�T�0�RN/?+T��s"�'�HJ0���F7:e 0i�q0�f�Qz@�X#��ld�LO���q�U��)R$:�e��&ɰ�8�G��4R낂辍0�&h~��F"АA9�(�R�ʜ�	&b�7쁕Q)�
�RE&L�u�ګ��.�R`������j`���{ժ�����W�\��_C*&�a#\�&��+S����phH��FE�6Q*��$T�B	(bSH�����Cr�P��#v�J���0V/P��5��S��`{��Bn��(23��8���̔%a��Lrt�A�uAAn�^z��8�z-#I����X#�@E�׷*��=Io�O��J�VER�LX��DX5vQ5�c5ݍt55#h<��kU��Ȼp��4��\G���kl=��D`�#���D`b	���XI�z���x&�F��$��ߓ�R�d�Qx���>4uؐ��4�Xq/��ѥՋ�9p����4��Ο��b���m��Sv��.�t�9�Pk�i��*�=v?���D��� +��7F9���)��^];�b�/�7�s�˻H.+S}*���<��g���V�}�1>4EC���&��O�;�Q)�z�kN�޲xO��h��ג��N�B�rvOщ�H�Wk���ԧ�ٖ�rv(_�`ë��6T,	��,&��%uW��w����qm�����o�WK�	|v���!%��X�[�/�v�ʬxm�]m��ow�մ��egj��$bi6����3�$��n-�Kk�ү{Lu�I��v�Ie�)��z �jB�N�NZ�����e�Dб�e|�%j�g�8]urv�O>��}�z�Fl�K��a�s�֐���X�`r���ь��I;O-�6�
�s���l�4��������r�|Γ��Mρ�}���=�r��U�JP�OV"H'3�Bb��$Msz&��e����}ZV�T��݈��%��3�h�R�c}�}r��C��g$2��N�N��-�a����z�k��:y;ى�ڻ�{j��xi,w�U�h�`D�+:��X5�i�]V��d���C��wv�z����>��#(AQz�|����hu>�,�E����;������5�����S��̗��r�W�_.u����yuiLpns��J[gŎ�&#�XXS��M/��,��d7��^�'��Җ�tD����VO�aU��=#���|��B[�x���3C��j��*�[Q(�c�v=0;��^�5�������6:�vdE�>�5˞R
���`����!�L��Q���c��g]M�1��VP�3�sJl#H���-_�E�=Y��d~�#t5���S�Bih��à/-����c�;QG�M��_UXE:��E�����MͼuJS��d���8v�WMglQ�O�e�0�`!ǘŊA�>����诫��1���<��|fl�6�|���}���D��ė}��&� k_��e?�x1����8U��mw%4���N/�%���̄;,~sd��k S�v5w�b_i��D��Y%h=���f>��KWQ���)j�H̞�Q�͌i8��f�;��8�C<���T���I�4#����3����7b،��5���ԝ��6蔾?��)ٛ�j��=��ڣ9?��/�9S�恇桅{�j�)utqϼ��	v%J�V�C��F�#��������)��u*�]�����	��S��N�]��vw�Ȯ�����9�Z��L�x66gpf?�1fb�����jr��fkv������(���iB45��+�i�x�|�[K'vL����Cm{��י,�|�$2��ģL욠�7z[��y9�t3��N��͋����M	��hcr�Qx�(�~���񭖹�w�v̷���׍jH��"<�V8<��7�~�v��ͧ��]OZ�<�~n�bf1]��н���:qo�����'SG?����������w�����`:1O7HC�K����sr���Xd�����>���L9=@�4�>�o���g�z�>5�����!fY�t�٢p�op��L|���Q=�i0�N�O|��=6?�E��N��?�ڗXi����}��_�VU���b�{�p�˖���3+c�Xj�1�����P�P��K ��Oj��@u)��b(-� ��P#a�����úź�u%�8�RԫUt�{Y��� Y`Y�.�o#��D@Q�R=	,�AX*=1�� 4U��P��\�
bt�at�atT���E��F;XA��ma�X�u08�TC4�i�#�� ��|l�R ̐}k�u0�<aV�:��0:��0�}�$㴢A�>��
Y ���EV���B����`���HQ��&�P��T�BC�r��Q�0���(V���M}��3$�k���SY�bE?���oE�1�/%,�����Sp�p\+��^��ى�݀�)z�(�>���/'0!��v,�6,ͮ�3��O���^��:~;�uI�H����gM�����'Z��YP�����p޴��
��i��� �Hf�G�*�ce|Ԭ��y�aB/���0�]�L�w���6	�n}N�Q�o�^�o�e8�Z�RΊ��m�^����L_1�T"���JVJ���~*�f���S�j/�a_ � !�yk�
�M�r�NKz(�����Fzbp�R�����-��z����p�$�L09�Z��s�"U�~��n��[f�B�������3�z2�I�@K	7�:�$ܨ"�t6���8�����2������p�.J8X�$@����>��M�R���`��m�l�4W�7��޺�գ�<��7��en�k�nxZP��k�nH����o�0�?��i^:f����J��s���UÀ�]��^�ԙy�a�S�!�F�v~k���ݪZ�Z��3�i!�w��ɲoJA�dIӒ���5/�B��\暜q�֩����5�0��-[��%�:�Ln(�Ln�@�d�J&7ڡ<r�q�ڮ�PHY՝���A�7L�]��m�NQ eE凭a�"���5�0�o�0
6nw��{{PE��	�6��
�׬h�3�}ݛƝa-agP�����a�W���.Il��ҫM�dIsJH�z���:TH��{��>N/����Ny���p�w�ᾰ��>�q��a_�0�k��&�R0���@�p��}��0�o���t�!A]��t��������ѷ]�'�D)d5�������ݳj!s`��s#��=�kf�jO��v+�'���Y��
endstream
endobj
83 0 obj
<</Filter /FlateDecode
/Length 6212>> stream
x��][o��~ׯ8����X�%+ϻ1�?`��"�$�����H6�ͣ�<;#{4��N����K�7!}�sc���F>:�7Ͻw�_~<���ʱ���������o� �6n�Qkh?AA~ÿ���[��_{�ß��o��^�8��k@>�G�|{�ó��۷�BE�B~�v��}����ÿ3&�o���`��o� \����, n^��б�/���~��O��z�YB9�}#�k����O��s��'f�
�o�h4}i�riPj-�dOnO?{��%fؗ\�?��?87��?�ƭ�[�	��n��@M�v�v���H�O`����{l��y��x����r#u��4���>h���;~P�"�U��$O�T3�������v�r�n��ee@*��2c`�P��w&��P��sVZ�S�LlLI�|sXX Q^��$��O�ʺ����_y0ޖO���&%W�aD�F�j��ym�m7X0�+B&bZ��b�Xk(�ƃ����1BDD2o|#mD�4Z����������?��!��7`&՛(�י�H)��p#LKN9�5&�-�(�YFI����[C�0ɒ��~���-F,Ԙ�a)!ˇ��B��ĒJ����:�ՈG��	�W!��S�Iz�:�E?��=�^������p�����{p)�.�)n��-|��ߙ[��Bܐb�T�f?a$s�� ��~"`����' 5��H�'��	�t�'����~"����X����'ҧ�O$��a��Zlm��v&�����-�mڭ�|H�KB���J�������g@W?��o��F!��	Č��y�[?�Q
�5~1-lù��~B�đ�Q����@A�"t��u+.B~���Z��F����V	���(%拼P����EC{L!�[Uִf��ޚ�G��R���>���3�m;��C+ɔ�8���;8��X���Ӿ������;8��X����wX������;D��`��km�Zu&�Z~f����6�LY>��%!ҾY�M{q���Y����w�o�"��"`ݔ"`�w ���!`ݔ"`�wh7� l�RlpU�z�e>e�>4�<N)�J,�4Ol�ZM��CL�p^�D�9E������X�Czm�"��+!ÇS�p
N�w����Mr��(v��ڛ�9��A�O`��X�p��au�d��<�����g�!27F@׀��@�Yg@!wD/�D?$,�ó�0�P�����g�*PPA�^m�sKa�2�Q=�������3�&$�YQ& .Uh��K�*�PA���7(x�쭶d��p3�e�y	�G^�@#���Z
��ɍK��$�� �,�����k����N������^m���gSh�ho�����p�-�[E?IU���C���28�O���a��o� _�Ia�3��Љ�#a����q帐'>
�W�\fc�`46㓱U�͂�pL5U�6�i����KX�6pAY�@XM��R	�\E���V��^&T��@�q<̏2M��<�Z�^;b�%6�CW]H�H��Mf�U*�&�FH3Ew���dB8�����5eK[���:�Q�㍋!U���V��F/���l��1��2nf+�$�~c�O��{�ءn�����ɇ#�6�iڨ��8�@�P� 1�B�8�����ڀ�
<��u��0�N#������q��Ccaۃsb�כ`�˖�/{��x�d�n�ǟ��;`�@�ɉF^�e�����q� 'mX��ΗnZR6�P���a��޸���s��~-�ƃI���X�pl��'��2�kuW���>�Rg�W��eA��i��(q�k�E�7�g��O�pڢ 
�Q�Z�xޫ����!�2,[m�ڑZg��z�x�^�����k�瘾@�JB���+�l=�D�$S�8�I����0ȿ�7�-��7�ܼ�7����F&~xM�����ϩ��s�s|^=g�.�^'�o�0���Dm��wA��1����S�&\]��.2i4�O"����1^a�Z��y�ӵ��4y�`�co���/K�+����>N����%Hgs�����(��a<�u��t0&QN{�����-��_|�}�O��d�{Op�
8��������4�#x:û	)�'҄�l
XQOk��pu}��i�5hL
�:�F�SQ�ᵄ�G�q�Sm՟�\AMܾ�ܤ�� �y��S�	����QM��R�Ljo�p�*��1�-7���~��q����i�6�.�eA-�=ʄ�j�m\~;T7썁>.��8? ��kV.���Ty��%��D���|G!(���A�i��˓�����\�(�e�ta�Y�z�Ǫ́��1m{N��L{�Sj�Z珍�l�x�ٮR;�b�굍@����; ���9�CP��e�v�9����D`gFqq��f.���3{����q�t�d�ݼ��(�bD�&�e_�ᣝj�G���U���1��s��Փ�W��8�൓};
�F��(�I��6���w�-8Bp���CЋ�-�Fd��F�N���Ǡ|@��t����O�sj�is�eP� t�tϷ�<zT��[��mp}ܿCIt��TK�t��'��Z۹���O��L�l�K�=7[&%��2��9�׃��Ls�Ʋ��B<�j��t\�Q��{��}>3���[��㩡�Ȧ �B�!�8�����E Qv�G�c�y��?��]�2%wJ�2�&&I5�S���J�&�x�� C�ȗH6O�$G�챘f�N���5��!B�[^a�`��Vxݢ�,�h��X�l�v96{�u���?����U��1{XZ�3&o}V��T.qb�
�D�SS�լ'��A�֟�k��˝u���������_���B���F�3�:-��:��ܲ�:����`�8�2��Hs�:��|�X�`p����9��u����hE+#A�G���A�Ph�.��
�~�q��η�预�'���X¼wvp�j��5������.�Hg"�5��qX�qM��rU���xh_�#����c=�AZ<&����~�A�r�2Q�xL����b�����j(h.g���˙T9�C�8Cr� ��*iɥ̍Ka�\8��b�Ʌ�-5���4��4��5��4V���j�a�f�v)XDCs���(����$�Ҟ��{r�h�� ������fI2\�h2\Ei2\E�VJ;D��"��B;1���U��p�̲����&�k`���^�t8 �ѯ�9U����)#5e_j��H-IZ����U�H��L��h%���U2�Z�J��d�Q^K��͇�B��p_q�)*�6�u�:��e�`F�P'I�Ԃ9Z��ɓ$!.c�I��(M�#�Jj3Uy����J:����E��8Ph>g���e|�ia�YP[)�G�%v��oij���1Jaʃ�%��O�T���y�,=HڒWG��H2Q��<�Aߥ��자U�� �K�e���AhU�$Z)ܗ�9;Rod����&����,D�t�@���ج�̖ì�x�d!�Ɋ�e|*iY,�Q�#�VgY7��YT�N���[��d�����'��kiuʫ9������w������*��cW�1���祸X<�ͬ�=%�7�b�o%�$���,V�q�z��k�~���<h6oe��d�	>.��FJ�����b�,�p6b��~8���4�+1l���i� ��&�����x�q+Ӻ���+�y��+�ǓzX���8�`*E���}������'35"��S��)Kk|�P���ۊdR���k��R���y�����B�����Z�����W���"E���chW���BaÆ��e�"��u���FcK���jy���:ߎ�l���ܽ����q-�l�0?^Ɵ���.Of}�|y�Ꭽ�����9�3��,��b�=�uC��YM�Ljw/̰j��Ǡ�Xs�No��h��C��\���1���ũ~Z/��a�=���o�D�͜��:�3ќt����}�����u'^�	lw�C�J����kj@ŃvJ����<e&�瀇{<�;��#�sad.�:s��d>�z �Q�������S���i�O��>�&]w��4P�GI�g`�N���[Z>�1=�;����c$�e���m�E�SS[�����'ZO����삠�\���ij�$;a=�Ou�N�]����9��%&�C��4�#�� }�s�����z�0�u�Q�rG�2d]���9�4��R�ٶ�6����%�58��|f3�aO=I�e�pI��ҟ^�Z��e}d�{�����q�e˟W��~}��Y\:7����ϧߡ��B���w�.׻0&?���|H?��sW,���q!�t�d�׃�if�uc�tq페���WЭyUh<�G=���'pQx#7s;�T9�""Ѹ ���	K�ƥ�|�8uA�Vc��7��;|��ǨY�k��ߡ����Rΐ��,k=�>����e��+s\ϬᒰݳfR�aԎ���Ȭ��Ag\�f�t&�4>���q:�~N_(����{����F��+Yk�0?Xئ��ZA�ʅ�3o"^����"?�i�\�����Y�����6XQ���+|�8aBH�X6�	���a�8��3�L:�0LsTo̒�%̩P�n r)|B����@E�R��@.�T�4�|�㌡���E���mOo�y`�R�A�RrO9Лv�:���t��p*A&�0�JOo\�x+g.���J҈�*K³���ט�[S0PaۄK�Ekh��
W��e+s���yU�b�@#.��t+W��D\TJQ ���n����%�]�z�p��XA.N�C-+D0�MM�rH�:���~��%E��;e�n�u�����rp>[�%�x_����fK�׵}ǂ���;:�q~�`z@/��=֓_n�2��1�o��rG�Ԫ
��u�/o)�ot��֓�$)N[Y�_=���!K5��!��΁��� 0p�&�CL�f�Bh���u�b}h���!ڇv���bch�h�,�v.6HB��u�,J-$!�X�PFb���~�$L*R!�T�����I�����҇ٹp$���(3b��1m�9<��Ev�u�Bڙ.�C����X��!�Gv�e�.��_Q#`CdG�i���]�����acӬ��ĚNRd�������Ee��Ã�_e|�r=�.\�\_2�l�=>P������ne;����s�R�s���9b;>\b�j}8`�6٦g �x��\8`�����#V<�4��_�k���4G]R����L?ur�Q��D��̒��ʘ:�MՕ>.��������I1�o)�[�[��������;p�F.�����
�_Q���4f%��n�T�L͋,��/�m��xR�/:<r಼rv�*�s��W��I.޾8�T.��Z>��>m]��ty�m��w���Q�߫t9}c}&}�ƽ���Q�F�۟��z���6�z1� {�-��0pd�ѫ^ S���]��R��l�����B��c�53���T�^�S�z�Mm�^�C)��T��;��+ׁT�J�{��W�{rA��_�No(������yr?`���~����y*J��hUEm�*�RT�[H�VP9ܳ��z���LVQ�T�ވ�~E�K[���k�t�\�����W�xG��8��=N�f��ыy*J��!�˵6��rNCP�*��^��!,��w�0�<Up�J@�+��+��z�W� �	�^ɣ�o��W� ^2/ɕ<k��(����Ϫ ��5�ҩ�dw��+yN\r�:WΝ���7�ƗԳ�7�o_+�S~N���kL�N��\�2�E��bᢖ�����Y��{6������S,k��ÿ�����t�6��%-U�r�=/{b�E�Z���s ����/W1��,��Mw[p�Z������*�%t�,-gɳ鵶:[t�![{��H�e๮lqX��X���yy}�u*��Ѕ�#�Z�ҋm��N�W�K*���#޽N�X���t�ǖ�ܙ�j\E��!�'\���&�qG�-�����(���x��9QZz���O�T���}���t%���}������X�x=�__ﰊ�Q��:�$+����{�{�sG<��K��'%%܇ S{����D�
endstream
endobj
85 0 obj
<</Filter /FlateDecode
/Length 3594>> stream
x��\�n$�}���� K��"Xi%?'�X��;����d{F�i���֮����,�Ƈ�_��?�z��Lu�������}�#�%$[�?�u��_����elZ��'|�-��?.��z��ǰ��_�԰8�=u�#���?`ӛ���q���/�K�PL��������WkC����C��~^��(�� <݇s����:��vz�pZ�����ܕ� ~3��J~�b��[��O	��-�n2�����*o۰w+�}^�`���`7�����e��+.�$c-���}¸�h��=I�CqD�?���9��?��kqlj������1�}xk�3Ψ�S{Ȑ��H��!0bQ*X�A1����X�֏v6��#������jJ����-V$�(��t�>t�_u�Yno���]	��0p�ycc�P��e�B�TzK�Z��@�(�������HO&�1!9�Z�%a5�\��s㳯Q�IX
���!��R�V;׊��]T�!́1"!��\'kCN^��1�_T�#�{x}�;����F��ꗱ��m0Vc�`�A�jZ6�K�i�+97�51�m�l��7�dmuƂm���a4��iN\!F/�0*@FsH�Wqjx�CP	ᡏ
u��̉a"5s�)�S6W�qxG���E5�?�M� ���B��	����F
o��F
�)�tA����C�q�D�6�,�Hڲc�`�%�3K0�a	Ƽ/M �%�i�1p��C?�4��&V�i���h�=M4�0��K�2��.��]=YDo=�����kfԳT��s����݃�������'1hۉ'�1MVS�y"�t��%TS�N�1O����Ov���'�`l=�Xf���u(�nuЉ :<��*��F:�Ew5/��������L��gd����ݏj�_�>��1���C/N!��P�)�S�R����-Sv����)�2a��b�(�aGF�D��J돝(֧�(Vl�����c�)����h�L���=M�f=�V#N�tX{���/Ӽo�� Vx��?�![�`l��my���	�6<��O Z4G�3v��J0S��X�N��)�=L1�� ݪpS���J��.*ĕ�2�iԌ&TsK�Z���5[���ܾ$mx#�72x#�?9�tY�d��5�:�ع@���߅���*Z�Ñ`th����j&���m��8�_b������ao���8�K%�#!��G����S�+&���R9��4m҃!X�w��I0Pt����C�u'���;h�2���� ��d0q�r�J0�G�8�*ܔ@��%�M]1�m��A3M��ɻ!L��FW]�{�`��I0q�RBD�{2�(\) ���r�m(�P��	�ASE�ig�RT
���X6�y�5�����";Ѽz���@��j�@M勞�ǅ\�/�S�$�q�£�	m4�Q��)�&�<-��I���h��,�2�A����` R��`��M�k���f�۔@����ۮ.��3�t�(��3��0
6������cG�r�kt0mOEX�K*ņ
��_�הn͈l���M,��w��ڦ�J��=�ȭuv���S�6�⿸�DX�����ۯ��Kl��}\?��aE�Q�n}���صc�����
?4Y��8���Ϗ�����N���R��nRhC�}i5,�aksF����M�,�`e�(��ߊ!���՘ÀYG�su���ر0���0+,����g�*7=.�&snc�E�}������s�k���>������Rf4k��R�@n�e�l������`�E%��Y̴Ӭ!h���, _M�{I1��͊�w��9��ՂR���z�b�b��a���1�Ywv-�Qv��Wq?�M|y���ͳ˜վ��f�gVJڛY�Q��;�A����#�أ����|an�\?� J�<;͉;2�#w�t+��M��t�&)v��S�6ϲ�2˔�߯�1?��y&=g���l�}&��5<z-.|r�9�C���"��إw�o�w���L;�
I���N��/��פ���i�2�
��z|�_�0�/&����	�s�#p{Ԗ�xK���E�(e�P��dI�bUs�_�'>��
S4�(тFww3��WZ��#=���͎}Pٸ��+��t�U^d����GK]�A��X�c���XȪ��`08Ê�� �m �����dǧ�Rd p�A$ԕ�ʎ�UQDS-�*���,#�N�+X�8�ٔ�ו�Lg�ʃ"W.���ޜh��nS�\T��u���:���3Щ�3�Wn�(�@��Cr��ɸ:Q��Ɏ�Sp��1{�"mM��� �����攇Vc����[�R)4���3� o08j�b��u1Gw!uKJ&�TR^QH!F�*E��*c
+N��L��릖�S4`7�lcr��-�9�������T����4p[�x��.�o�X��I.q��A����T|}�ZR}[`���4�D���C?({���c	v	�`/�2ξ�c��u���M�E���ۢtV���wtSF�S�ҷ���Ɯ��f¶N"�D�E�����e��X�.�We=�S�!Z?W���H�S�|m~��x\O��WW��-淓q�Q�󷫹��e<�L#om���iiLgY�eO=�j���x�y���\W�6sfE��볪��7���
-�9�V���
".���Ac�9��MX�W�b0tcL�S����N��@U&2�Q)��H%7Cv�5֭��(����:�@_�A,`"�W�D�����)�B3��6�0�*��؜E	��(y_|!�״D�_�]�@t<G�IT�9�SK��S(�kMt��� fq�땲�B
�)����	��j�ؔ=tJ��}�;dIQ�@�͈�����!c�I��&D�w��(�Z8ؼ�1�Nveʙ�ƶ\����U��1�&Au����P��M�*�u�tODы2��0�3	��w��:l�}�R�f/����-�PfR߳vg��e�#�5�N��.������x{�ŧ�f^���<�k{�K i��S�"����-��Ӛy��P�&Qi����%$��\��J����-�h����t�\Jג^��!nϝx�ݫT̯��E˽��\�E�w��ARއ9n������OL��|�o�8���W�_���R.,J�Qq�
�N�C���,�ӧ G1]L���pGM*^X$,'�kW� �.�^~�ZØ޻�=ĩ�#�����+D��,�\X,+��9"gw�PV�Cd�)��D5��~�����ůQqy�g��k""�v` 'J4�*��dm��2���S��9�e�-���T��1��oN�z٪^��y"��\��Z�T��//l��V._w7�3��n���m�x#��G��m^���B��CP���Ԕ�`ܒ���.�����;�,ǋ�Ub��m��͛�~b�hT����o�{���KO�eN���~t1�o��e������
1��(�!�I�� �W���PZM��k�{�rך�ù8��O�I��l�޿)���r�4��K�t�vPM��x�
endstream
endobj
87 0 obj
<</Filter /FlateDecode
/Length 5414>> stream
x��]ێ9r}ﯨg���0L��}�W�?`�]��,�����!��R�4LkvF�'�d�F2r�c�s��O\#�(c�_~}���W&���"^���O��/��n��Q�{�����?���K��Ͽ=������K���/R*���5!��?����O�d.�����Q�P^�?|��^��|���_����.��������u!@�03���E¾)�`s�� �;����p+�d�@��� jDΔ�O��K=�'v�� /�\hts���[�R{k�grg����h���E`�����$�;�1��!��E)Kv�H��z궫�#(���?I� X��f���C�Ŏ��/�/�[A�C��^tP�^~-������a`�G�*\�����&a.
՞:^~��Az�R>^�1�,2bIE�tWJW����J��JKOm?�'=,H�N�hb�\�XQ���$��O�Ƈ���ן�<�����:���?̈��Vh����.NEd2f5�v��{�l�H�J�c2�ЅȈ��Aڌ��$��g@�U�VU�_��yF��M�3)HX���L)��P67.%�*��'�;W�VdDh~�ȑ��cx��������m.���EwI*NW�p��ŗ'0��8Q�� ì�v�M����}.4���i"����Yش��i��/O��n!\�����ɑ��ȓ�;�wg�����/w�%�(=8�z����!����bL3p����wH��6y��m�6�Ct��[�CB'�������
�&X�Dc탣UW2��+;8G�8��|`�!�����Y\�������p����;BBP�w`��S)`l�d,��;0f�8gl��VUY�(g���!�=D���!���!��hH�[4�N g�L���9�9QE�3���X�9�ƪ��U�0��
ޝ»Sxw
��աC4�t/ⴱ!,��M���^����	��D�16����E¦�E�V7���&��D�Y�D��D��k�h�}p4�J&N��N��6Ϊ*�|U�8K��q>W�༯���u��DR��'��	��	���v�Z$l�Z$l�	��a�ޡ���EB'G���(�Uu�bp�q0��- ��H�V�8k���hB��ӄ	��3��fn�#��{w������1��W%��?�j%Q�ۃ���Ԝ� �9��I8i��;F��!���k
������0�tJ�H�[EA4�$9�"?쨙������5����3���Q�gmGR;k	qByz
;�Hh<��Hq OiAb&x!�Bz�l|�h�R��]�_ԑ]i޷��<g(���X#�{���K�Y.L�@c<M��.�@ly~��DS0��^�Q�fzo�����D���;��>:�gƶ�֧�Uv|ϊf}%�Ѭo�5�i#o_�� cҘ����W �(�M�g���SI����+�ɍ���m�U��*(�r�IEݭ/���\l��p�>O�%3���9,	jQ�|��և�)���jdF��%;����AL���w�~y�}�J� �ۗ6����)�yKND��ea�[^��Iv=m�uP���h
�t��Q"�	�W��0M�HO�9��<��j{��#>,���d"�X�)욱�-Ko����}��[Wߟ;~C.�UBK����o�1�+�7�S��6&�߾��8>�����]�mb���}*mc[�s�_[�<&�N}�>n���KSdZ���O�<#���Kn��|ZNl�*���Zhi|�7�GL<��O(�ˌ��/]G[��~^@�����H��r�喰J[��eV��	K:�"Og�!E}�ަe��ݛ�=��N�"�*�t/���,��O��U�7�A^c�ø.F���h_�.u
\So�����I���_�v���n}���7й5���H��v}����e�����U���j����"f����}#-0����6WX�WuRyKna���.C�c�.��t����p~�v���������&W
=�e-�Q�E�m4�{4h�/�h����+��;"�L�J�������ȼ�-)��M��̏}j6U���0o�JJ�Dq�I�Ӄq��s�)��
��B��-D��6��x���6�3�V�NSD+�)�b^��@��� �ML+�r�1�������Vs��7�Z����2'�	��ӡ�$�A�#�~a'�]���ㆇ��l9MI;嵽>�-'Iڍ���b�(b�\܌�S�Vm%?|����E�a��1,`�v�`�|uu
��3�ϫ�k˸Ƴߒ/'A2�)\����0���5^�߷���@����f���=W�9I �X��@��L�#\p��!�Qk!-@ i�zpC��`u�������iس bv`L� ��"0XϠ��d0ѳ2�� V�`^���ˈʔ�a�_O��J��peH�hS��:��%� �S�0�u:�i�޾+����uMwʻIt�lj��(Q,s��H��� b�| �tH^��D��L �$!�K���5��ZB>�02����Y 1�0&s�����Z�d���V����A^[��Y�.D���9��!�CX�l��H<�]?dqԜ_���!̤�dq:�Y��b�W��0MwHO�2��S<���8����1^�[\{Z>p���m��Hu��{Y���m�Bd�^aF�n
���o��%%v��ƞa�J:J�D��+�?�НT^]�H�PH�����iӖڗ�=-������М��W�i�����d.�&əGQo��׶E4[�`c2Whv��js��V?`x��y�iS��d��u2YA��T?�!�+�,�5o"Dϣ<J��S�Fg�v��)U;�|4�MI^�.���d��O��{��<4Cx��G�KS\'�j������6�Ey��$�%�I��t���n�H^�ׄ9�6g�?��@X���of(���ѷ	����I��I�d<��`��A�(9��2`�{�hv����bh'�C�����C@�=A���զk�6l%52� H�'Ȁf�)��M:��h�!AF'�7y��-��.��+2"N�W�C�3K1Z�{��9'6�+�wu�����z��k�����Z*|�PD��[Ġ��7(o�N��u�o��*���D����p��&�}���Ib��@�	G���H*]a�DU�:,"a�{k�-'�g��a��#?�$�`�%�H�B�`F��J9��m3hcjL����iVxg��O�JӇ�/h4�����S�#�L�O�>wh|�x� ��^���8�=b��RF��Zˈ���X%c �Z�2�C��_����!�RF�R�9l�/�}XTX�HϦ���llG�@�`A��<B��+�B���L��#o\VTnܥ������"LMb���1d�4�H�eP��E�6f�w�[`�9�K���W�FC��IQ��W�s��v�MEì�ʊM�\�Q_�Oǯ��u58)�X31�ZoS�Cy�Jh�x���ݰ�����-�QG�����D��L�~ilm���/�XJS_0B,CA#@O�cqI?YB ��R��Fƨ������6��a�U��r��l���asc;v]
�իN2����ԗ�#D��<�ʈo�VM 	�p��^R;�^a�Z!��i)Z���t��:�M�\$E��t�B��d�?����j?��l8����}~KҖ	�����R̉�lPP���A�2��H��o���F���ϕ�(�ɉ�������H�}!����8W���:���QB�uf��P�ֺ)z��j\e�%E�z�����e��%#�.�P,��0�b�y�Ƶ5��P��LC�`�"��;�`�5�
}**E|T�1L�<b<S��qO�FH]�KEXTT�h!XPKF���Y	=G`A�aL�ț<�]B�T�3�U��`.!X�U{r��-T�\C�>�`Pr	�*݃�ʳ��b�y��`M��,RkV����`��w��6��7��\Y�Pk��mW�c��%hJ�y�@6o7���p�룶u����-���I2� �NlM� c�~�1�Դ
�U�1ޕ�cl]�W��U����78F�U �rm|�1��V�B�5�+�Z��_�<%�>�I|o�8i�/��	��*u��� C&o�a�.�z����e��u`T��h��r�I�z]��ª����[�~��0�`R����
僑꓅�Ic0{�,]��L*zf�iA�╅ ��#,[�ۉl��[��^�]Q��[_r�^������F�z�c/�����NN��ξ��S��Fùi�7Xn=o2��^qۻ�s?p?|��ߏ��yGwKCԪ�y�Z�ay%s�A�Τ]��Y�M`ͼ􅁴��R�f^�y�=U[{�'�v�gd��-�-r^�)6�"b�׈��%"V�,"Va��UX#b�"bB��X�5"�w�kD���*a�UPq���m��j/���0ԫ�aHX9���af�
��Uz�v9c�[5bQe�E��-��rkd��Id��+;��b���L���K~�15�5Q1��ʮq��U�v���-4���}����it��8l�ί��ĆI�N�⪃aֹ'^��u=�i�����nW��*+EYd ��W�F�?d4yw軍&�C���#�_�����l�w]%�rSTp�vj�b�Wۦ�F�7��ۿN�[T���o
~ۡ�ǔ�v`�a%�a�
Z>�!����y�L�#�xI���xYX*�x	Me��x	K����6�R��Jx	�U�P�KX.��ގa�nG�|��P��Ɓ2Y�
j�Px�x�",���2��"���E�8���@"*w���!~�-AN���*��������޾���u��t�vʻtϬh-�5�|�k(�U��ja�kY�lWy��^�����X�K�R�KX����ݎa�nG�b����>N/�E�zm'��v{Yn�v�a���N�_��s2V("�Q|(�j]BiA(ąG��Z�bc�nG�Z�WU�0MgAM�@:XLc�Ċ~�r��O����F�����33v��&����+OP���b��4��l�h&�9�~&9-<�X�,�����rM��KW�enO#?D��[Q���.yƷI��Eg5�ufG��I9a�B�}����|����b�$SUQ��_��_	�����fM	'}�}�tH/F�����[그̠cN�\1>�������mP�%�������B��/�Q�2>@~2}Fyd�|�xq��>)懚��ڏ�̹z�������j�o�@��F��)���$k��M�t��8�(�¾��!�����ƃ��9+��KRn��+�z��	���-���Yq��n�_G�T�s��W������H��m�,��dM����T����2�#��`Q�Y+�|�w.J�xm��&��k��*ģ�çq& ���
endstream
endobj
89 0 obj
<</Filter /FlateDecode
/Length 4271>> stream
x��\�n$���+�l`J�/�a���lk �ؒapH�����l�]�Ӥ�8�z]��\���˟M��w;\&���sN��ow�����%�Y����������W�ݮ�k�5���Ǐ[���/w?�h�_�W���nZ���\ŷ�t��/w?|v[޾�L	�f��6~3v����JY�����}��_&��[�X�8 �
���C����$��N?}y\p��nt� ��� fD���ޱj��
<q�S����Dn2�����[�S��������ya�2(̉��������i��ܦ�ߕ�Xٌ�����'�]�s�@�4~Ga�tڣ3���P৬[�9R_�/�;��v���۾�������q&FR&���7�n�uY�q��y�ʭ��:��)aߙ3�B��4����1
Kj��КFjc��h#9�aI[2鮜5)7,�čI�}�w��|'I�b�����.�8��j�V;����Y/钱�C���!�
�db2�-�u�!ƀj�L�SF;�c:�VdȪ�doF�ހg
Ft�Aƺ�k����;����l�A�Σ˾�_E%�h���M��yQ����ᚑ
�s�����]ǀf/�Ú�Au�LÍ+=�v���q�p!2n�P�BЁ �CT��D;�.i1��3�	yV�����~�<�z���������B*�.b�7bx#�7b���O������h�Sd�� �8�2E��s���0��@qAO�cl!
�N��`Q,#�w]��b�(��F�j"��a�.1bep��.&�@W�e��i���׌�Y*��|�~��������<Q��<Q��'*6�DŲ����g������L<Qљ'�OTl削�<Ѱ����D�@���%��[�9@�SDA,I���#+�H�;bL�2����G�V�Y~���h��<�p��A+�y���y�	F���y�b+O0'����3d% 
Þi?������4�V���L����E�B������)d��Sp71�$h�L�2���Y�q��a�)��g��o�0Zu��LAY�LL�Xh�.c�B�A�f���1o��:c�B��+SheN���S�`te������bf�~;�R��N���Bw�0�Ewȋn$̞nL�3�:fd�fn�#��E�7bx#�7b����S�Dc	Sh���zݫ�ؼWY�S��:-L�����K�֥F��F�֭ʊ�DQ�J�c'�z5EŦ8��R�b[�KQg�}���`���X{�g��T��3Xj�O<�Ⱥ�(ز�(غ� ЭK��-K����DA� ̯<Q��(��H�4Q�:M���&��H�W�8bs*!<�P�%'�� s�)!��損�;��Ë��L�H��H�OB
?]V���zG��M�$������o �s�f�ٔ��;�3WҐ��J'3kC��vm��\Ĥ=E'��3��][��G�f��G_��L��U	XCa�Ǭ#���Ls�tA '��8�,8M�'�����{R�@MqQ�N`7M��`ȇ	�4B��T��9�c�$icԦ*ܔ ��6GW4k�X�J�4$	��ݐ �+�ѡq&���� ��1���h׫��%u@�߹`F N0I�hFOIP>e�]�[V��鴜��s "0C�/���D��/�<�z%����NR$�X@;�o��꫅߀9�"qJRn�	=��21�Δ�C�L$J��L��YY?����v)4��p']ȵ�s��������i���eI�+����E]�iK �)��-���d�#�$ذ9v�}�c7�r��JC����%�g��'?96z&�:�Z1Y��B:�17��9>3 �i�t��0�1�7�C~�0�\xW��8#�>�t����q4E��O2R=Џ�����9��\��#�Si��HFӳS��i�L�jZ�_t��U��`]]EU�Q��J�}�&�Oh����7���<�pP��ݞ�2�̡.�W�i7Y2^rD��r����"��i��i�Z}��3��e�J�Y��.��\�s�#����|O�\�A�sr-d������P�s��7ϳ؉��8�O�TM�s��Ԉ���|����̝�^>�X�Thm��V��Kl���#}��g�6�se�4lu���H�\-)�\Ǒ�E�Kk�h��r�DP��ƻA߳��s�y=cV��DC뷋��������&>���G^+��?4=f�Ι�%�X]�������;f�4�_Z22�/�[�^��y���f�2��ȜM��i6u�<�C�F!�Z;w.
yx"��0�M l�&wl�?pN=�k|J�����q��̡�!���.����s�5*�^��!3`�C��i4=fo}:��9��ɹ%����z�>���]�sh��i�s����k?�����52����gx��H`ٙʵjQ�wE��<��o�֌?�nq����h/���27G-o���Rjܓ�/�_�\ߋܓ�Y�?Р������=%�b[�m�D$�D���N��R�j��RW���K�m��l�eZ����"�B�1\��*�"i����U�1��-��L_9=�8��I���C����+�v7�����t�N>'P���eM1��5�K��!�#��u.�Q=E�[��\k�>�p@��bv�M�9Dsd�'=xy���)2Vx"����=�mRz�Q�w|�E{=�5���>�5�k�Gp��"�S�g�Kŭ���<��)�Ks��d!�Ϥ9%g$u���q���UN�M�xS{8.��+�o�� Ǜ*z�St�Xy)�&3oj~�@k�N��;EX8��7��M��dP�SDNE	8�u'P�K;>̨٭�����(	�"����|�I(E\,�P]ӂ%�;��皂ⱦ��G���Ev	
��:=�$��qp��x����#{8��	,=���x�iŧM��3	U<��p����H���N@<��3�9����p�J�A9�]����ٰ�bD<δ<�3\�"CY~��La@*��SA��,�PZ4�����Sp8��X�2�sLh�]��M?��=]�G"��+���>�g��߹Ą= �W�C[dĶh��EƇ��-����P�o�Ƕ_�����U[��~� �-��6>��NgOz��D��к���OJo�1;ɶU_߰+��sݰ����j�; W��;�cs�gi���qu�W������(��?Q���\�*e#
��_З��������-#��|ER~��Mu/��!f��_KB���U����﫞g����s�~s#����?��YF��F��(I�%!W�N��[�jR#�@���ʿC��0A�c�
�t�l���1R�����Ѷ{;7��k�I\���T;�Z5JW��!_E��!��|%#�g�n�K홗*����ם��d��+R0�zb:]2��fǜd.;i�ο�S�H%�w$`�/�7�������w7K��T��"���� y���4F*�V����3ʈ=[>�ra�P�����|ެ����Ahu�]��,�{e������F����τ\pm>Jvo�^P��B�c�2������s���և}N�P��kÛQ��c�6g���Λjvnv�=�)+o���;�H%����[�~��O�G�k��|�L��gP�PAn�7�f�|_ky #�_�Jޟ�X����jp�ښ����ymZ�[-�ɗ�Ro��]ɻ���:��|�46��,o�x�$e�2){�9q�I t>��,ڍ���*�ρ����A�c�������F�fX~h���5���_q��d�뵞J���<��lZC�o�T<K�9�f��1��˦�9����Tr�����u����uZ&�]���~�\2�f�ܓ_kU!#�i�Q�b<�ȭ_�)�-�\*P����� VRB�a��(�0�V	LeV����TUa���87<g�y�4�N��W	�XQAhy�:oxƟ��T�Q#��y�`�A��Q���������P�U��f���b��aF}yk�(X���w��@%�&�\E�_���cwӎ��-�TQt����c���C��G�(L+��(h��z|M�'ml�
��nIp<����)��X@a�o҈(l��<8��'��	h/�2��)�@R� �Kშ(%�S��0�T8a��7�#N�h��١D����n�D��`CE���T71ЩnB�O�0�2�G|+�C����^�>V�}�t���J*��|+��g�X��J���G��?��o
endstream
endobj
91 0 obj
<</Filter /FlateDecode
/Length 2925>> stream
x��\Y�ܸ~�_�� ��} A�9<��d�� '�A0�����x%��v��b{�U���c���ґ~M~�0��`�e�a������W&�I[���q�������P�V�`����_~����r��'=��Z�G=I�.�3QM?����ˏof���ϰI('�g�����������O���.�����$x"�JЂa���DЕ`ӔX	&-��}[p+�d�Lr�LԂ�\J���^�%a0b$�
r
`���;���m��Kq����i��
�\f�~�z����Iz;X����[�w�Rî�G�(��&� �J�Y;�c�Qf���Z�O��&�J�fj��/��#�|0�Rd������\��:N�qv�^:ZO��k#�"Q��H��J�BT�T	߹<������L�S�0Z��i.��@�h}	��H��Ph����狋�>}�Ӭ�4m0R�E�ڒH��9�1wTp*&&Ҭ�_L�y��j��Jf�ɠB3"R��.v�F���*�����Ҋ�Ӭ�����L;�u���-�"A��fV6M�
�*�5'�w.�-ۈ�1���hv��q�M��������D��4��t}��0���HeU�8ƞa�
� \�aPg��=QM�vN5%�c��l7V�][������?1<�)��Q��L��{P��������ۊ�]����$a�"�"@�hTi@>�$G���0G�� F!=�R{����_@tP�ՒLk�_j��B����,�Y$�@�d ���1D�o����������@�=),g��@��	�� ���@� bV�e�fZ ��?Ԉ0�+��lR!�%咲Y�BeiH��i�yK�l�Bd�b�FEc���+�Os ������@�t�B���v.}'UF\�"g� %�F��5zP ���mr��
m�AWg���! "��=q��!ʨ����� ����.f�U*��C���Vv7X��Q��F!ȸ8�CܳRq��(1�03�3S��Lmf����H����i�bY�i0E۴f����*"M΁T,�(���uX��D��l~qcS=�	T}�D��U��P��-��l-$;��ßy��Z�Z�F}�Ġ�u����Su؋�:�W�h�f|����i�ؓ�?0 �R�.�<)틨��y�=�HV�y��!!bb� �$͒6�'�"�u�k��`|����Hg�/�����V��I�*v�!����r��+*�7�׮X'f4�&D�� .����B𣓬��
*��}����CW�}^"�˶B�'<�B��9�-�	�RX�dw1q���ڇ�b^q�Ϧ�'�
�"��`�+�-��eh�q� 2�����o�'i�y�*��q�R��&��l!J?:\Z�`*	�Z����3�#��u:JB�EL��*2�f�}�ܔ�q��-���mi&�� ����TB���	锠^R¢prx-!+O!���g�W�K��x������Y����5��|��'=�<�%\��uE��nz��~.9����y��Ē2Rl���G\��;���VhGP)�{�&�"2���D���T���]��[u�*om�IZ'f2e�2޼2�<��)kh�6���k��DA����֕�U��0��:@�S-vH
��9F����y���A<�[�Йcj�i���\�z :%2�6��"��D<}E���h�s�Ӭ�Z�j�{s����*5C$Ws�r�r�3��~i?2N�mi��jy��־��><���>_���8d<cG���Z/���A�W��o'�(*�9U�L����	v��9�S����5�w�u?p��|+,7Nn�֤��P�����%�R�(�G<j��G������5�h<�^��h����R���R��v����5L�&�57�ҠtgM�c�[1*̇2/���P)��!���GX6m����>�~��H]%��^d��{ѱ=4l�Yn٘�W_��������5N��vvF8�0�!'��Ƀ&�X�B���c�Q,ҕ[��؇Դ�F��,cjy�Fr����yc���í��Mםv��!mBfg�k(�:�*=�i�60��	m�&�Z�pP����N:���r*Y��P�!�@`�x��m8�;�ê\�N��9d�n��L7����fK���bg�z]���l7�	���K- �v�^N�ec�O�ww��LvY`�!�A�^�YP���C1��v��κ��zQmc/����A^���a�A��cn��
�x�X�|�� �-S���j���ٽ9��liq�f��<��q���#.�!���`z�l`�kqF?5:+�m���W��ᶃ� �N!���\�՛���t�#�QΨ�쎺�,�iV��Kۇ[������q� �Y�'��;N<�bo�\��*m�@�KJ�s.�^�s�7Ə��ӵ��"�[�ÝQ퇰��j�59�r�]1Aw6rS�~��I?|�`���z������4��(�N�F�q	�O,��2s.��r�QN�i^n�v_H�mX��3����[#k�U&S����c�~|�|�砧�ʰײ6?�*U��ͻ�_朚�QG	���i�Q�Y&�kЦgѠ]�[Ef�z���!Y����-���)ovI�+��B�\��x��z-g����;U)t}#��x�@�T�e��U�[���]
_���v��!m�R����~�b�y���K�(/�������Or���y��[��.!��k,ߞ;���vl����ձ�����
ٸsz���T>7�t�:��M���}'� f�薪���@�X�_��R�0t��ޫZ�n;��I]�p��=p�X�mm�ՙ������Ae��W�ɨ��2��<}�QJ5Ui�J�ͯD��h6��mn���I���L��*ɢ0�L�z3]�x����ؽ����Y���-��/�H
endstream
endobj
93 0 obj
<</Filter /FlateDecode
/Length 2864>> stream
x��\ێ�}ﯨ� ���<�}N2@>��n�������Ru�R�U��g��n�$��G�D�=�������L>:�gϽwӗ��_.�{���f~��_��i�/���4�q��t�~���)�����?�������B�p?	æ�4}z���&?���$�lzrz�z�3cR�ez�������9�@��@-6lHn΃@��]|�8������Ypg���.�����|�b�=�K�N�=C����lT�{CPko&��.�g׍�L\5�)��+|�r�����ĭ��LBh� ��T�+g�*��H�O\8���8�� �;��goa,����0�`���R��k� ���?(��%܃Un���$�*Ȍg��c�O_��㖛0w����{�"J�T8Lw!d�+�+�ߙ���Ad��8%��0������$3�agFymsK0[��ʺ,C��_.����?�RrU��ht��2����r��#�"f�LK�"��ku�x��	�>(�N�
"J$��7h�TI��K�A���r�c���i����ȸAf���Wقh)�,t�
2-,�<Ȭ1	��Q�zo&�%��̭���d)~9>A�bxR�(��a'!ˇ�!HiN��G%�#�	7�����Bu�y�"2s
�d���l,�!��D���/�czpS��Y!�	��{R���'�?TR��m�ػ@`g�AT8�f�*�$�E/ao�Q�*��l��P�wQ�f�aWa_AD�@�/��U�b��0�T4�fQP*� mT2 a,L���R1ٛYct� �)�4UB{g0�1LH��� ����,y��0�W?R"�SՄ2��(� ���&�Q
�I M��(;e�%L��� V)0c]�5(UO������^)Q}����&��L��g"ߪ`�5��X�	�G�܇XI #D��S�@88�9�y�F��p��ϖ!J&�.4U��NpY��6���·,F�YH!��f|ЀO�L q��|#v	 ��\4> $��B�MBK�	$q���RG@)��bP�*p�h�U(�y39��@��z�23V��0W�J�$�
ؤ
QS��T"MLo��\��T��-g�Y�U�����s=���%7�az�T���. ��5�J�����^�{?G�r�2xrݖ���<�+�X���޵]�ª#p�B�;��`r���]�[&�>�Mk�Fw�b�X����X&��	����q�{�I��ϰ��&��{��#�4	��#���.���=H	���H����Ǚ�ຏLk%�b��ř��g�����Q������%T+6{���0�@C�E,�W,�4��ՐZ@��sP��]�����إ%L�0N�uѲ�l�6��Ѳ�I�Dh=��7�I'� ϸ�[�=�\�,[�3#�^ݐY��Qvt[��v��T��H~q
��e?q<�-�:�A�E溕?C$p#�C�zuǢu�(�H�#j��l��38{����2�qVck!��p��6�Fp��M2�$^5�wp|�D'�ʑ�e9�������i����e��+˺BBnn����y�*����<��gX&��jȆɲfh,D�1�np~���jt��&\��[��#b��n��pN`�U�<+]���͊��A�¬��fEz}�13�ر�jl���xg�¸��c^ا�Aˎ�U1]�m�b�Pa���k�.���n�²������Y�~�Kڸ=LV�ܺ����=���a��p��a��Xk�J�v\%�خ3o�l|�VՕ�c2���#�]$��0J�\��	�>��K����B�ϩ��m)�<�N��5d���nw���������o	.SaϐQh�|��J����#���Uf�����iW5�Mxe�ܸ�ۨS������mT��Vf������/��S��I����O�vT����ʥ�do; �o���	�لM���
sA��Cut�bj�y��v���謵k�Ƽ	^���r2�nA��3��˄�k%D r*�s~Cz�nw�$�-[�Ȩ�,��e��; l��P�����V?��j����m�S���m�|�B�������-u��}�3��[5�wK�z���#O��էa����ug�� �r������{�m�������S�P'�[�p��7�~�{! |(�,�vqH�<�^����T7.a;��p��jJ��귻���ib�z�ˆZ�b#E�I�B�$�s���q܄�t�$A��5KH���K�Af�Q7BU�ye՘z��`W.����M�6.8�6 �6�F���Ҧew�7���5�N�:�*u�?J.�ޱ�]x�%�}�#�v��c�1�|j���*��:��U�ߊ�\�������T�c�a&˺f�t�%���	��.	��s.	Z��L�B�L��ZU�'޸�g�BH�y5'�,���e��%�o+�W)(�7|���D�7����]齍���M���n�P�^@yX�n�Τ-��Z��}�j�WK�8�J�����/O�d�p�k�K���;}X��;�jN���?�:Kuv�(���'�B��Sj�ԩ.�^A����WC�?FN����=��}bÌ�4_����&0�h�Iz�&����U)z$�����4�qw5dJ#���.�������U�y��֛�=�O\;���^u�Mq1�k�:Z�ʦ'����S�z2���'�^�Z��O�7j�%������yO�cG?���Ѕ��]�2��So��nd��4{��{���i�(+����u9ඟR�lM��.�S�o��A����e@I���4.�:�4~w�,�]���NK�Բ>�������LGȽ�?:�?'y�
endstream
endobj
95 0 obj
<</Filter /FlateDecode
/Length 3297>> stream
x��\�n�}���� �������I����`7���d�Ş�i�Lk��Z���^�N]YMyV:��I��O3{����1L_��~9���1i+���N����_��Y:��
�;�('�����ןO?��������QOR*����(��0����ë����,�8����R�I������Bh����?'���s�
K�Y|"�J�"��R&�����J0yї�uƭ����3Υ_n���%�#��K�$l��bT9 x�G{}6(��z��q�-�Uf�h�_��/')����L�V,V��hV�g� �"�b�>I-��vX�ɇ(����$�/̻$�J�fj���� #�w|c�Rd�����M��(T't���� �ti=f�q`��1�b�H��+���S%|��Ls��ڃ�
-HXN��hb��p����4�ő���hh�����E_߽�Yki�`�8�b�%��s���E��h�H���8H��{��v�J��dP���-���H5�Y���h�?��4�p�E�?��H�ډ��h�X�A�ECdN�hfe��"P�Y���+��5F71,�fg�G=Ѵ(�#�$���)J̤� M�IJ�7�'f u83$Z�Y۞�fe��p���:���D��yN���Üyc��ڪE��_N�������N��{P���?TP��h�U�tVj�IF#0a�?��D�^�&Q=+`��!���@��]�W"Ző 5
�ɰ�3
�:���<)؋!���2�(=��n�E�����(,�
��e8itl)- S0&.%({a{b�%�/�
�����
�6B8��'�I��8IZ�G���d�ijNB<��rDC��Dk�h�7�qN�~���l+v���&��\�H�M�JSu�Qa7�~�nPU�e�h���\�� �l21�gKY	�:RAF�� �D�B
���Q7��_�\�fI�ʃ��0�t����n#��lT�/Ɠ��T��G�v��g����Z�{?��H��aj!́�y�� cy��,�#did�hɸ�K�h9 �jc���3�O�`�T�uU3�;�)"^���-�����X:��v"K�G	���i m)û)�!�AJ��2A�
y�%��[�*Y�5�wL��X�`}cmХ��[0��.
��G���q{�SԾ_�L��,�u����+���F'`�� (�M'�%q{_��&疒=����XY^+xm��qf�3q> d�%���G�L�x�_��Us1����U��<kbn�u�Ǵ�v�L�;�I� r���?&���ݦO�\�<�Ƥy(�k�|��n^�3U�
�v�s���Z]�~.t_�3{�B�p��.{&(h7`b줟�����3�䨦��������2M����*�a��=�!I�*&�\p@X����bb�%k�Z�{�s��,������cL�W�iJ�~��,<�����|$���j;�`f�f($1�F��lK�,��5%�^�|�>5�&����t�nR��-�V�&I]|1͕��nA����lq^B��D2d��)���{&k�����W����hnv�;\��+S����k���mUi��� �r�j�b�/��k���e�%�i�qd����Dk�Y�^Bnb�[��F`\K��3򭒷��>�_�pr^@1�^��B����V�P�تP���aπJ~��h�j����L�-�V���-϶hY5M�x�"��\SG����d��y�%��n��s��A1ܖh�-ut�Q�RB�W�tG`P�Q���K���yb)�"m�k��[*Z�j��a�U�e�T�,\m�^�����.I�>�϶�tY"Қ����M��Z%q��	��!%%���\�Oaƒ҅ոikR�<bQ,Y=�5i�so"��0z=h	�j�������B���!x��K\;5�5�0�&?��R'/�H^"�,=nߺu�u �gN'n��ڬ.:,t��.�s�G�ޅi�N��4[g|�&�V�6�_b;�!�2Ĺ���zJ?�w'��DL'^.�Xv��1�Aѽ�,�YAl���=F��O��[���1���\�!�V�2��������OJ�M-^�k�
U�<n�X�{�+1L_9�	���^:�gh�j�w���9�Cڊ[��Gj�m
hJ��-�U-��t*��UO+Z>FK^ι�@�U�*@�<��ř���6�ҵ��u�c8N��m%��T/��m�e��\�<He�lȔGC��]ϒx��'�7&�^o|�X�ܪ�j�ږ���N��a���ҹ�ۄ�G�C_\�����Y�hAѕ�fH�v����a�G����.UUry���[�G�1�`�a@��T���2�z\ok���կm'�m��b�ɤ�P��+[%a(�|PLI{}1��u�t��.�!ƞRt��V�g�#������lu��	Q������C�nJ E����8��CQGtHj����x���ݦi{'�?�N��{�nʉ��(����p}D�����R�ޜ�_�:1���;P�ă�S�#	j(`䋕��mg�����&~D���u'j����t�)��Ǆ��j�е�G%�#O\6��\��^�sII�!n��w��A�n���7�ؼ!�~��ԇk���.^���łkwZ��1�r82CH*sa���UM�l�ׁ,tR�����п�T��DC�l>���GN�a����<Į�S�Q9r1�m	��ƅ-��X�yd�9']�;�a����]���
R��{�v��] d��M֭�&F�:���-8��}��������C��+GC����]�����q��y�r�89�4�·I�4����:P!�����H�2w��и����E3#�r�!�c��oT��>g�D([�A��Iz���������&��;ϒ�j��ס;�>�`�K�L;�z��q*��4t���1�{��z8�t;q�7���։�r¯�`|�.>.��[��z��JwD�?"��s�����+��,�4zXn���^(����W#n~��A������t�^:ܺ������{��N�~�����=�c��N#Z��Nʖ]��}�U��RkjI����I�v9cj��6,��ٮ�&����/�0 ��S��-��!]��z�W��&r�:��h�=���a�������FB��Y>�e�:ǋ���h1�-���N���N�7�͌U��k�����:U�S�;���w����z3S��[�����Qr�s���N��-۵q��{���'֕
endstream
endobj
97 0 obj
<</Filter /FlateDecode
/Length 3216>> stream
x��\ێ$�}ﯨ� [��vzf��d�|�:v����@H��X՗��V�dgܳ]���!E�Ԟ���gR��i���9�������~n\R��*O�����?M���u�[c�ay����q�o~���Ïv��e���18�υ����n}z;���<���d��6~2vz�z��R��ez��!��o?M@0iMpkB,��VB�<�օ`��!�\����<�^����:�1�E����;��k�&\���&�)��/������ʮ�]�3c������+��z�:�ܤQ��bh>��vF����I[������_�OY��a���N�0�Q������+]�b��0!Eg`*MxC�{5р?���L�O�<}��IG�|:���9����g��L8�P�a�����` �%әY9kR&ZH	`*��w�x'0�bb�~9���;^��j�oFJ�(V�iه��"��`i�i1���!���N�i:�ԕ��r�m#�����K��������u�� �G���ļ���Zv�A�� [�@��M��Z��F:*Ԝ�$t	4?����*�ۧP]5��ʄ<�.� �v$�U N,/���n��ɻO4	�i�>&t.��YGxm����/�axHS���/��{P���������Y$-`��d�꠳*}�O٫�Y�{#�BCE����N�`r ���~�����	T���zN)���?$D' ����>�F����F�a�h��Oy� 3d�P^,�1V�&B�q j�@]�E\�2�p"v���� 0��+!��	`"�B�G�U1I ��R�Ʃ�Y�)���i�(�5שh7�p�M!�f�<u�;��簄xD��E\��O8��O�2�\���FgW���HPKo
��U��i���<ܩ�_�ʝQWj�`Vih0���2&��x��A3r��L����D�u���&f�/�$bl
)���U�~�Ñ
�k[��B@��D0�D0����d���H�k�F��`h;Īn�ni�_L���Ur� 
�u=��ʮ˾�C-fLKJ/�Jըa=���Vc<ס���Ɯ���B���"?2��q��'6w|�ZP���	^N)}�:�{�W��֭Z+ �ء�,���-����/iv��i��dp��_ؤ�3���؀�"�{�� �]���ic`�$�5yRY���Tt�z}u��&7��'T�Ku �=��@���`�3AB���״+@�-�(�.&�F�5��Ic���޵�>v3,L�i}2?"э/4i1�S7K��Hc7`�濴F��<�������g�V��X���g(`Y?o�Ws�
���>.����;)���j��M�����]\_[���5Xƈh�xa[���.|3"�BƮ%�؊6F��R��a1*����:'Γ���eD<�`�2�ґ�gu4H1Bf+��JO�s��C�f��U�]\��G֛��r�}�z�S=Ś��:Z�{��jH�{v6����S�x��]�O������c9�z7=��W�KS�Ub�N�Y&~��]��(����mZ	,�iۯ�{�絏��O���]]/�ƶ�QZ|BpEY�-���l}����Q�R�h��TX/��r�G`Ι���i��V�o��ߖb�s}��5f�7��a^5Q���*"���q��.����.t�y�뜳�O��q��4��}2V�3�_��mGE��8B9s��y�-bּ��c��J�'��.Ǧ����*�ܘ!^gM���]���ޞ�#��j�Y]���LY)�{aL1˓j���k^s�fo��	J�η�@(�F{������fV�Wh���*�?�W��웘n�:v.Q�c��A߶��;�ըyk�b3O��,�dٵ��=�*�oOdF�������0�^���^oqF��;|Eԃ}���fy���x�		�����F>�HӰ������'[h�b�2?9�.4&Nm��ԁ�T��4ek{_tH���x��t����ι�+�(]r�/���0�kF�e(��5rA�iS�q*�x~a�f.����ku�Z,�OO�Y��\�0!��8��LJku�σ"���V�m����wy��ԩ:	�ٻKdю�y��$dx���R}	G9�z^8｀1޵�/602�U�i�q�/�?4��s{�8:��T�%FZHƕ�O���>�L�9X?
�~���E?欨wG27i%j�(�+�zr���z;���R���0_�dghK�lh��44�����t)M{H���eA�Q�Žf��n�n�0��w��G�ڧ� FhYv�Wr��|�dmbR?�a�������%&��J%/=`O7¤X�ͤ�Zv�ŜV�#6�d�#���b�1�AI�%�9�R�K��؉+��3�uۘ1q/�U��ϳnu��4Ώ��h!�g#R-g��Z��ΤM�T�4�.�������LH����Y��r<��G���s��Z>�b_ղ�w�P�Q������螤ֻ�.m��?w�傫$���Ƕ����΍�Y�G'�}��$�}~��zR���usc>�֢��Z�Rl!��ܓ��1Nt������i��Ş���'�}���HF��H�ND��/گ�h�Cg`H�
��R*z�[�[$��\�����!�tD�<!=���#���}��g*��7����xZ��m���K��ځ ~B�;�ݎ%R!�C�p?_�W܎�1��䜕�'�/7��J����~�(���T7Da����
h���mS����Mdm�a��w=[�F�s�ڜ�;|�g�2���Bn��d�.��'�K�(R�ڨZ �~F�����C�-��`q�H��S��}H����o3�j��bک��7�s-��e)��%��?�:�;E2��n���s;|��SzFv�ā��������`��@���c_�aF����Yљl�<�-��q����C����ϝƠc0��Ջ��v+�����У��%��])F��Ζ��ځd�1�4���m���6�]N'��K,�K̿��q.�$HJHOO����<�KmU�П�h_P\~��J�T�'?��m�1_P�g�b���H<��	]��C%��^�j�R����h#�=��m�ʺ�G|K�B�����q�y6R�Dگ%˻D�i���"�ovb��T������?��͗
endstream
endobj
99 0 obj
<</Filter /FlateDecode
/Length 2903>> stream
x��\�n$�}���� ۮ��f%?'�X�)���B֕��=]���5��Z+��H^�d�w҇����O3y��=��M_�O���}���f~��_��e����,���l����OS��_O?�$�_�γ^N����(��_`����5���8(H�'ig�Г����鯌I���������?O@nIPK�[���>��@����_*���.��z�Y"9�K&b��/%�\�Ԟ�%acŖ�����[2^WS�Q�n&��.�gׅ�L\�)�����Ĺ�~��#�B��
@���k��,�od�'.�fFC�:� �w�'�����߰�g6k�)����@�Mo�Ba:�pR�	X�M�@3����I?}�ݎ[n�y��V�B�!bE0�@Bf�#l��I;-���JJ4��813%��f������� .��u��~��z2ޖWo�j����)F�Z�H�ym�m�*�iZ�Qi�Xk���vLpE�Aw�U�"�+|�6R�4Z��O�!-[8���;��H�ډ�hFi*A�y�%��Q�B��I�@��R���pK��f"XM���z�I����*�'1�yn��x;)ˉ#�S����7��Յ�>�Չ�5&
D$r
�$��$�uH�+��z�7�7��0+��CBcAF���'��I��*)���l��L:�AV.<,z'�O\X�
k��BV��0���w��gf� *���"�������J��:DWx�E\�@u�vr�1�H�����R2�j+��!d b42�p���ڍV6! .�hT>��%��Q8"�#�o���ܰ;qB"�� b!���d�U ���NUY$�ׁ�T\M�3���v�h���.�M5"���_}����,�L�8���3��N( ��ŨĲ,%��q�"�݁j��ZD*`��-�(�6~�!&�pim�.���I����"=�B�pL���B`(8(݌
$@?��h� 0�|Ҩ�����H��۩nG� \؝8!��z"!=`�G&�W�K��H�+���B�i1A��g�
B���l¦X�����J߸N�s�O��n��fl�_����j)�C�$f��(\cA�t�׿����aw���H�_��M�z�/�1(�r���$��T� 	��^֥T�)	�.)��>`���$�9ǟ�Ɵ�iӗ-�;2�D�ځ���RE���	�ge�oȡ�3KZ�6m�(!�ҹ��x�j�U���FzR/�Twiݗ���Q��F���� $�|��&����,���kD/��~f�za�=�su�#��-�"�S��"��C0w0��� �A�nu�l��Ii�z�Phd��KI�Z$k��74�L�p���EEa�I��Z/��[�%^`Ϥ���*<��X�dk��/$������稄��ցBjj��'��]̦K�^d�]��C�r~G���(������ A-P���tB��/��,�^��� �J.�b ���y�VE3��146Lp��0\�e���m����;�	s	-���f�&���$^n�c�j{�&Tyr�sMC�i�
.%��n�K����%)Q�e��^W;�œ�;��U�����;%���=����]�A)�Dy��xD��FNzf��P��ut�q�ǁ�O�g�:�w5��'�en��m�y�C�@��)q9_-K�M+5��>Q�ư�D�rv���?���k�+��rY�Ye_���m�z�u@pN�y��19&}��q����{r��r�&G��8\�Ky:������x��� 7���}^�Ϙ w�Nq:\��s�
���� o�yT��܌�z�A�.�(ל@3�͂��~L�S]�99P��F��k�_��0
���� o�yP�W�C:5���� � t9���.���҃��W&�5�L�a!�1n��t湘;��cC��y��ñ<�.�8�B�u��vd]��&{��[����\rĈ��C�9N��<�p>g3PT2�0D.l�F�峟������ґa�c���@�n��v�%,+���x]��!��+�r:d
�*Bm��[?�N���:j�Ag�������Q)"]���Lq�V���.��B����)�>�\4쇌P��F���ѻ^�M�["����� �^r%��D��������{����Xw>�E��K ����%S�)ū_��Q�܀�Ql�{�����DZ��D��.曻KUjH^��B���W��g7��߻܅�ץ�Vw�{oŚ�$�ə�d��ا�T�.���C��Ec�tH��*rl�Hx:P'`e�_"�'��.w�[-��c�=�pl�ZKU!ſ�4��+���b�W�F�W�y�u�>�S������A�
0�y&��t8D~6�A���w#@*Sjkj��p��/�)�.�d琉��7��T�.u�Ǻ�{j�t��aE\Ujx�O�����v��[�����87��٭I�w�����Ճ/��?I�\%9�H�:wa$����Er�tH��*rl�Lx�@�NV+��&��.WP}=�r�=�@n�ڜ��X ,0i�\�W`rQRC=}��$U/E�ˍ��g�GU��C�D���Ye~�V���e�|A�����6�u�#�7%����܅(5�,k���W��b���kJ�W�D����F�.��z�3��$���2�ZeR^�?5��$�n�2D�\��5eT����*s��V�}��{�~��{z���@z���=��.]ɏ=a{�h��K�������qϗ�R�k��.|��c�h��K?���M�.E��50ū_�
�$Ec��袑�܅����'��K5����i�Nɽ��?���;�����t�uN���<�q���)����nV��8��ju[=/�eч�P�� �p��
endstream
endobj
101 0 obj
<</Filter /FlateDecode
/Length 3054>> stream
x��\�n�}�W�s ���֒��I����`7���oU=�-����-�S����pV�c�Z�����`�e�a�����	�W&�E[���q����ܬ�AS�G诠�\��_~Z��~9��^~�O�G�H��s�l�_@ӏ�O?��%.�����r�~�A*�(�|�z����i������?�}�
[��
|�&�"	��1�L�6w�M`�>�n�]��Y.�V��(�[��[l��z+��⒡*�%@�/�����Ro���n�׍�B]5�c��g���IJ�:�2��H+�Uycj��B���A��Z�m�* |���w�F�?�߹�PF7A�|-�����(�l
6p�V�6I�P���q�����ҥ�dX�Ɔ1B��q� 	e���2@#t��+==�Q��k�)� a8�
�U�E�B��
���ז`.��U���/��\����V����(qݢ!Q�s�S�"��T4�L�Y_��y��n��J�ɠ%ZD�h��hg�K�A���j�s����k��B��q���-H�h��R�U�ܹ8�dVy�y�y�J�J��4F��X�̮�;�$Ӣ��'IMNOIb�k7�t�x=1���HuT�8��a�Jn�0�3ϩ&Z�X�P�c1g�زê�e�����?qzK���B}�&H�(�O
�O
�O
�W��_G7-�g���*J�5zy�v_����Q纩B��q��܂�{�,5�FP ����,�?��S� �I{$<4v��ԃ�2 bL5�) ��G���j1-l b-
��).�������:/@*E[�x#�mU����	�\��w�2�z��Q �c�`� �+l����$�<RH�]�ׄ���&�������Lv"ȿ<!$jJ�1Υ��)P#!D3Ě�^�����d4Y�.:�:Ȣ�k]�}.���v����B�a~Q���M��fPy��w��V�6G�By�m�O�Ly�U��Sf>+U��}���E�Yx�E�"�z�@!��u!U �w��fE x1�x R��\��� �EUc�Eyz�k�"[��kM���Ғ�L�ȩ����m���10����P��Nf�)�;GX�,�ݹ΍���U����� |+�dąq�u\�<���w��?���߶�Un#���.s,�!;��ݲV�l�E��^����>�:��t��E�Â	H�B�t��
/�Ӣ�g9�@� �p@*���A�q=��K� ��N���9�G��l8�����'Ȥ�=�&|߄�Z�P��+�.r3�������ڮ��%�E����{.z~d}\E[���"���c׶��R�37�c�,�U ��Τ�b�l1;1��f��Tl2Y�����wW|x*�2��)~*�ko& ߿�`�`��0顰�~����<����0�������
�`bOv)�(<��捸c��ug�|�a/�@���qB�|�;�s����\��d�(���ʜ�ǟ���L*B5�T)ag���K�����S0t�	� `���C�!�L��5���!�`�q�����&�&߻V+ءr�r*���&*T(	�2�
#�PqJ���͒y�3��^zO?^���c��3B�X����%/�m)�^=M̙V�殦����`#��:������>�����{I�t������L����)[��1ng޸_5Y���/�Sh�o59�w�2�����<�_e��s��br^���%�.nNTs.��C�Plc�����7-���K6��%s~�9�s�����_��&L\nw�<�U\�)%ݜ���j�d�Ζ�o$�V�I�ޛ���}�Z���C��!�;M��h"'��=M<~C��h4m��]h�o�b����<�¦Y2��,	�H�|�t<W5�x/ʇ4B��K�0]�X[��N�}8C*o�l{ �88�8ڇtO�}z�v����y���tZT��9���4m���z�i� c�v��Y/pB-%��~>M\����� �Y���oU ��Ɠ?T��(��Ua5�
=������+g�'[|��ܝ�T��#��l�9F���TWƩ>��rz��i�3����+�H}_���=Ϧ�\A4�d���WR�}~���d�*W}PM�1�֯c*�9���4��UŊ�%�mHi�k%u����%�6�ʹ��V\吉����ɗ[;��g���0��������[=��G�v�;�x��x45'��r<~C�v"��x����[��Cx�ޑcy+���V�쎸U�Խ�V%�(�8ΊtO�z�.��⍜�D·sVd�<·� 6�M��y�`��˽Md�1�6m<����]���Md��{�6��������\���@c��X�7��g�9��1~ϧ���W��xXA�H�F̹���]o̿����qń��Cc.�̡l���>��2i���p�C&�ǳ=��`���|��P�����q>�[;�]��g{G99�����~<�4�&n�w�ݲ=d��l��P�����t��;r,��tYFĉw(q��Խ����B|�C�'�=�S����>�F�0�������	�N�f�!����o�mg�ϸ 湝8gcڈ@��ASq���o>����<g��{28ܧ��Ѫ�_E9����yEM�k�n:���V��G�T�qν���8��<�ZI��8�`C+��7�ө2�=��>	v�yϚ� ^�99����7o)�㌣�[;�z<kr8����,U��x����0ӎ�q�(Eͽ��dx�1P�7}�ہ/uoRwe�2	������}�G}���UaCO{��<O,Mx��%|�W�i�֤�^�[T�gm���V�Ekr�{��c�c�Z�O\����uyHӳf��i��]{��g�ùn���P�)������qS�Sw�$d:m�uo��V�Y���!��l�S5��Vl�ye�$U��j��<��
�U�����~��_!�m�K�~m�1�����͢9u�q�7��]&�~h��?V&[l��
2�OB�/b/��
endstream
endobj
103 0 obj
<</Filter /FlateDecode
/Length 3651>> stream
x���n#��]_�����Ʋ��I�&�O���?�*���e2�ؖ�y�ͪ"�����kb��i&o���޻����o'|.�c���O�����?L������6�о��|���<���z��g9���0��r�\� a�4���Oo��^�䧷_`��!�����BOBNo_OdL�?Mo�:x���	 �-j	�`@� p���< d��������m#���w�`��r���/1_�XR��p��%D��_��_�B���\��ğ]GF2q�������ۉs3�RGN+��ƨZ+g� �"�"�>q��p���T�y�4x�:���o�1�5��JN_�����Bt��r60Ж'�Tf<��~����܄񸛭Ćރ�$�2 "�.��0�G���I=-���JJ0�a813%��	f������斀.��u�z�_~9o˻w|7K�Um����:$¼6�6�$�AaZ�!a�Xk(������a�	W��ɼ����т�%�@~��aY±W����G���ȸf���W��) �,t�
0-,�<��1�o�G꽙/�gn�z�I����*�'	1��v��y?)͉"�Q�Ƒ�nD�
z��ʫM�)�$6FxN��H�Xm�"��/��{pS��^!���S��~8��+���ް��,<\��Ѡ�W��=�1�y/`�jv� �3�� :����@0��w�Q%@��s��a� ��p�
� e��疂Q����B�  �"�t2 z��!�h�SA�( �y�@��'p��{岚Ou���%�9Lt�	{�A�٩�`�(���5<Μ Z�o�UQG�2�xT�V��T��Z�z��%fo&<A��*�a�FV�؀9$��ڙ���>ʆCLc��>*h9x�`.0ZK��w����B䝚b�.�~E����W��P�.��1� ,�2p��JX3+���b%,8:�EC�����	h)_� 	�Y�~���wsp���D C�$8�n��#&�jgx����49Q�) �hX:�˵s����A�H��M����Ҥ�c�d^�ְ��[U~��Űi	��X����fi��`�2���@*�;����G5�����|���±f�0��c�_��5��]z���>�ۗgg�y�m���il�9�}�i��6�u�Z�<oP��<�K|��q�8��"�c-��/���Ӏ/�1Z�V�%mR{MD���ZME��������X��1�-ǵ#�(?+ltU=�xpl|֨��
�y���҇������BK����Z����ba+��6���Iib�2-[P��X�}�M�Qp0j(�,���E.��#�e��Dw0C{�t�]Fp�ީ��z=�5F+.@��񌯯��됄]',��u�W����b���)Lƽ�2F�!�.VU��W}Ë�lu���~���V�������EiU��)�e9[`��Шi�h�	PU.CwX�����-�b�#,F3G,F�d�D�I�I���b\Z��c�}����~�͛1S�֌�$������#M��.�v	����J|�zD��R�)6�٢�DY���� �0,�ł:]#��P�OÌ]`���a|���ڔ��^��.�̝]�N7_�A�`�9}9��;���{+�w��!ү?������LyI���Ndp�� ꉕ��q�{���0CaE&x�p(�yE��c��}���.�#F�0HZ>�%���lfwtZ�v���-��Nm�"+����TZE������˵+W�Z��EM(�S% ��ɘ+Y��\���s
Q�JH&~���_�9wh D43��nAJ�D�$�"�7a}�U/Y�
;y���"Q'eq���J���ffN+3����Ac�s�˲2*�$^m�5b�!�=����಼���lgxEP���XK��T��E�b�ZJlo�R�X�ي�S���Y-7��4o ��hӣ�[ݖ�NP�Sg
Lz5K�m�%�)�3w���Bd�J�P�(gL�_��<�J�RА(b�^úA2��z����V�|<uK�c�a�e�� |p5s��/Io�K�ymE]���edQ��`�j6D��ê\�f�Gt%�fY4��djV`Xk.�y��W�M��ZI|�7� �J��M��A�7R� ~C�=��zѷˋxwŋ��M����ǹ<����C��<�7u�.H��%\�����ו�#\�dջU��J��޹��	.��%~zN��Ŀ�J��@�ϛXn���9̛��G�U�X�&Ī�TS�<���������2F�L��K �F>|D6 }������fGT1y[|�إ��j��n=K(�=*�Q���uwۇxڳ�u�����ldC�v�N߶`��U����_ng��	��B�S됶<�G�������~�棿�b��n�1V��B��J�j(�z�a�m�%��U�:���d�D=]6��<�<AEd̆<9O@hJ	�_���D>#�p6`ME�T�9����&�MDpfT��^n�cY��J�:\o�2���i :CF�ߌ�6�T��* ι�4�XU���(άg�fw�i&��-�A�H��7���!�w���L�!nrĄ�@��C&zC*}���&}z�tR���9.�T%}jY��٤� PG�?�!Y�ѥ��s:9&��ݱ�׉�C^����!���lU��Ɲ�o?(Q}V�azH�<N�����Bסz/����3���n��97MΞ�DNy߰gD<��hE�� ӗ���Թ��y���=����`Ɵ�֊Ș\�$�ơ���J���\��-*n�e��0�)^C2"�!Ɍ+�u�05u���2s�[;����Ё�����c<B�1ނ��������(�Gn��V�F�]V$n*eX��cd���3�%�3u:tg������n�Ȓ��?��O��Q~>���Y�Ο2A�գ�l\!��PA�,۫ ����F��*<�M�rZ�������v��ܓ��ڥ�J�3���K�S�u>�s����I�TC��҃L��F�l�tY��݉��O�4�����,���%k����Jc�̚`5���η�`~W�m%�������-W%r;�0r<[F�l����T]�ƶ,��m,�˂�~�X�brt���yd�J�F	�
����6������/�c��+���#��6 o��Z�{4�T�.l3|:���@{)�d��Tmd����v��������@�JY��Zy��+��ɍAFXo�����@B1^����୳�V���;KN{͏�F�sV�-��("]����3�4��/�O/��g;zÚ����x��+g�Q�{�����dA�X�\�p$�9��$P�~�,���4���S�p$%2����p��n:D�Kq�Q;�����۬d�t-�����J��C�s9�Zk��Nuo�w�����<�s��?^	�%�����r�j�E7�\S-sp���M����u"��Vq{X��|�L�?P��'��Uć����_�tO]���9T���3�{+�r�,I�yg=8��h
�h�C6��UR:EZ_v��|͡i�����ʙK%
endstream
endobj
105 0 obj
<</Filter /FlateDecode
/Length 3829>> stream
x��]Y��~�_����} ������ȱce���Rų��3ÞeK�h%��S�$��:XU�f!}�51��a&/���޻���ӟ'|_(�&�������_�� ����Gm��}����������?��������B�t�
�G�7�����'5���W�(p�'ig�Г������������������ ܒ���$w~�A��C|!�8���6��Ypg	��.�E����K�\�<q�Q��� �s<~�<�ZG3�dw�?�̌d�"3wy�?���'��l�8"-4X� ��Q�V�hA�D������J�0���
�x�y2��[�����D�C�Y�H���9� `��/:�C
�������D�*Ќg�<Ǥ�>�h�-7a>�f+�A��aE�?Bf�#��I#-�����h��tbfJ
��8��0��O��$0���44����z�W��\Շ�b4�U�D����fq�A#�"l"MK�E�A�5�*��\|�ƝpD�H�o�F��F��@�)�?�e�QY�/'�<Rf�v"��Q�rh^e"�@T��qp(д�T�@��$�F�꽙�@�3���h�%�e����IJ��0a���,/^N�@��Đ������6�Մ�<�ԉ��'
D�s
������v��-�t��7�?��!��� �����������!�ieD�N�F	� �jj�2��j% ��m� * �/� Ii�b4��8D.��h��Fk@E�q"Pq"�&Q��q"�j�D�5v��l,�,��vb��$N�-E�ƯB�������N�i<?��#I�@h#��9�i�H�4�e)���H��e�@�:R u)�Q�H��u�@���	�VB�*�"�hCE~��R��Z]e��gf��q���{��8F��O�zZE��d��ݬG�������C��~�m~L�@���x�0Sh~|&� �q��x)T�� 2=�.9$@����_�(��q���=2�Hsg S"�֢��6h �d���LB�z3kTE"Sx���@����#B2��2D�ϋD�ZbD"�O��KK����Lu!�~����4�ƪ����ƃ��$�bMW�H4�͐"�+[GW�U��(?U���j U��AD�ۿ&��d2�JD@#p-	�8�����>�V�����a�hW���&���@�[�Q���K�FP�Ĵ
|B_ͫ ���1�L!��4 �,&���HfV���梑AX���F�D��08�
z/�:�z�\b ˫ l ����2��#��U�'		4����xZ���XX /a22k�,PtְR�K�����[�P6�]����/��/��ZO��3�VM��DY	Q"��/i�.��/��<����cn]��0H�4� p��%1�������Ys�0��p�<�M-m:�h�h����5�� �������� <�]�g(�{ưG���F�6��9o)$�h�-~]x;݅waS�9aZ4A��"�K�yV9��(����� (8��K���;S�8:l��,$�#�C�������$���]�'AV�+_#�MR$M�r���SL��U�gȭ`4�˵���5W�[6���
������<M��E?�+tqT�o��1�p^8�2��Z�a�1�^��̮0���ǋ��>Ī-���_D��>�{J)�L���Q���ї����´��k�W,C��tړ7���H`A����b�JH%�H|�c00��̃r�*$n]c��T�-�A��0��z�����P8�PP&�T:b���+FS�W�����i�l�� ���A�)�\��ˋ���Z�`];���ȌO� ۰z-�N�,bI9��1�!�ڈ�CC�#�����&��nIqCb��l\RH27��!I�+�u����@u��c�7�k��4%;��w���w�w!ٻ���{<��]�?h�x��n��Rm��3� ��]����<��{�U?A�Y7�|�A&w�������[]��o������u�xZ���Ji��{)�L���Tw�H+k�����sAڡ��Xi�)u%����d���ْ6P��:H�5��)�tF�X�S�v
��u�d�mTꕓ�+���#+u2ug�����g�	^�z쎥��2V�H�<K�u���uG�����Q��6vd�:ƪ9e!T�CC�W��9�լ��LeAI�(�����s)<kҏ�緡u@��+�]���ҹ#loF#�^�e�6�kw�*�U�F�J��=�Lf!ԅ�;oC�Oz&S~&Cd�)�h�N��������*�uS����L\�n�P�̱�i�W0��VX�w��Gt>���`�m���m����v!��ܖL�65u@O)�s��)�yM�{}���6�XE�����G�~��Z�ވ�VN2�!
ݎ5P*sFb��� lmHו�EL��$�|NW�*W�LI�͸�}� ���Y�bֵ����^�Ӏ�Ʀ��̌��Tf��5L���0H�x{3g�u�Xh�����h�_�A��jP9_���a~�!m���gxa[�0-��2pn��ŀdJ�f�ߞO���/���jKex̝Y�����j^���=��)^�
w:�%�v`���!,�T�u��uu��_t���}�����e�B�e����1�T	B=�v9��H~V�j���eTI��J�d�ZI.3�`�15���m�4ֵ��!��������u����~~��oa�V�f���C��?$&�VW�nl�9��|�Dw���a�t$�=۔r����!n��;~����M-d�M���8��e�t�d�ew��	ұ{H.��8w�<��J�lW�2���E�}�lN}�S������Z�}C�Ya��ݬ��[����Aw�j���fmX��L�:}mv3���ՙ�N_��
'��f��Cw3���fb�E�V��غ�m�l��UN#�HW71+��}g����a������4{XY������ �"Ӆ�+�m���=��y�Gשѣi��H�y�w��ɧ�	[W?�H3��T,����*��sZ�jvF>�p �Cu�c>�@����$R�vy��w����ι��:���h�n���X�����g����o&��������J��T���	�^rG�ǈ�6mg�;��}���(����a��$��램�9��Hu�^�~i���f)����N�ฏ;�������3����h�����ֈ'A�ū)��1�4�u��\�˯4�8�f��a�� �_m��J�0@�\,�s�?>~��9�uT���y���7\���3����K����!L�㍪�v�h6���kx��PM���G���'�t�A�&�#S��`���AŔ��{m�tڄ9����y]b䥳P3.d���J�����|�0�O��R����Kʯ�Q>_��G(�	)�_tz��:��7�C��8}b�U4N�֭��[~U�![�����3{�U\�
6�;�*��YY��@�!��S�����Y����������ur���M~�@��Q.qІ��ߗ�4�Q�R������\��v��������U/#U.<+�xʇ!G���t�0��T�Q��lP5?Z���߰�ܙf��U9i��a}���-̓
�1���ҿ "Mt��1�=	H]��s�^�T�9��3U�� �֜JX�Zʂ��T�R��TlcM?�O�(C��{H��V���e�]�Pg}4((����G�<��Į+@N�sW��,8�F��4Cs�z^� ��>w���}o�>`}H�� ������+��ߗ�K^2�/z�
�\�+�e�������
endstream
endobj
107 0 obj
<</Filter /FlateDecode
/Length 3535>> stream
x��\ێ�}���� n�~� �V�s��J� �5`���T�,V{wgFZ�4Rdm�i�źr�����k3���]<�`�jk-ۧ��'�܅b6M������~<�6�����������?~���v��g�����_�~��9��׆|�� ���?��S��v�+t�,���{.��������Wc|��v��S�������
������>�m��@�M�B����ӆGwgK�ۼ�A�j��u�֯�3o<g�+v+���l|�rk*�6~5w�߼l�7�2c���8Y�����f��.B�:�|�>8k���C��D�,$x����g�AʗjG�5C_���B��Z��Gz��o��KC܎&��o�C�R5n�U�}���f�zv�.㛵B�(D�,T�s�0�Ac�\��B�R���3�h`j��`��R��Ѭ3�	�	>ͅ0�|���)�<��i��~����K�jL)��S-�K�a&b��/1�r�9�y�Zw(x�����G����*�#|�NĦa� b�E���x8�����&�E,��,@�F�k���]�iF��f>�����y	�Z�&�PzN��y3"8#�h�a�qlX�ڵ$����$s�^��D�ʬcd~��"�iF2�y�0�I�~ș����&)>�v)���?���$Q��?����
�x�F7j�Q�wH�\��=$c�+BqW�bё�+�Aj��#� ���+
��`�k����9��t� KP��*]��a�*��D�ISE�T"�.U���Ur3U��r�i�����7����vi�h�	E1EprCq�)0��) 90b+S VC�L��=0b+S vd
DW�H���#S �"�M���I�A�.3i�*S����I�����\癋� ��!W�*c��z��Ⱥ�(�*�JB�h�F7Z�^h���CQ;y"9��D����@l�j ��V��BjxI��d�� [i"YH��M V�3��DW�hX���#�D�4�1���K��8x�M����tT�дUQ����NT5:���y�EU����gK`�5K r`	�V�@��9�K ��bG�@te��%��.,����,�O�%��f	z]&R�U�2��+M��"�iB2�y�(�G�tȗ����)<�l)��ȯR7V���V�|�Pjd��9/4q=�b+M v<��9.4��J��4�s8�1[�����4ѰN�G����i�c*G�*a��*�����tT�дUU����NTE:���y�E����$��M`�5M r�	�V�@�pFYj���&�Ϋ�#��[hQ�R�eo�4��q���zFٰ��4y�?h���e&Q�2�� ��d�Hb��Lv���
r��r�����OP|d�RE�_�n�p��-|/��˥�/��O��U��1Y�e�(0l�0����������^d`a�~�jl#��t�	R+��$pA��m����
dHh#v +��=W�	�0��� ����5@uw�Te���	#�ORq�9+��,�g�΃��n�)���?�s �˖@d`&��>�ar�f76@��K.Ԇ��w,6O���ؐ+�-{����Hk8�l7G��w��3�g�Y�O�-�G�9�7��l�ЬEz7q7�B�[HbFbjC%Ytd���pd,�k�V�7���*��/vG8�)�������4��\��/&pK��_�����I$q��u�d�+�-ʩ,��v�\�p�v��5��	C��/H���%@7@�����9$����ڛcf�8��<fYMG�YVӛ�%9]0��L�qFsN��yBt������ W���o���5�Ԥ���W�0�~�-|����w��o����w�!�#�$b"𿙗����?�~ER=�M���6�fpQY����GC+b�g�
BmB�a���u��i��z�Jo�+�����^��p�k�)U3�Y���x���!���->}�Ҹ@�&S}��mi��W;O�e������d@�GEP�V����c8��<�ĖW0�Y�-�,�>���(�*�8���ٴ�U�X��r86�s�PH%�oQC1�݆��P�����!Ƙ��qy�k8,?md^�	���0��c}������fa�Y���$�} u��Aa ��)^�j���RUЭ����E�$�l�.B����.��E�I]�m��<GIZ��d�9�<�c�uQBCꢘ�N��Z�J�FX}MN���7&!�(� ����QL��+/��YꢎHU4�L}!��JD05�0uj1���h�R��F��lW��;�����vP�.*�9-!%���m��]�M�.X�Er��z�D1�'��0�uȐo���dvZe���Pw��u0�������}����X%<��͟�=~���Ib*gu^V:)^��ƹ��أݘ�XO/[3U�X4_�!�����E���A0��d����h����Fv�'O��y�J��VD�h3q���sȏұ���ŵWڌFE�����|�d5�Q9���f�W�x'���^���<�|.�#�<����C	�/��e���Oj��������5�=�UVX��!�<�c��G��S��`50!�f�B�	K�t�6�7�&��)�WrT��
�]���X�S��BfSj�B"�w�ڿ��C�D�T���8��AĹ�4H���⬔�y̝�LDM�/2(ɏ�R�٣�B�߽�B��kB]�"H���4I�Jq R*HjEj6E��{�3e�r�\>@��pz@�Er�����������d��#�j��#�0U�VB2Z�U[R��D�G�|��Y���h>O1�8|ީl�Qa�L�9�C�|C	��0x;	�c^$!� i�i��Ł�����Dtմzn�BF��t��Js�#��1в�L�X�і���.=�{V�Cy�jKO��#QE"�Y$�UC�QH�"l�U��fE"�Ha^jJ�f�9*��eqH�7U]�>�/|�H��h�Ǽ�>��j��M���m_b�v��]_�go�h��#a��f���k�8��r[l�^� ���j_��_��I֋�?!���a�h�S<ުP��w�R�� 'ʻ!�f�����D�ă�-����Zc��/�����T�E�<����8��-��\n7�!rk2����9=�׬�uw=hFt�ϻy����Ti��?}qz�����Lr�~s+�>[6?S���V�~�!�$��v������}Oi�1��	s�!1?Z�X���2TP�JK�U�L��� �u���� �f:�/8�/n��`6�=����ޛ�y#f�۝�۱�;��-��R�� �����\��j�S�Rl��9����`:��/]�����E�v6��!8V��*-��&�f�7��D��E�e���i0�׾g��/��`��!��S�xݵX��0���f��*�J�R�Zx؏�	��N��k�Uo<6�l��=��+OȒC>���T.��pq���|���'?�������k�B<$�t�&���Ѳ�ZS'�������
endstream
endobj
2 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F6 6 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 7 0 R
/StructParents 0
/Parent 108 0 R>>
endobj
8 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R>>
/XObject <</X10 10 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F6 6 0 R
/F9 9 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 12 0 R
/StructParents 1
/Parent 108 0 R>>
endobj
13 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F6 6 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 17 0 R
/StructParents 2
/Parent 108 0 R>>
endobj
18 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F9 9 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 19 0 R
/StructParents 3
/Parent 108 0 R>>
endobj
20 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F6 6 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 21 0 R
/StructParents 4
/Parent 108 0 R>>
endobj
22 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 23 0 R
/StructParents 5
/Parent 108 0 R>>
endobj
24 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F6 6 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 25 0 R
/StructParents 6
/Parent 108 0 R>>
endobj
26 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 27 0 R
/StructParents 7
/Parent 108 0 R>>
endobj
28 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 29 0 R
/StructParents 8
/Parent 109 0 R>>
endobj
30 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 31 0 R
/StructParents 9
/Parent 109 0 R>>
endobj
32 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 33 0 R
/StructParents 10
/Parent 109 0 R>>
endobj
34 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F6 6 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 35 0 R
/StructParents 11
/Parent 109 0 R>>
endobj
36 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F6 6 0 R
/F9 9 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 37 0 R
/StructParents 12
/Parent 109 0 R>>
endobj
38 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 39 0 R
/StructParents 13
/Parent 109 0 R>>
endobj
40 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F6 6 0 R
/F9 9 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 41 0 R
/StructParents 14
/Parent 109 0 R>>
endobj
42 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F6 6 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 43 0 R
/StructParents 15
/Parent 109 0 R>>
endobj
44 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 45 0 R
/StructParents 16
/Parent 110 0 R>>
endobj
46 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F6 6 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 47 0 R
/StructParents 17
/Parent 110 0 R>>
endobj
48 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F6 6 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 49 0 R
/StructParents 18
/Parent 110 0 R>>
endobj
50 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 51 0 R
/StructParents 19
/Parent 110 0 R>>
endobj
52 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 53 0 R
/StructParents 20
/Parent 110 0 R>>
endobj
54 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F6 6 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 55 0 R
/StructParents 21
/Parent 110 0 R>>
endobj
56 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 57 0 R
/StructParents 22
/Parent 110 0 R>>
endobj
58 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 59 0 R
/StructParents 23
/Parent 110 0 R>>
endobj
60 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F6 6 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 61 0 R
/StructParents 24
/Parent 111 0 R>>
endobj
62 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F6 6 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 63 0 R
/StructParents 25
/Parent 111 0 R>>
endobj
64 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 65 0 R
/StructParents 26
/Parent 111 0 R>>
endobj
66 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 67 0 R
/StructParents 27
/Parent 111 0 R>>
endobj
68 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 69 0 R
/StructParents 28
/Parent 111 0 R>>
endobj
70 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 71 0 R
/StructParents 29
/Parent 111 0 R>>
endobj
72 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 73 0 R
/StructParents 30
/Parent 111 0 R>>
endobj
74 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F6 6 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 75 0 R
/StructParents 31
/Parent 111 0 R>>
endobj
76 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 77 0 R
/StructParents 32
/Parent 112 0 R>>
endobj
78 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F6 6 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 79 0 R
/StructParents 33
/Parent 112 0 R>>
endobj
80 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 81 0 R
/StructParents 34
/Parent 112 0 R>>
endobj
82 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F6 6 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 83 0 R
/StructParents 35
/Parent 112 0 R>>
endobj
84 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 85 0 R
/StructParents 36
/Parent 112 0 R>>
endobj
86 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 87 0 R
/StructParents 37
/Parent 112 0 R>>
endobj
88 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 89 0 R
/StructParents 38
/Parent 112 0 R>>
endobj
90 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 91 0 R
/StructParents 39
/Parent 112 0 R>>
endobj
92 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 93 0 R
/StructParents 40
/Parent 113 0 R>>
endobj
94 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 95 0 R
/StructParents 41
/Parent 113 0 R>>
endobj
96 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 97 0 R
/StructParents 42
/Parent 113 0 R>>
endobj
98 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 99 0 R
/StructParents 43
/Parent 113 0 R>>
endobj
100 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 101 0 R
/StructParents 44
/Parent 113 0 R>>
endobj
102 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 103 0 R
/StructParents 45
/Parent 113 0 R>>
endobj
104 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 105 0 R
/StructParents 46
/Parent 113 0 R>>
endobj
106 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 107 0 R
/StructParents 47
/Parent 113 0 R>>
endobj
108 0 obj
<</Type /Pages
/Count 8
/Kids [2 0 R 8 0 R 13 0 R 18 0 R 20 0 R 22 0 R 24 0 R 26 0 R]
/Parent 114 0 R>>
endobj
109 0 obj
<</Type /Pages
/Count 8
/Kids [28 0 R 30 0 R 32 0 R 34 0 R 36 0 R 38 0 R 40 0 R 42 0 R]
/Parent 114 0 R>>
endobj
110 0 obj
<</Type /Pages
/Count 8
/Kids [44 0 R 46 0 R 48 0 R 50 0 R 52 0 R 54 0 R 56 0 R 58 0 R]
/Parent 114 0 R>>
endobj
111 0 obj
<</Type /Pages
/Count 8
/Kids [60 0 R 62 0 R 64 0 R 66 0 R 68 0 R 70 0 R 72 0 R 74 0 R]
/Parent 114 0 R>>
endobj
112 0 obj
<</Type /Pages
/Count 8
/Kids [76 0 R 78 0 R 80 0 R 82 0 R 84 0 R 86 0 R 88 0 R 90 0 R]
/Parent 114 0 R>>
endobj
113 0 obj
<</Type /Pages
/Count 8
/Kids [92 0 R 94 0 R 96 0 R 98 0 R 100 0 R 102 0 R 104 0 R 106 0 R]
/Parent 114 0 R>>
endobj
114 0 obj
<</Type /Pages
/Count 48
/Kids [108 0 R 109 0 R 110 0 R 111 0 R 112 0 R 113 0 R]>>
endobj
115 0 obj
<</Type /Catalog
/Pages 114 0 R>>
endobj
116 0 obj
<</Length1 8900
/Filter /FlateDecode
/Length 5837>> stream
x��Y{\Tվ����{��030 ��Ǡ���Hj�2T"�0Q@0��L��I����<t2���#3#ˈ{:)���iٛ�q-aq{3�V����~�^��ߵ�o���=�o��  �� F�L���ū�0����2�	��T��z��>����@ɡ�ԙs3��#�|��=g-p@n� *7Q��?k��~E�T�'ge�B	�;�l�5gI��ySo�Y`����i��YO�Q��?�*�{�� ��S96g�Ź�}VQY���9y33v~]�����s3�K�u�B�Q�1/cn���?|��) �����m�0 |�ڞ_������� dU&U��m����/��n�|�-F�>�db�=�����S�F���t�Y���0_�[��t�*����7�~��_0p���ήݤfy0ē]K`l��`T�.�����s�&�_�3_�☋ecX*����l6���l#�`��v��co��ٗ�Gι/�q�Ň�1<����|6���J��W�}�?���d�W>孔�)���Jy�6Gnڥ�mL��n�c����Xc2�	U��3���#|�����	���''{�I����^�<�I^|�pJ;6��q�i��y�T/���^<�p�1��J��)_%y���X�����g5�Ox��'<Ջh���ǳN����y�B��{q��^��p�/&<Ë����K	gz�2�Y^��p�� <ˋW���U�s�x5��^\�*��p��c��@1�Ӛ�^{���Z&='<ы#�-���h�����K8͋�N��t��x���7U�K�6�M�m�B�3�A7B[���%�
�磹���X'��_ќ�9�Is\���IsZ��&��5��Ds�&���FC��j4;�挆6�T���o�����~z߯��1�8��;�~��K7s4����Ѝ�|@�G��i�7گ���ћ� ��N������CP{{[n����r;��ӯCm!�ђ��HTG�~	u��#v��;_m!�G-���;�PJܔ��t��?�n�.S%�MGM���<�<l���
��YK�NL4�$��e
3��"M}L}MSM�&�fL�e[A��'ȏR1�����l�O3��!�%�%�Փ�="�m��l��v)s��Ӂ�}���Ć��~��� X�W[��M�����)�UP�Q)[�@=xx���T��gx/�;���,�z������x�t���s�c��A�Ni���4Q��>�`�T(5HӥB����T��A�2�y"��} �p��<%�|�l�*��FQ���28 �h.6���2>�j^�h�y�����4�l4�N��(��I�z��`
�3&�l��+ī���B��if�{P͞ƚ���c/�QK��*9�ju6%�FQ5v��Ět���>��ﰵR�tXe���PF�w�}t�l	ɮ�e*w�H�Ϊ�i�2�x��JDc>�'�D�p��"��d����4S�5�1R�O�$5@&�lB�h��^Xe�I�W7@��zVJ�H�2���8�C�t�tM.A{8St���AO���;GgV�'�9^�ի篊�⨆�j�Gm[[r�&O������WKΘK���R��c��խ#�{���>��&�TKTM�#�km�ղ��FO�v��ql�l��ђ5�W�_끓窾���?L���"��^�|�B�U)�~��h����I�י~����tP[y|Z�p���~C~�H-FÅ��_�x_{�e��dû���՛-*�l� ɩ@��$]�u��WQ(�Sw��/X.6]l��FY�Q֨l	Z
1��Q����}��;����# �����,�%K���? !0��P�ؖ�k贊��m�P:��PL�{�X���}���6œ�����'G���U�?Uɍ?�Ug]���TF���@�;@�����s�������`��:��W�,W�Y4�Z�\�V���b��_������Ǯ3��v����r�h�Sn��X?���b�(�l[�-�.u�����nw`z$���:;B$�\[헒v���'7յ��uUU(	H�=�~Oe��	֨�(�ƈGY�klLˁ*�pT���*b@+HC�a��kHhۭ�VY��,�[6{l�ER�93ڻXPni[�2�:(e��j[�T�	��8��z���w67�[��U�-�.�hnn�=R���,���Ea�!
��)��}���-��1=�$�$��~�Y�!�IB$��CYb���h��8�%��@�N��[Ƒ2�zb��/���9���"�VUU-b��>2zQE���u}~������+����]H�w�|wo0�3D�sx��v����S����{�= �b�sX�h�4身JJ�ߠ�O
��DR���t���&˧W,Z"��3�!3"#2Ñ%A:�`�6)*:�kb	ҟ�����M��������i��Nyu��W�<rtǞ�;'�.(<?�Sfz��u[����|��������.��{���G��'U��$+ ��`�bw83��I�>�GfXl`&#�uz��kywl�	f�3��]R�䲪v�|qH��d�+�'�WMz���`2��"��R�X�c=�?��6�mN����l)�ef2��Ea���5���:��H���[��Ζ���%���/�����2i��0�#�*�u��P�b�X6���͛�]�̈v0Zt�v�],����Ţ�2����L�u��	 ���:�@�d��aH��gZ�f+.�o���3��O���SO���6??q����G}�����Gc�H�e4�
-��B�;6@�u&��<����iCt�}��m��D�1*2�I���b.�\��}�6:�ހR�\�#�k"x:KgѺ@[P�\Y`oͱC����\A����{�Sf�q�ǽz��֚.1Y|��hWX2�o=���'�w�/���ߋo�M�|���RP3��5B&o�!��`�;X�r�h�(^�d��It����:����&�J{�671S@!Y���O�L��� y�<��Z����aX�:�gZ?��Dk�ܘ�\,�Pχ�H��4��@���&�v�y"zy��#6w�l���k�3P���oi�k�Zפ)�c�j�A�HoP��7Ś�W�d���د@yߴ����[Kʡ��Dy���ڵk�ځQ�kJ�o/YS�_�UZ�k���]����Ͼ�Ƴ�k��������α�%%(���D�$Q��11Jd[!�A��"=���N�n�
���h�Ys�~Ǟ�����_��BΆ�	;c?~6�.R��?���?���|�?��|�AB��DǱ�H��U�%?\3�Cq�Y>bȬ��ɸJ6��K��%���S�c~_}ʂ��l�����$5�X�{(-��{X��pu�aV#��)�xtj���F��@�I١F'٠��z�3�F��꺨�5��Ŧ�X�m2�/������5c��$?���?��A��f0(L�uh��XOei<�4���Ŭ�/�i��X_���զ��Q�����/��Q�O�+�)�}���������oki��V�b��<I^M���
�݁��P�vX��b9���A��N��ZQ7͚�4Yf�Z����3��*Kd�⒨Il/�a"G$����E,��f=Y�C��Z���htZ��:hl���b��)��
�K�Dc�.�թ7i��H3���Bo>�խ����A����j�Y��qU;w]$q7��~hU�
�2�W_�F��hH2*�O�}Ȇd@٨�KC�4��oQwKՒ����Sj�{�EM��j�TTg��@nS�q<Nq(qF����h����2e�q5/QJ�[y��|0��a�]����L�O6d�g��K�[pۍ6-Ii/�0c�9�z�l���XU/V�ɍ-z�����B��͗�V��tjzƝH��F�%����I���R��m���G�uh5�=�W6��H��mF�I
W5Oa����[~�z|���åvf�qGh�4�� 3�V�!��xv���dN�]uqJ�>�������l$ϑJ�E�u땝��Jd�v����Y��5�����|�2l�І�_�i񻯱W��i� ��ر��
ںR�U3Z7ȍo�����+�k֬��(nM��h��a�;$�8�ڎ��;���"���V�ᚷ�\��]Vcpݕ���#VGx"P�ykL���Xx�����~fy}��/���'�m;|x۶'�(��s���6��)����}VO����N߬�0���7��.\	4��;�6�T�E��^�K�������Б1�iZ�5���!��j��O����M�͏���B��m������:ۃ� !Pk���8S�����/X�����W/Y�$nX^��G���=�W�>�Z��������Ri��Y3���R�}��� ���[�|'{�{~y&HڝG��צ_ߵ�{�{�אgw�Rʗ(WP���Iy�2ʇ)o�\�G��%`���%w^�U�̿~t���].��>��#�`���(��'�V'`
��i����E+� z�w8�p�S�;�^/f����֎����&����Ȗ�7\����/f��X�1���xC�t��`�b�z1�!fC��B�D�yPH8
�yTv�zC�$*��7�qt�����a	�̅Y���]�L�q���@hQ�����^H��xe�\��F��4���J��ɫP+e�[�[�f�����)4R�5[�k�6����f�gm��-K둡I� .���f��%:�ϣ�3�6����'e�+L�*(�͛�p�N����@{�Cm�#/IA�n3�;\��	�KI�
de���=ofoǰ9sU�B�Ĭ¬�������t�vM�(�;;o�,GRFο��~fNƼYY����,G�<G��srg:2��f��3��������������v�]�lß����U��������ۉ���w����8L�F��
�����f�R����$�L�.���$��
�L��'����?nƏ��%�
������
|W�;��_+�����"�V`��;��x�N��f�|A��a��o�����P���Gȯ����\x^๵V��_�:�/	<+�E�g� ����xR�	+_甏�=vR�x�h�|�$[-��S>��nãn�oN|N�X#����x$��ſ>����OV��O:���B��K3���C��������]���D�x*p��=���=3a���2w�ȻCp�5�N��T��GV�qu�Q�o����}q[3�o=)��Z�.o=�[WKe9�t,sK9q��͛z˛n�I̍�p�zy���`)U�f�:��:'���הX�5K�X,p��U�m+W��W
\��gⲔ@y��
\"p�/.2a�
\Ќ��XЌ�1_`��y�D�g[��ٓ0W`�
�E�l�Y3�8C`�`�ތ�L�.p��)'���͘f�{�B�{]�*���$L	�I�"O
Ɖ6�0&@� 0��8�.�<^�]'p,��8f�E�����h�2�GV��
.��K���Nⰱ�x������Cmx�?�6r�Y�n��[�8X� ����8��E`���>r&�`�L0������������f�ヽ{���e��.�q�S�t��oqbw���)w�]�������郱cF�a�収L�l�!"��h'��5ch�P!D`p&v!MuD��B0P�M`�@"�h%Y�IhY�~��+�l
��MDm
B�F�L/P��.%j���jQБ�"�^�,Y-�\�����������	��S}
endstream
endobj
117 0 obj
<</Type /FontDescriptor
/FontName /DejaVuSans
/Flags 4
/Ascent 928.22266
/Descent -235.83984
/StemV 45.898438
/CapHeight 358.39844
/ItalicAngle 0
/FontBBox [-1020.50781 -462.89063 1793.457 1232.42188]
/FontFile2 116 0 R>>
endobj
118 0 obj
<</Type /Font
/FontDescriptor 117 0 R
/BaseFont /DejaVuSans
/Subtype /CIDFontType2
/CIDToGIDMap /Identity
/CIDSystemInfo <</Registry (Adobe)
/Ordering (Identity)
/Supplement 0>>
/W [0 [600.09766] 3 17 317.87109 18 [336.91406] 19 28 636.23047 36 [684.08203 0 0 770.01953 631.83594] 48 [862.79297] 53 [694.82422] 71 [634.76563] 80 [974.12109]]
/DW 0>>
endobj
119 0 obj
<</Filter /FlateDecode
/Length 280>> stream
x�]��j�0��y�Y�..j��.D�h.�Cm@��j1w��7N����s�$��j�F+ћ�E����e�Y���4K8H%�Nt��3,��v]N�fV ѻ�.ήp�ʹ�;�Z�V�N�U빽�j1+K�8�Nϝy�&��l�F��r��{��A��I���%.�h;="+b�J(��*j���W?��Β���q��r#��	�%Tʈ2N���)Q�yM�{w��u\-IH�T!�1d�N�!��{�`�^�M���Y�'C�A#ن�4?ff����{�A
endstream
endobj
4 0 obj
<</Type /Font
/Subtype /Type0
/BaseFont /DejaVuSans
/Encoding /Identity-H
/DescendantFonts [118 0 R]
/ToUnicode 119 0 R>>
endobj
120 0 obj
<</Length1 43576
/Filter /FlateDecode
/Length 19857>> stream
x��y|ŝ7\�=}L����sj.͡ctyF�ei$K�d[��S�[�m��F��`"B 	s8K6���Y�s9@�$�a�/��&�<لe�]�dW�Ɇ#�Z���f�<ټ��������|������w��j$�B:��������
������͏�yίA�}n��=HA=y��z��}�Gj�q�� ĸ��پk��]g�߆�>:�����Q���ض���B�-�fǖ]�[�>u�~���[G�W���p��7��	��p��;v]���oN8�C�_���ͣ���PW�g��5���R�B_�1��=�k����
��B���\;v}~ �H�\�s��==��78�60o"�Y�?�88~�9w�]���3�R���<�26������e�b~��~=A���@XFd�$oC,�P7����<�X�Ӿپj��~۹}K|�H�_ ���(#P��"�i��ud �	�h"W���Y�r�)z�7�G��C����b  �(Q`�(A���QE�)�P9`�(��X���wQ%� �BU�ը:�JQ�A)�ZTX�j�Q`��� �hN�m��؈ҀM(،�o��8� �����P+�|4/�;� ��- l�؎� ���p�w�u��-�؅v�.�ԝ�-ZD�-죸�.A}�7�R��-\x�p�� \�WP\�� W���ߠ�h��
p�\KqZ����Dksh��p#�2?�F��Q���F��hp���Jq��m܁��xڞ�wt5�x�	�]��ڍ����t�^��:�;�K4�������]x܏�<�>x#�!��	�<� ��o��F�qt�-� ���̀�R�8�(�m����v�w�['��'�m�wR<�n��x7���+��	x/�/�at��.���x���^��D�?�>x?���}��F�<���3�S��E�~=��9�<�4�(>����=�>�W�s���)~	}����_A>�|}�(��1��їE_���k�0�c��������c���)t�z�k�O�� �@_|=��|� |}�z���EO���CO>O��i�o�g O�S�D�B_�6z�;��O��<�蛀g)~�|}�`���̇��CK��%��]fK�aL��%��}h�.�%"�n��-Q���*T?U�����4��A��IuƤ���`Q�wS)�Pi�R��QI�S�P),�2����r���2QN% F���MP^&)�*(�*)?�(��)�S��5����Ru�:����s�����o�?K�R��� �	�(,����,�� ���=X���_� ��׀Л�W��؆��,х�K(���vb{�o�B�va#�=ԍ݀=؟�.Z����8�?��pp1�\���g�R<�7翃��y�o�|� � �=��h9^��Z��W�����*�p5^������h�濎�⭀��U�g�z�+�4����}����h#�p�
8�o܄�̟D���h�p+�T~
m�G�_E���w��?�v����󏢫�c���口]�)���T��#�ڃ�����M�+h�x=�A���#� ��俈n���ǿ��:���F���C�&����A�[���[������[�1����H�O��3��g�t;����N0����$S��Kt'Sx���߇�b����fҀ�0̀�2���a��L�_0��������=�̲���/����Ч�Հ�3���f৙M�G�m�	�������n��1c��g��oC_`n|��h�V��q��b��}�9�G_b��2s�W��E3��D�0e���	c<��߈e��G͜|�y
��������7�AS̷O0����u�$�2���>ɜ��EO1?|�y5-z��y~7:ż�u�W�kг�o �c~�<�v�j�����L�4��w�o�<�Y)�}�u䷡3��ߊ^`=�gY~3�.�oB/���D�D�D�D�?&">.:�M�6���\A�<�СnУ��������h|~�s��o�g�E�H���2?g1�r�����0�ȝ��z~���M�M܋�b����	�����]�t1;�WY�g�G"X�Q��>еe�����Y	�d7���&#`!��
�B� ����#`˖�m��{��½O��h��'� �K`	��qJw�s�`#�y����A�|<�v9)�g�MЫ�k�:P�ReۇW�\�|hp`Y��%��z�tw-��ȶ�]�`��ֹ-�M�u�5��D<V��]Se�.
<gc�j�c=#���Ȕ-��%�Q(�U02�����3��E�{g����;��;���zdZP[�E�^�E��놆��������4=�Ƕ$=Q�$�'"��]�)<��ٷ�P�H�wB��n�j!�d8��h�2���l���w�A�J^;�&�G�Lww�ѵ�-�uM��ZWd'i3�+r�������Ѧ���%�e���)v:�v:41e���b]SU7����u�&��=��AeK�_|��z,r�-��M��{KF�%|B�C�ŋd��cm�B��QҖ��ɢMp2u��p�<�6������S��r�t�ZE��R�r��X���{���o�w�M���>�M�/\�L�ɑM�w����C����VOe�� ;Z�k���z�t:���ahx�>�g��,� �+��#�Ǧ\�����SS��]�]��C#]���bCç ^y�Dc$p2�ZҎ)�B`J����mS����m��@t*�ȷ66�u-�RL��z^�o�OA��ww�f�s!!F�� ��p
"= ��pAv�S����a@���-�;��{�6���\bɣ{ѵ���g�(��KL���ҡ�b�
��o�V��4�*ҽ�kV�S)Wl`��?�N�Т�bxB$��-]b��P�@5��p��B��������Pvp��К�wɊؒ�uÔ�E)Y����������� �=�@���|=�x����}�ˑCblɊC��X�B9�7�@d���s��E�����E�Hϡ�g�l:t"�=��{d�<RO�oˡ؊�ڼ��7n$�sB��degm��1<9t"�'W�>�#�\9|���k��{w@��uG��\����Z"����_<�cm�T��N`�W�����)9�I��Iy{��'���q-�,�;�-"	kD�?k �֋?��&�]�Z�s�K�y���e����-w#�C~~�����\��I���+�����I%�|M��*�_U�����w5K���͈7:{�/��7�/W��e�Nw�}���ݿu��c�O5��»��K���r��@(����2��Dٿ��&C�!\Q��<��-���!��?���'Q�h.��?��п���Fm�[�ǾAJ���S�d���p����B�����^������o3���?+���E��T�R�KX�%��Ӑ1�F|���2���L3�.�#5,���%����B��.��q�&7k�������g/c��Z�9s!}fN���X�g�(V�ljlΤ��)�yve������ή�;W>w�c��� |H>�<^Ǽ��H���'h/� \m�0�c�aO{C8Ĩ�'Ȩv��Q%Sf�Y��X���X��bF弌����+�Ka�v+��oH��%S*�v��7�.{8�����n��{P@�|���.����~����د��z\����9�y�v�	��ѩt�@��Ws�/�n ��r�O�>�;�Cߚ�R:���3�K.h�����~���Zq�Ӏs9�i�+F?��i��O��=.�blelx{����o+���_�}�<��Ⓥ�~���Yz�
(����ȝ��qQ�%�}j��t�i��yL�����������Nρ����+X�h4�i�K�c�����%�.	K�d|^�O��!�+㠼K�Yf5�k��[������-�mjϴg�.����7�� �7M����0�S�ǁ]�۹l��e���qꖟ�j7�s��l��A�9L~z��.ɲ%lo���^��mco�a� k,γ�Y?��[X�d7�ױ,b1;Lڥ	ah�&K�Xۖ?߮�dEK2U��#�]	܂�9�A�e�ew�1�w8������3�ײ9��+/�>����n�1�#~�i�[�&�.�1���[B�DѪ����+B
kYu������
{�3BE,����[�	��H�����O�L�h�o�L��f2�پ�ټ�F��fR �L.Gv�}&5���C_�p;�,�pu�5\�҆[���xB�C� jb���/+���|\��s:c^[����������c��r%�JV��eM �||Q2�(�g�XSk�ؕ�#��	=�P�3Q$�9Y?7�
�c4e��
����8��H������_��B��/��`g�2�k�5=?�<��/�<����Qt2{՝B<0��^����$9�vu@eT�G�@Z��@�4Ч��*�B��p"���1�N�����z2;�T�L���xX��l q:ǈ\���G�D߇�l$ދ C=�ʁ������9����f�e.X�o�@��8&:�(V/╈��͠�{��O텶�2��(Y����8���O�ް�"k1��*f\��6���l���&b��q�~n"5q3X{Ogm�+r����ɿ�0�О0�ٓA]C��g��O�ބ}�)���;�@� �0PDn�>rK5y�\�(w�� �@��n8�R^W�Q�ݤ�'�ba�����r��Ep����IkL8��1t��Y��oOM�����mZ?Gws��Tq3)-J�Dc+w0�+�d�mL��]�n"�[7&��a������s_%��mKkk�nk-�	7s {�>(h0�����P��a�yޡ�#|^`6
�
�+�{u%�4(�ʈ�G���V���? ��iPX*�r/�2ӭ ���k���3�Īj-&��n���i��n�@�	Z�+�_��l=+��c�%��SM�#xt��
��@ܬh���WK7I�t�^'|v��8a�A�/f�po<,�iX�t�4|X� חz�ɿA�C��
%>�C����'�K,��7NBU��L@�D(��UV���vL*�lm%�J�҄[���{Ϧ	�LÕ���8Wp�<֊Z�dcSc���6�	J�������� n����m!_m�2#)o�!����t[|�.�_��2��u� �p�C�ِ��>]�.Su��wJA�s+P�%�&�%Py.�N6�H��Q�����hH�XЉ��Mp�Vߩ3�݇c����v��MI�K�J2RRJ6]��>v-:wO�p8�),��y}�M�ɤt�(����&RoS�H�ܰ�k��D#D�@j:M�����&�� &:���������6�2���t3!Y
7�/P�//�cb- s���!���k�#��qo��TS抦�=q%Q�ll����	O�c�BKC\t]=��,����e�~�L[$��������%��$j��FDE��~�A`�	������J�vX)Wrs9��a��Ի���\x�F׵�q�!���UU�^���Wi��lhTF�&Jd:������ur�����Ӡ_9�9��+��&+d*���._�n�{�9tż���k>rp�L��'������RD�;@"��\���>b�0/���p� �+�ʍ�wkl�eD�
�bwE�H q����{#�� 5��%@lZ��ѐJ���Y�0��jU�� �A֓~�
V������։T1J� l?s��&	y.1�"�Q+�`���=���Nsab���+���s�J^�m^v�l6|�߿�n�E޹�k}���֜�ˇj�LK#Pf��-��D�� &	�]�.h�Uv�^�����k���)j����v$gǧ���2���G��'o�ʳ92zA��haeP7v����;ij[�pu��j�}����M
�j����w���F)��Hǜz��<Z�uD�#wi�.��C#lh��AG�7F08��Ts�>�5�ꢶ��Tc��-��>�G�"�����0bq����V��keh	��Kab�w�h�*pj��ă���7�K}k�1 ��&gt���?,����K�Kmb�`A��,����#��Ϝ��<m_���۱��m��<�B-��f<F0��7�5�N�g"�����v�Բ�H��cyK�:�D���`b��P��.ᘻ+��.oʆ���ru"�v�+�HC�g�-�Z<l��	��&����g�3 -/ ?�E/g��E%*L�{��$�\d/&�A��f�����Qj�w#�g�GY�@z�;�Q}��t�<e��)� 0ΨA���h�+Aآ�I�&��m�Yr�nM�O���e�������9�U0;�4ؖR�A��
�z��CX"��[��.����z�{l�֥�������oZ>�u���k�� V�Ѻ�ځz���2o��+-6��:1�Y]�tם�*[rj`~�,��v-���Ƙ��$��(P<������ph���T�"��K�G#٤���s6g�923�"�8ú3�M⨇���D���_}��K)�s�����S�h8!є�|o���)?N�������PG:���y:�Q�����p�]doG�q(�=��gy�'����B^��bd��4���4��8>�mɖ��5����.ˁAC���i��0�6�+�?&��[���V����{g������D�O���f�<��}�;3��� �[��S���*Y��6
�*�L�I��������J�8�b��e��;���lx\�+����9�a�hb3a	��4��C�z,�<!��T����L� �@�4��x�x��$�)Z�U�=1b?l���jg��|UCk_��O�%�x����{��Rf��P��t��ʛ�k���¹ܑ�ڊ�uӅo^�\��ُ M��*�N������,d���U�x�	�_��=c��N�3�(�r_��YW_��o>l2�&^mb�Hٱ2f^[���?��P3с��p#v�Y1����|^f�w�G�r��w$�O�ɖ�$��?؂[V�N�&��>������u����N�]®g�y���,"Id��Q�B@n7ݞy��~s{/@qn�t!��I�Q�!�J�0�;J[�<Y1�6�=��})$+�'t�d�!F��I�^Wx0"��"�w[�a`^$4Usf����W������qxNcn|��~Y2�f�~a_w��+�߷;n�=o���˭E=])�����[V��uq��?>�/�~�ʆ9�o[9|��Z�m1����Ҟk�xus����v,�A�W���/\����}�0D򢟞B�v#蕮9T�P�.ɼl�z��MDq�2�񲋗9d�i�,��Z.Tp��c��2dXo�g�����ߦ�q1��ލֵָ�:-���J���w�<��R��&f;�W?k��م���8E|����?UL�w����u�"*�0*b=,W���gζo��Y�_�\�S�B��<��]S{b��G�,Yr�賻1^�%K�DFV���2��� Ϙxr�����	�>�N�8���
�C��sCR����t�	���K���#��̎�}sǸ��s��f���*�����A��v�������Ƣ�C���c`!r��Y�8Ö�3+����F`Ú3���j��`-��_�\{E���1O�^�?����m�l}�lNg"Qm���!�Lg�'���t.[�c'���n�\�G}��L�WGBU>�{����dV���@�gcUY�ٻ��!�ى��!GI�tM+�U���S�'�ҁF�}���	>E��c�@�7�.�]�I�k���H,IL�F��;4�$�	��r/)*���s� k�g�c�Z�0�`�CB�t!�m�i0=��L!�Ϧ�Ļ��Υp.��R�PǾ�:����������Jug"|��<���E����[8��	��^��ʉ5k&�lPt�6�;�d��l۶��2y���["��A
uD�f�.�tǥ�\���t.�>���q�w���� ��C���1�h���)�AUQ+���E�b���q=4�M�HdP;U�A*UH���R�I�$bf�0sx�{WUo���Z���msg&MN����k��u��I	�$���>�{���a��_o�VCG�`�dԔ
�&�%F�T�8��*�A��r'{ w�a
�� c�ֿ�!w�e:�b�~V�Gf���g^��'W�<t~*��K�`*�.��i�R��_����J����3����_@�?X>�-*�e6Py���4� ��鵓���bgE� ��a���*�����*L$���a� ���BT�p(���c�zx��^�Ac�Md�A��m���b�d(�i�1~���"�$A�.�������� �g���g{�|���/�*��{�?�]������tӚ+ʃ��̯���U3��$Ih��">d�Jn���\M�ޒ��Ƅ�T0GU�>&U�6/��`:QG�_�84�!w�4�#�����H��3����̓����i�ə*�=�aQ���@h�a�(c�ڊ�M.��K��m#�zt��B�!��<m��|p�Rmױ1f�#�WG-�f*p*K�P"��IX�\��A�$�%:�*q��p$��D��u��ţ��i�\L&#�MF�jZ�����\JZӽ����^ݑ��ޯE���J���G����Z�8�`T݅�'U�c�Xď�X���_���^Q�ʕ2+�cv����-?]��!���������Cܘ�wY��
��<��J"�X7H�҈�Je��s�;N�X��4���,lY��atJ�ؚ�ۺwzo;e.�_.u6��Щ���M�����x�iB��\
��V _�c+�(��gք��Z�H�\9�.�l��������}>���kV�C�[v��o\��?�1�rt���`�R��P �"�6���� �$&��ós`2~gf��ʕ (b�d^|
%���p�>J$�i�z�E�2�D�#A�-�}d�.��a/��V8�[x������ر(zE��"���9"�I���̄��C�|�I��Ա0���-<"2���P�� �=\�o/�T3 qy�>��ݩя�NnL:�'<*�i2�c��?��>XUU�,�t�d���r�y���S�	��e8>�wH$��&�gZT[br �I�(��a���h�G ���\.]`&��E��]*���*x�b8GvN3�d*���T2*�n�MR5��@[�<�w^[[`U���s��;F��W���f��^��Kj����������3��������Ջ�%���j���ȄGX|��Y��1]v�>椑������6�6��1�Q��y��Y��Q�Wx���|���:�I�Ng��>�3.�Qg]4 �:�NT�ID��m,�#T�@��X_��Ex#�XrQ�
�t��!3��ڹ���lc��;s���+7o۸2rV��{&���.!���^�e�
,<���ӼF�H��CJ�"߄#꓄btA���<rN�d
B���{
�+��d��Ȕ��ұ��U�UtTth6(bb���y"����{�0��CE��ZO��3F�	#c�nPS�
���ţ�,�ř(sVG,lˬ�9���5�?е��uMM�nX�u`}Ӷ��UMM+�G"�W65�����N���[?���o��[Qѻ���'Q��
���-'>��I��4�A�d��I�{�Qb�H�Ɔ�Ƙ|4�< B�4��
��4C(x��I�B��	�Gs0)Bц=�Q�v������}��U[�mѾ�`K(���<w�����3y�QIX�ΜW��Օ�a� '����P˧�Z�:�"b�D�{��Q,���������.UD6��I�����rI<���pI6���ldh�C���A��O�S��A�4�e�)4n��tr_��B��M')�A"h�{IP���A�DI��pxA\r�}�B��u�+1��66���ƍ����=����,�qm��yu�R���_cˬ�u՟��� I~T�n���|Z�w�K`�߇�EFxK��^2~�%f�F��R/Ǐm�M������Zp�8Z�Bd�p�N�[��=��Q��R2��,�>W��I�6;����//�_aV��-���9��U���zS8ր4V�w��'m�n"��L7.wu��L.[���3o�ܽ�{�eg�(�e�+C
��Q����tg[�
,:��b)�(�\B1'>�ēN�L�(!K4$rQNE]��
qf_��Gq������ώ���I�D:�Oщ��?VHx����fEGo�Os� ����9F�x}w�0�Bڢ:\�Zy����p-����|�dȸ�����ŀ+w8�w278�jh�!���(��4W�������҉S�6Z[�3�	.{�39�Gy��*��:�0\8;���	E�P���@��h�+<��}�7l�h)k�[�ʦH풖�����+�gC��Hmԫ��ڶ������S�	_Y2�U��t����d�����J�!�����$	Bcvl�v�� �ǈD��H,x�4��sr�r���@[1��X����O�'W^x�]Ij_��:�"n`	0�1�v2���AƸ�^����4Y).o�K��4M �s4J)j=M���ɑ���][���+'���;6k�}[��3�;6x�4�3���UCI�щ����4�~ow�u�:��7(�	O��~;��{1�#�_5欆��4�8Lsj�sq.�8�Ff�"���ɼK���������#�����xb��H��y�krXfD�tv�ݸR��^��r��ԏrg!ؾ��.5��S"=a������g�NO����#���Q���caO���--;��'/��}a槷�����e�������~#���v���^������7���'0�,�A:��w}?A#���U�A��7������q��,�!���w�e���2�PȅB~Ņ]�&~ֆ�ذH�hUqL���v?���݈A����J����KǬ��c�%_ ۣ��T�>$`��M���`��å�<y��oC����K]�2H�醯C�:l�l1�;w� ��m�L�9ߏr{�?*Dx$N��8'�y�r{K!<��?��M��M]��K�܋X 2�1D͘F�$����իS�MC�m�P$bT��XYqe�	���C��5+�;��#x��>��;Zw��;��s�����g���5���PD4�'�΀gQ��C.̒!�;�������NivS�L	i��4vG�E���s̔�1Ӄ�F�z���u��=����d�3����y��y|��a�W�c���{=�f��C��:d�bI_"6���Rj	:^��=7Q:נ��%i7�!Q�v"�@J6���֪��>_�vu�_���kҵ�.�70�􅆟��ff03���3k�j<Pm����N!���tJ�ENS4��i��Z�A�q�U@�8�g���ܘ�l_��so�-lcD����):O�:l{J�v}���Yj�����52E�&�\u���H
������KnH��PqM�]�}�+[�[����-߿j�ꁡ'^艅���
pى� "��^�"#�Sv;�y��!�;4�B���/d���Y2rW�yq���CJG��8���qx����n��;f�VkGOwG`�s�������n�]�Q9�eۆ��Ц��"��j��`Ve8;;.��	��@�~�D˯��<M�v���g��gV�������E藥��Q;8��<}�4T@��5e�e~I�>��6��5��>����Js�/ON0K ����sH�l�w3�U$�N��§��&��%�KQ�]�9u'���g���*�U�.�s���ɘ�E��-���-tH
Z�Qn��$�p�h?Y@6H�I�n��Oڄ����]��Z����N�E4MZ��t�dF$��i�).p��6�
K]Τ҅�B���U~�tsKS)�p�$l~��⥕N�*cH������_�RR����͡؂�G(�I��x]�!;W.dm��ތ���M}53�2�9+��������{jc�*�C Ơ���?+�'���'�BD�Z6>��n%�x�Er,겊������q�x�s���Ւ�R�K ա(T�4)��&�N��%��+��t]b�6�z���J��I�z�Q�+R�1��v��D�Ȃ�-��#�\�N��V&�~S�V�nYо�'�3��/�ل��+{2A�$:��~$,��>�<�l��[��{��2�	�u�����bL,��{��)p��V�
G����_�-w$�2��(cR-̿��l]-d�O�%�d��\�P&]�&;\$
d��Rg��5�Y��BqR���J�}cG$�͵�z"��^�¬��%�J�����l�R�Iٴ��'p��8���.��@@��.R�ҏ��w��A�8�P7�8@h�u�e�xL$D ���>z�W�7i��y���-G%A�$���� 0����N�4\C�2��t�
�Ō���H7U���D� ����j���MV���uK�G.��c�HW"�`���n��fz*�ol�#���L�lm_����+��{�?���8i���N���E*	�գ^�0p����KcA΍�&cnM$�M01�B�&v륹�[%*�P��P..�}4���k�}ڤ;6!	��.�T�9�β���������� �1T��tI����dh�L.}q�Ť�m�a�����Ds�.b�Tv��ݹ�|�_�f�BC5V5wmΆ�V���Sn�����U��;xSZi��쮪�ͻۇ|���1��3QW6j3�(8��Z���K[�NȠ�"!�0�R5k�
j�.;��sgIT�!�/�Dgh~�،U�C��t4��bn+*� //ZP�l��iٲ�r���1Qբ_�B��V9+r�Z	��� �H~�~���� �jߧ�^O��C�F��*A��U�V��+�4D$��2�#��+�G뼁I
������r0����Dm�$�Hc�Ȣ���]-���.�NQ���K˾�_�AVД�Q��X|��]W��-^ޱa~�h��G笉eC5+����rɐ�"H�9E_�}CG���
S�i��.�Fg/��M�4T��vA�|��݇v�UF矂�.ѱ��R������˔J2��|<0�M�|3�0�qt��[�,���D�Ⱥ"~�!悬7-�Fn/�v!o��5���\�tWc�9��`��9��J'�H��1��3oKr�}�i�Xo�6m���8�!�u�5r�LVG�n0�q��H��n#�(+�^۝�
�-&�'KK_H�����Z��J��,����b>�0�hYY�|�M�����M
��Sȑ�	�s�u����d��q�2n���2:c�q�~�{�Л���B�d�mH��K�&<o�j�$UE��U��5Ŧ=�sKY��V��a����K�,p����~��Z�h��^�/zAS�)�Fݫ�3��o v�K���I�N&Q\^��@��[ľp�E��]^j��"P�"n/IH)�2P���h\�\��t�U�9��i���d�U��+ӕq��O׉W�u��Ӗ� O�bn�!E�?OӐ�l!g(�Dt�o��9),����i!n��Jha�<�.�eA[Y.�77���i�7�<]C�X�¹���%���X�W\A��6�=�TFWdM!@!����R�Z}]Tz�[�q���-�'IA����$b@�I�:�m!�[���7':Cn��Y���/���v��?���Ѭ#a�����"�V�Q���_9Y\�\
��P�J�e�������@|;	�E��/���X�ZW��+Vm+��JL 9ȶ�i�?�;[F��u>2a-��Pj��x]���bcq*���ɀwRF,˓vBsx�x[�@r!
���n�t}a����n��M_h�i.5��{�Dfm4<u{�K�Jv��8�mTb�����.��i/X��rv_���
Ys�/uD�^[�^t���Pc��Fbj�:k,��o+/�0���]���%��<�
�Sf��O|�E�"��0Y�=^�=�����ָ�׽ؾ��'Qa�y),/��������hB���~�Ѥ��m2�M'>�?� DQ&
���B�O3 �T%�$�""�[ѣ��(���j����ң��<�x&��`q�$X\���
��tq����g-A�+��R�B���dR�#^ڏtu���m!�[ڮ�J�[�޾}>�fR�?��D�7f�Uu)�+����j �N�/�_��H0\�H/4j��Gc�g�w��g'��A���wA����k��T�=S�{�5�G�vq��m)�PV��.�Ժ%���b<<Z��s��4$���M�m�wWΧ!�+�	ф��$�����ϙĂ:�d��I�����4YeZX ���HZD��u%�񺜩�g�\tc���d��Y��X�J�� Y����z��5ȉ�|��`/�����e�YH���?AhY^�������9�z`Tt���d��R;b�h^���J�V3EV�Ӱ��$~�I��&��x�]"���8'�81ʅ8?;����������?.Wׅ�+�$�-�����~4'�&�+�\�I�A$�QRC��q��W��<��ߦ7��}*x&�թdi��"fOrP��7�-�m��J�awM2(Z��b��,K̫r_��{���{���>�W�����p��[N��g��=� O�,ο�oa���p��¾z_��5#�s�J=���U}>�zƭ�^�Ngv�t�'U]$3q:�T҇<��5~��JSm�
g@���U߿��hy�o�[�����ڦ�j#ǈ��Wd��i��@�@#~E/��׌�,4���^h�J����:���K��q����g:����m8�h�o�C�%�ﵙdYR�=�9�#��`��;�`�)k���̮i����3,�ো�C�u���<��FeN., �$�	}��I��'TL{rAg/�'k{�(/6ݽ�S��d���(�T�8^�w�!S��Rk{��<�6�V�7�}b��g[�.&L�=1�� ���"�Y"�ב��T��zi��m��W윳r�Ί-J4�4�d"�0�}3���*��7��]�*+��|��	�����^֞M� �qS�FA�܄$'=�E����|���*�woH���#���YzrF��1�?aZhi�h?�*9�J@�l7�q�R��7N�B$�{]g��8K�4���"�Ѹ+OF��L��i��G�~����*�V% ����!2���L�^@���_?��g 'F�f�7�k����-�Gĺu'�d�:48����^�X�A��ۃ��!�%e�t����]qcY|"dx���4��͍�v�q��O��}n�ō��q��ލ�rc���Y�bQ{` ��T,�
"4D +��9�8p����@��,d��B�x���McV� H�%�%I_�5�v����R�M#��O8]��5�R����׬�1��sV�z���6��q��gh�	o��,*�D��L����������� �,��X�>V��la�¿��������-��i��Z�h��Ş�0o��8˻X��`7��d��BP~��˲Y����댞�pqo"�8��s��������L�şc�=,����et�O� !A����%+h���4٥���^�]w�,�@
R����hP�*����?Ql��Ku����g'�_��$��h���,Biv�����o+���"���5#
H�v(jh�H�4R1\�{j˖S�۱x�~��m���Wo���~����ݻ�̼��d=��zxбl��E��t��uO�;���
�n*̺�w�m�4٦!tq���<�xa���4����s��}Z��X�ħҤ�~����&��|ޫi{�4̚K��xZ2�K��#�JӬLD��h�_�<x��[c��ֹ>_kk��uO����z��/���L���;��:�|��.�Q�y1���I���AHVn0G��C�ozL��1���Bx�ܤsf�1E�@M28e*�&i����H�4RQ��K�4n�]v��4{�Έ��+�k�y��x�u"v2XNh%�;-P�L�xZ�RJ�^HOx/Q�����#*�g/M���i1BKb�u�dYd�S��5�˓��ӵ��x��}W|�N�x�s}#��+��Q,4m��}N�~��ݱ{wf�˻>9��ڎj����8�	���:�	�aw���\�O(�&2��ٝ�M�}v��@.|�L�}�L�m���Jق���y������= )lhf��������=+���,k��jg.��$�f�t�ԃbh<;�k��	��&b��U�-,f�x�s<1�ؓx(�j�p�>��t45N�9�g����
w�kqqxu��_`�Iv:9��s��X-�XM�7�rt��\.}�4��'Z�7�������@a���+�m�6��A��zwְW>_�-��G�_�*�O�Q�	�����$9�����%�I� �</�,�)���s"��ې��<<Ʋ<k'��8��@j��s���  E.�KD�_� ����e�%�ɂL��y��yAd�F��%��c�_���/�rw���"R�0���?�/t
��ng	��(�����X9�'+�s)���]�.~�6 ��	�x����	��H7�,���$�vȪ�抪���7ɮ9��	Cy�'+�T�ݎ�� W.w?PV׀_6� #�/���/;���F��dI3(�$�/I���N8C�%��_�%~�����M����	�
���B~	��d# 責 �d�.i�*��=E�$���/`�&I,k�i�Q0�������d��D��"N�.s7�t��2G@t���%U�A�t��h�<3��Ȏ$����&q:yT �R-��]�@m��\�__�D�%��_���d��K���tEWeɡ��"�ϸYT��w*P-H�C~�Oo��,�Lew�)ą�B���ةpD��P5Evh<�~�/��P~)~�
L�/Y��/Y�.w?P�Á<��K��BpY�ˮ�ة��nMs誢��P����t(���hU$�t
��9Tx���� M�E�/w?P��!/�/H:�B�8�tv:x�G�4á���e85SSC~9��R~��*�ɣv�������r~��*嗁.�Kz?����;�������f�_�E~A�J��j%�/������M�Q � ���p*��&���'Ё��@@�;��4��;��e��p�z��5���?���I�����C�~��P�����f���KTLT����u�;u��0��K�L��pj>��p;5�4N���ɿD~�� h�O7t���p|ȯ����D�2�4���r�)~)e���t�5���qz�_.�/by�/C5t�0(���0�rw���&
)�T��?=o ��n�~�@@	�L����n����0��x7��~��/�C~����"a�(�j��(I�S�D�I7P?�H@Y���4���2���s��
�L'd����B�TL�n7������i�t]��]�@m���a�E����,�&�5��4Ej�m����eXF��w�-��i��Z�yT�T�N�rw���bQ'Q,̓(�ww���N��x�>���ٝng��n��z��䄐����N)�j��e���t�xP"��]�|pjW��rXtvZvZ����-��o7=f8�=.��y,��ˉL-x�n7���v#��Y&h�q����ڼ^��S~�����_q��p�������B�����{c^�[���D.��min�$������6]�������LBdh�� �J�jz$�#�@�<=���+P��|Vy0��,o�?jG��B�����1I��rT�9u�;�r�������GՕJ��N%���%3\^�;���,�y=e!���?�w{������������I�[�{}>������u�����TW����a8�5��'3&~�;�2�&
F��pD����xY��H(��5Ⱦ<�!���+�W��C�N���ƽ����j�P�<�Ⱒp�躷Lq(f�|��h$�c�/쯍W�* �(��G�A�y�CRf���w���  �`����^�.~��H5g�s)�'����A�d����ܙx,ZƓZ�����:ZN,�Ȕ�ÐU� *��"!+V�2G}����p��,��]�@m���F��
8u�fY��t�����A�ӒLī��*=��kc��pyees�<
Y5
�Py�<�.�jZH�D�ˑ�����]oLSW?�>(��t�8�x(����d�PWA+�1�#Ri�2��s�Q�����M��C�X�?*$.�p�t_�}ھ�o�Ò�Ę-�y;���0�þ-1��w��s޹�ݾ��M߻9ūrV�ߧ�XI~>���>ͭ;v[��d�u��f7VѬ�z�Q䴯).��+Z]YV�tyњ���ME�,Ȃ\X]��m���ՙ�`[�W��+�ߧ�X����q�+ӿ�[���Ss�?�#x	�}�M�M����C-;#vJ�'w�7C#!�|V����6�8��B���vBa=��P-'�Ѵ�D�i[� x2�/����TvZX/l`7IW�	c��Z0�p�b"dK����'�i��0��-�\��,;XҤs����,�y��:�0V�������Ɯ�����?����������/܇��Mq^|�v�m��5rQ<~�x��o+���2P+��?��KdAdA�
���KU/#�%0i��kV)�$˖? ٨qK��ߵ�]&G�`���1��%��$�'͋I����-�]L�3={L��fr1�m&�`3U�9�4/&٨7s�b؝PB��E�~����~�l`Ƞ�n��G�V�&�7B�~�����㦼}0@���&�L��IU�����C��=�i�C6�.!&��ɯR �� .F�(_�9z�|�CGwqe����W{�!�YR�����¡��k�� +�#!-"7�"��~#��sw�o����[��:��d�?�t�{e:�D���tCj0 GB�`��ud�Cڜ�3(��8�W�}���5w%dSn�N�N&8Q�f������9�)�ɯ!"LMp�+q��L^�S!�)����"�ɤ�h�JQ�=K�A'H��i�V�wo�t�S�[ӿM�������J�c	i�

�����륱K���b�E���]���S���e|���O��ϟ��sg��c�?A��b2���G�o�3���O��{�m�'�Z��Q�� ?q|�G���Əb6��j�{� ��pl8�&cX�����Gg�w��t��n�oG���(-]T�:��7�eb��Ei���Vo��&GgG��F�7G����7���	�o���<�Ônh�����o�>V�_��v�� ��i�|od���x�F�֡��̪��uUR)A�PXye�O����.�.e��]	�ڔN���n_���ݢ��V��x���Wvķ*�x��=ި�6�lݭ:�N��s+_��Z	W��3�Y��3���n7�'R��J�7��jG[�r(J�o�U�X��#P�S��iޙ�i�O��d��\͂�V��:U}�1/Z� ��̾5�ht�蘷����Ę=U�T@a#2��B�(�ɲ�Z
endstream
endobj
121 0 obj
<</Type /FontDescriptor
/FontName /Ubuntu
/Flags 4
/Ascent 932
/Descent -189
/StemV 109
/CapHeight 693
/ItalicAngle 0
/FontBBox [-167 -189 3480 962]
/FontFile2 120 0 R>>
endobj
122 0 obj
<</Type /Font
/FontDescriptor 121 0 R
/BaseFont /Ubuntu
/Subtype /CIDFontType2
/CIDToGIDMap /Identity
/CIDSystemInfo <</Registry (Adobe)
/Ordering (Identity)
/Supplement 0>>
/W [0 [500 0 0 231 276 418 667] 11 12 324 13 [480 564 246 299 246 384] 19 28 564 29 [246] 31 33 564 34 [404 950 663 643 620 713 571 537 672 705 269 500 629 519 871 728 778 608 778 629 532 565 688 656 929 631 598 573 329 0 329 0 492 0 522 589 465 589 559 386 578 571 253 253 522 273 861 574 590 589 0 386 446 402 574 502 777 511 497 471] 428 [643]]
/DW 0>>
endobj
123 0 obj
<</Filter /FlateDecode
/Length 298>> stream
x�]Q�n� ��{L��y,K��H>���� �)R�&�}a�C*�Y���x�ͪ�P�!�t�l�C��r8W'�xц������}kY��4z�k��( ��P��`�S�_X��:m.0;UM����_��x�,Aa��Z�����
u�y�<;�'��ɍ����ZsAV�pJ(����W_$ֹ�?��������P�:F$vUT�sAJ7������H|M!�����6%����<PXlR��k
U2�LF��ZPr��{�a��l%#�q'�Aʫsa��8^�6�حld��B��
endstream
endobj
5 0 obj
<</Type /Font
/Subtype /Type0
/BaseFont /Ubuntu
/Encoding /Identity-H
/DescendantFonts [122 0 R]
/ToUnicode 123 0 R>>
endobj
124 0 obj
<</Length1 21144
/Filter /FlateDecode
/Length 11658>> stream
x��|	xՕz����޻%u���ZZRKݲ[���,�eY�Mے-�6xŲ�M6��bV�d��&L0Nf2��x2�L&��L"'aY^��s�[����{���G�ꯪ{���9�{nI-  `G0 ,�N$G&��6 �b�����}�x��z��ܺ̓��
� �V�/_�k4����Gx��:G��߼��3 ��L���;��
@�1Ʋ~Ӟ���R~~�b�6��,=909-�0<8d����~?�_��OZO ,z��6���X(px�G���M[��O��:��g6��f��S K��-�����/����(��m[w�j��n��?��m�o��K�ˋ��~��F��E:�wܞ=�w�?c��8�(��ʭu���p�xm�s��K!��V�b�D�gl�����mF��9N?gDO	��o����[���]D�1��Q�UGH�Ȉ2ص��DEG�pj���Bt�ѭ�<ڟ�>D��@@b�#�#�	
� 1A����0b!D#:F!�XE�1�!C��(�2�}(ձ�q(�~�:V@b%$P�X�c5$���ރ��5P�8j���Z��`&�LgA#b#��ޅ�:΁&�w�iĴ�sa.b3� ���
��mЦ���q�C����@�,���a�"X��X�%�D� K��t�R�.�A'b7t!.G��X��V�r�^X�اc?�"��>�U:^+3�J���k�@F�w@�7�Ոka q�A�A�aX�8��Ð�K� Èa�ZX�x��&؈��C���_�V��f���zw�6�Qخ���w���p�"��q�B�7 �݈�a�ث�3ܨ�A؏x ޤ���Fď�A�gp3B�nB<C<G�n��	n�[�t<
�"ޮ�p��S��!�	G�B�	|nG�܁�i��3:���Oi���4⽈��}�����p7�q��p�p?�C� ��߆��qć��[�x�x�o�s�����u|���8<��%��G��/j�_������F��×O�����������G��
�#~N ��gO��<�����W_��"����/�I����+:~^D|^�ބ3�u��t<���7��o阍D�6�Q$�(}�>�D�͑Ȇ����HT�Q$�(}���Dl��ض�#Y�ǭU�6}LJ���1f�Ǖ��"U3}�8�����ޭ{�G�i���>�_��wt���}._��ݓ����t_	�>Q�{@D�wT�n�n˘n�b�B%�=Ju�麎�-��X�k�R�KB�B���j8����վ���;�w1}q����H�up^{#�ϴ��H�����]�;�D���H���-�D�׾�����Y�D���	���\bDl&��*���h%��
���2�� �<R�}:H���'1�EX@J�
�XD���I�v����K�l�+�I��H��<,#�砛,ў��d�����	XAVj��K�hOCY�=�d=�Jr��eXE6kO�5d��d�.�K�����5�F�1 Ӿ���(�%c���:�	�"�Ҿ ��n�r��yXOD�@���䋈ג'��:��Y�D�ю�f�<��v?l%/k��6��^�N�j����ۈ;���0J�������E��>7��ڧ`7�g�.�C�q/�w�N�G~�}��w�;� �����Q8H&Q���MԤ����o��0�B��-p�����j�[i��1��ƴ�`��!���A��&�uڍ�	:K; w�9�~��6k����]����=�i�T�>C���^m�MWi;���^�V���zm�O�Ӯ��m�;?Kwi[�A�O�у�f����	>O�h���t���Fx�~J� C�E|�>����C���/h��8��6_�_����im-<I������� <E_�����em5��W���g�k��m�g�w�U������s�_�oi}�U�S�Nҟi+����/�_i��k���]m�D���u��^����9N[
�pfm	|����*'k�����k�W[ g��6��h�-.���{��r��r��r�����mww����=X9��i^�����އ�q�8^��-��]k��W�~���};��ChC@K����R=�����~������ﺢvN�83w��HՎ�l;��*�����6�EO��{�`�Z�����0���z�w/��\�d��w�kokmi��n�3�q�̆����ʊ�XQ4R�:�l-o6%P�i����HGG��b��e�!,j���Ѐ~[��;�x��Uw��w���$�P#4V���"���[#��deW�����O���sCL���E8�O�ڼZC�d �6޾k�X�@+�wB��DZ�-��[D<�l�$��)�C�Z�6���hǹ�����ή���@8ܯ�A��ָ�eܬ���d�����n?i��q�Pdh�qn���Ǝ�+���H�x�ޟ{�����ֶ�x[�l����������L��ʒ�\����{`����j���s@�PB�_8�d9z2k�b�PW_�:k�@:�����T�������~| f�j�����?�6TQ������C�\l`��88<im��my�x�O҃�����J���؉�L]}�ȶqg�9{��6v���w������S㉶V&W�ml�5+ k+��w
s����	�Ma���w��Qbmc}C#������H�/O����#}���J�x�O�.�3�Oa߮�{�f�ss���YB���F�����Kf���P	��mȒ���]�^pE-��c��t�����WD
�d2��eǂi��<��hٻ�@��������QcN�\k.'e���<3g�TW�#�(6�1+zC���G�#�C��>�7�kݾ�#�V����y��+�����u��qڂ�L�T���_O_v\U=�:4�Gv���#�!46�e�88�՚��m��i�������ڡ�c'��mmf�v"��"�}�]�e}{��k�˛+�1�4���[�N�ɭ�+�N�B�.�;AIs?�~�� ���S���c�̵����2N"spQ�s�P�u�n#ͬ���7e�M�܌f!nR�f�;W83	�kD?�Ӎy"�|��ũ���ύ��&��<�4��%�cnw;~��}�Pgx?����(~����s��!�~>�,���^xR8o�[����=�k�<�,�~ߦږ��NZ'��eyP~A~���3%xs߲ś�^#7�|�/Y�ߎ}�����1���"�Os��{�l.,�J�\�z�`�PZ6�4/vP�Lx3g��x=�:���~>�zuUJ	+Ÿ'�]��7酋j��]Ĵ��ZfY�ɸV,N;d9(S�`1s"t�%�� �J����ųI�k������1W�5�u����=�\ӳ�q��:�Ӳ���G�_��s��n����+�^��,r�.��,g�.Q����ŧX5���r���s�ѿʡ����c
�N��tZ��<p]�`U�g�.�H]L&߈WW�K��<�����%����ӣB��:�-�����ј��T9��%���v�v*�a�`H`e%����$y�8®��N�'[���p��#��E�����Ӷ42Y��!�׉�~���_�i��P����G�hۗV$�ck~�w�O�5\�.KW��=]Nʭ�L��z�>X�����Bc�iq��D�c닍�z�C�Dӄ��K��������΢���'��LTWy
+)�|*Y�t'3R�9��F
�-�T��2�du��@c}�-���ؖ���g6�KC�/���̰�kf�g��̫,��j�(���i��)y�ݼ#�s䩂߱��V��3敕.v�{gWu�
�Ղ�7*�:�-�u`bG��N��i�X!j��v�mO�Zݻ�������
Д�H���''2�����zc�SF�*�X�CX�~-�;wnߴ�^(�W��暲m��;��?��� !�6l�F�W�+7��sɊ�h���� �$sґp�ښ�hwQ��p��=Q�M	ÂP���rI(�!������Yt|Rhr9(JW7#�H$���Q3�2�ب#o�VuT����y�W-9���v����E|E���޳1�����&}U�^�{8SeST���|�5�k\{q�z��<y7m��ʣ#75�@/07N)������枤�N8��$+�b-�����n�glD�l�b�-���HN��8�q�HD =c$q#��A8F�"��Tpw�n�?��h1ZS+����%j��b��ǘ����\���d{��ihh8�Ϝ��}]���=n<`?�L�d2G�3g���~�H܀5X
�*��\�QRh�DЙ=��\-���g�qjޝK��W�t���ɷ��N����Ҷ����!�z0B m����m2P�³��N��VW���>NV?|U�=|���6|�V�-A(l�8-Jk�I�B�P&>d'v��X)-���󉅼��y�Z�3D�oJ*��&]!�ט:ο�{;�|;�}���D2i��������Rx�T�b�3G�����^M`hq'S	��&��,�<^"m�J�����km��>ܾ��f���p��^X6|aO��H&Ό���0��SO�M��#�3:�5`k���K�P�JH�T��͆V�n���vG835Q#o�G���l�̰n�2��''��PM2[�V���p����;��E���'g���w֒���R]�A=6��6t�rLn_@�d�e�_�0���m�>'�&'�˟^��$��'���#�+I�G;^}<u�%l��Z�*��/m�`�/��J�Uޘ�99��(���l�I4-R���V1Ԟ�)z(J�(1�a�+G�kwĤ,h�'���୼��\��1Z�6��q���7V����}��=~���)�ͺɹ��U��H���-M�ʊ2�iGqi�s����%`-�[����u��U~�������Yދ���X>#G�i���oհ"�rout���\As��5��K���Ɇ �a&A��.A���Tp�0s��.�44dج�<7����3�r�>�Ċ+�l��S�H6z
8��3���~KzIakma�y����pE��d}��嵝3���V���T*��At��~k0�RU��6�@�'{�!�ߥ�����u�]��+=zc��h��t�Ҫ�~��}M����}/�!1�{U�P��?��fr�cd=5��3��5�mw�y��o�J��&OO�.�Udo_N��=2���%zηP7<�^�:\n�-K6�hk��鎺)���.�)n���>�|G���,�I4p�t5 .��@el����F��CF/^t�
��H�ᕍ��h�sq�kG�̡0d�3J1��~��=2U�+��5�:mHAig�l���Du�ӑ�N8�4vt���x��ƣc7VV�8v�����/���N����G�XZ[*�2���HLZ!�H��`!N�D�)J���&RѸ�M�n�5��ݴ������DT�?�_�s;}>�Y�"�.R�"g\?w�iu�
��"�GɊ�H�.�~;��(����(qD	�W4�P]N��/��2�d�s�|[&��F�bA�LD�� ��_�	�k@�'�@P�.  2N��Te���Q��;<���j�Q�t<H�>f_����1t�i����2`��,/�����:�:��b��n�f�{qm�0�m��q�%k���RVn��ؾ�g�¸Xri1Q�>����SF�ak~��nx=��#�f�i�ґ;g��<n���Z
�����[�$R������������`��d�Y�NUo�2�{�J\%l�U�bi'5
�(�u�w��HL�1z�-N�	6���J"�t���8�������-��Zb��2��c���9=س��4+2#L|����&"����Xo	����W1O�>G�` 6KcH�CU4M)��)�=N��(�S~�ޤu�~����4$��פ��.'��soJNS�8�<TQU���*�]���sQU!),��*d�qy��Ҟ
�LE�K3���å>Q]<͢&��,NJ���,5�"gt{r9.&�Dv�X���*ʳ'��f�C�wa�*��ϯ�*b[qej�۩�(y�H�<WP�Y=�wf�Z�\U��)F��-��و}m��7��	��t�aL�E�M8��+�*<TH��`!彦.�ް�����k2	�nE�u0����f`L��20�#5LrEO���' �.���{��THb�s��{��G�f5�8��j��+f�.�0�;�-��4�Ql�E��w�Ϣ��c�Y�B{��C�Cs�d��[��h/��r3K��� ��a_�K�u�D����U+���$��3�U3��	��ڡ��}(]����湳��]�%��-Abn^X.K7��e-�XĽ�=�`uZ�:u�t�4]u�Hv4u��l�����������l�-�k��*۳c��.��0�:��)LV"qW�J�ksf;E��s-�r�4�
�i/
5���}ǈض��D���L"o��nJ��Y�^Х~�P�yP̼~��OMf�6_Č�;�~_�\J+&�V�m�*�z�bFs����M8z��'2M)��۳�Nf�"sF�0�o�턳���v���cC�\o_U��c�L>e\�.]�sZK����ml��D�D���׆9h����m�؂��ZY�c�
���C;�<U�+bog��Y���p��t�w�3�b��D$�����V,�	���z�6�]���9��()&1�r�����RSK����΄3P�N�<���T�A��Q���Z6�[�j+�R?�B���G�d�H�Ʈ2�e{˫��S�<XNy���F��C��8�ʊ�6������v4��ݫ��R��3��e������TH�u�Ù��+&���Ƚ�M�SǦף�{J$��9k&���۪J������T���h�PS��>�$�V��L^��"����Q�it��"62!�gj��ܒ.5D�Y�Ľ�C0e�P����^���Tz9!Ԅ�RS6v4��v����R�\�(�b��#��~LN��=)ױ��3"��z�b"��� ��F�a�}�	�p}�ot��@���FI����B��e31�L��M��d�b�-�S8%]���cǤ���S���D�w��Nj�tW�ͧ 9"ȑ��n�J�e.���wHܓ';��g��{�r8�d�:���1�g�=�ҳM��2!\R��)���c#�SҜ2�{����I�!n͔hY;4���L:,�>��q�'�;��ID'���~Ar
�$�pJ�c����P�����H����$8M��/cJFy'&y^Q ��N .� e�d1��[5]ZⳘu�Lfz��:si�F_�g⸲�b�������'�Z�8�{˝(/�N�n,H7&�'쥕)߱c��[��Tfo�X���75�t�=B_�O*P6�el|�i�d2�l�8ql��O�
߈k����x�v%�c&%�����x/���%��n.�p1�<k��R�JT��K���众�h^Q�\�r1��]�ޒ��o1q\a�լ8�Y�t����f~�o��L������L�uq\�q,�_������
�@:�H54�7��#M]U걢
k\2��A���k�_��`�wz���U��'�iz�b_P�.�t�l��{]��Ȯ���j�u���H����̦�<�=�Br|`lF�c��[�k��b5��t��Et\bgR��$�/̍��g70n��
9S��m���C<����u{Md�����>�HL�0�.AvΦ�h�Y�b�mk��xo]*U_�J�~���%%��ϙ3�QR�12�m�Ҷ��.=�Gz���t�.�H��ʄ�221����#.	gl��\���H�sڦl\���P��f���D}o����Z߱���pmݨ�����=�Qb����|]<o$7��>P�(�:@a����U딣�����6�r�O�o�V�;k�R��X��kaa���E#7���+�8#&��R��Ջh�28���X��(�<��̓��( |��7�~��_���F�f��+�˗�Ӓ�bO��/�7�J�8*�,�E���d������C�^�_9b��	"�����Q1�f�:�M����v:a���G�)-,��4���T����ٱv��V���׵gT_��:�G(����؂�eT���&j�4^�����
ja��y�>����t�� ��j�{B�1P��U��E F��Y�HN;����T6ypԹ0e�2��1�سφ�ޔ�h���Y堟�>��T�^�GE{x��d��*�X�l�i�q�X�������*~�X-���%�8���������ܕ��hr�#�	�ݹwyȬ�s��G�춓�&U	�v�~F}D}S�
դJ�U�~Yu��A3�8[>�
�x��f����� �9pr �y2�q��.�e�Z��8A��8Y`j�����v\�e��n���u/[��KR�V�l�����ă�@~�d+�X�OlL�ū2}�h_fU��e{͙��%p2��,؝�C$�����""�h��'��.�������$��v'u�p'ƒ�͘]�jh��Ԏ��	/�,���P�YB�N�~�4|�w��d�0X8Kn.mؾ=��XQ0����FMf���~�;x����I2���w�w�ο�eΥw:�JB;+|�jYE��Y���Xm>����;�^���r��quԇQc�݋�Fo�oI�g媲�k������k��V��.��ѲEwg?H}���&��OTWg��؛��J�P�����J5<��=*��V�P���Du��.��r����(�3����p�qor?�wqdG����!���8�B��9�WH��
���7��� 	����b�v�C��{Xʩ*�F�[�^����+�HQ�T*�|6�L��7��19�Z=���-�T4�[�L�nu�d�劯b�LWY��,2���D�%q95R�X�ly�����T4�:l��)�������������i��߸����,#H��`��X�M�*�|��1���c���������F2�&�7����c��0���L��gN��3P|�6�{���y����]��?%�/9[��,���^�4��E�H�O:�e%b���2Ķ�Ÿ�K��X/��!z��^�P%��Df"1�6�N�����x�<f�zJ�`k��gNZ�D�=%�zA%��f�HE�;����U����>gSO�]RAFj�Tzo()�����塀���oeK�����ۥ�)�J��*�J�����b�I(��X��z�yUyy\��ka�2WH��%>�z+�Ŕ��he�3G`b��	�"���ȿ���-�!�l�/&�f0�A�2eK�j x 3�3�Ō'f�y{?&0���Ǚ�Ʉ���,`21���Wq��I0�J�9Fc �,
���fq��l6��F��`0,f���lPVo��/q +L���WrX��͂����v�7���`�y0�Gi��q�2��,�1'�^2�!�Xx��|DQ�ujb�xA0	��+� �z��4�L���H\�}8�5�!
����e�����!��,\�a�rX��1��E�!�h�m�C f���b4Zp�f�`x�K$�z�b����)����7�ј�&*�n��M�}Ì�EyQ4E�"ZE�<�O��~��t�OrȌ�����7�Yђ�KV���[�F�դX�V�^X�9\�C9���^.KV�ɤ)ֆ�zm�8l�,���c���RK�t`L9�_Ɂ��#���T��bW<�oLu�U���l��]�$� Z�.�9��s�Ӂ)�!]͡2�Ke����r�*KI�M�q�6�m�`�>��j�e��9T�P$��}�D����aI�ɲ(���:�-����p�����sb�T;��~$���n��y�����v@��e`�>�q�?�a����hxp�}.��;z�e��حJ�CAcK�q����KN{��r(�r��q��G�UŪ(�IὊ��U�*�Cf�s��Ǽ���H��i7���<�[?Wr(ȡJ�*�P��&K�݃f��G���K-]ơ^��e4"��|/����A`�Ȋ}Vv�C��\�	��@c�e�*��A�RK8@���W��� �Ǒ�c�X��]��8��q���s�Ca��B�j!�F ��7?�9�Π�}ʉ^_l�ژ�T�Sr��)�\.�����E�Z�  �Mș�J� �����c߳r�ߏi+�<n�ۭ��V��V�v��	T7�p��X�2S�9����p~�#�Ns�<�[� �9<��U����Kb���"�!��z���g4Vx"�;b�ˋ�2���uz=��k�xlQ���C��p�de%�K�Ò31�,�AFc�|oq�}͋^_l�Q����S}>��k���hl���	���d��{�'�  �,�L�6q�����&\e��"P � ��q`�H�>��<yG `rq /ng�ň��G$���p��U��ԯ{�4G`jn�¼���Q"E	`>�@�+��p<������T�'���c������p��M�r��-4́��!GQAU)�E�+I�q'�� �<��]
*U�p<~_(�������˿�:6H=�s��@Ŕ�L%�T9���J�u����N�H~��WX�ȅ�Ta$����+ ��C	Z�
� �C�ݣ_�r��\�9�2֘B��bHT7�>4UQIaIq^I��^�Y\Z���Z���e	���h-�g���B�}:����m��=�7����W72�_ʙ��,GA�GO�j��S��!ۇ��a�'�����_��I�e�I�)��n�F�^������kg^��B;�>X���[�/;`e/�C���^��|*�XA;��<�m,���X�:�N�<o�vn5�a9]��߮�����b�"�ź�4���,���=� od��Ye�P�����Џ�Q��'�6���i��'�r�L$�;�` ��s�df��f�ȝczK"�s�{ٷ�,�}
��	�ཹs�g1���9�5�s:xA�܈��s�&=���Z�	[`���w&a���!uEmh���8�W[`1��zX��C0���gB�mN�\~_�m�=(�Flk��Ѓ�p<U�Y2l��6�:�;��d���sV>��;kwϯ��Q����ծ�7z�������ժ��;���h޺ih���;6n����Oe�C��up���-��/���F���d�Z�n�s���FCɪ��P����[6����*C�E�o�1<ڹeh����᩶ڷn�V�UWV��:R���?�n/�@8B�
����E�pO��� �6ܩv�k�O����̣���^t1Bx�������(�шG�	K	�쯃�;��!�������-���mr0���m��n,�
�����A,��
��{��Ϸv�.,^�Z\�1����֡`g+i���JP������2��XF{�,(�A�Xf�1��z�X�a����u#9I�ZxҬ-[8�w�'��u3Lw�7�:=+W�� ����q4�/����\~���Cx�'����C|j[����z��Q?���.X��θw5�'Cw�
endstream
endobj
125 0 obj
<</Type /FontDescriptor
/FontName /Ubuntu-Bold
/Flags 4
/Ascent 932
/Descent -189
/StemV 172
/CapHeight 693
/ItalicAngle 0
/FontBBox [-170 -221 3475 962]
/FontFile2 124 0 R>>
endobj
126 0 obj
<</Type /Font
/FontDescriptor 125 0 R
/BaseFont /Ubuntu-Bold
/Subtype /CIDFontType2
/CIDToGIDMap /Identity
/CIDSystemInfo <</Registry (Adobe)
/Ordering (Identity)
/Supplement 0>>
/W [0 [500 0 0 240] 11 12 356 15 [246 340 246] 22 [568] 29 [246] 39 [737 0 0 702 0 316 0 684 563 897 756 0 644 0 667 582 0 707 722 948] 62 64 371 66 [500 0 553 604 500 604 584 422 594 589 289 289 579 316 862 589 607 604 0 422 485 444 589 550 784 0 547 500 371 0 371]]
/DW 0>>
endobj
127 0 obj
<</Filter /FlateDecode
/Length 346>> stream
x�]��j�@��}��l/����DH�/�Cm��
u��\��]�����̙=ì��Y��I���
�D�����_ME�L�V;�/궚V�Օ��Zq1�u�nz'��p?mv��,�u�g�}75�V_��wZX.���K�IH'IDM���ZoeG�e�&�m����<*�恄���M��4eE��rbiO"�=�C����Vٹ�~J��-�җ�Bޖ)@���GLa:�"P
�3��3x�B	�@>�ĴE.����qws����ew�;����!���� PbT�#����Aw!�l=*�*#��(���`yY��\�;�������.m5ݟ���j�� ZU�
endstream
endobj
6 0 obj
<</Type /Font
/Subtype /Type0
/BaseFont /Ubuntu-Bold
/Encoding /Identity-H
/DescendantFonts [126 0 R]
/ToUnicode 127 0 R>>
endobj
128 0 obj
<</Length1 20396
/Filter /FlateDecode
/Length 10258>> stream
x��|y`U՝�������}K޻��KB^�@�˾�$`4�����@AEbT���Z[��Cv7���v*�e�NE��8ӡ��:v�����ܗ�����������Y��������� �*���y��v1 1am��ڶ�����밼�}n���`�z o-�g/�<,ܝ.`y u.߰b��kO�oЄW�m ���2*+�l]~�fW@�a��M+�nI*�i:��r ç+�����Cl����
���_ �3���r���w��܍s�q��e������8�ql?����N�6@�ϱ,��_;�ת�X��oӆ�C��5��:��7lܰ����b�n �m${A�}_����V%%��38jT�5P�������
������Tx^� ^���:z�Q��&�Rk4D-<�HS=�/5�jo���^��7�0!��h�h�����
"�6D���Dt��n���DG/x}�C�_�/@ 1	��!1�1!D	$�ϐ)��Ð��a�D�O!�c�#fB��������,�l�"�@6b.� �A��	�Cb�#B!bǙP$�`b1�(F,��2(�����2��X�s8V���P	�1�UC��*���?�Z�A��Z�z�Cl�����	����[��Z�a.�vhC���	��q>�Љ��r\��C7t!��B���@��;�z{a1���J�\� }Ћ�W .�+�A� ������R��q%"����o��q5�5�q-�B\��#�;l�5�W�Z��`#�!X�8W!n�6"~���0�V�$ W�f�k`���V��p5�up�����E���N�&�n��o����zě`'�n�qnD���(���M���n���f�=o�QĽp��+�nE�n�	w�Ļ�v�{`/�p�>��>��~�q?܃�-�W�< �����0�G|�%�<
 >��qx�	xH~�� >	�"~C�.<���{�4<��|�{��g9>ߕ��x
1O#�g���!�g�s�p �8�18�x��p!� �_�#�/!�3�G_�c�'�8�)8��}x�Ux	��?���2�8�8��pJ�'x���t��מ�kO��'���/{��c��=�מ�kO����m�%�ݚ�}��MZ�Z���ܮl܊��f�6��\\��\�=\��\w}\_�\;\����%sr}
q푸��p�H���N�ҍpY�s�ep	ery����⼎r�fs>�p~�r��q^���b!�H~=���9�D?E�o�o�'�'�xW~=ѿ�����7�ߣ'�7���.�o�'�q|,����ψ�0.�����PE��O���心bF�%��c�#n�GPO��k�@��B#I�Ǡ�D������4��B�62K~�2�v2G�>t�*�t�z�$�#͈�I��2, ���B�%XHz�+�����/@Y.��d���rr�|z�f�(\A��G�J�M>}d'b?�%���f�yXF��a��)�a�܋���/��A�9XI���U�I�{���j���!��O�Zrq9!?��I�����*�"c򓰑�q��������������g�c�Mr^~��_ȏ�V�kīɿ��5�w�Cp-�H~��O������ȸ�-�A	��T#�;��j���]����&���4(�#4,�7�t�.�Y�p�E���w�m�X�{�e��p;�@�K��=pm�o�;i�|+�E�ʷ��t�=t�<
����Ͱ�^!��}t�����`?]��-�N��!�Fx�~S��W#>L����#��G�ny<FG�{���	z���M��t?�w���5�]��|5<E�D|�>-o�g�y|���	�ң�����p��"o�8}� ���y�c�C�������#��Q�3y�����8���N���k����x���%���^��)^��-���t\^	���}A#��W��~ XOy�ny ���~(��"�}}}����-���o�Y�B���Y�2���n���Ͽ?�y���r�z�?��Bձ����B �E���<.�ӧXO�bQn���R�i$ӹ����W���=�T�\Ck�Jz^Б��ˠCo֏:҄�6e�NL�}�/Y�6{�I~�ȅ�Xہ67-�}Y+��Mh��ֈ}��ߨ@���'oB�?@�	7��8����,��X��X\��,�O0׏ϷἭH��RP����W/�W�\GNs�C���k��y��s�Z[����jk��b�s�/�]VZR<+/7';3=�Ny�6�j6�:�F�(��p}�O�Í�9��Ǌ�)}q	����K}��4�g{.�\Ϙ�36ٓ�n$9�R]X��^���ŝݘ��6�#�/�|ϫ�y����|B�󮬕�O���o^9Z�W��4j�5����F�1�o8H2+��̺�)�̌l\����;:��j))=�j�XqMM\�ǒV�9�-���S��ai_�4迼;.��C�B����-���ϸ�W^\�`<;\[��q��y�H\���ǀ�_���5��MD�X�-q�M�>���ח���r��,�B|Gg�R�`i�y��E{ⴏ���hqu��-����S����?�Wz�;�J9��}��l��Bz��e+Y�?8��U���;��L�?�ֺ��yؿ������;��w���X!1����I<w�ġoY�x^]-��T7�W�L����>�Q��gJ�CE���y��5(�������P_` �s��H��z�}=���&����>�K��S�������V���nz���B�GW�c����E&��r��`�RI�`�i�`A��4�&�=Z�H�IQ��2�@bN�H\7e,+&�й�Ԕ�lB3����)�6�:1��h_>O�x� �O�8'��Z.�Q�W1)z�8tH���pOu(�����x���2?�ҹ��K;�%�����ɶD.NkP룁	��r/O?��4�,���-�G���Ā �6�U6��Yj����zto����$J�����KG�b���V�fㄛF���|z��f��x�nYP���Χ�`��t������O� �ȂT�0��������s��Y9���T��H�!q��CU�� �S����լ���W*�V�E�7�a;��������5Ҧ|NL|H-��?c���pɏ4����>���G�K��g��jn����H���y���+�/f�`��1?�S~ΛΛ��Co]3��ۏ_i-�|���G�G�Y�������B�Wq�z%�U�W��Z�b��z��\Ot�]�M��.�*/���)�/���2�.${�ߢ��h/��7�q� �#F	<����cݧ��"���:�I0�`��L͔LN�dҫE�)>��n�� �dQ<j�;m~��!ڈM
T��n�Q����jONr�-F��h�����V-V��M�B��J�{����lE��S�NيlEEJ����z�N���&��}/�#�oa�����()*)B��.�wI��Lɝ�]0w����;�.h{ ������w�/x�����cǚ5;�$㭇�ٰ]n!��O�,f��ۡ��A����!��v8�U{y���D�a��Cv��s���[Eh��!+i�)r�b��6;�b惉�CV�~x�m��v����S�K�B&�ɺz�y��
��j��Y�=�iԇ�g�
�!��~�"��t{��d�L{	�m��orCj����_V޶��y]#���-z�4ކ\����2��\Ys��6���X;�����C	^�r-l�"���ˡ^�mv�Jt"��5�6�� Z{�|�c��P���S[!̚��Q$.'�N��m�f9~����-�y'@�|4����b6�i�Ƙ��7�FfϞ-$�_���:�Xb�Bɘ���V:S���1���*�Ī+l�EH/Y�����1���yXxC���������{�>�@�\���#�h>]+��Q[��/fb&G�p�ުy ��̄�]��{R�g�,.*t���#I�&%���~s09-#�v��U����( Z����vcF����@S{4:�����
�ez�]��	�@^�)-:ԨT&>,,8.��4lAB�1}'fE9vf:]���E��L�U���uLا8��ť����$�|ꐋ��13��0-�8.���3�,���D�;�
��`�Z�;��b)�����p>>��f�ʌ (a.����u$K8�/aX��aZjdȔ��i>�p�Clin��&��&�ͿG�+�-��S��e�~�(��u�)��mj3~���sV�����_�w�m�¶2tm��2�����г�
�X�Ӷ������r'�6�\5|�&��b�IͰ�0S�
���4h�E�t��\N�P�3��%Z�Nͥ�~L�"�%3�+I.Q����J��"ܲ8���3ۜMj�3�<ӑT��yѽ�*2�^6�ݨէF��W���|�����+�[���ԩ�hm�?'�غ��Vw�u�oZ-&{A��ђ˫#-۾����"hU5Z�jF����w�c�}suS���1���Rg��(.@��G��	�Z-̊4j�J��	Z<�iu�}�a ��>w���'��:�A�&�wm7��dW�6���M��G~��\�}~d=�< ���a=��8�>��D�P�Ĭi��G�D��\�ݡP>�`:e�j�a,���T�6��%!8�MXD�1K>���ka9�93�P�sz/>��Ж��&3�T����ƴ!�e�FJj����`���8�Lb>��rG~�Nc^jdę�#8"��3��#�N?tB��Q��3��Ǹz�덞�0f/�-2@4�?�i��s	��I����T�
�)����8�2ӑ�xdI��ߦ����U�&jU�ڣ/��*�s�5ƀՙ�TX;�f�@��2>���x��i^[��)��M��\��S��V	:pB��2�8?B
�f�*;s̰M��:#���-Vn�����j���#O�����1����=�e����9�Gv���x�N��{����K��;�#�:�?sq����/��ND)<j�F>����)�L��G�#U��dI��<5Z���^�{�5-6�O
^��4��e���zO��řTP�Qw��Ag��_�㯸��RUNK�,w��@^���R'X`�ʢ�cF��m���<+�059l4A��q+�|�z�k�إ�H�3��`	Dv:�a$�F|�������+��ų���2�^<øp�p��!3l?WܖcR�8KTZ�S�d��c!?��W�����9�����Ys74̸,bO-m�!�ନcF$Y�s�5r#z��,�%��6�~��e��<_^U�ע�:����k�Fu�ч<�˵t.�r*�����~�r������4D�L>�$2Ui��V��BCf�"�]��O9^t�L��"��b����>f��R�C|���+!X{+��1��Kj�l#I�dh22��=h\�zH�C<�n�.�B��Е����B�4����B�9����(�H�<OsFֈ��u�G4y�J}�^�7Ce���!��V^�2��-D�}��W�YF�����'qyP$�d�&�h��������1���xFEN�N�M�\����Ŗ0j�Zsz�ʹ��aO���{��o*^\���ƙ>3�atw6���QiM����)�\��d3ɧ�uK
��Y�Պ.� =��c�./��E���4�-f�c�1�d�{IT�����#�x�"���g�f���6[�}�A�Ah; c�2��Dw���w{'m�����	���E�a�B���af����c�"NU���Lk�.��V�O��?��蜴���O>I��Ϝ�׍�E�õ�E�}�%��0V�n��v�&hwZ�!<�	�/�S�JhZɶJ�C��
*�f�Y%4�&��WPYy�Y��=�;�ޢ��(㳀R�T�^�'���HYTwE�O�$��d�|�\K�q66H��1W(�;�9��v(Tr3�b�jv~L�Q�%a ���h �����6��m!��v��mMb�~DgQ�S&c6��?Q��f��D	�+�T.�L_�s����[��2�:s�,[z�Ě�����M��/#OY��9sQs���N������cN�Y�#И,���>d�B��i��w����-l��ÍS�1�a1�6$�$�,��)1��;N9�yu�?@���TL�%H�I�x��Ϋ�<dQ*������C>P�^��2�'b�DsB8&��kGOc])�S�橋�c�!I)Ъ������ױ����u�8���=����{��	|�"�36���Z�>���٢w6;��M���L�� (c��F<��������3wc+�\|v�u��D�J���<aP�%nH���e[�jlJ�eY��ŕ��e�E����kkO����E��w��+6�b���C�&'%	��P0��\�z{*M�O�
I0��1�Gtz�N���-;�eѬ�#9�Μ�9$'�}*�f�f��?U�#�����`sr��Y��-r�@"�P�vO��ܘ~�L�A�f/�������>�X�A�K�L�$��j�����*!�`�����s"�V��Jmֻғ�r'�jV6��ϗ'~�wK�ꬬ�6C8gur示����<eI�4��3[fO����Nv��V�z����bK�j�)aw��Y|#V��{�K����6N�P���P⤄~}��,�ޚ�;&\݄��,R8��髦0�HY�4�p?�T���Y�K�4	7��ل��F>�5�DUI]�C��X0��jhX��ag����;��D�lQʱs�Ɣ䝂���7^/s
^��wD�!�����kb���*�����:��5�􈦠�<��2�G��͘8���4n��X��P��.�h�cM���3;���+�N9��@Kq�v��X��N�>��1�\X΋�ś�W�z��։��Kyĭ/Eб��9����\�a���	���M��Mܽ	.�˭�׌K����l	[��#��)Z7��*q���V��fm��8F��CgxT�&��S��{{�����zQF&���-S�)�:�(rMAC�'kѮ%F�!��Dֲ{c���TC 7͗�RH*�ɬ�~������}|&%ى@]�J�M��Fl0;�����a6��X-N��j�[���&�~Īf�8�0�1�6�#F',&Ӳ(,a�d�)����3��V4��˩���B�N7a���Z�#�S�x`0��|�E\���A��MZ�V{D�vj4j�����{A#xMj�h��uMN�;܍N�R,+/�{�[���{���Tx��B���{�$�p�8J�K[�MF1��[�-��3:��Ҳ�K�Zk���rF��,>:�7y�d��]�b�"_��}&�a�~<���^.J�,��y���c�|S[}���fv��D l������$� �$����~#�эjP�q�F �&moAlJnrzF�F��<M��	����P��z�1[�/o�W���v�D'3��M*X$�oMt�iFQP ��<I�o�,kȒbM�%I�x4Hu��L�䩯$:�kA����ӯ���ʼ�s�]��X����FsV3�.��Vȇ?Ť��e�P.��t�`�22Mfh͐�<��0�ϢL�9l0B+��N����Oc��I�<X��fSaRr�+YQgVV4����ݓ����ɴ;��5N�ƪ	i�Py���n7�S;��19)*d���ޗ�c�g�c��h�2��P6'����[g&�Ëgş���&�ǳ��^���G�
�2�EWh�Ë�!����2����]��NOv��ƔYm�*{ +��FĜ,�M������q�.�JI'�@�~8�j��I���n�����T�~�[/9iSQ�'r�jIJ����P��H�	�P|[F"���;��{�X2��<��ӝ�B:7��U�J�]�(>�qr�Qd�L=;�ZXL���߮�	j�5�	W�-�3ᣙ�5a��s>cV43gRx��Q3�2��
�nw��hRr�*Mcw�ч1�-F�)����?Exy���ų(�IbS��bBv�^|�+��x��"%%�w�,�3�7>+a��Cz<�I�I2iFȥ��$�S%�.�UI�+	��A�Z�[J����?y�å�$Fž|D�(�k��T��gLF���?����4�_EC�e4�ZFàŒ�}ۙձv����}a��4L-�J�#���J�j�+Pء��Z5}�,�����1N�t*�L:,!�X�BL��4�_EC�g4�z5�0뱔����6�sIa��h�=�J��BC��`�vEi8˙z�5��c�e�4e�豑�Fm �`40�VeAN�B���h8�����0��H�fVQT��˩(&+S�/��4e�F�	i�����3����	�f�<�r}��q�l�hL�0cI��B��Vhp�2�2�K�P&<���4|�W��|��I�b�h��`I����|��q�a*��i��/ߥi(�Z�D�V��n+��1(J��4�_ICdUhx���h$#vL���F�h���(j�V��։8o&)4�z_N#��4���?��i�"�l6Fä�`�RPq�	:�n���*�?��t6��6��iXy{J����'i�H#ti
S��iؙ"�V�i��q�d.Ao�O�R��������������Yq6�IU���bt8��4R/MCa��Ŵ����r��oD8;oO+4|�F��h�\Lk\.��	!�,�sRhdF��M���iZ���K�0s�c�̾��6\��ƒUqޞ��8��_��qi
S<�5�����K�BCaZnTqF\=�K0��E!��4+g���$���^H��}L�X����)Έ�3W�uZ�y���L8�ĸ��d2�aFRR ������Ņ���b������S.^(�40�J2g��I�&3`�~�u�]����3`�d�M�tx���4�	K�$Y,Aȗ��V.���T(ʟ̀�����Bťi���H�0ND"6[J"��WTIi'>!�@����3~�B���i���?}9���7g�/2��9��ɊO@ X�i�gz��>_%<�����^���<��qj=�`)�B�dY<M?̈́V�3��;�����9�C+��;
4��V��.X�����xZ˕T>�����PT�S~��Z���.�j���� h"�y�%���ߘ��J:y<.��D^&R��k�>�}D���p_"O�LoM�)�w$�ʸ<�W���&�j`��S��}]�6�:F́&L�a��e��\(��i=�i=jyn�`�a�V /�Q������� �n������Oo�58�؊}W�s+�NB�χ�H�ڏ�]�{^JP�eߗ�<���!��a�`��f������x�Ӟ^����]K7�ޔ�4ܿfղ���V�_'��)��Pۿfx���������Dۼ����o�ݕ~JC��[7�Z�rX*�/(�j�׭_�jY�	Ε��U��H��n��WNX�~ݰҼlP*��W��?⽋�/�/^'�@��!�ʌ�+ᝏ� �}xS����Ǆ:B'�?�z�ɐ���.<O�*��^��.��T��Sr2k	���{x�D{[������g:��{F�{�<�4yy�K]^<��/
^8��/N�<��	�;O�BO���'\�'�6�8B�=�	=��1��z��CU��z���Bߺ�ڏs���GB�ha��;��{�����'CwW�N��A|��{C����!��\���Cb{J/��Ci�[ܡ[o���(!G0�U�ywjhd7�l��;�б�o7e�L��ٴ�ބs<���7v	�(	ݸ���'C;񾞼�A��t��;p�Ť����T<,>uX8���[�Bۮ)	]�u t�	]���r���t+����B�ܴ=�yh ��l����6QqH:5$�q�I��o?ֵq�����o������%K�V,��k��ޮeK.�Z�����faע����{ۺ��m�����ձ���}�ܮ���d�{Mr�а���~IuWݒ���Ud������'{[��:�%��X'#��|����q�H�/�>HȞ�]����-�����G�{Z⍘����@�A7T�D�0�F����b2��KV��<D���ÄWD�X1�:k�/k>+��!�F���1�Dp4��x�� �(!T
endstream
endobj
129 0 obj
<</Type /FontDescriptor
/FontName /Ubuntu-Italic
/Flags 68
/Ascent 932
/Descent -189
/StemV 281
/CapHeight 693
/ItalicAngle -13
/FontBBox [-167 -190 3585 962]
/FontFile2 128 0 R>>
endobj
130 0 obj
<</Type /Font
/FontDescriptor 129 0 R
/BaseFont /Ubuntu-Italic
/Subtype /CIDFontType2
/CIDToGIDMap /Identity
/CIDSystemInfo <</Registry (Adobe)
/Ordering (Identity)
/Supplement 0>>
/W [0 [500] 6 [654] 11 12 317 15 [246 293] 17 30 246 35 [931] 62 64 322 68 [544 555 0 0 518 0 550 552 249 249 517 0 828 551 555 546 0 372 0 389] 92 [478 0 326 0 326]]
/DW 0>>
endobj
131 0 obj
<</Filter /FlateDecode
/Length 327>> stream
x�]��n�0�����.*��I������@b:���^��6m�E��;�1AY�*�;|�Q��x�kea�Vo��kF\�ҭ�o94�^\ϓ���������g'gg�9���'�[����.k��՘_@;.XQp���ژ�f �l[)��ݼ��G��l�G�!�����4l�/�r�O��?����U�v�X��r!�]�P���;"��B�@�Q.�\,�ND{�4AJ�,"ʈb��虈zf�3���	�����ǄG,�)ڣV���%يi �<P��N32��C�7t���}ߗ$�����O��YV�k��7f4�jy� c��
endstream
endobj
9 0 obj
<</Type /Font
/Subtype /Type0
/BaseFont /Ubuntu-Italic
/Encoding /Identity-H
/DescendantFonts [130 0 R]
/ToUnicode 131 0 R>>
endobj
132 0 obj
<</Length1 12328
/Filter /FlateDecode
/Length 8428>> stream
x��z|SU��̽7�I��杴i���-
�@
��A�iy����(-� *,�ǂY�E]�T
u?WwDwu]��]���
���ޤ������o2�3�1sf���I t ����i�W{�0���W����n @�������jj�ԯj��6q�hj�`�Xк��guO�� ����Z�Z ��ƛ.�~��/�~`0�V75�5p�rS��/�?���z) m#�75��~Bm�j��D�iiK}��O��E�e~z��V�r�p�dب�]V��8�X���#���Z[�ڥt80D/���hl2��F� ���w��c��~���\�����r'����q;T�{�u���hT�kF�p\�_9�QzTf��~�Y<~�;��U��	�dX���9p)x��Q�G���Z�i�k��C3����+�>�ΏեY�������(%&b:|� o!��y�'<��U8=p4f��Ә��/�����Ӕ�x>��a�O��`��l�[�i܆5І6x�F?�nx�,x%� �������8���,C#�Ǭ�|-��/i�/q+���2��l"D�q��y���?�af3�Qx	��ZX��/�k�`/n���x9�t�g�E������
7�&�^z�RW��?G ��v�ŧ���U?ʶ2GM�}p'}�ѧ�ex�R3qw�z4`=ׅ�至$�f�%,���)x��3P;`cI4vbL�,|�zHu�Uӥ����E8�ҫp\j��g�!�W�~]=/}}�e��D�ê����sׁ�{C������ͤ�'�ք��fTV��M�v�5S�L.�,)�8a�X4nl��c
�=*���aCs23����<.��$	:��W�8�A��F0\aӼ�`���_W:4�[�j*�S��#�:o�^\���TA��"ް7�N���pD���)�F��#��-�B���9Y��vcMy5�7�C��J}�R�ҕ��>�P�����D���:K��#v%�&�'6��@�.��	T�d�[Ia�P�0�%c��d��Ӓ��HYyuI���͙1���.��,QO��ʒ�E2�p��+�D�n�g��u��#l��dK:;7D�ّ,q$�\���H���$�-�:�����IbD�f�{;�ڎ���/���1�4�7 W#��VT���$Ywv��`g���;�1��5�;�����7�U���#��#�M��)܄cB�+�F���&-�m�#}�����>s����$I���p{���(����0�} ���P�	�='�z�UrOG_O����t;���3¥Mn��o��t�'�Z,+�o��u����� 7���W�y#�t�8��F��iR�oc�/�D �l��iy�I8�]���$���!̨���T��+��K3�¤�EŊ2#��ֈ�?�_�2[%�*��)�i��E���Hn�r��%����Z�������5��>��*�;&����tV7,�x��:w��n_D��C��Ɛlv$��w݊q�[�Q=��?�����8#�y9.��e����2d�M��[͸�4���B!�>MC`"�+X�p'z�)0�&6"Yޒ���8�}٢*ٜ&���������R�/�=Cs���	��,�Ҿ.rSԡ!��X��dY�d��V��!�7"�U�{�ţH9.E�q]͸�5@X$&�Qw_Cf$��(��$���,��{r_��S�Z�)/�/H�/mrd�2�_ h?�^����r�;�DQ>�Mc�E��:��Յ�h�'k�7ȴ,0�Θ04�\ۄ.?n,�qceM�aJ��gT`����L}Շ�4,#ce����y�
jh����"@���)�]ߍ��4}8��n&�3��+�Dʭ껹X��7�#�&��Pp����D�JԈZQ�wʨ�9B�T�pPO��E�*t7vtiEwlD�cn���tUM�A=�4�$B����Dʦ�R�m�eM��3�8H5���Ǒ����>��7N�$�'��"_ëe<O&�������P[�#�Mz��i�B�T��J��árȧ��� R�)����f�r8�:��w?��C����~�������t�������Յ���� +���j�h�4/j��R�����n�=��>aJ�A�^_�̞��Eyw�:O(�����׾��ҋ�Ki�zUw��XM��P��z�<ɀ�TQ��V�UQ2�'sO�-XP`�#��>3�3�ֱ�zIN������H9�}�Ff3��ut�P!	�Q(�V���>;34�����G�x��@��T�;k�� S#Bf|�2��i�9��[Aw�E=]!��L�PT4�G'0��p�M��^Y�+i�,U$@�,f��S��6�Zj�x7�E!ٓ�%yw�����j���j�����g]�!ʔ���%3��ys�$�\�O�lQvg� �l���,8r��nK�@ި�������|�5�?�C�hHu���Y�5�ұי_I��]dT30���=�Ñ�s瞌<qj�_7~�=�ĳ��k#�=��LP�2�`b�:^��y�Z��m!�P�prvY:q����F���M��߃�f|�q�[W�zϰ7V��vÒ�����bI,E���($k�=�#=�\�<c�Qea��^(5-nKB{��S�q��B\^�$����Wfd���L�R�i�HL�M����o�;��Y�;��f�Q���ͫ�n��ٟ�2w<����g�)���3�����|z��[�?��N�S��8΂�bq��lV�;9�W��~Y�C�y6����ͦ��"�t��n�q�i��5�Š�3�Y�����Y�ʟ���9J�R`.�q7��p�l����4)���������Q�y�(oҞ�\��չ�������ʢUwn�?����kg�j��Ⱦ�퍶]w��$�>�ʋ=�Gg͚���ʩ��j��gk~���=ɜ�Q:��HO[�2ttp
��ʢf��J�k3�Ҩ�j��j$�Y
r-����+4�t�|��3�8r�h5�>�O҅�uL%�9*]�3I��	�=����*[y�7g���~f�j�4^���z�$Bb���D��j��4�Qv+�Ʀ��n�ʐ�����]͑�p��Yy�;��x�}c&������+E������Qd@\��/�S4�UKoX�x�����ވs�}/~��oz���O9k*:V6��e.����|G2\K�ג�8����YRS���EF38�`�v7�+��Z�N�VP<��<C�6�B����A`6��T�aW�^�X��&�W+����
��Ζ�K�eE���+}�RWӶj����؂%8�x$��7�L-��T�-��wu�n&k(V�!G����y��	z�h5+CZ5+�� �ˆ+3�#�,���q�ї�7�!���p�=��F9Ə�?�=i3�*L�J�A0f���!ɚj� K�'��u�t�t_�*�"Y�)yU�ĳ٫�U�9�3�����Q>�a�0�W�9й���A���q��bKߞ�B�zw���߿��ww�ذK:z��y�C����eo.^�?;�ڟ�v�s��,������ur�'�j�Rs㢖��K�V��*~�^�N��].:[��x^+��� x�\�,A�������ϖ`�?hr�H�9�ъ9�$� �YB��U�ȫ9��ؼ�f&}_áw�������ٵ�ͳkW1����;v?�v��3S��}���'w�p��eK7������X%�g�6�e9 ;Pq;kUB��q�q攈����X�e���{?Y���(������pZ��@v���-l$��~����@>�y��̾��mҋ8��R-��*����|���}I:�a3�!��l$�}v҅�ܐ,��u�R� �8��X]]��G�g)�Α��W�쫝q��"�}t���*��;�����YzS�����!��k�-�Z��޵� ?z�R��^αŭ��l9�����ě�K��<#4�6i�����/uI94}ʈ�Cӆ-���̝��B���ZV�oCtPa���HŽ�V8,�c�i�;�k!F@X4�G����%��etGO�^��4�#&�F�ț��P2�\�`XY�(��e�*g-��ٗ��H�d�U�}a����,[�h���-�oD+od�����y�l���%��Qx�^��MM�����Q�.z蹟הY]w��7;��g��O.3���OH�kK���uj��qy�e��{�[I;�D;^J���Ub���q�����M�e!�ɡTR�L�&�Ƀg<Z�S��'���_��m��;����h�ޤ�D��z���:�t�PN�6���-l��|c����@m��W�kI:U_�[���W?��>t�l�ˈ�*ҍ�b���l6-y��$��,�ѡN�6��dc��`.ɪP4!+@1ρ�A�T��F�Iv*#ô~+]@�?����>ԇ��x�l������0ը���+�{���C��H�u����ǈ)�:k��t��t+�e!�����B,�P�#�-y�~�5����Z �$ks�.j�#�.ג��N[����D��~k}��E�q���3��0Y�bf������a#3h_�ou
=B�6��H�vH�*qh�^�Z�I		V�MI�X(�З��DO"cb���!�B\����<�pG�� f�O�Uj�%;�-2+.I_���W_��w��+����vt"o��%�Ff���vH������x����خ�o\}�l�b�����1ɊHY����o:��GV�0&�sا��d˧�6�]j
���f���o�q������o�5�na��T>�?��Z�X�CR[#]��pS)���b&ǲY�K��Z��Ó{zY�e7q� BNYH/؁/'gX .��z����j,��� �b��������#wc�0w|c������N,z GEWG�:�h�kX�tނf�����_s疫�~�N�5z���W[��q�o�g��s��O<zT���kY���N��d���tY���A��+B����S4��[�6Ƣ,c���=�_�w��I��k���J��kZ_�So�������{L�����I������D]:?����*�QH�U�&��/i�X�/k�s�A��Di� ��K#��&a�ŋx��s�L������y��i��Ji&�f�����b0����Z*k�`"{2	��"Ĺ�W��*��+��~���gn��g��u�fK0kd�����'�_���]��G�G����'�(z�yѭ_	r����:N�T��������#{v\���rH��ѧE6,��^&�7�0���>CZ�z��xB��]
*8����+���9�i��Gޅ��t83�����W������,@��}�Vz�ӣ2O�/`��\�4��1����E(��o"��!�GF@�V�h��TmjfV��<��du��ʕSp�mlw�ܘ>J~ڿI%M�����7��8�J����<_7~����C�53����YV&��jՂd,s�=�G��=�V�n��9��5���͕�=��ky�S�M�(�+:��:����$3g�*Bv�A�1|y.O����r]8e漉�^5mnٿ�E=���L`�d�-]z����Zr�{ִJ��r���䙗�ut)w4�(�w��Ʋ������p�)�'�J0���\v�t>��t�������5�-�kZ�T
�oR(3P(�������t���&i��v�4'z<:�D��t�`u���� ���40�t]�0. JL���)K&�F�]j-7��%O���2�c���'6.Pb7����y�W$I�Nz���4���ac�;�=T��tw7�3������D�Q��y��a�X���Ŕ ����2����$'W�ڰ��;��:.ﱍM�2���HS�cל��i��V�L�zғl'�P-��j�͝d H����!>��u����n�7�c�n��ՑG�<C���t���˲�F��/3�����Y��T�R���_d|g_رj鬦/�u��g>K�^?wACô�u�s�$,����{Ҧ���ȱ����sw��~G҄���і���\G;z(�5���A�?Jt��#�\��$�͡E)d8�d��?Z��k@�b�SKlRB���~�:��u�)��|�*q�ofQp�$飞�/����G�ڒ�o��ɵ�C�O���ph�.�b��gq�~����:+����Kϗ�hz�U֬�3�zՒ��<΍�}���L��Φ��>;s��O�=dC�e�N����X��%�?�iYڸ�T����xyV�N���p�C��UKif��R�}Ӊ�]y/�N�����{��8�1�+o0pVV�p�N��2�ӡ#��c��'����k����R ����M�0"�gV�}��J��Q� �]ؒȠm�ׇ>����f�`��~_/sh�JNY�N��_JyE�~���#�Ý�a�)���	j�@�D'�JŰ	�A�ǧ��x�W�?�
�<�����E���)2;��ې�k�x8O�LT�T-P�*!�e�v6���,�3����
b?�R���n%�-�~��)��Kk1���tU^K�n����e�p~�?{O)wZ�j�Ў�P+���5-	:�Egq8בЌ��-XJ���h9�N��:,�� ����@߯ar�;o�@p*\F�)=���hb���,�&(�^�!��Փ9V[�$�KbY�4����M�^���~���4Lc�7��%�u&�G�P���s�eԨ�%�Y���D@��د���MB��W�E�N�m'3��[��"��{f�_�}R�{����� T/��p�����&xfr'�M����w�	^��!���7�!�D�D���f�f�����R?���?�K��֍^��[L��`AAC|_k������%(!�@0[�_�y���C�kqҩH~.�R�C����l ���_-#<ѯ���J�� �s�:��YH�ulxg��#�������꜖Z����u�Tx$^g@��,����:GoB����Mz��V�z,���+�ک��`�R��P��K�f*#���^ȣ��p����\�ۿ����4���-��<�K�{��쾹���b�,$�{n�Q�נ���Z=�h%-�PF5�K��,e�I�é6�F�P�R�T_A�Z.�8�"����Z�*�\�*�s�6���ðk�o\Q׾�eٴ�e-C'�,m�ٸ���޼aÇ��q�W�G�o�o\�и�;�{E��{�x��E�nhl�6Ե�y�[Z�_�haS�7�>˛7|�p烙��K�[V���&�M�rX����(�k��N^V?b��H�䇓 ��`|6V�4��{&Π�΃U���{:�Z�_Co�=T^ `p,��B�)��c�}5��w>�<���Cq$��QO J1���	b�4o8a*� ��%,��Ke��!��)-�?�PՍC��_9���1>��?����qD��	��x�&�[���h�q���ԋ_=�QOѹ�s����}��~V�s�i̐���>�ӪOp����a�Rz�,#��~����Ǹ�-���=�!�z�}�ݘ)��7y���{�&y��n����w���V}��8D��Zl�fD8Zp������[lԳ����2/�P�^����$�����F߁g=���'��8��9��ғ����cG�<�Q��uG��N�L?��#���d����Q%&p/D� `�h-���J=��NL�\�S9���`?�q����1Y4�d#�
=e�����w~'vc��5x8zSD�^��1�~,�ػ���{4oo��[v��q{M{�{�wez�v�w3�ty���v1;��<��>ވ���`�`��<��.�)�~��h�ѱc�v�}x�/2=�_`�����ng�n�c8	K��6Ēd6n��!��DK�h�Õ�q�l�r��}Yi�Q��$:Xអ{a
�r�m[�m��s���hS6ex�+ó���6��ɳ����M�7q�Q4y30��:Kp��w)-I�^��YՖ�Yٖ�i'h+�x�a":�yЅ�9�uǩ��`7Kr�HL&;��Ã9��`���`�s���*>�V�Ʉ���#�+K��A���)fnp�gz7Z�D�L����yj�Ik��J�l���1ӈ>��#�XI\U���z��z�	󬛊Sif73=�x�ؒ`N	&{�M�Nf�&��`���tz)Stx&�!�.x.r��*'ګy�*3
U�<���.�
�P$��	� �
Ӆa�pV�
|��	l����H�[�fTfgO��S#ڲ�n��UʥX^Qo�@UMmu��[7o�	)S#y�ՑpJhj��*�\頊)��Bm�m�+�c�gg�g�Q���
�M������JĚmm�M���������+W�xB�͕�K5�N^�-[��ֆԓ�`i>�"yih�6�c��غ
gD�0�H��b}��>F] ��7�
endstream
endobj
133 0 obj
<</Type /FontDescriptor
/FontName /LiberationMono-Bold
/Flags 5
/Ascent 832.51953
/Descent -300.29297
/StemV 76.171875
/CapHeight 658.69141
/ItalicAngle 0
/FontBBox [-481.93359 -376.46484 696.77734 988.28125]
/FontFile2 132 0 R>>
endobj
134 0 obj
<</Type /Font
/FontDescriptor 133 0 R
/BaseFont /LiberationMono-Bold
/Subtype /CIDFontType2
/CIDToGIDMap /Identity
/CIDSystemInfo <</Registry (Adobe)
/Ordering (Identity)
/Supplement 0>>
/W [0 93 600.09766]
/DW 0>>
endobj
135 0 obj
<</Filter /FlateDecode
/Length 276>> stream
x�]�Kk�0���w9]��)��j�4��@�!ƅ��y8Sh@��=�Nh�6���Yx�F���u�Gp��$)��A���^��ݾZ�[5.�,臛���p��e�Bߌ@#����s�mZ����#UG�����~F��vn��K����O�k�4pO����9�^MHJ�V�[A%����F�ݛ�Μ���U��:P�(�*�@y)�	�-����Y���&z�[��\��Yq3*�#7&�������WI��ЅoA*�_�^�w��l�
endstream
endobj
15 0 obj
<</Type /Font
/Subtype /Type0
/BaseFont /LiberationMono-Bold
/Encoding /Identity-H
/DescendantFonts [134 0 R]
/ToUnicode 135 0 R>>
endobj
136 0 obj
<</Length1 20956
/Filter /FlateDecode
/Length 12267>> stream
x��|	xU��]j�}ߒN��4I��$)�İIXi"&� �AH@@F�&���0"* HA�" 2�(��l.����n$����Ά�{�{������OUn���s�9�,���0BȈ�E��٣���Y^%�b��LI�?t�x���E(.G:��9�O�0��;Yx`�w#D��T>����_0#čBH<<�����!�
ڛ&O�;iki�G�K�|�tbq	w���P�Q
�W�G(s �ۗ>P9�ļL
�R�4�M(��.o#����甋�;������;������������e�r�Ch����gN,�ەk _��A[=���-�X�z�y�(�]�r��Z�C�-| ƆcZ�&��'"�&�'���I�pq�FH�K&!|�����|��I �ڐ�X�9�R�YjlT����s��ӎ��g���	=��W�^W�iy�<�N��o.U8:�^F��N�:��F�����S�T��'�Y�,Z����h��O�=��WRQ�?��Aeh��.��^B��jLQ�DQ̝��r��C�|����!�D6�Ї���~1�z���Gṕ�o�z�M'O�,�VXD�@�0��h7.@��.�P H��+�B��C��պ�_T_�����+��d
��
ЈH�!¨��z`5ϡ#JYMS_a/-'ǉ��1��p����@{�Ryڊ�pZ+��w4��"C���:���o�t4��]��?�f�s�X�����i���j�� SC;�9�7�"y$�1r�)��*��
��\)�qo*��� ��!�ŋ�7$�S06��7j����:d�9�dg�߯��٧w��{���{Fz�Ԕ.��;$&ķ���y\6��h�k5j�(�%%{C�(+D���b��8�s�7�U:�sr�?�(�-�� ��99J��8�-� *nU\���;ZJ�RsKl��B��~o�� �����U�Ao蚒���%����=��ެP����"��j5���'j:'�Z��ZH�:��kq�>XI�Y=k	R�ٴ�Ҭ�P����n�/�9y`���T��ʐ!�HT��Na��om��u&4�(IW�/)�/?D��o5ͪ�^2'�:��:���+�J��
%�Q�h�gp˔8�Ǜ���[��v�mIq�D�7�B,"�CxD��]�l�uuu�ߛ]]T]\�X5��5��ku���,@7�͇!�_�q��WC��R�3Yz���!��������C	�e�}w�}��6���Z 9�a�����NB�!���{�x�!$�$C��՜j��籚�����E~������!.~`�?0^S��5��o
�w�����GJPi���L��@�j���u�6)����&H0[�=�0'˟U��]���蜤0#��I !G(�U��=���`S(����C6�f�2�����W�D��l�C��#�B)Yʾ�fU�����?���j�y��@��Ǝ��e	Y��%�B�"w	�I�|�/$��A�� c;�P�Kn�9�
���<�?x����"��+�p\|������a�C�x�7��i����	�^���*&@�R��_/o>v��� F��7k�H;�o3(�ةN�h��8�sܾ�/|uN&P�L=T�9MU ��B��?G)b�t1����'���RoH��gkc�Q�A����F�ɵB�	���)Ð�Nr�Fn�%ߜ͹�z`S��Z�<���� �!�XX���Vd��~��^lieCW�J�̥=� ��%������� O~��沠�x�~��A�������k%�|���c&�~���?D0�_�/X���	()����B��idTJ{�1�䪔ZN)P��0R�TMeM�#�2Sx�e"	l�	u\�Fjj�A�*\V��)W-b(�4���Ԓ�艻��CP�"�ej���a=v�B�Jq��UK�p�*h!�!\��2u����u�)O����]\�@lP+Y��(��EA�ِH8��}�L�> ��i�����~�<��g��V.�b��U@��fP��-�>�6]c�
�P�6}љ�|0�2#V'�L��{��9��{3~�"9d*�&��>��N��c\��Ž���O��	��~F�Rt(w�xB��S�NuA�	�B�&���i�4�5g����گtѺ!p��^�}���g���]�_k�
Ǎ&c�q�)�4ʴ����7��W�߰�,��/��˭g���1�Gm�k�S��_��o�_q;[ݝ#������������������3������}�s�������7<�-�5;�J� ^�� WE'�$RDUj��O9o��=�s�kj��3S�ٷ���2;��`!�6D��H���Q:IV*���Tj�!�/�AfJ�قz�R؈�2"�� M�I�Fי�N�U����Ϟ�����/��F�IQ T`p�
�R�Z��R[���%پ��%:�,hXH�5f ���Yȍ<�V�����s6�Y�S[�-��ZmO��	N�(���M��h���4.�O������X��A&��`0�n^�_�ߡ���z2̌���7��,y����z3�R�R�K0����7V�dFl�XY�beg%(���pk�>����,��|� e! �>+��s���Gˏ��>�����bpz>�M�����,<�?�+�:M.ſca�=-��K�ɯ�ވ�&5~ǽ�|P4�G]Q����QH�J��t	��v�.����B��>Z�M�8J�z!ȩ�p�E" ���LJJB.�S^Y �J~ ��&��%�w�������H�����ut����ؽ~ժ�+�'s��~���ӟ�~Q�Tɡg�ۿ���r���Ϋ,/��%��I���SRSB8^�E������쏰�-��A=j'5Z-G�?E�Q�87,����Li�8�	�l�t����:q�ݯ�8��X�k�W�K�<���ͫr=F��4�V��'"�F��6:���$:�S����s�ԫ��M�J�����e0u��o�C@B�H���M��)ՠ�k��MD��Z��jN5K�TGT�Zǉ�k�����r�J\+R����j]�(��$��N4�DT�P���\��w�Z��=�;H܁U��/�=�iۃ/�_u�Z�rn��%�����8���� e%:̍�#-�Ij���܁ �<�T	�5�;t�峓��|�g�C��Qx�z�_��H�G��t�J&�0�*��h[���0O6	����j�,t��0A�{�;�aR��$�����1J��}v|/I���������P��)i@/��PJR/1���+8I� �9��*Tx/F�a����(�aBG�s� �I�տm�/��e��|�9�r�D%u���Y,�	(&���F��E�.��"vE�jcEP-R{E�F*�������E��$SӌL)��o�חf�M�@�%d57�o���:j����U��^�a玍r�����O���8<V~R~�ô�ʗ埰a�O?��7b��$6���X�N����g4�BEP�F�a�+�L�0�b�>�Ag�� ��?=�}w�����G6b��Ӹxm��r�	�������l� S1�����#���8��l�T�"�FѭgS�)l4�@zܽNW�����v� �賯����+��f���ٮ�����6���Gޟ��ǫS6�3���p*T�Ŝ�[w�*��`���-�Ml�K���g����Iɉ��\4Z��Z,����>��+�lG�7aW�����q3�$�ރQU�o�:"ۓmN�.����;|i�ݺ�$�H�����07���?6"��q�ւmœƏ^3b��7��~8}������/�;}����sOG�=S�Wf8p��g�p�C�ړ����m�R���D�&��`D����x�ΣKѕ�8�k3E�����l֖��Hi�����3�C8.��u�;�)��3W�y��W���Q3޳P,ʗ:G��V�ͦ�f�xlQA���6U�n�nwU�<�Rq
�[m�0���p	�c�5`P]�� C��OPܠ�3 ���ٗ����=����t���3C)�װ4v�s�n��5�U����u�w�N��N3�
�G���x�R�9.N�i�N`���6��BF6��h��[� ���f
֍H}-;>��ʶ�Ԛ;�2����^����	"[���0��텫2V�ę#��?�ؾ��*N}u��Ń�~����2���><_�Գ_����ko�������;���8�3PA��%;X�LN��"Q%�¨�B�@�:Af��b��u������C�p/6�7\�")ư�)Z
��L�QJCS�.{gM�>��N��,�e�n�l2#�Pb�]M|��N��xj6{�D�����`HkC�;v�X��w�}���#[�61^k+{����o�5n�|y��W��V]�h�'�<��z>���V-ߺy���x^��{q�;�~�|������3�sp�Z|�l���e��9kf.[U�8e�?3�)��]� �ZtN'� ��A���1�04�065��dW$S��Y��U���l~�&N�tg\O`�o�jA�p����=����u[��+_���_��gv.X�iSՐe�����򲚭�v~?��x��2����j��z� E�r=/ Q�
�ժV����ؤ`Ð6;L�Ұ���h[j���J�l�}�wK^��*�*�8��B��@��d���H�f ��sz��T�5�ıW���Oӱ���x�y���1�@%���Ы
����9�M����\������h�IG8��8�r��£
��;�7�ME��$��m������揥�i�ƍ2ڸ�Y_�Ӵ>���Ȏ�2Q�{�52��K�%޹���j��V7Vwy�c�O�"�>�Vq�`� �GJ�����x�`��j4��hIa��X��0;��2�@���#%Тa�^������@����PNS�p~�,��jئ�ڌ�>���Y?��I� �w��PUTzdGq(W�uHV��!�Wk��F�V��-�A �]�,���[�\�;�����e^���%I�fe+C
����'w���͵�9*_߼��8y��P=�|
�?�:�%��;�r_�M�\$/�9Gn7�5��le�N�2�&� �.��9]�`2�ڣ&z�`+��	��$P$�
;��pI�):*j5-���m���jWG�<ݝ��)�1߅m\������=v<*��� .<r����'?��+ߐo�X�W^��⑤V��;c�̜�]��Bf�A�85��b��
~m��bm�PG��Q���47Q>/&����@���G7���	�G䭀���a�����X�b3���h����Ոj4"��"�
�>�'Fxd��� �=�#s�AL��0�,wھ3pM~�r�a�E�.�����P6J�6y�9���� EoE�R0�*"P���b��p!i�	���(��s0�EE�[��6�|f��̚aӂEc����N҇���e{�e�Ex�Y�Q�����k5v���nU]�M)Jo�q9�.Q��Z��#���ڤ��fFm?��xP^�����p	s���_��g�*Va5[�l�;{��y�w�?��>�+� \ >��V/���N^��`}p�J��b����V���JZ��EZ�mmv7K������}���|��?�{�g ��ݶ��3���ҿ�L&�*�Q��#�RM!�)��̷'�����q���0�C��މg��_��
�+�ŷ��w�v�gvJ���7�u�H	*�Z|�)崜N��Zs5x���Q�j�|=�^rk
�.���TeR�^���<y���TV�,��^9��j($O4���������#@��ΎL�8���d'�u{�6��2���;�T�դ�V���Z�||Ig0�XU*����g2;��;[���행��iB�����pfb+h߽�J��+�����v̞�|�SZ��_�[y� �B�[����`;��]����KM����R�ȁ���x���]��<���V�b��@� ���V�����[���΀�	�� ��i�'�d��M�?�~#�e��E���M�$�]���Τ�I�#�S|�樵0H��*��'�4��#s��~�I�s?`�Y����=�D�Ay#�����H~J�G�W�o`w�PD�*�eEݤh2	��D��7�D1�2UTh-DZ�8�{("$���`堜
�x������uLO�u�ˏ>Kk{fz��g}pZn���i��"�PJGz��tԠ� o�9�CG,�ՇY�ђi)���ܰ�:�Mϛy�6�ڰ{Y�
���	�qGE�җ���O�����K��?���7�k�c$��>�Ï��nx���(w�b�2�U
�JF�����C(��s����E�(oQ066�� �%ЗD�R`\+QأC�����T�+&�](�h�N�%�v[q�q\���Or�A�bBv<�w��O�����.%w����Ez�ܬ�y��̺��������ο�o��/o��/m��'~�kpW�ş�k�t��!FD	�EyI�fD�1�bK+����볓ߟ���n���c����p����Kf�`>�XM �t-Lh��LF���%�W�ޟ����Y[�Xt�C���������}��O,��G�iśO��(��Qk�F��>O�, ٜ͓)VH0 Xx������k�xK��ɸ�Y>�~��W]D�9��{�� I>* 5ǁm	���/�8�^��Tఊ�01��ڝ=ZI�0i���	W�� �����P��y�Z�9�?����n�ߐIz7�J^!K"��Q��>��M���&D���rQ����0��s�q�&"Yz���)Ŧ�3���x6�<Or�Hihx�L�A�\��"]��TDMA}h�b��DX0�;ue��C��`�3f�>n���hZ������ᢷ���,�-��2�d�x<B*5�n�'����/g��D�������c�Y5?=Q�V ��m:�$QL9����'�<����M]bl 8�6����E��8  �O�`�6 � �15Ba͏ G����ܻ�K ���<��%X�n�t'<�Ǐ�����z������tIZ4	��+���|@���N;9!_��e����6����h9w/j�RP�Գ�1*ڢJL�z��4�����Ţ�1F�E]����kiTTL�#7c��sai�A|�t�UR�AHIvV�bF�P|Zw�b�����tS|���9��O����E?��pOI� ��]�}'~����٥��]����vj�k��'f��
���)�s��߄���݋+F�q��j�.�Å���r$u%L<k�t�#;��������ۢr�f�I�4v��Q�,�&�m�"gȉ~��~&U�61��| �����ߍ%"yN8�q��e/>����K6/�K�ɟ�_֥��2�r��`��^o8w�쇟��ƻL-��D�R)N�DA�ڐ�Sn��j�Y˭U�SVAM���˱Z].Sn�堚ܠG\ ��(A����;��0�|Fk;R���ʠiݝX#Z��w/\�9e���}Æǧ�6��?xf�FD�o��h(�r��O�O}@W�x{���� �ଞR�S�E�Q0��[�����*��+�	�aD7c9�-�����@"C���������u��7N��s��J�aa?'4|��#�W.{tٜ�bv����7�'o[�f+��O�|��?�y�T�� �6��0)l� FY����c\�ҘL�ܠɤ������T�4E�k�cߡr#X��o�v��#��+'o�ޞ|�ɫ�OW�|#�?��'91���
�<	N����/��{�9�3�;�ع)���}T�ƜdZ��r�ވ�Haذ<m&s�b�(~;���bд�I'��i�3�⎦�N튯�������Q���U�x]��q�Հ�5r>������KI���j���I��6��s�N�ɐ�H�z�T�}��/-b�4?ZS;a��bN�����-�{@ � 4�2�F}0���\L�y�}?����y��s3��LUܳ�ߦ�+���-̖�F��>=y*��n��R�F������_з_�����s�2L2޵�����j�hmZ�æ���� '�R���P���ID���?vDM���dJ����s򼻫�ˋR���K�lmXŰ��7�-�G�$�V�Ì�<���A-R"UF�Q�0�7+�6�$�c"Ne�/�}y�w<��~Z~���W��q��;u���Y����&Xg�c���	:��b� �!7h4R5Lפ�������a�*2%p��a�;oz��Z�B��z�K�E�W�[� �}xn��FV�E��X�Q3'N��:=s2��4��vwfӻ��������zy��Ç����[���r����唆͈�Z��>��=��=,7���'$&$**�}ܕ�LL��q��zF7�/����c���~5gˎ{������ê.�����d�Z�#eI����=�8�J��Sw���@�h��j�=je9��@�7>m��|�\c��:���p�#�4\M�]�J��
�
�]��c��CY��I{���7�<��S���#_� uҸ���c����{� ���3�](Er�\�R���� `@����@���@�-Q�[؇	%t���5�7��O�1��K�R��vs�7�`)���԰��&
����_z�-�i�hف��}�C�W�]y�c[׮]�c5��o �ڃrr-�!��~����t�<������~������/����ݠ��r���`��K��@�;�Q�R[���s���#�Ab9m�o_;��śy�ѥ�H��7�T�e00�ep�	�)� ���^��^{�iO�2��h�t�kwR�Nk���[@s,����ʙi
��@�������7��֟���-]���p$}��7N��o|d��j�A�¸���og�{~3Ga;�h�t��.~|����d3�7/�N��JF�&�Q�+�ɴ����s��I ����K�x�;��*>�hIa�$����K2G^�ք���)�f6�3�7�A�$�{�N��FG��,�
\b��A�`ND�G-��v��!Ə��|���/}��2/���[�f߸�˃����o��'��o7c���򏫇\8z/z�v΃�F����kF��-�xF{V�wP��O/]`���W�����Yl'oҟ�Q���ͫ��f3:�fp�C�`vbJ�Q�N�ה�5=`�22���t�}=�����W�ȓ{�޵47���\�P9lH�]Vl$;�8�p=m�}�].u��l�þ�;�v�_���كV�0�d����^��Hd��yr��#���$��{�|\�9�ضY�7� ;�8הh�N�&�f��~�{q�#��gb�9��@�֙����,L*��͚MN�,v��NY�X�F��
��B�TtE��(�M��R�F�v�v��hy�G��6X�|p�
g�+qMd��Ş�����!��?�[�#qϛG��%Z�����T�ttb�鍚� �O�?�ٙ���c�L�[8:���� �Zf�XsEZ��	��E�9o�a�p������a��Gw�'�O�r�p2�tV����qy I&� ?��]�{�.�@�P~��Cr[�bИ�Z��lw�jޤ1">�ى�EK�0qp��1������4`�~PZB�a5���)�*;��]����2a�®\J�×�S��׮� H6 ���@�XE�%4Z�r`�sF,2����A�������mX@�4�&o��	5+���<�˰�x��h��f�;�T�8Oi�x`�x+hT��֨�V�P�f�R��&� X}��x����Wk���`�-@����g|vE�_�3�nl�1�v�_�hݮ%X�AAn��Is>���}�f���W��V<]�����F׆��SS� ?��c�1��!��o��Vl���m� O�C�k�	��ߕ����.7�Z���R�o�vǸc`����A���n�L�n+�Zn�w]����a���C�+3{����v[��惂�U�&U���V/}�!`�"yLMp*.���E�6�S��<�B�9e.`a�T��e{~q��D��,�ۜp�w�y�����\��F엍�a_�?lI`��6h�$�����	���l�8)��/ے��-m�XKۈ��	p�:�)Qtă�An���NJFN�sx0F�V�J�3�F�����nP�rLFm;POZgor%��g�����a�8�������̟���>1gen0��1�/��Ë럛�lC��͏����o<d#WI�!?����7��շ>|����E�*���G"�G���k����mq��ڊ:R5�c7вh�F�$��Rv���XXČ�-��#Up+� -yy�\��p
W{�V]mcG��ކ����?������"+�����i����錦�p���0B.���Ҭ�nB~&��6BX�
��H��vK!�b�#cW6��0�]fDbN�|���H�5#�I,��a�a�@XA)o	�-W@l�5ކ����CX�:3��@8�gA�
�Oh���H�o <�D�O���!��e������~����Z�+����b����3���@����_���97�w����_׿�]�.�#��j$+p;��
� ��	����Ǩ9�?��f�r4^Icd�#i�D</��(E�\�6<2��� i��B̩!��.���Q̋�	�;-����+��Z��Q�� )���)h<��f�b�;�Ι��*�2��YyE�ԋ�P�
w���B����J�V^�¯��mo�LF� �bh�o� %�!��yЪ�J��Ő� -��\��Z�B�u�Ҏ
���+/�Z�A�4��E�!=z����X������ 5"E��;R���eȔ�gWN)�>�lz��3+ �M뒚�%�oń��K&��v��4�v#&N�5�x���L�R9e��oIqe�wBY�ܙS&�Vz;L��MK�꽧�l���e3����h���,�;��)�L��>������hBw�=�M�#�����)�h<
ِ�A�x
�{�|Ĭ�7�{A�����nȳ8w;T�A}��n��(��PNCy�
�B��+�K�R#<1�pi
�B���,�@ �.J� 5�r��:��Po%?�=�}ͰA��� �a�~���3!�G������o�;x���乙��Ys}����iٍ57��x��Qx��EW��Ds%����<_~�����q��8��g��gX�,����R��䥷/]�D�K���K�.�qlC}��J��4�b��>��Q�k���;,� <1,ˎr!�^�bl�F�F����<�G�U}��3~�߱<������Uz�4~%7�S~{O��8u����:A��=�I����e��x�?v ��K�˭+�����aBL��c��(��=Zu4t��::B��g>�yZ��RҾOUhm��B�B�h��̃d��r��;H����dǳ�Ծw���zlDi�0�q@l�� �f�&Ɏs�m+�F۔��]v�'u��� �or�d3Xԛ��'6�����Y���=�8gIJ<��=ƍ7��H���]���7<t�l㆔�l���7��u��$/Y�*��nd���Z��{֦�%ek�%h�i�wU>~X����N]M��*\U�����ƕ��)+���d�6��ZX��B������ӛ}�%�\�-�fQ�gŠ^���z{�-��ydP�g�RlZ�]����.�ai�Z�]�)�!���<1@��l�B8�x	��<	�JB�Xc����/��� �[�,y<�y\NWq��)>����P�G����!�k�xpD��scx�p"O�+[�!��\|q�����ɭ�ni<���@���l|1�F6���Nl�s����ؘgJ3��i�W����1f���јbf,3�1^46�L(�a�e����<��kkG�LJ\'6�R����P�H����	�C(olA~-ƫ�KW�B�b��F懊b��C%��X�
��Z��������p$Y���*+!V2J��uRӅY'UTVVDJ��*�f)Ϥ�����-$L�WT"֩2�W A/6)�ƕH�V��)a��+���J�~�#T�ai����0�M3*�������
endstream
endobj
137 0 obj
<</Type /FontDescriptor
/FontName /LiberationMono
/Flags 5
/Ascent 832.51953
/Descent -300.29297
/StemV 53.222656
/CapHeight 658.69141
/ItalicAngle 0
/FontBBox [-481.93359 -300.29297 742.67578 980.95703]
/FontFile2 136 0 R>>
endobj
138 0 obj
<</Type /Font
/FontDescriptor 137 0 R
/BaseFont /LiberationMono
/Subtype /CIDFontType2
/CIDToGIDMap /Identity
/CIDSystemInfo <</Registry (Adobe)
/Ordering (Identity)
/Supplement 0>>
/W [0 320 600.09766]
/DW 0>>
endobj
139 0 obj
<</Filter /FlateDecode
/Length 327>> stream
x�]��n�0��<E�ۡ"I)m%����8��� 41�Q��~��Zi� ����������3��ݨ�Y��`�N;å7��L�j^	�jhm{s�L3���(��?��4��=��x��(~s\o.��h<7Wk` 33�9���L/�}m`1�6�����l���X`YP7j�0�V�k��������+����)�Ν�nF|4�r�*���UD%R�E"��D)Q��Xs�~��uoM��T�c^~B%�TZTD?�E��H�D�XP�N�(nw$�q�N��D!����DJW�Z@-���|��:�炗F���;��
�/���4
endstream
endobj
16 0 obj
<</Type /Font
/Subtype /Type0
/BaseFont /LiberationMono
/Encoding /Identity-H
/DescendantFonts [138 0 R]
/ToUnicode 139 0 R>>
endobj
xref
0 140
0000000000 65535 f 
0000000015 00000 n 
0000220571 00000 n 
0000000154 00000 n 
0000241130 00000 n 
0000262317 00000 n 
0000275279 00000 n 
0000000191 00000 n 
0000220813 00000 n 
0000286733 00000 n 
0000005836 00000 n 
0000011371 00000 n 
0000012363 00000 n 
0000221091 00000 n 
0000017695 00000 n 
0000296216 00000 n 
0000309588 00000 n 
0000017772 00000 n 
0000221371 00000 n 
0000025063 00000 n 
0000221651 00000 n 
0000031111 00000 n 
0000221931 00000 n 
0000038268 00000 n 
0000222201 00000 n 
0000042398 00000 n 
0000222481 00000 n 
0000046195 00000 n 
0000222751 00000 n 
0000050801 00000 n 
0000223009 00000 n 
0000054480 00000 n 
0000223269 00000 n 
0000058689 00000 n 
0000223540 00000 n 
0000063523 00000 n 
0000223809 00000 n 
0000069158 00000 n 
0000224100 00000 n 
0000073924 00000 n 
0000224349 00000 n 
0000076646 00000 n 
0000224640 00000 n 
0000081819 00000 n 
0000224921 00000 n 
0000086488 00000 n 
0000225170 00000 n 
0000090232 00000 n 
0000225451 00000 n 
0000095062 00000 n 
0000225732 00000 n 
0000098976 00000 n 
0000226003 00000 n 
0000102490 00000 n 
0000226252 00000 n 
0000105553 00000 n 
0000226521 00000 n 
0000111366 00000 n 
0000226780 00000 n 
0000115439 00000 n 
0000227039 00000 n 
0000120093 00000 n 
0000227320 00000 n 
0000125368 00000 n 
0000227601 00000 n 
0000130112 00000 n 
0000227872 00000 n 
0000134634 00000 n 
0000228131 00000 n 
0000139609 00000 n 
0000228402 00000 n 
0000143349 00000 n 
0000228661 00000 n 
0000147107 00000 n 
0000228932 00000 n 
0000151316 00000 n 
0000229213 00000 n 
0000157103 00000 n 
0000229484 00000 n 
0000161553 00000 n 
0000229765 00000 n 
0000165969 00000 n 
0000230036 00000 n 
0000170866 00000 n 
0000230317 00000 n 
0000177150 00000 n 
0000230578 00000 n 
0000180816 00000 n 
0000230849 00000 n 
0000186302 00000 n 
0000231108 00000 n 
0000190645 00000 n 
0000231357 00000 n 
0000193642 00000 n 
0000231606 00000 n 
0000196578 00000 n 
0000231855 00000 n 
0000199947 00000 n 
0000232104 00000 n 
0000203235 00000 n 
0000232353 00000 n 
0000206210 00000 n 
0000232604 00000 n 
0000209337 00000 n 
0000232855 00000 n 
0000213061 00000 n 
0000233106 00000 n 
0000216963 00000 n 
0000233357 00000 n 
0000233478 00000 n 
0000233601 00000 n 
0000233724 00000 n 
0000233847 00000 n 
0000233970 00000 n 
0000234097 00000 n 
0000234197 00000 n 
0000234248 00000 n 
0000240172 00000 n 
0000240411 00000 n 
0000240778 00000 n 
0000241267 00000 n 
0000261213 00000 n 
0000261400 00000 n 
0000261947 00000 n 
0000262450 00000 n 
0000274197 00000 n 
0000274389 00000 n 
0000274861 00000 n 
0000275417 00000 n 
0000285764 00000 n 
0000285961 00000 n 
0000286334 00000 n 
0000286873 00000 n 
0000295389 00000 n 
0000295636 00000 n 
0000295868 00000 n 
0000296363 00000 n 
0000308719 00000 n 
0000308961 00000 n 
0000309189 00000 n 
trailer
<</Size 140
/Root 115 0 R
/Info 1 0 R>>
startxref
309730
%%EOF