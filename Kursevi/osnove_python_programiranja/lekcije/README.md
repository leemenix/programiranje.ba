
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

#SluÄajnim odabirom u mreÅ¾u ubacujemo oba broda
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
#Da se brodovi ne bi preklapali, potrebno je da nemaju zajedniÄka polja
#To se obezbeÄ‘uje funkcijom razliciti()
def razliciti(r,c):
    while r == red_1 and c == kol_1:
        r = nasumicni_red(mreza)
        c = nasumicna_kolona(mreza)
        red_2 = r
        kol_2 = c
razliciti(red_2,kol_2)
#Kada izaberete jedno polje, preostala dva mogu biti horizontalno(levo ili desno) ili vertikalno(gore ili dole)
#Zato se definiÅ¡u sledeÄ‡i pravci
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
#NasumiÄno se odredi pravac, i na osnovu njega sledeÄ‡a dva polja
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
#NasumiÄno se odredi pravac, i na osnovu njega sledeÄ‡a dva polja
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



tacan = 0 #U ovoj promenljivoj smeÅ¡ta se ukupan broj pogoÄ‘enih polja oba broda
prvi_brod = 0 #U ovoj promenljivoj smeÅ¡ta se broj pogoÄ‘enih polja prvog broda
drugi_brod = 0 #U ovoj promenljivoj smeÅ¡ta se broj pogoÄ‘enih polja drugog broda
#Na poÄetku nemamo nijedno pogoÄ‘eno polje, pa sve promenljive postavljamo na 0
#U ovoj promenljivoj smeÅ¡ta se ukupan broj pogoÄ‘enih polja oba broda
tacan = 0 
#U ovoj promenljivoj smeÅ¡ta se broj pogoÄ‘enih polja prvog broda
prvi_brod = 0 
#U ovoj promenljivoj smeÅ¡ta se broj pogoÄ‘enih polja drugog broda
drugi_brod = 0 

#Dozvoljeno je 15 pokuÅ¡aja da se potope oba broda
for pokusaj in range(1,16):
    print (str(pokusaj ) + '. pokusaj:')

    nagadjanje_reda  = int(input('Pogodite red:'))
    nagadjanje_kolone  = int(input('Pogodite kolonu:'))
#Ispituje se da li je korisnik pogodio neko polje prvog broda
#Ako jeste, broj pogoÄ‘enih polja se poveÄ‡ava za jedan
    if ((nagadjanje_reda -1  == red_1 ) and (nagadjanje_kolone -1  == kol_1)) or ((nagadjanje_reda -1 == red_1_2 ) and (nagadjanje_kolone -1 == kol_1_2)) or((nagadjanje_reda -1 == red_1_3 ) and (nagadjanje_kolone -1 == kol_1_3)) and mreza[nagadjanje_reda -1 ][nagadjanje_kolone -1] != 'X' :
   

        tacan = tacan+1
        prvi_brod = prvi_brod + 1

        if (tacan != 6) and (prvi_brod != 3) :
            
           
            print ('Bravo, pogodak!')
            mreza[nagadjanje_reda -1 ][nagadjanje_kolone -1] = 'X'
#Ako je pogoÄ‘eno polje treÄ‡e polje prvog broda, korisnik se obaveÅ¡tava da je potopio ceo brod
        elif (tacan != 6) and (prvi_brod == 3):
            
            mreza[nagadjanje_reda -1 ][nagadjanje_kolone -1] = 'X'

            print ('Bravo, potopili ste ceo brod! Ostao vam je jos jedan!')
#Ako je reÄ o Å¡estom pogoÄ‘enom polju, korisnik se obaveÅ¡tava da je potopio oba broda
        if (tacan == 6):
            mreza[nagadjanje_reda -1][nagadjanje_kolone -1] = 'X'
            print ('Svaka cast, potopili ste oba broda!')
           
            break
#Ispituje se da li je korisnik pogodio neko polje drugog broda 
#Ako jeste, broj pogoÄ‘enih polja se poveÄ‡ava za jedan

    elif   ((nagadjanje_reda -1  == red_2 ) and (nagadjanje_kolone -1  == kol_2)) or ((nagadjanje_reda -1  == red_2_2 ) and (nagadjanje_kolone -1  == kol_2_2)) or ((nagadjanje_reda -1  == red_2_3 ) and (nagadjanje_kolone -1  == kol_2_3)) 	 and mreza[nagadjanje_reda -1 ][nagadjanje_kolone -1] != 'Y'  :
        tacan = tacan+1
        drugi_brod = drugi_brod + 1
        if (tacan != 6) and (drugi_brod != 3):
            
            print ('Bravo, pogodak!')
            mreza[nagadjanje_reda -1 ][nagadjanje_kolone -1] = 'Y'
        elif (tacan != 6) and (drugi_brod ==3):
           
            mreza[nagadjanje_reda -1 ][nagadjanje_kolone -1] = 'Y'
#Ako je pogoÄ‘eno polje, treÄ‡e polje prvog broda, korisnik se obaveÅ¡tava da je potopio ceo brod

            print ('Bravo, potopili ste ceo brod! Ostao vam je jos jedan!')
#Ako je reÄ o Å¡estom pogoÄ‘enom polju, korisnik se obaveÅ¡tava da je potopio oba broda

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
%Óëéá
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
xœí]ÛÎä¸q¾Ÿ§èë ‘Å3	²;³¾v0@À‰XvŞHQGJê¯Å¢êWÿ³öÌÛÃn‰d±XõÕÅN›4üyôô÷_»âŸÑª.©”âãO¿~ùÛ—ü½¶±×§ÇßÿûËşËã¯Ôn;åé§a|Ãö_ô zä¿ÿñ‡Çøáïùò»?˜Ç_şox_Hæ¡”ÖùuZúüÓñıô§ï_~÷‹}¤Ç÷?Ó‹†ª‡	]ˆJ»‡6ï¿~ù·¾7î÷ïÿûÅÓ÷ßÿëA:îì¾!ai0ıĞñ;”ÌÒàÆGÒÒ`Ç—~ûş|àN¹N«Š‘«°ïDï:Qû‘±Ÿ½2ûğ4Pí#§1Ú×?N}ñãŞìG·nÒ7ñ^Ñ÷>?ÍOÿ‘şşí‹R¾óù}¨LXíˆA5ÚÓ;V&5]f˜ÜÅøi÷Ø)Ÿjâì˜dTúŞÓ´;Ôø“an4¸½ÆÏL;ÒA…Îô¶+'ºŸÇ/í>ß{e×oFj(Õiç{;Ìhâ¼‘,4ïcïÃJ07ÒŸæëtß{W°¯š¿éi~>–Èw–fdôº'”Ÿ»	‰‰®â‘i_u†:1)?aÆ§R§½íc1ı4†Ö6›®˜ä´%é›Gììyÿ.²éâêÅ[Oõ]ì#Í €1Ó¢­cş÷ù‰ ¼ÌÚµ;îQe;O<ãâAHiÌôL*¾˜ÖRwvÇ2öz™Y3t´,$ÒsÊ¨ò]_‹'lAgVò4ŸÔ:°¯ó2+˜MİãofãÚKåö¾øæòö[Ÿ˜6ß,ıƒ¶ùNR¤YRL‹KjÏªLÚsjì´%ÎR‡‘ÒpŒK.¦ıp"ñiH¡à¹‰µˆå\¢>V:©¯›ºı@}ß‘~ÉÒvï¬Lš0ë¤'K,§’IÎºıÊšÎÑ“^YŞş2}5}¡öì¨¦n„¡‚äİE|—z•¼6G’Ğ‹’?È‡ã,ô/3KñŒÇ4/‡×DuW3m?–°õ¢ÏG5ÉYÚæÑ¥˜*æ11mè¨5…Rš¡áâ/bÄyÚnû˜ØÊt–¾(ôÈ©z“?Àã¸o7=aIï„beÑŠOr—X‡`¯·oZv¦é‰
éâN§ñ%çÔù’7t‚Xı+â*Ä 3´İ¯†u€¶v‹	Ÿ‰/eô,¿f1EP‹èj<Ü–ËòùlxBŒ½,œèj;t*š™»ÈTMnÏ€X®Y×iÀÔ°Øïkp©Ù#’jÚÌ*—Ğ²üsoÎ½íã¼·gºŞàíiLˆœ¾pù‰õö;x¡çQœníØc‡Í½ÌëU7Ó5å…8ØĞO¾8yâauogÂj|÷;ıñé©Ú‹Ì¯Ï%#’Ê˜àPŸ<¸nt{,³Ã²4Mó‹F¥R¨@1%ÁL)—áM<hŠ'[î-´KŠÁÜ™ìRgÒ’¹£üúÅÆañ	nÓ¿ÉFvú‘›Èò’-ÚVÔmÈ‚9·2ŠíãOùá`½öšZ	Á*²¶ó/=mÖmZ{’7Ôf•ÕJmùãøpş–,âÜ˜ŸºŞ†¶ünó°aèÏÅ¡-Âä§Ã02†Ö<^™'ĞOm){m~UÌø¼OC4å—dÉÑøòDc³$™{Æšm±Dc,Çå:
1V9~×¹èBt›‰ÌLÄiª¤ˆ#b2ë”#ÆvZ[µ¥±#ÍĞ‡aËj¸bµ†ÏÃéƒ&åSn˜¤İ¼ß³_¿ÄæI•¶y’:nff‡a|z¡h°ĞÊ/WªÚaz\’™üvî£\%;.W{YÙÜ¼®ıò`Á%cjä±…Ÿ–±|·Œ¹`Ğbv+/t(X~¡W±9VÂ»hYb³-+•¦õûŸÕÑw°ŠÚö[Qş …¤ B7X"†„­E.Ğ\ôü^`Ù%6’¿x´PÆóq Ò<g:Œ„!cŸš˜Ş ıIq¼ñÄ!\G|mˆ‹Q7 iL)¥ùf
Ú4Ë½7‰Àësf£©<ñY^‘”İ ÈšHF“ˆ.„#µe­·ÈÁ¥#r ¶,£c)˜©-ÜAjÍ¹:P[~¹+•µ-Ê|UÔz€¹ş„Aûèİ@‡õËEw­ïX•\ÙÛª×q­jsÿª`Ë™®ªx¥Éª²WÚ­º}¢²Ûb‡q=Ìˆ–õ>OØÁ…#v ¶<KµyÈÓtiœ?‚jËÓÜÀ"j>nÁµÀµÑË}ÚĞÕ?Ô˜ÇëJğ†ÿmÀÃĞ¼®şò`Á'cnÆ±Œ uá<åì
n^èPp½?‚‡’²ÅNZÖ Øp¡@Ã
¾F~v;ñ}š—­f°,Dc=+KŒå•ª×6Ò›úx.¹'ğò„TN­{ä°xÙŠO³[áŸæìÎœ…R2¦ß(%ú÷^)å¦½RÊmG¥DRiØû®PJ¹moÎæ6ú¨âF)åÖ½=›ÛöJ)·ÃØ(¥ÜºWJCÛ¬”ŒÑ¥T|9ËÄâ‹ğÜô¶ˆÙb\‹8.Æ¿îÍL_ĞdQí¥±¡ò¢^ŠõpÅzŸG¥Dô8(¥Ü¶7hs[¦Ş(%²×!›
¥”ÛöJ)·•Rn*”Rn›ÁJWj;(¥Ü¸WJƒù†ÿ•Jil^V}på“²‡•£Ö±¬œ·yåÑrv+7¯tX¹~¥×º?JÊ®;i]ƒuÃ­k•¦|©”Œ™ıw|S¯`¸ Á0‘³,%;8ª×ü[Œœş§ÉLb!–Å_XÁi(T– # ıÏ;ì Õ;˜°$ˆ-©#Æ„d©	¶‹DÁ¨ş˜ò`ú€õ}Lj:â73›ÊéIú ”:ãişğ®WÈª9ÃQ›^ïµI^Ûı[,‹©ıI\Å)âÙœõ·jÊş!AITreeN1ò.¤P†"ÃÜ»Êd*6ëOg&û!×X†"Šj*,~Ur‘İ!½éÉ(´Ÿ˜ÒîÈÎi-ö‰Äs´ îtÇˆğÁ¾a"~Â€>ö	>äİW1\ÂD¯Â	Y0·0/Éy’õû{Ü} ş	Âò¡@"J¤@ÅumÅ"ñ±nEWÈ¨m~İAFcW¥ì‡Y„Ö ‚®BƒØAœĞpÙÑ ¹¼…[ Rlƒ '`. ôzœÎ:Ñ÷‰ŠÃ²Dpg <€Ñ";WêZîŒOO=i¶ïc‘¼®f¦Röø<Q™Ÿ£)ˆŞ>V5“òp¤‰-f"ø*H”³>^"I3ŸaG—8&¸²7ÛÆ9õ8~hè®ÁCÊ•ü`ßù ª%›\Ì
4§ÎõêYÜáÔÔX÷Uy¹“­…PèœFŸâr¡\ ª©JâÕ…©7£™ó%7îì©©Vgu»ÃFñ¿!bµ	ø‰bùZ/u±6;Ñïir¾	_J€:æTğ|šT*¯‹†Ê¶<ÉRò1QJí•úŠ]øEuOmÅÑ«ğ<¾¡Îá¨Ê<®€İQr/îº©ùÂI„èÂœhU3;¹KĞ$ÌÈbGt±Ñˆ ­œÕç·1ƒ^pTƒĞ;¼Br
3ëLïviš?Ïû>;İŠCÍ˜"ğ| òP°}?7ïIU@ª2,¤ fÂmÍ†Ìp¸||¸¡{zeOİ5[‡bÄZ&ï„şÊ`_0•wÁŠ'Æ–É»RU‡Ú4;$à}é©¡p@ZğUì'8ıHce¾»Ê£±Ê¥±ïõ!ìÄÙÎl0Ù°êpê'–ÛKøR«ƒ²rËV¹4ù91bâÀşWn`Ò	é~?ÆÖìŒLÜ9Ûvà/7´ñİ»Ÿ1ú&ÇıØÛVå¬½èê“}RÇ÷w}˜‚»Â4”;|ÀÏV¡|öiÈ_SÓøœòxcÕŸ(5ìá¢ÍyÁ¾'‰  téó™‚®W§Çc‘ŒN…­QãÀî~Ìµ!°ËÔ¼unî'	¯üJÕ'e Ó‡‹À ra{p$Ï·œ$…e¶4³3ùE&ÇÙ0ü`9;ëëÁdIRı`E‚ØG¿$ÏÚqy']—”š³b7d˜4XE gã"³yÄ<¨›rir®´†¶—S„EÆXñƒ™lj«ŞT×`KAû€Š¿˜¬öA	
xÑùlR%Bë^%7†´´Ó`r™HÖ‰ ¡Ã&	?”Æ—¼5¦‘Kògÿ›O:2Î®³İÜ7ê­Y‚gÊú/¶<Öİ—RŞ®b·†ÔÏ;føI•ÔB<ğ«äB_ jÁH;÷v§aÕ
¶¸¯ùé°ü <;…Ò¤ÆÙ’Üî¬sßÅìl)JëÿPñ©ö'Õ:Áâkü9¹Ó.w„¥ùÙ |ßÛp¢åªK>B_U=ÄNâãEb{‹ª'ÄC¹‚Wˆ²ÖU¨¾[2ùŒÉU¥.€Ôtœ’ìô“cçŸ+mã<¾†m'ßâS¸”ÿÁÜµçrøàw1a‚®5ş‘w#-şñŸåï(¾ïç?[S}äöÇ™`x…•½ZN¹¼e^”÷UhR0ZÃO°„!@ny‚ê;ğ	Èn|

½0)›P2 }÷Ù³2ÆxîyPî|GÑ©âÍF·i€X™ÆV`X ªêçGP$ÏIêDvº&Š|òÏú%”s3~†ó/KA_ço¤´ï+üó+'îx·9kùsTz‰çÌù±¨9Ø×Ê¯Då­-Á#ˆ-ß‰]œïáƒª†ò'wÔ9e;Ö~GMn>¼QuêçŞÚi;¡İäaé½ò88tq:Ûâe‚@– ë2Ôë‚ğUUÑ½ª ğ†p«¬ºNnHP’ôRc²/ì£èÅéJïøU§•n>Ğ!|Kæ|q7ñiXÁ+^C?Ÿ²Á®~¤™ëùáá×©£|av¨Wğ¬ÄyDõI!±º¬|üÇÆ`ï»fWê	Ó›²€ğ…^?+‡yb¬m–B°ßßÄ2ÃÈgÕÁ8ş‚·"Ï+H )³¦Œ †¥¢üÔ¹*aoËsyr9Œ”á<@9¢ß¸ú¬&–ˆï¾šX"ÃGxÅ¬*
)f%4Eä™«‚Ô5µüo‚¯1kÖ‡¨¿À‰í¹»ËáøÄíÇ_oÑŒ_íÇ æöS·>cÅš@\ó¥ÕVÉÙ'Eœøñşjüs×Ÿ3û½‰6\õšQuy‡Ü•gRªZÌ¿3Õ'z
 Ú¿÷<-DEˆfò-dAÜwÇÈn¤» ß”Ÿïr)|n+,2~õ5ì¬†æ "ºäYx²àÇRCŒ ïfÁäp~\QnğŸ”¢g9C/A®=PĞã–ãÛ¯X“£bˆØi0ìB’õª*ÊÔ8ÆÙ SrÜƒ~ WĞñÖ»¨?&´ö$ ÀIîcßMw&ÔàWÒ‡Xs§v¥À}ßP	NŞ3ÙåîHŞ…(x© ¨C9T°Ş+¼+BÎ¨á”¸¥|e^Hµ9Ìœm4Ø`ğØ ¿øïy¢_-IêDâ&Íü„wOdâf[7ÎK„ëÍY¥[ÁÜÛßvù<(¶c®,DË÷ár³ëù%mùGÛ¸{ï¸ÿ ¡ Ä]¯g#Ø6Pë]¹õ®¨[îhâ·çW
à¦ao×‰/ˆFU*
ˆô?x[ÜKspo¹²Í©,%Ò9g¶>±	–º#&X‘^È‘übw8Ápæ«á*@XÓŸ*N³ëÊ]¼Şk¸ß¹¡P·DÌ5å§\næQŠÏº¥6š^·Õ·D¢‡ä´ëv8§¶Ü¹¡:.)©Û§d×‘â—'4ÜÙ¯jÈAUˆ¸ì ß-×+Éy£6‚úbH9 øõ!NeñS˜am$ÁËÚùQnvÆ5¿ŞD_ÁY ³“C0ÏPÊTÅF!¿ ;­ÃvVâ§<ËÎwú°§ÁÍ_Ã> î­G­U9>¢jÕq]b_2ó`B$X™ŸÊtÃ…Í÷0ª^7 Ø,ÒÃ/zÍgQ9o›$xà§È¡yT¸¼¢ò.¯ÏYòæîbptxá3zß2‚\Z?|Ï+{É*cbÈvnú}MéACõST«>4,/Õ®††<_˜ ÀŸ9›ì|°	m÷æô—‡D¼ñ{CÑÎ{®|<!Ç$‚(Û|‰E#èš¼rÁy¾{	ND›&B¸‡°OÍñ|p¬æ×¤!¦` LÔãH]ŠÙŒ¾”{O˜J…®´›Ûg@kÆ„0+h?‹33Š,RM/ÕT¥F˜âU¹«ÂªØ°]Kìtv>jŒGò,¿¬ÛUÊÏU©;˜¿Éµ«É}h`7=-Û"pìT!™÷|ÇáL³¼K¥]r%ÛR‡éÿìÍ)è2~zÂZb^d>l<áü¢Ğ©ïáaÇn—2SŠXÔ•¸´áæVäºmôšôÄSS.x‚N-ÀëñEœà9½„4dÊ%„¨_< ´jTY´a•¼‘†’öÌğ
éİç3ğ<8ü¸!>¾ŞâWšAúWĞÃdæŠÔG[¿²¾IÕı_U
XÛ‰ÕtŞ¿TwÈú·¸U„`ßŸ¦ßÇÉàçWfaİâ’³òÑ†S}"™OüAp^g€àº±ÅÄ“RØ~ÍDÁÜŒ[²£ùÎÖ¤¼`P®»`ú`sİ G‘`×ØÆN/¹LİKrä®ÜAl|öîg¨».\¿’´i¾~å·˜İ5‡NU]O]ûrı¹ÑŞ‘ÉÔ[#íìıZÊÚèAñªà˜dJ×Ç_bÆ/‚ıÎ£ï­§Ë/êÄOã{¶Ş™sØP4›]Y²jÿJcÁƒW÷]Ì±ÃH09TĞÍU`cø37!¼Úû%ü´n†Ÿ\pqKşâ7×q/…iN­K2bE:lŠjÏ5ôì¤áÖ{õ¼¢Á½ËJL|kFîü÷-%ÏØ‹ÊÆÜ· e´íÙaù:İú1åĞ1¥ ®º÷ŸRğúÁpöö«Ûú¥qR·õy…T{›’Ü
—K™ì>¨Tß™es2_f|ĞİwŸ#ÿøÈŞr4‡_‘	%KÀq¯ñ¨®¶¾‚Šrû%ó³¸—mT4¸ÿùf!?T«JÖ¥îC=xÑA´Züæb^p¾áÂÎJ<~Ë>ov­¸Ä¥Ù±A#ÿpqs¥2F†0?İaäAÕw1ä¼×sm0şëìÊ‚oµ¨d-ÚIF=-nöGúûÿ>­.u
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
xœíXTWÿ}Ë–Ù™YìÄc>Ô¨éÅ{‰½bA±Å€D¢±ÄcFåSì5öŠ¨ôŞAQPD@P¢¨ R—÷¿³Š
~Æ´sş'¿sgæ½û»÷ÎÌ{³£„ü[ÿÖ?\KqkC‚:’t;rËÜK2íÉ{òÛx€œbS €ò’:³©¾kC\;‘˜^R4„Cn%·Ç‘Ìqä·	2S~àƒ˜4Ñ‚F´ÿ#u±?¹6œè*gŒ%éãÈ	$kŠì“<g†òáªGó˜GÕÏ0Á ¦@ d´ HAğï©àÎ$~ I*9"Àíñ$ÛÁ,g†âá&w)ûxµ:êÉ:e‹ªà¿Ì3¸Hƒ˜4Ñ‚F´CR„,ÄÿÒº1Z2‚LïL”İw’?œËä.có×ª‘°p«¦x_CÛ§:ß~eá“õç§±s àƒ˜4Ñ‚F´CR„,ÄañÕw­É‘’şm{ÓGó™üÕÜ“LáV¾ôˆMYğ(!éC¦»˜&æ^óâÅÇÀ%#â¥Sæ„ ÈhA#Ú!)Bâ°€ÑŸ[SZ§÷¤ƒô1äî×²‡sTy+ù¶h‡¹îL;áò1ËKÌÅˆ#Ä‡aâƒP	C_:“ œå…F´CR„,Äa‚Lÿ”ê^_ú{q¸ôÁ]Êı‘}²^S´•Õj+\Y*fû‰ÂÄœ ñ¾/ÍñM€,µ 1Û"‚ d!.=ˆq’İSë?şÒ rk<ÉùN‘·’+ØÄ—ì­¡iÈ<!Ş÷³ÏQàÇ3Ü%*3³Ï¡"‚ d!Á¦ğ:Ö+Ÿ‰ğ3•ù«5…›5¥‡	ñsÄ»çÄ,7šu’Ş=%!û`êÍ:	)Bâ°€ì2+.ÁãÍÊ§WEøµšÂmæºcMW—‰ˆ}ç ½sˆşV¬7ÂÓvHİ9YˆÃF°3]ü‘ºeOğ¢ÎÿYS¸]«;ş¶!qÍ<@oí¤·wÓÌJ¸óF¨¬ AÈf€Œ`SX#ÀWŠ¹?M·Š+Ún¡;\ÇpÑQÌØAÓ7ÑŒÍnUBöNú`ÍÜúÜ`u d´T4i¦o‚Œ`SX# b¼AE'w§Èrb·X–´Bû‰i.bÚ/âÍuH¯„¬	çœO¬V’´šfº<7õ22]@-h|nêæ:ˆKi.°ƒ)¬ 1¢†ÿ¾ğcë‘ÛÉ£yª‚ÚÒı5õ-Åk‹Ä”bÊrš
¬ i¸³æê9‡m™ÉŠ¯Û
é«hz¥Ù¾Ğ@FÑşl²©Ëa!][SX# b ÌØß³‹“Çgyş¾xO­²u1#ÄäÅëhòzcá3¤,4¤-^4ÊzìGdÚ—ÊámHô‘4sésœÊÈ\
h £h‡Èsœä0‚!ÆÖ€“<æuÃÏûTú¶ÉıQ]¸ÕRw¸¶àİBLp¯Í¤IßÓ¤™ôz%¤Í¹é=ar{faoå²şÌÔvdƒc+zs.M~foÎ4Ñ‚F´Cä9Z’d;˜Âa	Á^§F“œéŠ'ëğ1V[ª®!¼»˜8&:Ò«S_Dútß=¾ k1†©öRÌîW«8Î‘^wª‚|İ	S €2ZĞˆvˆTANt„)¬ 1‘^ãÓî³š$71S¸ÍRw´®àÑHŒJ¯L¦W&Ò„—pÃaïÜ÷gt’mªv¡^Ñ_åÜ•Íğ¶¥×'WA¾>S €2ZĞˆvˆTA†İ•É°F Ä@DB0Ä{u"÷¾5“Vş¾Zz7+ƒß»4Î–^CãGW«ã]¾i6·›ÙÆáê-¶Ò-ÅÂ¾|¤M[9i,¦@ d´ í©Z¦q¶€ƒH†x¯®$;³Gs•®ZİáºÂÙú† Ö4n(R5F®¶o°°§|ÓõÖ‘ê_†0Ó:˜ÅìéD“l« 'Ùb
Ğ@FÑ‘jõã†" b "!â½"¼u’1Y–»T]´³FÙ	+ƒWúíGc¿ª—®²«·¸—ÂÕ˜ıPÆ¹ƒYô®/èÕ4¶ï‹¸:S €2ZĞˆvˆT«ëĞa	Á!««_»“»X<kùâ_kîõEß·ihz¾éö"Îßgı¤‹zVäÂLï¬¸¸ïcß…Fu¤QíiT;#ÚK§ñ]0Âú!åùÑˆvˆ”«UáÒa	Á!«« ÁøTSl4/=TG8×@ôkLCşC£ÛÓèÆ¿í+@°KvÌh° »¢|ıffõ`’ZÓˆwh°5nZ	Ò ¦@ Í´~ĞˆvˆHROeŸ3j ˆ0ˆ„`ˆ‡ÕÕ¥Ñfæ+·juGë<Ò€&’oxùi>¡Ò°Ö4Ô††4§ç›»¯|kN…iÿ®ÀÌëÇ>ğ}‡†Zó?PkL šiÿ¢í‘¤ YˆÃâ©]x[©1 	Â ‚!BV—ÿÚ8éÍY´ÃRZüŞoÓ@ã}nFClhhKÚ‚†¼+>İ<n“™]•†2®¶êŸz+×Œ·¢mŒœ*€)@-hD;D*]f3ÉF°±)÷
lŠ0ÒØ!½E²ºü)öÆÍ»»†şd}ƒOcØŒ™`]"…6Ëk±x¿²ŸÊe˜zNg…ûš†ô¢Ôòr~^´4Ñ‚F´Cäá;Ói`3„A$C<„¬.ÿÍI²¼lÑšúÓõEŸÆb`31Ğº’f³ÙK-Ü×7šŞŞlQwÅüÜığ–4¼ê›/!¼ Œ4¢¾¤lò•şJ¢)ÿéú†xY]~¼¯b‹÷Ô,s«oğn,XÛMhj5!¨!MK[ïZ\Ş0MÜ9›ßäù[	˜Š·d´ íÏ¤ŒÊ’K€	ÖO0ˆ„`ˆ‡Õå¿õµ,o•ºxwÍ²So¼Ş6ø7Ä #üq9(Ø˜U ÇMiFÛ’ÛÒ«-hĞÛ4¸q1 \m!‘3ÚJÏtÄÀrƒ¿	MÊá×a	ù!_µ~–«‹vY–¬+xÖ7ø5’àßHô—Dÿ†b€Å #‚jHCÒğFbHC1T­¦YÑHFK¹BP%qƒ¿Áh¿‚o#ƒo#„Ñ¬‹`ˆ÷Šõscö¯ªp»Fw¬†àQWğµü¬ÿ·~V4 ·¢¡õhp]1¨®RW­øZG«#†×#Œ¯C_F„ñ)À5¡B'D’…8«GÃ¬şõ`­÷{Kïc% çê"‚åş¤BÈêò'Œ•=Z¢(ÜÊ–ÕêÏÖ|kKğ«m¨õØ½†ÿ2ók;´¥~–4Æ’^0ş´¤á"a!FZˆQå Õ@š¬€±í’ÈyKkI£,ŸxXw1X«-ó©iğ¯¥÷­­÷Á?@jëÏÔ*=¢E0ÄCÈêò‡Ûš=\ /pU—ÖèÏXŞ–z_KÁ¯°Ü3Uı‘šô­oæø©bı•ÏRõıl/G#9ÇÓËœ„+7"Îˆ‹Ï#—Œ0qÀ¿ÈÂ¸\OîÊÖm®zÅ å„6òµeí,e±y*¹ë},õ^–zw‹ÒCš‚MjÄCÈêòìCrfËóÿËäÊÜµ‚·Vï§üµ4Z»sªz`]³‰MeÃ­HKÒİ’ôo@Æ¶"³»Ë×Û)ÏV®U^Ş£¼yR•å©zè¯z¤*ŠP•F«J£Taª¼ Õ_Õ3ª”#ªØíJŸÊ}ÎŠÕ¶
çNf¶ï’¯¬HwÒ¿&SŸL²–´2‹ÚÄÑpsX¾ZÁK[vZ[|€Ëwa!«+Ç÷I¶³,ÿeÑ¯¬ÎM#x›æB O£y¿µêÑdÎŸÔXî0dıWßtk>ªm­AÖòuÈ—¤³%éRƒt«Ez¿E[Ûdô{ÄşC2é2ñ2ö}2ªaC4&=ë‘®5I×¤³ébIz[‘Áï2vÕuêÛúÇÉƒÛcjKåøwe'YÆ	Áß\ğ2×Òícñ²ºâ•$¯ĞŠÂİjİINï­‚!˜§‘ìêQÖÄ©w+wO/ß OO3înGömŞ¹~éÆ¥ß/s8wTçéƒ?wìÓjb‡c>¶ıÖ¶µf¨;Ô†ÙÖ|ô‡Z»OjLêÜØ©oÛï‡¶›o×eÕ[×sw»,?~p×÷Ó^^~Aû÷î¶kÅMï(+ai0+ñ‚ŸFï¥Ñà
wªñòak–»X^°M­;Îé=ùCxÆE²N_šõiÁøuWPphHHhTTtÜ¥Ë	W“’’Sn¤¦¥¤¥§eÜJMMINº|-áBRÂ…ë	±I—ÀAÂ&_OLMKK½™q#õæõ”Ô«IÉè¿¾vé]ê“õ“•45±B0/økôç4º#\ÁVuîByDõ‹ßTKÚ‘œYfO\¤- ?+µ‹a¼ÆÒvû,U{+2eLO///˜^Š¿ŒJLLLNNNOOÏÌÌÌÎÎ~øğÑ“'EÅ¥º2½ RSéÎ‹Š?ÎÏyğ ++ëöíÛ©©iIIIW®\¹t)şbÜ¥¨˜GÔ©Y·F$lCcYC‹G¯Çıwç±øŸl`ñ^]Z%IÆZ©,Ú£Öâ_Î‹xW°7Î±Ã[Ë»4'_}Ñh†ãè}»·EFF¦¤¦eŞÉÊ¾—sï>¢=ÌË{üäÉ“¢¢"Ng0Êóëõ%%%ùùOrsssrr²ïİ¿›}ïÖíÌkIÉş~®.?=¦o×÷-»5#N=XÁŠa=Ö0VrÑ.5"!˜ö•‹ÇTGû’ÜùòÂ-Œî('xk¡¼ÉÓ(–^çÖ;¨Æµ–ÿ|Ùœ|şéõyÃI#{¬]şÃÑ»c¢#ğrràVÓj
àîİ»)))Á>ûvm^2wêè_ty¿æçÍH÷ÿ1ã…&?»AM¯"<À‚x½‡¦ô(W¸™É'G°×©f$ÃA–ÿ³²x¯Z†3jÄäÇ›MæfvR,îª\ØSéÜEn÷éÛštjNÚ7'Ûp}Û7ÓÿÃi“ú-=iù¢iëVüàºvÑ¦5‹Ö,›µlÓüãÇöÑû½^ŸYuj¥l÷éò.Ø–ŒoO¾ï¦XÜS9¯½bé0eÑUgÅHÎ&­Ş271òW+	Á^³ãÌ•ºJÀàƒ- Á+”Æp4ƒ÷ØÈ.î¨Ø6Dµc¸Êu¨rí å’~ŠÙ½äN]e:‘Ÿ’ï“>ï‘-I÷¤»ñoKÒ«%ùª5üı™Ô‘Lë&›Û[¾¬¿rİ`å–aÊ \ĞE‘èÅÑœdÉ‹!ÁKSz˜+ØÄ Ìá×»ù¦²P“ëø–^¡À.(‘zAúÕßÖìšÉ¬í¥8l§:9^ub‚ê¨½êÀ8å^;åöÑÊÍ#•.¶ÊuÃ•?S®ª\iÄj\æ0iğ¿¶Ê-#•;GKäCã”Çì%…ãöªı£TËº*¼·°ô/ıLŸçÅp!@£?ÍíVç-W "ı®šş1Éş^–¿^U|ˆÕ{b+iÄó<½ÄÓ.?]ãêÈ¸PŸÄœq`<Ï©ŒÇTæœ#sÖ‘qwPvP¹}£:5¥ßH§?ã :ë Ñ@–Z@Â²W­î­<¾JmÈÖĞDb;½W|E Ä@˜7(÷Áf¹äØ;ºã¬àË"xŸ:øÈ¹Å=J7ß>C½aêè×Ì'ÆÓ™ñÎø¼U%T~ÇxÎŒÇ4æôTæÀxÕÏı•'aõ9æ4[ŒñQÎ>œî+mÛrÄx“ôÆŠ'Ë["/ÜÁèN°zŞÃ‹x‰ÍäïjÿÌ®¢Ü?Auzã9ƒñ™ÉøÎ*‡ßK0ƒãı=ã19åÄì£Z;Btˆ™KËşŠtQxçó°+ÜÎä.‘ÇVÿ¯õ×)›šÆŸƒeŠÂŒî”ôƒ.ÆhÄx\OÓy1O{ÁSãú³i¤ê0VÈtÆsã=‡ñ~`ü*§ôÍxÌdÜœ™ı“T.#”»ç¨ScÍ)Â_ç¥ğy1
¿ø¼î$‹;SXÛü¯ÿ°ıŸÕ¡¹á`¼„]ŒÎÕp†HxQ#^æiO˜çİÑä·:1›ìT{&1Ç¾eNÏ`ÎÍb<g«=ç”ãì,Æm:sd*³Ó^µÑN…äç=5ºô7MàpCÄC¸FïÇá.á^Á¦°şS
:×&Ëò–J©ä«÷â„PBÚ<Mãi®¶ Ë">ÀüÔ:n×tõ–IÌ{fûfÇDfÇfÛxf³=³u
³gë¹¿­•’ß7—.?Ş¸àc4B°o‰’£Ò²ÉûI»ÿœğ¦jnA.ÚËrÉ6ªŠ¨ËÜ±8l4ÃãUàY¤ğô9Í³(Ê¶ø-I›©õ4:­â|ÍS.hïİ°bçi¥{~Mz•™’ãw
·½Ì-Ş¯†8,.ØËŞùÃË¦Ê:5Ä,{¶ìñji;”S—yrú@NˆÀU÷5öEOohh¦†f›ÓZúÈˆ-½kNoiLë¼<ùy^ç±ËÎá¶«ñd!qXü%Ñ+Êù#rmŠßØù.Ê¢}LÉ	µÎÃxøÜŠ6]ˆ´5DìÇÄJÀéei
¼a„PO‡äÇÕE{HA²ÿŠ•“=}Iú·2¼ßò7(±¯‹«KN³el™?§áôáœÉ	Ñ¼c"¥ALPæÁ–`µRã!¢"‚ dÿÎj !{û‘dGÙƒùfy+¸‡XE¿ª‹¨KN²¸œ’³¬ÎC¤Sd>¢4Ñ‚ÆdD õ~ÜıG™¥M•İûAz"W)ÿ¢DÂWUÁf#\U8Å ¦@ d´¼ÙWÁ_Txøƒš“õİˆç³óãe‰_ËReßJÀN1ˆ)@û{WÊ¿õoı¿­ÿùÖk
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
xœí×ËK*QpÏŒ:ÎLj––&™cA*±©®^HíeAĞ]„´hÑ®‹ "¢E´Šj×¢­]‚°6eTX¶¨ş‰Ê6uî8öĞ|Íœõıî?¿9çÌyÊdÿ“+˜ß
Ÿ\]„·æ,&	ƒ…³g˜–ç³… VSÁ£7˜•·£ %FËƒ×Ù8•ë ¼(çòéd¸ÂÌ>â>Í İ.¬“ÙÖæ« ª‹s«r UQ1ÂhÎ ,"C)Ë. ğ±Âüg€Ï‰çÎı( p®ÈËÌ—Q à´èÎ§¡Ó`ŠIiÂIÅ÷’òò¸T/—5 '¦¤r§üëóšSéşTóÙ ŒèÎ±Ş‹å­›ø9µ"C¸B¥v Ô^¢øK­Rè ¦j{Añ/m*¡8=Â!œ …? W/¢ùEµ0 Jí.šßÕ*“ÃGˆ_ø™‰”ü UeÍÇ*UIOšîĞü‰ä=FšQ½™Â’ß¯Fm5)´Ÿ9FóÇ)¯böĞü“?Á¬¢ùU†æOÕ4šŸ6+…ù[áO ğ„¿B˜¿˜®åÅß´è„õ¨†¿Ñ@¥60…%ˆ²-Ší·²aÅ:+?6` i	I÷¡Íç °ô<Jå=ŸÍç o—Ü€P»şû TÙzÎ¥ñó›*íü58&%Í¡Ä¤Ã~€Ïš¿æ±÷m£w_<ß÷6ş¸Åá&Ç¨èSèrÔaÂe™!çø­8~;îdHÙÏ¨YÏø…~ñÇÍª³¸L¦«÷ŒŠƒ¿cî:]Î_ ëİıëE~cb}àw.÷ÓÙ~õOœHçÓş.V—ï14‡wdù!Ÿ~Xñ:,š7øs“Ë7¶{ÏÆï±¥1Ÿ«É\’_ó!ôµvhf'şš_ã;3C~½VOäü ĞF›İÕ78<ÚGoïïo£áÍĞÔğ`ŸËn3Ò"ŞqrµÑÚÌ¹{}Ãƒ¡¡Ààğ€¯×Í5[êâÏ§TºÜÌ6´r]N7g×ÚÀšËi‘: ¤K&¦ÆÊ²ÖÆd(¥•¢ŸŸÁIñ!	E^ÿ½­Ğ
endstream
endobj
12 0 obj
<</Filter /FlateDecode
/Length 5260>> stream
xœí]Ùì¶}Ÿ¯èç –Eq	îf?;¸@òÇ8ÿRš–º©å´êPœÉµ_ìÖHÜŠU§ö¦³éùŸS+ÿ~×dÿi’I)şñÛÓïOÃóÎÅöd}›Nüóéo:ı[~w	ò§ıùóÿ“Íiø÷¯?ÎÿñÇ¯OßÿhO¿ş÷ù{}²'cºnøÜ/Ï¿´ÃŸÿCşôã×§ïp§túú‹|èy†ædû¦¦ó§Î¾şöôç¶µş/§¯ÿz
òüëÏ'ù¡‹ËÜò‡şù‡şòƒmŸˆøÆ<ÿ`/?øó+éòƒ;ôË×í‰{ã›ÎÄ>›¹é—ƒt‹AÌræë¿X®ŞØåà/ĞD»èNQ6xœ£¿ıÇ©Íş¸µËÙ-§ÛîŒ-´—½ÚŸÓÛ?É¿¿?š0üãN¦÷M;õ©ë¼i'ÛäKWRµÍ@6Ã@çÿÊ^şÎ¶®•?wqŸh;!ó˜Ìmª•¯»ùÂÚ“iİ´0Îô×8×§Ğû+Q¥ñh
É]‰Ël+¢Yn¨•»+—×fŸ:?ˆMç|êÍ•Öİ§ñïä~Ëõ»¼qŞîaßúÔ{¿?¸7ãr	SÈ^ø†(XÆyGB­Iùœâø%!—Ôç/|_ğÉ¦>¦«à'K?å¾ ÙÆíÙz?keìp%ÆIuNtQ±Œ3k3]#T$›Ş³J}Jë¶åtNqJ­¹(Ëkãş<¡“•>%Í†ì_€VÖŒ[Rçù¾FwåTºK–ZÅµÌîÚ6FÅÂsRHùÕÏ77fŸ©-4©5©ÏR¾‡rVû³‚c˜3U	Fˆ2]gä6»6ÑºıÍr?Œb'À=ë£UÑWÛİÁù~ÅÄ&i˜6¥†Üı³ÔÏ»o‚|&„Òq²³)»~b³½¬!„õªƒ&²©šñAodŸ²İø†€_º·TLı’lûÆİ\™¤ÿ4nSàÙ·÷ÒÉQD›±ÕÓlqì’låAHÂEö××'e¬°U9£vuËÖ»~¡cû´â:ë¡İ‡éC‚°CÎ.jåvƒüW§4Ş#‚Æ$—qbL
ü 4)LôßÉ©Š°ÂÎr~6Ål²m•›İ‹M4eäæïÍ4¬v!cªAûiÚnÙ=ŸA(­€¼·ı„!e„°ûçã^oÀAZàBhRa¡“óQA~Ò¯.ì!%¥ Ç ¬E`Â|Ş&úQ%ZódøÀ˜n»¬M8¦'´Ê…+¡Ëxá¾"¡¬x©š0ñV#MÈP¦ÃXâP¸=ài\Æğ#M·AÔF_x]Ğ~ ëaÏ_JMdpföãÈQ¾2z‚ë…ŸE#_j50)g9â²Ó~BiÎ¶<‚ûƒls™mv6,Ç^/c´­vÊ~œvjÀ&±’22©!ƒÙlsx£“m¹D…7ía÷aü”“>›Õ$-Ò@µÖìA«uk‰>B¿©PÎu‚öãˆ½tlÁÑ ~ bĞù:f:?§­â9³˜ñB—4DoèØçL3`å3şé '¹x”æßR¼a„–RÜ&Ÿ™b…´ºkí;z€uæ+ÓíÚ.ã•®§c?ÌK1œ.V5H¨Ÿ<dƒêo)²àØ¼qÚzTÆ“Ü†mY:û…Fòãu@Ó¼ıhxj?-(ª3+Šê.J×(0eÑ6Ääº•EEäƒ ‘Aq¹µQtP™R·ò
¸&
Oˆİê0ÖoŒ*œğ
Ó¥|¿Ç	)‹™|·b.I”PQ¤íÊ„·úlwÙ’˜fŸ‚¯\wQÄ†œw¶WŸ. Ş†9°šÖ¹¹™dä†²Fsm Îl$ÄÚÅË„'O?E´d°8ÍÑcú/¢\«Ø&›?±sÇÈå[Öw[¤­-C£À›¥ïW¶Òª-êI0V›ÂÚL¼ñ­/ù¶ôSš;ïæûŒÂC~ˆä@Şõo¤±l;š*º c¬b¤iYÅ€×$½!Z œÀ$Ø°¨§­^üîb´Ñ¡éâƒBÄC›hj:¡X×ĞÀïz>øL½‚G>a×¥€İ:“AOWM´ÉZcrºŞN]ƒ…Ÿªd#Bß{~„>wC¡íÅB¯ƒ?©ÙéÃJûØpu!«OEg%ïBÅcĞz"s îŒ¡»Šløo7Öi9íñÅÆ¸íô÷ITOĞËC=×<¦’M(.ZwÅ;‚ÈÊ-uÅ-HÙ‡Éúğ8GØĞ ãÑ!>Ú2 Œ(5İw@!Ô÷Ò œ®™”ˆ¥ÉŞXô 4‰	0Ã™¢Rq¾P+PHx­í
zØª‘€‘çaFŸ*pŠ#oxÑ”Çgyhı¯·“2\ÈmüP."~‹@w¶¿›}mM7²è1":5):«yó±P°<Ï|ø4ÎV–9‹4q{q‹FÀœÛ5PÜ¸^Äë#` K-ˆ‘…†‹ŠÆ}4Lóæ×ŒâQfœ4ØÇœâmUŒlÎƒñ¬·Ãª-4¨âpC.–PĞ<8DN…¶Î®÷‹š†	µ ´UÈÊå4}âûVH›¹ÌqhĞŸrZp¯ò]ÏíT5oo!1à•çx i –â6/ııŠHÏ…/İZ¼İ;è„~œWØ?ğsb-§ª;¸[¾6¥TÜö}a †×¼IhÜo#_ëæQõŒa"˜zyR¥A¹ç°ö½˜­@$;úPÏ‘b¾ÛÏêB“½š¼CÑ®2¥N ªGØh@_ Ş¡Vïf(M5yîÏ5H:öâ÷9¡ÚS‚Ó¡  ‚œ
J‹y„VQú©Â»@¨.‘ƒ÷ˆb‰EŸì¾€½>;'z«ğàĞÛtÛf²1)Úç
IšWúÍUyy‰}&éúV1+ÃøÅ»yÿT†–ãLnŸG*DA(}‚ÀÏveúÉ“eÊs‘µ9SãIÂ>:ƒOõ¬dz†¸w¨x.ŠÛFt 2~è<4´†6ğŠUFü©ÒÎ÷Ì(0‰\ş¾1½Ö•ó£/Ó>F™˜¿nWho³5kzYÌPY%û¾:¼ıœç{*8¢rtW$‰‚4‚Òâ!ğä]y¡Ÿ•ùrû€@«Õ/œ‰aSØ¥é¯»óI„¯ˆk»Qv B×óDşé¨B;„toøPEê|Z…ÔÛF†HÑo„:/ÌÉnàÙå§ÆÁ7ÂÖ§3ìÃàÒË3”7zùÙm˜·`ªËêA?q:3¾Štq€µ”ö×=ºSÓÉT}îä¼dœnC·ÒY7†şˆ&‹¶Ğ+œÍÎN¹#(T€—iğ:jA$*°T©gy1¨}Vë’(4á:¾ƒÅò!­ƒ5ÃËTfœ;XƒÑ ï}­ZM\Ï[PàË{wñÒÇgA(L)ÆaScæYÛ˜Á9à7PÂ
Ã "Õåœ¹vá0ÍšvàÂ£…Tu:ö bÚ@Ax÷¶)¥b¦ô÷ò{ûíúëg…÷j‡ß†G`8•¼-Òéú™GŒ‰›…ŞhÜ¡JdnÅØæ¡ÏzCÔtfó+|àMA:?m0åÁ˜0 o¥,Ç ‘‰œşBTÅ,A™<”…‘Vªä˜Ù¦ ´S€ç¦
CC(PPUØ¤·Gùè!>™õü‹¯‹ éÀƒA—[ÅH„Ÿ°ŠĞ7hXA3,ˆPVTÿt×ª¸˜¯×rcx1ê™°hw^EGtÎá7@w<%§Bö˜
&u6dë`
G½tÎW€güÒuû¹9ª >]“â¢),?ƒkŠ˜¦Q
Ótˆ1:	ŸÇDŠCSŸ—	çğY/S–;àÅšé¥à—•Ùj0î¥D©Y”AŸ‘º#XP®r
÷‘iå!“×ØÛ ·n¥ĞİU¾›@•Ò8¯Êîå½WØm÷(°G	ê* \{ÈF?'XM¥ èbbêÍŠ7o½£ó1:Ÿixåßã½n0‡Ü-¤¬–ÈÙ¸¼RiIfO€ƒ&ØBsà`N|ºod³‘(„6kÁÊç3Ñ:oÃÕhĞÊlYE†‘6Ysš®J•PËıC×ø3 zş¯®5ÏK'ÓË4¼È†¡àØıïû¿›öôù?Ï/ª{	ïnc®ĞÉ[ş9Ôò
½J9<SÛ›•	|ioMv„wS£h.£;ƒ`{ÄÎL™ ºş´—„„ ´À*V­AäÎº!ÙÈ½l»¿fÄSP×,ğFyŸ—¯™Æ“J)âá7úò¹F5+;Pú^Ì
ê!f£›UDÿöx¸½Q˜k{ªîC¸„²ó``IW«X/ë*t=]Îë5Õå•HÖ½J²J—ê^Å ‚”hˆ¨éê‡¼À‡hkÚø0u®©W ²bÕLè¸xHËPµÌ¼³tÀ#_Ï½bEÙ;lŸwRl–Õ§CÂ¼>†VEUö"è?V9K+Ör/•´ÈØÓh¬•%öÑØÓÓ¦ÑQVÅ&t3­‚¤İzÄÈë…¼şşòEpKë{yu,€ß±zw]è¯›±Õ‚âKT³{,:`^³ÈiAN½Há½ˆç›)î¡8´=/û`à×–ÉÔp?®Aæ&W`Õêk#Hc;|<£ÕÏhà‡Î_¿q	JCSøuMÉ›zCpaÙÆÌ›‚„c†ššÀ° m0¤¥4ïL¯ÚÖŠ¬<‡„Á;¸‹/_/”>òn² Øe¡Y¸…ÂÓÕ?Ÿ†P7î ßÈÂæ§”¡E%íæ+#*š®x'TÅdz<+h®„ğoPU-æ¯ ÷¢¼–½ºâ¹J[•O mŒ|€È3i+×°ê"Ó÷…®£]RÀAÍÒ±5˜·jÓV»ğÉs8z… zH~¬1Ê³Öî„‹™9 {Ğ‡t÷j¦Œ;*4ò£š…õ*NòvÚ¤ÅchÁ¿‹¨×âZz–mùû7éÅ’|”	—ª6CwHÕ}KyÅÿ'mC«œëk–M¨™µvŞ<ø@œ|Ì¦Ó;Á}Úms¼Ã?Ù™=HY¯cÆ£|¯‚ú;›u¦¶„œíLÒ—‡æã‚_>| tÇ)HÅâû(¿fK¢;ÚyDÁ¥j¬ôBUÚÌÿÃ­ú2¾° 3hƒù9Ì£k¸JÁè»•¿ì‘Ô¾wÎ ±¿øZÌö… ^à5j¾j1[§…Ï¥àg½Z)î-‡ OİÁ@tĞ„’WáÛóáÆ{¢Ï2¼¢Xq¼,o¼b)ãjm–Ó‡UPÏ-_~è­‡u
\&óNx¬Mğzş>ÈŞ
rfQCÄqùî9â¡ÚÒ½‹;ØÊ›V©³%Ùp‚hÒ—Wk±gM%òe³ÛQ¯Øë&J¾)«Uµ®pô0aošV`“àù,Ÿ~W±>áKTƒ]EÑÀ©@¨¹'oKòx4ÕÜúèvúmñL:m¯¢MªÕğÁGğ ^‰•«Hµ^ãØ®	ƒ~9vy>d‚´¯ŠòRÅ‘ÃÊÕú ØI†F-lõTãÖÙPğøáHâç“šõF?–£œ¿qõ±¸S*s,§L%\ß{X/_Dî"t1)æë }O0ãr²vÀÜ¢(0¦7Ş5SÏ*1Ë€ĞGy°6 w/´øÚ¸8=¸Gt2ŸSğÀ¡k7ñel/Í¤i½@¼Ói{õl%oÊ7ª³'?Lœ6£ÔçgEW!©n¿¯Æu*ª¦dŠ¦Zƒ2ÿrTüßE‰¬˜{ëºòî‘Š5SèÜÆ7†Jad„Æ´]÷Ãfp4È=â	T†J]Bş´S}<šåZÀŠj%MñÒL•G4t<íÕ(ğ 1xB «ÇTK ¯Ø,/\m*S¬˜sË/\Uj³dûJ»¢«£×çıy×oàSN³£bB3v¨ s%4|ÖswiêT±çûz)õn+hpÈ»½°ÑEÂ¿ùŒ{x	v<Ü·Qip{™)^QZWC¾t^DÍH›GŒ=¯¸¾·¥ÑÔ‹œæA7cN»xqhÅ(L>àøm­+öl¬•"]µqïFƒVZºÃèå‚L­zõPJêBò@¾AWvB¸”_yAy=å`=;]KıòµhLuÈ”Û6Û®:W`Êô
lCi~vM &V±áç=ªüWH®	á÷@ñàÖw)«Í
 î7ıöPtóR3kéˆûdØóÑ}2K„ñ&B@%2ò}Â˜_A¦1şó—òaä…G»ıfÜU6ÙÑÆ<«†/W±!sAÁ÷ŠrÅ•²\µ´"YaëÈ\…-p¨Ü~ª¦õ|”VA±_>·’6Ìâå33TµI_(^¸¢Û£fÊÏ;Iº©Ù£á1“nJVÈ;_ÕDÇƒU DQ+ÊÕ$7y8*fšğ-|`3X¶«
L°œ•îC[üŞÙ¼wX¬qrç¶	˜œN7¤cZyW	ß|›î¦«»ÆÇÌ{	½„ˆãÙyÅ\‹‚Ì)(ªéÁépl‡æsIî!Q±¤
^9]§‡Ï®æ;¨„Ù±ˆŠƒÎf±ÄÕ³j´Ó­¨Y¼“
ĞCí+zVY3Ã›¬¡øºÁàhş/ ¾¯×j“÷ŒÕì$‡ô–—¯pËÏÄ¤÷vË/»õ´ùò^D¤6}¨+›|úSg–ü¼“ÙÎù¹¬®}rÎ.§Ó0WİÉ|cM—ú•µ[>eCL®Ó|ê¼cšŞ
îÂj×e}±İá¦mR¾º®¯èš(ü"v«Íİ~k$÷­µ˜3¼SòyQ§Ó3´Ru+Ş˜3şØ4i¸Î‘V¶æ|æf©qƒo2ÍÉÀYãŠ0®]M’ÿ]O
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
xœí=Û%¹mïıçÙÀ–u¿ A ïôŸXÇ‚ëü?RWJ*ö)uŸé™5f×—Ó¬*‰")ŞDI‡Ò1ısğïOù3yDc¸ıúåé·'|®L7mE¼ıó¿Ÿşë· ÜÒÁ«>·0şÊşûŸ¾åÿüûÓÿ¬oÿ¿Ôú&¥RØÜßDà«ù¼úó§§?~4·xûô7h(a(oÚ>HeoJß>}yú7!´ı÷Û§ÿ}rğüÓ_o Pa˜àÀ7€	ø6¤L İ 6ÀäFùt¸•öP2x‚¹ôs'jêDÎ˜¯oÌ£—z0opˆª`n\pt/¿yYè»]q§o=Ò÷BŸŸë×ÿÿşö$¥;şcnÒÛš7ñ¦”1U@n-uQÕŠv”‘‚7İ¡L´÷…V˜‡(‹ÔÑCSôá»m(q ë}p·/õ7<øŒ¿Î¹€ xÏ6Zf˜6Ñ ÌE¡ê{ÂèÛ¯øq^ºÔš>¼v_ŒæHçà—„©­”.0øñc‰Oó·
¿qø¢×¸”aA:¤'v¦BÌ0búX!ZÖ—7]…oúÆ‡CI/¿~}rÑ×?>ã‡ÖÒ´7à¬Ğ‘4‡°hóCÇ.†C9…i("Ìjø‡aŞy³‹ÄDIC¨ƒ0T 4DÑEJlí¬"\I0à!ÜCXaoş¨ğıó};8¤€¾ÑVæàùĞ=À€µÿ‚gğHƒÜUÀ€Ã¸?]¡Z¥PøÍ@Ğ²H0Ä!³®1 €­¾Q"8³şÂ+]~¢‚Q_¦T¥¢Ö»§BY%²[†Ce¼›L†B:e*éÜêô¦³°r†ÎÖÊÁ>³}úÔ	á–ÿƒª şNZøjä‡&ø¡	~h‚}Mğ—ï x©(UÕ€"2¨†5’PQÕ€°Y5 I8ê†Õ¬4ë„-º!F‰ßhªÏS†!lÕuC‚%İİÿtCñkÍA%‘n(ÉoC!s„Œ™L¦F>çÉä,ÔuCc™í}E °ê†Äxª0ë†›tC‚Íº€nÖ	6ê†Zt@ı8Q	MBó$ô Ğ%º!ƒªnHİP~SİĞ_îÔÚì’F;ï2ÙÑl¢ÛGÓeœ»M†FŸ>e:ûä¢ôîÓ°s¦O×ÎÁ>µ7¼„ªà‡*ø¡
şµUÁ_NR_ÅH9{“à^Àx„c²DÀ|M–¨)7b#”$ªs²ëğÂ*Ó“)&ç…âá´^õVÕVAŸ²?(™¤ØèpÊLYp™}¢§ÕL(-Ic‚sK®líÛÔQH¢$8ùÚµ)Ú7 krNÅ÷î Z×F*¯í…ÁırŞu…*:åÌÉà¬wÆ8ûjT9êMY7ÇI”ô€p8,{@|e­%„‘œ ÕñDí¤Q+Å¬ÕÁÂ’?•^z£½_™…væl¤ÜmCúhDÚ¨ ÌLKPÆyáÕ…aTÑŠZHiü}t_"h	×ax#ªH=Î›(\TD¬cyàA?/`ûÌ‘êÎ¶ôKy Ó4Ñ	©fÛÀaûÜ9.sŠ÷¸±gIUøT'«’(G^èó‡›¬¬Â.«<gÒÌ´*¶Fêå},~.sWÃ´Ğ÷;o´Ñ`ßlè}ï«Á*,ÆZ‚]Y|U3ïwÍ™–,ÉÙ>ÊD±,¼€ÕÇJsçÄ%¦9‘ÏkOÒ"€l‡» {‡¯wE;yà¯£ÀIbëG* ‹33½Àƒ”JOèÅ™|NLxz±c|<½Vc->ÌFÖ,”Ú/îèË@õÜsU€ğ#bRüµ€ó):-gz ­ğÑ‹…‚àŸ
x@ÔY›Ú‚¬[3¾€'6Ä™Ná:7Ä¬VgG‡½"\rÕæt¨Wú)‰ÄûHñ}{†"M¤Ğ´Äû£»OAˆ"ôñ‚A8a¶¯ÌÖÕšCäcös3ºøèˆ(7b(.ÑyE'À4‚¡^Ç îq$óÎT>X|ˆ‹èƒÁ‚/¨Zmdr
¨aí<'`@?ê¦~(ÈZÔJÍÂ²l@£›Es¯}‹¥)_›ÁÓ£OÁ^-Šû¤‹}ÒV)0Ñz·Hæ		w¹ÄvaCs­ìÏ“¶	ÕÙ*$„2‹f¾>:VrX¶6á4fŒ¸ÀoVjG¡‹ ˜¦±"	½_œLBãìNAQÿ„à®íáÒğœ<'´tx "ï#;°ÏzF·Dq¢	ÁÇˆ5®~8i Ck¿Õ.	YónqñX¶f}´yAxÆnóŸem€ZFcÃÆÒ™%cÉèÈùqp´b›b±bûĞYF¤8$°â#äÂêt_–!¢=€S¡­<‰ÄvÑÅ+C¯‰Ìiì6Í¿\ÆWûà½8qE{[C9{aæ”¾ìP/WªXİö ã’=Ü1'œµä³Q“Ûq|ğ¦¸®÷§1cvY{¥\õw]ö03Ì]ä}[Y)gïüÅ°Jñ]‡U<V’¡ë~ ÆbÅCL|Ö$ßƒ”y½DÄ/ø´3¡š½ÕI{¢´–øóN¼u‚UÍş)ïSÒV¿—¡ìÉdY°}>§Ó{›mŠ®9n7­² ûLøíÖ@éD¢¸‘3”º« F0;Ë›ˆ!İÇF²¬bä\ÿ†İlàÆ©Rê„:s¡%Û‹fv†¶;áI²m+X›ÊzûÃx\Ô¿ïLğŒúú!¨®ÃpvŠÉ?TÃgASĞ4*ç˜˜ŸKçĞÁ«°>3ŠİsşwâßKb5DÛ>ó>V|<tIzN#ÁËÑ&KöıØŸW%|tÌ„Qläº­ÙùRi°jY}Yw6wó¸LÌ%ó4d0öç8=P<ù¨üëça¶“ÍÙğú^–Ïİ4ÌğKÜæ$íÕã~ÑAÒ€SvXûJó&n­x¹CnTÒhÔ•¼ö¶!ãL"îñÎ×–Cœ¸Â×³óÌ(X:í.ˆlä|Û™ókIêK©–©¯ÏÚ/¾Û9+åbŞmË5™ê!–Xi£©7:xC®ı<Ş;àòlSªÎcÙ*¢+x·±õ¼à²ákï$2w2µ”³ƒ×Éq¶åïœÇX^İç,o)9Ûú
ğŠNºšŸç=UVª/E‘ƒÓ´ïÒpâ°f)åádŞL¿˜xÓ¶®g‡ ŞÅ¦µ8QNÚZüR_ƒèš*ªöQH%Njğ0¨ñFĞÁÔ-)¤–ÚoÜN­A;}y2!eN£K€C9x„0Uyé°
!ÁxÔ²	âA¢o¿â·Ş8åBA$¾ç„`†(å4ÂŒ4JÊƒßå[xêpÛ Bá«ô¦Bƒ~J0+WÕƒÕğ+Á Üî P«„V1C“N3)W¨D…áÈMj
k¸i4}êLê;ÚˆCYÆtñĞ=b çDRÄìS7Øô˜vª=ÀRVR¢XĞÅ—F:{H«”‘#‰-LSà¯ï¬°”Sùô"ş8Hw¾8H5¶/p”&·ßğğG™pkøÌc1ÀğwşºÑÀcI•Oo6ZZ7U&mÚ‚AÈ@@ØŞ(—°-Ÿÿ?1¼17=èüoßI!™jèÙkh)%$òÜHA¤¾‘ŒÎN\:*è|«ìŠ•‹¸è<†p¨`B­=İw®™–kY/6¹bZ¦’“İï#]QÎ›àà,A¶]Q¶ †5K¿Rl;e9ª	Òh‚"îòj’o×n©…P¸vã¯,ãîúşUf¥%°×jâœ2à, ˆ“¤a¨KèFØjãŒ“CÈlã¶Ú8„Î6a³C`aF‡ĞÙÆ%Xµq¦*Ôª=ûÓ¦d{#]ÓîºŞîˆuıŞĞ-j·(İ¶TÒuDIÜ­Ug†¥ÜÊ+gdf¼ß¥aú±wbåŒLã´·ã4N5ÍX9„ÎVa³•Cà!+‡@@8Ü>ÙÂ@;Z¹ü€H@ı–ÊJï„J•]¬\G›Ê©=±rTî+Éèq'V®³Î¹Ê®X¹ø²•ôª•ck/¸‹K¥.—Çı%¸6î6n»Dx3KÇ'ã.U€de+ÀXCM+À	ˆË0Yu‡8n°6Vƒé
e©ÈÊ0”éV`I[†<1q5ÂŠ^y
§imêß'ºÎ€¤¤CÖR”yÈšÃšMj?dãB†%óŠ.Ê bGBQZ
¸ŞBQk„v)©*‹J/dmè#}š•¦U¤‘¬]•{Ëª)ŠVÑ×–¢O4;h¶ÆS‚[!;Õ²MÑ~¤n±>šòÁœğËfnÂô©Ê®ÿĞŠÊ!ÂĞŸªjvÀKæ°cÀ_æğd©¬*~ ‰L_İÚÉÔúHeYÍËÀ™ÑÀ6Yø)³ tnã"õ["8½*a*‰í.±}xD°+¨ôWzÑyÒ)KgTåA8áU¬œÄÍİÓVîÑI†ÌÖ}"/X“ítÿ+ö}°½o¯g|;®[ í/˜¥ÿNn)JÀ(ŒñJQi%LÙˆ$¶u7fXñÔ;o‰ıy„ûa,Û9kü·÷‘<²p‹vn®d½¯8Óª	Gõ¡K·Eskã<V\MåÃæ$ve¿bü~õÄå-ƒ ‹U²v.e´gÕ¥ó®^É°-Û‹nïC¬1EFmL‘„¸, l\@ˆÇ·ÆIs‚ K‚`'	€.	€-	€$H ŠN" Ôò#QNù‘ö´‡çµÆ“ÎHÀßĞ"‰†>q¿È@I²¡‘„$%
áHò‚˜¤9
#,åSş£&GĞí™– 6/ ì$9ü²€°y	 a'É€&Ò
½Aôä(Uƒ?I pI¤ŒWşÿ19’Saûí["'¤"Q"ym"£d€Dš)ˆÌ7’ÑÙÎ’#t¶…¾¹x'9ëcS¹ÂÄtzÒ]äZaèàr=*M]Îª>‰~·=6s±mßùè¾º Î=Hêœ%­øÀ`»ŸÔø]±Õ=­‘óq·‹·¸ökË›©¤©«ì˜šÀ’šAØœšA˜ÇXvHÍXå’z"É¡vê¡.BÖäBáG“3ƒ¦%‰±´&g:%g¨&g¬òcr¦?íÙ€ÖHOĞŞz‚¡£ÕınYè@{r£¤'A:İzº„R¸'V:/Ì	Ïlæè±Ê,é„Íé„­é«ô’AØœA˜ÛNsõõtÎétÖ'é„Îé€ê1=“‰Ğsz†vBe¬¢Ce±¢İe¶ˆ¶^Ò3^t®˜“ôLçA8áU¬œ¼–Á"òbJ÷=¶şow¡­‡|EQ"£ø^qÆÆöŠÅë@ï Uë¦ê% ,Â,–¢çakèb]"¿Yİ=„xKê"ÌHÆà¡sğ‚°9xAØZÁ„Ğ)xI ¼äC(‰_ÜŸ6÷¹µÑİlÚYwÈ;ZİqïèåDÚƒN’4tÒõğ‚¹"–ò+ÿQëÖ&„ÍÂÖ ÆÚ¸¬î"l^İEØÀ t^İEØ¼º‹°¥†	sÀ2íTÃ”t	°kí„H•]k˜:ÚDNíYS'‘üF2:GÎj˜:è¬#5L™‹/0ÖÙ9€¹|âÑöfõû;ú^<•ÄÅ+¦à{Üøm“Ïlyß¦½ÃvVHŞ°iØÅ©`«ıñ}/;–‡Âjq)E?EJÑ¯‘Rôk¤ıÉ"6ÈÒ¸ˆ€q!'qRkœÃ'ÅŒÁ'Å°ÄI18)FNİíö”¸åµâ¿“Şˆ§ßĞ"ACŸ02Pe4‚h¤PD-„º$¾i|0'ü²™›c”İ%Å4h;öçÎ¢¤h×()Ú5JŠö,JŠ©¢ÉQR´k”íY”í%!Òù‹)JJˆ<Ø%J"P	³k”ÔĞîkO¢¤F*ıv’eéŒª<'¼Š•“×¢$t‚îÙë]ÅóÂ:Ç¶Ñ|àQû'Ğ½¢Hl;¸ëí§¹^q0»F¿Y’Åš Ş!ØGvŸ llJÏUsò~!Å~ùÃ+6)n‹ÔÃÖƒùQ¼íH—áÌvC»]¦’ß¸"{÷XÃëÇâmo¢ã÷(2ìè›Õ¨æd½0 äÈ›Ø„YEmBVÌ)1ú`HfÑR2Äò!t.$DØTHˆ ’´ 6¡“–@ÕsÕÀWcŞŸv£ßéŞí­û­îotô»gBÚ}˜NîëTªuŸˆR·{O•æ„W6srğÀœ‹†°9O°ÕsÒçÈŸbeù˜! ã”ş¤Œ¡sa³†°’Ç Ì>g<(Ó`ª†üÅèå]Ú·]lH'D¾:DÚM^ÉğºX7:Ùoô¢³$œx`á„W±rò¢ÖoD¾¶«vpQşT?	½š&½«V4suµïk^ôU3U;XNâÑk6Lm/E­ÃaÈe;²sn<¦·.{µ^ÊÏÀƒ…	ÍzİzB]±| QÎ8`ß’;ƒ'
Ã»T‡b7!F«Ñ1G O!ÔËŞÀYzu¹”³A7È·º€ Í¤îŸxfà¡öá/«–›)Bº-ì¤Èx¼oàpxÕağ&¼ğmÖûÎåé©0¾
£>àªÉ…ôGÆ1!‘Ğ'ÍpãûÏ'0·Šã%àğ·Êm!Û1¦·‹ïY—ÿÆ¶¾pÄùÿ¥ÄH¯ÍĞİ+¹oÿx’¸Ç9ÊTÔc¾‰ëåª0_sûsƒ„z¼YšÇ½ØB†sÀ~§êHÁ?3x/ZN‰†Ë ­(Şë
:I‚A	½¥“
ú‘xI©)}^\ÍáÑ?ìP¼¡"eĞ ô]€¡Ş–ô0°ÌRÄ#”Ãà€â0y“û)c`…éë
m”û<BATUn³öƒ@ûXŠQŞâP®çk¸‹w—	Ä­Ñàıè6¬Q£ÁÂrŠ\k4nPÂ‹ÖáÁˆğ·áNä ñLĞf¢Œ)-£4âv1[eŒ@t]dl€BÛ{ğQÈ	…»½=Ş-(À¿QÆ¼ÏY8¼û t—ˆ}”¸4ª´EP–:WR7«0$¾‹UÄ*EÌ£"LŒhß+o˜“C?ÊƒÃ”Ö‹(BÊ£­“Š¢¿dºÁ±±À<!FúºBá>?‘ïBo(&<j?Fá(Â€&}¾½·ãn4Ş¸|##4:õØ6ZXÂ§Ó­AŸNáş}cDí¤ó‹"Ó9ÛÑ¦ÒR‡w"AUº~{J?)êü‹h¿ŸÎle0MøåéÀs½òÿà­hFÈtéŸ\Î96x;³m¥º¨ìYı£Z.5Shs †Î	öEÿn–fé"âuPézÃŞ8ĞàœÛ´-ú!~ßº@1N@c?b6Ş·sò•ı""ŞfG¾Ò¯²WØc÷‹Ş:t¼ñÄê“|Öpÿ@Øı<lŞp{åó'’}Ë€w”×şŠöö‘û—ûü¾®¿aü7pÏrIÜKùÄíS;ï¬«ŞÓo;·C8øÂÛ‡j>ğÖİKëP‘«	—šÚ>˜¿~cû:”Ş¬òŠÃ•x²óö9“ßùÎË"À¥§—¾ÏÕ}A7%Ø©¸1Øµ¸aã®,„¬¥Á®¥›÷e!lİ—…Ğ¹´asi#ÂÖ}YJ¨–6;•6ö§­°®µÑğhg½T¯£ÕKú:ú=ŸMÚË;Iz9a']/<¤Dî%Š•–ò*ÿQ
ƒ]66"Æ)ÇÂÆ`ÖÃÙ6ïÌBØZØˆĞygÂæY[vf!pŞ™L.lf*lÌ:ÿÛ·DRH'D¦:DöÚDJÍYac'‘{³ÎF‰KgÒZØØÙ+_.l¶6òWøñÖœİ¼½¸»_Å°_à÷8·œK¡?pÿ:¿åèNmúõSö#¡íŠÕíÒƒûÏåÓÁxzÒãâÕw½ë=cC®-âƒåK~î°;ßQ¹Fİk~9wbïè6ñ‘S´°ßù~I{‰ß¾ïÏÖ|p<ßù ó #¹†qÜƒÇ Ş×Ë1…›)DØzLağfÚ…ÅÛóæÌÛó&—šRËìMÎ=SîM-^¥ÖŞ›ÅÛó†x{ŞNŞ^{Ú½ÚñJHgÄih?§¡O<"2Pâ;5’«øb„ÀÄkk¬°”Wùêíyµz{^­ŞoÇ˜ÈÕÛórõö¼<óö¼\¶± lŞÆ‚°eçm,x«{€œ¼½ô€ğ_.ÛXh'T¦*:Töä²…Ê³\½½F2:?:qéLR«·×Ø+ïx{íğï£ ñ«İ`Á‚Ë›¾ÇABÜaÂº‡¼6ü÷ mŸòÅAğ®ôö.Ö÷ğë^qÓÛW9CmòaöÚ¿¬‚u¹¶]yö
ô·U0­œã±‚¦°œÈ,Gw¼xyS”z>xİJÉÑ ßç}‘û6è.=Rã²Ëœ¯?[÷ú^Qn’=î¢ûêów±³õF¾v{ÚÉŠl2® ½Çu†\ámk1ÙKñîÅ×o·Ü^BcirÍ±œš>YËWÓÇx’,C/×­…«Xü–ËÈ¼kÁ®5î/ŞíßZÊ]óxí•Á·¸ä{’{EVŠİ»´íñğ“™]¼{]%³¬¿: ûp¿ƒ­Êí?L·5–ïÅp¸eÊd»aÍ›Â¿z
ÛG6-³ñ¦SzYn¼¢Òm³bˆ}ûø¤Ş¹ÎĞ»-›Áû“‡ìt ì½Óş‹;Œ+m`uª)m•ŠÕ´ÛßÁ
×¹lß{äNíjñ2İé ¡‡Zbİ+ÜµÀS¼¡; æ€u
½f`˜éaØé PèÉ	ºÓ`úğ¹
¿ÖëwİéĞ¡t§C‡öİ½Ÿ¾¯€bÔw tÜûN…>FkÔ ;:å>P‡×Ò ó‡õ¸¿®cät€‘?ìtĞÎà~KÌš÷1"ÌåêşFw:t(İéĞ¿'¼hı®ŒîDÚÏähİé ÌˆUÆT’2~
ÅIw: LJHºÓAK M9ìtĞ8¬t§Àl&J¯Øï0ºÓ¡CéNò}Û-@úiû
„Ú‚zÛ©@†Øö4tbĞpt§ƒvR kÙé 0  7’bä KÔ2ÃN›AƒÎ›EêÓÏ<5ŒîuèPº×|ßXÑ»é<£uîvÔ‰Ä´!HÑ·Úí /‡wÙí@:ÂİâùA»¤Œiÿ»¸·mAÂ«ô}}çıD*ãß‰T­£Fª‡‘+»·—N u\ĞºD®¶åõk“«u4ëa$¬=İ%œA»æ‚?6Æü?2–Øî
endstream
endobj
19 0 obj
<</Filter /FlateDecode
/Length 5976>> stream
xœí][¯¹~?¿¢ŸpE÷°X 3¶óœÄÀş ç²Xœ	ìÿ–Ô…¤T-wUŸ¶ÏÂÛñLõ×%‰7QK¬ŞŒÍåÏEÁ?6ñ19½esº|ıíåŸ/ø½qI]¬Wùò¯¿¾üç¿]ş¸Ût€[cíaüõÿùÓ.õâ_ùİìåïÿSú‹Ù^´6»û[AŞZ/àÖ_¾¼üî³»äË—¿AG…B}±q‹I1öòå·—WÊúÿ¸|ùï— ßùË “fÀÍ@,@$Àª¤uZÀàk“L€«~úrp¯ıftŠ‚rçAÌ4ˆ)ßß1s¯í,îXj’»$ğ@ãòæ¬ÄÍÊÎÔÍäªcƒííÆ”ÿÒ[ÿşùç‹ÖaøÇ]4
Öx0P‚Ğ©İĞ`pˆz%š}È.êµrÓZØwÊº™ë–#ô$ÿíö ôaÔæ/Vù­^“îòŠ×'[BÀAÉ\ğû`Õ³î,deú}ÊYsùŠ­“Ø+ f‹6¼3g˜r!À•†ImŒm\dl¬ñÛÚVc‹7FA?K:Dg-åŠ…”KcƒtùØîzŞ	ô»˜†6Ş®¾¾„û‡Wü°Y«İ‰@ğÊfÑbÙ‡‡CN›	EB$"æ-ü¬ CŒaà9ä¼Á¼ÖNH1L2DÈª2I»µu6x#ÔR°œ+5M}ˆ5ıÖFMñ¯/|7({á^à{1|Á@}üB'€eà/ÌNÁ@‚ïÁehR«4n8«.,É‚A×NÈ¼`@D¹k§ @î…5X!´`Tqù„ú6¶_¿¾°ağÍl@Ô'[šœm’É$ÓenØÆ%ß4H><eXŒ<¹¤¼y²fxº²yj}ù/t
éRÿE_Ğ¯‹=yº‚§+xº‚ÿ®àÏ'âƒcÔ‚Nİ7XgFß ÀÎ7D¨%ùˆ)gâà }C@„VÊ±Ù7 X&T¾¡`0ñ²Ôb;ßPĞÉ7T}C»ª¾¡}¾¡AÂú¨;a§b`aÑD¢°|bEÌÁ³˜L$s$C19…´Å4&½ˆéNúkş LÎ5?8 vÎ±Ù9 ¶sAgB”Î±É9 ´w,dvˆÍÎ±½s@ÈµÒ;„jÅÍ;„bßÕ;ÔëÁ;ĞÍÂ„¨Salbxa–D([/ñ#Ì\pÎó¡KHÌ¤˜_Bâb&’nÄŒ%òì>)<½ÁÓ<½ÁÏîîbd÷¡Á=Ä’äİbÓF¢`5´|Fígï€Ğ´(ØÎ;Díæ}DÁ¦}DÁöŞÑÙ;¬x‡zÕ¼Cı0x‡
	ókİyi¨e`à~ôÄÁ;+b’Ål"éğ¤k2´rvVaÏŞ¡©eğ¤¾æP¿äPñƒw  E ¥w@,0ãÇb«zğ1æİF1oM8e’ØÑ=ÄT¦“—î1è[ROe~êÑ= :»‡‚‘{ÀOİ=ÔëÁ=ĞÍÒ†ÒŞ=´á'÷@„
óíüH;gÎÅ„è"’ó¦‹RN0–¹œŠ];rÊv-òô>-<İÁÓ<İÁOïî2˜A÷ÉN»‰d÷»	ÄæİbûİD²¦7Ë!|’‚C.âà ’İå6;ÄöÑÙA¬8ˆzÕDı08ˆ
	¤î„©Š…Q‰Âø‰1MÏbB‘txŞ‘ÅÒS™ô"¦<é¯ùT09Ôüà  Øí&)h9>b ?8ˆìín7Ø´›@h¿›ÈŞívˆÍ»	Äö»	D§ÄcÈ=à§îêõàèfaA½Oajbpa”D&Û.q#Œ\ğÍ³¡ËGÌ£˜]BŞb’fÄ|%òÜ>+<}ÁÓ<}ÁÏíî¥hÎÁ)•ç @œCÁ&çP°s 4L;‰MiÇ‚áµt ú9íX°)íX°Ğ³jZB6Š¡shWÕ9´Ò94ˆ­»c;•³E3‰lùÌ
ÏÉ3O&–Í9–!ON)mÆ¬î¬¿êŠ‚»s(š—Îy'Q°)íX°y'`y´f„s(Ø´“(ØÎ; çDÁ¦DÁv;‰‚Ş¡B9•ÕOÍ;´kéøfaB½Oakbpa•D&/q#¬\ğÍÓ$f	RÌ/!q1I7bÆ’yvŸŞàéŞà§÷>z¤òò`f3YT¨İCt»ù•@‡ HÆ«”ìÑ¬t*hÚ ˆ‚97mà€ø|Æ9§‘€Zg€1ÀAVÁ%ˆ}t
 #4E`û kq•Óu‚³Ûb†°Œ@Ôl±‚‡ö€‚eå‡± Í›Ñ*O”«0­¤6 ÔpK9Ğ*œÒ¾Mˆ¯B…EŸÂ…‡)*]HÂgˆàL\e´QïD¬)GÜ1u>C(Xˆ+t°Ô\SZ—-·a-pß¬1Aë–©e+`®v„&ˆ¦e!‡?ÆÚ­­<úU³,‰Aä¬m2hä~SIg<Õë7 Ê[îÁ=fmÀS} ùà´™ƒQqŠ|@_su§aÖy“LË9x-Ù”REÌ!w{ m)‚OHÊÍL„ır/00qAy$ÅDph^›j32èşI¥uÃš¼^_¸­í[›@<ˆE—ê’—ä€×ßlÌœF9Øófêñ7bÑ)<A]ò”$‡ŠbHXjHª¢m—¾‚Ô4Cd!öf«éætüì7øms©ÿA‡ŠÑˆğ&©œ\×`Än8»îğ˜D=»îaŞz¯”ûş°‡µ@ÑñõÍ!ûÀQ®5Ãç^ú°f®S¨x1‚AÔÇé¯§°µL;|2öëp|ÿJ#ÜÈ*;7³7šÙéüƒdG]•İÃä'EÁCŞ”`Ğ0ÿl[ 8#@h)À‡	¤T{SˆQ÷ÛïZ7Òü‚Ã#«à«~{q©.¡ IxĞPÂõĞ´›6o04„¸ÁÅè}Å"Ş÷[G ÂC`i”°"¦¬ÄisVY]1‡Ü–¶ğm(j…Ve¥•M±bÑy#f}ªPË7 H—ÉÍÚ ôã2Q±D–®0Ru¸ù€ÙÊoaY‰9Ù	nf\°z¾Mh”„Áÿ£Åª‚Ø\%“Y…˜$'XÔ¤PàÿŞFÛîT*—µ7Æé.d—kk0ŞX9AuÀ}R[õC¹¯,².C+‹lš±‹|êÚ?SbÏÂSl€OôÀ›)×µ5KÖŞË,-ƒ½»Q®éĞU)¤ ƒ°LS ©*gõâÂz[i+<ˆ´ªN´¾N¶´SfPZt…´û.29CX¸r.u5È9×Õ•»1İQ|…Ÿ]E@O‘ÉsÖº?àÍúü\·†Øœ-áMo,ĞÄµj>×âµ-¡)^i`<ëæzBB·Ğ@;´!ŒQ®^tŸ[ØuæÌ=­¸s½#¯ ÜaÒµşwµ`P‰{rÛïAÀkn±fÂö¸Á¢Àò×F °á_Ô²@ôÖğ…­û¥QòXÊ\Ÿ$Öıº`»ÂÎg<œA_¤FÌûí‘1Ê[½âbMìã•7³½’øOÁõrÑ3ié ûÌ“ÍNLÕÜìF‘{ù…oÖû©œ¥È¥7Àıûn+˜ÛA»ÛcÓŸŞfğSŸ¬JÃd]¸;öåÒè¥ÄpCÜ f`²Œ›óF®	ˆì£&£ã5!+“•«bp­Ç¨	Ñ9jBlš*Ì5!:GMëQ“)g~ÅjÌßÒ¢Íğê.‡ã8€	ãxàÈB²Ê1…c•.:i¤ˆ9úéªğRSõC‹™L9ï6ÆLˆÍ1“)èæ˜ÉàQ»)fBl™ƒk7ÆLˆÎ1bsÌ„˜öåğ¿C‚ıeĞ’kêscÌT¿úïm¥¥ğ Ò¦Ü.fb²¥•2ƒÒİ.fb‘Éùá¯ÄL¬9ß<ÇLU‹ß™Œ¡TÇ*Y/Ô«°âPçüúzz©^~È³bjôœŸ^“†¨p­¤ó”KlLùvWëPü|p±6ª³ñËšªÓÁÖ:lëÁE@ƒ–ËøÊ Íbr÷şXhÙb$-ã”¥ùR—ä3İc¾)”MÊ¼ÁÜ–Ô3¤ÌğÉãøæté°ŒT—n>u[‹f~ŞÙšÆ°_³agŸ0vRyïW5>MÙ›03~Í¤»0ÕÎåâS… ûêœfÛM›kÆÎR„@B›,÷‘Õ¿åÍ˜áĞK‚›Fvƒ¬™oöã¶ş5!¯O}xëMŞÏó+²oöß„”dŞMzŸ–ò¢÷œG½§ÍkƒÉóĞ'²§ßùhaØ
EAÕAÜ¿!¿%ãË±—³ü|˜ô–‚Æø•µ|¹È‡¥Ù"çæ€ÏûÖŠê]c’Õ’}ÌŞÒ"bNr™=&*¹‰_/ÙËuv5ú`ˆÃZ~>^8”•º’Œ¸Òb™T9ğâ•Ó<«#\
q¬„¸–Õ*`X¾n±dp¦-sYÏ3İ˜µƒ¬ºq óp(â;MÕÁu3™R”û1g2ÌƒáM¨õ¦ÜoÆCcãšÚX¬Î¯Œjé–}¼ãqíWaÏ2‰ğûg¬ÜS[OÓëì‘µã­‰¦µ-<nğGfÒV&}Zåk‰,]îã²$çMáwå?ğyÊ™un,—‡Óù–¥¬úût/²¶Gu»½éyrWaÒíghÇ5øÀ°uÉàrñ=¯+®Â½uÀ~^V§ƒéuWœ§cGˆÑÎo<îÉ«ùjİ\»8éÂƒ:¢Â†ÆKg²\ÿ¤Ş¬ë/oç3İæçåfuªå|H¹ìj-œ<–_;´¹gp:Üšg9¥°µ BZáÛ²Íå¹çÔhXsÒ¬àÏ’}` ú'„N?·uy%¥W»˜Õ£Ó®$¬RˆÂ¦µjÆ®ûêyÙÛœ­&ÚÒ¢¾*{-Ø³›ÙÇ=§¸1ø)µè€á°jHÿé-ã«¤Í` Ñ-LpxŞx:-õÀ€r}àĞÉ¶`wıÎd5šMG’n? p[)§E¸¶‘ó´ÓÁár>¶Î?W¸½ŸD¿0Ääì’RñH4y¯_øvlú¡œ>K”Â˜)Èb­{‡œÈ¡¼Ğ©Z.4š»Å”Ìeø––ÍùTv Õ]ÕS=l°–ê#üÍ¨VUê«°¶
k¬”Å-^Å]">^Áşœ}Ãç†¹¤JUéë´‚*µZ¥vË¡×­ı»õ3öÑûÄv¥}«ïÂï{;˜%K>^÷4wk˜x›Ê»µ1©•vra/€a³¥ø˜+€t[…ŠRaø¯İ"Ğ‡ÚnürÃêN+J»¬V\¡L¬ë&PÖuÈeÑb. âZk¦k²“˜zõ+ƒ]p¯#6ïWÃ$7$(Ù|¹±¤$¨6U~*ƒYD¬¼\EÑ!YÖM ¬í&P(ÆúÔÍv²…wWìg_Ü­“ÊÍ´h<UKPÁ1”·õj`m\Ú¬	ÎˆÂa ÃæÀg{Yà¨›÷øËTŠ`)æ‚åÈïÉojIeÒr ª¨i¡âkI7UiK©š›d!K¼Ij²È['­7°¢(òä­•$%|Ù(¾Cy
^×:/Š¼Cáák#X©×é™%zqK–Û’xÖ•$†ÕÊdK!ööÖsG™÷Ú×Û%ŞxÜ¾å ~ßÿkù¾±‹ÖGJz]ŒıWîr]
p‰@·ï>+*ïíKDùîÓ~Iº¾TÜŞàË¸IÅ1¢s8+!læµ—UÅ^Vß¬h}„F<yÿş‚e*ííRBo¨±–RäÍ©8çks+jj*áTšTæYİ¾=BŠè1å˜joª›·™C’üæ}È &Lîa!=3¶¦¨h(kÊ˜6¡\ÕT¬55¾EA¡]™ôˆm;VîK-ní‚ïcE1ºÄuQn}y)ºïY³¿><¹Ş”ÔµjÙİ6õÊAá›r¯µéç‘±D}8İ»8À¼<AÜr/yKYÁFëÁë¾î8%½:	şÃã«Qî8Ş’µXÏâÒ»İòº®ã„„—‡Íï0	uãA–ÓaÍE{ŠqãîòË0|÷·Ÿy,{Á/îÅêÎ•ÎXÍf~~`õXVùôÉé7”Äì#«ƒ4Ë¼üédÆï8}}\=-Ã;¾?ÎH–nNŸ9ZÛÈéª¾G–-Şñ„ıqƒ›7~õTéØ¡•e™×İ¬ß™ù&÷™/£{:€Ó€ÁØÆf‘÷öó^É<
lšai³Êi/|¯Û¦õğBCÀğí“œ¾i€Ìx5Hæ»Ä#î›sK’
NB1½œ¬b¾¬§H³W2] î2]€aÊ¨d)ˆ[“KfHuašÓPA¤º
LMu!Ø+¹.e®‹[ÑÓ(BI‚¡N¢\¨İî³]$Š}¶Ä°ÏvzöDbĞo(/çìIÀì–=ÊÒ'€ º¼«•ò, * ¶—Ò1`áudÎÚ$S]Ê\7¦t‘ƒK1”‚dSªJ°G9­.™ç"yÉ<—±5”E°’0
’[RKn|™!¾u“PQä¹ K5—Gb°û,WÇd–‹Z’ì¹{V’$„ÕÉ$û Öö6ó^¯2Œ~xò¡Ä®íâlßI¦údÄÑ}76½òÍx<ÌyIÛ:ÂNºS¢ÇÎÕ[Üı†›{yFØÏûÀØ«ck>°ràü“àïÇ8şr´ÓÕ%K…Ÿ|Ø±R»ó•ÃQ‹å	Ò³5QŞìêJï‡S¬O9‡xØÓ*-"#/”wiˆ=¬‰0Ê{Xé2¦›‡€Ø+|sŸbßŞ%,¢<Ï¯æxĞó;‡9pì ˆ/i‰
jDÌJt‹Ø–ø0Š¨ì"{ÁŒ©¤!2NIoÖŒ‘qáy7GÆ)á¯ÉŒ‘qJu‘qÅ¦È¸ƒCdL­…h¡-AĞ+Q.ôO^±+‘qj9‡ÈØó¦B‚z‹ÉË×|C”•!4ò)0ü-ïÄ
Chì‡ïı{3„ÅŞL!±7S8\pDÉ}rì)ç(•Éäh–Ùá°×ÓB€‰Šsëäıu{û(Éƒ˜á™/`ÀŸùš„¯Nc,œ ˆBá
‘p…†@¸5#As×¬IëÉ•ÖĞÙÚ[È{ÅÁ)ô'¶åÔÎÍ¿·bßòó^áÔSà”ú£ÿ¹†Ş·şúÏ·È€l{¶Æ½"&«ğ‰áŞc¼ æˆ‚NcöÏ”ßgo‚ûŠ¶Û¸QøP~½ï~ÃŞ„{yîM{“ÿë{“UW§øı·çK³¿ÏşàÊÛ~îÜX?åÊ­¢¨…cC 5¾ÌSî¬rZÊ½`	Ïd{@#ß”{ÀÂtD” ¹7 Pîä›ÇàX\RÃQ;ÓÍÑ=ó7`´UaĞOs Â[o}QsNr_ XŞ\}q» Ú'µ›å¾ 0æ’å¾ bã¶ crWÀm…ôi¡'AĞ(Ñ-4OüM6såg<XšÜ€¥ÒFJ‚¾ÔŠİ `v+ï°ãØ0ç0‡İ€UäB-w€¥ñDhGä cr[@-)¾ıS$>Â?ÆÃ$óö0küÛ>ŠvPDI?÷ã=¾_?É]`¨ı4Ğ+8Ìã4î
 Mú±+ ¬? x~|À²òüø€EJIğ<kHÃºd²¥etöFky§ÃÔ~Ç¿M{+Ğ¤ÓmCG·ƒ^h¤¯Œ‹cöë›cke6\ ğW¾dwGFOj]|œ­û3€¡K¹ı/çJ›
endstream
endobj
21 0 obj
<</Filter /FlateDecode
/Length 7085>> stream
xœí][å6r~ï_qXËûØc{Ÿ“ ?ÀÉnŒØÍÿREŠd‘TµÄnu=îñÎÎ9ŸHÖ•E²TÚ”éÏCÀßmäk0r‹2Æğøå×§<áue‚xh+âãŸÿıôŸÿòø;àf“~êsı7¸Q>ğ¿ÿøó#øçßşôgıøÛÿ¥ö|Ô)•Âæşš?Íà§?|~úÓÏæŸÿ
¥Ê‡ö›RÙ‡ÒÏ¿>ı«ÚşÛãóÿ>9¸şù¿ ¨0f||´H@àÛ2º6ß+`r£?}>¸•vS2x2réÇNÔĞ‰G>ÿb¤^ê`~ÁTóÀà}ŒáùGA~,ô8ºq¸â¤oĞ=Ò÷ÄŸÊİÿÿıãIJ·9ücÒÛš}UÊ‚š*`·ƒ–šªêÕ;ÊŸÈÍßIå‚ßô~ª´
Ô<D¹kí=4Eÿî›AhC‰Í>À6ìã×ı³áñ?´¹€€‡õÀëN-3¦M”ˆ¹(Tù0Ê?~Á»ƒôÒ¥æÜæµsøËÁH2dœÓ%Á¶•Ò;†Ÿñf‰Wó½ïqøC¯=ˆ)cAº…Ş´
1c8
¼Yá¸¬ß	ãµøK¿ñaÇPÕ÷O¿<¹èË—/øeÓZšúKœ:’æ‹Ö9ßuìbØ”SÑ!"f5ü!¤ æ‡O”f#è‰’†p1T <DH‹èbÇmDvV¹$ägˆüÛœoÚ%ÿå‰ü5X°·[EÌ¡’ş.È½©<Pé2!wµÓƒ˜Õ0PB9bğÑí|Ûy$=áAx‰´-)×ƒQä®«|…ñ>ˆcYş†Wº|şòDT£ş˜¨Pi“èéœhefSŞJÑrBw3‡Ê b5•‘Ä¾Ç‰%VÙ‹­2lÖıËÓÿ _ü?tåsò$ )p%ŞàÃ|xƒ?†7øËB”°G¹tqZîAË¤^–ºÄF÷€0±÷Z&ÍÄ; 4zÄàCì¼ƒ–³w@lôˆ¹cï½CÂ’wÈŸvï¿tŞ!CDûjsDOIÇD£ë‰æWRˆš‰5Uî4£Ûy¨©uff+Û{‡*bïU|»C@ùVï€‚ï¼ “w@lôˆMŞA1yÄFï€ØìtxuAÓ®c:`8ˆŞ9 ŠÃ¥Ş±İ5äÙ5äÏkÈUÒU³Ö1UÈ2D¢·;!T¿ÅÄ
k¨½RÃj¼¦&X¤BMµH¯™õJ”ğá>ÜÀ‡øfİÀ‹Ãƒƒ+~Áƒ*t~Á[‰¤n!m‚££Gl×TB§·"ëtcB£_@lòŞD¼GR¿€¡Clöˆ~!aÉ/äO»_È_:¿!¢xµ9¢¢¤c¢ÌuˆDç+)Ä:ÍÄ*wš¹U»$Ü&\åB,½ˆo÷(ŞêPî[  9`©[@ltˆMn!ª0¹Ä¬VŠ|”½[ˆ*NkÄÆµbóÚÑaí ºvÀoÅ3äÏg¨?&TÚ$ªF:'JY‡Ùt·RC”œĞİ¬¡2ˆMe$1/ÂqbˆU6Ä^«›m¯Ä¾àÃ|ø‚oÛ¼4P°FŠâ¬¶˜		 ˆÎ!a£s pZ@$lX@$lr	œCÆĞ9ìŸ²sØ¿Pç°CMûZsMOiÇM£Û›æ7RšPš›55îT£k<lÖI˜İÌ¸I¥™{“^öI¼Å9$¹Sç€À¸~HØà6: åè6¬69@šñ	’ÀJÊsÄ´ıú!¡½oÈPñéÛîöÏÔ7´*mM#¬Ãlª[ˆ!*N¨n¶PÙCL¦²‘Øá7±Â*b­U‚Í²Â„Oğá	><Á7í	ş²–ñøûÈtSQ:÷Ğäî-üğW‚~']â™ –~©8&M8³)eĞ.B†„âÙ\:f“
ş ê¶ßS(#ƒæ+ ğ°I€E28àŒõ6ƒoAmÌ>ŠæÓÆh6¥§0Ê9ºÍJïh ‚NEaig ÆMI‡‘)-€Ã W€b¬»«4whåPjcÇ?¿PÔÉM&^µŞ44`a¼ŒÖ@£Õ!¼¦ºATêÓ/wjæ»wÆ4ù]¸ØP”daxC›dZ?MŠtDMâmìM7GÚ…zŠš§&Œ9¼¦MÕ¼†~'µošGq#6|08WÁ8ƒŒ(1ƒ]yëĞ¢P¨Ê¢æ~û„…j¡Qñê—U²9Ò'Ş`‡JêªzEQ¸Xt¯á¨||èKßŠòf³¨‡]ÊƒóWIıºá)>ÑJÕ£|DÊmOøúM©oLıòÔÚĞXãL2‚Ò›ÖpÑ:0mp›ÔÊÜâN¨Æ´M³r¡<ÔëÛ¤|…3CÿYøØPOå9¹¿‡tSåHÇSEŞÆM4©’w ]Eó²Á`Püè¡1¼ê‘¶ÚJ)m0=€AÓ¤6ƒçé*Ö9L‹ËÿıÕ?wrssRÆÍ‰õÍÜ–FóåZ#0'ÏG’rj›mo™Gy¶ÛçŠ‡ÁpdÏÍ‚)æãhIŞÌ9‘0KfrA•[4øx«[îáï)è@%¯yŸ?¦à8A¾5eræ$FĞ–U¤)Y:VGkåy[ŸqsKbS<³½Òû.&³´:åO;ao°~ç¢12zÎ‡[Qn4‡|ÑFsH"x‘èäkÆ{¡ûQì{VïÁ=Æ”Á¨"z—s¾°·˜ŸØ+¦³B;aRyP¡Nåa¾7Áõ¨ñv3G{°ªtœ	b¤¸8QÒäÖc„¸`Ğ9¿hËk;*<˜Î^hésa×˜_aAeíy×%%Âs#¹Àva~Ş/äùlû`a³¯‹f”)f4Á… Ï¥Ä–e!×‡)¾O`µ'ğeŞZ·KI CËÇŠÀ·Äi'Û£jµ!át4Ñ‰UÚu=`ˆà%±la»ÿ8Ğ(¿k”ò¼]%Ã‡É{ÏÃíè3Ğá9©rm‡Å…;:Ê»Ü„@LÊœœ°Ã…Mô`Gàºãİêòx;#°ñ†ÜÁ7µ>¬Î>LœæåÚY
\S«¾¸c	í:G¸1ñw°äQ¯/Î÷¥ó(i`Á5Ä‰•+K_yÒ	¢İÂuñc¼©‹Œ»¢\7EL¡õ„¯ÛËDŞÎ—İ/ówB4ø+òÒ©J;qaŠ?%ıùØĞ—ÇÍ^ë“nœVºÙñ’ÙüîCÖƒ ãù`¨Hu^vk³á£„³tñ’ñˆ'¸öf$ÖÀº7ä‚*Ó üqñ Èp×(jøXğ¸Y„0•Go&nM£-~ÁÜ8Ÿ¥1Yìq;u¤ÀW˜İ¨Ğ¼Å(ü`¯„µü‚n^OÎ§=ëñ™S Ú}$Âë<•W“˜À5—ëİä+µ¾âWË®êFçÆÇå'ÎŸ•Ç]Ó9ÖÇ+Š¥»Lr’–ómïàí»É™-ñ³Y§é^L{I1ÄUx»ÕÅKv]ÅI|4KU‚¡WğªÓ+k³‰óD°²AÂFh,åÜŠ‡• Ëvv{6ù;˜ü§	JeSˆ@
°Ë_˜˜Ù	ÒöÏûO¤ÃƒU¡¥¦ıwK†paöÒ{†Mîˆ7»ÑÆR €ß@YBÙéã¾Yp½)ÖÇİ¸IÉº¬³ä<øúÔüËvæ;g„!,ºùòhpSŠEÀ¡ıd´¢a6°"éAhP4ÿv,„ÄípºÔŠ Äæ¤”–dV –‡ÙRFó*JÓ*ÚZ?-u¨%9´±·dˆF#Å
7h2EãÜ—¸ÁãŞÚ8LoB$CP_­Š]:À
hËGÚ…L Ó!dT$¡¢‚}FiJi¢‰„tÖ¤×¬	šÑ4¢Q{¤QsZ˜gÕ¶†‚dª¶TAÛN¥„¢r¾`5d¬Òô >(ª-½§éA)äRzĞªìƒgÚ;o) £‰¥iäşš€@ú©™
İ€jJzM} $Ö$‰Æš:ÑGS'`»ğÂŠ¤N@€¹9àA #‚ø‚nÛ¥NÄ€éZÖz’:Cî[‘Ô‰‚õ©¥©äş"ÒM•N•,6Ñ–JŞ}µÔ	$”-œC1rÛ“~B/Aaş¿[Ÿ¯S*0Û¢ÅU¤È0£ı^ÊN$; JWG}SÆŞ{@ìEÓÄ«Ò ¢$#Ë õ~¸-¶ Q„UÓåtšº¾¾ƒµæó‹´;¶#î‹	®G¾{é±¸ñBCNYùÁr1à}§Ë/ˆÜVÃI^HË{¶[Ì¸\fÚî<Ø(ø™èí¥Cu_§ƒ=z^_Äó[ì±%{†¶¼¯Án_°£¹²0ª ®p—=Ä¢,±ôüİ¾`İ™Îå÷Ÿv/&ğ$@–,ŸÆ×ÎaÆA±›*ÜøÄ0ñlSÅ8¤èœù§)Ì…‡ˆN‚Ã8ÈáÂtF/ÜÑúˆÌş¸IP’éÜr¦ã¬svË‚Ñ:P“ğ—÷úëóÄékNR¼7YMDzpÁÇÉüÿìÆÑ%s—u‡×rhhÃò‚–¹Èô„4°pÎdŸù£…ŒÁ;Ù@óÒ¾÷QNİåä<µ§GŞø ½³.9éª%ï¸í›8
 Ğş÷mïçuÚ‹²+{Ş8Éº0%ØØòñ2¼‡›Z>¡<]+0Ç×³¯IW‚òåú#/IÜY_,Ÿš~#¹	¬Şv„[uUMA.·"¿”öÑ…ı¯ÛPqWVï‘wçÂí¾ôÊ×ÚM¸´|İ2.?–ñ¿Ée<®X¶ô|^›ı?”·-(!"ØL0iAYùÛYÂ•Ø¶ïĞ_2©â×±Xw¹t¿Û–['áÊó!k,«ô¤Î±Él±,¸ÕåğRçÖÏ–£§ó'v.+æ¡›şiwS¼_ ö-J×"¡õQa£¤8ß,¸cÏÎİPƒÆ !ê§¹R·uÁ
ãF*¸_vL‚Å×|¤ñ¾ãK+°.&>~(æÒc‹İ>8›¹œ¡É’|à²ºÙ~Ñ§„ãl|¢=°IgÏåŞûÂ.‰ÏÊDW“ûÙ$ş“I)ÅÙ'ü:Üyó–OúÃ4£á	E÷|tÜbÊtP#1Ğ†4®{f]íw8<ä?82ƒÕ!L³Áb3QºQ#ã&	ÎMœ‰›BÙyù4·ôé¯+¨ƒÂºD§]ï~ˆ˜«
ì}DM÷.@ŠRéà§¹ë<a	§sÎrD°D3ìY  !m¥»}…6ãœˆ“ë9`Có¾mÁĞ„Ñb*Nğ–Ìxs¢w»÷¸¿©9<Ş·¯Ÿ1—íîÊo–Øß-ôYo»ŞÉò9ş}Ô¿ )né±œj¼üPÈò9Â•Ùõj÷bª¿öc¦åB×”ùÚc7>ı;«°¼É¶şØÇ¶øï|r‡Wv=ï{Öç]¶ˆÙ ÿ ûØk„ËİiR?”ˆpÜ°[¯%°^ğaYİ£Î¤.°®¢æJPËreıñXv_^N·Ó´ÔXio–Äå;ïòü»)B-ƒ†
ï1‘¯¶Ä;IÖëp±Âêåûsc£Õåc¬e±~6Ët±şÜdYo¸`5sVİù´˜eCªåŠbÜÉúúãÖ¯ÛÚ¼VŞê|¾|ßaü·^¢/-I;Ê—½áºêrGwT{:7²¼BY/§t-#åÚâaıŞ<X+X/ÿt§ç»¯€ï¨—‹¹]9Ëu²ÖZ.ÁÂ³œ=X-oóUÏ:o,ÀÚ8G7›s¶ß^Zæ\‹J—“«×ÏÉ—3ı¾æ¶Ú¥(®'¢ŞöØØ‹·}ş¸UVŞ´HÏä±¼™ùíL±g‡ò·Ôw}çHìÆGo.Ešß`P®„’WNÔ8y\yDÃ™8>¢¡Lbz_ÀBj>?_½s¶„Hq5ÚºÖ¦±ŒÿùĞ‘Şmu_ ïÛv‹>{uiU©vºñu0Ş1[Ô×Ök¿Å5öy’Oßø€­(]g§5h±¿>™ò×£KÀ¦¨b&ªıG¾º6lÁx< HˆÇô”_ğ^oœr
Q|ÿ¾45UF8c
ë-f¤Áz?	3RïwÃU‡ï‡EîJ¿RhmæÅ×ûâ#‡Ú†Œ,Œw{—Ğ*f4…C€)Ì+>ÚdRSøB&ƒ/õ3¸ÓH®ºÍ€Æ:Ú¾$Ğ8-ûîìLE’ÌnŞk|¡ !Àn6XlO*(zøvÂ¶­Ñ	óì&­RFöl¶`ìÂgJ²8,•Vş’~ˆŸğÇX¯‡Ş%Ì¾y‘¼Tn¾Äc=”R˜Ç—eQÒ ƒÏ&ß]™à1q.÷S™´n:¶b'›ŞÃHø Œ…ÜÄ„mùüo’x•nºĞ ŞKT…tB”ª‡(_6QSB QèÊ
¢ø•eÔDs©)íR W„‹ñ¢Ìã"…Rrq½\àòVGÍF íˆNO¹Š»Á2­`ò#ˆõ~‘Ùxa&?‚ØèGƒÏ²÷#ˆÂ]úÄ I•1GïGÅñR?âEv!>Õí"º™.Tím·65§4ƒhÃi†Ó†İLŒØŒ±±¢mcY3oÊÜæŠ,•Qş²{/Rİ]
É´}û
é4½ûğB"úÑX¢ÍÄ6yà>Í´[X$Ù8á«œİ‚£ûğ©…üoç>ò"w9¹Ú	Õ¥2ªseØT;åûh¬ ú^XF-£1—ZPµ´"®X¤ø¼ÿğ°<Éh`÷”ïÛ	¾o	r¶§\\øìŞE)ĞZ´Ê`À@â¶…²GNJ¹ÙI69)¬}8;)@Ç`±1ØA,Àü28)…Ù/¡wRÊµ`Ç§¨R3¨W›µÔFˆY‘îˆÖC­“&¤ã¯L!N¢2¸Âfâxª@,•XşR–wŠSmw¸Î4*Úƒ9ˆw¼ÒS¼ƒØï và° `“ÃlvXJÏKé]„zpXéÑ=;,Ò	Õ+=;¬:lª©úÈaUVPİ×S¼C™Kí©ˆÚ]W,R<qXõÅšğ’,ßú[í^UÍYyï4v]1g…oƒ¶`”´–3€r{+I-g|*ÕBmÅ€Â÷‹JÛ•r|$NX­ÀpÂ”¥¯È®-ä\AZÇ¹‚­rë£ÕL¦£iå•ë°[æF]‡e6Ğ"Î•a_:Pæ·E“Î€¥·J{:/Óû§UWÁĞô¦jG
8'$æIıæs]õæ
ÒÚÍín"‚Ú‘j9‘~¥ğ@wæ²ÍÊ³«eğ»Zu , ¤Œ¤h³Â> B“¤0`b^:Z´YI\¿©IÑf…ensg]Õj‡hÉæ
ÒŠÍíæZö˜ôQË#wƒ©…”É°kÁeB^-Í\ù@ë5WÑrÍ ¦wA;R®°ôÊèn<.â»¥Mì
6šŞBmHÁfÀÒËª=)Ø¼c²«×\AZ®™Ü]EĞ:i²¢ÃiRm§zRœuç«ÕköÁÕ½‘ë3ÿ(ríæ˜ë1—¿öçş{Â®DWÃk:'ÜÎ¿§í`ûéO8ƒä6ŒÏãH÷»:ßñ/µÆ—ÜcèÑÈ¸ôjí lıùó)ÕHi±ÏŸ±†4åXâ€Ü)2´“a‡I/à«:èè®£J‰³³w„#1g¿¹òw½31z¹9#œ¦Ô\#Şèƒzãg’<ú›ë¯iDúûlUq`ŒñSÑ™FÀ5zú–„íÔñ¡<ja
Ãı.xÙşÍ„½ÿ• téÎU±ZG~‰Pp$/ğO¯ù»âŸèè^–¿¢zş<.XÿáÚé¬Èäzñ¤ú^x¿×ÓêôC¶t[Ia±¡ºÈƒUdÄuø´Èƒ‘F+
¿³µ¤.Vƒà†Ê2ÏrÌ«¼+ƒ˜vó^ZW·gÓ{Wúã‚„uÇ	ñÎÊn'ıó¸—°a'.aÓN\B‡¸„;q	›:;flß‰ƒ/ı±#¹Z¶H#u¿¨ë®î,‘Õ(B@İ«êH­»Z„)u÷‹0¯î“ul®;jU–J+Éûp8;Ç	ë¤´Î€'¸§Ô æ½¢»pÁç~Áq±q±iÁq°´	‡ÿv›pùBİ„k÷¶M8ÚIÛ„kÃi›pmØmĞ×öà*Ú\c5ÆXjFã‘#T,ò{váw?r\yå7µvGÚõ}E-^Pµã]^òö%Æï|$a=Kn¹ŠÄzúÜI=ß2W+=ÌÕj:ÚOØpn–0 fk•Nªu7[ãÙ²®›­ñä`LJè4[ãyÂ8[+s4[+3ÏÖˆÕÙZÙa¶®WÛl]!³5éÌÖu`d¶®ÙšJfëÊ2[Wæ‘é”°™Ì»U –J,)óµRó|­Ô4_+5›*Çc³„Çf	›Í:¤	%lHJØ8c'p˜±Û%ØŸóïˆ
Lçü]'T­ä˜&D†MõàœŸ°‚ª¾Í:æRsRÓœ]…‹Oælå?æìßâœıöÙgÓérÑY>$Y-Ùû’R?ËÃ]~QÂê`ùGÿî¬dÄ>tö$– Ñf*Ôwßı‚w+¬?xôöÕøLöá­åÂw–Ae­¼s¹N¾¦˜Pícôbì_/ „s[©Ó‚§Oÿ]z)¿òŞ¶³g+…l¹>^ğ"®î.W¿÷Æ‡»é½&´ „š¶F×+8¼vëR¾KK±KµH}øÂBËÃÊ
ãëqe…±t¿jòuóº
#éq]…qô¼®2S>bÂ¦u•qGë*ãæu•qd]eü°®2c>"i„„ÿ¤;²P0S>"!€,=©d‘R™B3•ydÙcò«8,•VşRVUÆŒéÓ	Ò§6¥OªÇôé„éÓ	;XV™)1aÃFhÂ`Åcúe•I…º[V½PË*£»eU½—êJë„jÕ”H†Mõô ‘°‚j¾Ó§;æR[2cú4W,R<YWÕ'TïŒCß£`ÆWŒC×Ë@,W÷¸¯àİ»Tş]O˜gå·‰‰-ğ¶ZJ†%›Ğ–…!L!tkJ‰"<	¶î¼)•›Š›Â÷€“cåVu{óXT~s˜¿²,YX_Yôp»õÉ-õ)ç¥,©=›*%9|Êçõ)ÓdO€?` ISdÈS&ÇA†ş®æ-Ñl,ƒqêNÆ¤ÜóŸ*ÁxâÿÿH±‹ä
endstream
endobj
23 0 obj
<</Filter /FlateDecode
/Length 4058>> stream
xœí\ÙÇ|ß¯ègjÕ} †z¶MÀ@[2Œ¥ Éÿ8³®Œê¹z–½+šØ¥(ÎÄtWfE•U³«±¹ü,Šşü°ÂÛäôšuÎiùüåá·şÜ¸¤ëU^~ÿ×Ã?ş´üJ¸[u Kca~G7ê…ÿüí§¥¾øı—‡²Ë/ÿ-ãÅl­áá~.ˆâKëºôí§‡?º%/Ÿ~¦Š†z±qI¿»|úòğg¥¬ÿËòé?>ÿôÏ… “¶€Û± q V ]CëØøzK€«ƒ~øt^q¯ıjtŠ ¹[!f#Do5?½b;{m·À…+.)j’[ÜtÌ×/Î
.Vv«İV]uC6ùÈ>áçm¿û¯ôç·­ÃøÇ-:ú•†'5Æ“›¢;ĞHâªve·aAõÜüƒöY1ên;­!7OY7¯]s¤¡ğÿtß)HcµúÅ;­–/íµViyä×c.1I£DBŸë¬®˜uY3²2ı:åìò™oN:êPFk´!ñ…9SŒTÈ…`£)´±£™oÖüi½×ó=/Œ6’•*–tÈÄ'3)W,¤\n6¬–íJR×ó•¤¾‹©aìéíÕç‡cóÈoVkµW2¼²†c,ûâ$8ä´š`²ó–~`*ŒÅéÎ9äLnb´vÓÉ$à!«rÈH6ƒÎoÀ*#ë9°cÍ¼õ¦f÷Ç¸š f PGe,Ğç(1"A·¡ªNkæÀ,0Æ¼5'Î½Ô¶F‘ÓdQ¥`’!MT"çŒY•Bµ]·£¤î,PÎÅ`õÛÛØşúñc\ÔÇOáà“CMqİ>pq˜µÄÂ BfĞ±|CË@´Jd~ø7ç„´Ôÿ8ô×%‹(¼f‚×Lğš	¾ÿLğ÷;ªƒVaÔ’—Ô@“›Sƒş$50¶MŒ)güœ\pÄ¡ÇÜÀ]<åÆè…›rƒ–ïÑ˜#3¸Éb„æF·¹¡`%7ÔW-7Ô7Sn¨z_ıT£GwÑñûT0DdÎLˆ¹Î!§°aÜí‚áŞí×óA’ØòSr à$90¶MŒ$‡äÙ«uÄäÀy¿Á™3vš’?Im“c¤„“£›äP ‘ø]Oõõ”ÆÅàA}Lp5N9Ôßí“‡YK0z f]À7Äá°Äë° Äö=eÂk.xÍ¯¹àûÎO-‚÷a$‡LÃNÉ!s¥²IŒm“c'kˆ¬2×¿rCä°	ycìd‘U:YC0¶]C0všİæ†‚•ÜP_µÜPßL¹¡Bà|c8pS=T¿S9C,v$ä‡›•ìmnfhæké€íÛsC1<æˆ 7Œ<Ğü‚e¾rq›
¶É;É„&'É¡`4¶Öv’
:'‡
õäPŞµäĞ^cr‹Å…Æ˜âk(\¼RÔÎ+³/Çyp‚$j„H	/d\Ql#+6”à¾£RxM¯Éà5|ïÉàï÷í|,¿>Ğ”V“5U–Z•=OW~Ø“?DŸc$.;J.WŒ¢’YËJ'ÂÂªcÈNæh$ú¡š•Mê=—Ê:q‰Ks^¼eg×!Ñ•ñÑ3ÆÂINd9WdŒÃ>S-‰0AÙº9¬^G¼–0r¤¬<È!Œ"Q«<id¬"J¹İ	Óä
,gÌ°ÁF¹»¡@İã»•JÂTFm’$Ó—2(E yˆó¦&¸®?ÁP¾äÂ>Q«fN˜
Ñ@€ÙzkBŒÂÄ~“bbj˜„øL÷¬W±ƒ²ËÅÁô³Pt”¥w¥XLQsG'Ù·)ÃÅè8°(rh(Ò8R :ŠøD4#!RÇğs†«qÃ+¡mçk`l†¹e‡‹”<’š+º•Rø$ÇÄ°:Ã¶E…ÍØxmPuC/5'˜bÃ"Qîn¨÷ø ÷ç¤Vº;–1›œÌ63Î&Ğ(Ó˜Ñû:bÓ<“sĞŠÃsøôæD¶§òx‹}o‚’>ƒa¸¿Ä‹:Ã² ¶x‹LïŒuïºc'—²¼Yêÿ8ırù4#² *ÛÑ´L$Ûà†´ãv~tmCÚ½ã}ú7ñN6=îh¯	 Âr=È0½ïçNEP„;Å	±ó†ş!	îıËı´cZ„iG¬7Âæ=ù$ä~jÁu½b#D_$$Eµªç*€LB—Uí¼¢­ÎkPÙòÓCĞ%|6êÇè»Ø0xS`FÈõ
Œ½$K‘ÊHMÅêUHz»g*ä£ír:à5PçÀG]`ô—&Å¹3J6E4¥U;ê{~ÊRçbM <ö»6z^)iRrÄÑC%jxZò\¨¯99ñç‹lßÈn¤—ÏØ¾İz9€z¬_<ÃË5?¤ÚµyŠ{ §t·Ø¥Ãs¦‹5¼oÎäõróìs¢t/µ´Bâ•ÒB…pª³Şb—/3 +ê°Ş6—jqíãÔÁ©·›Çğ»<C’Ç‘äÀªøÜˆˆÁÁ¥Tz“Ê\ı™ŠÃI•ÇÏMÈ1¹÷A|‹(Ãç	j*CiGòäü³óäüÄÓqÏWeÆóU„÷|¥Ê¯e.ıº9|şf¿eµ|¹çï®Ü³»Ö1BĞíÉ?`YáÈ¹'ûìsOv3÷ò Ÿ|ğÒü¹Œ÷¿Ä‘æ5&Z®¯!ÑÛÕuZOÀírØŸäDµxZÕö¢…i}_£¡D…oñØ½üƒÄª~Sm’xA×Rx7™k×¶¨á+c»zßdZ®Ş·hÂkr}İ¯+×¸‘+¦uëİ“ì05X-ÍŠ0µWµ†VôÒ47khXl°èÖlBØ¡ÓÑ®Qg¦+Áfu‰36ôıtÔk*İ$è
ˆ]V€±Í
0ô)Eô4Q1èÊ$ S*Ó@iî<h|œÁ\zĞi56inRFPŠ0Sú™SŸ•P[ZŸĞf%¬tŞ"tY¦ë ±Ã*w‹IDŠXõC‹æâ2Ã3uÚZ5¶4ÄÃÜY5Ø§FXq-'FoUçD:D›±¹ª‰—Cœš«t9ÃÜ]Õ™&ë7íU§şªÀSƒ†+“+ª%-V˜ôXa®Òd5Ğ¤xpˆMV=·!4Y	‹¥]	:FÓãBÛ¬Ærg MmVÂÈøÃÁÈ€°É:@ì±ÊÍİ bØmRf˜ÔF¿éÓ;õ¥?¬ÇJ¹y iãC 5ÌÔ‡ÆaıWMsçbWˆ¢?TlhÏ5İÄ=GG–B¼×š }O÷Àë|gş¹8j”®õxŞ~”Òë®xƒ´®åAê.®l_úßÑƒ|"7Ğ´±ÌM©uŞÕÉGØÓÆÆ52üé²ÿÚåñòr~ZS~íş‡*Ñ××V±9õÇ¶¨ïd«(»R%RC½®¿Æ5WªEñÜşíë´÷°‹ò¾¬éZ09ıè@"Òù¡ò|oùÜaiF K·ÖZŞ’+ú-·»l/·&µùtvÏkkŸÎ»[ôÄXWoƒÛhKÏÌÚêÅo™‚tM&•Ÿı=fúò2şP3ˆ zmA7ø™Paóô(‹ÀFõXtaèmúr}!xõ™Õ®;ÄlJ¢Í4oÍQYˆ;İµËhörÿáX£AÊÃªûLŒL†k†*˜C÷¼÷úW¾š±¾-³+^ªÜQn=!á¦IyëK©wÙzâ£vÏÜz›î«èãÂĞşÀà+/{Ïe j]˜íĞ‹ú…Boú-U	Ã”{YŒğèvfù¾š»å–ºÕIã]ÛÊ!««qß‚³Në+½ˆ{Õ‰²ÚÄÛ­Zç˜UTk[8€h´+K¤C°¤AÛ1?ÃÁs×p4•3Òo><ØÕm9“¬ípÁ¨òË$%ô]q0Í;Š8¸k—ÑÌåƒÇÍ¤o´ˆ;Öh&=õñà÷¬t-±|æèDIí‡p£iÒ6‚m„J¸íOıá4°uU>Ï-ğt# ¨i{ªØ‡íö®Ú©Øü­jÛ‹P9$©Ğ'X¬Fú¦u÷…âQì>ü W+oD×up|0u#Şz~[³¶¦0¹+Ã¶ı4Ç=?,™D#ëÄtoÃ½Ë‰|3vê¹<‰ìÁa]hİ™ä>NÒõöÌyÚmóÙª‘g¼ëÕ„huhäñŠDŞíşmo´z\”Øc d®÷ .èÚá–›†èe¥È~™Ã¸»C—Ñâ§¨ÒÉÉ”º“Ûº¦ŠÊ‘‚ü">WgéVmSÖò›ß¼m7KkB˜ö3†¿¼5ğz@<­F›¢¾)¡ÿîº5FJ	ñÉM–@B¼pGK’üe9şœŒÔ~ÏİJiÀ¹àoŞà>\Àİ“ì=bp¾ívã!ãCZ£×ÓãªŒ×p‚0Oámpœâœ¿Íç§ã„’Ñœ^ ¬nuÂŞ»—}RÙ¥÷²O*Ûù~l²]ÿ!Î€6p’ «Æì&¬Ò€Ça3V­t€ã
„Åµ<ıD>vC“ª_VŠ;
¯rö+Œ,æá¸BÃæã
Äã
r·˜@¤ˆ±P±ªh.Ö—ñÓã
Î—oÖÍÇŒ/ ôtX@M/u†³
†ÕÊ¿œ)[Ş¬T9¥Gô¬Œ…“
¦k;í¢(ìÉƒ!eï~Ü,[ü"C 2rl@Ô–ã2=9‡ĞyÀÃ	ƒ1<œà|Ğk¦,‡»´ÓáÂh‘¯6‡ût²ŞÁáW}šÃe0áÀÏgNr€pww€a«IaUPüdLğÔwş°ã	y>F{Ç_EôX=÷‚
ó±ÚvR§]×<ƒÙVRğ8oÕtvÁ‡¹)µ_8/Ç¼¹¯8v#ŸÎÌ®:*Ë9Ö~”¶êcUµ]¤ÃÂò™¨×”§6K¥üüe/ø¶Ç¾MkàCGÑzËöåH¦¡{L”ÑOvó–ú~@ëõ—LÛ+ÀC³{ÿK Gı½#LÌì!ÒŞé[ H½ı ûj½/ ZÛbl–ô>eo{õÕ{#Ó÷MèkN@ï¼»MäE¡%sËHEf[èÕ7¶}¶m½xƒÊàÒš²*p÷t£Í½gÔÄ».<Âj;äVÄåşkÏAò>EcúŠ{°øFBî+˜ÙC|¾Ïv±@¹ùEİ¨Á»4 jîõA{üƒV[ÿòZºÏôŞİáÛÆC§¶‚PaoslßS=/÷çÊ•ñóFıÎ¸ô”ï)ìiÍ91„íÿª|¾ó
endstream
endobj
25 0 obj
<</Filter /FlateDecode
/Length 3725>> stream
xœí\Ùn%·}¿_ÑÏ¦Í,  ÑâçÄòãØA 1`çÿTq­ŞÔlM_K3’î=M²Š§ŠÅ­®F¥!~ÿ}ÙÛ`ä _¾^~¿Ğse‚´0üñ¯Ë?ÿ2ü†¸¥Ã¢>µ0}‡å@ÿşñã^üñëå‡õğëc{ô ¥RÔÜ/T4½À¢Ÿ/?<˜†Ç_°¡¨¡´}ÊJ_/BÛ¿ÿ¹8|şøó€€
sÀÌ_-"¶Û2º6U
˜ÔèıãºâVÚQÉà™æÒÏ…¨™9×|YbŞ{©çÀF‰-EU0C@‚³7ÏÁ
=×n®®Ø‘¾Çd/øù\jÿÿı~‘Ò¾Ì ‰XeÑAí°æ¤z$‡!é«öI‚”aÄÊ»ŞªĞ¿Èì®#xl‰ÿÄzKÛPb´ƒ³Ö_Ók‹"‡'zmh°*°øÜi£eÂ´I˜¡J9aôğ…*é¥£ÖŒ^;Mpp$È8%qL+¥3†/€*K|êRİ@uôÚ£y¤¤“„© 	sbeEjYŸK¢ºD<©o|È¹x~õåâÀ—7OôfÔZšZ’ g…Öa`óÁÂ¨œÃT$Ìjüb]!Ì;¯xŸÀˆÃZÆa2¨À8$HpPÈV6W6ÚYÅÌ14Ÿaæ#,Û7UÊ†º´Ò Â­Õˆ9CO«üˆÕNMEEôH‚ôCëOÄ,Z™õ<bøRfŞGˆ†‘ÂĞ¸Œ¶-ëC-RíbŸˆ¢¾C³a‚ ¢ÉÒ;¢KéòúéÒ\£n.TÛl¾Æ…7¯ljVçm½i^Îû]‡C#¨šFd^œñ6›mÚ€m6lƒûËåßÂşS4(¯c AKa$ùÁà#ü)‚ÁOÖyğ
ÕÌÑÁ9\#óè€€šG‡ˆÍ¢CÄæÑA9‹šE‡ˆÍ£‚±dÑ!b8ô·a8Hí$:DÔ’àæ¢à_¥àßğà!æ|¹5ŠÜiph2Ç¯=aC„u™¦JNs•B68×lW£°Ñ^—ÃY·Ä†hv˜Ç†ˆÍbCÄæ±A5›Å†ˆ-b¢z"6‹Ó"¸Ilˆ¨ÑÖ²à°â»òkZáæA­Ñæk\|óÊ¦huŞÖŸæå¼çu84ŠÚ¨iT¶áÅ9o±Y§ØfÅ6¸,>‚ÁG0øÿïÁà§ŞóŒá·‹$@:7HíâÉÅW†}rÆtÈôTAC .œ…@–!—´^£ğí(~ˆœ€Ñõ’Á"áØY‚‘	i<•Åö¥E	Òq
õPt“äÛtÆBÌè©ª Ù¶ä¯ :Ë!ˆëu)`ª”ÒéD7â@P¢DQµ«0‘«g°°÷4Á<6îmĞC“ƒ š×à:!ˆÚã•©§Y„Í¨82^éiÉşahœ h#Ç…¹Õ
¿¬Z³Ğ¬6Q¦Y˜)Ş|uqéIä‹äcJĞI®‹OŒN>Ö°ONò±	hp€é@E@&RèĞ^rx\N£)ì³0"ÍG(˜†Ë'§q/…%iû‰#Ğâ@#-o( *©«‹˜<ÌAñ°„‘ƒyA˜Ie…¬á¾n*Fy7Œk¤<F9+ÕD{å:j'ıÌ oŒÄê,Ô=]ZmÄh¯O«É	‚6L'©Ñ»µiëSõG&ÀÒ¼ôÁ8”¢ƒJ2uªÜU•ª,óêÅ\NµÜT§je®?wœÚÓ…7?ë?šÅÈ®†ôƒB.-™¦HÛDÅƒe‰ÂÌähÙà4)ƒ¯'Õ¾?an…°¿qV1¿oÒokñùC*g ¿ñµUøÛ¤²âöù¶íCŸ\>é³×ni{¯“óø%m­@Ğ‡³·S‹ÈF¿ÉÅ­NDEÂP™ ›~GeCî¨KJ›»LtîD|fSHğ]‡Jû|çÂ´éSİi¼ï^O¹zÛŸ³Ge£æ‹±g<ˆWÀat™°Úcü‘o‚Lfô[êüÚ¥oq»Ó””8Má…5Ù§ÓïĞVQGĞˆc§î‘€ÁÙë!ç¢ã£”#<*.·Æ^°ÀE î–¤æšt)ëÇwè%o=XpV{Œ R¶@İÖeŒù^¹#AÊu>“Ü§(îŠSq£ŞÆw÷oºíZm8Ö=ÛÇ=M'MhŸé}ïúS•|“—C´,ºo‘-®CMÂã SÍ§ce^5PìPbiƒæè$pÂL‘àDÜÏy*P™Ô‡6e1T†‹âTÒ3‰å°iÅ%|kí^ÈÏôè—wê™—9{dYVmQ-êÎ§x_°W¤g>wúo¦Ô‘…|Ó¦OymşTssÿ;ÊLÙ¶,øbì¹Í¿Ê+¸líº‚ËÏLS5^İ—2ısp“Ü§¨W*¯8PãÊ<nöDÎ›Q€Æğ‡–Ït/’Š¯Ü&ÀŒFĞ9k¨K.F©…Øù1«Î[ßv/ÄšĞfú«äˆòCÆå4%P(a5'K5Zë4¬©ÂÉ§qÀ¾[‡S.rQpHqMA–ùÂò^úİ†R6±½‘à5¼¼¡-Jğ¨±x°LÕœÊ‹ñ%ìSau–`,JĞ²=PùnÁ:Õ@îV +Ã~¯·•İR©-]>ZjeÀƒìAõUŒ7¯gìÛÜ» °ÛÖ¯%4zå7U|Î’!hğ¡ey›û,p8Xï:<Ğeÿğ._ç~cG@á6ÀY~`ƒ»‚÷O§*»\]uéâeVJplHT/3h ïÌÒ¤{ J­y™E›Z9ïÂ²Jî„G÷ÀNk»dC ãÎv´´©U±„P˜¥%´ÀA.=MiÀ•Úì`öt5O9¾Ëş¤Q¶Wf¿ß/½Ùó×`}‹Ã:bõÜÚ}m·{~¸©9çCiSF‹~l‚=‹[ `´æ¢7{±ÕÔ¦Go+[âš2ø@­D#İ0kñ‹d fë§ËÖUßÁ	è †Ö¸Âe8{°iØIÏ?(E€	L«›¢.Hûm÷{{`nU¹Íá`Õ?gç¤´ŒÅà0Z‚±a¿ãÇe·Ó¦É7µÚ¾­î¦¿mZŠ(0ôø(Ø¦¤#îÍjÜoÈØîàË½DĞqœ	ßĞó×ÿu©gç2JÏãA*¬¸ã\ÑtÂwxÉfÏ×cŒ¸­½pB2	í^
 A£¸fÀõH¹&°|<U®/ò¼('tæu—Î¿â9˜İPŞ·30y·‚‰|gEGÒ7y'¿q¶Fe÷ÎÔd¹Œ«KÕ—dj\Åz–z(qJ\¤"hGixâ!BztŞÁæAÑnËLÒ¥M+YÖ!b"*Å2ç
Äs+Ès+È2öª–ÜÇ´ay€Uo–0Xº7–É†•°§)èF´G`É†ˆáÎÅkkˆXÀN5I5ÔÎˆ}Ã±LÃˆ9ex¢aÆ¦É†ä	‡­v3A“ÒŒÅõifmš7ë·®øÎ2Ù%d·b9ca%ÛP‰äÇrÂ˜éc>{MXô¡k“3sKj[8ÿK|ÌRàÒ°$ÃğÃñÃR­¥çµ¶[&W¢%ı5u[v`íUK"+™…•'Z¨”¸ßŸ*BCÆ¼ÖLÄÜ((5›ç"Š³6–¥"F”Ï*LØ4©°`<§Õ-¼3Õ@eª)™ÚÌ7j÷–şò½ò	½*·–%¾Ö[±{Qs#¦D»ÿÈGêtÛN+iI*¤”¶¤_§›å¨§ñ/tš6$Fİä™à>ä[%uô}3Gã”’”Á¤õ¶{ãPuÃ¦±œÂ¸A8/£¥O% ÅQxüŒİ|†Àv‰ÔtLSî„Ñî$›ÇºuõÎ ¬Ş¯9F˜¹:aUÇHĞ_hÈ¹4§×n}›¤>ò‚9BJÄE³SMöÂú,·ub•5cNSlúOïâÎ 5ø8ó3]”¡Ï¤ô¡•¹•ÍsšŞËÛÅ3èô°”ÔG¨:tKL¹Ü¬Ù‘³Üî—ÌAâş„9ˆÍ
MKaËÅ±˜ÜúŸ31ÖÍ$ùò¾í¡^<Éìİ8\ÿ£çÒ{ŒèÄ{0bÕ²Ñ5i´-Æ\£°fò—-(›Š¸3”mìiNaŒ§Ï qõÏòˆ%Éß¡œ¢ÍäŒîüç¾§é²qFÄnönóŒÕ”üÌéëqiïÁ¥«–Õ¥y¾[=•5óin©ãÇL1fL´8è™Ï­ïNáÊÄOì&·™p³GEZÕÂ‡Õ°"iÏA­	#ê2³e—ƒBxZµ<=æ–³x{U‡7J!ësø^ÎŸwú½ˆæìèÒ
–IÚß¿É³è@$î3–’VRän-×ß3ü-ØòÂ…I`şvê@—Ú­vhÇpÒ˜ü'y­‘zñ‰Ã78Ò›–kSÑÖ^sOós¦ª@€)º‡v/©^²™Ş]Pòº=¥¯Ë'¬}>Qµ\õ‰Ùfùu|ÁÓŸ¯ˆŸ`Úí¼g»K ¯Ë¼Â5êqè¨àÈQÇµu›6¯q¬Ë¤uPå…TG¨úÇºLÇ+ë²ÖûÓò aßåX—éXuıUu™¤>ò¬8BŞ[;Öeú_íX—Éè£ÔÁ™”¾Ö±.ÓûÊÇºLR¡áÈGB=e¡¼ùõ	Óò•u¹D¶æˆ¾—‡N77›Ç¼k,˜z'õV½ƒÍÓò=õrõ¯å%]g&ŒÉkÕrsrÆQƒ—¦İ´zÔÀZîş¦ ŸÖëÎ¼‡áPµüÇÄ\‹oôêÍõã™§Jí@w¿ÓAŒb.lwë!_oLÈíñÛ ßƒß}­0şıNy¯®2öB]ıDóD8û?ˆÎ
endstream
endobj
27 0 obj
<</Filter /FlateDecode
/Length 4534>> stream
xœí]ÛÉq}Ÿ¯èg[Êû0;K=Û"àX[2® ÉÿøDŞ"²jrºŠlî’«áŠD÷©ÊÌ¸gdTti36—?7…ÿ~ØÄ×äô–uÎéöó/Oÿx¢ëÆ%u³^åÛ?ÿçé¿şíöwànÓ·Æ:ÃüõşûÏ?İê‡şõé²·¿ş_™/f{ÓÚšî/Qtkı€[ß|úÃwË·ÁD…B}³q‹I3ööñ—§WÊú?Ş>şí)àúÇÿ¾0i¸=`UÒz­`àë< W'ıéãË„{í7£S”ë¸_ÄìÑ{Êwì¹×v,îXj’»%¸Ñøşõ›³7+»§nO®º³6lO¬}Ï æ?ğß?´[ ?î¦I°ÆÃ@0©İÈ`h‰úIûÁkİf1ú®¹xÊºÙë–#¦’ÿbÜÄFm£“¾ıR?‡ ËÿDŸy["À€¢p=XguÅ¬Ëš°•é÷)go?Óà¤£e6½E,İ˜3¼£B.øt3N†™ÓÕPÇ–1šnŒ6B?KÂ1e1“rÅBÊ²|lwzZ¸Pïbj™xûôóSÈ±ùD_6kµw¼²yÌV±ìCˆcİ\æI›	&;A!aŞâà„°bË!çn­a:™$DHU9d)kŞ¥ÊsBy„5íÖAMíŸøn n<kÁ‚£¹ÆòËŞ‡6U¡ t¼1;óĞ±`¼`ø¨›Øªˆ€ÚâÁEY0Ì­…ĞfUªKwõÔY_ÕSuX±œV¿±ıó§'6¾™-ˆ'e[“Ë³U2¡Ãx™¶rÉùp{‹’İKÊœ‘µÃËZdçşùé),¤[ıEƒş¹è
‘ä-¼ƒ·`ğ/ş|!GhyF "©jÑ!z¥§è @‘Ep(u)Hê	SÎø):DLúÄÑ¡@»èP°}t ˜hLÑ¡`ğ½,5FXóR¡[B‹?(…‡ö©†‡öE†‡	ûÓ	K›$
Û¬/<Òa·2ş)¤-<yèEx|W_‹¤ŞHïSx p„íÃa‡ğ)ŞíÂaûğ@Ø1<D
xJËè@†(¥Ì	;FBáÈZF‡‚å\ƒ}éÁ¡~‚C¿WØÏ˜RXšX\Øä “M·3#L\pÍ¾0Ä#\fˆQ8—·pÃ¡á­CƒìÙWò„·Hğ	Ş"Áï9|n’µJ#4$p>…†”üşQ°İ¢`û#@·;Bh;„†„,lw„(ØîQ°Ã¢ ó¢B%2¤–P³I-£fU!a{}6a¤bYaÎƒ@aõƒá‚cáIC6ìpC‚Â3«¨÷a(EøúP^)…ŠÚed €$ Ed(Ø.2–ªed ˜÷‘¡`»ÈP°O‘!k­DT ¯˜VE!ğ‚Yç¨PĞİé¡b-*”/-*´Ï2*Œ{ÙtxJ62¹8›#“9¬¶0Â–-¹.ÀbaOañ±KI9³ó±FØIYsìĞrƒ· ğ ŞÀï1 üùìÓÛßŸ4.²©NCY¡t?ĞH$DŸìĞ¬tª¨Ş²K>¾oÚàOAí†”Ù7º˜*Ø-¸ÛlÊNâğX¥¢ÄZ
#qˆzö€‰lH¡bCHŸ9l^Ç0
ãÉÊO« …¤!îMÆ*R»9 ªam­Îí„VÁ”	8d% 66ÜxºJ¦rĞÔ(r•ÍF~#>Æ3ÚØÌkâ¨âaUá°Xy+€çfe	"X¯L-[ su°2?2+£èQ.y€Í¶šC?è~ÚÖ\p*Dº¤³+(ñ•å½aËÚøbVtB
\7,M>B0èQÙÃ±5åÕ&Õ›é±#ÛĞ–­JÕ‡y$ò‡e5”¬+"8$åæLt›'yL«™6ˆ%ïI3ÁÍk33bb&®ıÌtC#Ë§LĞ@ÙİÆ&Úû:m‰ijáj™°Ñß¨/'îÎiã³˜W—‰ÓÒ³Û"–º›ˆzdËìí­©›Ù…G³ˆãæVÿ¡(K™ÑŒğù¨<YÆ©Î*Ÿ-;*pnª’£·|7OÛèÀ]å¶{SÂqò  í@v ÖĞiÌ‚úÕÌ´UÏóª‰öt5äÚG1}_Ï¯¡äÚQ!WğuêGìøğ n´·/°3õ¼0(à0~¤ÑŞVn{3;¼8Ïƒd@½ÇwÑ¹vÍÕïtÍ¥†™6FUìa‚7†â¾¤rş™Ws Æ)-øÊ¥Pyrr¶h)rÀ"¡®\V=)Sâ¨Œëœ5½”ûÍ‚ëOXKğq3ÍX¬¿d,Ş}Æ2¨|ÑX>°h]#ITø;
¿¶‘HnO’¤÷r´_·­HîKô|rÖ¬ºE‹¦f6ìÔØ…³MÜûäj+í×A#iá^µÖx¦‘àh‹4pßmå¶äUN†ûİ|¨Íká3¡ï¯r}._éJ0q£|» •ÏQĞëªúåj¤Ñ¢×Nwá™ål5F¼ëW4²ïYfŒNÎ–;È†2Şî®_{ı#«¤²à&{ó·%åúØ•[%!$Ñï%Esô~/)¿!;Ë†µ£´$t9#ûß‰
”ZO§ €gğ|”.‹“BØ‹)n
DÑ¹âîÚ½ıçh›³lØ¶†qP¸ßš¿ÔO#ÄT.®¦ªÂ¸€©ÌÁÂmÊƒjw‚óÁdÀ¹°Âç…DÆVQzxb„O/ëo-Û•Â—òÜå3•òı%ÜO+.Vì­õºÈj¡>—bIÈïšÈõÅ—œ«÷-èy7)³7äEaÒŸ°Û•é¬Ô4	g—¹H–ÙkÍ¶¶ğ-<Y-Ãçj®%¹nA•!öæ$ÜOú¥÷%2$ëq»º%ÄuŸÕ—@’•©®x—Z×·¦W#•Ü¹Px†
ÒF’Õ’ÁeÄ½ÌàäıY¬1Å—{Ü6òS›*+ìïr;“î‹\*êÔ(ù˜Iú„>–:_îgiµøRºCˆ;ºî7H·f»ZFŒË÷æ³òæ¥H–‹?’ÁaÌ(dğ'ôqÙ¿7º¬óşÓ—ÃˆëÚùŒöÓ ´Š{ª^O¤cn‰ô$§ S0–;ÿÒr®ç²«<s¹Ÿ-2ºeö4-§ºœñ¬Ù[&gR…iÀ*…_Çô»¹ıùäp•.Ÿ
r¦uº|]×Óå•?C±×mä²Ô×ÙıåSÛÊÖ¢ZùåÕƒÓzX¦ËÜpéË­Aî–1Ÿˆ`'³~™Ä¯ãöŠu;ÑyÒx¨Í/„*Kz5‹ÿ”…-ùXŠw­©UFw.K9%÷Émb²_ ôÏHÃV	ègL%=0‹½z-ÄË9ùT•JGÅ~ÅÄ:U¿n#KÅ^?>./ı‘,MaJNmÙ‹cÿœ’ÿ2¹>U‹W¯&¦Né91ııVÊÚ!ÄHNÇ°ÜA,N5±˜ç&vMuï£äM;—B8ü˜>oÁúàUØk0o6+ãÓ!f`=:¦q38*öòBhëî˜JÀŸ3Ì'*P¸ Mñ ^jŒ£¾·ûÔ¥Fp[íŠoß÷Mí‚|6áú‘JÛ”õ±èç6•¼MépŒ>ŒX*c¹öŠ‹f¢Gq,™XÚÁŠ»åLW5±”Æb¢¥æ.›Ùu•JœL¯ßµÎûÒÁ’éÉn$ØBBÊ…ÛR}¸{ Çóİ—]Lİ£éAì3yD{ ëÛƒÙù±³oOñõó5•À¹t¦6UööÁ±}j<è•ÇCàwmí¬ø¡»«Í*åşxü9ı”˜8—¸²£ScG›*¹Í§¼è§h±Yª˜D‡@½%"§nJ¢w¸¦E3%¢‹²|•M”=”àîC1)÷)NpK£ –{[Xø—}“CPŸ&PëMÓ®ÀË 3p'GÊµ}ĞÔo0 :'ŒË¢s²asûä e%f±ó*¬!I+sÎJgş^°˜c%’[×ŒI€ÚêjL3	FŠK¢‹`€{jgD#@–Üe%½O(“D%@¨Ä0: $Û'(»'yğh=”‹Œ.Å™ÑĞ(i’ËÑ!ÙÅ!»&‡Üdß$@!Ø(ú&áj´VR„ì}SÔo.û&)½ƒ8/ú&Aíµ¡|#&N–Z]œ,\;”ÀK°º$1¬Y&[ÚJgïh?¿Yç¤¿ÓH7ö™Ïëo‚K;E^+¢€Ş+ûÆ;Ş#J¬ÿQ|§ı µAQèë]ceßñ/{Hk‘*câ¼g•½D·ë}IbïjIe_J¼ï<¤}
;72×½îµ3¹àzÓ•¿Öëæ_è~Ú=dèŠÚCŠÆˆ=ö
4mì/·R½­IŞµİÜÛYª÷šÓì‡H×`ƒ«²eúNI)›_ÉêÇB²zû¡^ÿ~< ©-ùlÓ$»€ ºàÅbï¹t»íGÙ‘”>7Sí"s5!.bËUdF=¢?ÛS/ -ı¬LÆC¬ä!mŸØ£Zcª î”L]~M¦AîNb®3ò8¹½•KW3“2Zj¿Á©~s{N‰>¤¯üCŠûàÿ¬¦nä.ø»edUlª¢l*yÑ´İ±ÇXµâ{¦Şc³'¿+ş.—]Õı¾b¥‰78÷,®¹;ÚHS¦“”ŞFÕ1Î¿ÍÆ&[ü±)!°Ğ½šÏã½Y½ok}Gî×8Éì‘©Ô(Æ”Ÿct¼ò7½L†¢pô¾LljC›ú÷‹có»GÄ‡¨kÖ#h?%qç¾•ÈÌ¤T¬¿nt¾#!º‚¸Sbœ{>î¯ß‡¿Ì<²Ì.VÂ¾è¯<H¦»¾é¥tL•Åæ^
>ø—Ü^mÖôÃËxxfaMQ¥pxv{¬ù^­Œ/‹ÁKZUååóo¥Ü<1±*7g0Îz;ßıç&×^<¶¢†O>´¢Õ7XÑTu#?–mcGõVT7­‚Óàh%*ÚÀÂ†UdAÛPöŸ½·S=¨¥÷bÉrvÁJáB­¿à%]+~À=j¿%â±†(&jDÕyĞ-ªÓƒ¿	ëÕ[‡È>Í`¦_AÉ·*^ZSj’`¼¶úc§((¥ÚF±´Ô$»$6·(‹Û<šuÀ«°¶$=¬W¦œõÏ¾`=ÇêvĞM?²º=ö‡O3¨á¢ô“ûQ5‹!XÉâ6°¸£ kÛ =®C¿\}%L”µËWYÒ.€,g×£,æuãiñQadJ´`g”¬y_uì!!YÇè·å‰:60Ø	¬@ĞÊëH¼uS;h­7__ĞxdúKU» 
6W±$‹Øbd—6Ï?´22ô'H–ÑY;ZÉoVÃÎãg–_¹šÇı«Ö°….Ô°Å¨3	u¶ÇªÇÊÙ§oº†-è;%¥%«½Õ°'iœ­a‹!µçvöÜ«<2•/è²™ªDİpZŞ*óâ‘ã:”ë„Ş§rZ×c¯\¹yŞq½—ÖZ%«—àöz}õUé¾Ÿ$zw8‹iõâƒÌ²ğóˆÂ˜¶¡9¤à„c'e_]Å£[,Ô¹¯x÷&Móß}¤…ãè¬SâòWı%Í7Pvd|ƒ|$u§dšõ7RX¤|Ÿ|$gDOo8|ıİ6§Íü®–“)//zF“?‡Æ•ÙÜ¥3÷ÿG.±ò9B]z”0w/ÈysÅI‹¡0±çx¯§‹çy+U«ÔæéYt{ùÏü
³k¼ß÷n¾eSËÒ·ç„“Â…3Ò /aÆD¤œ&i+©;Åğ÷^wõA'ƒ×BÄÂMê„3%ç7÷ŞÓuÉı§­åKßØi‚Jqü£_ßhz±˜ù„UÏâÄ¨é}Wÿ3ØıÔ
endstream
endobj
29 0 obj
<</Filter /FlateDecode
/Length 3607>> stream
xœí\Û¹}×Wôs ÷òNğh4ûœì ù ovƒÀ^`7ÿ¤Š×bK-Q65Y[3Ru³.§.,²[½*ñgøïİÊ>#W aùğéğû+Ä¢­€åşù—å7¤›U:<Õ'ı'(ú÷—ôæ_?ü¨—_ÿùyĞ‹”J»_"EĞ©éúôzøáÅ,°¼ş‚Œ¢†rÑ~õA*»(½¼~:üUmÿ¶¼şçàğøëÏTØÌ–à#ÁW‚‘öyH	ºl•`ÓÓëeÅ­´«’Á3Í¥ß
Q!r«ùù[ë¥ŞvÎØST³8ëx¼~2v²Ğ[í¶êŠ²1ö˜ì3|Êè¿ã¿ßRºÕÑY¤·+ ¯²¦
ávÈ©…ª^)lHPzÇ¿SÖXs´_Z…a@æ¨]Á#+şÇ‘‡«]@Š°|Jï}nùHïå\ êìš€Ç6Z&š6 ‰æ@¨r0zù@ƒƒôÒEnfõÚi: s$‘Œ³aQS[)iøh°Ä£.Õ4FÒ‰^{ôR¢‰à(EÂT€Ds1ÆÁŠÔ²>ŸiI°"í™Dß}88ğåÃGú°j-M=“Î
‘À:ç;±ÂªœÃ$šÕøÃ!šwŞ»Îb€A¢¤aØM‚DÒ¨•ÍƒvV1§D:Ï0ç-{7ÊnÿxhgÈ"×Hs“i`­Ì¬¢¢HAú¥Ùi}Ì,4Î¸%Œ@J±4é#²iZø4°x&R¶É[É}‰†IKîblèòşã¡E=·…NcÙ‚ŒoáØÔ¬Qi‘Í­­)Ğ`i™Òàk)ÅqnÉ×<Ò’´y®%ô‡Ã¿©„%ı§
PŞÇâşÁêñ½ |/ ßÀ7[ ~º£ÈıDb`ƒ.”‚®" !|¬ D’6\L{¢a”v‰Ø+kkZAˆ$ã/‘†o/HtÛ‚i›‚ig!RQ]Ë*B¢QEÈïREÈxEÈ$w•‹P&˜ÅrU‘…{5…%³™¥PE§eZÅ¥d›ånõ
Ëñâ¼\È¹µ ×»‚€„³‚@´mA bĞK%nSˆ¶-DÃ·›‚`©Æ	Å‹‘µãM‹°)
Dİ…H+E>”¢ŞwE¡œËÂ§²dÆ„³¬j¶È-Æ°gV·T¨ğ°Œ©0²Ôbx³$¬a¹Z=ØòúÎà{ø^¾×o·ütß¦ÅòÛ-ZHìhğ·Z-Zó‰ßp+mÊ’…lˆŒ®ò:„…ˆ dˆDŒ&ãÀ!Ñ¬Rá±§B—jBDÆ–­&²\C @‘òÈzKD…zô1&i‰¤å= ¼€¨12¹0k¥wœQG–C"öeØœõŠ)-¨G”H”QX5·#h"ƒL®0~ì‰èmåãø,	ivÅĞòL)Bw%e²5ëÔ°JDci†Fš·2Î˜dšŠHü*‘üWn£›Kš”æ=®OstÓ¼ED³ğBDQhR°)A»·Ô>+tG¶F|‚¬ÁÖ‘q¦Óšƒ9HÌ$:ÄÖYJ ÔQ*4ñqE?§	{hO	„TlÚ…§¶SÒª@gzŸ€G¢.¡–ˆ:‡šƒjL¡æ±xa:Êc‚#8\–òn5Š"­Ó
!Z••ª³@y cmgk&zKdÉÃ‡Æ@‘VCsi’†:SkJ!ñÅ:ŸXfõ‘jWpÕN¤aØxX!É4+d¯QŸ
4]üÁ„TÏuêT'3ÅYäTÏ£©Ú;±È_-éÕ`jŸzJ[KÅídÊÓm(ÚË6›ıéÓëaµ'Q,ãÆão‘÷–V®Aì°Eu3[G¬…0G!¬¤+ø
øş)Ñ-·H³–ó_&§—ÂÏN<âqy~®}Nç–1&¦sÚÿ€;&b³³£± qKûíû`B¹À•eFâ)B‘ÒD3ªYÃ˜úT‡ëìÕRS‚1ƒ‚ãÚzKÜ7'ÕWe¹zÒOÀ	gïU	-5çLÎÇX)L6f[RèOŒmS%ÎÁ±] 8÷1|©'®×ke%ÿÔ(WõòõÁiÌ8?OSœ<h!VÆJl`ïX¤ç<!_Gf#§NÚˆÁéÁ`œØ6%İ´±µüÛ<Ğy/ìÜy³ø‹ñ¸Nt¦ÛüWd}<§OpÑ˜€6VCc(-LJ@)w€¯—’qEOôh¼ÿ û|%ö´Ï×ó™¶â}šÙÅûÑíp¹„"B'á8İ.è6<.¾"à«¶|Œãc‹ë9NÀî5M!MÖˆ46ÀÅymäÔ˜Ç¹+Guş;d<©G‹ÕMıƒ^Ä·]ûâ•#ÿ3$FRĞh;3· qúáÌ‰]+õ¦éÜº‡+lG(é˜„±º'.è6º5_èUÓÇÕ<š>tl«˜´!€«®k#gV=ãõ¦¬ÔT~f%áÔ—:VR½”	®”¥ã•–í%Ë-%%—"úlxş¾éy±RTJYÜP¢[Å×ƒb[)“ÇM)+ºQi”#±j¤3}Ê>×)®‹*ÅÄ8î}¦‡Ã)›ıÒLfö¡Şã3*±¡t¡Ìò‘¢`åCVè¸K!²K_,D»Y²Î3–u]É‚Ç|V“^ÒE‰º	Fc¨n^Åá‹khk§›æTJÔÆÊÒlTagD ¥*2É/_h6î²=±p„VTŠg"š/íÂ¢ÌJLƒcöeöcôeF·Ö”[óˆÅîéœóPPºófûÚéÁ_á/ô˜²ÕE¨¸¥ü¯ó	Ñt¦Ípôá\ziOJ`ÄYÑÜßæT­ïHñ±µƒµ«Cµu‡Ùˆ/poãË&ˆl¾Úóƒ”q­JîÛ‰Û[É«t×$“p4¶Aú ½4]}Oku¦×”šª l3Î7Wå›ó‡Âjûõ†9]€3g—[CÈ›Å2ãó5pô€um[h£kêâÍÚ…í\¢Šú “7em,õêlŠ;s¾J¸š«—–Fë§Dç»ÏKiuËâªF,æl_¢vÄeo­Íø^D,ÃeÍ6%Ú~ÓnÓ ®`Z‚ .ãy¸:9Öˆª
'mšËß)8ñJîZx!¯átbö¬M¿6ÎÂ0òäü¦å›´¶lÁÏ$Á©îZlx=ıŠ@9ÿ%7©O9²G›T¶ÛÔ´3Æ~Î.û^*våc1Ìßøeƒ´ïÓ43È_o£çåÌ4ïÅEYÚ mÚOá=t;àåuk†.k~—ŒêÖM|7¼¬ìüæxŞúŠ3º<ç[·ÊlÒLÔm-ñİ÷R62­îÀgê"à˜í²…>7AÚm4Ò¼ì™î[Œu0–%,›°ŸsœSÊvÔæÂB<‡íÖuP—í«“èvãº{vÊÖ†`ó'şÕÈOÑë˜^eç/ò³"/Ø'Tjgp±q]ÅPr’¾¹7Ş9äK¸LÚåV³v¶yÇDŒÔéE7f9{óN¨ùÈU™¢Üb6¹&b9{WSŠíÁÛ#WeFäì#k"Æ‘ówµ©nŞ»4¹*3^“z~rMÄ8rpWG
ò¼#Ğ€‚Ï˜ãv§ÿSv Ì|éîó¦ï[Í}uLiHùfŸó•°bãÈ¼Éàÿ‚ùÎ›5/+™†âÀÜêÎ{çÌ»Ãr©I—0ëUC_Bpq®±Ë#\ç{÷ØÈ!İ­%ÁCQ¬Ò¥£×l+û»QtwíiC¸¾§ı`«tIWu¦ÔtbpŸ‹b¸g—ÊÚÿE&.ùÈY7è³Ù‘‰ù˜!Õ#îç zŒÅfv,3œÈ+ ¶Õq×L¹»Pr‹LÙûááèŞ¼³e2ÕÙrwqêBeÆíïT8:sæv /ú·öÊè¦vŸÀİÓ ƒ·ômDÏˆ¶ßÎT™å.à1QÑ.a2YS¢"~C Ç[¸kí¡ŒÍóYm~ä£Ëø—áÜ„ìÒ”ö#?6OR
Ğ¡=e-_ã£¯	:Ô
ÚSñò#î¤ZµÃ~P=×Í¬Á
ª=YÏ&_ °@_‚¿-e——±{âm:V‰Ï¨:$ XÍ¬L_p±+Ö/ğm„IOş“ôåò VµŠÆÖH ¯‡×1ÇË¼ò3eXEÀ˜.†ìyuAW…2ášbFxÆ&›m14xŒ†ÙôS FÏFÇo…(µµÚã¤†"´İíW¡0Àlm>g•olÒT Ø­[1Ş´à"ö¬È(yLWÊD¹Ãs@öe¤0¤/…£u†ç2vY}]Ş(!¨Vœnân[~¯ì²áXmÀ13äeº9e/J¶†(îÃŠ Ôm»ïÇv?vö´oSôLŠ‹1…£¦Åm–oŸcŠrìçCKL­Jµ€ÕÖ·#].Ó.:Ê0!,áPº	·mßeÕÁÂÙ¬unÈ.&oá|:¹ ¼Ï#ªÂxdOß]^û)µ›„<m5ìÄÜX]X›À,Ô;²oà.¼{yT•áÙ¶&Dl=ê=HÆ„Á¾?Y:=bâ]êç¬¯VA¹%äÜÄ}…wwÏë»UãşlÛo}vÕ·û=UoKÔ%ÖÅÊÇ»Ùc‰ë1FôeU½eÆ=÷Aß÷ìÍ{“¹)—½
·çøû[±-‘ş¾Ñ˜3
endstream
endobj
31 0 obj
<</Filter /FlateDecode
/Length 4137>> stream
xœíÙäÆí}¾BÏ,×} A ïåçÄä6q‚`×€ÿBÖE–Ô‡z›ZÉÌz<jT¼Y,V‰³›Ë×¢àßw+û˜œ^³Î9-Ÿ¾¼üú‚¿7.©Åz•—ßşşò×?,¿ Ü­:À­±0‚õ‚ÿşòãR/~ûÇË÷?Úåÿ.ãÅl­Áá~.…·Ö¸õÍÇ—ï?¸%/†
…z±qI¿»|üòòG¥¬ÿÓòñ_/~ÿño LÚÜ €U®¡uØğõ‘< ®úşãeÂ½ö«Ñ)2ÊuÜ"1$zKùş-÷ÚnWî¸F¨IzI àFã‚;OƒRéie·änéW·‡³Êpbv{ÓŸş3üûõEë°ür‹~…2ÈÛx°[ò0Ù®]ÑQ½bgRx¿½oÅì>eİÌxÍ†âÿ‡çö@Ã¨Õ/Ù'»|i×Æäå3^;tÂ„€¥¬³º‚¬Ka!+ÓoSÎ,ŸğÙ¤£e0ğëŞ˜3øL¹à`<®nŒm0¸pø°†ß†úlÀg4Şm%UXÒ c ™5)WXH bxØ YÙÇv'‹‚Gê]L†–ß®>½„û‡Ïøaµ@Å¸Á+›ÙpË>„8!9­&˜ì‰ó¾+‹!Æ0ñr+1Ú1é L'“˜dU™Îo˜V
”çHyjÊ­Ï4­~a7  6(Â‚Ëv„tª’é“è¸0næAÇœo„ÁehRkò	¥ŞØ‰ :p‘#ÌªTÊA¨³¾*§i°À`)ÆÅ>l¿şüÂì¢ßËÌgÉ!g&9È$ËíÌ0g\“+ñ0bd®ÅäÍœph†ùêĞ ùõ§—bDHKıA¿.1ôAä5¼Æ×8ğ¿~z 3hÙE@+d¼G†`7‘!X4®È#‚¬‹ùÛE†€¹´–E¹à§È€0¸#C°èN‰ÁĞS`@Ø>0 t
¬†zÕCı0†
b¶7†cVÊ3{$2³ïœ0ÿ`3O²!‡dI¢f.<tÂ\½«®…TmUé<0È62T H‡†
ÜÆ€fµ¸‰¸Ö˜P³øPaB-}ZçQÁ›Ñ€-FÔO-Hô<JĞídLl\²»‰2QFï°dâ‹L~Áp&-r"&Wr·Iä™L]äÁL±ÌßÈ^Äk€xÿâ§ÇŠË// é¸	 D`r5ïüÂÀıqÌJ;Ô-Ñ®&À  –•N Ók^°lé’6ğµD /oQC35|ƒæVÀš€º„Şå#hŒÉ<:9ÄM0Œ’µŒÆ8 ¨è¬#¿``XYy†`y5Zå‰"cÓ}¢` [xˆGÒ(O7(İç²‰Ì0ió*[F”FÙ„¨M¨œ6úuOFÛ|,®^o"éÀ\åÜåÇÀ¨¼.j6é„p‘ö&²HÑŒ²ÆìE›BóDƒ3
KÂ¡üÒ‡apƒÛª,\2%´xPAÒJ"Ä½˜,.‚!kƒá-BtE¿G'‹(>J!AlYƒ‹™d¸WhÛ¥5`¨°*ÚEk‹D’š½*ÂzÃñ€İ¬Î b=&&d×pÂ\êS™ ÊÃJRûüÂ×>­É©¸0<:€%zœYE:˜5%•MxĞáa”ÂQçR—Šg(¶6Ò€•.’.4b(„á"ÍMt‘’Ür:³—¬©›ÚõÜ«Êõ1»š!´+Eit7•¥®ë³š«Üï?¾¬Y!åº—1}î[ûá<¨ +ÔlTk”òI\‚Ÿ~:øğı¾ßáçõ ?W0ëRŞãDC²´gÅ Õ¹¶õ3Ì¿Ÿ%|ÉÆY	º
Ş¿«‚÷Y€ùÏÓ´c•	L<ØIî÷L(	pc•Ûs#¤kJğÔVÜš,dæ9¤ktKÑ{‡ÅÚ¦´'Õ50¾œ½`{¾xs–B›’¸n¤D>\sô§c­ÙÈú¦P…‡ŸîüŒÍõ£ K>]0„=OWÆïDı¼aƒ%aò…ÃßşÃc÷ÿ^c?>–„ªaùëø!—î]eÀd|R Jaş½ Ÿ°é3ı‰„ó„‚ĞH'·`"ãEœÙĞæã>´ùÙkÁ¹ÙÀ8BÜI÷Y”š­³òª*³uó©ÏÒì/ç3´®Sz3Ã<9»á*ªæ4œ—gƒ¹Ñ}‚ösg![µ¦+ôæ Ğ‡õ>XvÁóe[k¼“±Ld31íÌWíT˜EüVBŞ¯ŞŞŒiÕ	Ñ®$UÚodr™ògU
ZµÚ˜ŒöùŠ‹¯ùÊyùÊî±|%„Só•1¼VÂùÊy„OùÊ@#¯Ü`@6_ˆ°åb]jˆ:%gÉ;ä§§+²šâéÊ†Át…h¾–®H«xºÂxLWdİœ§+—èKWˆì$˜®ÉÒéÊgKWd]ˆ§+÷(—LWH«Ï'¡0\ò¯éÊyéJò¤+N¹3Ó6ü;ÙtåDÂyºBh¤Ó•[1bÔ˜¦\&DÓr–tF}å›ñÈvC„uÅvC¶|H$,µÜÎh¾–°H”ÚKÂ²ó‰|æ	+îç%_qv+zÙ|Å–xIãë ‘²ld,–°è¹È',u²v¢’² ["]Qyc1?ÊTXÜx=ñ5e‘OYHºÇRgNMYÆğZ‚O²œGø”²4â)ËD+,„ÈDÅNf¨²	íÎÉZòùÙaM±
Ë–¹
£ùô„¥¥uŒ¹
‹°›³
ËEz¥*,Œìç'¶Qaa$WX®9“T…EØ…X…å.å‚Q­ÂpA¿¦+ç¥+CºÇÒ•tÚIº’®ĞğÓ OWÎ#|JWÒY'bo1 ›®¤é|ràçäêO'qèÀx;æ÷$wH6˜zT•)bÌìTã«m&?Ï¢xHÖ xhC¿`è‚ì7Y•„w³2œñ2l0âe KôJ–Æø2yÕFÆÒe +$X’u¢^ºG·dˆ4*qBÍÛ<€¶x+Èùæ4tÒüêÚô:°ËM¯=^`ìé·M×Xı{‘Õ¿ß(JbRÍumE£¾©§Cpçeœ1BÑÁİ³96ø¬*kG|Vı
ÿ8ÑwJÜ†KyğkQB»z?%¼îg_×l|Ív=F’;&ho™Û»ö½“ì¿Ë»K¦%û=2µ7Êö'Øo}5ıó{útÀØqŸNjxcnõU.#ÂôáÕj¿ÎjışÖ™ıñİjˆÊ!È¢œO5\ï€¿mŞòõû3KºÓnŞ¶÷ÃrsßL½™¥{OÓ~w¦Ú.]Yá4©÷—2Ûï}{)¯ñÅ‚Ã;!n~ğRëæFo¿J®SKkK£ 35„Ğ–½€ÎŞÿÇõœ75„ ]Xl¹A=¬×kªRX÷ëÕ´Qµ„(ÀJ(ëi@@Ş‚yWfmkÁÀèbİˆÖ×¡³:èís~€ÓL]!¬Åî!ª¼¾ß),-ÖSO€‚­ƒ(XOˆ‹^GÖ¢ÁÌÔb y;zšôAXHsœR2QN¶@^°¥}#k!_¬fÆŞç·¼§Glƒ¯Ñ±&»xÈªxC˜µ	s3ÈÌİ ,öÿ(­XCNı <5„`CPS†Œ0LtQ³Æuu`ÜRËšjxH‘·…  )«ÄÚB ,®!Q ƒ'l³µN?"*j£¶2YGˆâı wƒ ‡»>Š¡¹‰˜¡dF6·œÎŞŞš~·6!Ú›å,±õ>øz[çJvç‰u®2cKCÓJíÚcº¯ÂØCG©oo«!±²ÌÂ»¶È¾Quç†? µ±%Î:"¶¨õ·¡Äü“ò3H•nÓ}	²²{ìííÒó"(õÂ¾JC³÷<Ÿ¥œ¼šQ.¢l]ë+³PîkÛŒâ	{ê²]şæÊ(å•=†>GÙDù)‰õÑ}ÕMãª0ÅpûUî3t?PRBJ÷4´9C÷4¼ÌÄÈ=ìß¾>àèá¡*WLñ›+{ ÔM{&e¡ÙñrAeåâÊ&ÊQvÚWáVo!¥ÄËzıf»}.(©ëoG
ğÇQE©>ÊÙ7B"ciÃõïd©7õhæ†zkÃ³4âgCWÏ(˜™p‰=·2ÿmG.õìû“`î'¸½‘§ø áƒ‹u»§xÊvÇSè¯õ„VXßlÜ•nX¦™y+º—
èÅÓ?­ÿv?VKØn9:SŠø»¿5t{®HÎ}ë¹‚Pj‰ÍÏ)8Œ¡Ù¹¹‚Q.=W0Ê˜+ØS‡”ªKàş@³n´ïÚfÇ¦†Œş xšƒ­…‰²] •÷bH*X¼}\ë®´îj8ªUÕÓ>„íqæà‚şëöÇÉ‰	²kÕl%ªŠ|wn£om¥"1ïÖ¦VF!’×ÂpÑˆù˜®èËæ°¶	c=¢/{á¼ÆóSXöéÂ6¦¥7M¹CÑušš;¡ÒÔv÷¾.×~+ÜuÜÜûuj4m¬c»I8}~GÖ3¦c¶aèz³JN›šÿmÚöSÃà+¢.­©è`=¤×8–`½a®DØ‚Ü§G-ÂpŒ <6ë¿AìfS2!.•f™œ}”Œiô#RÀ*¿¼{B4˜òùk6N®ùGyD{;#c6ıƒğ:%MèåV(õ´?[}#{úŸˆ14\¥Ä’ûMÄ^§„İ£ÇLÀßŞBcáüÍ&0ĞË¬õ&cŸeD¼ãœõ¨î:1p4Ø¸yğ˜Ä{/[ö«Ì›âF0Ğ‹mm‘Œ±Ï2"^¢å×ˆø‡ã@|d¥÷ç»K63ôLvÑ2í"Í×·>¥l$÷¿ÍÑ’²Ñ¦­˜¦GIxù¯‘2Ñ2¤,bÀcAÉQ³ßrRjCÜAÁšÛßT°f·Ÿ'2·qÁšüµ‚5læÁıîBÛá§W0nkŠ¶tëg+GÊé›ò®,)/UJëfÀãcZvöóŸ`åŞ¾$t¬Ø,Ûå©ëMÈ?ğ¥æ½e"ş%û®ÊğÈ²îOc[æ‚èøÑVö¦ÈÓ»A°@S£_f~(Ñp2Æ¶:ãX.+Yˆ£š±0–.Zšˆ»§V ÛòF{“·&7…ûó£GŒPŞYµfÚ•èKoÂQÉ”S$<O1ùÇÂ)—/=zL¾îŞzËµøÒš’r…nNˆ¬XaT÷I÷ğfOŞA¹†»K,:6œ$×AˆÌ–¸ãc\h
a¿À÷şÎV®y
endstream
endobj
33 0 obj
<</Filter /FlateDecode
/Length 4762>> stream
xœí]Ûä¶}Ÿ¯Ğs€È,Ş	vgfıœd|À&vÌ°óÿ@ªx-RÍ–4Ó3»Nf}k‰d]‹"»½JâŸEà_\Ù¥×°Á/_¾ŞızG÷¥öbQF„å·ŞııË/ˆë,>êRı6„…şúëKúğÛÏw?ü¨–ŸÿûsA- RRw?EDĞ£é>úñóİŸô–Ï?aGQBX”[i©–Ï_ïş$„2^>ÿûÎâıÏÿX~ô¸¸
(?ï ª&5	Ğ©ÓÇÏ—7`V	Ş1ÉÁƒÈa%ß>1jj&OÌ•Î2n$Ğ×[£S[k¡FqGùÅua”\˜Á>–ÖÁ¿~½°«¥?zgV|  ½¥Á¸•h‹=µØU+Å”>±ÆT<¬ñûQ,1î}€ÆkpØÿ7¶Û‚Ø‡+‰‘–¯é"X–'ú¬)=Erİ¶J+HÒ.b6YZ._¨­6v†©¢¬¢CÀ¤I¶Æ/uSRªŒágMïÚÔÖ®$ "N9tR‚°kæÄ±‰1ëÑÄØV¢TÁ¸ü$JK†Gá½v>cùùÓ—;\¹x¢‹U)ĞõI¬*°î†ÌÁ¶Á¯ÒÊ ™ˆ„…š&9ëœí4¶!`HĞÌ6„—Y %‚ÜÔjed>‰ºN7×”]›Ú§?İµ§#B€¥u›@´‚f$Í ¹»(*¢A  —TJ A?3íˆŸm¶]²Á@ù²4{&<Xfú*‘Û/%X+“Ü”|™AœOÈÙé*ÆŠªOw-HÚã-˜X¿-î:Zˆ2yk$7½ZÈw&¨ÉÁ¬Õ’ˆÙµ¥[ç‚–™Ì]-ƒ™cY¾¹ûQ…_ÒßÄås$t²Ë;A¼Ä;AüßÄßNÔ¹É=Q„¶¾£BYtá’¦´·¬A¨Eƒ½0Ë¦­ö	ÄOqj¨,Ü/¢[tçC7ä‘à=2¸Èz?óG¹âR0›µOÇl|óUVU+HÌ <éª±XvV£òDnöç9_]ÅÙ¡ø´ğy½±	DÏ&ˆlÙ„@«C/Á˜M\`7lBà6	@Y';6!ûïÙ„@%üÈ&k¥mÇ&¬lBW•MÒEÏ&åq]µ_‰LµU^ŞE/Ì,gªµxrU»ò<d.à9[İÅ“»:–qÁ©rã<ŞÉã<ŞÉƒ“Ç³K••M‚5›«7lBØ†MÜ²	Í6!lÃ&nÙ$X¹e7lB õ~d‚½TêƒÀÄ&éca“tÕ³IÂºØ,}vqÜÆïb¾ÈÚ%GÑªK¤f€.éŠ±xv£v‰\íßå|qUÇÙ§•?¬il¢cB6lÁ‘M"¸aDDtlA£@q#DĞ¡ï{6AØr&¡kì;vX=Á-“Dxd’&‰W…IòEÇ$õqY­_…\±MŞÚQ'– \õ–+ÍJ,©š=YşqÓ³\mnbIİÊ8àL	òNï¤ñNï¤ñÂÒÃ `…E@èY@=‹Dld‘nXQ?²HÄF‰à†Eu‰àÈ"Ü.d"<.dY$Ì,’¯:ÉËÚ'a6>÷*+OŠªO f lÕX,+«Qy7ûó\¯®â¬P|Zxƒ¼ŞXÄX3°"[!pÃ"nYÄĞmXÈDp\ÈDğ‹˜øş·Y¯·,Bà!x|ŸšÀÊ"tUY$]ô,Rç‘UûåQÈdà[åe¡M:ñ`ª³\©VâIUíÉó™çjuOêêPÆ§JwÒx'wÒx'TzlÏ$å#UAe¡?û"°rEİËÁ¤t†ôªµª6ÒŸâ,®”ÄÀ—íF:[¨±…`B;dÒi£Õ.áÆ5~VÊŒÚ"ş0*š¢ŞQåÂÕ²ÆÑ÷Y0(;ëdóèíre8½£WoDğÒÃÈzÇ‡`T;Ì“P]’kn—Õ×‚ş@ı8½3m#ŠÇ0ä‚g¶|L„ÁÊußú:rX­3AæÉP6¨>åÀÍ,æxÀÀ,”ôÙ{&³/2;t³‘ö¬Åøƒcœ9¢×ß{ I1İi›¹šµaM¦}5Á”‘A`”.üŒ»}Ü•Óä¿³¾^hI äQ¦ü:kq~Œ¹ò5Àp&ŠûwšSŸIØD³QŠ»Nt]xMÍ5Mâó>™‹îNæN#òÜùú¼’XÊPåö;»ÂŸéÜ/àŒëE€#‰›4İ±äÛêî]©’],,'µ×jõŸdn<ÖX2…T#AÅY#H9Æ¶Xr9†.Vïí¤ÌìfÕeå³É¬E9Œé¡Bà]•Á¥FqåKºÒ55¶ØN‹T–¢¸~Ğºz˜Ùê¼‚j"UB4"é˜¶£c±…	á9 1NûÛxŞö4U¼„ó”Ä·š?c(ò*Cov_Á¸S—Ïl8·™ó!&êuCót%‘5M«®êi!üD(¯˜Í³A E»Éà˜ûctjh&Uçï·\x!xfòÎ›œx¡3M:ºr¨Èƒ=Ì¨ä²GçÎÙuÊÇ³üÈ‹»¤ /‰¬ó^Ï
^Ğ|Ç$WZ4ˆ&¡Ü4c_$êAY‹¹ugù<¸ÓÉv%Üı,F§™*rŞ!<¹¼çCq&sOqæ½°hÛŠûŒàòÏtğ)™©Ş´}åú{™å§Óã´Eù&\¤`j–yIjÃæu×…™–ç™İÖøiçe™xcêîyùvÚRçË9×IçgÉRá¼ÚÇ&Yû’%ÁùxîæX£_d©ósì[Û!¹°üÜNA]´½¤°yFé6or¾PQÅ$Ö“ï}	ƒEm]"ÑJŠDæóYEŒôÎQsEfÍ-§¦¹±n7È¼«óñ0÷yğNctFW|l#Ã^PÏeê†uÍtÕ1+õæï)ĞôPš†/œ¯3÷0€’„±cäz(Ÿ±Ø›†áÔ$œ0ÛeËci©Ñn$©ôj”À÷å T«ó^.«õR/«6>AØ€å`R`êò%xyO¯öH
J(J\²ˆ¬GîK¸v(ÅÃLĞ—øñŸ{ú) ÄdjK}GŸúÔ:µÓ6İ×	£öd…ò¹ôÛÜ§{EzÆ¤şU¥ë³ßÙ_~¹/WÀÒ)5ÚÉwnùÊ@§ ‰…Z?UT/N†ÕH+ìB”0ô=Ò‰DL¯ ñbvõJ:3 Ş¬JKˆ¢ ¤ïÍ–¤ï)iìŠÑ‰‹ WG9ØPÚA”8?‹ÍAÂ°q+é×I$Ñp«¦MvÄ`:StdXµFlÑj¸§¤ï"é—6brEm1µÒ:=)™EGõ‰^©*FÌJ[gcdÌEû»U\VÜZ7G´QšË¸<Í¹MòMÃ1D{ı^RĞï—Ğ¡)pŒ^tÆÖğâ¨ÂèU˜µR €ºÈ æ´ÒtDYÈ…NTIúx Á¯Î#8íP|)I>Õ‹ôôZÁY
P%¸*Fv·!WE)¸m;ÍÛK‡´„6áãHgWLøĞÉ#ÍÈ{Lp$@ÒĞp3æ˜)bëŒV«=İµæ¢	âWÊë0ˆá]O‹yğúîK­"9¢s ÆQÑ1ôº¡L)¦¨4)V« ŠSÍÛ'°!ª³:aª[™Ø<RŠzÛè)uâ§FVúÁ“ô/:ÈB3EgPÀ³…¦ãÔï~¥¼½˜=O»qñù:Sû4#ˆ4Ñè‹²L
5d}¶v«16,«¡E/º)DG¬Î„Yµ(ıÚ<»}L³–Î³]œÅHŞOù¾Í÷Ó¬E³QÄ]ºEWÈ³Ÿmÿ÷ µ§çbÛl'Íga‘gM6c–ç£=eÓ¸6Ã9cºÍ¾q†‡ÔÏâ³™¶öQfk¿ã/k•õ¾7ë±1õWQ÷C6c²H¶©[®µg.(&Ï*·­â#Ù0‘QÒ	/	Iµ*êAÕœ?÷|pW³§ª£‰pbŒÇSeİõ\œ@µ°)§êHljŒÙûVÁEC‡lTnğû§¾U‡ÂÜÂàV6ƒ71ïw(å•»)aXÄÂĞ™4JDÊVN×Õ):«!}JìÎˆ,¢ãuNJıéVQŒÓ(.„”ïÕ8•t&÷UÌiô`NøÄ¸ë!›!1húU„6ÙLÀ²~2wSMy3ó¸„˜XÅc§ÙÄMµc&vå§Üö¨¹.²DKE)D7•Ü”48ÿ51¿;ÖP¸ĞÊ™^Ê=ÒP¸ÎğÒƒê›İ6ÌƒÂüêôü©×2çUF)m‹Ï˜q¯ÅÍñsß—)eŒÎaÃ¼+X»<^L¹ìÌÛÙÜéÏµöU.†ÕæáD™ÁÌz(Å”*ò¢ê™w¨Ğö˜ÇìUGi|µ©6[åV+3ÃÌb{óÖª“»•¹¿<KåSqÏ4,
;ÆÿŞ"ÿŒ^}N@¦ê1×è¶çÉÄ„Û—=m¤H`i:èòåàMˆ	p±zaxêşñX5~‰òSÛFÉ°^²K©§c0™$X™:KÒ” ¸‘´vuúdâì1¸6f«Ã±¨³çŠsWÏU~×stó{£™”gæhÖìÏ¼°g|ö•ˆ÷Íp¯ï?]‚¸	ülïM”¸©'1M+Û3‘w“•å8kvÌ•õÇ{_{’`¿:ü-&	ş£ÇßÕ$ÑÛrq¨ÂPÜ	Vôù[Ç\æØèJßÄ^–~{4×^]+ÕjÑÿ£j‡òB—¥æEÕô§èî­lw7í}uÀÍ©g_gUF»¦Ãª,´r:®rrÂw«öy\ÙTZò¹ÿÈª&Ø>WJõJ,âJçd*/„ãs¡-eÆíÕúrùÂKeS^ş5êüøfu·qyÏ:èâ¬›îYk±»g]×IQ‰dk±ñÙÒ^^wô-÷°x·ÒFßÃ–²î¡±İK‰-ıØ.'Rê
Î9¾J¯ã²ùvÜwsÊÛÂHÇv°+Ä7°+È÷¯+Èö€ël·˜IÃö•«Ülÿ¹ê×ae­ÕdO=ˆ#¢ l÷cZ¬èW¾{¬AB¿{MßÑ[Aß½˜3Àw¯3&»İë
òİëÖºù Ò¼Ååi~m’7ÿ7/DÏv÷ZıT,¶)©ÚÆ?-&7™®ír*¼mèûöl?g™Õéü#„eã”¬¦‘l÷:béë6løŞuùÖukÜöÛm§˜Óö”›Ømï¹©×6©Uİõo`µß¹Fm„e;×ˆ¹U1aÀÇUüÄ&¶¿8¨Ù¶5b@;óí[gÌuûÖäûÖ¬u±?¤:ª§º´HÍ#¤¨¶šo·kMÿç™·Y+´‘Êzï—}‰:=lK€ò2…¿ìí^¶æÙ'ş·¼	ä/}]»Ö¶ÍFü%ò¸ª–(ÛR5æ77«²&µÌL{Å¢QôÓæë)‰ïmüÎF"£6Üøˆ¯‹²?brmÍ~ËÊ8--×¹ä»o^@–ovÌÊ½•+T÷Â+†uâBÊÄª¹ì¯<4s_Ú¯¨Atû,W‹¿›.{EZOr=wß³@]OòfÇgì[9Îğw]ß!\r^v–ÎK´êìÂØl“œ—ce‹ı'>6Ík Å#ª·r*ı åÆ
»nÅ@Ç_Lìšs«;õZÖ\ìÍéŞRç[½ífby_:Š¹«š¾ù{SÑ<¿@a¯[y³CPgùÍ_3¹ôŠÀoï^/Vo½ßæjìº—VeƒêÇ|«ä	ßr>/{ØõÅÒ§V¾®Ÿé˜V®)šøÏIŞ£Áµo	Æ©Rür5w‹_\
åâ—7;f{LöêóN¼ÑDßF¢÷‘¿Ï…Ò‘.şn†}<?}Z±3”t0¿·ëÍ
q'Â¥¹µu¿·VÉuãìƒaèßh­ÎFJaxâ:—ò5|*¥Ï‡WÙHû«È½õ­úr¡ô&3ë®2l—wÔæµ×¹FÊZ(±¡÷ß9ÀE‰Ä¯oõÎ¡Tiôn±KW3ª»_@Å‹çy³cş“oõ¢¢Tü÷ı¬y÷,U^B0k¤‘#å×.¥ğrª‰p³å8ÆûºqÒ>k_s¬Yµåïe{d=UuÓíÕ ¥^cäri+5C~š¾÷ êÉgcf[¦ÿpßc 
endstream
endobj
35 0 obj
<</Filter /FlateDecode
/Length 5563>> stream
xœí]Ù®#¹‘}¿_¡çœæ¾ İu«ül»€ù€ö20ªØóÿÀDp=L^^eJªÅ°ººº•GI2[’‡LjS:¦.‚şüfƒË`äeŒáòË¯/ÿ|áï•	â¢­ˆ—ıååşëòÂÍ&İêsã”şóÇß_ò‡ıíå·¿×—¿ı_ªÏG}‘R)®î¯	|kş@·şüùå·ŸÌ%^>ÿ•*JÊ‹ö›RÙ‹Ò—Ï¿¾ü·Úşîòùï/¾ÿüç*ì³||´H@X×!etl.`r¥?¿-¸•vS2x\ú}#j×ˆÜK>ß±ï½Ô{`qÇJPä%‚‹Œ“öıÒdÔ^Zè½¸{ùÅûÂh¡P˜Ia?×Ò ?ÿ|‘Òmÿ1ÉšV–<V‘æÕÑ½VoìAÜDşÅ~£­Œnc;]õ_E¢,¼EOUá©ÜRJlÜ¦uöòk½ĞR\¾ğ…á ŒˆHB…ßà´Ñ²`ÚÇ ‹Bµ…Q—_¸x^ºT¡›×Öğ­1RÌÌ8CuJŠu¥té“áò’¾v¥¸çb’oõÚ“
$iI)jQ«èB´\^‘tÑúz/ÉÍFàn*ÈP?şòâ¢oW_øjÓ$L¿™g…X'ƒÑ:çÇö]¤®8ÊÊ ÕôöŠAï¼w£\$U
%*‹AT@¥2FzwqĞ?£F;«ĞT	$›°)cÕê¹Xuˆ//x?!¬yÁšt&B0­•¥º"/©ˆ"ı;Æ %ëJ`Ğ“í‹«Â¬óÔ*]SİÂ`4“Ëvk1l´ÍÖªFM =a²Ùù*9n_^ĞaêíèY­^ôB=¶É®Í}Â €®C¬4-aP5}büê1V›™0¨›A!üòò¿œ>Â%ÿËY£~N	‡ŒFç™4Iã™4I’ÆŸNŒ9Ê¸¥Ô@’÷,âHcqÁNY„±)‹08g²Ã”E›²ƒsqAÏY„Á)‹0èBØg†-øĞ)˜³HşX³H¾³HÆĞ/[èÃĞ>ú{“ƒ¢õ
€ÁÖ”QÙ”ŠÜõ±ŞL…Y¡Ú´æWB/6‡³!sa42
Á id—E¨‹saĞj©%0øFñIØ®Uº³ƒ”Ÿ÷Y„á)‹$°e¾jY$_ŒY¤ŞÕêE/Ğc›¼àÚÜ' è:ÄJÓUÓ'Æ¨cµ™	ƒºrÀ©¡Ç3i<“Æ3i<“Æ}ChtÏ"Á˜]	FOY„±)‹08g‘`Ô”E›²ƒsI¬ç>‹08eß˜À0<M`˜³HşX³H¾³HÆĞ/[èÃĞ>ú{“ƒ¢õ
€ÁÖ”QÙ”ŠÜõ±ŞL…Y¡Ú´æ¶zÏ"ìc‰\É>‹08M`œ³H4fÎ"Néó>‹DCRÈ!“06eß˜Ä0<e’¶LÂW-“ä‹1“ÔÛÑ»Z½è‰ zm“Ü»öT 1Ó´…ÁÕôŠq&À˜mæÂàn†…\pjòLÏäñLÏäÉãæ¡ˆ’¤ïšMYzÌ&„ˆ}6IØ>›$pÊ&JÈ¸Ï&	Ûg“NÙ„Ğ0e“î³Içl’à}6É`Ê&åcÉ&åjÈ&ßìu‚cûàó]VŞ+$T ]WVÎ®TdĞ?Ä|7d‡fÓ’?’Õ[6I1dF¦l’À}6IàÄ¥RG)DÙ$û	Mç	ÁrŸM&Iµƒœ'5	Şg“Öl’®j6)C6i·£wµzÑAôÚ&/¸wí¨ b¦iƒ«éãL€1ÛÌ…Áİ¹àÌPä™<Éã™<ÉcH·E”ïËºJF»Ë&4Ø™²	cS6apÎ&2ê)›06e•vÌ&2**æÆlÂ`vÌ&ÎÜj‚÷Üjs6Ék6ÉWc6ÉØà›©Î]6ÉíOÙ¤É:GíÕH]CĞUeatV¥œô/wÙ¤™jÈÅ¦-DÙ„bÌ&„ÌÙ„Á)›08gåçeİî'6	œ'6û)›06eç‰M‚6nÈ&	lÙ„¯Z6Éc6©·£wµzÑ³S6iò‚{×~a €
 fš¶0¸š^1Á³Í\ÜÍ°NEÉã™<Éã™<0yüéèØË?^ÈÆ›Š’ÆNÌ±¤dÒ!iònØ/£š˜2Q°	Œ40gPoÎÛhHƒÁl$
õU2#h­Mã2™–©»À)mS±à8¼¨–±T2Û˜ÜvF8!ÃûHŠª›6’F¥ï÷Â[µ„Å¤‚q†•ÔÈœ@É!è±‹–Á/+*û2@v3Ş†T_i$RÑh9j—‡®7é¢ö¹ƒEt’cÓtcº³t±˜B¹+"Z‘tZ•Å×l¤ªÎ^¦ë½×İM„Rtkvy»Ù{¿&a—cWR‚ßàax¤ÉZy.UˆÛÔYW€Q€'ÉxÂn"H–×SóÎ0FRHÅÙŠâÌ›™JŞP—b‚EZÅÏ!
4ú ²—K]=([K¹X¼'7¯<¥€ jLx³Yê6ÖÇi;6¬<e/+Š¨è£LÉ w¥`¾u9•-XÑÌ——^4RúĞ:PèMDÅ)5Ua¢"Kú(t®°ˆ•ßè[—î,‹Š¬ªR¶hÏX~>WUŒ¤i*„²UÓĞD3É L3ˆİ}¡woïÕqNlÊßø¥€üÎ—<6‘>»JïHNÃ[&m«¤GH~­ÀX!,ÿUôù•ş*~ïßM 'Èÿ7è{Ié³ô—	¢½}°Võ;æwX†ëú*Ë,‡ôb’ü  QtÈÍş¿+Íû|Íâ$1Xä˜¿K"îº!_3.ÚG4·•‘”È¼%ı0¼¼ñF)k6@È]õ•bÙ>*ïØÇ~kû4qØÇø"2]›Ÿ¾•XÛÕH]Ü«Fr<l5:ŒÅ‰òb¾Ÿ{•´ñZzı©hÄc ±öZ(Á&>.¾·WdQ&hP c0Â»_™Úá‚Íó’ÇPÄ5{ ×õæŠgô¹ûú‘’`çGO‚ é™$ÅÙ‡™?Pìâü[$A÷L„b‡ŒD]¹%	Æò½‚ï~'?ì’ä™òöˆ
¯„¸†.TŒçî×á[¦ÑŞ\ïë¼1ŠOˆŒ)ÁEMéú5É"Õ&4MëtÙä·nyDîd´±¿˜\Ş2¦2Ú…h”>RÆåW•7š°D«ûë³&ë†ñ’¦ŸÓK¹HVÄ º\öµÔhfÌ+(×_×U¥ÒÎFæ²®×UŞ¹¦™ƒ‚g4íÕ´âĞÅe+6+2P”Ñ‹#Í›OE]ÌåiŠÖê’ÍV'æævÛ"–¤Çš?fŞ¥K3ÄˆB19²‘ã»ŞËÛó>ñ~{y%Ÿ#1ØÕ+İS5NÕhY;&#uÌº}—]èZµº(‰Æ}d¿WwšÜÆ¨ÔŞ•Ğ¤ÖÉÚo´á‹åÍÒ½µ×Û¨/»ÓsDÇ¨íuq‹±ífIE¹dçÏÌÄ¸ù©àäı„¨iİ?±òÙe?ÌÇ¢Ä(¨uğ³¥¸¯Uİ Ã•9nèùké†T"Ä;¤2~åˆ«Æ×Õ´šÕç¹Á×C*ü[Ê5¤J¬»K	Avrñˆ9‰ÂôHI6!à‹µJ–Î¾näd7^`¸Ş:ö0hs½Ä7¤ûı%;ƒ¹«ñÁ¯°ªntÍ{;HµÖâ²uÛ(¦§¶:ÓÕ»$3Wu$:ºÃªñ;ƒm¨j¥÷uR<íïC°Quì±Tû÷¶e—YUµô¸óm\}ëp:›¬-ue”–‡WN·)éÃãë:=d¸eX²tÄ:²zà­Ÿô«p^=ĞoèÇyq‡ˆ›œg6TÌŸëÆÒz™fÀÃÊ1İ?/k%ÒÂªÅ¥cÍ»@½Vµô¼Z›^÷€•cM‚ñÊ®Ä•c]ƒ¥ã
kÇ+«Ç½X=F`õ¸ÉëÄ½“(§Õã¦¸/#¨7GÙ@Ã2wt^+È’ ‘y<\B&ØSçŒ³°†L`ZÖ‘h‡•äâr2kô†Àr(¹w Ü¡wõošW•¥-KğÃº²n{Ğl*¸´÷³­,“Ø$ƒ3
—–5ï¥Ö–µ›Ù/.kÎ¢éëË–˜34¬2—b}¡*ï+Íƒ}©dîkÍĞ»¾Ø¬ûş„Ú®œ^ÜŞ­óêwmˆ2y²Vœ	¤¾’[ÚaÉ™`Şwb¼‚5gÉğVœ+‚+ÎÃçV²iêï†déF¹ÑQZgïù~«Î|h\á=®­nÄBv:`Ô?$â=]Ë×ağšb7õ©·ÚÉ™[—¢İ”Ği5£W«~*„óÇöà»Â S"x·ìK œ“b^è­ÜİqJz±.,|Eá¥ä%Õn_*z8¸ğÕÅw2ïÖ|¬ğ7ç§ûzÂ“_“(yäÒ+)·É/<¿ª×~³*F95*¹ìó·X&y‹–¦‰Uå™ÇÕÿ·ii¸ıZºWó¤¥Ÿ´ôşÇÒÒ«	ærFú=Yé¥BÖtõJé¤ïĞGâ‘|q¾qSÕnEŒ>ñõNUñ®ƒ#<ëyâ}=".—”ÛyÖä<¥i~.b‘WdÜÉ=ßàŠ+ªó‘|à‚Ã1µŒen8­“kœí™Yöc!«˜ºaÙfx¤z´á#Mµªki‘uUËe¦+)öıÑ`Pu“ÂòéµÚ%%¾ÌÈçkWm,§‡%Ë6Î?Ï7şÌùÿı¸o•@ñ”pX!J8H½…q} Pw×Íª•°»å âF³¾au€±4ıîw…†Õ
«v½µD<Hœ}“ÈıÚ½jkTå­Üæ=7{„šŸF„ ¸æEqE@I-6§ó¥k„ÉL×VT*†këzïõw¡$İ–MänñŞ³¯Ìü?uQìß)kï¨Ùu2ÿA[
§‘OšWµ~àıƒVTÕHû‡¢©Nb‡ª) »CÕPâµdgÎ{ıdGA:ßE†wÌjÏğ³ş–d“ñ'@m6„?alø€¢F!Í¯Á"İOhØ(yX`ûÙÛ(2ø%ğ¦‚‚„‘ñ‡ÒUóĞH3Ñ N3&Q;8zË÷ãúƒG¹~x“ÁV¬lŠN{¸y´;Àù3ƒ™Ù×ŞøøKÕvR÷j•/¦-ëØ½ŸõıA½íß0¸OwØÍ8¿u«öøumQŒÒªUu+»¼"UÒ¥Ä¯©õà†6Ò[ú´}z(NzìÃØ÷ïE2Ó(´²Æîıù@>F²ß~ÉÜ«y’ÌO’ù€ÏOÚVsÌÓtîù™Ùù©çÒq—äú¢N»ôz¾œ?0z µVïj“ñı8Íç>Ê9±1x½±s¥’õvÓÓìºÓº2vaó¥®ÖœÛ2]­¤‡¶´êö,>Zw«¸îÈ*låk“÷àºFùİPšXÓ¬#(s‡+®½úüféóK!ƒNe-7ÛŸÛ2•=~iêÊĞ.¶CE–ONÜ
CÇe0/¬<}=8½ûHâòÅªÆIäÓo+İ0Ğ]×ª'GÆë¡ô:}.4hª¯EfŞc=1h-çğIğİbñ@9¤ZQ³Tˆ,¬; Âe,=°eø}Xô¼üø1ŸšDR9øã6ù¼‰V÷iw1ëJ»rÆ°¬Ú±ŸÄ:av³‰-o¬­vfÓZŒ¶)>AJ¼:a|®"PÅ@N½@È¨¸éV7°Ø ĞİU\`Å[¯¬œ-˜¯»²¢Öv„ºg25ÜdOXú-t52êŞÔ4òAF1o"î°ÏØS÷õĞ8Ğf+Zom€}@0d“Şú7ùÊÄº—j·Õ+ëÑvˆIú˜Îll¬¦EËÚë¼­©u-É!Z',Ÿ|±†CÓ³¬ûáq‚n…;SİÛèœ6
ÓÙï.vgÉ{÷:•^Ô0ĞëY[Áî%+d$Ø)õ0õ6ã%•˜vÏ'EîvŸ^	vß_"é
óíEPl/İôßé†BqºI»àè!µƒ{¯ùn;Ilo Ø×ÑC¼Åæw™6QCÓÀ“¦…ğÍòù¦Ôª ÿ½ßßìDÔah Ìp'µ®„77Rë7ë¬-I@ãÔXgí¡ù¨Å
Y}ÔÃŠÆê‚Ã#4çã¼«±Ö@ƒÜ«1)ëWÊô¥˜¤òêJÒÚ‡¢¥y1 iĞË=Iãåûºœs]ƒô”«qÚÅy¤ùÀ¹§½>6‰2B~ïİóJú&“ÚšÏ˜î·ß±°Õ<6t¸ÜòşoµO}ÕÄù}û?ş~¾pdê7Ù {ú†ë“Wµ\@8Mvş˜;È¿ëé%ßä½ˆå®ïåªØr‘â´_İ`ó+}}ñÂ’¢pÚ•Cqâ*W:èHZ«*•wÔuyà‹Fí’Ê[›9L>mqWâFšMK§ö4[,4 .‘Æ<Ş,[ä½nb`Ù¢H‡îX¶HóòàF–±áh‹Š<[Á¢­`ÀYµúİI€«"]Öz6`…ñkPQÓ—2{¢0»'Ús3ÑFhØm	Ûm‰¶Š!ÑÖËvÅ÷6º‰PšnË.w·yïßä-3Ñ¦eakE‰•›DÈPã#ÏµÚ¼y¶¨Í
Äğ³*ªHšy¶zĞ?ĞFğ{ `‚èLT+Ü	«ŞF§¶P˜N‚u±;YÖ»×9µØÒ¨PÑÒlšëcG³işaÍF˜™i6Í?ë±£ÙtşUfÓğKM_ºÿJ×+”®ê‡FšqšEApğÖÁ½Ï|?š¢ì(	òÚ§ìæcŸÖ·)~İûçà³Ï4Sú_ŸŞ;ŞVŸŞYÑîß©éE90juâŠ0YAíÇtìœGÛ~ê³R˜Ê ×"ó3½ñ«
·îÖÔn#é3óÔëİ[Ô<‚Œ”»Ü–~p(ËûjÂ^íOlFşÿ$O‡9„tPø#%ç]ÂéÔüC…PüÛ\öÑšf†MÚ½¯0á§%ypØˆwö€sÿÔÔı=¾ö:/9ÉTòS•ßy.½öõ“Gö‚|Òfï99ñ<Bj^š5ïÄé½Dªö²Zğy÷‰L=;b¿ƒHå=ğ›“ü“Yq:µ]éNjªS1òt#á„î:Ò”ÿö]&ˆ$¥¦G ó^4RŠOôÚÏT(™Ñdˆ3b7±RüCSŠÇ«m(GC“¤y‚8—Ğ‹Tš2ÆÀœY Òÿ¡d|ã
endstream
endobj
37 0 obj
<</Filter /FlateDecode
/Length 4694>> stream
xœíÛn·ñ]_±Ï²áılÙÎsı ·IQÈ’ş?ĞŞf¸»ÔáJ+ÙdGñÙY^æÎrx´*ÓŸEÀßVöŒ\£Œ1,_¾Şı~‡ï•	bÑVÄåßıó/Ëo 7«tĞÔçú'è(üûŸ–üá_ï~üI/¿ş/ç£^¤T
‡û%A6Í éûÏw?~2K\>ÿ%å¢ıêƒTvQzùüõî¯Bhû·åóï¼ÿü¯ *lfğ	à@‹ã1¤L İ 6w‰`ò ?#n¥]•a.ıvµ™Dn1ß·ØR/õ0h1BT¹`pÁq‡{¼7•z½Ew‹¿x-GfÇ°÷µ÷ßáïïwRºÕá³Hä´² ±
8ï`ÒZ½¢áùëöƒV«½­½
ô=DYÔwâÿ‡~{ Œ¡Œ³J¹|­FËåš_H(ù8ï3LŸ€.
Õ
#—/Ø=H/]PÅÕkk°iŒ`1fœ‹’`éJé
„OûKxíJ÷ İœÄ¦^{R‰c*˜Q«Ğ…h±¿ì¢õµ-à" 2‚ñ¡QıëÇ/w.úöô€O«d¨1Bœ:ò1-r§›ßÅ°*§¢á¸"ĞjøÃ©B wŞ».ÆL_Î,Ê BcªÓ	¦Et±ñ_•îF;«¸¨dj˜LV¥»U…x¸ãí‚ìÎDÓ!Àhm®àkA‘•“yÂJ-H¿cá³+\¬³RC¿Ì¯ÊY„É ]'jr’‚6¹mlÂ“EOIyt{x¸ãJS›síjãrMÌ8$¸Ö6|™zWº¸!00›iÜâÆÕøÊí‰€Ûl7î&Xæ¾ÜıİHXòè=êçäx@xàyŞœÇ›óxsoÎãÀyü|")qLx¯È›8 ¼÷&N¨7AØÎ› pïMœ;o‚0ãLïM¸÷&N¤n½7A ˆ¥÷&<ğ&Şy“ÌŞ$¬Ş$?õŞ$Ã¸næ1UïMòüaëM®Ü8UÜ¸Ñ5f1ëlLå†œù¿õ&MTÜ;T™VÿRoŞ$)DçM²ó&	¸õ&	¸ó& ÕÀÑy“´ZjÎ„ô ûŞ› ØpO‚Ï0v°I ÷$·$«'IOÕ“”‡Î“´æL³h\¦…·ñ$„/©v¢‰ 'l…¸ÄŒŠøÉì³Ù*‰‰5	”ù€3!È›ÓxsoNãÍi</ô0V‘Ñ2ØŞ‹ Äl½H‚m½Hî¼@õÖ‹$ØÖ‹$ ÒÂv^ j—È$à6‘IÀbÅ\ÖNÏ•"“)‹)O)0®—yÌ>‘)óoÂ•E£Šc 7¶Æ,f•™©¦7àÌÿŞ‰¤¸S¨"­nCKN$éCçD²s"	¸u"	¸s" İ;‘Ü:‘ôÎnœHÇdó± Ãô±s$	XŒ˜	,·$«#IOÕ‘”‡Î‘´æL¹h\¦ˆ¦´„/iw£‹Ùg™q‹Ùñ•™!3Y³m,sg"7ßñæ;Ş|Ç›ïà¾ãçƒcÄp¤ã%lÛW	ˆc5ÄÙù€I}Êƒ€Î™Ì}>¶Z­‘1Âdí0Ÿ†¹U Ú|TeW|t‚^˜P¦
¦Ğv{†¶¤cd/l~d ‡¤SKkë -ˆ¸9G9£<ê&NX6”)sˆJšÜÆúz¸È°úT
˜(	şaÀÜ6…0R˜èaC¡Ohİoåq‡±À?FÙŒ
qb
UynÁu2vØ,ÆüŠõãˆQ#Şë¶‡¨Ò3 !a‚µæ]em”@·¿­„ç	3}¨ÏCí*g®Uñ¶0¬ŒÙ~ÅÊ
ğQİ6TĞæXoMôs¦˜rmaàÙ¼“ÇR
¬Ç§áÜ¹¸BÂêduZnrd8IG‡õv«
nZF/ØìÜbÊÛ
ú
G[Çˆ½‚vJ2¢¼³$[v3Ú£3K$,âhÍ~`P@å÷mM´ÂåæEÈ²ı¼ŒµdH9_ŸâcÊGsÌ-¿s^i¨Ô$r÷ñÃ.C5áËc~‚‹·<V­p„ Á•ôy~ú\è¶]ê:¿0³ÆkWF2Fâª~–Š¡í#´c‚ÓQãi–Cõ©ÂM„Uk3‘’—qÈóÌå÷Yáá‡ãC}>OÇ8j.¿CÊ_;í^pÒ½;LGÎ{ÜŞdyv°Ü/[×yâ?U û«Tœ^dºS—qº®©ı\=Ì3‡9½ú	ç~/Ìi.€¹lI¹M¸ŒÀØ°•ÒAFÀ½ñŒ"œ,F»?CîUU*ğ_}Äú'‹ÂfœÂ†)¯Ğ¥º…á§éñPcLm·„©INód¼DÜO„ËF„.ŸİÆÛU3Ég··ö{Â£mÈq1Œ‡¡ép¨©-Š:ªPãV¨R[XéÒ½.\ıqñ‰Ç•D Çêíxã¨oÂ¡lpšk´¤Ë~ëa¼)Ï7¨x21ÚQ>½zzûûB…<z1äàˆ!7ãÿ¡Bª\ôNšóé†WJU=¾W·²ÏßNZ~»ÃV¥s‹ÃPhö•ÁŒÎ°‡3 Kd0k:2 L®0^°Ã",@X¿|Ş`oF£Æ²và±‚†Ï{ap%Ë	åÓPG³zä*#ˆ]zjŒ%„¥áW%EìğPZ¶8Æ “xïe–9úXåÔCs«„2WæpÁ¯Ök<ÊlØ8 ÒG]&® í¢X…L…8„9•N"2Ì&VfUÊ¨²”úçi’Ç†¤Ix“Ô‰¾½ÆàI(ê’x!kÃœE—f
ì¡ƒ¹Õ‡ïÂ®"@0³;bn _Ğ%«Vr’ƒ œñ¬ÖX¯­Âòø°¡€']õÍ.‚gÔ¯V„É­•‡ù€p>òn5
•‡O¬<Z¼TEX(ËI)0ßHN}ÌZ_çä@s€Õ‚‚fU®Ø ËV\Œb±à£‚Ç6>µ,”9LBô*é€Gí•;ˆ4öÕn•Ålè&‹‰&5†.i‘µÓŒª3Ó—#W¼š™ÿ‡ç÷XªÓC6GïÒm}¦I×ZœmŸ¸î`ø„‘.è¦éÇ~¢ÏúcşWb›—}è}ñ²jşipƒ×_éV¡Şá‚{,f¾ÛÄ{ü5h]¨Nßm®¼»e²C-9H$KŒpå+h¸c²ëäŸÍş}‚ÛÍ³;hãëç[¤‚ÏvF8İ¡Nİ^âöííºkL<¬‚&ÇSıÓ1ìùí¼ó;ƒßrÿUövGaåy¤Ps:œÙÛ…{©"ó1øˆòáÃœwÈ‘ËêeÆ–É·ífø1N{Îoï1Ú]o.ƒ:¿?Ş&šRÃ©ÚñöêßáÏuÊOØÂ•O<¡ÔdÊ'u“O7uûãÃMÑ¡ NH‰+„Ğ†®.€ó[9ĞÛë·µÈÁBD-°Ähçnmä ËÚıÜ— ëc	Æ 2‘`"G653eë{Œğ?•¥÷%?mÇñ)i:„~)Fçi:Hr›4=z±J¥di:ø½ÕAÒëX
!Ä7»4=B¯4ä¡,Oÿ›P¢Ô³Bx^a<O¯0Jxi|J9&”DÎ”lm–yÀõÊ«‡·%ê ƒLí„°„‹ÛñD óÄ¦Q0ËrôôÈôàÙy¯iL’
ŸäGx’œ‰½ìs!ÕºIÌaÕ+ÚÃafUÍj–˜ƒ§\,ç<¦ +ñ‘'æH7›Ä<âKÍó3OÎ3„§ç¥OKtÙ¸-%îhÉ3Cµ%ÙŒ¤–ŒWÒy‚^YÄt€AP†E34ÀPÂA3lî!h;x‚®p^[– ³¼ÛÑ8P`}–Ş€<Og½+ÓÙ$M::Mq®•À®|«Tİi_]4yİäÍeñÀjœÆÃ«–ºßL­³m¦İ{šu.³Æ,K†Øˆ÷OÀşşÆ¼JèìˆÙä“Èz{„¬ÏH%dñó}~ÛO#`†k Ê*<÷çv3°†åL{/ëW áÚÈ¨køÇ‚v vôÚÓ"ƒVvƒ)ª4nñÈ^³ÀPU¥“ğ8ŞjsMĞcº!¢ıtŸ8«HŠÂ1ÂQò‘¸×B^E¬/D‘_7 Èf™ 55~»„í²>è &ˆ=›¾ÏAğçKè€í¥¤c`­<–¾g‘u¥è*	AjûRYëFéb=®ø„OùßK(rêÈ'Ü\V=s¾z=¾Nùà[Ë‡„0Ì(²»)'Q´r×~ÙD îJ%9"ƒ·°Gt5ëkÚ)ÜÁÎ
›ÒĞ…ÜBvzçŠB×wuE½§[;ß³Ö”¥ÓÜ:^=s0¶¤½Š]Ûñ6ŠT/˜âÄuYôÁj¦øè¾Ø2gdj
m®Ìi	§JGê«‹©h±;Ü°ïî•Îªn¥}•C£K°w\}+ÏC‰Œ62ic„"Ã@*_yg+¬Ê½˜Àã|}ÙCşVŸÎ‹˜¦L$PÁÓ3¬˜EO©şhµx%R˜5}_ÇøHÅì£¯–}ŸXğO#ãj2ˆÇ¶U?·8¬vÙÍwÄá†œôs¸|Ãê\fÌ¹ä(¸Ãäè;‘HC.mIš+¤ë7DóáçÄ‚g Ò¦óÙpò(:´óÜï‘Í¹¼ó{5›éş4›Ácsçâ6<ùnÅBÈ]£ùäØÈ ê>Ée#¿c.7ä®Q|ÆeùÃu¨£a•TšMpÅ‚…Ë-¡=§J¬:æÒê:©N|ÇÚÑ»\;häÒšà*¯N xR7°ÜÒmØ9©~Á_‘´âÜ<œ™z†Ê“Ó²üXò“ô”íÈ“Èûä‘¶òŠÁÆS‘¸—qbwøJëÊß:)¯µµKşGÙ4Á7¶Ÿ»©íâƒÑ=úi«ì•R"KI®®›WïAâqñÖ9áë[Ç7ßÎå2ä.NÃØÈgÓ0Öu’ÃöŠ´êÌ† ›òõJF!¹:™ŸÑ¶"EKY½·É—lÌb”Šİ7-µGxûÆ0àeSÆ´Q
mÀŞ…6–_2t¥f'ÀG{pQ[ƒ§J©Vµ{Q‘òŞí
ÔÖ¼+g°-¿ÙgÅš+Ë‹ËoG‚ Z	ëö­¤Í¹`M8øŞ´-¶rÄr(½»óiVˆä%~SàMtkœX…ğJ«]EÔUeLZºš\\ZÆTNnGeL£SİkË˜\Ü—1)Ï®²´úàÚŠbuL ó`ì]ÁèÄ{éë Yi‡1XÉÊ˜,-T¡ãÛMVÇãéšÕúT +	js°â!†+3ªh³j¤F‡µ[>ì~QÜ—2¹˜Jœäwb*ŠüÀR1‘ÙÜ9Ú—2Œ—2¥Çş®‘ß^4êJ™hLvÇˆÍÎî5<Ù£FÏ^OîÅ})“
²UŸq N¬–	`bÊñZ&ÜÂÖ”o”¬e5AxÇjVË0.¯fª^ÏTa¼¢©õ¤Ú Ÿªˆ8"ToD(S]‘FõK•İ­£¸/jXªù1üÖQLµA>ò[G1W™şÖQÌõFüÒQÌUIİ½£xPÓÔ€İİ#êİ®µ9èöG†nÚ\?*y;ùF%Màã‰TãÅ
Q¯QˆÂ§»¸eKÉ+¢\M+DÙRô
…(—Sƒ…([:^±åjzX!Ê†ª×*D¹š"Vˆ²¥è•
Q¸+œ*DáxNåJ_q„}*ï¤)'Q´m{¦°9¨„
7ÆKÃ•›„ÜÕ›4òF™Ÿ‹~·æúï®Úï}AÌig˜cî®À\C€™_}.ê† Cß\T¡¡ /ğ/®<é[B^™.:0À%^o¤pûÊwú=é¨‘>ç\üÍÍ³Ngº0M>‰l<UD€¿šàD [­¬¾+ebéîûK0ƒN$¶“ÔiıÚKM9‰¢=uğ­µ—gf
ùº˜xÿÌà‡­D„?¼H¢®™ƒ¦üºÜÈÇZÂQ¸i^,aİº-îÿ×­
endstream
endobj
39 0 obj
<</Filter /FlateDecode
/Length 2650>> stream
xœí[Ûn$¹}ï¯¨ç ®•¨;X{í}Nb 0›İ °ìæÿÔUİ=­Ë—™Ït±%ñvH‘RÍ
&ñ¯Eáï‡U<F«×¤SŠË—÷Óï'úlT‹q*-üóô?-ÿAº]µÇ¡!¯°}Â‰z¡ßûyÉşøíôÃÏfùí¿¼^HfÑ€–û•)Š†æ8ôñõôÃ‹]Òòú+.ÄêÅ„5Dn³¼¾Ÿş¬”qY^ÿ}òøıë/ î	vOL`âõ5´f‚i—§¤F°yÑç×Ë‚;íVĞ1ÉuØ3½—ü|Ä^{mö„+#®	
Q/\d<“àëj:µÏVf/î^~õuaŒ)Ì™Áëì¿âïßOZûÕÓ/»h²48D, å=®ÑQkVB±ÈŸÄ´«=D¦ŞÄ/ âcÒÀk
8IşóÎ‰¸¨yZ‡Ğ/FG·¼Ñƒ¥ ŒL±(TXh€7ÖèB360Ñ'm ²zùBÓ£ÚçÍŒ³44%Œ™B³ŞÆ4Æ:€©D0ÊÑ|_û2pš×44˜€~*Ä¨iM@b*D#Ï”.¹PÇ:2;=f…+‘ ~ürò)´§7zZÑ¶&ŠwÊ¤¶¦ÉÄäÈ:•ÊkÅ<$+e%¢3øKjEÄàCğ[ø”V~m¥±ˆˆc3ªµL3*ùÔì_f[ãHO1]j…K‰V§U<¼Äx¢5ô"Vf¢·i#“sº,—ÅE*jæUfXôb¢3ÚH01xç‹‹½˜Lû0,Ò0Í‡¤˜h”Ïó›Ã˜lõ‹ğk&ò¢u&cÇ´‡·“ÀL.ÀÕ×@”2Ğvy;º›^"¤	zÈtk‰Øêva(] B¶»KÄvw¬H_Nÿ¢,—ü‡’GıÌy‡‰ç{îø;¾çï¹ã<wü}´Âˆ°I£¾&¸\½âƒ²d%PU~Åê%¢¿)¢‘ˆX(%|XœXÉ£$HD¸éD˜Fˆ¢ÙCæÁÔÖüÑSh¡`HC¢1c3ÛL¡dì’F~M~u:ôqHA%åÄúHKXgc“"%ÁE"†¤ĞHÔ”ü‚ToCÌØª„fª·-Ñ®Ñ)Yx Í¯ŒÒ - šˆlÖ®ÈTŠ#KY±j‡4ŒÍ`Y—b…BslÔj®F$OU«öÙİúK÷“”§»´KŞ}ß5¼€
õ~¿*åó» >X¥x‹LÇ1F‚±[U$?!‘ôƒKyl?Á ğ#¦Å–S¨ÅRãj]Â¥Ğ¼;y(ëÎñj¨T5€OUªš `<Ee7Ó!`2!HFüj¡%e‚€	ÎiØÈ!‘ªn£i!†lZÍjo§>ÕDuĞ†YHCgfØ.Ò¯+Øª’#-¡°ªˆ´@™„°UmÁ´¼ƒ›†,&¡,Í¶bfõ`Ğ¼µ¥9V-pÒ”;ÇN…ÕVm¥V1ÿE9•Ê§-¥7oÜijÚº6½&Å‡1Im{×Ú™^˜)ãÆ¿sJÙ'üWãî!êŸŸñÇ–ïl~¦ïlìãÕÓ^ıocÃrPDÜÏ·¡Œ]k¡²ïßeõ+¿5y…¥¬£2 =†œ¹9Şë©Ïp†# ùÊÑ­?àık+'·‚¢mZ.­^¤¹VK€ÇèHùŒjó|}iĞ°]í‚ cÙ‹­B¶­š¡¥ºÜBD÷Dùp3m-·÷€ÆrPÄèw˜) ì_å Š“E |‚ì»T#U$ú©œˆ@¡óÏ<Hñ¹åF„Hy•LÜN³;!½¤:ËA-œÇZj4lbb6óvİĞy],×
ôŠ:öe‚}NGÅ¨%Íó¼4î5Ã"l%Ñ~F"jkAE ØzÈaÇ‹ıæ8=öĞ6¶S+úy6•ÈÓÅª>[#Ô–13Šşl¹¡K3ß¨îañXaåÒ±*ÇëZå°*dt'TóErÜVS©*NİLIşfjåc°õØp˜’ıæ#2q­i¡/=5f5õVú3déZ‘élè±²1çK¡Åò/¹ó%?[ßwÂú½\Ç>–µkqZöè>î¼<vÊàİÎƒ¨4µšª$18M¤‚*)Î-ä>•q1«_Õ±±ïŒßCÚ.ş ºîîÅ`g9(b8Vút¬xÁ–öh÷ä»7ëøÂD]¤Œ¶YMS©
Åò7«BeZU(¦ÖÀ½±ÕYŠèÎ·áæÏ¼nP2qîL7Ik>~Ú©½OŠ/‚^Æ*Ó“pmhxN]k(muåCYŒ]ñ4|Ö9,¦=o[Â4c.ŠÇÊŠ¨âp–eƒ¨š¿1„éU{—ƒì?W=ÏìôDp
vSBèCùKš<wë5°èY‰&t²FFÙk•œë“Ò¥OÑwãÖ~ÌÖ&ªs=|®x›RÛç)úpwl€+Ş1O½ì²U£Yr&}–F¸c\Ó¨\XBÁLÒÈÃåœp«d6°ğa‡r.†p8Ó
Ö|.n:O«nUZ¯z?kp—±w¯›;ËAı±º9F{K¥Z?è#*NîObëO»È‡Îtš3r¼Å0Ï§cBš!ƒ'u¬N0£–×?õtË=Nh`¤cº¨Ÿø\.p†gOíÎõ897óŒMØ¨
8!Í€ì±CÇäg:Ö™;ÙuL\õ^€ë?p^Ü%3×“¸êB²‹ëÍgÍŒíxKoLv)ôZ¿>·S½x«´°Ø²9uÆÚe}è(sßÒßšê¾¨v¹é©?³–§Ã]½As¤C‡™Vé£/¸Š öBÀdp÷ûQ!İĞéòF²±œüª4ŸKQÆkî]ş	–ƒ"ºCåŸUá›ïĞSÿ®¾P27€I±y+ìË¾¯çª˜SË?)Õ˜ÁÓ½/ÍË1µ>T`XmôÑµ«[@wçq‡‹2ãÓ'`O¤l¡â¡™E›RıaÍS 'Dó;´ùZíg¼)wÑË7¯èø±€¶‹1(v<¶I‚:²I^RçúÆy@Í.Æ Ø0cú°wºƒbÛómiÂ{8üõÓ‹	qGïÑ—ªC2yı,ùó{ƒ#o0Ü4{Pµ/Øˆ2ñâÊB4»ôöÕ•(R x§­fòÚ{ñùBíC’0Á…7˜O¥Õùµ'yêëË±Íœúº¦WÃÍÁY¡«§qQ¯¹¥‘
 [j-L|-KYAñT,Å±9ãŒÔ´ãh!Â Èpd[ÿ´+5!Ç=®Ô$»ÉWj{Mît¥6[#q¥¶×èWjÓµ¡+µ½w¼R›­¸RÛiu¯+µÙ‰+µ½FwºRÛh4r¥&'Ì¸R³ÆŞå S^©	®Ô¤¤c»Œ»÷Ì,ç£&ÄO/F;³
ìÈÕÜ¼k¹ŞÑ\Ëu¦º"…ÏwE
{WÔ¢÷ÿîŠ´?cv«0÷å¥êÒôŸ ÿmr|£
endstream
endobj
41 0 obj
<</Filter /FlateDecode
/Length 5101>> stream
xœí=Û\¹ïıõ¼Àœè~‚ì¶çìØ˜d²XôHöÿ:ºPç«¤.uÛÚötñ”$ŞII,Ö¦tL.şş²‘—ÁÈ-ÊÃå×ßŸşñ„Ï•	â¢­ˆ—şõéşãòw€›M:x«ßgè_Á@yÁ¿ÿõ§ËşË?ÿöô‡?éËßş?Íç£¾H©N÷[‚|ëş¼õó÷§?|3—xùşL”0”í7¤²¥/ßú£Úşçåûÿ=9xşı/ ¨p˜#À'€¯ - ğsH™ ºì>$V€Ù'ıúı:âVÚMÉà	æÒQ‡Eäóó;ÔK}0ïàUA^08ãxÂ ÜBm£…>¢{Ä_ÜFFE‘91ìsıgøû')İæğ¹Hä´² ±
8ï`¦µzCÂ%ößÈ°_Œ	Fo0ø®ú*PøeÖß-z˜‰şãÎ@˜C‰–44ÿ÷üBË`//øÂ ı…1€“¿àœ6Zf˜6>]ª¾Qyù‡é¥Û'"´5øÖÁd2Ì8.J‚©+¥Piaq¼„Ç.W0ÌI|«×Ä”Aâœ
VÔ*Ät!¤ñ
°‹Ö—÷Zä: 8
õ¿üúë“‹¾¾zÁW›ÖÒ´7#ÄY¡cSïÀh‘;eı¸Ï6åT4WZ(UôÎ{×3ÀÅ¸íKC™…@*SI0-¢‹•ÿy´ÑÎ**©‘"R„¡ïÃŠ>¼<‘÷#¹!/dæt&v8$`´Væévt
”9±/˜éJ@«¥¦<H@ï¬ËLÌüJ`„± /ï£§BH@-Ü>¾
,6îBäºÓ¤edÒ]_¼<©o'ÊÕæ%ŠHq JÛğmÚ]é"v@YĞL¦q‹ØVã+1C*b²M\Ä¶›`‰+øõéÑ‹„Ëş:ò{ò; <p<¾ãÃw|øßqöÿ=‘ä,fŸÁFX¬8àEçL "Î$ÁÎ$OÎÄw½'œA˜qºg"OÎ áäLğèLğìLøèLv`r&ù×ìLò«Î™dÕÍ:'Õc²>ÕùŠ+5J5$Â jt•YÄ:+S©!7şS›¯¢¢Ş¡È´ø”zõ&I!:o‚“7IÀ£7IÀ“7¨:y“<z“ôÎ¼	€5õ$øæ'I@-üÁ“$ğÑ“ìÀâIÒ«âIò‹Î“Ô·Íjó-Ì8=IÃ·©v¢‰ %½ÙJã1ªÆOb”õÄV›˜ˆQ70“|8§ñá4>œFN=O_.Â4ZE	[ía–ß	äíŒHo~©P“ À@+ ÌÁ¤Â	¨· 42c©àOZàªÁŒdàºsA°Êé28´+@nr 2¦ €ÀİD³ù(=¢x£Û¬ôN @Ğ§(,]
€`™RÄ-°Uà(è%€­ĞSb{àÎ—4>Cwş½tXQYP©¶ŠÅ‘1`[²ûÙ.,œÈÌ¸[ÀFêèÓ;3‘v?
k¼È doaZ¡È
s3¨‰ Íİ¤E±h‚mø6htµµµJ	<zF3°R%­jà^VÁ—<ƒÔ )Ò	2&‘ ¾£e)á ;e“V­*»³K€×AA(ìİx
&¤‚ÊÀd-0sSª]rÊÅªP;6Êƒ¬ƒ0İ@åa#Ìè–PŞ^»2l”€äså#i;3Ğv¤ñº³íå©ÆójBHæU@'€ıÁR„¬„*Âoi¾Œ»Egda¿qiDZğ[éü»2¢@ĞívàRùZGî“é«œ:DªH	ÊDG*i½)ú4~D¼á	õş:TLšzHÛn¥n‰A»;â6[Œı‘ù×ïO›µÁ'ÿš˜&?ÂÊ=	7¯e^‡sa¾
ìVÂO„×şoáçüş?ø³¿×Âë÷çøÇ˜OäyÈs~ËÏËûëÁ{üQ•F:2úûlëóûYÔÎ
$%=3™5¾±Iƒ·Q‘Ô¾ÄøtWÕ½æI‘±ÜıPÔ,¡>íÒHK#7í
Î™İÀ»ÅÆø>?óy†üÒ;?Äçyù|g}•ü„•A´c¹!Bt)zˆÂ; Ùº
Rw¨4ÔßänŠ:˜Mö	<‚À›¯H÷{3)7iEÔ±]ZfKç¬Ky`}¢ËíB„ÈÒ.:¿¥'UH ,Ô¡,ãu Ïİîé¬Û/Ka.!?>^ÿ™- bAµY¹_¯B2å! âï°;‘a“ÆGÈ¸ÚU)	1ZMĞ²eˆÀ`BHüº•„4×7@#‹˜øœI	°µğBŸ1F÷ïEãŠyÎÖĞ¼	ÏvÏ–|“}Mô¦ğö¡€ÃŸÈEÀ CéŒe2‹œqD_%§¯¯«•`‚“×Æ’™X3êùâ©ÑE ¬Ø$³üÚ‹­Â² 9À”Ê{ò²V¬rÃÂv3†4T{NF“üfœ¸x‡DíÈz2¢L¥W}-^ó:„!UÄ+=©‘TYn Ü±^_3bH¢¡Şø™xª!;7)ı•RHİhÏŞ(	:Z¼„Y{Š²)¦ÅĞÇ4Û\OÆDkà q6:Ã!9Yø£p'.‚£¶{€Ã m2’¸suŠex#!V¬íÙn#	rìâÆsSqXeÍÁ4Ãƒ~Ø£xğ¾à—e[<{ x #\4÷Yõ%ÃÑ[Gu2rlÑ…“>]a•¼.¾l1ç%ì—L·…¼tğ%XO‹/ûCÜ5ÇHá‚,Y¬82Ø™X²òæF˜ÏyDŒƒ&`Šz‚ÿ uS÷uŠSnı™éÂC0á:}@Êõ5‚n„—b?ÜŞEO^éƒB õ‚./î<H\MÒG×^I'?–ŒÎ{v‹³X±#¨ß‰ÂPNÍéJ,¹‚.·ÕCaÀ’P#ŸÙd€™F´Š'ƒu#1 û©e»¶±CXwÁ
vZİø5h4Ãå×/Şù*:Õ<VDG”€û#†Æé:o4ĞEsÊ2wÍubÄ}Wg,Å8"w`ûü|`^
ng¥şıÁY)y¹Œ‘›J~zÎ› B/š†’3.)å³š1Wx>šÈó¸Ì‚u…|šÎN5Ï§só,äYÅğ–ÓXås+¬b9rwã2¾«àècwS1+nĞSÜ€<Ä‘@ı—R­ô©lĞ˜NÂx:ÊZœ-Ç«ZÜŞpâÍo,(…VÅëš8”Ÿ½"±áØ›wxÛ½gT”2‹_cZãæÓ~~¸æSˆéKù+Òßi&òñtšwÁŠ•Ç´û³ÁÎ)²	ó:^½bóôŠäûŞ"wòC£r~È‹ƒ?š<Hî_|:'âOê¨Ó)-—MóØÃÑÙ¼|şÈ—ğÍŸÎ“ıŠ]=oÀâ“{œ?W˜ÎŞx©N§³CN’ÛCŒñü[Uíz}è?‚¶ ™³ã’°!gÀÇ&ÅÜÆ‚ÕÌ¡ìá!·2o_Ó;ŞRgxÿæbgtâ!òîÔïê+R°3sòşùÀÀ:OÆ}Vbµ.T*¤®ƒ™ÍÙ½¬YlulÌ©PØ¤‡eŒ9‹ĞXx ¯dŞÁF+ª`lÌ¼8€H`ˆñDİ¿dO¾šT)ñH±d0=ãğö´á÷–ÿÛSÂ}^¹
¤Iyğ9³CÚ~‡—×>¢Ä3ãÆ“À]õT*ÚkyœÇ‚MXF¬Ù,*AhË’`@·GŸ×BvÌâÔ°æ4Z"éWB2ëtO««Å*ò”;&^ÉÙnÓ¡ÕÉŸTú­M†Óœ¬kà©$ÏŒÒ,h§ì+ × .‘e$İğüIÙïîıÊ¯l¸4nÔ@åÇÊ“ñuõ(İA©}$g_·™}ÅQóÛg!,gë Şt’êH^	g·ËóçåóÕ6+Øc&ö´=”)¾ gÃüyùÂ»mnWqñV4w÷ñmaÑ"ã·ÂTÛéùş+Î¬Y¡l™³ço{^ÁÅCOŸpğ0&
§»˜Ã8„eü\İ•\K
™>Fw–†„À»Sš39È]ô•{ª¿"Es;cï
)búHO#…uC9•6›…€ÄÈİ'w^Ã_u•^áŠƒ?Û½}’ñÌP}/àí—Jî\â>U˜®ü¨menòïä¬º|iZFóåÜMètÙÆ¬Îemş“f3ìSª2ËXVË~hÊù¡uf·°&y>]ŠÉø°H[C>K5í€‡NoƒÈq_qÿÉæ(ït·Ë\ÉÄ+RC6š.ıX˜Î—eÌ‡ĞW¢.¬ğ`j§+"ye˜¯‚e±b³)VEÙ: «¾Ì1ĞÏ¬±•C¶Z“õÛïQûØ¥Ÿ÷¥”á±<ŒÔ>ve¼†ôMbåç<ÉY}	43ÓÊ"­»A\˜«N³jYÕÀ|&>¯!Ó;|Ç|uóPI9­@¸wÆ‘ZÁ¡ó0õ*ÍÚC®pç£¢ZÀt©K|7İôq'Ïş×w«dÇjÖ¦ë?´~ŒÅv¨Îx¦bŠ?r3¦6ô úóí¶Öƒ­æ¬ëGq'L,/?âêÛÅÕé;´éº7ŞÉ<öA»ë;ÙJ%VwV–Íü@]hIíæCP—Íe.›±aï©tÖ¶J×óß J	Â6B_Dj¢•ja-l+ô,ºF[Æ_®À~7GşÁgyÔ‚(?Ç¶Eø:ıîÛ:µe‘ÈÏ±Õ¶>ªñ5MÌmiSF@ooDD{2Pn:µl­û¤(öÙh]ş 6/¬1]OF {È
-(CkÀ½Ïbk.XA´!cÒ~ŒØ:’EZóÃ¡Ö'‘ ß*2;àÎÚŒ±²î¥¦^ôcXiúXQö‡Ô±ëÇĞÔJR‘~Œ	¼¡-3¬oÊX´-cİÑVi2£ø4ñ6Ì›4
¯hÑ¹9£‰YõhFiUÈ
Ö!íÓ.µ0-½ü$6O×;KjÛ?‰Íd›–¶gÄâ+Ğ|˜š´g`Hí,k³Á¡İŒög¬#kƒCº@í…ØãRÛ&R¼kEJamÃXyA{3V®ÑöŒ L­iÏhâŞR” –ÚEöíš:KZÒ1Á"¡7^ ¬ïÎ˜ ´5#UxO&¯RêĞ¨%S)„õæ‡õgÎÖ‹q³[\qÿ{ãÀº‰Á ”¶À›ÅfÄ€3¬”úó7ÚZˆ­Bïûš†‘¬7Qô”Nbòîû©[Êû8ò S1ìí	î+úJ0€·Ä¨Ïy=ÁÜ­À<b¨So†;¨Xî¾±&¸û¸+)·[
óºV™ØRç­™6Û²ö˜ödEcÖsËæ~æèı—ã<$GõF¼1ë\‚70{ó¹ÿ)Yâ^_MÈTk¹6Ô4„Z)Ã´rä÷PD×Sº–¶%ÇPŒ¢|àµf«‹Ğ›È²mË¢§ÔÜûüÉBdÃhyˆlS‹oƒjRj¸ÈĞ1¾:ñŞšÜ–DÑÇwÕdn–}½8Õ=6}şçÒd‚ÑjM&Sß—AKáè°1ÖJ¨÷Òb²ä ŠÖ¾£“åÑóçğ² E<6„¦-âËÏ•¶î©å;^Åü{jõÙô-³bUZœû¥Sô†Ø$¥"Æ›ÌÊ¡™oJ—$™¥GX]kÄDŞ±%éwÒt‘¶dêÕÛıNâ¾¢µÚöìâ%¨?ç`ºÖbsöı£;2âŠt\ûMzyàĞÊİîT"^²ñL›•ôAï!Üa˜“&}ÚÏ­—XCÚaœõÉˆ»[ŒxµAO£åÆÅ‘!¯4OP‹£lè¢oïæ•Å§Ë·@½}iAeu÷&ß–bÑ”¡	sõÛQÊï2³*³2±/g¾4šü+å[Wß°‚s•¬Â–¬b…»Õ:l¢(y˜Ë…•ğ„Ó•¡rV'rÒÚ°ZKE7éîß$’ÌGR‚ş]ÛÃSA¿Û6¦ê^"ÿ¸×[h×õ»pâ5¿ÙĞdNïË×å[×jüb7«½¾à·û]6W®”°;N0dº@C‚ëÖØ­òQßş6jHrrDH†lR!D8xÌ ªÇ¤¼27rò8Âk)	¼l5?¯MÍHÑ_âš’`÷Ó[2õzıñø—ª' †n‘¹–k'LŞÅ¹ºJiòf 2¦4A/RıuiÜ*¬­øI½(láá–î¦F‹îuãÖw…å½o>ÆiÄîgætÃoÍQát›zçô=.§Ò…6h¿jn¢˜L0Wò]»ªH‘5Œ7&%}¾ŸÛš!/<hª!íUIYçÂI:J¦/I@ñİÙTSvßğôOe»´o©ö¯S\áÓ»Â×AÍ¶o³KÕş´K-áz´ú]œ9y5dZ¾·3ü©„Êì	ÓâÓòÃç¶ƒ-Å(š4¾ˆ…®UÎÏË³ç^Bó]¨ØÔ­$rèñ;—M¾í ,}üÙnFËoÚÔoS.Dq_Z.ôF˜·r!Šùâr¡·Á”QÜ×–]Gıár!:í•-Å¼•1_^.´ïV.tÀû-Ê…è+wéÜÿLÅ{ÅÑÃi²¬ÏWÄ-á¶#ë†‚–‘+®èWfçä2¿!·&~µW›ylW.²k´¡ÃøÁ‹EóÁ
endstream
endobj
43 0 obj
<</Filter /FlateDecode
/Length 4597>> stream
xœí]Y·~ß_1ÏÜæ} A ¯VòsbùJì Øùÿ@ªx{¦vÈ™Ş•âìÊ’w¾i’u³x4¹)ÓÏIÀŸï6ò1¹Ec8}úòğÛ~¯L'mE<ışÏ‡¿ÿéô+àf“õ¹†ñ”'üó·Où—ßyøşG}úå?©>õIJ¥°ºŸ"ğÑü<úøñáûæO†Š…ò¤ıæƒTö¤ôéã—‡?¡í_Nÿıààûÿ8 Â0{À'À7@‹¾) `s‘Ø “+}ÿñ2áVÚMÉà	åÒïQ»Fäòó'öÜK½˜'8BU§ .4QŸ/Jí¥…Ş“»§_<OŒŠs&°ÇZú¯ğç·)İæğÇœ$JZY°X’wPG·Z½¡aù7Rì;0r7¥¯Ú¯‹QŞ¢‡ªè¿Pî„:”Ø Mµ<})L€ŸñƒA	@”?áNø>cÚøº(T{Pyú„ÅƒôÒ¥
UÜ¼6|¦`ÆéxR|])]A¥…Åò¾v¥x€bNâ£^{ĞSƒ´P§‚µ
±€.„T^uÑúú¬E±è *øPAt€úë§}ûô?mZÃç†!â¬Ğ‘Ö‰`´(¡}Ã¦œŠ†ÒŠ ÕğC¹BĞ;ïİ( ãÎ/‚JR¡"¦Etq?¢F;«¨ª:5D§ˆU­çbÕ >?çAqÈ©9ÎÄˆFkku™^@Däc	´Zj*„zĞ}‘bÀù±"Uüu§
›¨…Ïe›¶l´q'¢ÔFj-™G·ŸˆÁ´Ç‰eõz‰ıÄb;½İ´OÄ(ëİWº”ˆSuyÿ£¢'¾ÚÕDœº+”Ä€OÿÂğNù?Œõ÷p@iqŞ‚Æ[ĞxoAƒŸr’·äœv¢E§Œ£ ¥I£HÂ´	r‘@Å‡(¨ aZEfh“1ğ›¢ˆƒQÈYIà>Š$ğ<Š$xE2˜¢HùµD‘òiˆ"#vÙë$6LÛ'öŞi%NÑ¹"D@œ­«{e*q`"âë]U$*4–¸‘´Ş¢H2ˆ!Š âCI Ğ5`´fŒ"€Ê³(’À}Iày4-$$	“AºAG’ï#Ik$IŸj$)†HÒ§ÖÕê¥–Hh VÛè%æ]ù¢@D@|¦I‹:W“+õÃ¬‚}4éê¢ÎİKbÁJ
ò<Ş‚Ç[ğxCğ¸9ñÖ÷3ÀíMNŞì¢	b Ñ1š İE#ÔiM;‹&Â‡]41RŸGA-c4AĞ…¸&ŸE“æh’­Ñ$£IÆ¨m¶:©“ö©Í7Z©s4®¨#P§kÂ"ŞÙ„J¹ËŸú|SU§5~ Ö[4I1DD6­i,I3R°hõI Ää›Æ‘Y)÷	óû(âQ‡Dšøê¥rOøî>
nN£GÆbÈÑ#}ªÑ£|¢G{œXS«–!€Øh¥´›râ…<á¸»Fq¡*AâkDÒÄ-›NˆûVÕ__I5Ş‚Ã[pxÿgÁá§ÙµœÓ¯ ÇMEéPK€~!Àw@bÎÉ*f†¬,´`2d*…D>mRÁOÂ®"2 ™*p	„Ã&5˜¬Ót ,ƒŞ¤
À<LmÀìñ<"JßATft›•ŞÑâ ‚íDaiC ÆMIG¢” IÌş;ı€aF_Z*Œ`MY+–ÄöyÜæKÁÒ`@L&°Ğø[!¥‘-=NUêd˜•?ÀÀ°PUAÉVyUµU[±.ÿ^W¥¤+µ‘Ü•ß9ÛY“¸~í,ò·ßI|öBŠE±‰0›†ğd4	ÄÊaX§*KY•@$7&Ÿ@ek™@‚*–˜€«ŸöÁ ÔÍ–2˜ÉÅjLEk7ÔA˜¡åÍfACSÊ»Í¨dM„(å!Y©ú•Èª8- o"I¥–äöù¡— ,®,M ††[(Ä Î^i)d6S¨.ü†‹³‰½*‰‚åµİª€@N/)]Õ@iú¢Ô4Í²©TöFÛ©&µ°Ô¼áRwşã(æE#ÒGNi¥\â*Ä°Vnp®İ@w’Ë-ø¯µB˜wğ	0ñŸßÃ_S¾3ù3~Ô´çõûº®¾E' 9³ØÇĞjÖíÁº]ãœ*	z7
<} ®lJÀ&øæªN¡…Jk~:tğ%p=4à ª#GÕÓªAB¼6D\(
ı¥ÂTíöQpÖNúíZG#è9ÈBbİt3Tÿ„¢¾&fè+ˆ,æVtRÌÁ"æLêÑ]åÑˆ<DÔhÑND†ª³ES¹mÖBB‰¡ñğ/„bld=ÓLZ¡U#Âa;i»,Q2¤0OYÊéy|&(Ü×•¿3>×…åÍ»ïûP´%Êÿemï aÚ’ùP§,Ï
{öüÏõÂØo”u“—,2,–kŸ²ü“œÍeY¦ï‹|Ñ—.õÅ^Î†şLÓc’û2Ö7:“ã(aoNÌ¦îá»êÈª°'ºÙ)1¨Ç`’”ö?ŸŸ‹œ¢Å§N¶£Šµ&R°ÉCÜn%P“ææ¤åT‡¨È¢ì$™P¸—àµ’¹Şô$©0Ò]Pl•tµaÉ*ùÈÈİ‰”@˜<Âho×«Ÿ“„{ÕËÉq&ªVÙÉ˜$[Æµçu¸Ûç/…²òŞ:é“¬Zÿµ¶7=Iª¿;ÕZ%7e:©wîOí¡ÑåNsb½n‚pØœÇF­91xi^I-	´‰åšm˜4ûêR@êlNŠEëo!v2&É¶ê¼t¨±“2Iº_ëé|“†Kó–îB¼_({QtşÛÙšCñC½Ş8™F’©?èmMÒ¦îÿºNÉ¼{s“ä™óîíˆñYpû±°±„}'./„Mœ{1¦Ó¦½>á"Óis6ä¤r]£-´^¯ˆÙ|8 eu1MÎ¥¸71£á#ç¯¬¾D…tGL^áê]†GÏ¨à,ª¹Ë"r\0#n:$=ëEÎ³æV¾—¢OT%¸ıËGƒÛæ…yióìM€¨Ñ‘º›E¼ÌËptõáBRŒ´¸¬ËK™PVƒm9ò–dfÎ@–d#Ÿ.ÃYÓa¢uµ/²ƒ¹×’1ÿl¯eÊRBAE^ú«s1Ï×77h°")Êó@iôQ]/QŞB•bÓ„¤ÜÍ´Úò^$Œ¢€iuUÚV! Ô7!½Ü#øÍ½&UeEÛ-
¨Ê¨«<pµ•9pÃÁKÜ¾/´Ê¨q!ïj7.ØKFñhgô
t…3Y¤µÉ•Ú›ı…/B‘wP mÏmÀŠ‘ë¦: #º3;¾ĞW[¢ÉIi#!ªéNö×•gÃe¢øš|Q‘S`Nv‚«“mF.œ¸Ë¨}‹lÁAMæÆ¯6ê3ïMøk¦vÆrB"\	óû‚+!>şŒ¹ìg|3ì±ò`í™eoİØLå"(PŸ¼Ã–}‰%v™&Ş•¨  Ø^ÖjĞD9záÌ®Õiƒ÷Õ"ƒ!à^´BÆÂõª–9dè9iá©ª	Âv43lpÔ¶ŞÊ¨Šs¿AˆlãËÖFİÒ’Nz’fFèƒû™@ØàÂ¯¿»4ÌØç„Âw4±mKFR|X¥q'Ğ6Şs
§üá6´ëT­ËÇT>@ùàm„åc½*ÖÜ,'öÊ¹€¸ê$áœö½ö²;)iì„H–½ŸÕùzã¬Ï}Ê +Nì¼HXƒ[ìåøš+™¬©£ıTÙƒ¨àÕDš²Ş.§/|ÇÏ%|A]ÖÓüŒMÃj?`$Jäj†ûŒğ™,Ë—Ù,·Í+œåï±TúãÕÄ
±„$¨:{®%Ù¤2"¼ÖÄYËSË™Âê ·NvTÈöl9®»æ{š‰Ğ|’ªån|n4ÄÄ@™7ª2ÓûÂÅóÇaQ”ÃíöÑ{fdHû¿[dr`âÏú +÷+ıµÛ‚Ö‰°Ö³òu¾Jæøª¦ˆ q"÷•ğ³Î§ZVQ¼•üPKD'Ôtƒñ°ş45fâñº²–ÛŸKMÛl^â\¯ÉõËƒÀq¡ìº®Î“ñMÜîKÄ&ÇCŞx`š45ÃE§×5Ë!Ø&¸Ümµé×`{=»_µñm¿ÂROÕ4<nÚk=K§-×ó®õ¾Mïœ¬:nb/±<±·>OÎÚ;ùÃ¥Ë¬fœZ[ãä¸dò——î§ïÖóÒ+	ÏJ^ºîË:ÿÃG¥z‚÷üÚV97<n*@FNg“®Œ~¯ä²¡mŸ¼ÖŸ1Óç¹O¡kÁëCì„CÓrÂs\–Âhv‘}9±Ÿ›çŸJó¦&¦2ª×™B^]ê>r$ğ5“ÌWØ/39ÎÖõøå!úYÊòdñÜ®<:hÚ^vì†ùÁõI=Vîë™éÓ/Ë›t‰³»Nî]íı,X½¾Ì £ÓÈtåÇNÍsİ{Ûõ'ˆ˜	Ïà²K­Sµnßf–ûóçüŞrÚx×6H„™â·¼ÍàùDSÊözÓcñ»_ài™,ÊÜLd”¬÷‹wLë³¦¬…p	7ß·ŞÄúFÅå´un^Á1Qr*±âätß¤ÂÔfŒãv,×tdR¾< ZŸß‹^Ã¶U‹š™øİz.r¾J¿tÜjÚzgÂŠ„ƒ¬‚q—Å>3Õ8Äù!>³³d\´Úé%Ûkˆª6°ß”ÃÚÚúNšõ¹†å· ş(cÌõ­û¯ğN[¯ñõ`5|‚w§3oï7ÖgYTË¯–¬›:?±ŞW/ËöÀMúÌ~‡õ©àõÙñİ»Úç/ÇëXØ#¡òğ×Ç´-o\’FÖ§S×³ŞPØÕîWx—Š¯_±':ğµ¬×ˆÔ·okÖrœãS1f	‚s¼ü”4/”|ˆwx O-'Avwï`ú|«–œÒõH'1>¥Î¢è&|: …”êiâæCP§Íá×fêKôgàs'?bÍ^“^eÌ¿[|İÿâÿO¢½ÅG[âaõtúÖ:,ÏëÀÃ Ëù=xA:å‘Ô‡m¼ëõ¤Wé?”úC)Ó^¥g®¾œ«v4˜ªï±ãÅ·.ÜÓ¡6º?p‹ØzØ[ŞËşM
Ö_Ãå«bSöåén7Ûò>©ÿ­é¾õÅõ~W³SË²¾èxÜÉú;“7ìÒàv´­oºaQ†]{YßHô2¯…•&V_\ =Òx¯dˆ_Ö—R¦ŞB^[+ú×q.ì7»ş&ç-×¤háò7ôªÕo’è×e(¼3BšÉU)€Aê-½Cá…ÆÚñ¦@ñ:+ÉE)
o‘Hg¶k?D¯Ii ½&¥ı¶‘ŞF¿—„RÓ/0ét÷‹N:Ö.Úh`ÙçÕXA¯I"ÔĞÚÃ{ó-—r@ñ¾t`e0aÁ›@nJ)ØxUJé])½t×Ao¥k‹ÒÓõÚ)ïúï^°ó+S´0¢V•W•T
JÜQ‡FÒ.× )hví…×Ú@l	ôÖ ¡ÏV“KST¾Ö¦ßı¡Ú=7íU/êW‰Ôbí¾Rw»˜d ¢]aBÈmW¶Ú}(zIJ“½(@@R;rQ
`á(MéÌÃ·z¼)P¡cÉM)	K-u)hè2†[R@oH!¥ªÈIåM7M‹„`j•±s[ùj×¤@çĞÆ“6íå!*®™Ø^ªÖ2éäºeØú\ıö†úíBı‹CmJvËk—e8Œé g"Ù©1êg"×[êÁ¦P-Å~cí…3ñ¤lgâ‘:çhĞí¤Ş¯n·Ôÿ[C—ì¤&úÈƒ|ŞB&Ú GË’¶^úäÄù)¶!t]œÒ±’­PU™*‹¤Š^ÑŠE¥Ÿa¢„4
•İ¥,ß×3?Óï{ƒqDMNôCŒç„¾Á
endstream
endobj
45 0 obj
<</Filter /FlateDecode
/Length 3672>> stream
xœíÙ#·ñ]_ÑÏÜæ} A€Ù9üœd€|À&vÌ°óÿ@ªx©–Ä^±å²³Ş©ÄnÖ}²åUH~~XÉ[§øê¹÷nùüåôë	?Ê±Ejæ—ßşqúÛ–\­ÜÀRïĞ¾ƒù‚şòÓ_üöËéÇŸäòËÂı¬—çBàí~†KãXúéıôã›Züòş3Ü(`ÈiWë¸Ğ‹Ëû—Ó“úOËû¿N>ÿû áz€ê6 lH îò=8 Y :^â@Å›¾¾o#®¹^w–`Îm¿‰è6á=æç+zê¹ìV\BT8¾8`pÂñƒ§ëWƒPëÕLöèöø³ëÈH&(2gû”¯ş3üùõÄ¹Yş¨…[½Âİ= $4è­ ş¸SÕ]¹¢áFñ¹øÍ…U«÷æ¶Ğ{çyRãÕ[¸ı®;Â=[5biùò%½1Š›åß(4C €¶q.0RI`Rn 4‰²)¹|ÆË·ÜÄªÕJ#q©÷`9	¦Œ‚{r°x!dÂ…×søØ¤Ë%2ãR+-ğ3üÆâÂù4Îk¼^ vÚæµÙ@ CY—hùåç“ñ¶¼ûÀw«”\ÕÅ1ÄIï‰@¯±íşÆ»UáÅZÂ¥
ÖXkZïAuW”YäN8ÊT„IæoøP%TT2UD¦ËR—e…ø8‘õv,ä¾d”¡˜×ƒˆ+ 0c!$R`Ö˜Ä½Ä(‹2$ÜÄ÷p_Ê÷ ’ÌFf¨’j!‚Œ0®Nï‚²ÈòæãD”¤,'ÚTnK @t4cZU9ĞBP\M£°†˜Pæ ±5Âib–E&Ä|³èˆ­>ıİ„[âèòëàX@DàY¾;‡ïÎá»sø¿tİ—Ë@*Ò\…ç€/èZ¥Ú¿¨ˆW3t
|’«°ÒÃaq§)gaKÉ¼€Ÿ€SÊ!7¸C`TtÖà†¶x—Õê°w %
w®0´|–á¹%P”ª7«æ–®ègºìÙ3ó6B2à&hÁ`ä»Tú¬p"\ •k-Ô¬Òú¥î0»j´ŠŠÀ sïx¤1ah³xV&
Ìg—Ê‹ó»™oŠË®×W9Ô}ªÄ(FU¶÷ª•Æ-BmDı;>c>ëW…âÎä!<U(˜œg`}‚Û^Ü˜ƒ’`êKü”tÊÛ`¥Oƒå's°@-œ V€N>*X!óO
V ¨``¢´£±"Hî5°…î#¬Y•`¾EThPPÔ¼äÁqTÌf„«´2îãT¯—†ƒ¯0YŞ`ÀAk5Á`PO*–q¨]*–iX4£¥r£ÂĞÊ¢b
“ë³(È6EfBEºu¢1…Ä-Ê¶£[±$Œÿ ¿Åü©…Ôò,T”>ÁpiM©B˜õ¹
W¯ğWAA¯ão|¯!R(—`Ï¡PÕ 7ŒV¬«Ö[ÁÇƒı W}@¦‡åFÆ9\ƒ‡b2PKğ	›€ÇÑ²â¤_Òo>Kx©—ˆ§2ñ³ {-ø°ênè³ÀuÙ¢ÖëX‹Z×k‚*¢‡leŸÆXÎoìÅÁb” ŸÙl9ˆ"èõ®õuÇµl–iükâoEX€ë¢6))´² +¡ÿÕ¼¿"!&C@‘c°‘xJ›"ba3ÔA«5kjİ¿ÜKƒU„££b?%ÖÚÈî)ÔHáÏY÷ÖXö×Ñ#•¹DLª‘Uâ-şBO(ofËFa<@GO&À’Œ^gÑá0³>B0
Ëæå¹`Ä+±Û·j§S‚(pNĞİ’ÁòãÆ†dR8’yKáa–Õ`¢©X¯g†İğŸPCbz›s»Jï$ÁËÄUİp^w3Ò¥³}„	 ²¯€¿õsBĞÍ$j„0ŒòÙ­TÇH3õîZeòÎz…<yoøä>c(jÁ#è8ƒ‹f(ÑäQ	7&÷R[<gKÌ¡AB™yNĞ :(ım™vEh ¨L¾U}.¨—V¾U>LÑd’¶t–vHìü³nV™²Í”{Û÷UK
òë† H&i±Lq"¯ãQ’–^‡5~£2Ìkr=bãÚ¢¨âVü\ê^Öƒ6â$5r‚BPHDñy‚ 9!ÅˆtûªUËÎKÇUK+l-/kŒAâìJ¶î+r‰©’«·Y˜¯=ƒºÅ,y·Â­N¸›ôsCØ!U°-Âp–òŸi&ÌÔª¤íx,«û¿áëKµ^•ò‰Š³‡²vFé•FÊÍ	†c ö%åVßLÊß*…sóÙ‰2¥¹o%éÌ-?'—PJğPÃËdã*]KÜvVâï\½fIğ‹~’/%§íˆ“«İW XoÁqîãRdâ½§ë¨Âê²‘ÒŠ>°ŠV%‘÷Eôd"GÅõ7·†è›ÊêXhz
”p[á[[Ğ˜X~²†$ìxÎéÃ–¨õ++å„v5S¡kŠPÖ<W²Š¤aeÖ–§”áô¾ÒÍ*[TdI%q%òe*}`¥Šk‹İ‘Ê9ªb¡’«$(ÿM4o*ğ¾ÜUİªè°ßäü)cÒÕ¥–¹°¿%®XEzH+å·ŸÉuìPõå%¬äùîk(ªî–3¬MŞKqÚ³•Ù˜(”Ç$èË€mOÅ÷­«tã—ı¾ççIïJï+Ùˆ6eM Óª¬=4#¬ÊÕ`rœ¥Õhgx2§#¨±På|q†ıOqVäØÓF-ù4›we»©3Î–Š‹3ÎÔÔ'ÙtöŒ³“Ê¥QÚzêŒs¢lèŒ³“Í¥¾ùZœ/ÇÉÒÑÌ\ hs¬1ƒ2äœ(:äl	™ƒ´gÍo1µw«Li%ÁgÌ³š[SÀi@Ÿîõ\¤¹VI8ÌÿÒ„l÷v¯¿Â¬"»õ–ŠL§ÉPé	mö°Óç¤çSm=ÏRX´£{îŒLyCªizŒi®{Xç0Í-$¿Ïá¼²öÎÆĞ;Hd×»ò’ÜRo‰ùßR`¢…•ŠÙ• Á§,³™ÔmÌ!¹lÄF€¥Kv­Ğlôû+„IiqÚ3Ñ†ÈÎ-Ñ§*ß¬áõKİ?ÈÜ¶{l·á>o­ÎŞêšpÏ¢SÍ¤ãv³’°uPå)Ñ-”w›‚'¬3DŒ«7pcŒ}İ8ömçzIü×Ám¤¬_ã¤”plÃJuÁ c•³}Šu™–p‚avXdj¢s^úÔ*1ulÔ°"|ÖØ?	BÚ +Ì®enÆ‘è¡¶ñP«aBŒ%İBŞá1V1pğºİóŞjË˜yv¤ì‰°M¿Œr>ŸüîæÃúæèƒ’å=‡‡3NnKa¦åíœór$ì;=´siòùSºaãT€wÃØÒğ}&4ÅËğ™®¬Úßvš<à#³”á `œ½±je>d¤”ec$Ê#lËdeE/n‡wl¸DÚ%²ºˆöxjS›kQ‡¼È÷§×_Š*6#Í•¾meá Ëå#;ÿnQ¢’wh?Jz“ùtË»ƒ”.´”Û+´b='f¶oÏG¤H¶É‰sz†)×ƒÅÙ¹ï;÷Ã#óZí{¾Œnk7Ül6„&$äµ¤„Ê°3ŸÃX—ÕÎzĞ.O½«;c¹=¯T'½,÷¦×€­Ê¶p’µC/—ü©,çŒ¾ñz‘\¬ßW%
ŞT‰ßÔ‹ ÷ˆ!Ùnæ«£â1C.ºéä!W/•‡¹fÊ†¹zÙ<hÈ5[:dÈÕKçø!×LÑ!×#ECä#Ûîy’b;æweéådbëÈ´¸í—ÑçNM…iøº;İu¬¤»•äÃ¼¹’ Hô§n7=;Ô:wÇé6ô¨ta «í­œA±&­¢^´v·G2FÛ!3¦…º|éÃµCûçzùÛ<êXrKÒF×º¾Ï×ì-ïÃ£¡[ûÕ3â÷?£b…½Ü–œ ø¥4dæPğáöÕ‡-¦²ÏóãÙçyÇ¾{èø3‘Íæ#ö%ùyÃcFAy^ïtò™LUm¶èæÖ(­Ø%KöGbn™P<Gx>Ø^!·EN¸>÷‘\Õ]+ 6¥ìLg$/²Ù4ô!¬©r;&®U8‘:°¢y\é„ÏXÇ9<ÙîşÒÉÖ<¹¥âØÒ‰T8dÛ)Å“‘(:¶x’[êpù$]Îü;ñ™¢Óg²x4Ôƒ›W<áÌ9>=S2áß#…'¤r­n{»n2zÕi
C°s¿Æîu¿ú÷p¿¦9—„É§ˆZ7}?Ç“¦iİún…
ùnRt¨ZIüjĞ–9Ø¹KôZB¹8[6áçìG×5–™ó3}×¦€Ùã™.ıW2!¸gá´é—*=ï$àı]ƒ·¾ßc
%Æ¯ŞÅÉ]İò¦ÛÆï”=CN[±½C†‘œ™çoı¸P*ÌsÛGÊæ3™„5¥’»Zı\®ÚÃ“·B0MIAaLš¢´.¯”ıÃÛ[òìÔu…j^çIay£xİ÷Ìl‹W.j¯¸8ú|geë TéİršZİ²¦ßV×¼:NŸ½]ş¼gWs¾d°ßÏÓ4_ïóRéi¾k¢;Ïr•WûßÇƒ*{ÅarOíê‘›,™áßëÁ´Épü W==¿®h>¤½Q·›ÚŞh©xX{ƒl;»½ÑÉåQí‰ò!íN<joLiotÒyD{c¢db{ãB¡íºí®öÁ¶Èÿoÿ_ 2
endstream
endobj
47 0 obj
<</Filter /FlateDecode
/Length 4758>> stream
xœí]Û¹‘}ï¯¨ç&Íû0úâgÛöÆkÛÿ8‚I2³ŠªLuÖìjİÒHê<•É¸LVÌbl.¿.Š~ÿ´ÀerzÉ:çtùù—§¿?ñçÆ%u±^åË?şûé¿şãò7Âİ¢İ×Æ+zP_ø÷~wYøÇ_~ó;{ùË?Ëx1Û‹ÖÆğp.ˆâ[×èÖÏ_~óæ.ùòåÏ4PáP_l\bÒÆ_Œ½|ùåé·JYÿŸ—/ÿóèó/º`Òp[  vÀª¤ùZÀvÀ¯ä¸uĞ×/·÷Ú/F§œë¸%b6Dô–óë;¶Òk»&wÌ5I_)¸òxÅÁço?MF•§•İ²»å_}›«2s¥°ÎÌïé÷ßŸ´Kà_î¢£_hôL,O~kHÿFßµûZ‚‡òÎeE÷ëû^lÈïSÖÕ—i(ü›»i£Ï\F}ù¥^§Ãå+_8ÃTb;¤ß¬³ºbÖåÀ`ÈÊô•³—Ÿùñ¤£ë€n‰6X¾5gŠœŠ¹àhLMoŒm ]8~^ÓÇ¡>né± ùÖh#é³‚‰ş!Å2E“rCÊŸ7Ìí^Ïj'Äp15Ã ıøóSÈ±_}å«ÅZíäfF‚'sâ˜fBé‡œLvÈ+ƒŞÒ/”ŠÁb£BÎä:F;Tƒ:™„JeÌªò FŞ ©
H6u`SÆšÕ×ÇšC|}‚û!u\`Üƒ‚eß8Xy%Ğ2. R¼É(}ÁbU{UQ‘mÚäkõ^ «âjÂf¢‚:ë.`ÈËåézUœÅö‹¯Oà$ıvğ¦>,80 >Ú8W.²€ÃƒÄ]5BMƒk iËnßf:ˆõŸŸşÊi"]Öÿ8;´ŸKb!QfùHÉá#9ü[&‡?XCÔuÈ:B"«ölƒ‰c¶ ¤¬o0[Ìº4À˜rzL„zÒ ƒ\Q FÍ1fì(s;+Ú€±¤Gk1Fa:f‰‚z¦ö/XIõÇš$êÕ$*†Ø†D_âèÔMtü&†Hc©é"®iCSôAÜ,ƒ±Ş,Ø²Û¸ç†bş!70²Éj«2P°ìı´›ÜP Mn(ØUn(h.áÜUI˜Ûä‡]å‡‚nòÃŠµüP®Z~¨C~è·ƒõaÁã€ğÍÆ©xp—<$—è*‚Èiš„C0vÛ@Ğ6B„Y@|¤„”ğ‘ş-RÂ÷/¼–‘lôc ÄmsDÁ69¢`W9‚P»Érô!j1º’¦©¸‚1Z³&cì*It“$V¬$‰úcMõjHC7lC¢Ã
qôìÆ&F@cEäÆ¨j‚ØkzÄ c87Û`Ô7¶¼ÀV–,Á0f	B¶Y‚¡m–`ì*KxÍ¾m†4Á˜·CMU°H…Î˜&|Í¬M‘tÍ*gŒXØäF·9¢`=GğUÏëÅ˜#ÚíèFmXt8a ]³±
ÌÒ ›‹ÌM96M‰`¢mÅfÙj>ˆïC‹†„ğ‘>Âÿÿ„ğÇcoM.{â¥‡ÉšÇi2œçô'«××&¼KÕ`W`Ö`ñâYÑrª€¼ÿV$EúU@Ş*S¼p&Né!tÉ¯Øjòä¯+˜¢âÈa\ã€A]ò¹Ì³³…égOke‚@r¨¬<#0/F“eÆŒU¤\r)‚@ÍÑQÜ¬ª)TXôøQ6^Ì1^„”3¼¯dŠiWÎØEGrÂUØ*€£jÄfŠPURgŠaSÁªR*–uÑuÓ  lÂ¦ly^¬"tÄ€È‘ØZx§oyû'{œQüR™SQê'èOVYŠ'Š˜ìbiPçd!W@®«Ï>aÉÚxSÀH.àË\£ˆ>‡£y‰Êód£˜÷TnuÕ„†C´:\Ù!7‡ë0;ez›”†0”ƒ=ég fbXH3yÃ—‰”9nQ3‹ëi+Q3e€
‹¿>É6siiba«’²œ…½qÀ”#g´É®Vî"ëiëóEÄ¤0!HÅÛšF*Vl+ê”Øéš†ç›E€L·°Ó,\ƒçtánxSó´/„~-½şÅ™˜WS#"5Vy«Mó>0¾×v%ÕªP_l»WúCÒx¿şË×f—*öL¿Ë_ÿõ”Ü[}F×ûêıô±ò¯í½øâXy¤ì¼®®Û!‹kş§Ñ)lªO4| 2ŸW–ˆòp­>u²;44#MÖ"Ï5~ ­_Ş)ŞD"ûR¨ªR_VÅ"å}ÿ,êÏ=|¯<”°'òäU÷	ã,yœ÷Wò¼Û6.ĞºUóBúW•Ås~,GrFë'Rn=–— ²İhş½]S‚áX#—ôiõÊâgI®)™Æªèr¾æ½†ÔZ/z;j±£®ÉJU{¾%	M/9¹ÕdPwl¨i’³[>í‡VÑßç'm­WK—{ª·ÏÔç´Ü}Zêùœ6-ÉWïâŠzyÖj‰‰æ* i_œO«7\Û	Ö_Í"Š7ÃUcŞ~<åuZ±(oV½ğ¬e«>Íª{ırS«u·ÏyŸÅL§Ø£Î#Åª^ó=¡Æ@¨³¨^íåŸ¿KÁCYF…e*ë©¡,ó°æ“¸§"E™¤e$­\Š°¤÷‰
|ë\J2²Â¢IX‘ù_Ø”rB0¬ÇÅrLP)f„”=È‘HÂ»R"#b²ôT4÷uD3Å‚ÃBÌXš7,-#Â	\—ÆwBKy…aT5Å”¡1A±Tl!tÄjÈ‘ØWx?oùÑu!Fš°ÍÇXÈè'¯¡
|ÀÆ{›`!´¡]Xƒ*HE:C	Fón+0Á° ë/x¾0@§:C½"Ö{å$ö+@+¨¨/Bı5¶“!Œˆx†#Á|LCíe,M¸!j/ÂGQ„Ú«ay¨½ÅÚo– 2İdCİ¸À:úKñ†}Oùå}È´	ä²eIÂSÄÛW‚Š:½…5ë—Ù²3gnÎò
fær_Íæe–İŞ7›bÅ3Ìğ8yÀ_ëlmëLådfic–Ïf3Kã³İdõ\Æk?ûõçu•°g’ÚèÌ¼È¸|]êB}ıYYËš»èä¼¡c•ğ¼¥ƒŸùxÆÊÒÛÅ´BxÙµJŒ:»ŸÂMV•{Vö+Š¢wUíşz‡>–úÂÆN¶½”?øçeD¤e@^—ç@ÁoÍŸadoZW€ï­…lX¨|]‹å¹'‰D>{K{÷ªZC)¾RhÖ]nı£İ@(°şÚ®ÀY:Ü úÇ¹ÁTïá
ÚŒDï:åfÖnŒºË	²{´¿™Nw‚NêN0ƒççsD¡r÷wÒHîùùWİ¾Akî±~ÒöÁÖ
;®Í°¾:ßús1Êìşv–8bJ x7şyî(ŒİåÖ<Ú„/‚Î÷€Nêğ`1xk³æp u7ö9e$½åpŸé½~´é…B]?•İÒG,…ÔL?£,ÛÏNı@î@êGkî²~T¶¾P µ—+ÑúÔ¬?ã1ÖrG¬ÖÜeı”m}¡ĞfÌ¼¾<ßúÔ¬?Ã'Ù9½²GJ@4ë7È*=Ø€O›uËƒO§»:ßæbàû¼²«çÏ.m,;Zvdã®[8ËûÜÂÄG»…P`}¶÷r§URèÔÜb*Fyyº+” zdg ºË	Ü£w	‚_´möóÀ=n—p.F?Ÿtº# ]İşİB“zµ€æİåáÑ»…@§Ú(»ãç»CxÜná\Œ_ÇÂ±@Z:ì=~ãHÙÛE&ñÙúC÷›VÌâFKÙzçIâó9¯\ì»O\ºz°~È+“â!~Wx÷Xœ D÷ÁéÌn¨ÔÏ~á Fè„Á*ÔÅåf„€óéş`„Nè¸Â¡z9©x¨°J*§_Áh|ÏØªÏï5bÌ‹±¥–’ĞlùBÕ©çúç–­‹+“9>½Ë6ZÇİ6"ÂC–Jh õ¼'ÈljßÀG÷Æ†Ş06Ü0Lcá$ãä%¸²ØCroï”b0œİV4]¹í\R=Õ¶AœQjç¢Ú·2ü™®éj=4	l^¥½§Í¾õ%ƒ*êq¦~{{l¬ùk;²Õ—İñıàãb‚ßt_Èø¶Ú\º>Ûx"®oP<Ë3e[ÓƒÏ¾*9‰–e¼ro³î}ç9èƒÍñp õüêôx2¦-¯L.iµD¯©ğ“¦¯~=1§ÍBìgïµ|¢gŸ¸×6šÓ>{'íL](Ÿä%—½…V•ø…Â*Géê^&øxïæéød|›íìJ7R€SÕı–ÕHñÄoôVntÏubÇmÅi—£–»­,å7›³õ[=]äÜŒ´¯2;rRÔVè¸d¤*N˜r~öÁsåÖ;3Õ:wÅ¨š
|Î:}‚M£ásFn_&$¦bÌU8SúŒöw—s†û_ªÔ>“-R¾¯@Ÿë@4¥åİ]šk|JbÆÔœöÌ¥|¨CG˜tíŠ´»OcêÏSG8¬‘©«¡ÿ§oËÑÿÑùk¸÷Ci—;ãPCà»¼ƒ8N3'…ÏNßVz²•rÌ¨gŠy¾¡PğD|ò‘°GÖKœ×SÃSMó*Ö·»7}•8×î”İæë^erj°à,ĞöÙÜ§«nß7,ˆæqz«O$C4&¿çÊø[.ÑL¦‡}LMM>u+œbœ„&EéubxL‡šÎ˜sÅ€FÑzí`Şs{ÂcJ|à>5™{wÜşi8íš…öå$ÀA…‡ğ¸
ÏôÜ™€5ïİY•öƒ§û’^Ø±”Ä”ç¿­ñSŞ¾UÛtmqx¨¹)&CéOÏµÒP¼\MG{V[31/_.cëÿ‚ãVñ5[	Í~|õ9«ŒfÖáeŞœ×™‰»à´”:Ïÿ1öØlWÜØµçNjeKErE çI'VoùJ‹ôúùÛÉˆ¿´hë¾°Ù¡_—né]~2­fÁ<§“oI*öUéç%«Ãa>÷¹ãEØñºşhjmuTçmœ¨Ûé8oXGÿ½¢¹Îg)t:´¾c?øİä¥s`ÿà¹­F<w?³·5 ¤qŸ+SD`(æëŞÙrõx0_ù/î¬¿½0´ZºeÁZuÏ^Ûñyn¾ª9ìj³°˜{Î®
6¾'`OWß±ë:Õít¨é–ï4çp–ÿ/çí‰ŸØë|¾ŸS?\#äÊnâ~œ;Ö¾Çw¨÷©*M–@»6döĞŞ¤ç]û®)`¾Ç1İƒ{WAo½¹ûšéèÄ>wÎéªzšØînñïNÜ?Tn™FŒ4ûş6T–äY›a*“Ë»p›‡6T&›¼xSú-÷6EÙRÖ–D½¡Q6öÎm¨%´ƒ.TRkèŞK©cØ…JPìB%(trjd åğÍ¡:çĞDªKˆXÓ6¡½}Ğ ­†&T„™Åsãláˆ0K‚%=4¡"”Ä!õ@ª‚“"4¡jØØ„JPlB%Ï‹%„Ø9ë
ïâ"ã-/ºÑ¸·ÁÂ&T&ûĞ<l@-¹pé‰İe¯y³@cK#Ê“$•óØ…ŠÀH"8]¨ã®ÑÜÃKš)u»P	Š]¨àyiå$t¤é2$í¡„ui#%"JÃ©®Œ¡ÿ/tƒş¿¤ÿ¥ädèÿKémÑqhCE“SªM*B…ÂĞ†Š°ÒfÛP5llC%(¶¡‚ç›)€L·ÙÀ4ÖÑcšˆ7¼è­pr*÷M,µŒÉpğfÛöÉ¬Ÿ÷ïóñ¨z­«ú¼¦Á†‘­ñf9`Sëğ9§Öì°·¿Úó\k'Õô´†“­eV=WWî}ƒ³Noòüöì“oãÔ3OåPÑ‹Úd¹qæÉÒzsı2¨rß™'gúÙÚz¦©÷×|ñğlSgLÕ¶#[½Ã«·ª¦-¬âõ“n­ƒX”Ÿ×çîğ'VE‚»í÷ñŠtoUá¯ÇóÀ!°•{Ú—X•HÚjY4ğã·Ób/¢~æÏsÄÆŞä³»ÁpO›¥o\s£zv©3;dçR;d÷ØŞ¥ö©PıŞ}õİsDşŸ'4OL×ßâä¿ ÖPlE
endstream
endobj
49 0 obj
<</Filter /FlateDecode
/Length 3842>> stream
xœí][¯Ü¶~ß_¡çQx¿ EØ>Îs[ın“¢°$ıÿ@g(^FÒÎŠ<G»9nÎq³;9Wr>’ÒxV:¦ŸIÀŸïfò59Gc˜>½üzÁëÊ1i+âôÛ¿.ÿøÓôĞÍ,Üê—Öß ¡œğÏß~œ–¿ı|ùşG=ıüßÔŸz’R)ìî§Dxëòn}÷éòıG3ÅéÓOĞQ’PNÚÏ>He'¥§O_/BÛ¿LŸşsqpıÓ?' ¨°%˜-Á'‚¯-!ğ}H™ºìÒ$V‚Y:}út]p+í¬dğDré·LÔ†‰ÜJ¾¿c«½Ô[s'¨
r
`à,ãN‚÷·[ƒS[k¡·ânå·…ÑBQav{WZÿşüz‘ÒÍÌ$½¡÷")q«Àşzj±«gŒ#d´|"¿³Ş7+ã£XAÜ‡(sÏÑCWôoh·'BJÌÀ3j`÷5	NÆé~18C¢*LxƒÓFËLÓ&Ñ\ªŞ'Œœ>cë ½tK0\´Á;c„q“IÆéIIîJéBƒ¨„¶®¹ÜÔAƒ÷yíÁ’™$ĞğÒ*ÄLsğ	+*Z_î´ÈE¡ôÆ‡BÃè/?_\ôõÛü6k-M»)Î‚I—H‹Ö9¿bîb˜•S piVÃQiŞyï¨Ú.Fˆ%±ÒdPXIZDWöFªÑÎ*â™D‹1K³xiÅÇK«âş/r?RÀ
é6‘\î6hÑÚÜÕ")-Za"
%š7ÍÍƒL‹İ²€ê&bGüSƒ'’~q]qM¢šd êÀ…SëüeUº~ùr!ÁQo'AT»%áF Y$má›t!!N4nc¡š†™jB2¸ˆ­É0¬^!Ãµ8ŒíÏ—ã´¦å?œÊç4‘€`&y›Ş&ƒ·Éà1üı
ÔÍx"A ¸×¬!•€@±:d¤ ¦AwTDúaAG³tŠ[Œ¥Á  ğµm-\n¡´PşšÂÃX(ÂcÁîÚFGzZB,½mÌ‚=ú)º Û…'æ/TÈ- FOÔàõ[0º„±|F˜¨ÜWô1Ú½	5ª¡Ì1ïC0‚ÀMÎtHËùoÜ†æcæøĞ?p~×ıjŠ3`Ù¦RÂF×‚5H^Q]úcƒğ]qŠ?#¨˜!À
Åû•µaÌ]ÁJ&x†*w‚Ö‹Älu“p$¦Z9ÖD]z!dH^…>«Û°[¢Õ¡cFâƒ„ò¤+VóUèFá™Ë–˜_eÄäqudm®G	½P™C>‰Æqé<b×2>çX]âzoyğdc—Y±¬f\x4Kã€rÚuE\ìpGß¼NmÅ›ıÑƒsåÁáÁÉJ%JV1æ¼æÜàä8ãÑÃû–8Ïˆ~–á&{G‚Ü¨N¡’%ãy•ÿ0G‘ğß*X6ètêDF§gælËu5Œ$NÄ”}ù†tµN°Ä9Fì4ÆªÁ"DÃ“¬âÙ ûBXà{ŒÎ®GğÍZğLØJ³¬SúP¨3ÁéO{=~(Îˆ ¸aò\=3	¸Ù“‡I]“$çÁY~²èZ>õ`ĞC´7‚A‡¡Í9ù²m\uN>~ØÜø+rMxÕ‡q+ß‚÷a+òâ©¾‘¾òT›L”P’Ùè²î7¶\`M’Ì9Î>5Í.(3Í°¶]AvÄræ/]İEÀŠ˜ç,	´
fEµºñ Å‡+4Çâğ–_“û0¦]H›¾ãgƒ|Bæñ„Ö[x™Ë=Vä{%Îˆğ[ÏÈ‡¥§_.2¨YE‰ûÕ a¨N_	Õø0K ù—J5@u,ËÙBØfæ$<u0Ğ~€¦g/¢Áh°ç¬r¨j6Ç…xV‚9Òx9|dèòÄ»Ğğx'šÙcp6*îáGˆ(éé½@ƒõ{–ğZœ•q%‘Ëáî•hV<Ñ‘ÒŠ5RëLm–û²¦¦}?5>@‹z*‰Tbv^ëEË,;PA¡¨ñL¢è45§CfFCË5*z­Ø¸Q›/Ÿæ5*Qóo“½ÅAÓñZááÆ˜øœÃk>Èc
"Õ£TÚ@œÃ`„– &†Yk¡ñ€æ©,ÄXÄ³€˜é€$ÌÏGØÇ9@…ØxV¼\oÓHº„X¥¡ñ]Ì!V©bE:CÛ+ˆ˜V|Æ‹Â£Æ °TTtH
¨£¥*fš'ÆH­3µîË¥µ*ÌÿNª|àƒƒŒ«‘h0[â!]ê3ËTĞW¦#®¢#t®W‡L±F¡¥SÖj¹F‰ªIûâ
Â¦úl%Põ.FLQñJ•x¶f¶<ƒÇ|
JfØÒ6'dÒmóƒIg«V×MLK5“bÂ‰–¿p
A&kJÍ=»¾ÁîJè¤aÑ[ÕADÜ“9›aï;"ÏÀ{ÜÈôëş1½¡%-•T—R•[¾×„©ÉÓ­š9:ì-İ‚ıgz
iKäe’Ñ&­õZéwğûş›*©VË«M¦+”˜uNsN°ÖA´X\uÂˆˆKmh7äQ!?V¸êŞeèpşÓ=6û!Ã„Éo–@„â§J?Á”F‡y/¹>°ç2`¼ª÷7©“dïmQZQŸ±ËáŒ¦LÇ×«ï7b	RZA'ğÑL”£,šòh	{F Z3\âª‰öş(@á¶õYrÉÉá›úõRlâcÎªuë&O«£ÓuO ô˜GºÈñ]`uê3{É|ÌDøOÆJ¾/}¦PŞfØ]Û1>uº¦Wb¢.Wy@W/™·3&7@ ,pqÅ²SD®DS_N½Ù/ œ;'ÓÆâ>É´õÿŠ’)QúÜdÚ:J¦×œp3.‚{xÎ <_[Î ¢äjÅ«aÇî‡1’CÿŞUVÑ¤qJ¾!ÜV³ü-Îò€8XÃ¤aFÄ:ô‹öùÅŒU³>;›—áõg$ˆÆ²SD§
níä  Çß'\?¬£¡àÆ`]÷u`®-¬Ë~´9´Ü
9QÈş-N®bß²¤ÃSg$.mğ‘Şdm¢e—µq‹ç°'ÖÇlï{‹ûÀÖÿ+‚=Déwà§¨<áÀİ±:BÆ^1[gZÿp Dx ¡SfÑe«zË{"‹·oÛ‰ek›v×el¿ÇK§L®Ñn'×·5ózÍLLÔãª(¤y1$zé˜ñ¢ t"šGıExÊ9lˆ‚Î(»Ãñ ÊÆmÕgcırØy¦«8ÉÆOdP¢ú´µWCh”íÀÜC›õÛîà	P#
/ï5‹»@ÒÿëTé-ÔÀh,3€o‘y‰®Š*Æ!Ñ¢.¢®ºìfEñhBy>†lµ½C*ı…§íš2«¯NF$íö†Ì¯g)¯]z@HVû4¼²ıSÄ³Ş1Qš ÓÇÖÒ=qˆNÜ¡E©ÂB»‰Ğ¨‰ú\e^¶/~2zhâ<¡vÏ˜& Yk"ÍòpÙ9xQæ@ÂåöøXÓ"iÖ%Î½ª(qî÷À˜„í)ÑÒ6¥h‰gi|…»„Ía¸D·nĞ(a¿@<cæWÂlg~Šl	8Û¹µœ³e±ËÖtéÓ‰úijûÔx¥¶¹ï²ñšş/ÎHò¦ó°V»Ëüª–“º©ÎÓ2^·PI	’°ÊÓ«á$ĞH§İ&fÂŒÅKäF¶b–‡xÏT0Ã²ïLÅ:‰‘f§®	•)kÍ»­	‹û¬	[ÿŒ­óÇyë>íÒIöV³{ì1ã!\>5'¬w¸zÉ–]µıÍpp’şú{RÈQ¯UNûåã¶“ñ
«¤Ì‹AÂ*ZßX™¦'/¶
=ko¾¸6İuI[©©hB£	åxË“$„8ô SÔrl•£õïŞ³Hàº„’»÷W¢µdåòfV„>b½¥ÍÛBø ·“ÑFòSyãK‚<y«4o£I¬€¢U¤Â2t¥šµÑĞ6–½Â
Í¹ÓŠÔîºÉly¯Í½Ø½Yví¥SK~ù‰/8±—8O:nøÊ²Ğß°*7|¼ŒF;CâÇ·utÔ x¢Aá©*T{ ø×¹òJlÎşR¤ÉÜşÕE¸b¬ ‡›öë‰åêëaf®òzØS* 7GÕ°¯ÉŸWµ`¼„Ôğ{È'Öœê+ĞAßñ.Êpâ›õG…bÂğ,šè¶Ñ6Rµ€-ãÄéÁÖ `jjñÎ­º¶zS”*Á–?à´î|;x5fÎ+u¢¥¸Ò@¯çmÛ‡WÎ.ú4ş’<[caüÕë3/½ÎWôùúJk`»Çµ²¼]¶õZ¶«"{HÙ–Ì}¦ğ”“À®ÔxK"ˆ{ÉØªàÂèÍnfb3³f.‹³&r)¦
I…ñ®]¶¾10	yæíú¾ü|* j„2ÇsiO¡³·	¾Ç†À®=ÁümÕó.9^œ¨t%@o'Í6˜¯T|LµñRX,ä*™r(ûUâ¶8.;¾;J%vÕ_
›uöJXÿ²úJãÕÇ‹fv™ÂUBìª¬X¶Ä,ãfåı*ËñmX*¾¸‹ØÙ¢a@|FÉEN\¾«ûd³>Ş‡+éşJ°]9hUtõÅÏx?=¢âë[¬áY0”Sq3I–Í6tµnÍKjp_å²jF¹°Û°g‹Ã”¡dgûóêSòëß¶fïXışÿbÌ<?‘^Éf´TiÇ¼ıŞÏ@UÃ¹ù}7VqvWŠÍL@Ì7<8¾ËFÜø¿eA3©“W0[Å¿ÁUFUº
Œ‰İˆŞáÏ;düß/×bÙÜ®Mº•‚ìÂğû3ª´_Êó6³ÂÕÆx©ğëuŸ¹³ÇêÁn+²‡‡\f7z˜Ô|â6ä°v/<q;\|VÍX˜<ÊŞñi5c#şªbyø)¿¤€ÅßRX+je†RîzMØÿQ§}Ä
endstream
endobj
51 0 obj
<</Filter /FlateDecode
/Length 3442>> stream
xœíÙä¶ñ½¿BÏL³xdgfıœx|€;fØù U¼ª¨î–²Ò8HvÆ½Ó*‘¬ûY²26—ŸEãï7J\&*CÎiùáóå×İ7.éÅz—ßş~ùÛ–_îë
óN„…~ÿúİR¿üöóåÛïìòó¿Êz1ÛÀZî§Ñ4´~Á¡>]¾ıè–¼|ú	*Âb£Š	Œ_Œ]>}¾üQkëÿ´|úç%àıO?.0ipk@,€8 V@º¿@ØğuJ W}ùt›p^HQPqÄ¬ÀšòëkîÁ®wFÜ#Ô$X
¸Ñ¸w6*•gk»&wM¿~{9«$æJ`úì¿àï¯€ ı¸¢W¸zF’ŒG»5(ÿ€+±íZEvDˆê71ù› ³•"<¶bƒvŸ243V9âRò_œwÄ5ŒVh¨â¸|®½wË+]8rÃT ‰JÖYh0ë
,dmÆ8í\š B¨ë­£‘9£ß4Ã›È±ÆØÃšx3´¹r ÑFeƒ%Àõ"³&åø'$+ûØG"Á4Éw1u™ÿúÃ%ä8®^éJY$xT£X’`Ù‡'ä!'e‚ÉNI0oñG°C°bß!g´NHˆ`Lr$Õ9äIâu6x#tS`¨C'tH°®å:«Àë…ÇŠaáe+(¸ ¨°ìm[ªPJ@ÃÂüT7Yp^a1„&·*#‚ÖQUå×¯ «cU]SM…º"Ÿ®ÀËev»"…;.^/l<œˆ—es“°aJ‡ùV^ØÆ%ÇÃX4ì3C‚ì\RÒì†¬v×¡:áÛ?\şAa!-õ?Šı{	$¨"Œ$_ƒÁ×`ğ5ü_ƒïwÔ­Î¨+€ºGƒEí²6G‡
[G‚®¢C9r[!9‚+ƒÁÈ›Ü"u@°98TØ:8Tèl1ãvıJ‡“Ø—”¶ÊÈ¥Qw2¥áwv¤‹¶¥/uùëR”®Éò–NÜ5#}½k°GÒñˆEıSl È*6PhË6
ãÌ$
Ì£šç‘¦)8 ÔÈà@×´°”x!	st(P$VF‡
ëÑ¡\õèĞ.¦è0†+Ë
{Ë¤²n„‘Ù†p„Ó!
÷Ò8ô"¶«Ox÷bák8ø¾†ƒÿùpğı¾­å—r£L†@†j£*‚ş, œ²1áô×ÅEñ[À²†şfcğ(ˆ9Õ`ğQgä&—R’G›€Äf”-¤€âğÑÂ	ÅÌF>ŸŠ¢€’^sP¢‹0´¢¬½Àƒ°¬FA‘±åiAÒ0 ‹ƒC	é’(s”¥ö:C£!“XŒvZEm$=ÃxÑ åµ
ªEv,zK–ÛeÑa¹È·Ë¡¤±.aÏš`<¬3Ik—ig`oÙY#ÙÎT@–HE­éö%¡yØ—„dQkâÍ7A	qNù¤­/w3˜
Ut9}jÔwÍ\šv£Ü˜ÜÉÃ"¬yØ!¨#á‡Ü…Ú¡d`’vr¾‰HŠEâ11(gŠBA-Ğx0’tƒ5õ,
a”ÙÚ÷z‘óÑ‘u6eşÀ5©QP8£Z]sĞNÑ)”'$æ±ìb&21–F…Õ@È’ëP¤HÈxÌgU4Bg‚ ¡İAº´˜Îâ+ê¶coc0|
ü:wª5ÓÆORe“Ğ;Ü´ÍìÊ“9¬ûÌsƒKøÉ}{™øXê?Ö	Ééç×k£ÜÑ‡
ï{£ª	KãÊêWÀû"úg¶q^ß½hí‰?ğä qIOeŠë”§Î5ğ> GÈ!­0é„±ÑÈ=#ìé Á··$ÏÓ‰ÁynduĞpÇ:o_?W¬üyï½¸z zF°+6‘lÂ¾ñ®§¸Ğm„´x˜{d\°Ls9¹õÒllw¦eÊò«9ÛD…áf×øÔö¼­ÚwOøğ›£¼œ"r(“Œşiƒ
‹­Pü×ÖODN¾5Rˆ™›„ˆ5ÉuŒô]°|Æ2V®Q~»ÏI]×@_7¬>Ï¶lò&§ÏN#Œâœ4"X89NŞ%0¾]iä–Àß´Ÿ§4r}-$7P”8“jŒ!]	Â’’›X:&+èâTDX‹¦z7¢røùPÿÒµnù±…hİà¹‰ÓUq–{íoY§…s—+…İÖõ>±Ej(ã_ê¸òıÏíØ®#Óã
=,+¸¤®Üf1É¼dª ˆÙÂh'07ûJøÌĞöõ¨r˜¤,ä}UQ‚ğ{¦bF|*æµ÷¦b1s›íu½tD*NŞ½K*NÑŠÅ9©X°pr*œ¼K*f|»Rñ-¿iÙœŠÅû¤â™¥ãSñ†+IØ¢…°o¼Õk‘¶´J)ÛGNÑÄŠÑ"İÒEŞbÂ	ì1)×â:/]âúQ²/¦3Sß+#¸z)ÛŠ‚n-£"zêUJ¦%“š:¿«¡W;²òATO±İïÙ¸SUôFB¸õÇ6Úµåõ;/¤}ÿ°šŠNé˜ÖbÙf®×_ç×LÒñïF:CzP=ô®‡Õ…ô°¯¦ÃX~ByAFŞ¡¼@<£1ù¤òB¢8£¼˜X8µ¼˜8y‡òBâÛQ^Üø›6àÜT^ÜsµÁ^ÕYqyÛaºŞ&œ#ğˆ|ıy÷ùšE­¾S«ˆgÓ'SŒ£Ãr[Ã 2›0|¸P˜[¢M˜6›Â„6),ØsëA‰â=êÁ5Kïs`a?Ê3úMHæı]†qnqh×­ énñßç2ÌÖ—I{Šw£Aï)Şé8W?(;N:y‚Úõl-ÑyïE®½oïeš9„xæKKòÀ‡!${åäÆš(4¦–/‰Ë¢~·­•²™Q
qîÜp/m) ‹©Õñª“¨‚:Ã7ª0›2ğ;^-]Ã]Ãà-µ˜-«7Ê¬Šµã1©9p.…¯T_ı|€Hıêx¸‡ú>±GI£«ÁĞ²{¼P{½1«`}ğšoøö† ²àBâÉç†"bİ‚ákwY°»)2}Eõ[4z¾æîØŒÏM|9YHîÊ^)ªE"µ–ûÊõ¢å
8b›¿JãäÿfŒš'=NÆñˆøş€©ª¾ÓôÂ(~2½ºŠ°¶FÉ¥í~H§ïo>ì·Ü\ÆBK%#Şşç=‘Áµ¦¿©'ÒX§q|ÊSO¤±6©¬éµ(î›³6*gr–vs„ÑÙO]‘u¨<ÙY@¹hî0ÙÉPÙÉPÑZØÑˆDAèV”‹®ÆÁ¡„uYÈ®H–Ûë

‚ğù²4É‚–¯d§¦È€úW(TÙY`9Ë‚a²)’¡²)’¡¬ÆÃ*“±r™v6‚Áâ-ºî‰Îçn_¢ÇÍß‰ V¡Ñ&ÙiñQ"ÙÒĞ7úë¬G-åªÏÑˆg}Äu²‘=‘	•ñ¥³ztöØÔ9 SO$Ïç¾BÆÃˆ’ îUdÒ¹§‘YäîÇ!ÙÉ‚“=‘˜š K@jêx†¤l¦a@´SO$B#R³è‰DX¢¶Y'z";lî‰d¨ì‰ó»*š¡³‰ ¡]Aº°˜Áâ+ú={"17Ä“{"%Šs¶¸«§ßºï}ğÓ‡`ç´}®qh Ñ=ŞæJ¡ìQ¤;BÓò–¾Èqsk›áeRğ—ŸÉ Tfqíÿ—ñ…â-É¤JwW×™t8{s‰Q¼ÏæÒÌÒ®M¢i?V®³I”7zŞ?z
ÖÖgôaV—Â„éıêNíÛ¼ôF¦¹;àfl»„<^œ”Ì‡óı|ñKÏ-Ó^Úå‘áYl¯91Ş´Ç	§ù`ku~Xäó‘m¾ø<ÑgHİGwõ(Ğ[7fµaöˆ]/B›§ãTq®W¾Ñ—ïâ `jD{ğD¶UMë'“0©îA»hªÛ£ÚÊëÃæ8|üH^¦âÜ&~7š&›Ù*½e¶†un´î«h!ÎéLFŠ$°…^©¯‹éˆ|çÊK’µ.p»ú4èm³‡[½§çzªv«Ö†#ò ÖåXXÛ¸Z›dnœÕq¸íø=lğÙnXí¾oõB1r/Â\â˜!ıº4­Š°Øwd&£ş8‡Ür-bD±‚>&ğ-šj{ƒìçßXëÎ¸‡»ñÁXÕ"´ÛÕª€ãG«Âæ„ô(a”uıÜªĞ“l¾']·Cz29îI¦oXÍ&«aP&×uXì4zACÏn¶ìûéÒ¾]Ïâ¶4ö4§âİ¤foä»Qƒäü5ù[áaíPqóAvØæXÛMQ
2é§ªÆÑÕş$2à¹1Ïé©i¨lï¦Ûf,M`Z»«>‹'h,ü¥fŞ«.{±~@7'7KçluŞc«C°óá¨­çøQ—×¼·Á­·„LÇÿÚ2ãí
endstream
endobj
53 0 obj
<</Filter /FlateDecode
/Length 2991>> stream
xœí\Yã¸~÷¯Ğs€Ñò>€ ÀôµÏIÈ˜d7zìæÿ©*^EI¶è±4yÈt¯{ä2YçÇb%ï¬t¤ŸIÀï§™½FÎQÆ¦/_/¿]ğse‚˜´qúı—¿ıaú7ĞÍ,õ‰Cÿ&Ê	ÿòó”.~ÿõòÓÏzúõ?ÄÏG=I©²û…(‡¦úô~ùéÍLqzÿ‘†rÒ~öA*;)=½½üQmÿ4½ÿëâàó÷¿O@PaI0K‚'‚¯-ˆ®ó’ºlš+Á$¦¯ïÛŠ[ig%ƒgšK¿¢BäRóõˆ¥õR/	WF\ST9ppÖq5ÛÜAm³…^ª»Ô_ÜVFÅ•Y9ì©Ìş3üşv‘ÒÍÌ$½{•”Ü*ğ¿N»zF¡ tÅ&rFÒLtû(V€ûe†ñ=°âaŞš<”˜Òz1}Ío ©fúÀ7—a Š¥ğj¶N-3M¢¹(T'Œœ¾àì ½t‰Ÿš½682FX7™dœÉ°Ü•Ò…¨„¹>sy*$€hpœ×<™iAM,­BÌ4W0YVÑú2Ò¢…Ú
Ñ_.¿\\ôõİ¾›µ–¦FŠ³EÆiÑ:ç;á.†Y9…
W5‘f5ü0sæ÷›íb¬(i˜&ƒ
Ì‹HÒ"ºØù©F;«XdˆcÖ&Ei%ÆiV	ÿÇ…G
xabl‰ä2Û¬ Ñ¢µ™UÒˆ½01ƒˆf!ÌÌr¢yĞ)ù-û¨jb~Ä÷È˜{œh BŠ]‰QAÙ‰E0Ñ"*]æ¡²J×7†:œ¡¨²exc
0dVU€Érfs[Õ9lÑT'²åÅ¼Íb[°%|lu¹üC˜Ò˜Ê5¥ˆä’éàG:ø‘şOÒÁ_ï«W \kf¥sğ‰ƒÈYpôWFı¼3¸â£’’İì•ŒjBb21Ì2ZÕL€š]ÁaÒˆe°àvå$¥m€¡œb¡€¸Ä8pµ€“ÈÄ´ö£™}”“1ÀÑÍVzÇY ğ…e²€¡Z†IZJp- Š› D‰kÏsc;bq1ÈäæÅ
á2!ZEr…Ui4¨½–ÉÖ¬?PÍ¬#!´
4Š«ŸšO
-’§‹X|İæ·˜49-|\£é¦{ƒD³qSˆNÄ›ØÌ9ú2VÆ[£~
&V¼q²…µŸâAï #ÆÊ¢áÆb’uĞU*‹p³ñ-Ó
é¸†€fcÑpğ3jh(ä9/ieë
·LLps±À­’n˜‚0t÷tÂ Ç(Â×KÊàZu6(@¤Ä¤ÂŒÍ4ÏıBó3¹9ñãÒ ÕaLI,	h€!mJiÈ`ˆÊ:eı
ñ“¸ŸWC†ÍL@¸ŸZJ’ºÂ­PA£êk6¿Ä„‰©Ñëªfªsô7UĞvG36cK˜ş`.Æjª§´öŒ:J	Ø7]OiĞuß£B	©öÜo&ØÊBb¾¤•ƒ‰5_ï!.ÑÄ¸›ÏğzÂ*ø×ÂËàû*qÀ˜+Ò$Õ"ÜŒ$ÀÚ,ì¥k¬7À^´í‡[~s Ñ¾·‡rFXãØAH§EÒ.74L4ñÚÖÔÆk@¨Aô’xÃ1±´0mÛ±Å>W:l9bÏq°”Î\ãŞ5ş…RÈ†ìmyà¸ß¸-?ÜôCw$æ¥w‡ÇaM@+][•,İş–r–KÎƒ> Ølû€Ò>OğzŞh §ÓVÆsL/|A¤Î¨|F$&d¢üU|võÑ°
Gê4öƒê@´^~õ»ñğ-¿íz€_SÏ:]‚šHP'ÓìK¦™d:ºáZ*¤16í´xEæ•İfÌ­°i.t
ù_—w£`@pxiŸŸhÕç4õ@=+g¦£mc‰Ç+ƒ[¡½$;h¾o0$»Ô·ù£ú3lÈ-²ò5ÚL¶;>túËœW™+Ç`ôõ×T(ê™…1›)“9Æ±9{«ƒä¡–¡çn4Ì…>ëd3x‹}ãUÂ'JÈY˜Ÿ›¼¢KñGı<óï &o@¢„óÌu½Ì=8@½]àÀÜ;‡ äépx¤Á“
¨•B§ê if½/?XÏ$¾¶îßyq›x€©ĞÕ­¬‰`ª+Ôm6ØñÌ.(CÜWÄ¡b¬ñ' ç‚¬ä;Š ÚØš1Ò±‹ì!¥0X­{£ŸÒj½® ß‹—âå^İç†+QéÃ^{²]TsS°qç§»Ñİû½â˜I*·}Ö_ßä:Ÿ—«lÀ*}ÖmŞ9UPæ{Î 
èÔœ…íqÓ!Ì&ûŸù³tj-£%[•\¤ÊÎ*5C¨uØ
á^Èã}•`”î¡ÕÙ¡åáêÅ,$İaŠµÛÚô>Ôj¹±oÇé5?¡×İÔÿ`³]ÒÀ)ú+hob0z¡¿­=<º¹†ò¨ÊIúk?K/·üˆşVÏ¥µ=G§f=Ó?Ôç<ß}`e-ı¿—Šh÷1KT¦m7j¢Ç›ÌhWk.i#‹wTñ¹ê®}îè¨r¨8²Ş‹^Ÿ]ï5çÔ{Ì„×ìJ{\–åGLÌ’›(l°ì7<·[µI'72¸n¢âUÆQı„ÌsUÄy¤ü¸¬7ióØûåŞÏö2ÔA*·¹øH!?N|µ8yu3§¬nnB9ÓíšjÅºêÛ‰%Ó­:Ò·BV>8+/P3—Î£™¸¡f.ß2ÙŒÔMğ˜Ø¥…µ§¯Uëİ-'6ç›•IObô
àÂÂ€sšO–x¸LìA¹ñ[ı§9°oTR•ffiú`ã(ùøİ¢u˜·½²<’>¸k5~ÌC´cİÒÖ1”†»h	Mˆ‡6Ôt‹–ÜĞÔ<¦bàn¬÷“±Š¥Fƒ^>GL;!¥Y¶õ`ßõ0-i
ƒ‡ã¤XŒÏ^ß§ê[Æ+;æº&ãm#U–#/×xÓIÌ[ŸÂîÖ‰«Õ#{7À+m‚Ì‹cÑtµKiÒ^Å*I/o_¬îØ9±¾Õò"êAâHsGcÅ=ay«É<‰z{å÷7™('•g—“MÄ9å$3áÜf‘[ò=šE&ïfqÓá71 DWT=X%°&‘³şÜ^ê3•r—µœË×;“Qôw&YMVÇ…¶„ù®yµn{ë—z]Ú*YÎ[K¼Ç4¢õëpCwM»ˆEX/ëş{_š—Ù¢…ÊZÅÆ”½¥„‚ï+;á/·^®>æ²è?ğ€y¬¤“f6™ú¾ÎrÓƒ.ü_¼ÊfÖ=Â›[ùÍò²BJè¨<y©’=‘t.r©÷K—Ö$q@*n!cH§è¶sáagLÄw98[˜ô½Î:ñ#Ğr]£ß¯KÕ8–/+èAMü!M>‘§cnoï¡ô†µC>Ob3Çœhk)½QrvÜÆ1ÒùTÒÃŞun-µ_Ÿ²Ñ á·€¶*¤¨dÆü$o¨¨Ö-“Àr¶¤úÄê†|Ï§Ö,m”ãon„[O]-Ÿ{Ë:ñìîÚ\Ú´Ë#PO9»ËÔtömÉ#¥>~?Ÿš27…ÛH±·vMN=î„µÛÄ£Gy zØ–éÿ±õËjx6uÌ“*îyò­ñ˜§s˜P:ıÜrÈ¹àâ†ÜÙÕâSÇÜiÂ;©Æµ÷t0«øã7•ÆûÈ'Wö9	0åyjw5Ÿ÷5¦üØŠŠs]Œæ¾êÔ¸½ÇíË#c‹uªø PyŸ¦üñhÊßw_3`‚Ûƒ@wâh„CÏÛ{÷¥%›9äD+ì}.St.cV%çˆ†¸Q¤'¯™ÈAÕ^±Vñ Æ}ç¦o¥MÔİ[)›:æ\³üÇHüW´!5éKŞÉ@³n<ğÿğ_bÊ¡
endstream
endobj
55 0 obj
<</Filter /FlateDecode
/Length 5741>> stream
xœí=Ù$Émïıõl@©¸À0 ÙÖ³­ücK†1#@òÿ&#ã`¬Êìbv/°=£u±2$ƒW0Ù“±¹ü¹)øû‡‰|LNOYçœnß¾üã¿7.©›õ*ßşùß/ÿù/·¿ÜM:À£qÆ°üõÿşÇŸoóÿüÛËÿloû¿‚/f{ÓÚD÷×Qøèü<úË·—?¾º[¾}û+ *ê›SLÚø›±·o?_şU)ëÿíöí_|ÿí¿n 0ipk@,€ØV@âqh] ¶ü<$w€›‘şúmŸp¯ıdtŠ„r×“˜Õ$zMùö‰5÷Ú®Ì¡&é[W7£ııÑ°¨c´²kr×ô«ûÄXe(1ıÒFÿ;üıÇ‹Öa
øÇİ4JÚxĞX’€ch­PƒpŠù'2ì!Z?Cê¯OYWr„Aô_·£&¤MûpûY?€ÍèÛüàĞ S($ê†ë¬®0ë
,deúsÊæÛwtÔ¡àKyŠÖà“9ƒÅT~C7Æ6è#ŒÕğ]¨CŒqø\´V¨Â’˜™”³&å
)á`TeÛ“g1@}r15ê}ûñûKÈ±úŸ&kµ#$xäk DXö!ÄÅä!§ÉSnd"Ì[øCØAX1ÊvÈyk×Èa:™D¤ˆ «rÈy#ÔÙàY™Ë³øÚ
"¬­ñ<ª-ÿò<B@
7‚¶€BE[	(°ìõ3¥ Œ …á§€¼É”ñ‹@Ò,¶*¢E¥#¢Xš€*ô³ª._[uEH}gXÁØÆá(cû‡/DAúãD‘:Z¢r„ ¢œÔ¡Ã#¢ë„÷a]HÄvš,‰‘™sì«CÌ¶-"±ñï/ÿƒî!İæÿ¡Wh?‡‹åÓ)|:…O§ğ»r
9‘3Ô¼£b6u/øÂÒK˜’ñ„D½DY— L9½ô u FG¼D­¼D­¼ÀìÚKØÊKXHyé%
tå%fXñõÇê%ê§…—¨0ª†%UØ19UíF&5Æ5–Î6µª&b{MŠÔH‡¼©9·•¡VßV°ù\ãá%pù—^ k/ PÑ6–½_z‰`3Jaá&æa™)çÛº	„®İDp
/„ «âÊK Ô!E,°î%ğS÷ó‡¥—hSEjh©Ê¨rVJ‰
7~¨ªÎ‰M4QÓi¢¤F6dNÍ±­5ÛºˆÄÆO¥ŸNáÓ)|:…ß‡SøËN½¬¦¥n°b‹ºŒâC¯¤Ø¹œ¥k²Ã2Ö\r‚¬ÈéÉ~.üx\úìó(Â¸¹V†é€[WÄ cóğ…ÕãÏ}Á¡j…¤Éz‹_ø¯sIh‚¬<“óÁ¢r¿ÖAi`ĞŒ9L#7ÇÕàÜëú…q>G=ê‰¾ª&0YÈà‘Ã½–/À•›“"s$fr^V±NáŸòÉ›Hr€1<!]õK\{ı@õ¥2j‘‰æú¼I3¦V¯uç@ şÀº²úÉ‰ö7H’DÏczŒI}YVı¾C ÿ5;„Z#O•tÑ¬U v:`ÁØ­Ò`.ì˜ª±6ƒ¦mMÕĞ2³‘Fœ Šd„krMFç¬×ëQ´/b©sQ^ƒ‹Ÿæ½~;µİy­Í««>’~GT÷+
'øÇÏ7å0 Ñl´c+Yn÷•‘,‹‰_n†X^°ÌjwG·¦µk&pí†VË­Pó×r“è,Šaƒ]¼î®ØKPFLı]Ú	Æ:¥RÚ×ˆûúŸ,£…>2ë‘è,½<Y‡V*sFFYwjfÓcD<ã¼Ø#ÄEÄù’õàQqaW¼£RåbêÚ¿È•*Êzz@$,¹Ü^á8OB©…œû1µç…»ˆ—4Ïáõõ¹œó¢:m‚<ªó¾ä¼å°¬Ÿ×Ş)²J}ÈS/µAvrêÃó6ÅÜYÛÓ¡J÷A¦æLO¸Ä†W…7D">SQE¿Ù ˆLÒ74Ù@ÏI…'ë4*Á´•MìØ¹9uL–ØTFàà¤]çEx·›rZÍ.§VçÃÄ™'¾D‰,¬OÌU’…x§˜C:¤Ú^Á73¨|Ú4a]›ğÏqŞ¸?0Ç9R{!dèYTµúã&ü%¢%©Ó/øl›Í28…ãwœùB0ıè²<Ùk¢_‘œ7NÉœóünB.çäÓÁÓ;Ü^…Ò+k~`æ'<Üy-‘Ü†¿ƒ}J9£V5å<]Cd`l4=zp¥Åóµ£F“õúqîÆæ lŞÑšÙúòš&;s‘§ 4yÆQYˆÓX¹r±d)òléíPpuôø†×°wh¿º¨®,Šy9L,w=Ş<®ĞãÅÖÖû	÷Ã¤rå÷äÈŒÏ
¹¬Ïd½¬V•\€ñ#¹QçÃBXh[‡är
>Œf¬¶µpè3KëtleMÚB)X¿ İã9>4ùM‡Ü3•HÖGŸuê3ÔhYj9PŒcşõôŠÿ6—é|†Çºu6yç¨âç8]†|ËÑÌ3{X£ŒŞÙ·ÎÅùÂ£"Èƒ$ÖšV7e¢,Ÿu°œ‹×b…µÓU'ÑJ¬‡BM¤í'\òÄóı°†}7ÔĞ9ÎçŸ?mCg Ë9wÎ•R9õQO9õ#Áêõéóù…È=!çÒß!ò~l¾Ã©±qæ|
È‰êPåŠnŞãÈPğ ğ|RÌ/à¡U’ZixC;K´M^ãn§Ïqc—ç7lW¹ÙƒïÃÎ»$öˆ‘s¸'£8÷ê­Ù~¤¶sfædìqo¯-¼Ó}ûû‹Nf2Y‡pÓ)¹ÉÂs?	0:;Eìo  P4ãh8À²Ò	ajòø~ø0inÑæÉZøí;Æ–|4@Ó¤µû×	Öè"¢"K(œ³|Æ»ÙMw3Õ3È¬¨Bà3ŞKSàXŒZ(Æ*ìa×„T i¼>	GV/#+¨èÇ&Îñ6¦ P¡@	xqvæ«R­^~Ôxå­sV`Á8l²oüW˜/¢lbê@\œ&Ë1zÈ|Ì2V‡Ò3–±>V{ğ·£)ØOJd¾¿"”¯|®J4€àõf%¢ À´Æö|?©¤!¯ŒÁNÙk‡ışaÊÚxĞ¢`€b•æ~@ƒíş1( D•+¥
†˜ÖyË•Y*rU¤
CUŠf²I¹1ÒDF«øM“3¨L”Ñ(µ¡$ƒ-"o²Va±I ­ .©/c,,¤r°¨Æm€ÔĞëj &0øc%€à!Ë}æÎÀPh¹\ÙÈM›:5]XÄt‘’±MòdŠ¾D”–¾–„h¢¹­¾4U:ñŠ	¬éë0€>/xÑÏ«[zs­Ãáµªñ‚pĞéb>‹»LxÑkwG~uÂ·jÌÿàmœt	i/_ÙÎ§µŒ²å,zóÄı€oÆP—h}ÀpĞsƒ'Iwè‡BŠÒ¤ãZ®±Ê“Õ ï99›„‰»\KÛ}‘ måÂ(½/„•Ú¡šûªòEO$TÜ@PŞNõ4°c€g°oÁÁ×j¤êË]c‡ëz9Übqj6ìºOñ4×1³îXeÍZbÖr”£§Ók¬îO˜”WÑÇÊ…1s½#¨ÕË‘8¶?/À8¤CµÕÌš²Š­ß"¢V$#JG‹‹V¼F¡Ùî`*[QÈmî.g2R2(ø0©ªÙÁUk¾S³Ç³=¿‚Ô²^ÌeÊ²‰„«’~KmÃdóF^$Àf~ù(É˜ÀD½–s7Me}WÓŒº:4)$C!ü«PŞ&1Ô@èbi-‹–î÷Ğæe“Iù14mç<æÌ²ÍWÅ¦º¤€¦ij[Ä*Ã›½áEÔKt¼h2e«ÈÎ¯ÓŒ»òöIÒãxCÈì¨E–±)Ô 8Ì!Ù“=lÉ:tıY$ÛX~‡£#®÷ø°yMb¼Ì:ê÷²Â‹¨Fšèæ[a·‘kÑ=¿µS¶xH»dD·M)aÄ1b‚©û÷=>îjc’é¥QºŸ„=A-èqÖ–•#ƒ¦r2vCÔ|—£ÇGRóšÙ«kd
ÁD`õÍ¿½Ö)³Í;S=ïéL,5¼5Š¨Ÿt¦¶Kÿ]ğWUêîéöû‹t”Zğ"¥(#ÕeüÚ[]É8šËí.ŠU¨İu¬×ÛK»,Øª„Íí×éwY¸«Y_fzõ{™^¾¤”B	c	K=65S<"kİ/%IojÉt…üŞ¤]î
×\µÛ'¨ßI‘)/’ŠL©›‚VµYú¢k~¡=M†Ç€.˜û"ÖM^XêYş‚]Ú	”±›†×<A²šB ]Bı5f!¨¼éíÁEâ; <Ô¨ ¢Jas·İMÚ¦¬É€¯ûpß|A›Û¼Én;33AïŒŠ˜Ş4åç) ÉÑNTÛ¾°>xµy=âVHµQo¢ºãæ*Ô†ÖşVAë"^„?@;Çv[8…­{İ£¿3yplsÜ½aj*¯7×<v$È(?/Y]¿ /düöÂõ•¸W»j–7ÿÛë12“›¦Mm¾u_Óœ&m®úõì–(vr£Äæ`ÉœƒE%8‡ru„//èLæè‡BoiÔ´¶6şÑFMHõ”V­š T ÒÙVM£BšB¤Í€ ŠøBÙ°hÕh˜Œõš´jl&j´!vmØì@Ú³Ù£rÌ1Z%)5£§²“=Z/wØ,Ú¸Ùöc	„Ã˜`Ø1li)Àğ-ÓÎ,:7
„‡Eçf¥XŞºÜQaËÎÍ¤›côX‚1ËX,JÏXÕAùXıÁáîl[7­­ËC[7a÷ĞH] İdRÑ‘Öğ03©X”®uLa¿¢Í›ğCšÀÏYÒ¼	°ÒÎÛÛ+€¶nVíÜlÃz$Áİ[%Dô¦JBno¾$lõ.ÍÎ?mİì’¢­› Ü°’ÖM9"¾–Ò0X?ÿ†™N9@Áã$çIïfµwYç¦O«ÆMkW]›dT9AŞ×fAF_EB0Õ‹ÆØVWø¶Mª.óbş<´µ¸ßµ	¹İ…'Í§­}qekìÇ™p?ê-öO5^)A.4,óšÿ*A¦m/½Üœ
mRµWóIL~ÛŸ~­²,rpe–³Z©Ö¨ÙåıHmDN®bXs"´ë1œ¨Y•§Z†Ø× 	Ú½^ÏÑz¹ç*ë8Ñõ^€'§7«¿åIâ¸)èÒ[”„×¶P“ûFı,É˜õ,EcÛAaëÖ}­%G×7¡O–Ãfù—¼pãbÚ.ã£ƒÅpséîš_ èŞçÁ>·œwŸ%÷¦ŞQ èœäÙ‡X3)ë‡ûú`½Yã§S3VyÆŸõ×G•`ë/º=@Óne5‡}D¸Œ ²M”®Ç¶âÔÊ¿^¥†KÜ¸P¸F:ÔÏ¾~öõó—úÿaùÜÀuDhÅ‡Ãm& I­ÇÄ™ãÿ!cgÿ(ÜòtJœÛ87˜¶í=ü:iå¯2QØªìFâDè§(’Mö!cáÈ=ò¥ÙÉó¥%“Ú¬zk LJo|=û~GÎJ¶_z„×©¤ûw¹y–r×Ú	å4Ù×sv©~Ú©;5o)?Ïà¾6rÌæÛw’ÔšXïŞ¤*•ÄçÜdİZ¾BIvKÛ•Û<Ù{èYß¯ê1ôğ9QÉßLğÎOk.¥Ü[< YÈí°]*»¿¤Ö¿]k?¸÷™}P4d(röÊ4¨c×ÖKÒ ëÈ¦iPŸE:ºCşuiPŸñöËbÕMë6½W$»N$b8‘Kƒåï’9±î`’É9Iƒ©iPGzEäD;ÉI$«á$”qŒSÆKÜÔÓ,îdI$>Z·,Er*·öø×¤mXìŞ°g©Ø¸Ômô¦Şb.%ûp"yæ3yû¨ä-îŸGHÒW&o»Ñ½ê9>cGº`òÖgNŞ."½¦ôâÕ*ì´¿D‚éñpa -.¿\“‘H,uœ<‰.u;ˆ€–İî÷ÄÑi/vQÉ$7í¨½D
<§5²Ú^R`ËØé³D[ß²šAô•Ù/¶Öm˜y6ÙÁŒÚ¤…‰¹É’Ë*|I€ç¼i(¼h¼ç%ò_µt-rùïUK€j¥o—×‰”İ¼ùHï–ŸÉ{@T)/]Á‘Äò®kã“K÷q¼…­wAkäÀèäØã_ ØÌí„êkƒÛáF Ú¬•O4Úà%jYŠM¿Bİ‘¢ó“‹7Åm¬5F"à¬”E,ŞÌı™Œ‰K;ÍÍ†}‚ëVÉ=-µûÒ³õ¶BNĞm#È5Æ1İßõYjyçRËı¡ŒÃ^ÖÑçÁ®_ÅK-é‚×¬|gë|oa‡ôgÉvº¿£c¿ä@¬T[æ÷bX±÷ÇõÛ¥|­eTr4—bËJ¯/¶Ì½á+’¨·\ ñ¥ÜRÊQh|©·¬©¾¼Ş²áF¢à²2[1gY
.¥$%I1¦ÀvéÆdK.fm¨R)°¼†—X¯MRâÄq®9q”¤Oç¢¡úªÓÆõD2§ëàüğ´ñ™„ÍäI±!éNÆæÏ__«õÉÅkDo`ë#jD² 5¢şåjD>¾O€t;ÜÈÕˆ:RÑ YkD‚QGzEÈ‹¾„xÔˆdUœÔˆ—«õ	®®É)Ë¨œïP#ºãmÕŒœ¿ƒD v?oš}Xí(¹jfò•WÍv`S¼vÄ.X;Ê]5»'uŒ5ù_ZÓè7Í1&œÍÕ-»L£Åz‰‚Çri®¯wl˜‘¨w,ÕKÊ¼Kµ£¾™Bö¢ÙÒ e‹óñK–¿gæ/pC%™›å ˆ±Ü±Ô‰kªví?%ú«ÍRá®ë¯6ÂšµD®.xÌ]O{Lği¾ ïÃ
cré‚Ç[Øú€‚‡° FÁc±‚¡ú}
”±‚Ç@*#ç‚‡$Å½à1^PğXkŒTÁCXÅGÁƒ3q±‚Ç˜àâ‚‡ ²ô‚ÁùÆëØÖö;oŸ¥‚w.ÙŠáŞ°ÁîùRÁîÄKér¥‚1ƒp©àB©kŸ6“ˆ'í­)„òñlÏFGæ@zmÏ†¯¯5¼p1zû†°&ö=âÅÚ7ÕïÓ¾!¨O£}ã'4Ú7$)îíÄäÛ7Ö#Ô¾!¬á£}ã"7_rµ²é%~ò²\m5‘L®F^z2¥Önò@^ù›Â××¢üMÜšs<`K Æ_½Ü˜É¶_“ùUõ_×^=ÿ*M‰hèÌ”–ó^[Á˜-Bv¡ ÏÙ¥_¢z1oÍã;İu>$Bá¼QHECáÚ4$"á¼QïHeË;¦,ç-¹¬R÷×oK
û~©Ñ×TöË‘„ å¥²¿\¾ë
ûk5‘¨ë›¥Z__ØßñéGIŒ^-œXˆ÷Ö/è}V‡NT‡ğW?ı?Â¯
endstream
endobj
57 0 obj
<</Filter /FlateDecode
/Length 4001>> stream
xœí][·~×¯˜ç™ğ~ŠñÚ›ç6ô¸MŠb éÿz¯‡DY”Ökµ5Ÿ†ä¹óœ3Y…ôágağç‡•\:ÅWÏ½wËç/‡?ø½P-R3¿üùïÃ?ÿ²ü¸Z¹[mì¡½‚†|Á?ÿøy‰şüíğãÏrùí¡?ëåÂ¹Øİ¯axkü ·~x9üø¬¿¼ü

ù"íjzryùrø+cRÿmyùïÁÀ÷/ÿZ ®TØ ØH ·ßçĞ±‰/€Š~z9N¸æzÜYB9·ı ¢„÷”oïè¹ç²vîØ#T8¾8p¢qÓÚœnJ­­™ìÉíég§‰‘LPb6û[ÿşüqàÜ¬ÔÂQÒBƒÅ
¼>ªÕÊ-‡ˆŸH³,ÓÆ­Ğø¬ù
0xçy²ßÕ[è‰şí¶ ô!ØŠ¤é–/ùBp³¼â…Bÿsª|‚ŒT’'Lª€ÏD¹)¾|ÆÖ[nbjµRáŞƒÃ$H¹~.„Ì˜#´åğIM%´QxŸ•”0Ç0–Î'ÌÀ'h,€*¯m¾Sã(©WÖeÍ>ü|0Ş–«W¼Z¥äªŞŒˆÑLzÒ%b^c›Áw«0	.d"¦%üv³ÆZCÙ6Ş¯àì\ù ÆpDŠIæoä¨’F¢™€yŸ¨‰D,ë8¶Êê=Ğû),´[„Lê6€˜×:u•(5Ò£ÊbÔL9GÌ“ä–e„(Z•¥Q:o„d6ª¯¨Q„T•°Ğan‡ôˆ¯j ùvjH¹[jr• jœ‰RbÂ™jê•sâYDÔu²(©“U™SwÌÚ¡n›”H|üóá?ÜÿÃ¨?‡€º‚ˆò
 ğ
ßUPøå‚œ!å±É!+*Q´ÛE	Ô0İD	Ä¤2-€¡ºÚ(*³RĞ(P%ë£„ñf%ë£bÆ¹.J ÚG‰€Å(?æ(¯Ú(±ÆS—Á–ÁËNd6Øi|%³İ8U’õ½$ÅÆI‹¼wNši¼>i°Äïk”êo¢"]”P%ÖG	 e%ÖE‰€m¢D@»(˜ê¢D€6Q" ]”ˆXá*G‰tÑD‰r;1¤Ò-19B 1ÎLi5áÂ1uÂyõ‰""â:E”ÄÉˆÌ‰;í·ÍJ$>~Iêğ
 ğ
ßIPøúÔÁ)V¢„ÄÍ·&J Âû(°n°ÍPÖE‰ uQ"`]”œû>J¬‹Û,0ÚE‰ˆ-¢|£Dºj¢DÂ3L]6[o,;‘Ùx@b§ñ•ÌvãTI>Ô÷’'Ey÷Q"i¦‰Eƒ%.A¢ª¿Óç6J ÔG	Ä6Q7‰û(˜VÎ³ÆuQÂ)­š(tŞH±m˜@´+a¯J˜ˆm˜È·SKÊİR›«PëÌ¤#ÎQc¯¼¯ÈB¢Î“…Iİ¬J:dÖuÜ¤Fâå%°ğ°ğ½„…_œ¶¥4!œÂè…›bÌµ§;óN›ÏcÄs<6[AKL^Çâ1¸…ĞGıBı”¾PZC¾­ëOáÈ¼¤ó¼ğ¨xÜ
f–9CùâS[K´ˆ³å£¨ÕZÏ˜=Oª–ù©ÁºÈ.}Á•rÆÔ@ÎÊV°;°µzÈ¥ÔqZµÍ$k^µ;Ä…l³xr¦Á‚Á Ù ­<‘$Á
µ«G¥éÜs+'öœHbBIOZ\®Š=®÷zºØö˜Û')«N[£”©ªcO;‚½”V•Åa„ùó²Û¿Ş³ãvYÓÙ…7Â(ÒõEÇ/²Jç=Co¤ÔÎwÇñƒéå÷Ì Y>ÇıB ˜Ã¯S€É…ÇÄ<ã1˜¦€tèÂĞü PŠwx"!_¤†LÄÁ¼Îîqh 
!	ÿr¢QaØ„`VåÕjQSÃ97R¸­÷ó³gºv_g¾¡C€sÀ|Ê)Å€…äÑÎ(%Ú&ŒG‘4€YAu6´L# èVîq²©Ä s÷<¦Œ™ln$Ì¡`˜3fî ÊF°*†ê Ó,®Œ¡–²PIã*|2LÕSCRU)!¿ê0ÚYNïhL71Ğà f1·Ï Ä¸dLs¸e8¦øz‡´K½üäÆÌê¹ uJ‡;!ÚÅÜR9L=$ É
æ~áğÆ ŠpLmÉ%yáÆU2%—Ä%„…TÊ1Uš	«V }kÀTĞ’(ÂBú¡¹ ä
ë‘/MÙJ˜-ì‡¶	2z=Ô† @bèÂã:e QûNB€àÚÂ3{Ltì Éñ÷ø2w ¢£(7³%±âeEZ¢ŠLió,{:NÑRKSQ(¥ŸšGá´µ™lJãÏË¬ø¸NüU\r¶H—g‚^ÀAi‚©0Å¶R¶ÏA]rÒñ1om®óÃbÛş´À)İD“*İJ
ÎÂqFÀD£6ü~,3;ÀÑÎĞ<Úì<^¸4Ç˜ÑÏ3ˆU*?W×L¯%Ü(ND<
_ŒÂ×~/V;ı@WS/®[ãf‘ı9Crø‘¸K½ág’V$L:Úb4İ¦¤„YÕ¸]Ê'Û—„ùz«!)“fĞºXÖJÉÜ®ã±°ü>é4“™ÔB3ÃêÒ¨ğÜ\K¹†è¥½lƒ¢ÔI ípÑƒix

vWFÈ=5i‰['‚Ï6‹3LÂ#Ö03¼Âì òäP†Ÿ79Oş
Öî(Œg7‚”Jòäy28c&2-w„†éãSœV°m¢WàgşñœáõU^‰6TIŸ2¦ıÈ!§‚ÕÎå–§Ÿoe©±oÔªSfÄ”N×:]?¥mÔ«Ji‚N÷á6+~ÑÏÑ¾GD™§"š!Qz–MNŒÿv/¸ÿı÷=cRnuµËFìcjr°¾Ü³ø+İ×™¦ÿ`‘œ±\3_ğèä!8ãaâTW»Ÿ?ÕÿduàšeËRİE¼j9äKîBfOÊ,¦RTai¡äaˆ“VİÒò#C]ÏcM‡‚Ï Õ¹° —{´zÃĞ†g +Ç'ÅÃ3>=xfIäz?ä3|\1½rË7Vu¥œ/éú‚“’u!?“peËê‰P>m•©¶|-ÅF®^vÏ¢
÷;EÜS¸‰]C´ZŞéZ™øµq~åÛØñD“ïkØà2~ãçm¤´º°g-ãÓ¤Çu27îÌÆËgI¶}xÜSÀ9÷€äÇ”çLÜ§—Ê>Ş÷Ù8Í(•ıE©òvŒ‰ŸùÇ¹jiA„âi€%»s¼ßˆ?±½“³5"Å!©óJ}Ä€Ç$×tK÷9cÖ`g±1‰ÕéÇÒòşKË*ö15y¦nº´¬ıK‘á£ğem¶GÿÌ36ÂÃì3¶SâŸÈ€•¸w*d4uÈ3g-/%$¾§urCÃñUÊb©ºn´²Üu=ÖQÑ¼õå>½SV—)å©Ì[]êŞç¬.ÓJêJI¶J5İBÂŠUnœx
Å¸j.e\¯ò]LYYâšug®,->MÕ[È„•%[·×¬…¥ÂJÃM™cqq¹!~xmyŒ°¡EŒ¨{éùÍ×—T4C¢T_sdûŞ×—ù÷¸:Î­+™)©5ß¸Í·xN9b¹w]XR1‰Õ=Î,ß`aYÅ>¨&Û3ËÚ°^1é9¡æÌòÏ,	ÓÏ,O‰^—ç7ZM„gf°CB)73àÌ™]KùÌ‡5…åLïœ.&é¤Yû½ÓÕê-ñúØó(!¦OËJÉóH#’˜÷<R+„¡,53¸ÑN2şnOAË÷bá™¤.k½$KmD3$Jù=‚ìŠ]öAio®Æ÷Ê¦7âR‰\¿÷#ã"k­ö8İã™j#¦!±ÚÇÈ%™ê×”HJkí¾4e“Î®m‘$@zµV-´ Îá[˜kjïœ\–hÑI@ùêVs‘z¾X¡F«şje[­¬¥mµŒ0×¶ÕjÃÜ?-L¬”ĞÆL3-vL¬5]ÛÉ,§×aXíH•$`
fZg	-€áË*½hj$a8oH‰$`_:@+$ÖH&ˆÖGÖ–¤6µŒ@ªX	-¤ŞµPMêbw[kÙVGb®íˆT¿YŞ
A æWÏ±$µ–ÓYfWËğõµòÎÂ×ÎÆ·B”=ı0…¯‡¨µ|–ÅZ:Ró—!Z#Y@Z%Y×zÃ:F-M¤ÄÔ*ÆJv-w¬ìÕšÈ(Z&™…E+%ƒÅ¢k³RŠ	]1á5q¥hÄ8Û”I
æÂ¼ U’€¡Ó+Z$™°¶H²€´H’´.õ©uZÈJÉ©%¯•pj!™ÁÕ¼U‰¤äeJ:šÇËølùÄqº>&£·O¯O^Ì’qÆ&^n·‡à«–V.ø&—e5øj¤¦ÇN`¿¾9:Q¤ha³tR˜#
=[ü^K×€Mw#R‡ê²Àã™×µ[Ô‚È˜˜Íı”XşÄJ½]—ìÙ8ŞŸ¯KíŒe¥“Í8#“(âÓŒ”ì§3¢•ø¶Ÿôÿ{ ÒˆÜî8¯‘‚¹j£l”u°ã;cÇœs¿¦û•$…!’1Æ«eoÉêè·duœA©¸²…‘öÜ9¾ÈDßB:á^ux‘†«kà¢iĞAÆd"ÙvCaFtåÜ2º×î÷CÙ$vè,P‡÷ y8ªc+T*²vG)˜K²Ô³X(Úû¦M×C†¡úmŒÛO`dÌ÷4²Ÿ&Î.¥ê–`*÷¼!M
\U–›íîM%àA—,™p6+[åZÌ˜\øş©şî)pÚIÌh[6:©ù™«Ñ÷7×:¦A]“Êû"ê#{ÂôóÉ¹hŠ©âKšE¨*¢$ŸÍµxŞûo„;u’pe	ĞìO`ÚÚ´Ë(g¦Óá±Á®Ù˜â6Á½-ŒyÂË{Nkî,‰’/°@*Ü!eˆÛ$ûJMög$úÄbÉ(cÜš·L÷ëè·M÷ë8ƒR±ošî×áç‹Åğj+ö²„_Â{‹X®ùMşÚı]~ÂÕÔb~j×-k’şòLFÓõˆqhyÿ¤ŸŒù’~Böm’~2À÷’ôSó2W}ÿ¤ŸŒ‰æú©—Õ’g•»&ùÂ²jšz8ÉÇ§¼¡J¥9uf°÷Èòë(eùµÙ ÉùûgùdÌ÷’å’/Èò©pG”aøm²|#o¿¥OÆãU¿e_G¿m_Ç©œà“,ÿ­Î*
endstream
endobj
59 0 obj
<</Filter /FlateDecode
/Length 4582>> stream
xœí]Û·}ß¯èç nó~‚ ÖJëç$òJì X°óÿ@ªH«ÈŞéÑö®{åØš9Ó$ëŞä!»³›ËŸEÁ?ß­âkrzÍ:ç´|ú|÷ëşn\R‹õ*/¿ıëîZ~Ü­:À¥±ö0~ƒ†zÁşöãR?üöóİ÷?Úåçÿ–şb¶‹ÖÆ`w?Dá¥õ\úîãİ÷nÉËÇŸ £"¡^l\cÒÆ/Æ.?ßıY)ëÿ²|üÏ]€ß?şsÀ¤p3;`UÒ~ZÀvÀ×&¹®vúáãÓ‚{íW£S’ë8b¦Aô,ùöŠY{mg`çŠ=AMÒK77­/«iÀ©ÜZÙYÜY~uY«Œfc°wÔú¯ğÏ¯wZ‡5à·h´´ñ±, Z»báõ“hö]´1¹ÕBë«ñk âSÖ-€×¡+ù_h·¡£VŒ‚äÔò™¾`<â‡	˜
¢Q¨/ÖYİ0ëb!+Ó¯SN/Ÿ°uÒQ‡ÚŸZ£5xeÎ1rÁ.p½±ÆXÂ ¡­†ßBmª3´qx<Ô°¤30–5)7,À'hl@ªì#]éqÒ'a÷ôñÓ]È±{Äo«µÚñÅˆ¯l]"–}q<ä´š`Pà.&bŞÂ¡b1Ä¤Ú!ç²];aÄt2IX!«rÈdo›[cgƒ7İ3¡\‰.tÂƒˆ‘k+rÿã¼°Â"»E(€Y¤ ˆeï[WMR¬×`…E*„˜/²æˆÅšİÈFÉlµH["VGÌªXı×ıƒ¨³n‘^,XFÁ©
llÿòx'#„.—‘DİÊ˜cdt’¨"ˆI#ì¬»È
2’L2¦L3¶ºLHòLÜæF‘åŸîş"-õXès))à-¨)oeá­,¼•…?XYøûó†6÷¨=8ñ^'RSHÙ£‡:˜õ£ü §2‘²3Y&rèmi9ÀàËX'R¶Ğ(u±¹N Ršê¢s(X­õ#Õ‰úm¬â°u9Dl|®UÌ0Ô	RgÈ–®÷WÍB2ıš‡<í2ººfÈûæÁ^@Š^'Šû‡:ÈT'
4Õ‰‚ÍuÂi­æ:Q°©NlS' Õ²Fà÷¹FDkDA]1P÷`Á|­ís­íËP!&"¨w)bM.¢²‹ÉÁ[4.ôåTè†Ó(rKXZ$a÷‰HVrÈì[¦o¥à­¼•‚ßu)øòi‚ïSmpFé±6 ¢æåDÁ¦åDÁ6Ë	§!F"ÎÅ„E0æÆåDÁ¦å`i®Ã¤üØf9QĞ©6Tl1ıgªíÛP6Ä_ërˆÔ>øÓMÌ!î›:C†ÚC*5ûÈŒkV”©Éö–IL‘¹N¤j€>æÚ€îk sm@h®ˆmjƒóvS›kbÛÚà¼j|ßÔÄ¶µÑ¹6 Fµ¡~nµ¡~kCÅdQ—2Öxp•$¦^ÔD8ë+2#†(S‹--“|"“µ¹NdöMÓ„·RğV
ŞJÁï¹|ù4!ÁH½6x•¦ÚàUœ——Ú,! Ó¢@Ó¢`ó@¿©ˆMKˆ‚m–kCÁjm¨©6Ôocm¨˜Œ?êRFj|®UÌ±6:2CXo™Kd!‘rdG™›lq™ÅÍ52×ÉƒTĞÇ\Ğıcm d®Íµ±MmHÖljbŞêAsÄ¶µ!µ
Bv„ï›Ú€Ø¶6 :×†‚ãX¾õêP¿ŒÕ.—QDİÊxcdd’¨"€Qå¬³H2Ì2¢Ì/¶¶LDò‹LØæ>‘İ7MŞÊÁ[9x+¿÷rğ÷£Ç&–_î@Õd³ËØ~ø,°ï´7©œ¥xì¨+h^Äš^ÍJ§‚¢4Æ&(L¨ü)(hí`
²éäÁà&è‚ãŒ
¦Kpu ƒxQ<¥á Çu‚`qM
ÛÎn€‘pË:
}›ÃêuC€B,eå‡Ñ …I;20£lÆÂ4L=jhÙpƒÖ#Z-Tzh(ÙòqÀ0[UBÊ‘FŠÖÆf-¤Š×®ø’5ˆ]ÁÅreÓ±¦O·JÅ|±5Ù0ô!YšÛ²OxöŸ”†}ÍrsT°~Û˜Â¨Äh3
Ï’ÕµŒjÑÆØRÙm#ê×¨ÑÓ>©¤sñ”ºlpÖ@ÅÌĞ¬D›‚•–wªŞ ¡è #‰˜œ‡¤Ö¸³gR¹Xã>dÆPÑ–ƒM·íKr5M»˜JFRnlm",>À4ãH&Bq75Ğ¤X&BÙƒÖ£&fÔØ
74
ã”Jf|¼ãö!Ã
D[,9}¤=ˆÒÆiRaı4 S]y“¥š'Ê•MWÄr½ct›@-,e‘ì†ßAŠn]Ñ†Ü ºî„èŞâŠˆéjm¢ˆâë†3`+A«ÿÁª‹ó¦áµT9Â·xHXyˆÍ!…’j§Øü{‰ÿúú7X³ş­ñ8Ü •<·æ ·æÕãÍ…ŞË‚né¼ävt]¶xxÓ†s0d€¿Sê€¦{ƒD52ëÛ³IÎ›ëáÆwY¼Û.p#OUŒÛ¤ôU§õëîáß|‚‚AA4‡z|“»Gw9ho„;ı‰ê”3.ÙNÃâpŞŸá6V›U0[µ04P“bAŒØÔÂ¥Eª~ÅÃnØ·º>€B”"­–EqpxVWıôçZn<P`r=C<|¿d]¸)[‹1aóCóêø;5O73ì{½^OßK–}¨²óá5g¸$†»jÒvû~<3r˜ºXQoÂ.S˜0Û%°E÷‡í{ùì§kcµGñ¥j!LaÙ®=ìDÈ•ßïùïri…3TÁ‚‡ûKğa²é±põêM’…•êÏk
d{(³<-[ùpú³Š|Z‹>Äy*Àœklº/ÉÎ>C£Í(û»+·ãû#…ùˆ'r1f¢ıÇcú:(ã%6B‘CU.}vJyƒi›3º‹|Å¬¥*n=wbó­§ı¥cä}åjìÁ’,'77;xÿxíc^ˆÀ!òZş‹›ÏËß`E
‘oˆ@iÜ—}FE®=ü¦6á´<E’¥=´b‚¯³÷šŸ^ªOE<F5XüğaçêÃ8«q6GÃÏN¹j¦²ŞËÙ˜ù‘©›Fh}%}hàësZiUÖçà¹iÒ¦3?øå|»ÜÀB<jş¡M¯au©@;0zÿÁPŸ³Àİû­éÉ1L—œX"oIR—³Ø¸¿1`vNÃoØ¹ÔÿÌÂ¤”ÖT#fkÀ6ö>Z'ÁM–Û^¤\‚ßA°E©…$ÓI„H20IÅÆ$÷Ït—”„‰±.2óg¬™ÀúúŸ1²ÔãˆÑg/È7 3xo ß4Ô#ğJ®»]p€5„XQĞo š²åLFh€¤Ş$™·±ÕEçì Av%ËÌ.ÊmãeË¼rsbŞ2ó•³mAEÁºe­ eCÙ"'+<ác–Œ[VºñÈQtF(«"SFL[ƒ$ÑFÍ:C%úî\Ö Dg½„¸ju-wš’12“dÖ
‹œlªÄ\À Q–Ê³$€qM1e=k ƒ¢*»(Ø5íñ±Sk2DıÀ±uPm²9™_Ó5ÊÔ}*å—AÒ5İDÎ—°mgi·l‰rm~p”y:ÃCˆy¦AÛä($ãJïğĞLû/kbšî„6E#ìA,ôÚ§Be±ÙgÏ&Aë5¨lÓ¨ø»yÀ*„Æ¹ÜC›³=õ»¿ò{®gøËA ë&±¯Î¬$SØuòÅ¸sy˜WŸ´ ‘$qÁ)£nP`×¹mÑ ¦QÖ}–`•ÓŸ¢F8“å0p×¥¹ÿqK\µB8s®R¦rèCQÒ´š;5údxô‘úÚ-V’´(­Ï`šÊÅ¨ÒÓÖ¿bÉ)ÉîY4ÅÏã>ñ	§å3Ì5;³?j²Ÿ¤ÂØ™ÌÎó…-qj2GE+òÛğ¼<Şz æ@õğ:Y,FzÙ,TzÚîÇ³xèîEá,CœÎ
Š,Ã\@­½&g0À!ƒ9÷Z!ØGzéTz:­o	AÑİ!‹†-xñzX¬5»<IÈ>g50ºÏ^˜DûBhıÃ…›'z¢ëº`8O~ïV¨>a’ÿİY³HJÜ“?Öµè$ÿ«&“D²ü÷GXpåhã_6ıÚ4¸ÓdÙå´oç¡wÙñ´ÃCßLhG"¢­ÎA‹vˆè]æz‡ßeÌwm÷8ó=jü!ƒ
î É~ûØ»ô{»G08´°şzïØ/òşÀÀ»[ï[Ox9&ñj¹½•}­÷”xÆnÄ¥ÔŠ´´²ÕHÈ§‚³½ñWí´5ôî¸ÕX›³°ßí®ŞïjoûgëViwÓtoûl/.{GPY³Ëa6l\ÜBv×#|7œv6Éş åÒ­Á¢¾Ú¾Lêñp¹q§“³k7îty‡‘qbßNã»…<>Â!ö…’Å	(7lÜ
£h¥ÅÆ`q•ûvÛv’»v{_½o±M&¤j]^±óFjPÑ^nÚu3=`9pŸÄ¦	õh¾ÜB¬ã7Ã åÈ[v€Õ‡Ä®]ÃÆ}»Ê;nÍ–çQØGRö&KÎNgŸˆ˜íÖ	í¸Ü»ùR¦ğQ‹­;€ìš=N*yG(ÁtV›ú†­¾w”`l2>éÂ{LÉçº—Ë{QÉí»Ê<nÌû`<o™IaxwÅæm¸®ïÖ5#È¼n-¹…`9[Ä`å¾”0<±oÇÃñàñzº_lßVŸ»w÷î$wîDK2¾ {i¥ûS-ãƒ”ÛÆÌW;#ïŒíDÊ%ªøIZÛFœrZ)ª¾$dqpqmS[SÓAh:‘JÇâÚZ½‡»šjĞï›rÊ!%!XWhBÒ««3XóÒš]4;DLÀzù’ükû§‹sÄ?åø­¯¢à)å×ñZ›œÄâ^uR°´g)›sŸöGë<1“í¶“³f+Ğß‡ß¯q¶…Ü/ôtP¼å.]oa–w….»fˆkşQÇÃï¶ícgy[ó[(‚,Î·^…¤·A{ÛF«³}ñ›(‚,ÎÿEâŞRím{·Ğ(~IÌªŸ7î¿_:ßr?É[Úû#&HøPmİu°7n%º7Ê\ß'z•2êØ–úZÌ°Kş~c†ß˜áWä»l*Ë\Év™Ô×á‚ùHJ¯T|,Ò3,i*%â‹Dà7Ğ]€Æ²[Ò]H’–·‡ IyuP’^ôQCMBAI‘Ø‚¹êÚX~¿ƒÍ\#äV°r¬``ot2íÅy$6 iÕ¶¾¢iW°XßwBf¨ØHz&9/nËæç1ØQRö(ËÍgı6Q³e¼ àÇuä»LbªP‚~õ`†$»Úúr•Î¥$|iK®ì¤KÂÿ{à%ãeš-Ó-&xn1ÁQKf¸æ—¤ ÌD±ÈÌX±jLm%~éH›­$Ûec†[sJ’íÍ^_Ñ¤Á‡Ì ¿4²]€z0G–l—­™â$ÛeEusY‘gİª¢5_Ò½4ˆÓı)ñÑœcæëñ]w¤,õöf—/±ÄÀ§÷Û)X!æ·¹ÄPiË!ê‘£
âÀ­lzh¾ìƒ¾eøÕœ×Åüf×‡å„¾e=ä½ò®0«yÌ{ü:S­O’wêK6^c5_î¡Õ ü•#™vErr’ıĞ–¨íq|N»6üYaìª3;ˆU»ê×hˆÓñ·½Q¦ş/òF^ô2¢û#~¥ˆœ^ôÅ\Ò(€oÁrÊûeà–MÔxˆëoT€	0>·½:Æ…ƒ¯¹|Ïİ£½37L‡'^&rJHn^:òÏ‰Q^?2Å‘[!†oìŒø,ïßòR£Á4‡"óà?.G¦ŞÙ°ù’È|â-¸”ÿX zÛ
endstream
endobj
61 0 obj
<</Filter /FlateDecode
/Length 5203>> stream
xœíÙ$·í}¾¢ŸlY÷öôs’ò›ØA°kÀÎÿ!uRUÍiUf6‰g×ãíf—Ä›"%{S:¦?ßläm0r‹2Æpùòíá×ü\™ .ÚŠxùíûÃå€›M:xÔçÆw0P^ğï_~¼ä¿ıüğÃúòó¿Ó|>ê‹”Ját?%ˆÀGóxôİç‡>™K¼|ş	&JÊ‹ö›RÙ‹Ò—Ïßş(„¶º|ş×ƒƒÏ?ÿı ö ³øğ E~)@7€ÍCb˜<éÇÏ×	·ÒnJO(—~DíÈ=åÇ'öÜK½0Op„ª /\h<Œ¥öÑBïÉİÓ/'FE‰9ì]ıgøûëƒ”nsøÇ\$JZY°X’w0G·Z½¡!ŠüŠ{ã=uÛvX{ˆ²ï=LCÿã@˜C‰Í¢'iyùVßX._ñAç	â x8màáÓA.
ÕF_¾àà ½ty:·yíğÉÁY
È8Q|\)]ağKøĞ•±9|Ğk„.° H‘©Ì…€ƒÕ¦M´¾>	ôâ“@½ñ¡ÂĞæëË/.úöî+¾Û´–¦?Œg…dJ„EëœoÈcš)lÊ©h™î‚0«áaaŞyï¾]Œ¸º4DB“A"Gi]$P£U]5	4Dƒ«:Îƒªú¿>ĞçR¸ĞYäLğ#,Z[¦*„­P
ÊÂ,`¡œ#Ì»PäVeÚ.GxGu×tƒP“Ô5˜`‰®ãX¥Û›¯Ô:êãÔŠê´ÔŞ:Ô2+©Ä€‘jågâU8Ôkª©uiSG¬z¡[ÔG¼ûËÃ?10„KşãA}B	h	bÉk8x¯áàwşz"O(¹FÁjÑãƒ•Êñ óLg²*	&Œ@ÈĞ ‘@?ì¢K0¥‡ø 0½	¶‹	vˆ	º‹–âCyYâCy7Ä‡#6Ø¦$ÖJ»ndÛoì/élwjòé^×¤HÜ“È›8rÓñ÷¦Á’[|HêâBvñ!œâS‚E«‡ø @4mÈª800ñ4&‡î¢ÔüÎ‡AèÓÂ!"AÁ&hˆÈ°"Ò»"Ê›!D´Ç©!Õi©Éu¨qVR‰W¨­wŞ‰ST!Qß)²¤NÖeNİ±j‡ºmQ"ññ3IÃkPx
¯AáwîO"¤N-JhëwQB[wˆÓÆŒ Lh¿‹ÚÚÍk$bœ0¥â%´5[2[ª€í£ÂQ¡û(‘`9Jä—5Jäwc”È°ÁË”ƒÁ6äƒi2(ìÎÒøÜªHˆ:_£½4	<îÂDVÂDUaÖ“0úÃ@öaAû0°C˜ˆÚïÃ‚öaaŞ¹]˜@è>LDaaÇ0Ğ}˜H°&ğ]ùÍ&êãÔ’ê´Ôæ:Ô:+©Äˆ+GÔÚ;ïÄ-ª¨óYR/ë2§şXµCı¶(‘8ù©Üá5*¼F…×¨ğ;‰
=¹üò İT”@©nÃãªoöÆH•äWAA+ÜQÈ€0k„7 4›TğÏS¼ó]` ŞÃ³€RZ@š€øB ¨Ìì L
 3Ù|”¾ÁP¥@°•ŞÑÁ D]KÑ 0nJŠ8’¤´ Q‚Qòæc®{Êè TÅº*¨Êíë ›Í¨!÷›ğ:Rz Ö29t‡9¦4™òÂ£ÃœUô–&‹³IºUf†*«Âíc»:®0JM×m§»Açïh?hhYJàñ0†$ëe±¬{£ƒÏI@0…€®" f
( "½u§ TiyGP òÁE jÁoRÜ’àtV…ô(’ePìRWÃÒV¥\,–¥»"•‡Ø„†+KÚE¤¼ÛŒBÓhR‚pıÊGdÕœ ¯Iƒ¨
îëCk=V:-H,á<®Za*9…tãÒ“…G@í&­
M	–C_Z-M¸ddUAĞÔ5Ò4Kˆ&–Ò˜;XOµ«Éã\Xo ²c„¿Àâr‚´‡õê)FKˆif8ÆüÇx <H› ?Ÿàç=üÄz½á©uşpD4Bêå†ãüTÑÈXÄ«àGgŒÖÂ¿şõnó3ğ2ıô3õÍ @a1ß­ŞóT`¨ğSœ‹ç÷øïF•TÃäòÃpàÊ XÔÀM0»DscXVd)]”Iœºˆge¥xïm†£XÍøQx	#I¼kæTÁû[,˜¼Ô5aNè£Œÿ–Ù°|_Ëìd šk-³M~Î2‰h¦,ÚÓ-3ñ¾È2	AK-3ØeZ‡¯[fÃ"?L¨ VhTœ‡ÎiWÊÍ=Õà%,©B§o'j9d<ÉÅ?Œ.Ÿèq™„7úĞ2Ş:CQ‚ÉóL9ó
Ó·=³Ã–n)$'ÛIèç»Fs<÷}&İˆô¢^C|›èP_C,e¿˜M ôÉ|´ÒöO2Ç‚Cèû8ó©À¡úÂQû Ô©¼rõ‹pE
fVÄ úÍF›?€*E»Ò“Ù|Í*`#£a‚°'ùş"&ˆNB†n,ó½J·A6q»ıæˆâc—¨JDÇ®ª|©$a0“· q‚H+Vz!Ç’É'¶ÈDÂCˆÑº2—vP¸p…w¨Ò#d²Xxyqf¥b,«xN‹Vµ!!F«»ÀÌGJ—1†×‡h«¢¶a§4c©z]0ŞÊ	ËçÓÅQ?Z;ã<›Éı¤0§x´åÓ“(~ÏÌÅLsj±¡~(;+VrŸ¼„0ØÉxí”)b±¼ÃŞöˆßÑï=Y“1aVuŠËEr‹Õ,$g‡æ'>Ø­˜öÕá
…ß­PzCÂñÿn‰Âí&ˆ *ìm%•ü1*µ—•Ş‚‚ä^‡à&µİËCoJkÀb÷ÆÀa…ÜTeyÂİƒûØÛD}à¸0…XTÌêµe}°›ÁEˆ,[,ÆsS¹ºšQ<ã•yXiàá¢yQQfƒ•aqæ é¸,áû#C‚™é4jí³t5)g! ™Åû"@¹ÑÓ¨ÃÚõãpXqqw0FÈY÷5‹›š»,Ìl2€qy=:‚ğ5A^”äpûØ°·©š3Â ¹á9Ë ;Uù½~­¹‚„/;ÏûÛJp”$ıcÅnª—A<ç¿"«GcB ãyé²!ìEMÖ(	Ör±…Çn»rÀá6LEFpËßŠ½åW,ñçàæà$ª³ŒğÈYiôR>|¢8ä•Ç©xä–3Ÿ®A%”œ	œW†¥…ÖN}ĞNY§3ş>“ªºaÎû·2ŞL:AÕRÃÌ’I%N×^ÉÄ<Ï:>›ÅR–^Ãyá:±r¸Osñ=åÄ&…su
G­Ñ¸»ò”™h<õ!ŞVÒ\ŒFœUolì ~„šP8›U°#¦r6ºêrŒŸ§ö”Ë§ø8Ë‘[J8µ9ì¸-hÜE=l'œI‡êf²îó«›*óô²9Âé©x>Xœx‡‚;„Ã–ó‰4vaºñrwL*îÈşXK\˜ë°ùíA†Óù‹X;—³"Ñ¥ÿÄ†\8œ—¥Û2ÔÅ‰·ğq#/Í–c´¼u€[!âËx¤U •œ®œß­a÷ßÜvñÏ/uWÓ© @³*n3ŠO/˜ü–ÍØìé´<Î¦ÖçyX·|ÇÖ*§Š¹i†•ù*W"°ÚYL$GÜ6ğœZçöÍØh~:6³û÷dNë6œxF¸l€wËu[	ı†IŠóÇË*é—ÑÒoEpßDl,Øœ¾²({çñJë{¼ì`c${¼- ã^,ì
dLşõx²qA9»±˜…zÒUú;ÅÍ‡G¬wlÄXwĞÅ–¾ì!Íjçëñ)ÿ˜­&[y€*z;„•l g\W®	{ÜÄ¦Bt§vb_G=±Uz}-xr–r~{éôÈùÃr”-¶àÑ‰Ğ#°¡œzÒQ¶‡+7'–våà7ÓŸt>K·Yøâõ±ÓŒ/\Îø°Ãmœ¯/ù’ûôÆKlOÜ.<q£ÓoX­Øf¹ƒÜÓ©ãØß—áGœ> »cÛ‚JÄ	¦¶#÷™‚¥ê<ƒµæü†¦–5äË(a½8·æ3ù©³ñ!–œßÑ<¿eËn¿p5ûµ¢ıNÌäâø;ºçuşÏ­êÍè4Òª&ö(n ,,ø<óìÎÉùÍ~Û‹5„ugdßw&§
:NDè;rº;vú×¥ü9Êis;7lå]ó¹ÍùË/|ÚzşšKîù»:ßóºÌiİéô»¹Î>‚>Å™"Ïƒ\¾ÍbûÈm4³/5äÌ¬¹¯;”]xlfÏ‚OÔ«êª¥0˜ì©Ûço¢,»>2—OeOw¬Ëìèg?úa×qvËı|Â¦UwsˆebOİßúßJáŸ¶¿Åf#ë®Æ,\İî§œ_yÏ_¬x‰Û¾üöëWŞoî
M_l¿cå;x~¥^yŸ˜İ:8{ş\ô®ëÜ‘‘³Û[çï6-½îÏjıtrx>½çÃË:‡ceasãnd®õ<ù?9²dqô,zó!¨Ëæ*›©=9ÀÖƒáºè¤¨_E¤°gÅŒ¡¢õz¨½%Rg‘n|m­±ƒHºÜ‘Dâg8Ç[LWò©/EÈğC—ƒÒCîDîQÑ~­õ¶uJ¸ü	í['mí×{–—
#,i\'ñkš,şnloƒ0³it}ë ¬7 YJÒ·€Ø®÷_+ Ú²®€hÇºê-ßÈä½;Ü@Ho$×iîçs°öÏk°&®¯#¿Á¥cX 7Ñ´]^À£†vu •›J­	ƒ	<¶glr(°±_]Ò†u}tÇÒ5Eéé:í”wåw¯XÎ±c¼Å¨:PZ£KëA
“ğR
Ú³NZ¶*¦=ë èlá5íYPäl«ÙÚªôrhÍ×ˆv¬k@Ú±®nMß(’Ön¤§µ’£´·s”ËÖœ®Šƒ6¬kr£ë «†L–TÑ b­ÂŞ•"€yøÔë a0–4¬K°Ü³É¤/†vu	@›Õ‘QUúdò¦'JEÓ(!—ÚHeëh7g›ÕM4×¹İ¨ÎBDnK£h¸Hc§´bRX0¤‚YROñ=p¦õÁU¾´nMã(‹ß&XÏµöëIÃs/¢ài]+²’Ÿ–ËKj°íÜpŠ Í‹æfÀY[³(:ÿ­fàÊ]şTo=‹%Û÷Á¢8_ëƒånÌCJ,ªÛú\ÒsÉgÖtó±~Íã^4		7{]aïà+ÓÌhDI?h¤{£uàtÖŸå¼qã9s"uŞK$n\úûÊ1	O°mc®âŸ‰Ş·Ù£4®vrüˆFiÃ¼F
àr?ó¤ì©w–Üö;ÃÏàĞÖHØ1¡;«¢µ3\cÃR2à¿«š>nØ[GäÜì›ˆÍ·\<cKºùÂoÈ®×Z›ç¨ÿL©ó0¿%Ê,½kÂó]¡	_y½¦4˜óÑ:P©–’Z@AŠbi^]j( Á³Vàq°¥Fì¤Q_Ç`i˜`¸œ’ºF‘„½U@Š$ì­TR-aoUÃAj/B©Òİ¤šküQXKL;Ğ”™äæËlÀÀ<c$¤ œóbZÔ¢ó“…7€9lİEP!´¬0ZVX|Ÿ¿«ˆRÒ•ÙHî:ïœí¬åXû±«û Èh%3êMhGë>€	(<s¹YË	À	ò±V} „ÚËYMŠ>€eQõ
FUQ‘2GUQ‘r¨ìESŸ¿WW”^‡u’{½ÖYë…jµr&IÑJ P „àH¥0¤=PZŒÀïPTaìMPÑ,ÒR`è†–z6v'o@Zò‘ÑUôIÓÑ@NÓ&!œÚFep´—ÓÍÉçR³‰šOGIR³C>.zî[ã{jëZ{[ûşºö†5%wNÏcœeñ5Ç^’7£İ©G¦2#ké™Úİ–¼¡’kÔ•òÀ]-‡ï,M zr¢”O–Ô¢7-a…®wei•«ra=DëœÄÔ¹"Ï˜@sAUÒ@¸fjk$š¾U¦#«:E™NîXt¬Øá0Á=ûGÇ‘¼ümñâ¢@[ÜA˜^Äq¥Û-Ò‰wSRfÄn…½¶ÁpÓI½¢ËsK6"¢m•9!÷!!‹íÃ]ògSƒÄûëÒ·uìUé/Ü¿€I·€_j4²w«2!¦”cĞÖ”vÕ±jzôy£_¨*í˜RUêˆ»P…²€~z\Álsö%MÕ!1y"”ßÜg‚º·:&6§
§®ÄÃ'í1åyÃ>ƒ©‚KÙñ”[Ûu½oóßİ*fÅÖ†*ü5„‘Å)Q-ÿ5N§å%3‚uNb2¾|ÆÒ‘>OÆBæŸ‚IÛ®É?ÃY‘Ä³Ù²ÅÖ	[sîÅeÛ}êIY?+£+QèYäÌ@†â¤_!§´’ÅdÏí ;_³6³ÛŸ=lõÉ:qdÏjèU,¨W~…Øæ€dR&ñ˜ë¬(¼4Ï^t3õ½…Á2¹¨àóÂÛñ
× ‰•Í"úéyQo=¡\Âq-nŞÍy¬x?QÆ¼
¡Œpş?mNi
endstream
endobj
63 0 obj
<</Filter /FlateDecode
/Length 4672>> stream
xœí][o·~×¯Øçf8¼(
Ä’ç6úÜ&E!HúÿÎğ:Ü=ÔîJ+»IeGÖ9ßÙ%‡sù8.O„Ò1ıY$ş}'ØÛ`@Dˆ1,Ÿ¿ÜızGŸ+ä¢­ŒËoÿ¼ûûŸ–_7^êsã;¼úû·–üâ·Ÿï¾ûA/?ÿ'µç£^ ”¢æ~Jˆ¤Kó¼ôı§»ï>š%.Ÿ~Â†’„°h/| e¥—O_îş,¥¶Y>ıûÎáçŸş±  Â0kÀ'À7@Ë„y 	Ğ°ù–Ø “ığé¶à¬P<“üºµêÖ’o¯Xô˜\1TX*¸È¸¹;>}7µß-õZÜµüòia´T\˜ÂŞ×»ÿŠ½pÂÑ³ iZYôX…šwØF÷Z-Èƒ¨‹üŠİö.Èzı®ÿ*ôø¡8°ˆoâÿâ}[ÛPR l6j·|©o´õË#½1€!!I¨….pÚh(˜6†0¥j×Ií—Ïtw .·g…×taŒ01_Æ¹RºbJEºğCWn5x“¡½öh¡‚@L	i´
±`.ºY¡TÑúz%ÊKW:$*F~__~¾sÑ·wôNh¦_Lˆ³RGÖ$aÑ:ç‡Î]B9E71	³ÿ°áæ÷n·‹Q`¸ƒa"‚
M*AZF›ÂëÍF;«ši\º’lh˜		«FÎwUû?ŞñëA5,¼Y‚\i¶
@X´º4U$ÈŒ*_WÇCÅQò‘æQ¤¬·ª#BÉë¸.£|´N˜–Å~Í>„š¤¤nÅ„¥ë}t—ÒíÍã÷z9÷¤Ú,÷¹. ÷Î**sâ:"îí}ì,,ª’xğ]ò(ë:çñX­Ãã¶‘ùç»?„%ÿG´P_'FAc!¥¼±Â+¼±Âÿ+üx"k(™GnÁilµÒ„“Øò@ˆ¨5M$L“ú &Œ4(©Ñ0H¡ îšK˜ÒM &×4‘°M$Ì…8ÒDBW4‘±Dåe¡‰òn ‰‚17lM2‡e3×nb²hÃaÁÒ‡Í¢ªé§Ç^Ó"R¦oÎÍ2,ê›/$7–HæX‚K$hÅ	[³‚qÅ	Z±DÂ6,áŒ”œ!è=¶;è› -ıH	5I?İ~	«‘ŞU‚(o‚h—sªÍroëp¿,’2ï¥±pï#f¡PUÃ#¦h‡V×4Âj¬Åt,²ÏdoTğFoTğ‡¦‚g§	itl\­&Ù¬&¦Í8 ÂrrËGjcNƒ™BZsaëå‚›åDÂÖä@Øf9‘Ğ59$,“C~YÉ!¿É!cÜk“ÜY{çÜ««˜ÜóëpxŒôqóhªb1WõÈƒ³kœ‡qµöjÃÊdåÆI³;²b‡¹B:E€„Ekv@Ğ8=$ÌjàCO˜wa¤D-§zOs•'Eù!¡(,ç‡ŒU~Hï*?”7?´Ë™•f‡+¬ø¡ˆÊø!†y9r‡¦5M‡,¾˜²Y$6³°ˆ­Öcá}&Wxãƒ7>xãƒ?>üxt?dùå5.Tô˜ ĞxÙ†½‹4WC€˜k½%„1 êñ­ …D—‚˜ªPF9@8àHuôt­C=XìAÔ!„€brß&- ƒÁ7ŒŒ‰nÁ;~3‚Tá‘–wƒ ¦d€^4ˆ¤tJaA ´Üó`öª
T=˜ e¾±t¨ äuäÒM¦	ŒL–»Œ0‡#L,šÈ˜Mº­«¬ª¶ßÛmĞûèæâÒtËv¹»ôñm}‡¼¼JIÚ&
2¯êØ»ˆø8JØ(J0´d€Hf±4Ö@œ$ˆ ,y•OU”yöA™)8Â Õá¥€ñfUH—æ®èæR"»X}ª€äTù HÃnVƒµ1t¢Ğ9ŒJ.ÅåQèHÊ‚dWèt@,ÁGY@Ÿu‘n-@UØã]¿3 ˆèt¾±ts Ÿ¦æ&MÀ€GBI4ĞG®h —>¾ ¤º3U	ËeÔª°¡,M­ìÎª~ÖA3Ô J³)º{HÜÆkª?Ø´E†E6'V_pÂ9%Zc}¥”öÁ-¤|ç™öSĞñCÙz6÷øÓ¶¾íKçˆ°©ƒ©/lÛuuíÒs ¬y‰DaéGa7ğwÀ‡¯qjğ‡p‹˜-×<ä{àãÁ{?æ!àíù7Nğ0l½oEÕ Îó W¢îÜ–5g=ÿyJTú?J¿“˜P®YdÙöû…!¿C'ù©‘áı\û
‡$!¥Š\DT‹~B,êÚ„•øß—ß¾k”~§k<»r{	·Å‘r{Æ‘ŠjìÎeRDq0ï~Çbƒ…	ae¸C†Æéé¼¡gş,?ThÚˆNâbÆRŠˆqR¤ÊÇ<hò&ly²†:8HO*!ÖGT’Y?–Á†Lêqş:ÓEëe7tq¦Á¬o;fQZËÜ¶h²¤]Yñ¾Ä‚í1r±g<£ ¹gRñä>á"MsGá:8¤3­7×_áX”?¼âÔ›?jŞ]Ï«…’:=¢7´H"Ëf…+fH{ä¬Sì@İ—àı™©uê:Ç×Ù4	VñÀŞÇóÅ-$…B‰™•òë8ÄÖ%sf€¡zúŞı‹Ê(ÜL—z{”_F{/§h´ßvÌ—iEğÕ}™uJ¾ì²&¹ïÖÜ„2AòK¹Î WyÍÔ×¯ğEkÎÊLô=_ÄåC›¸š_÷aP¾^ÀËœ —Áã$"I&_iOçÇ†i#qA	ı‘c“ª†Q­«?W\¸Œ‹¾?)[Â „Æç6Gá´u˜ÊõììƒIßõq]á=2X—ÕêICÏöÃí®M¶9.ÿtˆàîäz€%º™–èPrènÈ¦K\¼ãÄh·*ğ:FÕVÖê`‚^K)åöÒ«µnªˆSÌòiŠÕƒ„=j„¸L.(Ì­LåâØÂÒn2!I»ÌPù.M‰yZ«S"ñV¥…:Uß—3†ĞRÇĞóä%¯(4Ri(ñ`¡—6:¶\2¹Ô¯éSbj§æ&²/*Òg&Ëuy’ †êh*¼Ağò( ÕÇ†)BÏHË
¤$Däª^pCL¤ë£ƒN*Íê£	$rj¥¾ŠğâhÅxq´b½ÀÈ:èµÈA˜^¶ìr÷ò&à z1–F›ÂGcÈ¢G÷N”
 ´Ò¼6ŠÆ¡1j¨"Š6ÍÛ £Ò#ÕÅ›"
6GÈ«£ıînŞK7—§›µKŞíßGxÃw¶åQô:]Üªƒè™*ïX0ÈF(ê[5A/<¯"hEğ2X^!EÔ 	$¥	­”P:ï¿ñ
iy…´ßÜ
¼“V“åiåK.{«sòQ¶‚hÑ¯‘6­ñ")‚è˜ +’"†¾£´f!†ã²:ER-ŒeERÄíµV$MØX$-/’²;«XÍVƒ(Í¬Lhî'up[ßyN•ô@Ö¶_!uÒÕr1mcæÂ¼5Y´…õÓ×Úë}¯wrouÛ)*Öõ¡„ÜÉàN]²uV•ª:9©&îËkRµe9ë¹ŸÕzA–á$`İòA¨Z¹UA¾püÈÜF¦¤‹õ™†«4P‹¬ıƒ:0¯RÛqÈj¥]‹k.ó­·®Xñ7ô‘’²‰×„VzÎnÎ…"»SeaUOÀ\ÄIk†uÃ>»4‘ÃÈ,¯³“@3]õ¨À+H:”4µV{î™L¼İ!™«wŒkywË>8ë8ŒL}ËL;fEı_bÖõN|-cb¡´ÑaËS&~BÔ#æNøpıfÿÄfĞÖ‚{‡m1æÉëoì*¾Z{¡µ~Yñ§)Ë<¥†İÛ±˜÷BÏ¾_sòeó¬Æä±”ÎØ .™dÓv1¬T³¿É¬ 3nºÃ“î³Ş«ÜÌôƒ×)Âb†ïdu¿aY=AÃkÉê°•:ªœ|YÿÙö¤î}$ÿ!J1WÑ‰u€mw¡I§’è¹½e§¼;hß—óÆ"ö·õ¤+ÒQ¶G¶äRnlç^È™¯·“Í–!êøN6@ÖW^9·•íôz÷A<g=«?œ Şç8å)ÍË'‘½‰^!_'slÔ´§Öõn÷µÎÖ ®]O÷g˜¸ì©øq*&Ü(b§rQæ¹·e}ŸÛFwºíÏŞåçÜ»Å `"üÏlË9z´»rÛl{êcÙ†2çq¶ËãSYtŠ*Ã»]³}¨¶&	šµdUİé"ÅXv·Àf]èïó¦£@Ï6¼÷¥)m <°=©ÙöÛD§‡=İBœ¶dË—ı û;cœİ—éa2†0øííİ.ÓöÑT5P6:¾¡gŠhI•:X[*Î1¢nt¡´Qo¼É	etô*¬ÇL§ :x•.2ÇR¨ÒÎ©}I±(DâJÙE³ö¦TQ©µ+cô5ß˜İJö:õÆ4~€wÀ~ßçU55ø¼©Pƒ[£ïéb2Šfét4Ñ­u3zˆµ»Æ››{5•Ü`s#œÏ3hF8‘GF,ã·‚mcL‘WÍ½)YÇk«ìíÖèÀœ9z6ø©¡
Ù:Ú®CâÖ»êºĞAçÃØ‹@/¢|òy(£Ğ4neöû¾0ÈO«°<&Ñ×İVØ§ÃÁ§M¾c>ğïkF¸ñ8 `Bº˜Ët–çÄsŞmõ$4ÎœI‹©Sîà^èı„÷LğB€3ß^Ò	7¬‰ş¶Ş­ŸpX”-òÅ'á}tq±Ç?¨[‘I¨÷»Ù°ùŞÆ­mI>%®-1
$kë}e·ˆ|N¹É8ÅŸjæ»CS!L¨‡Ûi*ÔyòùÛoî œ`pñp4ÚI}c]MÙsâSB²3OIòÂ9k:=Lû˜‹uİŒ2›.Ì3ç:<=ÕL3¡óÒ^7	}Ë	pîU5?³Hl>°%ìl4§ıµˆDFw`öû8f'Ïi:iMyç`Ìò)sNn‡”sôÔEçÓò3²…Yút~1ïã ù¬¦ÀokÜ¯¡“Ó4oŠçşû«õcÁx±oæ¡Ï0ì,?œ[œÃI³Õ9Uè›&n%;›*>BbÊ¹¼çûZ‰à Õu~8w“óâN#°­èùùx f‹TOg•Ú¶f68}ó	ÊÊªÕ²h”›7ê9×Íò÷¡êı®JÕ#>R@¤’ÜæˆÊœr·‚px–Ÿ–Ns'	âùÚÙÂìéÎ§Å'ë/çS‹Îe=¶NœùEå—yæ¥Æ©®®[(ŸÎ‚®ó^+Û™Óö´÷Yõç|ò;]yO…½ úFËr"ÑzëÇX}#¼Ãd!n6âè[¹67hÏ£½ŞœœÎ4Fûô<'œËjÙs_=½¾páÛ.D§Dpººqvÿç›V¿Ïî%³Óı/œ–†Ï{áTªçnÎì$”íáĞgìDLvê!§©â´fO»´¼ûš¾Ö×Âï¥'|éyÁœğm_xQn­'{‡ç¯:ÕkÀ¥/8ã‡zja8Ò«}K¥7ŠèEŒ.ÀÏˆ†h…Òçy5B;	ì8/bšze‡SÂóVŒç­;ÛÚg§g™$ìœm™Çm#cŸä­:z0­zì/b 0³PLÄ´ šrø9^DQf‡ã5ÙZuğé-?¾› ~t7]Ï½ÍnŞ{7]—³›¸gëÛC»Œ«ï4TQ'vPÂ$sô“QI¡$ğóºØY ‡Ö?®KàÀéËFû™ÒX¼˜<­?­Û@~Z·ßÜO¼ö>úÙX.L?EÛÅî§mûğú±Ü¨ÆsºUQü˜.bôÿB	‘ÓEŒì¸(¬DQÂxL×Ğ4(zî«Íô“ÈU†cnÚ2ìsÓj¿¹êuÑŒ4ÓÌÉÄæ¾Q‡·ñ—owN—ôotN·w}ìéU‡„}êzWë­sº½ç«Ïéö–ê ´£N_íœnï®8_2j6œ;	äåödÉgt½ª‹Ê×;£Ûûøšgty¯‡4lÖÿSÏß×]&ÿïâŒ.“÷Ìİ™J^ü_¬ ;˜
endstream
endobj
65 0 obj
<</Filter /FlateDecode
/Length 4450>> stream
xœíÙä¶ñ½¿BÏVæ} A€Ù9üœx|À&vÌ°óÿ@ªx¥f‹ê–ÆŞYÏn«Zdİ)–<éÃÏÄàÏ§™\:ÅgÏ½wÓ×o—ß.ø½PMR3?ışïË?ÿ2ı
p5s·Ú8C{ù„şñã?üşËå‡åôËÿÂ|ÖË‰s!pºŸ„á­ñÜúùËå‡75ùéËÏ0Q OÒÎÖq¡'!§/ß.eLê¿M_ş{1ğı—M n	PK€ [ ’€ëÏÁy ÈĞqˆ/ '}ırpÍõ,¸³„rn—HÄ	_R¾¾cÉ=—K@ç¡ÂñÉ€«ÑO·GƒRëh&—ä.ég·‰‘LPbVûœGÿşüváÜÌÔÄQÒBƒÅ
¼9ªÕÊ-QÄOdØ''•ä3 7ÍW€Á;Ï“ıÎŞÂ ú7Œ[aÁf ÍëÓ·ta´·Ó;^(ô? ¦	o0HS‚I`Æ3QîcÒO_q´ã–›8Ÿ­x§÷à0	¤Œœp'…&DÌáK“Æ*¤ğF+™æ8ÀÄÌ”Î'˜q Ëk›ïÔˆF ùNY—ah÷ùã×‹†óÕ;^ÍRrUoFˆÑÈXa^cäÆ»Y2¦%üvfµ¦áÛx?ƒ»sE$„0î„#rDdŞøFâUÒhAt`Ş'r¢–µGex¿ûb˜È´d@.„€ óZ§©"¥ T(†‰0`MX0k²à’ ª'"H¼Æ‰©ÈHˆÊËÊ	P v"*Œ0DçqH¬åâıBÌ£ÜNÌ(MÛ\"ÀFkÍ¦™Hªfˆ•–«;Ù¯)2$şE„M<±¨…xlÖqï¯—ÿ`dpSüBşb	(	‚É÷xğ=|–xğÓJ!Uq§ ˜ÉÂB)Ù€Øe€0É* Œ)Ş€¡""€"À„lâƒÅújlÌ8ßÆ‡ ]Ä‡ñ!}Lñ!]5ñ!Á¨	æ)©±VäÔ¬3™Ôô3;ÔI
ÛÔ›²|ˆÓe)Rï¬ò¦~œ5Cİ=k0Ôq	AıMx@È"<IQ'`^Ë&< ´jht A0`Êâ&:¨ş\D	01së¨ĞL2İFˆ URĞa9B„«!ÒE!ÊíÄÊ´ÄäÄ8©Õ†GÄÖ	ïÕ)ŠˆïdY'#2'îX´CÜ6+‘øøªá{Pø¾…?IPøit—cúõ…ç`8€1lr|#°O2İı^€
 {Íœ™èwèf'ã T0ü (cJI¬½¸ƒ*L	ÃŒ<+ká^¢Ğ@] :«<ÁZTÄ€A`)³õÜV ª*eÍ­¡ÃVä™¦ˆ ègÁ¡mˆ’8Á( äèu–²Ú £PÂğÌÒ{o`°ª€Á~ªhÀºg)¤§¿‰ B¼×èI‰öÄ¥×à™A•Y‚òÍRË0TZo†U-Ôù«Â(%U·•æj•·µ¡¢m	†½”¼pÉ¶*ì“ğ,ÙV” é0™è™9ñ€PÔ‰AŠ™ÙÃLvZ±¸„^ĞM>¡P™S»8z‘p"Ñe@”\Ób,ÈÛølVŒ“²àö©f˜°Põƒ4ÂBhR-ÂB`Ó\4të‘Eİp˜€¶Ê"OÀ,´÷Kí%›-æSEã%(J„õ}¡ÈK°JP"ŞK°# =Ü™¸ôÒæœPD°÷²´"()B%ã²ğÉôEM!E£„äj#•µ•İd‹ß’qG8ş…A‹£R—MaC™C0SÍ–²Â•8¤²Å5¬ß˜Fõ—ıüWøU°vÔñ_¼Ö¸$t	&à÷	>ã¿†Ï<~ÏÀæ şÍpŸµ‹s°²o=+”0hÃÇ§Íu~²fä,]Ë%]%C›ˆ>qƒÔMVU¼¿ Bú€*z:™£!ÿ¹y°¦Áü˜Âm+ì‹‡X¿ç~Çôê~¨u ªÀêbò]äy	ësmÁ×|ódvÔ…òÈ2‡ô,Ê”O,0XŞƒ–Ì‰¿e/¤{Ã`‘¢±òÃ¶ÆØg@BxPPŞº†ú´êÙH.æøÔÎü²a¡Ê`’Ë9Ü4¡¶L÷‹)ôRoFn8àÉæW©<âFhh>³tßSŒdÁ¶2¶†¼/Ø}!ã`?RÔQáDB‰§V¬m…¥l	¢+}méWÉAı>78ví· FÑ3qÙ%‡Zï
®A¡qfÌ,³ßR~sGpÏæ	–ÍøÀ9,Âm+Wx¿)+(ˆî#Mçàr’¯;‚ÿsrâğkKšÇ“ÈV¢‡õzRÇRLbõPìß-ÖäPä—Äˆ½"ë‡å9~Îs•ÜtÔãA;ëÂ`+AÜ°c|ú•òÜµaºpÔ÷g9/	Ë¦óÂzÙçœQ‡¤Œµ4˜Ò¬aå“qÒ6ÆDİ¤Äi’1Úd Ù8_Ò÷)	çd‹F|í¹úiHÖ†ÔüWw4näDNéÈ…@“}_{\#™»c³Ó>dèkB¿©$½^ ¨¤:»©‹¨tYà[
†v!DI¢ÌS š®A‘°²÷ÑE\J÷:+^$?§ K«.…Ç­"şb O5@ZızL©úrpwinİÏá¥‡‘bfNeGy7•mÍVØ¿^Uß—Lã*hƒ0¡Õœ+©}gY£{øÔ»¥ˆáƒh•—¸õã q±zRÇcz÷’¼×²¸Ó±^w3ã±bu/ìÂtd.Yæ2Î+2$E»ğÎkA°Ø„E)î-«ç2Õ[ø"Âğ–‹úÅKúî-Á¡-é•’‚H¬oEbgP¤tµ”nÍyoÔRzVLzK¾Èv+é½ÔKyÀL
$ÈíRvv€ÃÒ6á0Âz«õRFpïùRa“Ï{Q¥¤]ÂÍ¤öFË²ò€n¯5_
ÄÎŞ‚…TpDË@«PÜm¡XÉ¼O-¿Î^2‹§E¼q|M-„uo	Ù°a¼˜ª«¤ç2úl˜D•P@•p˜ÊSS‚¢Ä6U]ÛérŞ³Â®6öd·l»’zĞ-s×©ò$zîvË…v« ŠÔBf¢¸©#ãÃ±Í2óg4„TKN&9¾×ù3Œû9»>x¦SQ‡UÎ^7J.g)kp(ó¬âfá*p3Âyc¸+¤KÃ‚'Tİ1ÍšUoª>òYu]ù• ÀçÓ÷[OW³*gê¶˜ê)WÎŞ°+ªÀ.ƒ=‰ì÷§“¼Ÿ–cîOqÜaë¾cn}×ìèËJ0(zwV0C¦›¼ÀàCï6ğíI?İĞŒİDÄ.çİ©¶Ê¡Û¥,gy¿¬ñş&_wyÏ—»#úÙtw¸;ºX7Éx¯pì.ºÕŞ‡pŞÅ‘#ìmn×ñ=ûöv\qº{aÓõ¾6<Ë%ÄÕìXæñ¦Æ@¨È?<3Sw«ªıY`íİ­rûµ^O¸ûSĞşêâÒ­WšŞÁùXRÈ~İŞ[JGj ¬ÚïO}³êúÓîÕÈ%h—’ $HD,îI·Bë‰¤ï7]/Ğ=ä=›îR•zÄ7
4™w¶¥OóX#½2#™ôÀÑsşŞ®Mw´»Yõb]öúSu
õ”áVmj TdçcG'éV€{%Û‘Ûe÷²9°æÿ€¬¿Éº{Gx(Á6>¶Ûcz#øS4tl¦à{·Óåîf?Ávqìõı¢jomôdİêmG?ghÊÒ?´âøc÷vèsŞÅÑ­}úÂI|–'‘Õş*eiq\}ÖbwÛë@cè‡»7÷#¿ÃÚ»áŠ&æ+U&ƒâ	;¯¯¦_=´wÿ6R¶éüˆøCª³ŞÎÈîgjûsl­bgëœ˜æp6vVùà×
XNtt$çóÉiAO¶à‰
<E’)Ñ4xÚ„¿\ˆ|'gñdF>µ‘¾ÏG”ğ³"xx>•“OäàéœVNìğÜ¡Q&ŞÓk§•míø²É à`V1Mšì Èg Ì:Ò³@6kÇ¤hšì¸á~–&Mv „e„&vBì2Œö×eXíO#j+[CLíz#„×ö8Âblë‚¨Ş[€™­Ğ†tÕÌÍàö´«`~V<õgª5ƒP HWÀ8Ä,Oûê"¬í«Ë0ÚWWÇVÑWUK”šªĞJwÕ|åoa/ë¶:»º3€›ĞçKÊZ‡¥J÷ ñ 'W´Ÿ€r––9Mûé Ê{†m¿¥õ€±[­ö‡í¨+@ÚUW—¶4Š¤t°µô”f7J{éŠ£\–ö¹ ÚO§ct¦Cw°s4Ó-ÀIB
ÀÀ¹…k›é ê °«ÉÌ,7hf!m§+@ÚQWgéEO1E¥„lj™½Öbîè¦<¹İQg‘‡Å©UABn>ähkH¦­Iì-!‡ËéT2^¥Ã!tÓ•”X>x™O²æC‘©%¥à!t”€Ë{nªMt”1¤=F§ûãuS[\9ôˆ¯ŒG¶©G=ZÈ­åYa‡²DXšüŞªè2;EŒWØ­**5ÁãgÁ­ğ,Ó]2t™ÿó£¾t®åLò+G^ãYåƒXâñ%•§V^æWèú&ôA4•¹ïìÃvîÕ¬šİ<™¸Ê×¤¯ë&•[DĞbèŒmŒ„¼í^=X×£°\GV·ì_bU…Ñ^¾jH[Í,´ó®Á5D›¸Öjğ¸JeÏöÁŠb¤Çø8$l”ÍÃÜÒ²İÌ!òMFË§Ó™‰1ƒ&¼©‡Ms.=FÖ!*İ®&ZXB(’à¶L;ÔäëA²XQ¥£i—}MÉóÇø9:](º·â½À7Ë$»ZpòJû[µ•c8rö,hh9’Ï$ea°ş|dj²ü
GŠm¥&ÇZ:äª¼Nú´@^QĞ’]%÷n`àÒTíVî‹ßg7¬5Nj•
13·rñÁ–¡çÔ"4ö¥2¹´!g(@*Ñ„ıƒ4`X-<+ŠuF9BL\Ã5Üeü;›{F:—·2š°,g4JÁÌ®öd‹¯ĞOöœËÈ´ıÒËdËÌÙíÀfdBÜÁÍÈdæºÙş8éµm™’ÄæˆüÅÅY”cFÆwµ,(WGQ.m^àC¾Òá½òíQäC,O¤¼İ½>®ex–=Ú,¬~³FÀ7Šá–¨ƒ+ïO¯<]I/ÃÙ/DñuEMØ:¬D HËÒÎ¨½½èÃ&a¬ÑïÛĞÜı+Šó³ÿ‚ÏWhd«%uè7ÓIS^{_Àãn§µ9Ûí*Šs;ÂÖn×²t½0?¥’¨ˆãcæÃ*	ÂÑP`®lhRa™²ÕM`¸±´ÛÃèê‰â¢ËŸ³6üô5pEñq.FØ:ÃÅZ–>ĞÅ*âPò‘H¢‹Úm¦ÇöêŒ„úÃÔ+¥…	,–ÓR‚*tÄ<}÷ ¢8¿~X°óhı@§’¦^oÜìéOK+Šßà#Ü²Á×²ö‡oğQr†ŒÊùÓ]´ ø mÙôã›{øT-Kßí[`á›‡Îpi+NøZQ|\½BØ:£^iYúÀz¥"æG¼¯õé•ÈuãŠcÈ˜Õòñ¡!¥¾`:ãåÖFÖ¦÷É~9u|ê_QR÷áæ{Qgzó½³Îäÿ	n#Œ!+0Ë¥aï÷ô·PSZèé#òÀC“wêüBûüâËCRã{ôÓ^9!g3©gÛT¢ôìøÿÔ¦‡Ñ
endstream
endobj
67 0 obj
<</Filter /FlateDecode
/Length 4903>> stream
xœíÙ·ñ}¿b¸Íû ‚ ÒîÊÏIä”ØA°2`çÿT±y{º¶Ù³œµáh¥•fª›dİU,²›‹Ò1ı\üùn!_ƒ‘K”1†Ë—¯¿<àue‚¸h+âå×=üãO—ŸnéàV¿öĞƒ†ò‚şöÃeığëOßÿ /?ı7õç£¾H©v÷c‚¼uı ·~üüğı's‰—Ï?BG	CyÑ~ñA*{QúòùëÃŸ…Ğö/—Ïÿyppıó?/ Pa0[€O _Z$@àû2tØµI¬ ³vúüyq+í¢dğsé·ƒ¨Í r‹ùõ[ê¥Ş˜;8DU— Î8^µşøzkjk-ôİ-şâud´P™+†Udş
~yÒ-ÌE"§•UÀy}4­Õj±~"Í¾ğ¯[PN‡ú«@ãC”Y—è¡+ú/´»BJ,€[0€Ü×üÅƒj\^ğ‹A	â©Şà´Ñ2Ã´	sQ¨zŸ0òò[é¥[ûs‹×ïŒ,&ƒŒÓ%ÁĞ•Òúm%\s¹©…6ïóÚƒ„2,H€)K«3ÌÁ'h¬ «h}¹Óâ(
°Æ‡C½/¿<¸èë·ü¶h-M»!Î
I—‹Ö9ßîbX”SˆpEaVÃ!aŞyï(Ù.Æ¬]Â„É á"‚´ˆ.vüF¨ÑÎ*"™‹1c³JaEÆk«"ş—r?B€Òm>R,Ú‚ıŠ) Aªë}™²*RÂÌƒš¯lË,JPT:ÂJ€©Eú@™`Zdññ$(èÄ…q…¥K;l¥tıòò@¤ŞN©vKT @”³¢Út¸RDtĞŞŒ¢2‰ØNá%12ÂsbU:Äl‹‰yø7º‡pYÿ¢W(Ÿ“CaGùæ¾9…oNáÿÊ)üıDÎóÜƒ—ÍKgbï% ¶^"Á´é	@Ø•— ¨ßx‰Úx‰Ûx‰€©SŒz‰Ûx‰s!ô^"A7^b…%/‘?f/‘¿u^"Ã¨–.©Â¶Á©j4©	r¨±T²©UşÛ+\¤FÚøMÍ¹H†Z}‘`ñ(ãæ%Pü½— ÈÖK ÈeçS@X´¶÷^^y	Y2%aŞ…—ğRu¾C¿¿¤…ß8„šÄŸ&¿«¿U±~éD¹êPé–j[C€êeÆ”h/ÒB5¼QLL¡°†ZLæ 5­Æij„E&ÔX³èˆeŸJ¾¹‚o®à›+ø#»‚¿7.??€%¼² l¸ï+~'méş—
5	
l±"èB£a…ê%(€ï‹Tğ“ ø‰D|>,ğ[9™à>ƒ™X¸íÇÂØ+4x6&¨Š)Xä1šÅGé	E­ô®ë  JQØn4€ÆEI7¸)-€µ N% •hx¾£º‡®J=dheæKtr‘B„K
` œ X-€i Ñ¨•ÜL@W‰n¸›`N™DjfK†ÙÄíÂÁ
D1f·ÖM,m”&BŠOwÃ¼)F£pG¯P5Qå”À²oŠ1J›¬r­¸öPğïVP2&Ay`¤Zƒ8\©lR9£[#ÖTüJÁ,N&¦‚ÊP´'´gİ4.k›‹UÛ²¦Aß:Ó·Tğa3Šò0T«¦Q””Z¬T=ÊG¤ÖöÄf¨'ŒI=dhåáËCë €À§S§y(€ÁUî¢¢¥”İD§šºÌ$ T-A›4x&` «Ç,,Yaë<JWE[a€Me1i[dA†¨bë©"&hS½)ä]ëRQ³UÛ«Æë?è1ê!m>•ŠÎ¬Ãtegƒ3uá¾”±éo)9ƒï‡8ƒñæ¡,¬maeãzïA<I%ÈH&Àï'!¬ÃÏu¤‚˜Q$Ä£uÕŒ"Ÿº¢û^+È.ò:KÇ‡ƒv‰oàvùvıkñ×¥ğ?ø0!jII1®Cİ÷W(ŸåDæ,ÁÆ±jå,cÌÊi[Ø	œV*,™cdÔÇ)9¤ĞRo7ÄhHn¶÷¿Q)×~mY¡213mƒÀÏ ¥+‡ê¨I³H€Ài„ÛŒ²jØ${b¨HšlVM6V[&ÚÄQ,+™¸/è9•z¶ÀWFö¢Rº”÷’ ƒ Ç°G)zğÀ‰êÄ(3†´×«wr¯m¤k‡3E%âÎP‰˜Y·¼€´ºxiÚÃ£d¼mùæqb
•TeÅ´œ—©§E*JÓ"Ì”®¡…y.Ì·Œ_cFRŸìÀFK¿.óÔf
9‚<gÛ—ÙöË5¿Ş‹°t=d…-úà½©Ïêd[T4å>ŒPO“rf´F‡´1Ã´"»ÒgBjfAB54ÛB2€¢ô¿~~k@ã¨.·á]}XY—p³985L B?Ü§N»n#Eál?§%ÏÙ+Ù–– ÂÌ¡(ø{Q¤…a(ÒYOà«Átöc6‡i/ïFÌ²İCÛÀKÚ8™cí»fb¢X¬ÜÓ#<ŒUªf Ó©Im„Éõ“Ú6Ä=“ZBÈ]’ÚŠı¤6û¨ÔÒ÷‘¨ğ8˜V&§¢äª¡@úYû$8ÑŸ6Reâ	lµ'`„¯:Ç#Zä]£ïÌpÕĞº·sïÂU.Z(\mêØ7 /ÈF&¾Ou"­³A‘™e å,™TúI ë}kq(ßó”mr8‘œƒX²Ë äÍtRt]M»cı¨”ÙÕô#é:áŸ;cìˆb‚ÑwöodˆûÌ—É$rKÎ`$é<Şa‰­æºÑ†˜í®'ã&–A„:Á-K:A„ZÓ¨GîˆGbëÅ<g'ü˜m<O:¥8î»o7Âèhƒ»Í~+åÆyîR¾§ëO­°4I´kÆ“IrÆ½ø)¼–ğ.ı8rolÚ°w-ó>’—øÒô¹àã?µ±Fµ?å?¤ŸµıQnÁá…4é¦¬R?ğÅ·¤º"ŠÁTò\vıåshí:Ö?’ÚÅSîëcf_,aeO¶ê\Xæ[Xë×4^íÏúmÏ-´u"{Ì*¼¥íó°ac"ßKÜ|orSj/qqKé¼1öúšoş–µ‚Ç{Ô^èp“k/[JŞ©ö2›"R{ÙPô^µ—éµÚË{h[«½Ì&„Ô^¶„¼Cí…zŒµŠéÌÚK±$ú÷ª½!jh#ÙFÊŞHÒ:…#4M+ÃÓãAƒéáhæ¸ƒñêŠ³#Ñ
·ö³´ı‰tŸcµ¥²Üîy‚®{£«<;ãİ¥Z„L;U·„?“L¨¨àáTÅ‹„ÇØ®¯§63¦*¸•‡äbåW÷y]±ÊùVÉ»6S’äñäÓ—¬ÓİTAŠZöH¥‘²şFsÀ)I-©Ğ²ÉÖñßÓ)§ò|Z¥›”[¢ß(ZãO­œ÷VNßîñµ(3—:˜Q&¥¿APWˆ[ö.(“z¿Õ€	‡
ŸQÑr­()]7Ÿ~óÂ;Í‹	áE]e.“ç2AzÎÌÆ¸ZÑk¨[•vO’¯*—
Û“§nö‰$We™İÓ9Ñ¼­tfÔ0š³ÂÉ¦†êz=ìUæß1çõÁ6ÄÔt.¸+ô§®¡ÑU.JÃ´ô-å…=ìòÙu,zøX^+Ñ=¤*nƒë{»W”Š[ç¬×sê
Euˆ´`ïnuˆÊß
IÓ×e7$½Îõ£íf-/¦½0Öˆsi©QüZÂ¸)ìGW1s{eZ%ÀRf‡´œ2IÀ=¾ÙF[×âÓ<ÜM«6ÜİÜm/E1²§1¥¦@šV…¹ÏËZè–~¸Í-øx>¼Ò'RˆS]#Ö+Nq‰&DJ]êë}ò{o-‹¾½°&üÍ"uˆ²½Š&¿HâÃ"V‡Ğº2Oû-r-<.¿!ñxìò:Å{¼íõEÙ•â£xø¤]ƒÊ#êaüCÙÀd0„vÁª|Á¡•ùväWõ,Ö;ƒiğ‰¡‚£Ú®ú¶>
ö*XlYòX~0DäxEšÜ¬,;æ) ùX5RzIø*:~Ğ¡ş™";'¼î¸Á Ú¹k-!âNõÂJ]0#‘DØ¶è¶Î
wL6Û‚¿À™ä¸õP¿¥ú³ÚÌy–MÌ°×\ğË¶î…È~„*%wåíb„øâªéÁµÕ•öï\™AYà†½f¹Ò:Fr!“ -µÑ]	ïº§Ìhã·2Âgùb$TœÚä¡µÀˆK„]8ÉAôDûYFe…rĞX«Â1yÅ(Õ"Ğø¬¼¾¼¯ÆáÓ¨ p}ØS~İŞ5}<9pCd³À„ÄGoí€²Š`¹±¹gà<5Ï²ØÑ)–nª…–š+ea¤)•·÷á&ìÊ2{¸,Óy^Q:ğñº]Û°±KGÆ ò”y]±¼b	Ìq	“‡1šÈ;fâ€œ:%‰C‡SŞ¿°t”÷tb¹7º8 >ùí qÁ¥.¬ÿ®YÂk(Ë+ŞpX¥>M/K!Ë–Âw°W4îô 9‹Æ÷=lØBÎë‰)"´bãûX¾Ÿ·)QaØ¦¦ÎÊê©Ğüæª«ƒ\ÓÔ-”‡>^ÍEv¸ÎyNGøPËe1l^7/C¼!ƒ¢‡IÕÆàóV.éºA§ÎóŠ£P®%˜€a’wÒ¿5ÅçöÎÁìÔ^v¬oÈÁPã8ÍÂÎRló;¡-¾î²JwLgİ¼…³égÉ|¢›†Ş{²“6ü²)ğù,4æìÏ^{ÕúØš¶›œ§œËaØÁ¿¥C'Ò!V¯bÇ¦+İó6x>‰˜È¬.ı™r=sôÏx&ò0feæßb„îêDqcVdÊCa(™>?KÓ«&J±,¥ù·8,V"|WCÕKWvjÜÃÖ¦„Ó r·«‹…ĞßiZÇÁU¡nHYî/äq”óÉØ!år'5ìD{vŞÁ3—õL
Åó–K€Y~U<‡5ıt9~^õ™÷ÄlªI‘²A(gQ¼ œr¿«±8~º«‰µ¬oåË»–ZÎgG«60UBvâƒF¦/9ùÏ—÷'N¬nÈŸN××nàéñ†5’ƒZÙÎàC!¾Ãêx­gÃŞœfâ‘hR·º·r.lQ×Š[¶£Põ0ã>g²qÿl´~kıu,«:*Ğ9‡ˆ×¬Wg]›3Î+Êk_øŠtH‚¹ì6›¼ëSuzá›mÀ¹—ÅIÕ"¸bQâ¶pÕ.“+ÇÍ"Áø¡Â×i/Å®5ŞRÒ*Iw©ç#ß…ôjübÀó©4_8eYÂ¸jÌR oÄa^á3kî¼ÒUdÜDÌóuzê”œT<9]ÍÏv½RÅ—Ó*ÓÇ1‹­%]x=%pÊİ¾í|õà´‹~rÃù y~ÛÒ¼Ğ™IÏD
o_kÜ–ãxÊ‡ŒüH8=½‹Œ×·í™¦[Î5ŞdÚñOÏ5Q!Èesª‰‚||±Ê(r¦	À@VÒÓ0‚Ç„T¸î8€ÂøRHr˜	ÂÈ)&j{€‰Ú]’ äÄÚ'9„ŒNN)h’ÃF*5¶RMO*©ìyéøøhwR	ÀÀ-÷'• Êö¤€z ¨;©`ØT’aıI%HO*i­ÇÛ(M6Ÿ&Ä†yv£pGS®O*Ñ"?6BO*QQ¸esN	À _‡’jGX ‹Igp´Ã.BÄ÷%¬r¬§b`¡xÄP;<#äCnÈœ†Sãä0œzjGmÜ÷hc´c@(2íÀ†v;X¤‘×N Él §’T~ÑSI ñ¨+z*‰­]œOG‚t ¤
í»SI 
¢×F‘SI †­;•d…õ§’=•„´-ü'CTAuÈT‘´©ò®õæ7;•$¸P>Æ±×'¾Ó{>­‡¤ÿó«Ìğ‡¯€‘ÚÕ7Ç´îßùq­Ì×·õM|à­;üü@hŸ¸)ˆ_Á©x<rpÙ}ñ3‹l‚{–Vc‡ö¹wù"—ä^™ã2QqÙ½Xlçüc7»*•şM5êÄìäöÖm'a¸e6W³é–K»ò·³c&ZÇ¾a|¥ñôÎ§6ì²tÊ“®lÂóäw s;Nowã7úœ­œ¾b¸§Ÿua‘nXù9½ığ†-§7E×’Í;S™\ÉÕ·Qp.üt‰i^y‹P¬ŒN—Î‡ùó¹ÇiŒq„mqÚ¹º*ú0î¼%½÷İ¢}Ÿ-L3k6>Ü´6¾~LUÇï=\ş‡oØæ:j}`6½q÷4ÎÊcÌ#q„ƒÙ"}>s:©oxÄå†G:Îo?ÍÃ[Qœ‡/Ÿ²~0õ©sÏGŞa³Zm	zÆ†ßÿw8w›1A
šÀ7¹cÁï*`â
endstream
endobj
69 0 obj
<</Filter /FlateDecode
/Length 3668>> stream
xœí\Û·}Ÿ¯èç nó~‚ Ş›ŸÈ(±ƒ`eÀÎÿ©â­Š=Ím¶4»’á•¼òÌ™&yX7Éš]•éÏ"àïw+{Œ\£Œ1,?]~»àçÊ±h+âòû¿/ÿüËò+àf•õ¹‡ş4”şıÇK~ñû/—ïÔË/ÿKıù¨)•Âî~NˆÀGóxôîÃåû'³ÄåÃÏĞQb(íW¤²‹ÒË‡O—¿
¡íß–ÿ½8øüÃ¿ TØføøh‘€0îCÊèØÜ$6ÀäN?ì·Ò®JÏ˜K¿Dm‘[æ×Olg/õ<1"ª‚\¸p¼j}ÿrkP*µzKwË_¼LFÅÉ\	ì®¶ş;üıí"¥[ş1‹DI+«@òú «Õ+Z‘_±fß…œZí±õ*°÷e1ß5zèˆÿí®AèC	è]EãÜò©¼	Áëåßt¿…”|Ài£eÁ´I˜‹Bµç„ËGl¤—.÷'W¯>#øKŒÓ‹’àæJéŠ)•ã‡®´ÅFôÚƒ‚
$`0˜Ñ*Ä‚¹°1ÒŠÖ×'-ƒôƒñ¡bhöõåÇ‹‹¾½{Æw«ÖÒĞÃˆ8‹£.‹Ö9ßîbX•SH¸ÑDÌjøÃ¦ƒ˜wŞ»nŞ.Æ¼]&!ÄdPÉ!-¢‹Ä5ÚYÅt“°¬CÄª–s«j Ïö<" †…u› ra­-]e¦ zÃÂ&”0ŠfSO˜‡‘³àŠŠvÇ„	X€Î¹Ô¤…Ïú«úI¨ÑfaZÌXê°¶C¾J·7Ïf!íqfI­[fsŒ ³ÎÊ”l¸Í‡;›9yEs&JæfLæÌ!›v˜ãV%2/ÿxùˆ°äÿ0.Ô×)¤€® ¦¼‡…÷°ğşdaá§yCÉ=Rf¨[œˆ’è.N "·q"a›8‘0ad'  FÃâD‚~ÈD‡˜Ò]˜ˆVFhãx˜HØ&L$ì*L$t&2–ÂDyYÂDy×…‰‚q3¬]rƒ¥Á¹eWšÜêt¸¯´is§ªòa¾W¥È”äÍİ¹j†{}Õ`¨ã%²úy”HH%2äJ·™@Æ¢Õ<J hVe‹³iæÛF‰ŒöQ1ÛG‰m£DFû(Q°%ò»%ê%èq2$ê–L ãlL›	Ó|ÈÔùÌ›OˆÈuH”äd\æä¤rÛ¦Dæã'’‡÷ ğŞƒÂŸ%(ü´sbVR„t’bĞXw2#0×Õæ³“O¸ü”^[:ÇzÊG4ğŒQ>jPNÂ$HÕjÈ†fšäÓ´ ³áù€Ïk|ôÖn‰4_ÇÈ{R¥'!:C¸ËGE«22¨p<„1…,˜CtÍâ¡Œm<îpzc¶ƒyÇ÷4œ_,-£ÔP{ã±Ç
?-ªóz²a_†õ„v5ĞS˜P†Î‘à¨D¥ìV†~0¶‹æld,D]õa@"’Î¢­-7=×× 	ÔÂTZQ(¤nƒŞ—ºõ»Â2B„pÜ¢#°ã®¸˜è÷¥ôÀ™ùà‘D±Ó• 8iöUÊ:{C“æl1â¾;Ÿõb À)á–[ˆ³ZÏã@êob"ÙÑÓı±§mD2b5µÒun3·Ò…c›îù	>!Fæã1Ÿëü¼v1fª«áàŸnhWC‘ğ°å—(jØÕXº£ Ó-v\$ã™ı¼¿Ÿä‡V”üğtª2ÃØkF}?_˜jO°Æ;³+À~aîâa7ÁóIÚíd8ÈêÆóÊ	æÒøÓ™U¹_«/„—nâC¡Ÿİˆ§“d¿0sƒ9%óñj=Hr‡œfŒó"Ç‹ÃTL˜KN'Òo’##ºXÏgd¿CEİ.M‹äl6t›qª7ÔìpâsûbÏÓÃ¡QiÎÖß@ˆã±Ç+ÄCÍ-&ëp–_/2¨UE‰çÑJ†ûÄ0íòÃÏ3€Áì`nrA’İ€˜Zu€™U*ø˜\hOõd°«6ÊÉÂÆ
‚‚a•(;„4ü_†€úÇa‚'ĞÑ¬µX1<`Œ`AÒÓs€à•¢°Ô=@qURÄ‡ÒB¬FKÎ°tğëÙÌ8–%Ú¬Jê¹Ãğ°Ğãñb0¹&İÀô*]Tyr…6 fÕÙ´É%,ß4! f“8«¤€Ú©Â¤V$sê´Ãy‰1é›fvm+xŠV¤¦[u¶"ÂtÅŠpqYí*‚Ä³i`”30Û(©ğ¨<h˜ùvM'´@D:‹GùR¬°íø ¨/At5¢ ˜],6”!4!¬Â´fÊ›Õ‚xßÊ;°4!NByôI©8]ˆÊ8/Ë§U0ß¦ŸÚ¬ŠéùBmÃÛéÚ–1 CUÍØ€>˜}1¡ÊPĞÀë—69Àri‰ AxÔ®›è4Rã*v6DÓOG¦i’Ñæ–Q§we-Õ¦‹W,IÌÿàA>^ÈõÈæ²Ùh,Á¥´l´<®ä[¦]÷h×m½™§ÀÃzØÔPFT®VÌ>b]'¦ÊØË*ÙkÃ^öÚCq0t´BÏxWÇ†›¤gìˆPı"zÆ£fp’ë©£×†›¤4§Ç)ıEôÚpSô"l	gè¹±¢ÏĞcÃMÒSòMéµá&éqîyët4¦s˜şb"˜c•CêÖ•øc2nòsøÙÑ}êß'Ñ±T±UQVWÍnzĞ*ñğ¡ğrÄ8ÈÁÂ2!péãÒ˜”oW¤êõ~pÖßR?_ö3%×èo"×CG¬@Ú9§zXò«ãÈl|æ1;^2Vü±¸‘&G1÷Å‰Bş,µsßs¨=ÇwÌiĞ‰îÈòXTx´˜…Ÿ‹CsSœ)°çê3, ¤>h^ü}÷@¦w0é/L²“šĞuy®’®!LÔæëlëzDNšX¿“<,­Ã¯÷³JëÊsÇ¬€[Æ‹0ß EØSì ô¬E˜SáÏ¥22ª¯l-?¹cn`–1cLn\ÃHÒzz&–çkß;VRÛ’•œ°ˆx.kS²¦Q½2v;iMg)GiÏÚh¸IzZ|#†Ò’Õ;Jb«Á\
[ÔÒ{÷F¡ãHÌP¸d§4aâlèpgBõ;ÉÃ½g–g¦än“YŞÚ;¸kãVS,)œKTµ8JTÑ¢S¢ŠÖşƒø¬du˜¨Ö¸bÙ¢S"_®b‹%oš–œX„H²“šPÓ‰ê©´„úäa¾Z¢ÊÓ‘½-Ì‹¨‹÷7”–pÉNiÂé½´„oÊÒ’£4š§%4Ü$½ğÕòW6¶éÈfgs˜¿¾UZrbGÃ%;£	#ä«¤%Ôï$õÕÕE´ÖÍqGÃ%;¥	ßrGCÃ½×ø=«à e–ÕØoÍ®ÀíÅÙn…b4±’V˜Ê<0-Ú"›b5%Jk;˜È‡Ö‡–hªåÔ¾|I—ìµÜ±-·s—-%={O)UÕ™ÄCwÔÕıIAw…:–]^)¡t½Ğe7ç:ªUÀ¿¬RBám0ğü.^‡¸j-tW)¡ğ.KV*˜_y¥Dx¡DxDX½Aë›U&0¬†¡ñeµm^VnrYíD¤‹ªU—k1FŒX1£y¡`Z˜¾PP·ªôİ,ªA,xÃ%
ÖK4LPkV¤ÒFaå,Œ+|iÌYL›áÍ\WLèXJLxÉ„2­Ä„c^by
]´‰_`CEÑ•¼‘
H‹ÀK& À¿ôI7üF”úª¨/›h /œ ÆT‚@cP±'CeD›ÊhzT&aj	/§hEI¬î":èZj^;¡#DY£4§ƒßn‚Oóïä š¯DÈ•µ0±R~ÓêG¢ï'À‹&X«V¬BSU§Aõ/D˜[GØµÅ|¥²‰hí¹íúY­g/ù¡l÷m‰òŠ­í‘ò%jRÇY£cÂ/wÂŠ%Œ˜~UÃ¬¿¹ìåµ—ˆQŠ9#£—n½Ê…'u]j¡oÂÂ‡»½÷ˆ_¶õ¯F«‰¬r#vsêJJ`òšÜ•€€[‹{¸w•Ük×~…¤jkëîÄÅ_Î²±õ¼?8ˆ	
Â‘V[S˜%ñú òA"øÅÌ1Íc‹g’úu²màmij¸êÎæ0I}Ó5œµ¤´öas?†PµÄøm‘Êv©nğ1%Ç,ánÉ6ßP?1œñ1•ÇSå?#w§ÕF>öxu6ÎK¡½^âW.éÿõüT0Lœ“¦ve,ûÀä––šX»I¿­ ^&Š9ÑÙvÂ0YÙ÷¾—²Ù¬ø3´"Ş4,ç‹hj~j}“ a¨üÖM6Ìqœ€ƒç)á\³,tnÓïBÜ(ÉxæË÷EA|6)±('Ù¨Ú¤7›SZ[™ßŸJ‡êËm@ãö§\€n².Èl•6Y­kq¤ÙL2œ»Úó"ì,ÚëıÈ²ºzê±Å¯Z™ğù”¡­[¸–D³1^®“‘‚¾
2á’|è)1Ç¨Şlv"å¶™á6ËE(®¹sÊ˜\¥œ÷Ô¥Ùìœ1÷Ë[Â‡gN7Ğ2»häœ¸³À¿Í•¿&RJşˆ°Š,cr·ZOÒ—w¶CMÊ2œ»H
B¿¶±³!xî¹ÉsRŞczãæNP×–íº•ú{aİÚ:ƒa…×ÛK[Ûæt–¸Ôêæ4w6Íò³Ø÷Û·Ííèh‡wşíãv¦´©jîÖÒj»ÛıN¼ydñ¤n<û¬¨M<–%ú&»ZcË2H¤û‚ÿôëç%
endstream
endobj
71 0 obj
<</Filter /FlateDecode
/Length 3686>> stream
xœí\Y·~Ÿ_ÑÏÔæ} A íåçÄä(±ƒ`eÀÎÿRÅ«ŠİÓ;' ]y¥éš&ëúªHI¯JÇô³øóieÁÈ5ÊÃòåëé·~¯L‹¶".¿ÿóô÷?-¿İ¬ÒÁ«>÷Ğ?AC¹àŸ¿ı¸ä¿ÿrúáG½üòŸÔŸz‘R)ìîçDøjş ¯>¼~x1K\^†’„rÑ~õA*»(½¼~=ıYmÿ²¼şûäàû×,@PaK0[‚OßZ$B8îCÊDĞ`s“Ø&wúüz^p+íªdğLré·LÔ†‰ÜJ¾c«½Ô[ÂÁG‚ª — .2º+[ƒS©µĞ[q·ò‹÷»ÓBqav{¨­ÿ
~;IéV‡?f‘hie±
,ï B­^AÈ"bÍ>E-|HÔ‹øU€øeğ=4âC»=úPbµ ™ĞzùšT´oø`0 C¢HjÁœ6Zš6‰æ¢Pí=aäò[é¥Ëı‰ÕkƒoÆSH¿”èJéJ<B[	ß¹ÜTFhãğ=¯=ˆYhABw
xib¡¹°±©¢õõMßt|¨4Ä}ıøåä¢oOoø´j-½Œg…¬K¤Eëœï˜»VåT4LL¤Y?L¤yç½ãj»Wˆvi˜}&ƒ
ÌŠHÒ"ºØÙ©F;«˜g<h˜‘V}œ[U÷¿èıD+,Ôm&¹Òm Ó¢­Ò'I‘hVeÃB
ešU‘iidÊvË6ÊTDÙi:gFÏ$ì¾âL5ÉHÕ‰…–:¬íĞéJ·‡·„^' Q·9. ³IÚ LúÔ¹æ-&ÈD:dJ
2ns
Gò…ms"‹ñ/§azKş³Bıœ
ø
2ÊGRøH
Iá»J
?]1g(óÜƒİk–€î Ç<K Å¢—N, iÛË$ì‰'	¤‚I´[¸A€Ô'‰Lƒ%¨7Y"Óú,‘i>ñ,‘©}–(´Eµ¯K–¨O<KTZÃÒeØÆ¼Cv³‹€¢N+Mï.ªŠ…xğ%;š>J“Åû4Q\cÂÒ…}qaKÑQšHşïÒRV0.Ï‰æŒå$d¿.O q—'m“'m—'u“'€¶Í‰´Ë‰ºÉ™VóDzªy¢<ty¢½Î Ôºe c0xVI	ÄM†v¦9…E3‹fJgÌæ, ›wXà6/²0¿föğ‘>òÂG^ø~òÂO£eå×¸tUQ‚¬^ùÊ?ĞSohbô‚Ä(dHDÀ©×QÑ¬RÁ4Bá¿@Yå$’ıj¥ñø®CXà D¬­À‚€Sø—‚¸ƒ#JODôitĞ“w¼9BQXÎˆqURÄ^(a^—@LSvÏUíˆÙ(©y!úd$şìV˜ŸáÂ§±ğX=Á“Æ{>sJm‚û XĞÙ6@+7›
-[íUHè­j×B"ëSßä(.ù”ä%ç“^=jsˆ%%°Ò‹«HûÊ?yĞ$c©#g§qÁ)Àş„ ƒ×¸PnàkÄ’€¼,ŒHC€€ƒ*è)@ Ì¬
éUğ°I‹*©”˜‘äbER¦!<¤‚ L×XyˆV°EÇFŒJ@â)0–²RuÒ+°«ÄÁõ,DOIÍÍöv¢–ŞªÕ†Ş"BæP¤ñ]Å*LÜÛ°³ÜECo!·û)Õ™–$i«4¦™–µ­.`,š³:aš_™Ø%M½9OWTdW¬ç¿0‰ât¨§ĞZ)”¥[ (yIÙà*<XÓJÔ¼ƒŒ8^,0…Ì`K«{û¾ İ]*ò3&
aüÚÆf@‹ÁíÄ7Ğ·ÄøğûÏĞÄ|¶È7ó7OU•0QBKİ«šD™ ¦’j¯gÈzZüW”gø`ü[tÅ(èkÔŞ©]Ìíôs6:Ój‹@ˆ”Öâ[â±ÈF´&8í—Ü`#q„Š:ô]?Mö}Òû)ëôF,¼}³ŸÏßwvÂ>àñˆıv{2ç`)M…ï7[9G‘çuy“#ĞÃ\ êìƒÆ)$NğŒÊ:
œUm¹sÇ1›| q²=·_1çÆÃØd06#”­Êqnóœµs@¤qÏ@ğ…c†ÕYDî‘ia©uãáoÀbBæ†ö.vL…qtÅÍ¢ ô‰ÂÔ”°ÄïĞİí½ú+¡l(=÷–ÍHÍğšö0İôÆ˜#ÆRÿİ>´(}LÂ—o2ú¸±Iñ)ÑÇFôQêmèûmÁ³Ò<™lˆè5˜<ô¶¸Cø…¼QÎ²¼‹É}I)ÓŒ,û¯õ9C.¼‡4KèRPI/ÉÅ¨w²…ëßI£šèê­şW°Öh
7°‚“@ã…IóŠl¤à+J®ÍJNÀ›·—‹Ã¬÷cCik6âqtªÛxÜê2Ÿ~¤yâµóiñx7LìW!±öÚ‹pßƒ<|Iˆõê^$²ø:p•ƒ\ §v!ÅÎ|å9$,”•ñÑZöjmBŒVÓ¥ãŞL6•]ÁÑïN–É +jëöÖ Mb•2ÀR˜”%šÖjLÒ7Bq°PwÂ_æ~¨É1“’æ°€à`]éy)\¼.°¦èìPËHÌVÄ üe.‡Jºbí°¨AòÚì­ \¹Mªæ‡l8´ÉçúÔ>Âw#väìC`¸{:úâ_E0(EÃtéÑ¥È[ÀúŒl5@Kõ±1 Vë`t½ÅùÈ", …†Åómf™‰ãŞ•\â–ÒÿÈnƒ:Õ¦ùw·á½X¥Áå Õ¦aL_ÍX;:s>k}·Û Êƒª’%Å£Ë"Qå¼RøFC¥ñ}†J£Z=õOU}.	ÕÿIfÚ' İ8m¿¿PmõÖÓÀ· ÁbÒ.Ğpg0ªn¨`€Ò4í€æqk)°m†Dë·
‰o3PK²<q qYÈ›$5y´Û#f¿Û€µ—Œ%¢Å3÷bƒÃuA«KÇåáÛ`"É­ïv ÀW#-î¶µŠ8Ì­p·¹UÍó3ßeÈ¾ÇPÚ´*=ë·Õó;ZåŸ‰Úv˜Jm!ÙY¨&â»@kĞÁ±İh€å‡"Ğt|·» T ‰ˆŠí. #æ5Z¿½Ğˆ|µ®FgLšw:qš™àUÁVş_{ÀT–°T±Iÿú¼¬ë—E¼}´ÄƒXËE$ŞıØ|_²aÿ;±\ÇiÊRœŠ®/S—’¸xNµûNü6ªæ;+÷”¡·â»â§vkş\	¹W'×]ËA´Ö#¦£µq’~6ZI‰û¡•ÄŸQ‡èÑz7ù	­$şŒš­­ï«ÑÊĞ7„VV{¹3Z©8ôy6Z{%^î‚Vÿa:Zï&?¡•ÄœV*.^‹Ö++jWù»Z‰Ó”mpVêúra\¨µ‚D)9¾k«vùğ"«˜tÛ+—Ø˜kvÑá}W÷8‹¶ïÌ9'ºaˆ'RxTSÜ-½è:M³å‰¢ÃºOë„^ò)s¾hkÆëÅ(ËTÒï…EPß"(šTsL›AÑ:½'(HòëŠNüë@®Ù`×Õå7
’jÎ"%‚:½#(˜äSr¢ÿ*PPÓAP¨}íàÆã-¹_İVyõ`‹$pÕ3z¸³¬´s‘åù¥<«V×¿Ñ¸©r™d&Ù˜…ì~0ÅBŞo-4«8”ûnÓÿ~‡ù¬.é0+³ÏíìË/#í/Ïúìs¼Š—6#¼>×É?.0ØçÇ«xY=ÂKÌ	s~{Ü‹Úİ€nëqÅ¼MÜ'ŒÛOHh÷{zæª‹=‰Íç‰ª°“4J³7Ëtl¯ÈQ¸x„-çƒûnG €7•îz³˜}~+¾qåXÊËL8dw‘Óp€ëÿ½‘¶¸¾è~>?áİ¹ßZæ‹/ÍRºYç5$›Û6¦d©àî¥‚»;,»,E*MÎR"ó²T¸®ã„=ÓI¶lÇï8§©àHE¨ë½6÷Ãxna:MCÖw&Û‚}çºÂ„2©k4•u–¿˜Êb½ßÓ³Õ¼ëe –f_š± qn79­±]üV#Õ#ºÄÿc	Ëèü±ä‡‡Ò^ÎÌá.´Õr]VÎØ@â9œX0“+”m5xhau`€½ïˆc™†T¨ç¤ŸN«+êµªAÍ(Åì…H±9tnÙâ-ùı(²¿ñ1cªä«„\œË©#œ3åX<‚ZÛÃÏ–PoëéîrkÆz¾ogcŒ¥ÿqe÷üñ­&ˆ19Ò5Ÿiµ0®àAäuÓF¯ûiãVÄbşª¡ÿ~—dÙy¦Î´1¸ƒR§R»‹Yå³hwcÛ1ùNÀ?Š±{ h¥{ =û! Ù£-ó4¶ÔR`ñ</„9]œÙ^K¸TœQÚ·‹3$¾?¿‡:> ó†8F{÷ˆ‹|š8e<å
“ç½,ëE—s°-£N½èí†Á©T¨Å_nºSãÿïç ›£„x&¬¦üI_çB¶”Á,‘´,}½XDíG¤›/â‰R“İEFÀJí”ÃEé{º»ØÙ¸ê¦êB×”;]ì¤“FÆÕ»g;¼<ÏÕ#ÄszÌò‰îœ—CVšráºW(¼´¾w&#ÓoêñC(ÄF>hÏBqÙÌ]RÿRR3nèL9 ×¥$²ñÿ %‘.wII=^î˜’H»¤$æ“kR’İï‡áí¥ÿ>ëJ–
endstream
endobj
73 0 obj
<</Filter /FlateDecode
/Length 4137>> stream
xœí]Y$·~ï_QÏ\Ö} A€cıœx€ü€uì ˜5`çÿ!uRU­i©§z<YÏ¬w§›]É‡X*ª½
éÃÏÂàÏw+yë_=÷Ş-_¾~;áçB9¶HÍüòû¿NÿüËò+ĞÕÊ\jãí;Èüó–øâ÷_Nßÿ —_şæ³^.œÓı(//àÒ»§Ó÷ŸÕâ—§Ÿa¢ !_¤]­ãB/B.O_OeLê¿-Oÿ9øüé§Âm	jK°`A²@pı98Y:ñ… â¤Oç×\¯‚;K$çvËDl˜ğ­äû+¶Ús¹%t®è	*_ œd4ÛÑêåÑ`Ô:šÉ­¸[ùÙËÂH&¨0;Àîòè¿ÃŸßNœ›ÕàZ8"-4x¬ äÌQ½V®èAÈ"¾"Ã¾óTXağE÷àğÎóä¿«·0ıÆí‰0‡`«^$gJ._ÓÆ¼YñÂøsR·àF*ÉMj$ÏD¹gú‚ƒ·ÜÄéÔj¥Á+½‡xI$
a.„Ì4xƒƒ9|hÒX	ƒ^h¥%šã
 EfÂùD3ğ
‹U*¯m¾äÅ+Aze]¦¡Ûç—_NÆÛòîß­RrU/FŠÑLz2%Ò¼6Æ6Ìw« ›)"&Ò´„¢Ò¬±Ö4zïWˆv®BHãN¸‚£
$	6òq+i´È¦L¨ˆ	‘–Geû?ŸÈõHYÜ…ÌhFi*A y%ˆ¢tÒqpÒ(Ğ´ğT÷@³Æ$äJŠ~GĞš†É)ì$™Ì
TP*fŒ´0a‡f²¼y>)—W*Ó§#÷Ì’V'.úo'š×°(‘è)P’8#˜“€,Ö![¬HÂüËéß˜!ÜÿÃÄ_‡œÆ‚¤ò‘>òÂG^ø³å…'*‡T}¤°~Î‰‚ÆÚDÁ¡xÇ¢†&Š@“J5 IÛf
 ‚kH’(EŞ@‡4!|“(€B-´M¢4ã\›(u“("-$Šô2%Šô®I‰Fı0OI=¶2§®Å¤!Õ¡ÁRõ¦a•"Ñ—`¤QZñ¦ñœ-Cã>[0g´qÍhş6O PhÒ’Œ2 HóZ¶iÂbê3M–@Ò6K mŸ%ºÍÖï²’öY©Û,h%Kà»’%â›6KäË©åi©ÇU¨o&I‰g}¨«WÍILdˆhä$$iˆUÄi0fÛĞ M&$>U;|¤„”ğ‘ş)áÇÑå×Øsƒ¤6}ğ•Ğ¾B…çBT`Y¨vèw‘hV¯œ¢Z¹€Ÿ@t+7Ëfî°ÚàğHÿrPÚrg 
"1èÅøŠJü5pzníéÍª¹5t 1ø˜¦,€èWÁ™oÅP[ƒÅy#:9ê–*ÙãşÏ©3nÏœS3'—ÊÆr·:!='Y°T’G“ğÉ(®LZ"ÍY…y²`i:`›Ë44X†¶­6¨<ª¹¨4Õ²UîêU¿½ÿ ¢g	†[¾1!±äY•PÂ¼AĞ†bIéĞËáÉqÌ#àfN!˜ìÄ…%@ï%Ì„b#Õ®î¡ !ì´pñR°:˜ˆ²:V S
ã‹s%*:˜…ôà˜j&"piX	kV%¢ƒ©„…ô¦¹h4Ö£²ºÑ5mE%OÄßó©6ø CÉl¦0!•!a–Z±$P>¤m§L¸2i‰4V†Š‡+HEÍÆª¡@KÆd©‹±!Š]‰¸ÄSŠZ;ïÉ~5¾E»âqü+–G-¥Ş6…fùH5[Ì
oÉ“eËšnJÃzK.!¬N.2ØÒò³ŠıÜ†Èc•²Ğš1åà7`­]|¯ya9 Q‡çğL"^[•
Ï‡ÈS}ü•ÂßÍü™yCšÙÍzaT Ö»¹ëÏ(Ù(±z„×&¾GM ä	¿Õ=¢eB?/ÏÖãÀ§}|ªÔ¼AÃWÃ¼«²0@OºÈ/ hÿ$c@øŒ¼ü!9”>ÀºÂEAîp­h÷`wÈÆ#£ÆŒ¡X6*(ÁePÉjŒ¢œ7îL4–{µ0kØÉØ¸rçGÀµ3dÆdÙ2õ ÚÏ]5(No=ÂKqC’™RáÔø(pSÉ?Ç÷ÁGMõÓC}S`Åš}³Š„Ó?öÃã¢ïbiTÜL;d¸Qx#NÁgBåP¬¹…ãİkÃšbğE¥Ù]'zïGğwvİé8‚>g@ô	§€~ÊÌÊ§uÕöião”©ñ¶b'±ÊaúH Aº!¡«’íÎÅÍç¤Èµv…	WÉĞmD¼éÓtZ†añŞBÆP—‹„«êV/y}ä¯}ü„a½ê¯MJåO€»vs¤Çsqo™ë1X;e¯5¯cÂ'pÀán®v2¨Ø2ÂqÁAí\EN¸‚.šy'ˆÄŸ2.­×ª~¢u’˜ƒÂVŒpÑ±Sîˆöøx©yì)©îÏ«Ò˜Ç¦³Â‰·`à‹#ºĞµ2ïÊ÷Y\%áşÙ±Dš‹érÈ÷a¼Ëì…ƒ»«ë˜0(îµ4#“Él`iœïÁ¢õ€¯¤”	…8“Ş‘}±ç¶Ä…wR)-æºË**7p®¢²É5z—1°¡öÊı˜X;plÜ¥ÙHkq7n™H¼ea!«z»÷ıˆÜu´
)½—zëïáV×{Q™§f®sÑŞcÒ¢³7
íı>Föb¥È…¨R‚}Ÿgäµ)p°`Y2•Ë‘ ^=€næ­q‰§öèñNùïŒPŞ}shYİ›Ê¥©XÃRĞ²â@w~ÀL»&ŞÂL{mÍe}»êdWANóë<"i÷„>¶ŸòLÜı"uFZ
ºsî¼§kš[‰TNªóN¥ün1@q¡ò¡<æGğÎˆ«Fª®]Í»é¢/–ìøtƒ»§PÅ½î³&Ü­Áû‰úŠ÷³^öÏI?¨ì½±G?<zˆtåíúUõ´S«è8µvdÑÌ
:âò5Æ–šûXåĞ1Íƒf}òìÌTp;U	™ÊçVÂÇ¡HÃ ¯z7§QìËKWO4ìªŞóùôÓµmo5¿”É.|ªlãe1ºzt×Ùùuh¾x;°¨<°îy‹bóLº.İ-\{)±[uª•éš²ïnôQùİ†B?ãÕkÜª[–¥^ß½rÏOFY?éŒÅL³úŞèæÂ±‘•ñ11÷î~m§§ËC¿
€fìæÛ®æóğtauyYŞYğ¸òâµGWóãËÜ;¶Î‰e5êÇUåçÆ;bÙAŞ-¢Ê©ôĞ.¥iK_ßã–WÚF¾KÛÆ.m—g¹u;VÚ¸=«~~íŞÓÎ/œwi„uà¿¦SÑŒ<Ÿxû#zùr¨¢K×­î›íĞQ	*txÕ©éTœæ¤±Ò³ùÁÀ§ñqKx*¡Yyz<Fº"[Ã~x>şâ¤ß‘Ç7¹]³òpÇ¨O¬¶7˜8'òä¹9 ìP^Ó2'ÿŠOiÏÇÆÑ¶ÌqlgÑB1MZæ€(!0ëHùê$(Ó´ÌaH¯†ƒÜ¤e.txÖÖ¯ÔğYûÃr—oi"„ÚgF&­-i µ{[ÛÜˆZ1èO{ä
PÏÑğìàH“ĞÄª­´D" IPH‰¦I¨ze<t;eıÍÄF­B¢µ]r…HÛäêèŠ{åRMDå©Ö¬’W³WÏøÌ¾ON2©’;U"’Gw¢4áÀM9—¤Oˆ¢’ƒ\µõ
ˆ
tbNÓ>9Ô4`xâ¤4sq‘Zk¿W!Ñ&¹B¤=rupi2£LJ?Z+Oi]£²—7ªei†ËpĞ¹‚í"€`¤!r@ƒO­”D"ğtğGì-¦r@J“9‰§tllÎ`Dšnºä2vÊ‘±Ù„E1W#L±,›úJVoï?W´Êö²]n—©]MR–•ëŸ›â¹û‡°àÍ†Ã~˜µ¹±‡ŒkSºíûÃİ|VÔC§åÌÆgó7iAÃ$›ˆpıg[Áí=“PÆ(<Ñˆ5Òk 5”²*™GOurˆËyÎw“œ1Û%±¸–ÄÙì¾Kñ•­ŸQ~Ÿê—kõWX†tÂTnC†3Q:SÉ¸1«HÎ†¬òÊ@ Í€”'é±Ú•~´Ë'ÅK(EÍQ=Ò¦oñhDºØG…A,öÛPô†ĞûŞÃUk.¨ñ®"à|sC»à›x*9ÍkÈ_y J$!.cÚš¹>3ì­¿Eäb½{ã®²˜Yáê¨1€”PÛ`õ5XK“¨mƒ¥m¶.Š¿º¿·¶.Á@'ò¥4¯éŒ,}êµñ.è@5î
íÕ8B…ĞH›ò9ÕaÈÔê3D¸÷TÌ±f‹
÷yÌÛ3”Ï¡)Ñ½e1S¹!R2å©ŒŠ°	5Ÿ~gI‘¯Õ•v1Ë
0nÑÍÕDÀçÍk"ÂSWHš¾ÿÙ2Ëâ¡ÁX&Ùò‰ ÔL|L­”›Ç© Cÿ)µRLtd]ºßÂ‘+·àÈi33 í"×³ê‘
ŞëR‰RCÎ*İÛ;«lª¼‡ˆ4SÀSô†ĞÖû’öˆ[o_À.cÚú¹ú›€näF–ã–·*à+‹™¾HïÊ†÷QÀWÁnQÀ·jß°€'j]ÀS†LmùÆÔï¨€'Â½§ˆ5[ÀS¸‡ÌãÇj¼×ğ”Ï‘)Ñ²·¬{*·£
øÃĞ …>ksD
€$é„ãr‡‚"Z]\3ÂÁí3ÓŒ¸*öº*é²›ªÒ–B9ê¤Ê¾¥“*z~ö&Å9e1d:c†LwdqNx¾—âœˆ4SœSô&Û>>Íêd9ÍšN`bw·¬7²zµRxËwÇáÎLíó¼â êìĞÔû†oOêò	*¤GV§ÌöO¬öOòCt&gQù{³ÌCœ=6udkv¯ñ½×„ùŠ.è-‹n§n·%­Ûr÷ØAêŠÁ××'3¸FsÈä	pŸ›ñ4@B<½Unô~ÓŒßëÎî¸çµ‡Ï@;T×àóíğ—#fÓĞ|\ëğaz=ŞW4OŸ?šo0ÿVÎN!Gä
_èîšï÷¿¢­ÿb×;T„^é¸¹|,rwzmúÔàü©&»YzôòÀÓ]çÏw§š>äxEĞvcs«ÆPÍTCÅ–¿ş`­é)Ñ?ÖvñhÀ‹GQ›ã½SmÓKf·Êœ?K8]mW–ş‘%D©ü?j
éÓÍ”sšc9ç¼³›Ó¿-CßUğ‚49ıuNB×Øş	¹^½Õ¯Ğæ×¿JsÄNxàÌ—z~ôŠJáÿª^û®™1&ó_"Ğw¾È=ğKZ¾ñ[¤¾~ó_ÅÒ@Zöš»­+RRù

ÜÚıTCQÃ
endstream
endobj
75 0 obj
<</Filter /FlateDecode
/Length 5715>> stream
xœí=Ù$¹ïõù¼€Ãº`aÀÓÓöó®Ø˜]ÏÂè1àÙÿ–ŒĞAE$+¤HuVõLuOõT2C/Q”(2¥ãúç&àïò1¹Dc¸ıôËË¿^ğ{e‚¸i+âí×ÿyù¯»ıàf‘õ[í'h(oø÷?ÿzÛ~ùõç—?şUß~ş¿µ?õMJ¥°»¿¯n¿À£?|yùã_Ì-Ş¾ü:Z1”7í¤²7¥o_~yùw!´ıÓíË?^|ÿå¿o Pa0{€_¾ ´XïCÊ ÀnMb˜­ÓÏ_î#n¥]”`.ı~µDî1?>±§^ê=€y‚CTyÀà„£»ßÛ„Z[½Gw¿x-EæÀ°rëÿ€¿ÿz‘Ò-ÿ˜›DN+«€óú¨Z«Ô bû4ûCŒ á‹†Ö§ú«@ãC”I—è¡+ú/´;¡%hiån¿äÒ‹ÛWü`p„¸H…>à´Ñ2Á´E‹B•Ç„Ñ·Ÿ°q^ºµ;¯>#L˜2ğ¥’0Ï•Ò°±„/]jë¡‘Ã½ö ¡Ò Gq0b‚¹°±Z´‰Öç'_|°7>dê}şõ§}ùô?-ZKSFˆ³BGÒ%Â¢uÎ—ÁãÚĞàT4MwC˜Õğ‡ƒ0ï¼wİ.û„’†pa2¨PøhVÑÅÂq™í¬Ê¢VˆĞ",yk•åÿõ…>`Ãv‹ —ºÍ ,Z›ºJ˜jå‘7JÂ,š’0ïBb\fˆôF	Ÿ¡ã†ãÒÂo²+²A¨YT%¸ÂâÚ:}B\•.¾¾PíÈS-ÊİR}«PÍL˜ıEZ¨’WŠÉlÈ¬¡“&³N¯Êk:³Tè|MÂ#“û§—ÿE»nÛhòï«%)ù°ÖàÃü>¬Áß¼„äi¤œ2Õ<XávæÁ
‹Lc¦7´
Û´•’j…YõšpA'.aÂ”nÍ~Au¥B@ØŞ< l›¡T°İ›‡¶™‡í×l¶O­yØ`Ts—TYëàT«3šTó39t²édÊü!s.s‘NÎÊo:³dèlÏÌö e\­Š¿µ Ù[9ã­n­xÃÀ…Æ8 hov44Z5aĞwÃt„-B÷b…ŸŠ…Ø>´"?N)wKU®"@•3£Jt8SDu½ÒN&Ef;/[3±1}o&6ñ´f"I‘Lò!§áÃ*|X…«ğ;±
×‡hb5Ş›™ğ^öÛ›	„¡¼Z3á½>R+ãdÃ9„í­„÷Ú¨ÆJ ,HİˆaÇ­B÷Vb…mVbû5[‰íSk%6UÃÜ%UØuğ(wV"£I§@&‡N–B6U™?dî%&Ò9Z¹Mgs–ôY~Ù, „«‘@á·F Ëæâ×~æŒm0@ØÁJD+eCc&f•o(G˜wng&š·_™—ÑÊEz×paZØ™@èŞL¬°µÇÜ®˜‰íCk&òãT“r·Tç*T;3ªD‰3ETÙ+ídVd&Ñ¹“™IgYå:Y>tŞf9’Y>ä=|˜…³ğa~/fáowBlÉMXC/öBkB9â¦e”9øb>oÁ—%
"‘°-¦’³@±ÙÄ nlô²FÛÄ_¶ ĞbŒÁîcA8¦cÔõ«™¸¡mŠZA.QëÙ'ùèmÂl‘6¾atAÖ/~LHY#a«ÚUHcm£ë Â„4D l=ıâ33ö8Ö¦/LO…Áâ˜”ÜjpOÉèò>ÓyÂG5‡§â'–SlOãÊ9LÄŸ3JØaü¹aLìĞRGÜ]NG4xå‹˜Æ QĞİ}¤‚6÷‘2ÑŸcÅN%^•éFˆhñŠSš@ÉJeXë¨î“D!ã¤§90ÎXg c³ÎêsB)€(Á•7lœyf[\°ÏÜ`×nnğ³‰4¬Àùi3qa+É›0f¡á/¬¦_Y6¦Î~¡«q×…ltm„ÜÊKJPJ×c.Xy°ªK=×c’x	ò6”E‡É?÷Üp!jV(v!'„]»x
»<Íf‘è2£ÍÂÉr‘kÑ8ˆÍ,Ô‹qdq¾ Û¬6·Î{Æ#êã»<Rº<ÔXŠ5£Ô_á[P)ºVÍ¼m(çZ\pKÆIŸÈÅSŠå";A¨!ÔPCªd‡#\"ÅØá@^°q¢ÇSóùÖçÄMçğJvÎÇ˜évMô+GxtÇ8æòôn)ù±ë ìX/x›ÃáÇ=!áİ7†nv°şÓy†õƒ?(cm*»÷·ôg_€ƒ‘©œ- ‚(fwñÍÖ¸®­fßbÍ±wN}$¼r’Xèqovxı™¨%¬£É:O3=iÖ	æî8ºçGi{gd¦ŠvHÄÇ¶#oêÆÔU@OHtø÷¬ã6QáÎç¹t½s|Ú¯»ã[…ÇüÌ˜ã5üBşØf=5v±ç ~¢{È{ıoè&}8ëß“³î–(-,$7PÏ2%t>w×›,ââğ4~t¸+$f•ÛŒ'Uƒo~ÂÌ÷Ä¤Æƒ=NWMjÏ|à¬ú]†2‡ÉùYÁNV®óÎî/gÎ°XÎ°t­Ò}¡ùa7=g÷Ér¶…o³»ÙOYm-N¯ï“Ñ„~H„Ç[ßˆõ¦¸İ†Üæ¾Yd æ>ä¥g›U~;5|&:¾E¸Ã³‰CbU5êÏ®ÅIßì>:ßµ7²¡LùçOi‚G¼ã}ªì}fıÁÃùñ»Üà¼dçµóêÈw¼é;ñWm‰>_¥võ&Æà'zÃ§²ãîuñ2®¥Ø¾²Öpb÷Ğ†±šw=s"Rü¶šÑÏ™çó£Nÿø¾‰%ûôü¡ûˆjÜ¨^8Rg=ïá#Ãq£úÀÙ®
»•‰^C;CqşÃ) RCêá|bœ—Û‡M¤X^¦ó=b?Æ^°Xuãå7ñvÈ÷u¿‡§câÖiæVh<ÄqáRğøİ¦ñˆÌ¼€Ş÷©‹'ş¤ße…ÜYâÇ/¡N¼–;ìt…ÿè)äû<\vİºü‹‡Lg:ñì%Ñ< ‰'Ûì15«RlĞl^ŒÍİ™wí‡åÔøİåñ#,öHa¢«ÀZá'xOãv»'_DIYâVem—xÀkzö"£&¡ï¼í±‹ıã×³"³˜°QUNÏË®Ğì8<ÆãÃwîXƒÀ=?n¸Uú·±R§¿Nêôs°2šd·ñ[Kç÷j(•ëØ‚¼ãıÕ/şŞ{_kâéÿ[ŞêëHÙmÊ&ZÃ]z6rW,ãwq‡wk¯ª»"Wï#QìpÔp­ß¢Kg|vé\êÇXı#»„y÷¬&FƒŞÒ]?fQt¿ıóEµ¨(»É\Rü
J.XşkŠEš(@Ø „E: P†f©àÂ@ĞÕş'h•ã,¨ ª´–Á-AâZÀ1êÀ:xañœhf¨ ±6JÄ@®'OoƒK`\”±EHi!p›@q˜ÄªwÙ 7v¬­303îk”r‘0±õŒcÁXâ¤8Y©4,•²Ò™ñÇZüB®å+v¥Ó,!W8b›ïlaáqmN¤Q"’£H!Wˆ:TRïhVuAES_¼€e¥a6E#@Xƒ“¢5@³¨à°¦V#2¢°XSğİ±p^T5Í´‹a«\¨K¡Ãb¤]«ëŠ%Â/ø¨^K;K]ÔLo•r1+™ö©üW‹Â”fÊpµDÛ¹òn1jU0Š‡òhÅ¥jpk…äÙ†ºô•kóÌûúBšktzÙe àk¯£H™Z	˜é­×L€‰jSj_É4oâªa…+p+(T¸–`€Re-i\d@F©âj0ª¢%ØSu)tu(«×Àû|_ÃöV-Âòc-dWsHºıšf°ô “—šw4åhµ·¡qåJ°qyCş¯phŸ7ïaXmøÖöáŸ„CëGtM7\3^+vÃ¿7éûµİ¦f™?òÄj¹(‡È(kvoÎàXYŞ6’Ñ7>¡“Y¦eú¿¯pd]fãŠrÄ3zk	}›ş/¶ç¥9ùŞîDAXiÕ†ÃÊ¿µ]Ùú9}VLªünÅù3asbıëtğÍÁ\
Qlì&ìëb7˜¡–İùgÏF)OØß¡Ö¶'Ïõıœà¯­Y‚Á‰Ü’ÑE¶“3È¶dÛœ”S`aÅŞ¡ÖEJcÏÇXBa;Û³—â›5ÍV}j'×:–L¶èa±¬öjÅñ³Ä†}ÎíÏl–]…ÇZˆ”E•¥ßæ}=§õìÀkÍ¸¨¼+òvƒò‘¿Ÿx—;¯ñóÇá4/şÀbü”a<Icbe«ße
ûx*×ÕÔİCRÓ3’YFùt¡Üø©îÄ‹3])§]G±»%ğè3À>Í‰¨CcYË8X‘Ô‘lŒ$³8“ãšxƒ•Rî¤€äÛÎg>Øz½–ìU¶Á‹U¡&o¦	ŠtåÍ4všæÍ4ÊÁûÕãÅANCy½qÛY¡|®*kÙi;6kÉÆ¸O,›_´÷†ï‘LN\ÿf1‡3!/¤ëQwßUèŒŒ‡”Î*Ú‹œUxıà_yvoâÁxWVcO]§w¯.qô®ô´ë÷FË¾M.Ä…Dàñ¦ã^¨ñ.õ™†j^âùÇı¼ûy÷,Éƒ·ÖÙø2yÎ×¿şôègÜá/;5<2Œç«‘²S§ë†MW%¡¾p×… ‘¥‡<Íæa¿8ÙSZúë·Ã[âãä¼(ĞÌxÇÍfÎ™Ï·/i?xV_@²¾¥ÎÚ÷ËÔÏXuøûEÜF°«BãŞ½Lİë®.35ø--¨%´<Á£xñõMÀ?rG-e4mŠ}ƒi¯mu]gyÑğB2 ë'NtsŸQã²œ˜ú ~¹ŞPH‰¶‰ÙWÒe»– oÖò÷“¹0Š¸à³ëÏx^*Ç++vpÊ'*ñ4~kú,›wsƒ)òêßpñ“Íƒô`ÍAÌb,çTåãë•KQs:ú3ó8åzàDÍÅö¾óY¸úÄÙT%·™=fî©ÑWèeÜõÎ
ºT3iñOvì²yFEYŞ•ö».¼&à·‘²8íÅ“SìpÓŞ´àİø	âÄ¬3Ö?e_ÖòŒ÷5](?3îV“î»/ÒW	ïµNÆó8¯F4g8ÍÏ˜|a|c÷&¿°b¼ ?ï±Ë£Ç•ß|®ü”mş°6Ì|ÚIÍ¸¿¸$Î¼Y:|:~³tŞy]Orğ£/¤¼rğp¡¸ú{(ıø}´g_(dÅùëóª[~«˜õPg¦g¾|y¼
ÀÄ›Y÷C>xjÕSJò)+İc©è&äƒ¤r¡ÖJ<ZˆƒZØ#™Vüí-áøÚÇRÑaë74]	LEàš¥­H&º³¹IgĞš÷íš<t€n)â$`û4ô¢ièHÓĞ°¦q×1jÆ7Å¦&‡´ky¥®SĞÃ¾¶@µh+É@ÎfC±1ÆBcšôs€ŞÎD’}¾ÂÂ*¾ÂSÒ•	ÃLÉå&ŒÍ@Âÿ2‘Á†ˆ4£M$_¨»£7Ç¤se’²Ñ¤s%â1é€[Z6É9Ø–¿Mr˜¶¥zÓŒsøeM
×$á`mÂyĞ„ó¢	ç¹YÉ×&}—Ôî‰’NĞ-éâ„¬’W^è§Éæ…S4Ù€xçD;’k® <Ñoğ1
„¶¿É4¨NKÍWXŒ‘æ™¯ÇÚ4É|ĞsÒª°¼v^eCÑ¨R¬S½È„uåí’Ë­gÉå9y;%kæÄÍ»ÉšFóf‘¼“—º2i»ÚTÑèË3µ$e—Û“CjÄ–c÷	1g#û0ö|ô½±—}Êä öl¬UTŞ>óÔYİ;ú¸#>#™sbĞ´ü/ş·õû®Ş“5îßN|yÂÌwM>û"ï³KåM¼Öò­¢‰ôpb8(Óì#î¸Mô­ê¸Ò]ıS²ñšÛ·¬~!?%+ƒ8Ğ¼^v6«…¶9°±×pË§¤*°	l¸ö1ËğX¢Ms¦ymâx$nü½'å\_?rs>ûòï´FÇğ¥$6ö2ïÎÃTÌ|±òøû¦¥˜ûñß[ææø{Ê'ŞS|÷^¶ë
–Œß9]eWƒæ]~Ó,Ğó‹èxI3¨Á8Š—vR $8î\Ùñ>—i¯¡å4êf^eOá²\†ß—1\FŒ§büŒ‡“ŞÄ²RÃ«Ì…[·¯MOã•wÌA`ßû¡ÙÍêx@yâ‹®ç]‹=ó¬ùUk!ObS]êHb™ts˜0´1Qœ§†Y?…éG^Í¦k°ùÊg‰ÉFºÅ-[Zêr+MP·Åábè„->r şús:6gV+KuÄt$•VSåÕ\I•VlÅj²¹škõôKe× JÚµ(¥¯uAm9Ş¿İÖÆ‚øvÁíXjˆ“g~q&DÜÂ¡À™Fa˜ºnG¡¿‹n#L¶Ñíj¢ÛØD·3D‰Ë$L°!ç‚7	PúX®^™c_[Ö¹²4ºU¦ÁDF‚6N€lbİ¨\Bˆ4º0µĞØvĞÈvÑ¸vU¾×¾«„(U–İ*òJÕQ_Amm°èò.¦u©NæÙZƒ»DC£Š‹õ–Q–·Ûn&” kT¾ocÚQ5í¨vñì¨vÑìµA×>kì˜^£ÌÍ®äÔ°u¦›Æ²3ƒh(``éu ¡l€9P«@Ñ¬G¸—¥¡l€‰"ÒP¶Ş®ÊÖõ*Be“&×4
+IëÌq2HMƒN"AœjE&ğ )W"ÚV{}å`¤³ÍŞÃú¢ÚA6ª]Öˆ :3PLÇ¨k.P8¢ó$ÓBƒİ€|Ï`tL‘é:€f—Š	ÄÀÜXR:âiğ^‚í±°ŸÛaÚÊ7ÑûB…µàö-Öÿ‚ÌWØÁxJÀô¡º‘R‡Ø}^«£§BÏ¹Júª!i_?ï¾o
ÜÓÂÔzÃŸõMáªµïÇút`Ëuá‚+ó&é“:†ÿ_•’qŒ”úæi”Êµÿ´ùIĞÿ6ó³"ßU`‰æÉş=øŸRAç8øøÊLÅ9õsÜ[	ŠÎ‹¤«	¶ZA!JsôeËw*écş.ëmîÏŠú&—|aG¯¡<¢«ÆãVj-Ÿ[É;µD«ŠïÒ©àÎî.½V§¿á%¹¶Ság&3ÚRM‰İ…j0¨Ş1½itøşz‹ˆ¢Òƒzûwn¼Š:§ı»Ïœ‘`²šP„ºP#o±`§U™»Ïô ï£Àıáÿ<RüR
endstream
endobj
77 0 obj
<</Filter /FlateDecode
/Length 4378>> stream
xœí\Ù·}Ÿ¯èç ns_€ €4šñsù 9vŒØù U$‹Ud÷İæ¶$ØÉW>·›¬‡d±zVcsù³(øûİ*.“ÓkÖ9§åÓç‡_ğ{ã’Z¬WyùíßÿúËòànÕnµ…ñ
ÔşıÇKıá·Ÿ¾ÿÁ.?ÿ¯´³]´6›û© 
o­?À­ï?>|ÿì–¼|ü	*êÅÆ5&mübìòñóÃ_•²şoËÇÿ>øşã &Í€›X€Ø«
N·¡ul|}$wÀÕFŸ>îîµ_NQH®ãÜ‰™:Ñ³äÛ;fíµwœÔ$½$0p“1ÌO‡óOƒSùiegqgùÕya¬2R˜ÁŞÓÓ‡¿¿>hÖ€Ü¢£_•‚XYŒñ·ì %]»baGõ'ñğwbÄ¸5gs9Œ~ÊºÅñš#´%ÿ…ç¶ ´aÔêA®ìòò™.btË^8‡© ¤JŞ¬³ºaÖ,deú}Êæå>tÔ¡¶gÖhñÆœÑq¬¢a¸c	ƒ¨„G5|Ú“º¨P´üÔ°¤¡9³*gMÊ)áÃ„Ê>Ò .Ş	Â»˜Ãè§?=„ûÕ^­ÖjÇ7#<ªÅM"–}ôdÈº´”VÀ˜BLÄ¼…?BÄbˆ1HµCÎ+F;aÄt2‰ˆˆU9äÁÚˆ:¼~)øÏ	ÿ!F®O‘ó_äı€¬`ÚE¶‹Xp~ ±ìIú&iöj5¾>L
!æM4G,†ĞìF6B4ç°H[f¯WÃ`uÄ¬jşëşAÔY·H/¬´HÏáSÆö‹—!t»Œ$jVÆ £“DALÉ`gİÅ¨ #É±CÆ”£Œ­.Ç#ùG[ò£åŸşƒ‘–úòı\(ÜœòFo´ğF2Zøçë†¶ö¨-@äøÎ–¥#O âf(ØÄC<¨C:Ašˆ¢`Q fÈÆäŠ‚%¤Ó
¶!Š‚NDQ±BíÇFíj Š†‰@ìMŠ‹àîbŠAĞÕÃ…ÕãªÛ‡‡_³¢¦ÕÜ3QtÇˆßØ¨¡¸¸Eñş@ˆÌDQ°‰(
6€a&Š‚MDQ°Q ‰I’Àkhx08B ÁÈ8¢bÄåŠ8¢]Ño—ADÍÊpcd`6IEø¢.2ÄYc1È4rÈ	åàb[ËaH^‘Ã•¼'÷-«†76xcƒ76ø£³Áë(^§XÉLô ÚĞb3= ¶ÙT jÇMEAfv@lf“·ì€ØÌˆmÙÑ™
VÙ¡şHìP¯Fv¨Ø‚yËÜùÕyË¤Î0Fò;}ä˜Ëv`k£8oÙü×ù Kv@çì Áì€Xhí’ˆmØÁ›b…óVš#¶eoòÀp=³B›ıDAgv(Xg¼êìP/Fv ÛeQ³2ÜX ˜MR¾¨‹qÖXŒ21dB9¶ØÖr’Wäh%ï‰±}ÓZáŞÈàşØdğú¥B†Æ:;3åÙä6³bÛD0fŞI äàKi;Äfzf“€,Ø”€,Ø–é¡`•êDõj¤‡ŠÉ¤&e´–ÎçdS†>©#IW[&²tdE9:ÙŞr“gäx'# ™Ğı#? ²ÙJ 6o%«i-!j¶v³•@lŞJ ¶åD§$`nÎ@lKˆÎ$Q°NxÕI¢^Œ$A·ËP¢feĞ± 2<ITÅ¤‘ŒvÖ]2’=dL9ÎØêrD’äÈ%?Šq~Ó²áŞˆáş<Ä Kˆ˜’Y`Ğ@ ¬Î§Ê—¥”Cû¼9Ô†`F†§j5‡yTÊ€O†‡VÊ=bYüÿ©â¬¥?ì` éÔ>¹^CÊ¹Ú¶¥áã1KöøªB‘å—ˆÓÕdæ×ÆC0'¬ù,`‡÷[D_:ê ?ª ÎG,ƒˆÁHµ6‚a8ŞÀÀÀÑÚZä#<D‘=€Sm•†;ø×Ã3ˆÕŞu‚àJßC6ƒÌ:
ƒ5‡Õc1
¬¼è°‚¨<HdÀt ²–²¦!°±Ÿ®£ÄÈåé†
Ó½pĞ«V	ìÅ=û­„Ud,€vMÀ¦jÚäœgŒÃHŠd¥f‹`l@£÷ÈÖ¢	vŠèŒı7Æ®JpLuw£
G†œQXHÊ—È-ä†ïBÔ&$œŒ#MèĞY¿&°°fèBÚ„ÁÔ()ˆ
¨·$8ö"x‚/İ®cè†[Àu.$åäó&u‚eD7˜uãMŠc"¹×F
nbF½T°aQ˜¢<İPa·—n `0BÔ¾´Úzg#\Ú…ÒÆAŒjtei·‰0ìğ|¹° ?ûXâLB`¬ÛOÀ X7µl‚<"ûê¾åên–:ÈàéÚîE…Û-•p0óÂ‡sP?Í36Oa\9Ê€9¸N.7ò7½¬ˆzÅÚ¿úÎdØÑˆP‰è¶}<ÈÈU²œ>|€L>Õ)Ä¥:M Æ•ˆ×*y¢wíaV9hùX§§2ÑtĞúZƒÊ6mÔµ'ÕŠ.wšŒ¸ª0³/<Uİ
ëùşÕ{ˆlX}¸ÿ‚	‹A'ì´‚µİ©İ Ö¾jUŒëëÜ_Ö*^îkkr~¿'ğ=§-u9pœiNõu-Cë—²Nñ,K¹÷	û?ÀéÎÃåCu›æ:Áú²Şÿµ ¾l²^—»:ä²âàRİ=\Ÿ‰i[µ´Çy×,ûT»Vşˆ!”âÚlÉ=!ü:=,¯EÒFK¦E]Ş‰èUg¢ù]Å…ÖlÙQÙìş=n¨`B€6JÎpÏXpl5Fµ¹ZûŞÀ?ïª»¥ÇZ¿ÓLn[‹ç:n\:@¯wããñÂ0öÆt~æ§®üZS5=îÎeà¾‚.I[&¨",w~¥°°>VX­y&.CêñÀ‰Ê8ŠMœf«A8
ßíÍ…ãÚ=}&#Ám{V·ÿÓÌæÏ·…÷Ü>£ê·T•Ñ…u®o¿@1?ëf‹ñ˜X´c—;:š9€TïıÀ×åJ»ˆ é×&&loÌ§yî÷Q]½ûúÁéaÂÊ¡º”M]tf}Óı°í»rù…XQ3Õ5Â×]‚u2cËì‰}s!ùóÅ	ìšVÜœÚ±ÛC–b&ïëCähšñ/ÂJüº£^˜nÛÂ“ºİ½v±iÇ€ú}å~yï=‚û
z$µ£‡•âèõ—ĞåñŠ±ì1½Õ¶(âÑë(Àä;'´=j(k/ğĞ¢9½Î‰¹/ïY•CW:§Ôxõªç‚[¾Û–ÔB¥ë¼éÒ«	ışc	Z¦ÉS	mñL1ÍÇ «Uû‚8—ĞV'XšY˜÷DbæÁÕ…ùdà°ØC:q4 eÑEjİÊ£ NÄ[q^"’ö‹ô>w&¤`âØ€•¬î ’iäÛñeD¡YUh]˜0ñš„T€áËGf<Ÿ Ô ß•Ô2i
˜]u9hëFaLN0*Ï&e¯p?ì@)ûšeç `÷¢j{*aT3àp(‹úĞ#n€´i“Ç Â\˜œrÛÖá›UÖ;y0'Q@ÑÃÉ`qõj<š <›°<œMpzŸûâ“€A*>5ğù‚Ğ•Ï"Ø.òˆ‚(O( …	)jy@°B-c © ƒ(Ñ:Ç°ÑVNœN`&a¢8œ ,gŒÊ£	ñ<¹DtÓ7Ôı,D—ÑC*îDÔ«%®˜ÿ¯8°FæÎ÷>—²ÄG|ô3¯ïi{†[µ2›fÎ|—¥·SS*êÜÒÓÕí½qv³}v+3ØWÿ\ÚŒ¯Òj”E½Rµ@‰ó9³²÷ñÏ;ønFúï¬_Š—ãñ WŸÉµ›ğJ“§pC4¡É¿]4¥Û2«Ny¹Tly¿§¢éuç¯‹¦Sr~›¨²ÀQíÔ–My¥éû½D‹z¥j®ç>Ï$óÎEnş•.EÕ¹¤ã7‰,XÁ¹T·«lÎ+ÍÌï&²ÂmyK—(oyn·}.²¶Gb_6²Ï
Yé¶40Èsa¹9šÿB›º¾‡£¶‰¨/ú«±äºî+¦è”J›ÂO‹¥ĞÈjv°KğËHûïP«YØ9—Bà_®Ö<Í»h|öü…iOtrÒËôëØàèÙ«p¹úeekŒ×üËát×­)k,¼ø€Ë$¬v!Gñ;ã¨k›•Á"¢ş…>ñ…{ª¿˜nÕÚÂÜèø‹šÉ°o°s&|lÒjò
µ?œÀo5ÇíJœ~‚¼êcpXÃŞ…rMmo±„›ğ',{ÒOû¹çf‚ÊWtLæÂ5Áİa¾v.ãWä3«ìQQã¬ßoÂ·‰š”1×py úSõÖ¾gcÒáú8“‡Ì–å#àëkßÏ½ÃüBsÃ¡EïïÚ*!óôW¦ÌvšK§WåpîÄôˆßmÓ	ÇÎ[<ÕÃ\Û¡63‘*¦!Am`]KS–%¦R’ÉMëü
†wCrÚ`şv¤Yä¦ñœ¢TÜŠÔ4c23Í¨LL3*Òº½‘ ‰Tq—]¤”IE	‘-dFšíö2¢n5ÖÊšy¬CX£*ï/‘@“çÙ„4d¤-¦ÉµÃ,yW±`X},2Ò„iFeFšŸgWp?ì4)»—eç(`÷¢h›‘¶XÀ×"Ldm‹Ğ!!¨YNQä£SkÍ«ö„¦	3iHF6sI&£«'"Í˜LE3*3ÑâyNär?œò•qr¸KÎ9dV³Íİ2Íf“9hËzØ‰'rĞå5v«‚•7Ì5&€dß3_sˆVä -†Pf9hÂÆ4£2-'OˆnºËºo…è"^ºŠ;1ôãC¯ .D.ˆÙq|ŸÂĞ‡8.‹‹VMQæ6lvn	AVµÆ‚;¸¼¹ºC¬µogğÜ£şpi¯ôêcË`î™â¬{DµuÛ›í¤éi^.Ûã–.Ûd²€Ø~Öíï½å:ÀJã&k‘
\Çoİ¢‰ãŞó2¤DİS[’RÔã]¯å;µêwV#Ø`{!FØ¼%@¯[ĞÑ;9ª,„”X(¥æ8ÇÕ†C–œ)Yï»T'‚TÓÎ^ö´?k\©ßŞ‘‘âº&¥AQõâ«Š£(ì]{×«4AÁdÑŠF¹vÉQtwê’¥C!<¥öyÄõòî»»~ªP\Ë¦íŞó
¿P(¶ÄŞp´ô|æ€€¾;•æ¥öNV"Qƒ&^0`õ.?¿<°çñ³.J–§ÌÜdÏM…¹å'ã—f¨ì;§Å«¥£(I¾,ê©3 “İ|)%m¸1îTGŸ]”Ş^!ú™ƒ†!¥¼¹ç’
½ô5ŞXE-ğar&ŸİCf÷ë¸±89İXÉ˜¦¢‰/@üÜÅñÄŸvŠ!%şQø~áä@ºŸìmØëq—í`_ÜúÇV-Ïİ]^v©éÙ§W†™¨ìŸƒÂM¼0Ì=•¥Ö‘6ÄÃ ÈÍ¬¦¥ïƒ¿şc#Ø!¯éá,ĞCÄ]½3Ã÷>)Dn,æIaŞ—}‘Pgv“õé5ä^æì{vşÎ‘æ½è—v*mîgù®:÷pxıÀ7–%Q‡ó…Ç>'Ñ.ï¨=µÖ=°{/—SgNT¤ë‘²ò_y@p_c@ä"¡c÷púå_<ù?÷‡£’
endstream
endobj
79 0 obj
<</Filter /FlateDecode
/Length 4344>> stream
xœíÙÜÆñ}¾‚ÏL÷} A iwåç$ääØA°2`çÿTõYM²‡ì"Ç»Ò¬fjØ]÷ÑÍ.jÒ‡Ÿ‰ÁŸïfòÑ)>{î½›>¹üzÁï…rl’šùé·^şñ§é€«™¸ÔÆÚO0Oøço?LñÍo?_¾ÿAN?ÿ'Ìg½œ8§û)@^ßÀ¥_/ßR“Ÿ^‚‰…|’v¶=	9½~¹ü™1©ÿ2½şûbàû×' ·¨%À€- ÉÀõçà< dè8Ä€Š“¾¼n®¹w–PÎí‰X áKÊ×W,¹çr	è\Ñ#T8>9p¢Ñ,G_gS€Rëh&—ä.ég×‰‘LPbVû˜GÿşüzáÜÌÔÄ­[™„Ğ`·äo`¦j»rF;BDñügÚ+6n÷ÍX€á;Ï“ÏŞÂ\ô7Œ[aÁf=I%•˜¾¤àfzÃ
ıĞĞmÜ„¸š'˜Tf<å:&ıôG;n¹‰ó©ÙJ¼Ğ{”E„(RáàîBÈÂâX_š4TÂ ZiAQ	æ8Ì'f¦¤p>ÁŒs8X U^Û|%Ğ‹WõÊºCóÏo?_Œ·åÓ~š¥äª^Œ£‘¯:%Â¼6Æ6Èw³0Â+B&Â´„ÂÂ¬±Ö4|ïÁZWDBãN¸*F„HæoäP%D3TDƒË:£²úß.äz„€ÄDæ0“æM˜W™‚H) å,t¼01`ZrÊz€Yc’à’É#Â„uk¨ØL²¤À¬  …_Qc„…ó8%dùğv!&R.'¦T¦%FG æYH­V\8"æNx¯~Q„D¼§“ø‘:ñÈ¢â¹EÄÏ?_ş…!ÂMñ/F†ü>PD•÷ÀğŞÃ.0ü} vHõGšùÈ‘Bi¹ˆ A;S4RH¥á a«HĞE¤E¤0P [Š [Š =·"@"ÂB HoS HŸš@‘`Ôó”Ôb#òE (dRÈìPo)lS·Êò!Ş—„H½´J›úsÖõû¬¿PÃ5NÄÌ@¯È¢mâÂŒÒ[Å	Pò*N LC8¤œ#l'ºŒ`„«8°uœ@¨’M˜ &ğS	ñC&òåÔÒ¬Ôâ*zj›™PbÂ™jê•sâYDÔs²(©U™SoÌÚ¡^›µH||¨|x
ïAá=(ü1‚”Ö91Ñ
5ÍJ»VÀZ:„í®'Ğe³Ã°µy‹J<1¦Ÿáåá%à¥áÅSO¸uÿ¾D¸iñç€¸K¯ Ã9 ¦TœçâğÒ0N?İ´™3ır+…ç ~.-¨KâÖ 6@ß
ÂÔß\P>Â<‰0ô|iA0jF?  {)1p‡®(0ĞyP¿’ŒÃ•0;×¸µçA«;w`‡*âÎ0e¸^ğÜ(Ú*§ƒ‘(ÀĞÈ˜&x ægÁ™o( :0eNiÃx2–¥F'(İ[ö³ÓåU0qé8z£õ„( ŠYkÁEä4Ñ`¨ª­Pè€™Q Bî„	$™d` ¬
€Q{YÖdŠª‚¬ê¯!¬ªš0Qm‚°»iUèmhr‚áf·	_jYL®‚ÁF‹É(ayéÑƒÁ¤Ç`È-¼òq€ŒÍ¸[!=°!$p9+7 nšÂáuÀYtø2Ê«ÂPÆGáV(œ…Pè˜¢ã……UH† ÖÀ;PmC aÍ%\€Ôxˆ•Á³Dat‚¹½]ê Ö³³&L kb-!
€À›á©HÈäsi8¼*0ø``4Ø[IFÂŠü+¢¦SdP\Ew-]EÍ”j<…Û-‹Êæ6²[yâ7¦:ı9,aËD`–‰@a–†pò)ø‹rëõŒûóñf2DÔBòmœõüR£ÇXE±`úĞ^:´‹)D¹˜&Vïe²ƒƒ„“(È†Ë§˜B:ÊéÎÀ-àšóÒ­Ø•]v›#SZ¬*ÄR€;£¢ZABC×—®¿¦œÛeš¯5€w8…ïËœY¡c+úx;°ù|EÀÒ¦Ûk”\T¦øÊ‘—ˆšé3ôél(@dŸ½	Q@#nÅG-òò!¾Ç2*”SOä3–gÏQ¼§ğ
µdı¥d[f½a°ÕXÛCt‚9ÂÆÕx‡õAİÛ²Í?Äê?Áä‚‡³áüÂ§‚÷St åN`GK¾Š=íø³–~m¸Ç‚€³9$KÌ|tàñà
¬ö9Íçãµ*Ë,ym]ÓÆïv™…ŠX©O“ˆ†l+.e£g†$²€]3Z˜—3“ç5·‰ 'à°$^^^Wiª7ào¤)à45d5QúNõNÅU{|y~`]ø=t½‘°äF{–IÓU%ç ùPŒ>€|›´Óˆs±§#ì`-"poŒ’wŒ5ûmÅÅİñ£óI;¦–Êƒ¤
Ê¹Û&®D*‹ÒvH¡~~Jnø’Ê©Sò9&)ƒ[¹Ç”%Ø=Ê2‰½Uô‰J¸O–"H%3ÑDB¶‘ Muz%H“¥ô÷Èr7BŸVÕáŠwW¢y"¤'»GŠZÍy9VQ”£+d„}D!ssø¯ä$ß›ßsVÉ?Æ®äú[Îv•¼ÊÎCÏ"Ò]›ÍİûˆÒÑØ¸Ğ€Š_r¯ëéÖ|,xüE×C­ñ7¥½åõ€¬¡RÏŠIoªrê5¢° A§²i„Ö[]¿PÓÀì­¨Ti‘‘kï)
Û#Š§/˜ÔŞèİ‰Ò¾30êµæÈSšJ+î½°«çÎ¾p{ØµÛIŸÁt¾o1´Úè’Ûo‡Ol00ãÈª«òqQ©Oi„0‚ïãî²qîaË¥êsl“(ˆV®ã4ÊÙ}Üı©úJttHvrˆƒ^é{ÈR*áÌz'Wf•Ãñ:¹@éàSİWC_Á£4HXnX¯ò—X=K®tgD¡Ì‚Ş­¬'ş‹z Ù*¢­É©8º'å¥M-«ø­ğnA¬&++,[0ÔÁŞğéF”ÆñGøBE×IºŠïyOù!¢Tİß{ÉèCöPÏ=îíÊv88t¹83$÷}}Ôx†q[B¿–¶ôyö"r?Egƒ¾2†%˜“¶f¢X·;ÛuÙŒ¾VRú²dêÕ7°İ-¡ºZíZNOK©më:wJ.zÉ`¹E‹é	ÖRÅxx¢'ÂçÄ‡D
üádr&ã~°şíº÷KbÛƒ9ku^û¡e¸&Ğã®›IºU/íõ˜ë«èe44»W¶tKFaÌlÓöq~“xç
P«ôppá×ŠZù_¯úTy·ğ…Rk®
‘öÀ*‚I²íYyÙS‹Á3PŞy»æoˆ1Ãf:¾`ïGŸ®É÷JÀ¦ê8î‰µÂ°ş®Dİ.ã£¥ìx}Ö3…ñ}Šñb¡¿y’s Æ)çà‹]£êm	t
İ°cÒ•tƒ–¿÷1T††ßƒ¼¿U@—Z››—G·BtÏĞù%­£›¬Ö°GµáÙªëç¢Pjı»NBVÎ6ß¾©¼|“Ã#Æk¿D]•ö#îàÖwwÛb|gd<-öÃËx	A7ß_BÜÀø¡€K³\7íotôÔ:œ`óóJû|Î¨Á6­¸k-™uÁŒôØxS¾ğI´ïGn€X'·u„Í ›ª Y¦Ÿ5ºI±›ÉT¥$‡¶iÎêæ“&óúQ59«—şú¬÷¦ê2Ø/¶è½ˆ‚äpRşVïhŒÓÛ³Ş~ñÔ±Sl˜uÏ°úJïC$Ï	'pÕ ï9ô»u•ánö.ıºåU·Šê×];åU¬Ë9‘×ğãëÏC[ÏMN;ñ®ÅğBoE×¿%İª›‚oİ…âÒÌ¹f¶«ıu (ş¦Êÿ5r%²%Âñ}y—µdÂUQŒj†|å	{fÇ5„ÌG/Õò Õxõß_¥É4ÿ/ººM%+¶»÷ÉÕ¥0¹“©
·Ş¹9ŞÚ|¥§Yişæ§ø9ŸüÓ¶^‡ŸÏìm–*õQ6­ÍÜ§îØ¦µ b6ÚĞÖf€ñ™;Ù´Æ‚{ÎAé´µ Øà(<im0lJ$­ÍF[›+”¶6W(i.xH1¡ˆ4ÚIgrá±%iĞÖæ*¹·ŠMy66ãiRì×”„"”	¤îš¶f<¸9ëĞ^xXàÑ¦æsMOs…Ò–æ:¾ê¢â©Z£UıVÚ«T·ìhİÌñÒd«P0hŸm¬B€ÄJz™Ñôgí” ı° ³ÕÒÒ^f<¢<û¶™9ÀĞH3s…Ñfæ
¥ÍÌd|é&xJãpCPé1&¤—fdÂbé[®Â İÌUp´™ÓÏ¬,öæ×®i•… ıÕPsƒ	qÛt2K<„$ÌØ·óà³jkw‚¹¦¹Bi3_ÚÊ+šÚN	ªê•tj1™Å+ú÷/C8Î53•ÿÄâa_CëŠ;N­;Óà GîÒ˜BÂiWÀşÌ=¤O'Á*‚ı^á;˜Á–ètO´bäÏMêŞ…ğ6eï-Q\U«'ıãë›hç¸Vá±A†ˆ$	5¢¤XV»â9êc-'NïİÁÃùè9•ŞicÃÇBÚ2IÙ$éš¥ÈÃ“ƒRRf•şdYYå.Ş¥ùY:¤ÅÊâì„mdWÈ¹ï1†Í¸ÊNWQT‰œ£(ù‰Q„x‘^T•6Ãò{{’BÜIÏ Ü¥v•ıÔ³Ğâİ4ç¤.ìU#Ú'ÖoªÂ9tòu¯	>oè™Ş{zò m/%¹{•¨qjKÃWZ™E0(Aa!¿k-Ê¾—&¼.Oõ!R õzáÖ÷;4Ğî7JÊ!Ò!ı@Óõö5{,(­‹t„Ëäˆ™ô\„šÌæ5‡ b@Œu#[Åè+Šó=%ÿ!¾%¾m¡;/¸ãÎèãft?#úâ
Õãtûµ/>[m©ÓƒffØ¦_dnäáJS(¼Î°´ÆF†£o˜¾¿Q™ÍjEXıO"î)!1‡—GØè›MÄŒ-¬].b*øLó,²‚1´ÙæíL—·HÏğ4¥òV/åï¼ÈAŸëU1HK’ÎOßi"Æ#Wë—ë°‡ù~Á”ò´ÇqÎ‹a,û“ûº[@åpDnÛ¯ìã×pÊßc¢bxÈ#©B‘¸d‡™«Ê•c‹§õ£ë´Šâü:’ÿ:­"Ø}<‚ Aç5†Êí£J¸°BHX¬èöó³^Ó!ã³İeİæ3*NÙI«HƒĞtº‘IVåW5­òÍÌ=‰]²ŠR¿ìo¶35,?7¦àƒ¿[¿aÁx`ëw«(a].´wHÛ^îHá]ë]©Ñı‡JJ‘ÚÆvÇ!=“gV`pË.áx[Ièmª;k‚C”‡çW¤»ƒg—v‡×²#tÑÙçØ5CcUîï'³²Büæv|±CÕ.³MPñemÜ%8JĞr—³vUµe?¢ˆü4KBö)÷Yğ‰Eik•L½û #ŒplEÑ1Ë±-¯Ù£+ Šâü
ˆ’ÿ
¨"8ò€¨ÖôÎÛ‘ÀÛèi5F8~X¤[ËØ¯ Û£ÄdG#WĞô6(®=©ëˆßï?‹4½R2è!«ÿï	
endstream
endobj
81 0 obj
<</Filter /FlateDecode
/Length 4825>> stream
xœí]Û$7r}ï¯¨g›Ëû0ŒºgöÙö ş ­wc´À®ÿp¯‡™ÅªÌê¬iÕ3*©òT’Œ;ƒÌdhQ:¦?Aÿ°Àe0r‰2Æpùù——¿¿ğïÊqÑVÄË?şûå¿şåò7ÂÍ"İêsã5”şûºä/ÿøëËÿ¤/ı¿ÔŸú"¥RÜİ_"øÖü…nıéëË¿˜K¼|ıu”(”í¤²¥/_yùW!´ı·Ë×ÿ}qôû×?_Pa˜5àà EÂ¼) `s“Ø “;ıüõ:áVÚEÉàré×ƒ¨Õ rMùö5÷R¯É3BU—@.4ºuëp»5)µ·zMîš~q›-³ØOµõ¿Óß¿¿HéÇÌEz»A¶rQÊ’İ*’¿£ºíê…íˆÊß ñ¤ˆÒºEußŒ~ˆ²Øñ=õ…ÿ¦v[úPb±mbt—_ê…Õîò/ûaHÑM$ñN-¦MÂ\ªİ't¼üÌ­ƒôÒåşÌâ5ß#Ë"#Æ‘T$¹»Rºbd•ÔTÒo®´ÔÔFñ}^{ÒSÁ‚¤îÔ"ŒV!Œœ+"*Z_ï$rùNG¿úP1¶şúõç}»úÆW‹ÖÒô›q–Ùê]2­s¾ROaQNEd2FßµvóÎ{‡l»ÉV”4 ÆdP¡‘-¢‹ƒ´5ÚYzIéÏ€ş«Î­ªò¿½àı„,$ÚöË˜3v €±h*…RRò¢ln\bÌ*?pÎ˜w®È­ÊˆQ&eIF¸Hï©3¦EÑ_Ó£&«§*1A©ÃÚŒ)İ.¾½ ÔÛÑJ¯hq}x´ÍJ(˜påM½s>QE„SE‰>ÖeŞXµƒ^[µ>şóËÿpx—üG…ú=RE” ğ>‚Âï*(üçœ¡ä¹K¦Ğ¢„dC” D²1J$L›ƒ„m¢¡bŒ	YE‰„­¢„&VWM$,H‡:KXvTPnBWQ"c)J”¯%J”«!J¬°u	ö
ƒƒe72Á;à+mpª&Ÿî{Uˆà£ mğæ¦ğú¦¿’†[”HÊ¢#$…Q"a®ô[)`,Z=D	=K£DÂ¬–çŒm¢¡#_SÇƒÀ"
Æ ‘P£FˆŒÕ‘®j„(C„h·£ÕnÑÜ:h˜…R0_æM¼s¾PEƒSEˆ¾Õe^Xµ‚ŞZµ¾}$eøÁà#ü“ƒÇS…@Ùx‹ÎËUtp^l¢c«EÂ„¶«èà\\EFÖÑ±ut 1×Š„­	ÛFF×Ñ!a9:ä¯5:ä«1:dM°v‰ÆÚG«®d¢åWvĞGÛèLU>àsEˆè›]ÚèÅU/èíU5°†{t`åÑõ‚"a«EÂÖ
ízA‘°Õ‚"aÛèÀèjAA˜[G†¶‚Ñq=‘¡ øªˆ|1ˆz;ÚQé®¦Yè®Ü ¡w¾Á#ª€Ğoª ÑÃºÄÑ«nĞg«ÁÃ%!á#$|„„ßCHx8mpÒŠ#¢«uÜÄÆÖ‹
Æ¶‹ŠHÙÖ#YÇÆÖ1"j¿YT0¶^T0¶Œ®cDÂrŒÈ_kŒÈWcŒÈaíÍµv]ÉDû¯ì §4¶Ñ¥ª|ÀóŠÑC»´Ñ—«^Ğç«şjT`·‘”?ÄFÖ‹Š„­	[/*”ëEEÂV‹Š„mbDBW1‚0µŞ‡LØf2¡«•EÆj”HW5J”‹!J´ÛÁ’Z·`s@ Xg#µqãŒxï^Ñ„¾Ó„	^Rlú¿mz/?’:|„…°ğ~7aÒ‚ºÙ*sYå)>lÀ>¤—9¤½6‡·CÒD*–÷9Ô«ö>‘>Š>–>RóÊ/†Ğ?gÜ´äÛLğû(ô‰üVaÜaÆä>¸/IK¿Ù×‡^¹üí…ìtQQ’ø¥$^Ëwş°nè·†’úÈê!å3‰PÆÂ",¿DW‹Tô‡0·RN/?+Tßs"¤'µHJ0ƒ´ÔF7:e 0iì†q0‹fñQz@ÙX#¥¼ldøLOÁ„…q£U‰¤)R$:²e‰´&É°Ó8•GÀš4Rë‚‚è¾0É&h~–İF"ĞA9(‰Rï¥Êœú	&b£7ì•Q)î
ïRE&L„uÌÚ«²†.ºR`°®¿°®j`¢Û°{ÕªØÛØä”àWé\ú‘_C*&×a#\—& š+Sªƒ¤phHÔÆFEò¡6Q*Î$T§B	(bSHà‡ ‘Cr¼Pï#vƒJ˜®×0V/P“Á5”ÎS¨Â`{åÍBnÃ(23òØ8’£ÈÌ”%aáŠÌLrtæA©uAAnß^zÓİ8›z-#IëÈ­ã¥X#Š@EÄ×·*ù“=Io…OÉ´JöVERÁLX“ÀDX5vQ5‚c5İt55#h<ÛkUÍíÈ»päï4Çñ\G¡¿Îkl=¸õD`Ò#àÊD`b	şª½XIzá·ÿò¿x&ãF¤¾$ºíß“óRúd‡Qxú°>4uØ§ò4ÁXq/““Ñ¥Õ‹š9pùš§§4ÕéÎŸÀ­b·”òmØÕSv‡×.¯té9«PkŞi•Ô*…=v?åùşD™Êù +Íç7F9„¸Ç)ıŞ^];¹bÌ/×7ÌsÒË»H.+S}*éÈç<´°gè“æ§Vƒ}ô1>4ECŒ„É&‹šOù;§Q)z…kNÏŞ²xOáÕhõ×’™NĞBÔrvOÑ‰úH›WkğÆ†Ô§Ù–Ÿrv(_Ï`Ã«ç³â6T,	ï—ì,&œÀ%uW†¯wüÙòÂqm¸û‚€©oÅWK¬	|vàãÁ!%ş²Xí[é/æv¦Ê¬xm’]mïóow™Õ´ÄÆegjäã$bi6§—ñÙ3Ó$²Ân-÷Kk¹Ò¯{LuÒIñòvğºIeï£)éz ©jBúNõNZ÷¸×Éße™DĞ±ûe|‚%j¼g™8]urv’O>ÿò}ÑzFlîK¼îa‡sÅÖ¼ìXÿ`rñîøÑŒùŒI;O-6
ªs·ïœ¦´¨l‡4êğúµ¸áç²årÊ|Î“”ãMÏÜ}Êòî=Êr…½Uì‰JP¼OV"H'3ÑBbµ‘$Msz&ƒî“e´ï‘åİ}ZV£TèŞİˆ–¯%üë3¤hÍR—c}ˆ}rä©C÷ëg$2‡ÿNÎNò­ú-çaüìzùkí:y;Ù‰âÚ»ñ{j¯òxi,w€U­h¹`Dš+:éûX5âiÖ]VÍd¸‡ØCíäwvŸz†÷ãè>·ğ#(AQzó|†–²õhu>ô,åE´¼©Ù;çƒÉüŸ°5ÜæãÂ¢SÎôÌ—ô£rÔWÇ_.uˆî›àyuiLpnsüšJ[gÅ&#ÛXXS’’M/ïó,ËÈdÂŠ7æ¡—^¼'›íÒ–¢tDİ­ıİVO„aUı=#Èâû|ë©B[Æx üú3CòÁj“¡*£[Q(­cÔv=0;‚^…5š¢­Œ±‹Â†ÂĞ6:à¬vdEŒ>ª5ËR
õ­Œ` Ôİ!¦LõQıÖ·cÏå¡g]Mä1¢şVP¯3¶sJl#H£î‘-_ªE°=Y¹¶d~„#t5áçÙSªBih¯ŸÃ /-œòÑÛcÌ;QG“M´‘_UXE:¿ÛEóóœÉö¸MÍ¼uJSÁ¤dñªœèË8vĞWMglQÅOÅeô0Æ`!Ç˜ÅŠA„>èëü™è¯«˜ò1õğÁ<‡é|flÓ6ç|©æÒ}«²ŠD•™Ä—}œï&ì k_Èİe?óx1¥÷û°8UûÌmw%4ë¥øN/Ü%‘¹ëÌ„;,~sdÙ‘k S™v5w¶b_iöóDº Y%h=±Ãàf>àŸKWQı•)j¿HÌ¬Q·ÍŒi8Íİf†;ã‡8æC<¤¾ÕT¦IÁ4#™æ¦ÓĞ3ËÎı7bØŒÚÁ5œ¼ŸÔ˜ş6è”¾?ö®)Ù›‹j–ì=‚Ú£9?•Ş/Ã9Sóœæ‡æ¡…{ÂjÏ)utqÏ¼±Ï	v%JûVCŠˆF±#¯›Óû‹‡§§)Áóu*Æ]ğı“Ä	½òS¿ëN¡]ïÉvwùÈ®™ù¸¡Ì9ŸZéáLéx66gpf?ó1fb–Íü¦üjrÎËfkvøù©´ (º“óiB45÷ã+µixÜ|Î[K'vL¿ÕŞÉCm{Ãñ×™,á|ö$2‡“Ä£Lìš ş7z[©Õy9åt3ùğNááÍ‹ãşÜM	á÷hcr¦Qxš(~äÎĞñ­–¹ÔwìvÌ·Ÿ­Š×jH©¦"<¾V8<‹ß7™~ŞvÕñÍ§²û]OZ®<™~nÚbf1]ÔıĞ½½‡©:qoïÈÖğñ'SG?œøŒäøÒÿŞàwÓşÂåñ¤`:1O7HCK½ÿÛâsrı¦ŒXdäÛÍ¾>¼§ùL9=@Ô4‹>¼oúŞçgÏzà>5ª£Û÷ó!fYÿtèÙ¢pºopôÁL|‡Øò€Q=Çi0ÌN»O|Öö=6?ÙEîN÷ú?ÚÚ—Xiÿñçğ}‚Ø_ãVUÖÄªbğ{¬pÂË–®¹Ï3+c¨Xj…1”–ù¬ûPƒP½ğº§K ˆOj¬«@u)µêb(-¸ ¯ŠP#aš«Éô²ÃºÅºíu%ú8½RÔ«UtÚ{Y‹Æâ Y`YŒ.·o#šËD@QÂR=	,ÔAX*=1–Ä 4U©ğPƒ°\å
btëatËatTÑÆ¥E ŞF;XAãñšma¨XÊu08¼TC4½i­#ÔÁ ÌÒ|lÔR Ì}ku0äš<aVë…:†…0:Š…0 }«$ã´¢A­>Ş
Y ‹­æEVÂè‚ÃB„¦Òê`µäHQÌå&üPƒĞT™BCÂr¨Q±0”Àè(VÀ€öM}˜®3$¨k·“SY¼bE?¸ö…oEÒ1«/%,»–¼ïÄSpÃp\+½¡^½¥Ù‰»İ€ó)zè(ò™´>€ÚÌ/'0!¹öv,ù6,Í®´3¦üOâ®Ëà¦^àÜ:~;ï«uIúHõ ‰‰gM¨…ÓÓÕ'Z€¤YP®ûáÔïpŞ´•æ
¢iô¼ÿ ¡Hf¢G†*•ce|Ô¬ŸĞyÏaB/’€Ã0Ü]£L‘w®•›6	Ån}N²QÖo«^ãoÔe8ÃZ±RÎŠÏ÷m‘^Œ®L_1ÓT"¨œñJVJ€æÿ~*¿fœóèSûj/Ëa_ úî¡² !óyk¥
ÅMÃrÇNKz(ğäàØFzbp¼RâÔà®-Çz¢°¦÷pß$ùL09šZäsë¥"Uî~Œn¢˜[f BÇíÏõ£¢ï3”z2¯Ié@K	7­:Ã$Ü¨"ÿt6ºÖƒ8«®€¶¦2’ï§ÛÉòp°.J8Xˆ$@¥ç›>Òó‚M¸R·äÌ`®—m¹lÒ4W§7îŞº½Õ£Ó<å¥í£7ˆçenškÜnxZPêókìnHÂùõšoš0Ô?ùái^:f–«˜”Jù˜s‚‘ªUÃ€È]‡é«^®Ô™yêaúSë!óFÉv~k‰ÏİªZÖZ°ï±3¬i!w‡’É²oJAÉdIÓ’Õ·†5/ˆBÜÖ\æšœqÜÖ©¤µô¸5œ0‘÷-[Éä†%“:”Ln(”Lnã@Éd J&7Ú¡<rãqÀÚ®ÔPHYÕØåÿAí°7L˜]¼àm½NQ eEå‡­aÃ"·°5œ0Ïo€0
6nw·†{{PE”Ö	í6ÊÁ
‡×¬h»3¬}İ›Æa-agP¸‚°‡aÂWÆÉÒ.Il†ÉÒ«M…dIsJHz…ä†’:THîí{…ä>N/‘ŒµÛNyÛ×Ûpîw±á¾°ö‘>ûÂ„qíúa_˜0®k±Ú&ÔR0ì–ª@ã¾pÅÆ}áâ¾0´ošèÃt•!A]·t°—ÆâúÁûÂÑ·]Á'ÖDî£´)d5œ·›„›¸Àİ³j!s`ªÛs#›ó=êkfìjOêãv+†'ÑÿûYùæ
endstream
endobj
83 0 obj
<</Filter /FlateDecode
/Length 6212>> stream
xœí][o¹‘~×¯8Ï¸ÃûX°%+Ï»1°?`²É"°$ûÿ­âµH6ÕÍ£–<;#{4ÖùN“¬‹ÅK±7!}øscğ÷ÓF>:Å7Ï½w·_~<üó¿Ê±›ÔÌßşõßÿõo· ®6nàQkh?AA~Ã¿ÿù§[üå_{øÃŸäíoÿê³^Ş8«ûk@>G¿|{øÃ³ºùÛ·¿BEB~“v³}òöíÇÃ¿3&õoßşş`àûo¹ \¨°°, n^çĞ±ˆ/€Š•~ı¶O¸æzÜYB9·}#¢k„÷”OôÜsÙ“'f„
Çoœh4}iÿriPj-ÍdOnO?{™É%fØ—\ú?àï?87›Á?êÆ­Ş[¹	¡ÁnÈß@MÕvå†v„ÅßHáO`—ÒòÍ{lÆßyìxóê¢ÿ‡r#u¶é›4¨û‘>h¯Øí;~PØ"ÒUî†©$O˜T3‰ò“şö–vÜrê“n³ôee@*º»2c`•P”Ãw&•´PÆàsVZĞSÂLlLIá|ÂŒsXX Q^Ûü$‹OñÊºŒ¡õç_y0Ş–OßñÓ&%WõaDŒF¶j•ˆymŒm7X0Â+B&bZÂÂbÖXk(ÛÆƒì˜àŠÈ1î„«BDD2o|#mD•4Z½ô§ˆşË¥²ò¿?ç!ˆ©7`&Õ›(˜×™úH)€¥p#LKN9˜5&É-É( YFI–€‰[C¥0É’ş²~ª¤º-F,Ô˜Ëa)!Ë‡ïÄBÊãÄ’JµÄæÄ:©ÕˆGÄØ	ïµW!‘¾S„Iz‘:éE?¤ß=’^şËÃÿ ƒp·øú…ü{p) .ğ)náÃ-|¸…ß™[øóBÜbTƒf?a$s­Ÿ Äö~"`ŸØà' 5­ŸHç'Öù	Àtï'Öù‰€~" ŸˆXğé×ä'Ò§ÆO$ŒÚa®’ZlmœÚv&“öÌí-…mÚ­²|HïKB¤½´J›öç¬Úï³ş²g@W?Êoı„F!×ø	ÄŒÒˆyå[?¡Q
Ú5~1-lÃ¹¿÷~BÃÄ‘ÊQ‡Šë@Aï"t µu+.B~“‹ˆZ‘§F”«¥æV	 †™(%æ‹¼P¯“¾EC{L!í[UÖ´f­ĞŞšµGúöRĞğá>œÁ‡3øm;ƒ»C+É”Â8°ËÖ;8Ãï€Xï½ƒÓ¾óˆôŞ±Ş;8íï€Xï½¢½wXôñ×ìâ§Ö;DŒš`®’kmœZu&“Z~f‡ö‘Â6íLY>¤Ï%!Ò¾Y¥M{qÖííYÙ †‹wÊo¼"ı”"`İ”"`½w ÷Ş!`İ”"`ƒwh7¥ l˜RlpU’zˆe>e‘>4¢<N)×J,4Ol³ZM¸ğCLp^ûDé9E”¤™“ŞX´CzmÑ"éã+!Ã‡Søp
Náwâş¼¶MrûÇ(vÅÚ›Í9ÜúAĞO`›ÒXîpª‘auûdøÆ<„«ú† gÜ!27F@×€ğ@¹Yg@!wD/ÀD?$,ÁÃ³Ğ0×P‚†‡ÆàgÓ*PPAô^mÖsKaÔ2¯Q=×ş˜¦’3ß&$é‚YQ& .Uh¬°KÀ*šPA‚«¿7(xæì­¶dàæp3µeày	ËG^ı@#„ÁZ
£†ÉK™$Ìñ ê,ÀŠ¢³¬kùª”ÚNÕ¥¨ªºÒ^m¢°¸gShho‚á²Áïpû-Ù[E?IUíÂİC‹×Ø28Oü’Ñaøo¹ _öIa¯3’óĞ‰À#aú¤Äæ„qå¸'>
úW¹\fcË`46ã“±UÍ‚ƒpL5U«6Âiæ‡­¡KXœ6pAY×@XM˜¥R	Å\Eøı¡V ^&TÒ@ˆq<Ì2M¾Ô<™Z¦^;b„%6µCW]H–HÅĞMfñU*’&å³FH3Ew”¢dB8±œÂà5eK[Ùÿï:ÀQáã‹!UÕéVØÉF/§š½l…ã1ƒ2nf+è$ê~c OøÉ{ÙØ¡nñèø±±É‡#Æ6œiÚ¨»ë8˜@¨Pº 1¡Bµ8¯œˆô‡Ú€ø
<ñşu‘•0üN#æ“ºãÁ€qŒÑCcaÛƒsb¸×›`’Ë–Û/{şxd…nÕÇŸšƒ;`¤@‰É‰F^´eËóô§ğqÒ 'mX»áÎ—nZR6ªPù¤Åa¨°Ş¸®í‘s¾ñ¾~-£ÆƒIæßÑX´plõû'üî2“kuW†¿¤>áRg÷W™£eAÀ®iîØ(q˜kåE›7ºg“ãO£pÚ¢ 
ÓQ½ZùxŞ«ùü‚¾!Æ2,[m¥Ú‘Zg²×zÂxı^½àÈè³Ák§ç˜¾@‘JB¼§“+«l=©DÂ$SÒ8§I§—ç0È¿7ª-½7¢Ü¼…7ªõŸòF&~xM¶¥Ò÷Ï©ÿÀsês|^=g¢.ó^'©oæ½0¶Š¡DmìĞwA°¹1®ƒ‡İSâ‹&\]¾ì¼.2i4ŒO"‹¥íÑ1^aÜZîµøyµÓµ¬­4yÛ`Äco©ê¢/Kğ+¼¥„ˆ>N´²¼%Hgs£„Şåğ(èa<òu™¤t0&QN{åëåÔÕ-È¯_|}ñOÚÂd“{Op—
8¡½•ºÄÍÀ4¼#x:Ã»	)½'Ò„Ål
XQOkŸ¾pu}¢éiñ5hL
ª:ÁFêSQ¼áµ„GqÆSmÕŸÛ\AMÜ¾‚Ü¤ƒ« ŞyÜöSª	æÇŞñQMµáRÛLjoÎp±*şù1™-7®ò§ù~ÛêqÂ÷”‹i˜6±.ÁeA-÷=Ê„“jŸm\~;T7ì>.Á«8? şåkV.÷“îTyŠµ%”ùD²ËÕ|G!(³²æAÔiş¾Ë“ø†ë\ñ(âe§taœYÜz¼Ã“Ì¨š±1m{Ní¬ãL{ÚSj¯Zç´lŞxõÙ®R;÷b¯êµ@–Õú; §öü9ÊCP•ïe÷v¥9¯öÊäD`gFqqÂÖf.´ŒĞ3{¢ªå„qˆtİdğ¥İ¼Ÿ”(¢bD¢&á–e_¡á£jíG¥‚åU‚÷è1÷sš‡Õ“ÚWŠË8†àµ“};
ÆFíı(ôIÈã6˜€Ğwü-8Bp†½¥CĞ‹‡-ÿFd‰F›NˆƒòÇ |@­œt›õ¹ÖO”sjïis–ePæ t­tÏ·İ<zT’‘[¡mp}Ü¿CItŒµTKÔt¬ñ'¨šZÛ¹®£àO¯©LülîKÉ=7[&%ÚÙ2û9ú×ƒùLsÚÆ²¢æB<·j³«t\µQÚí›{ÃÈ}>3Á¨[†©ã©¡ÚÈ¦ å­BĞ!†8¬Èëá«ÁE QvÇG÷c¼yˆ…?ÆïŒ] 2%wJ•2“&&I5ÀSÓóJ€&İxã C†È—H6O‚$Gæì±˜fÄN…‘‰5‡™!B™[^aª`Øï«Vxİ¢Ô,‚h¦ŠXálµv96{£u²·?à¨¸íU•ñ1{XZÏ3&o}V®ÇT.qbĞ
ÏDÊSS˜Õ¬'·¦AˆÖŸ˜kÌçËu‚ÍÃßÈâü…ó»_çÑòBßë¢ôF†3¯:-°¼:×ÈÜ²á:Ÿ˜ğ`ª82á¼ÖHsÂ:é¼¾|“Xø`p±¥ò9¶üuÚæÁhE+#AòGüA²Ph¶.ÉÅ
ß~İqİÙÎ·İé¢„Õ'†×÷XÂ¼wvpÉjáï5ØùÓ¬“â.ëœHg"Á5¦ãqXqMÆÉrU¤ƒ¹xh_§#ÚáÀíc=œAZ<&¸ƒÄª~ÒAÉrÈ2QãxL¦•³b÷çÂ¥ÈÍj(h.g§Ë™T9ï‰CÈ8Crá ´ *iÉ¥ÌKaš\8€¸báÉ… -5•‹€4À4À5—Œ4VÓÎÂj†a¢f²v)XDCsáª¿·(˜±“†$ÃÒ¥Ê{r¬h’á õú’æÀ‚fI2\Åh2\Ei2\E‰VJ;D„"¢ëB;1ŠÂãUÙpèÌ²Å”£…&‹k`‰ùª^“t8 ÙÑ¯ 9U€¡«”)#5e_jÌH-IZ€™œ¥Uò¹HÓáLÓáh%¡Œ´U2ÏZªJ’å d³Q^Kâ‘Í‡«B¤ùp_qĞ)*¿6¾uÓ:æÈeª`FğP'IˆÔ‚9Zš˜É“$!.c®Iˆ«(Mˆ#å‹Jj3Uy” ªçJ:±ÂâEıäŒ8Ph>gà“ëe|İia’YP[)ƒGŸ%vÙáoijªáî1JaÊƒÜ%ÀÁOåT –ÍyŞ,=HÚ’WG«ºH2Qßà<ßAß¥•£ìUñ–ö ™K®eş­ÌAhUÒ$Z)Ü—¬9;RodÉ¡Í‹&àØÚó¾,D¤t˜@æ‹Ê–Ø¬ÄÌ–Ã¬x–d!áÉŠ¯e|*iY,íQ†#ÚVgY7¢äYTÒN²¢Í[±òªd©“¬ÃÖ'ù¶kiuÊ«9­»¬ÖêÏwö³²‘®œ*¯äŸcWó1ñæÅç¥¸X<§Í¬Ï=%á7£bşo%ı$«šÿ,Vïq«zÍõkË~«ïá<h6oeõ§dš	>.¹àFJóÖ¹ƒb²,×p6b¸×~8ê£¢4Î+1lû¨Íiæ ‹Ï&­Çáı…xÕq+ÓºæÍÏ+Óy•‹+‘Ç“zX™ƒ¹8Ù`*E®¤Ñ}¤¸öÆñÖ'35"²¯S‘Í)Kk|àPóãúÛŠdR§Ùk·ãRöôÎy‚¹’ŸÒB¢ä¦’ıZ¾æçÃáWŒ• "EŠ¤µchW´´BaÃ†ÇŞe½"†ÔuÉı¥FcK”Ÿ‰jy·¶Ï:ß¸lÇöÜ½éªõêÂq-àlÈ0?^ÆŸÿ¹.Of}û|yÓá­ÌóÀß9…3ìªÌ,áºë›b³=£uC˜œYMâLjw/Ì°j¨¥Ç ç§XsNo¤hò»ÎC¾ğ\ïô´1íàô„Å©~Z/ÑÚaã=ò¾ÎºoÔDÍÍœÊï:•3Ñœtş’„å}Çáô°úu'^¦	lwì¿C¼JñÔÈØkj@ÅƒvJŸ²Ş‡<e&’ç€‡{<–;Äç#½sad.™:sø÷d>ã¼z ³Qá´ãÎÚø©öSùÀıiê«O…¬>¯&]w³Ã4P™GIëg`N˜œÎ[Z>€1=É;Ôúá–åc$×eúİó¯Ÿm™EêSS[·¦ùŠ'ZO–¼óÈì‚ ¦\¬Ïij²$;a=˜Ou¦Nû]’ÁÖ…9ï×%&ÎCòõ4Ã#ïË }µs¢î˜¬ÛÉzœ0›uÜQÕrG¸2d]¶İõ9Ï4ŒŸRõÙ¶ó6¨£öê„%Î58“î|f3™aO=I¹eï…pIêÎÒŸ^ªZ¿êe}dœ{éËÖèæqÛeËŸW”~}®íY\:7‘åÄÈÏ§ß¡§ëB·“ëw§.×»0&?åÙæ|H?±İsW,¯æÜq!ÂtÙdæ»×ƒìifæucÓtqí˜çşáWĞ­yUh<ÕG=¶Ÿ‡'pQx#7s;ÃT9ó""Ñ¸ ¥„İ	KÔÆ¥ó|Ø8uAVc÷Á7ıà;|úî†Ç¨Y¸k¹³ß¡•“„¹RÎù¢,k=Õ>’ú”„eÁ›+s\Ï¬á’°İ³fRÂaÔÍÖÈ¬…ÔAg\™f¯t&½4>ùÍàq:Î~N_(­Û²{¶ı¤í™F§Š+YkÆ0?XØ¦Â×ZAë·Ê…Ä3o"^¶Œ˜ò"?µi¨\áè‡®ˆYƒçî˜6XQ¾¡™+|ó8aBHÄX6ç	ƒ±´a»8¢¸3ãL:›0LsToÌ’Ú%Ì©PÚn r)|B½Òø¤@EøR±ª@.¾Tá4|ÖãŒ¡µàÛE•‘¼mOoŞy`R¦A‹RrO9Ğ›vÚ:İòªÁtÀÁp*A&¾0ŠJOo\¡x+g.ˆÙÄJÒˆ¦*KÂ³ø«Ã×˜©[S0PaÛ„K¯EkhÁ¤
Wš‹e+s˜ÈáyU€b‚@#.‡át+W‡ÇD\TJQ €ĞÕn ³%ò]ÔzÕpøŠXA.Ní¥¶C-+D0ÓMMµrH:‰‚Ú~–í%E´´;eĞn—uå‹ñ•‚ûórp>[½%íx_ı‚›ÊfKÃ×µ}Ç‚Ëó´ï;:øq~÷`z@/ªã=Ö“_n2’õ1Öoˆ»rGåÔª
½Ÿuı/o)®otş¦Ö“¦$)N[Yù_=ÔÖì!K5ò›î!çØÎ‘´± 0pš&¶CL‹fĞBhí¦ıu¡b}h‡ØÚ!Ú‡vˆõ¡bch‡hÚ,‡v.6HB†òu,J-$!í‘X¥PFbšÂ‰~¯$L*R!áT‘‰»ˆœI„–¢©ÂÒ‡Ù¹p$öÖƒ(3b¤Œ1mÙ9<ƒÚEvˆu‘BÚ™.²C´ì½XÙÙ!ØGv€e².²‹_Q#`CdGÚi‹õ‘]¡»±ÔÂacÓ¬ìŠÄšNRdÛô¦¤…¦×Eeù¢ÃƒÈ_e|°r=î.\¯\_2¼l¬=>Pñú³°ïÏne;À‹‡¤sáRÓsÄúé9b;>\bîƒj}8`ø6Ù¦g ¦xïÂ\8`ƒÌÀÁƒ#V<¸4½Ï_’k¡®¦4G]R¦‹º®L?ur…Qê³D¨ÓÌ’£îµÊ˜:â¬MÕ•>.åàÀ¸”ãÌÜI1úo)Â[®[ŞÄÎÔÑÁÖ;p€F.ÅèÀ¥È
½_Q£¯í4f%énÌTìLÍ‹,Ã£/Âmú’xR–/:<rà²¼rvê*§sÁ©WšíI.Ş¾8ŸT.Ÿ´Z>Š´>m]¾¯ty“m¾õwİŞÔQˆß«t9}c}&}âÆ½û¯ëQàFÂÛŸ›ëz„ãå6z1  {É-¹¬0pdÚÑ«^ S›”é]êùR¼²lãñ½çåò˜BÇËcÊ53£÷ôT”^ÓSÑzÉMm§^‡C)ªçTÚë;•Ç+×T´Jî{‹†W¹{rA’_ùNo(¼¾½ŸĞøyr?`ñôä~ŠÑûy*Jïç©hUEm§*RTÕ[H¯VP9Ü³¢ñz…ïÏLVQáT½Şˆ¢~Eé•K[øèÍk¼t©\ï˜º¥WóˆxG¯æ8¬ã=NäfŠÑ‹y*Jïå!åËµ6¤rNCP¹*‡^®Ô!,–Ëwª0è•<UpôJ@Ã+Üé+ê¯z§Wò Ş	ß^É£¤o§Wò ^2/É•<k¯ä©(½’‡”Ïª Í5íÒ©Ådw¬è®+yN\râ:WÎ—×§7ÀÆ—Ô³’7o_+¯S~NÿæäkL N·œ\¥2ùE¡¼bá¢–”Ø’¯ŸYº¦{6İüÕçÛS,k’ÂÃ¿œ•ïãätÇ6§ã%-UçrÚ=/{bíE¶Zæ×õs ­¡«¦/W1«,ïÍMw[pÖZµœæäÏÕ*‚%t–,-gÉ³éµ¶:[tº![{ÀHùeà¹®lqXş™X§¯åyy}Éu*Ÿ®Ğ…§#ñZïÒ‹m«¸NŠW—K*¾°ò¸#Ş½NX¦´tÜÇ–õÜ™ƒj\E¾…!‹'\‹„ß&éqGÌ-ÅÁ˜Üæ‘(ÑÁ›xÙÍ9QZzÍÒÊO±Tâ÷ö}èáæ®t%çù}ø¯ş«ˆé”XÁx=õ__ï°ŠQí´ï:ë§$+÷¬êô{ñ{ÍsG<µÅKïç'%%Ü‡ S{¡ÌÿµD©
endstream
endobj
85 0 obj
<</Filter /FlateDecode
/Length 3594>> stream
xœí\Ûn$·}Ÿ¯èç KóÎ"Xi%?'XÇ­;ÿ¤ªšd{Fši²¯´Ö®ú›¬‹,ÊÆ‡Ê_‹Å?ïŒz„èLuµÂòñÓá÷}î#Ø%$[—?şuøç_–ßÆelZÖæ'|Ñ-ôç?.ëüzøáÇ°üú_î¯Ô°8ç=u÷#–š®?`Ó›‡Ã÷q©ËÃ/ØKè–PLçÓâÃòğéğWkCúÛòğŸCÆÏ~^ğ°â(”Ë <İ‡s„¤õ•:€¸vz÷pZğä’ñŠ’Ü•í ~3ˆÛJ~Üb«½[à‰O	êÁ-€n2æíÛïŸ*oÛ°w+¿}^˜`½æÈ`7ıí¿ãŸßÎe“é+.®$c-ÆÊâ}Â¸õhÿŒ=IìCqD­?©—ß9—«?ÆªkqljÁ¾ôßøŞ1ˆ}xkÆ3Î¨åS{ÈİòH‘æ!0bQ*X¨A1¸†…ÈX®Öv6Ôå#½®¸Ìı¥jJ †µ’-V$â(Şát÷>t£_uøYno¾“©]	ıÔ0pˆyccğP–èeBÕTzK—Z¢ğ±@Ç(úû¹–ñôHO&¥1!9‘ZÒ%a5å\¦Ásã³¯Q‰IX
ø¥Ô!¬äR²V;×Š±â]Tö!Ì1"!ÁÖ\'kCN^ù…1ô_Tş#¬{x}«;ÿñ Ú‚Fğ‹ê—±Üúm0Vc—`•AôjZ6…KÁiÍ+97»51ÚmÔl‰˜7®dmuÆ‚mşëşa4®îiN\!î°¿F/ù0*@FsH½Wqjx›CP	á¡
u¥¹Ì‰a"5s†)ÕS6W³qxGÍÚáE5Ç?şMô Ëú±Bÿ™	…ŒòF
o¤ğF
ß)ütAÎĞòÖCòq°D‰6Ï,HÚ²c–`ìˆ%3K0²a	Æ¼/M ğ%¯i‚1p³ÓC?Ï4Áè†&VŒi¢ıØh¢=M4Ñ0†½K°2¸í.¦]=YDo=­º…ÔìkfÔ³Tì­çs÷Œ÷İƒÈÇÂäş™'1hÛ‰'Ë1MVS˜y"ùtÄ„%TS«NØ1Oºå‰äóOvÌ„Æ'¢`l=¢Xf¢èÍu(õnuĞ‰ :<»¨*Š»F:ÜEw5/º‘ôìéÆÔóL¬®gd÷¹İj_”>¼Ã1¼Ã÷C/N!À£Pƒ)ØS¤R˜‚°-SvÌ©À†)Ù2a›båˆ(ÛaGF·DÁØJë(Ö§™(VlŠÃÖå±cğ)¶›˜ÓhêL³¥«=M«f=ûV#N³tX{šÏÍ/Ó¼oşÌ Vx‚?ñ![`lÃŒmyÁ¼å	Æ6<ÁØO Z4GĞ3v¬ÎJ0S£ŠX±NüÔ)¢=L1š« İªpS¨Àì’Jø².*Ä•Æ2†iÔŒ&TsKÙZÍÂá5[‡÷ÔÜ¾$mx#ƒ72x#ƒ?9ütY©dùí€5¾:”Ø¹@çÔò“‚ß…šäâ*Z²Ã‘`th¥”ŠÀj&Õï¢µÆæŒmñÑ8_b¿Å¥»ãao’Íè8‚K%Œ#!ˆıG– ƒìSª+&£”‰R9Õ‚4mÒƒ!XwèÚI0Pt´÷¤‚C‚u'°›†;h°2äã£  ñd0qïr©J0ÑG¥8¿*Ü”@‡«%²M]1ÈmÉÜA3MÁ±É»!L®ìFW]ˆ{Ô`âÊI0q»RBD©{2Æ(\) ½¥Âræm(ğ»PÜÀ	¦ASEÅig®RT
üÄëX6Õyä5æ¼çÅÃ";Ñ¼zÀâÊ@ó§jò@Må‹‚Ç…\ã/×Sü$°qêÂ£ˆ	m4æQÄè)ş&¹<-ÉùI¤îˆh´¶,Ú2ÜAƒ•ÒÂ` R¸Ë`¿ŒMÙkÁó€f÷Û”@ãù„–Û®.‚Á3¿tÓ(ø3Œø0
6Œ®»èŞÑcGÎr§kt0mOEX¿K*Å†
Öë_Ä×”nÍˆlÀ¸ŞM,§Šw¤•Ú¦ÒJŞé=ÕÈ­uvı—S²6Şâ¿¸äDXñşîñÛ¯Ÿ¡KlŒ­}\?¥aEÚQñn}¥ÜÚØµc¤Úø½
?4YîÛ8±õéÏÛû•ïéNÀ±R†nRhC}i5,òaksF‘Û†­Mè,†`e²(ÆïßŠ!¹ÏÛÕ˜Ã€YGŸsuŸ“´Ø±0úØçŒ0+,¸ÌæÙgÎ*7=.û&snc„E‡}¦å÷ºú·sŒk“ö˜>÷ÎíÑãÎRf4k¾ÇR@nıeßl©ßùº¾Ï`ÂE%¯óYÌ´Ó¬!h¢¼», _M”{I1¨ÀÍŠ¼w‘ç9óá‚Õ‚R¬±Óz¸b¾búîa©¯†1ÏYwv-•Qv±¸Wq?M|yÁ’¢Í³ËœÕ¾å¢fÚgVJÚ›YãœQ²—;A‹ªòÿ#ÊØ£³¿×û|anú\?¿ JÅ<;Í‰;2É#w©t+æŒ÷M¥ÆtÔ&)v¦ºSë6Ï²2Ë”Ğß¯Ï1?İßy&=gÒ†Âl¢}&å5<z-.|r¡9£CÈÁğ"¬õØ¥wÎo„wğÄL;Í
IŞÌ¿NÂƒËö/ÁÆ×¤Šßáií2©
ÂÓz|–_Ç0À/&ƒ‹‰	Ös¶#p{Ô–¶xKÒÃøE¢(eµPŸÃdI¶bUs­_¸'>£ä
S4ë(Ñ‚Fww3—°WZ°õ#=¦õîÍ}PÙ¸‰+ØÓtŠU^dõ¹²“GK]ÙAñåœXÜc¨ÓİXÈª²ƒ`08ÃŠ×å ªm Ú¦Ê™ÅdÇ§ÃRd p•A$Ô•ëÊ‚UQDS-˜*¶ˆª,#êN +Xù8ÃÙ”’×•Lgì–Êƒ"W.ÕÄõŞœhnSõ\TÍÀu’¢‹:ƒ¹¦3Ğ©¤3ŞWnã(Š@Ê×Cr¢âÉ¸:QÍÉÉ SpĞÅ1{ "mMªšƒ ¦©ú©èæ”‡Vcíõ‚€[üR)4¤®€3Â o08jêb‚u1Gw!uKJ&“TR^QH!Fé*E› *c
+NµœL—éë¦–“S4`7µlcrè÷-‡9Ñõƒ®åäT“«®å4p[Ëxªå¨.†oÔXâÆI.q¹ÒA‡ÒĞöT|}ÁZR}[`üû¶4«D±ïÂC?({ß„²c	v	—`/Ã2Î¾ôc®Ëu§•©MòµEˆåîÛ¢tV¾‚öwtSF·S¼Ò·¡åÆœÈåfÂ¶N"¶D’EäõòñÊe»ÕXû.ÏWe=˜Sÿ!Z?W¹µãH”S•|m~±öx\O÷’WW×ã-æ·“q¥Q³ó·«¹øà±e<İL#om»œ‘iiLgYµeO=»jŸ÷óxúy›¥\W6sfEØíë³ª€«7—­ç¤
-Í9àV¹²ê”
".×¦“Ac‡9¡‚MX¯WŒb0tcL§S›²©NÉÔ@U&2ÆQ)‹’H%7Cv•5Ö­¡Ó(±ÜãŒâ:”@_A,`"ÇW»Dˆ¡‡’ƒ)‹B3¶‚6Ã0Î*‹êØœE	ª³(y_|!ãˆ×´Dâ_‘]â@t<GÇIT¨9õSK´S(ÌkMt ïÃ fq¡ë•²òB
”)º¢çü	úàjÙØ”=tJä}É;dIQ´@’Íˆè’öˆŠ’!cè¼I§Ó&D±wº®(ã„Z8Ø¼’1ôNveÊ™Æ¶\®éˆUÆÔ1˜&Au¾¤Şï®PÃŸMï*ÑuÄtODÑ‹2¥”0›3	·øw¬¼:l±}ÙR–f/ª£¸±-ÉPfRß³vg©ğeé#õ5úNà¢.ğ¶­ùû†õûx{’Å§Òf^Øó…µÇ<Šk{¶K iæíSí"…»‘ÿ-ÓóÓšyÜÅPş&Qi©ı²ç%$Ã—\ÇÓJ½éÒÍ-—h«—×Ôt¶\J×’^®«!nÏxÒİ«TÌ¯í×EË½Üñ\¿EªwúARŞ‡9nï®ÏäOL—é|¾o…8±¿‚Wİ_Œ½R.,J–Qq·
ÚNCşæå,ÁÓ§ G1]LÍĞùpGM*^X$,'ŠkW‰ ©.å^~¢ZÃ˜Ş»´=Ä©å#¶½Îé“ä+Då´ı, \X,+£ô9"gw¤PVæCd®)¬àD5æ‘~› œ”Å¯Qqy‚gäŠÍk""¦v` 'J4Ï*ıçdm —2‰ˆ¼SÅì¾9óeË-€ıæT„Ë1¡ÖoNÅzÙª^İñy"«¡\“ÈZşT»¤//lÆéV._w7¨3òçnŒ‹£müx#®ÖG‰Óm^Š¯‘BßCPÆÜçÔ”¿`Ü’¡÷Ç.ÿîâº‹Ø;Õ,Ç‹öUb·ÆmìŞÍ›À~bÜhTõ‹±ãoí{üŒºKOêeN¡„…~t1¹o±çeÜÛö½úû
1˜ë(©!ºI‹ í’W©§ËPZM¸k{±r×šîÃ¹8·©OIÄÓlØŞ¿)œÅrÈ4ºKÊtœvPMäãx‡
endstream
endobj
87 0 obj
<</Filter /FlateDecode
/Length 5414>> stream
xœí]Û9r}ï¯¨g“Ëû0L«¥}¶W€?`ì]ÃĞ,°ëÿÁë!™ìªR—4LkvF•'“dÜF2r¥cúsôÏO\#(c—_~}úÇßW&ˆ‹¶"^şùßOÿù/—¿néèQŸ{¯¨¡¼ğ?ÿñçKşñÏ¿=ıéÏúò·ÿKıù¨/R*Åİı5!‚Í?èÑçÏOúd.ñòù¯ÔQ¢P^´?|Ê^”¾|şõé_…Ğöß.Ÿÿ÷ÉÑıÏÿu!@…03àà EÂ¾) `s“Ø “;ıøùœp+í¡dğ@¹ôó jDÎ”¯OÌÜK=›'v„ª /\htsëç×[“R{k¡grgúÅëÄh¡˜E`˜§şñ$¥;ÿ1éí!ÙÊE)Kv«Hşzê¶«¶#(ÿ‚Æ?I‚ Xúëf¬ÈğC”Åè©/ü/µ[AêC‰Ã^tPÎ^~-ŞÒûÂ†ça`ÄG¢*\ø§–Ó&a.
Õ:^~áÖAzéR>^óƒ1²,2bIEÒtWJWŒ¬’šJºçJKOm?çµ'=,HêNÂhbÁ\ÜXQÑúú$‘ËOñÆ‡Š±õ×Ÿ¿<¹èÛÕ¾:´–¦?Ìˆ³ÌVï’±hóÃà.NEd2f5ıvóÎ{‡l»H²Jc2¨Ğ…ÈˆÑÅAÚŒí¬½$Œôg@ŒUçVUù_àyFíúM˜3)HX´•úL)îP67.%Ì*œ'Ì;WäVdDh~ªÈ‘¯©cx‚ˆ‚¬ºªš„m. ÀŒEwI*NW¬p¥ÛÅ—'0ö8QëÌ Ã¬”vóM¼€‰Ç}.4ÑÀŒi"„¹²†YØ´³µiæö/OÿÃn!\òÿØÔßÉ‘’È“¼;ƒwgğîşÎà/wÄ%Î(=8âºz‡ ½!òàèébL3pÀØâ£wHÈä6y‡ m¤6½CÂ‚tƒº[¼CB'ï±äÊÏâÊÕà
†&X»Dcíƒ£UW2Ñò+;8GÛ8™ª|`Î!âÜìÒÆY\õ‚³½ê¯úÖp÷¬üÑ;BBPƒw`Ì¯S)`lñd,…Á;0fµ8glõŒVUYº(gÁĞê!=DÂš‡à«æ!òÅè!êãhHµ[4¹N g¡L¸òƒ¦Ş9‡9QE„3§ŠçX—9ÎÆªœµU‹0Çï
ŞÂ»Sxw
§ğÕ¡C4Át/â´±!,‹„M‹„­^‚şº	†İDÙ16»‰–EÂ¦EÂV7Áèì&–İDşYİD¾İDÆĞk—h±}p4íJ&NÊN–Æ6Îª*˜|UŠ8K»¼q>WÍà¼¯¬uÜüDRÿà'™·	›¶	›ıvŞZ$lÚZ$lñ	üaîŞ¡Ø¦…EB'G‘±ê(ÒUuåbpíq0¥Ö- æÙHíVÜ8kŞû´hB‚ÙÓ„	ó¤3²éfnÓ#Ìó{Â‡wÇğîŞÃÈ1üå¾W%—¿?‘j%QìÛƒ¿ú“Ôœü ª9­¸I8iÂğ;F£!£Ãk
°éúŠş0êtJ‘Hâ[EA4Ã$9ë"?ì¨™õ¶ Áñ€’æ†5…Œ†²3ˆæğQúgmGR;k	qByz
;ŒHh<”¤Hq OiAb&x!”Bz“l|h•Rê£à]¦_Ô‘]iŞ·µÑ<g(…ãíX#Ì{š¤ÊK•Y.Lø@c<MİÎ.@ly~ÿØDS0›…^ÙQÖfzoßÕÓÇéšDŠºÖ;íİ>:gÆ¶ÊÖ§¿Uv|ÏŠf}%¹Ñ¬oÄ5i#o_©× cÒ˜±‡‘–W á(•MÖgü¡ŒSI‚üÏ+†É‘ÏâmÍU«‚*(ùrÁIEİ­/£Åú\lÖ×p¶>O%3ö¢¼9,	jQ‘|ŒÊÖ‡ä)–¥•jdF‘Ü%;ñ‚úAL©‚w¡~yê}J‰ ÇÛ—6š·æÂ)”yKND»ÒeaÂ[^Á¼Iv=mŸuPÉúªh
–tİÙQ"¨	ÚWíÀ0M‘HOÓ9¶Ô<±¯j{÷¼#>,ùŒ¹d"ˆX‰)ìš±¾-Ko»Ùšá}·á[WßŸ;~C.„UBK¿Ğßèo›1ú+İ7´S¥6&”ß¾´ı8>Ïíùù¥]ùmb¹Ïã}*mc[Àsµ_[î¹<&ÿN}ê>n¢ƒïKSdZëıÚO·<#ï¡ĞKnÄã|ZNlä*…åZhi|È7ÈGL<ûÒO(ôËŒ§ö/]G[İÕ~^@ş¡ÏòHôÌrå–°J[í÷eVÚÿ	K:¸"OgÉ!E}±Ş¦eÊóİ›Ú=«¯N"Â*†t/äûÕ,ÓıOãıU•7ÑA^c¤Ã¸.F¡û‹h_™.u
\So¥ÛşıøI½ú„_˜v‰Ûùn}Êëæ7Ğ¹5±›äHöv}˜ùşĞeÜãÏÅUØÂ™j‰·›è"fºªûª}#-0•íËè6WXäWuRyKna–ùì.C§cë.ƒ¦tÕÑà†p~©vĞúöŸçÉÖåÜ&W
=Öe-ÑQúEûm4ƒ{4h³/óhìƒîüŞ+ñú;"õLáJŸ’´¹“¼»È¼É-)ÊóMô•Ì}j6U©Ùå0o˜JJÑDqºIé¤ÓƒqÌĞs´)ö¼
†‘BÁ¯-Dì6­¤xö´6ô3—V—NSD+ú)¿b^§é@»„Ş ŸML+‘ræ†1ó¤½‰ÊËŞÀ”Vs¡7ZÍËù¦2'	ÎõÓ¡õ$äAû#’~a']ƒíæã†‡”l9MI;åµ½>‚-'IÚºèõbÚ(bË\ÜŒ°SĞVm%?| ıÃáE‡aâØ1,`óv™`É|uu
ª¬3ìÏ«ÎkË¸Æ³ß’/'A2ò)\ú÷çì0Üäû5^áß·„âì@ÒÚñá«fıã¡=WŞ9I ÉX•¤@İÂLæ#\pá!ĞQk!-@ i›zpC‚‡`u˜¨¢‚üòiØ³ bv`Lî ÜÓ"0XÏ „õd0Ñ³2Àî VÑ`^§ËñËˆÊ”ô€¼a¼_O›øJıÇpeHëhS¾Ò:„ñ%ï ­S±0¤u:ŠiŞ¾+¥ÓõuMwÊ»ItÏljÍê(Q,sÈêHî¹ÚÛ b‡| ätH^áĞDº†L $!¡Kµä5‡óZB>‡02€”ïêY 1›0&s°‹–±Z¾d¤ª¥Vƒ–ƒA^[ºä‚Yœ.DÌâê9Ëá!‹CXälˆªH<’]?dqÔœ_±Å!Ì¤ädq:†YœbÚWÀ0MwHOÓ2¶S<±§ß8‹£ãœÅ1^Û[\{Z>p’ºm˜¶Huë˜ú{YÃûómíBd^aFÖn
‘´o‘™%%v»†Æa“J:J¥DÃõ+Ñ?„ĞT^]—HïPH½‘¥¦¹iÓ–Ú—…=-ä¬Õçü·°Ğœ•ä¹Wìi³¯”œÕd.ï›&É™GQoİõ×¶E4[`c2Whv›¹jsßóV?`xĞy³iS¡dÊÓu2YAª¦T?‰!¥+Ë,Ó5o"DÏ£<J©šSòFg¥v²®)U;İ|4»MI^ı.”ÔÈdÉëO¢å¤{÷ç<4CxııGñKS\'õjş‡–ñ¦¸Şì6ÅEy×ó$¯%ÓI¹‘tµ¦nH^í×„9ó6gÇ?¼@X‚»Ïof(“÷¥Ñ·	ÂÀßIÑI½d<ÿƒ`ïÑAÆ(9öÆ2`ˆ{‚hv›¹†ûbh'ŞC—õ«“ùC@Ö=A†»óÕ¦k¯6l%52ø H½'È€f·)ÎÜM:÷ˆhò!AF'å7yé£äš-÷ª.İå+2"NµWùC’3K1Z©{ßî¸9'6½+áwuüÀÂû›zØÃkùìÙôÂZ*|ŸPDÅî[Ä ü×7(o­NÈİuµo±§*¿şàDš“ÑÆpçÛ&¶}¨ÄğIbïø@	Gúô‹ËH*]aÌDUŸ:,"aÁ{kæ-'Úgó·a”ô#?é„$¸`Š%ÌHòB²`FæÆJ9—Îm3hcjL¾†®æiVxgµ†O´JÓ‡˜/h4–Ÿ¤€S›#¶LîŠOÎ>wh|Ğx› Ã^»§å8=bˆÄRFâ÷ZËˆØÃëƒX%c ÅZ‰2áC¾š_Àìì!­RFR¦9l…/œ}XTX¹HÏ¦Ÿ©ğllGË@Æ`A”ø<B§…+ŞB¢¥ÓL˜÷#o\VTnÜ¥Àçõ¢½Ò"LMbµü–1d4ùHÒeP“Eƒ6f¥w§[`µ9šK«„öWéFCí¢IQ åW‰s¤Év˜MEÃ¬ËÊŠM‡\ÅQ_­OÇ¯’—u58)…X31ZoSıCyŸJhôxÃ·áİ°ğò÷¹¼-QGöã“Ãæ×D¯¹Lï~ilm£³³/ãXJS_0B,CA#@OÅcqI?YB ïşRº²FÆ¨ÔìüôÁ‡6¢¼aìU´Ãr¸´l¸Ûıasc;v]
×Õ«N2÷¤¾¿Ô—á¬#D…ò<ÍÊˆoî›VM 	Šp½Å^R;ş^a£Z!íái)ZÖúÕtìÆ:äMœ\$EÆætäBéd‡?ÉÊÅŒj?î×l8Ÿ»©±}~KÒ–	” “§´RÌ‰‡lPPÄáùAƒ2ÊÀH­¤o¿œÉFğÔÇÏ•¿(ãÉ‰–…¦·¹¯ˆHĞ}!±ƒÒô8W’‰ş:¹ƒñ·ŒQBÚuf¡·PŒÖº)zÅ³j\eÊ%EÃzÌÁ‡±†e‹°%#Œ.æP,ğ›à0†b„y£Æµ5˜³PŒë”LC±`Ë"ì†;„`µ5Æ
}**E|TÊ1Lé<b<S¥qO•FH]¾KEXTT¹h!XPKFĞ‚ñY	=G`A®aLÉÈ›<Á]B°TÄ3‰U„`.!XU{rÁÒ-T¾\C°>Î`Pr	Á*İƒ…Ê³¬Êb°y¹Æ`M¸Ã,RkV”›¯…`¡çœwÁË6ª¹7¹Õ\Y†Pkì—ımWßcÅ%hJëyÁ@6o7ø–pîë£¶uŒ³ß-ûı½I2¼ ì´NlM‹ có~œ1ïÔ´
á–U€1Ş•àcl]WÆæU€±§78FçU Ğrm|ù1®éV÷B­5¸+üZ£ü_£<%ğ>µI|o“8i/¸ó¦	‹ª*uÂÌË C&o¦a³.œz›—Ææe€±u`TÓŞh—ærÂI°z]œ×Âªşô´ä[¨~½¬0Î`R…¢Áô
åƒ‘ê“… Ic0{½,]¼ÃL*zfœiAÖâ•… ˆø#,[ï½Û‰lëİ[‘İ^ü]Q¾›[_r÷^¼¼û¡ –Fâzşc/ó»õ½—àNN»ôÎ¾§ßSöêFÃ¹i÷7Xn=o2ô¹^qÛ»ßs?p?|¾İß°ÔyGwKCÔª“y¾Zõay%s²AßÎ¤]‹ëYM`Í¼ô…´êâR´f^¶y‘=U[{Ş'„v²gd£Ø-í-r^)6›"bå×ˆ˜°%"Vş,"VaˆUX#bÎ"bB—ˆX…5"æw´kD¬ÂòŠ*aõUPqŠëmˆËj/Àõñ0Ô«”aHX9Àà±óŠaf•
†£Uz·v9c„[5bQeå¢EÆÊ-‘±rkd¬ÜId¬ì+;¿¢bˆÛL±²K~„15‹5Q1ÅÅÊ®q±²Uƒv‹Ó-4»ÆÅ}œÁ°ìœit–Ú8lÚÎ¯¨šÄ†IâN¢âªƒaÖ¹'^‹Šu=ºiì½ÑÓÎñnWƒİ*+EYd £ÇW÷FË?d4ywè»&·C£÷æ#§_ÁïáÛ÷lÛw]%írSTpÓvjßb›WÛ¦è®Fä7¿ËÛ¿N»[TßÛĞo
~Û¡¨Ç”ô†v`óa%½a¬
Z>õ!ûÁºöyøLÄ#ËxI¥ÔËxYX*ªx	Me­Šx	Kõ¯ø‘6ÂR©¬Jx	ÍUµPÁKX.¿…ŞaınG±|·£PıÚÆ2Y 
jíPxÛx°",Üí’û2¢î"àÙ£E8ŠØò@"*wÉöÅ!~-AN§’Ï*ŒŠ…»ÅÂİŞ¾«¢Óu†ôtívÊ»tÏ¬h-Ü5¶|©k(ÜUŞêjaškY¡lWy“‹^±ò“®õX´KàR´KX®¸…šİaÉnG±bÚ÷Š×>N/E‚zm'½Ûv{YnëvÁa±®±Né_Çğs2V("ÌQ|(Çj]BiA(Ä…GÂó¨¡Z·bcµnG±ZÚWUÀ0MgAM»@:XLcñÄŠ~ãrİØO»¶ĞğFãÂŸ¥…¥®33v¥ö&¶“Åí+OP£ÑÏb¾á¼4¹òl©h&Â9æ~&9-<¥X¸,áû³ÅÒrM¿–KWÚenO#?DŠí[Q¦œ­.yÆ·I¦Eg5¬ufGúšI9aŸBî}÷¤úô|’½÷Ÿbü$SUQıÊ_ùº_	Š™Ò’fM	'}õ}÷tH/FŸç¡ğÔù[ê·¸Ì cN¾\1>ĞîË÷äÎñŠmPà%Àæû¿²¿®B©ª/ÕQ…2>@~2}Fydé|—xqº×>)æ‡š‘·ÚâÌ¹zˆ“æãù“Çj”oû@áÖF·Ÿ)ˆ‡©$kâM†tòå¯8¯(úÂ¾‘ó‚!¾‰ó‚şñ»€ÆƒÆÇ9+íøKRnæ¬Ô+ÖzÆú	Œ‡ø-í‘şßYqÄën‹_GûT‡sª‚W­Âúïå¶ÚHßÚm,½µdM“…‰‰T³¶µÂ2ö#êĞ`QšY+ú|İw.J´xmèö&£ñkÕè*Ä£ˆÃ§q& şó‡
endstream
endobj
89 0 obj
<</Filter /FlateDecode
/Length 4271>> stream
xœí\Én$Ç½ó+êl`J¹/€a€³élk ÀØ’apHşÀ¹ÅËl’]İÓ¤âŒ8êz]™ë«\¢¸›ËŸMÑßw;\&§÷¬sNÛ×ow¿İñ÷Æ%µY¯òöû¿ïşù—íWÂİ®İkó5ÔÿıÇ[ığû/w?üh·_şWú‹ÙnZÃİı\Å·Ötëû/w?|v[Ş¾üL	õfã“6~3vûòíî¯JYÿ·íËï}ÿå_&­€[X€8 «
îCëØøÚ$ÀÕN?}y\p¯ıntŠ ¹ë fD¯’ŸŞ±j¯í
<qÇS‚š¤·Dn2†µõ‡ç[“S¥µ²«¸«üêya¬2(Ì‰ÁŞ÷Ö§¿¿İiöÀÜ¦£ß•¢XÙŒñ·†ì¨'‰]»sñ@õ4~Ga©tÚ£3çÃØPà§¬[ï9R_ø/µ;©£v¿Ùì’Û¾µ‹”²ÚøÂq&FR&©ÒÆ7ë¬n˜uY™qŸ²yûÊ­“:”ş)aß™3£B¾4šòİÛ1
Kj«é»ĞšFjcø¾h#9ªaI[2é®œ5)7,¤ÄI•}ìw’¼|'Iïbê‡ÿøõ.ä8®øj·V;¹™‘àY/é’±ìCˆÓà!“
Ádb2æ-ıu‹!Æ€j‡LÆSF;°c:™VdÈªòdoFŞ€g
FtàAÆºk«îş‡;¸Ÿ‘l»A¿Î£Ë¾‹_E%hÆ×ÆM£‚yQõ‚Åšáš‘
šsØÀ˜„…]Ç€f/˜UÍİAuÅLÃ+=övÜÊØqñp!2n‡PİBĞ CT‰â¡D;è.i1ŒÙ3Œ	yV‡ŒşÌ~„<ÿz÷¦ˆ´Õÿ˜úçB*ä.b•7bx#†7bøÓÃOÌÚü£ôàh”Sdï¦ ¡8Î2EÁ¬s“Œ0¡ã@qAO¦cl!
ÂNˆ¢`Q,# w]ˆ¢b…(ÚÇFíj"Š†aö.1bepŒí.&æ@W³e¨iÕíÙ×ŒˆY*ÖÆ|î~Á¼ïşëÌÀî<Q<Q…'*6óDÅ²ËÈ’£g¨ØÌ‹ÁL<QÑ™'ÓOTlå‰ŠÎ<Ñ°ÆõªñD¿@Û%’¤[‰9@¢SDA,I°£î#+ÄH’;bLÉ2´ºä£øGòVüY~ÁâŞháş<´pıôA+Õy‚º³yâ	FÒÂ›y¢b+O0'¨ÈÌ3d% 
Ãi?¹‚°¤òì4ÂV¢¨èLÛÌøºE¿B¢èØˆ­Ë)dÇàSp71§$hêLé2ô«Yó¯šqÊÓaï)£›g¦ÌoÜ0Zu÷ÏLAYÁLLÁXh˜.cËBƒAÍf˜˜‚1oõ¤:cëB£¢+SheN˜‚±S¦`teŠ‚¦à«ÁõbfŠ~;†RïƒNÀğì¢Bw0ÜEwÈ‹n$ÌnLÌ3±:fd÷fn÷#äùEˆ7bx#†7bøóÃÕSˆDc	Sh£¦Ğzİ«¬Ø¼WY±S¦Ğ:-LÁÈÊŒÍKÆÖ¥FÅæ¥FÅÖ­ÊŠ®DQ°Jõc'Šz5EÅ¦8ÔëRŸb[¯KQgÊ}²Ôû`öé´ò„X{Êg½îTŠÿ3XjçO<ÁÈºÔ(Ø²Ô(ØºÔ Ğ­K‚-K‚ğDA Ì¯<Q°(¨³Hê4Q®:M´‹‰&ÆíH½Wˆ8bs*!<ôPÍ%'†‰ s†)!ÇÀæÃ;µÃ‹ã—LŞHáŞHáOB
?]V±ızGİMÖ$±¶èùÎo ¿s‰f»Ù”¬;†3WÒÌJ'3kC£èvmèƒ\Ä¤=E'²­3ÿÛ][ÍåG‰fãÚG_ÁèLé€ÇU	XCa³Ç¬#ÂìæLsötA '¥ò8,8Mş'ÁŒ¥ÉÙ{R‚@MqQêN`7Mé Á`È‡	4B²¼Tƒ¨9îcÁ$icÔ¦*Ü” Øí6GW4kêXüJÍ4$	Øäİ ³+»Ñ¡q&®œ·ƒ  î£1ÆáÊh×«…ò%u@ß¹`F N0IhFOIP>eö] [V‘§é´œÓÆs "0Cî/‰ÅõD–ã/ò<z%›Ó“øNR$…X@;Âo€ìê«…ß€9ü"qJRnêÂ	=™Ç21ìÎ”èC©L$JôÚL˜˜YY?éÚÀˆv)4¬øp']ÈµÁsğôÁ¤Øğ©i¦­§eIê+ö®ÁäE]¬iK ç•)Ñ×-ÓÁâd±#À$Ø°9vÑ}ƒc7Îr—£JCÛÇâ«ß%ågô£'?96z&¥:íZ1Y’•B:æ17•Ò9>3 Îiµtî×0Ò1‚7ôC~”0î\xWÿá8#½>ót¢§˜çq4E£¸O2R=Ğ®ŸÉÿÊ9úù\ÿï#ãSiàéHFÓ³SóÌiêL³jZµ_t¿ïU›Å`]]EUï¯Q«JÛ}Ü&ÑOhßëÖÆ7Çğç<ÎpPŠ¦İç2œÌ¡.ÔWği7Y2^rDÀ“r­Üóû"À–i‰³iêZ}àŸ3¶¶eëJ›Yªƒ.Šæ¥\Ôsä#—ù¶ö|O\â˜Aˆsr-d®Ÿ¶å°ÖPsÓÜ7Ï³Ø‰±›8‡O”TMîs×ÛÔˆ‘–Ç|“õÉıÌÄ^>¸X­ThmÁV¤ôKlŞûü#}£Ìgû6¹se–4lußßç„H¾\-)£\Ç‘³E¿Kk£hº¯r‰DPş¥Æ»Aß³ÔÇsÌy=cVû‰DCë·‹î§™Íó¬ò¸Îı…ò&>ÂèúG^+¶Ç?4=fêÎ™ú%‰X]´®²¼ãô†;få4â_Z22ï/¼[ã^Œ‰y“áõf­2ÚÏÈœM”äi6u“<çCÆF!§Z;w.
yx"İÁ0—M lÒ&wl™?pN=¹k|J–Œ—q…óƒÌ¡é!«“Ù.±ú‹²sÙ5*©^›!3`¸Cö†i4=fo}:™¹9óêÉ¹%ùûæ¯ûzÍ>åëò]÷sh´Öiîs»÷¾İk?ëíéêã52û®gx»æH`Ù™ÊµjQëwE—„<ú¢oâÖŒ?nqõ¦îæh/’¦27G-o©ºúRjÜ“¡/¬_ø\ß‹Ü“¥Y¡?Ğ ÁúÄ±…é=%úb[Şm½D$ûDïÛĞNÙÉRç»j¯ RWÔÂÈKºmƒ¨lóeZ¬öˆ»"õB†1\ûÂ*ú"iù¢áUÎ1›ó-úÁL_9=¢8­ËIÏøâC‚ĞãÉ+°v7ÖæŠëºÔt»N>'PãÉeM1¨…5ÚKÒô!ã„#úµu.ÏQ=E§[ù§\kú>çp@ÜöbvŞMÒ9Dsdğ'=xyˆ¦î)2Vx"Şø˜â=ˆmRzÜQ¼w|¶E{=ï™5‡“´>Ù5¦kGpíÔ"ÁS’gÏKuÌ†Ó‡Ò<êê)³Ksï’d!ÿÏ¤9%g$uœãqıù¦UNíMñxS{8.Ó+ïo¦ Ç›*zæStá™Xy)À&3oj~©@kÖNÚÊ;EX8•7ÆãM€ádPƒSDNE	8›u'PÎK;>Ì¨Ù­¯´¡³œ(	¤"ŒüåÍ|´I(E\,çP]Ó‚%®;£†çš‚â±¦ âGˆ‰¯Ev	
Ññ±¨:=Ğ$ãøqpåñxáÀ¿¸#{8Ïä	,=©²±xæiÅ§MòÏ3	U<Öp©½§H¦€ãN@<ÏÏ3±9”±äØp’JA9Œ]åàÒÃÙ°ÀbD<Î´<«3\€"CY~¡ƒLa@*ÂÈSAÇé,“PZ4™š¢„ÕSp8ÉìXš2ÅsLhß]ÃçM?ƒè=]ÅG"êªÌ+±§—>ºg—£ß¹Ä„= ‰WúC[dÄ¶hè£÷EÆ‡ºÈ-‹¤¶İPî¿oØÇ¶_ô¹ïµ…U[œ¸~¶ ‹-Öê6>”«NgOz¢‡DĞìĞºÎççOJoè¤1;É¶U_ß°+†ísİ°ê÷ÊÊj°; W¾;ìcsægi³®ˆquÚWÂúıœç(÷ƒ?Q÷œÿ\©*e#
šò_Ğ—íÌûüÎÜíü-#•¤|ER~–íMu/¾‰!fô©_KB·×UİÊ×Êï«gÍñÑšsœ~sï†#±µ†±?Á¨YFïÉFïÎ(I©%!W‡NÌû[±jR#Ã@½³ÄÊ¿C¤0A«cî
—t²l¯äŞ1RÉËûëó²¸Ñ¶{;7÷ök—I\×ÂÃT;ïZ5JW Ù!_Eõü!óí|%#•g¦nöKí™—*Ÿ•´ë×áÌdìú+R0ßzb:]2±fÇœd.;iÎ¿–SÇH%ów$`Û/÷7®ÎÖËìÔÂw7K¾áTÑé"§ºËê yú•œ4F*§Vı–ª3Êˆ=[>ÉraÌPğÙ‚Ÿ®|Ş¬–‚ ŞAhuÌ]é²É,ï¿{e¤’ƒéŠì‘FÆãØÊÏ„\pm>Jvoî^Pï÷B«cî2¯µ–‘Ês°ŸâÖ‡}Nâ‚PáÕkÃ›Q¥”c‚6g½ãİÎ›jvnvÌ=î²)+oõ¾’;ÇH%ûâÁì[Ÿ~îéO¾GökÊç|ËLƒ²gPåPAn«7fÇ|_ky #_ŸJŞŸ²X©µójp¤Úš–ı¡à¡ymZ†[-ãÉ—äŒRoªŸ]É»¸¯æ:æÈ|Ù46ëç«,oçx©$e¸2){²9qòI t>‡ú,Úàºõæ*îÏº—ìÏA³cş³¯µ¬‘FâfX~h¾êÛ5½æ÷_qŠ“dÙëµJÒÑ¦<ÚİlZCóoËT<K¶9Œf Ù1ŸùË¦¹9¾ÖºŒTrÔÌÑæÓußÆÃôuZ&‚]×ÆÜ~Ú\2‚fÇÜ“_kU!#•iªQãˆb<±È­_ö)ê-Í\*P»ÁòáÕ VRB³açï(«0¹V	LeV«ú²çTUaù÷å87<gÏyÏ4óšNäùW	ğ»XQAhyÛ:oxÆŸÇ¿TäQ#€•yÔ`A–ƒQ‹ĞÇÁª‘ëºìPÑUœ f‹©ŒbØíaF}ykË(XÜìùw‚‹@%ü&ö\EÁ_ÓêÜcwÓµ‡-¶TQtª¢íÁcğ™Î’C‹¡GŠ(L+˜Š(h–z|M¨'ml†
ÂìnIp<„×üË)•X@aËoÒˆ(lùÕ<8ÿË'Åê	h/Å2”) @RĞ ¢Káƒ¨(%ÃSáÄ0ÜT8a¢æ7£#N˜h¹–Ù¡D†À¦¥nÂD¦‘`CEî¦ÆØT71Ğ©nBÚOÈ0â2G|+‚C¼‰¡ë^ü>Vú}¶t‚òˆJ*¨û|+¨—gõX¬µJìúüGúş?ş³o
endstream
endobj
91 0 obj
<</Filter /FlateDecode
/Length 2925>> stream
xœí\YÜ¸~ï_¡ç «å} A€9<ûœd€ü '»A0°›ÿ¤ªx%±¥v«b{ÛU“¬ëc¤¼³Ò‘~M~ÿ0³Ç`äeŒaúüåòë¿W&ˆI[§ßşqùÛ¦İÌÒÁPŸVèŸ`¢œğ÷_~šÒ¿ırùñ'=ıòZÏG=I©.÷3QM?ÀĞç÷ËofŠÓûÏ°I('íg¤²“ÒÓû—Ë…ĞöOÓû¿.¾ÿû–³$x"øJĞ‚a¼†”DĞ•`Ó”X	&-úé}[p+í¬dğLré—LÔ‚‰\J¾±Ô^ê%a0b$¨
r
`à‘Œ;³Á©m¶ĞKq—ò‹ëËi¡®
ó\fÿ~ÿz‘ÒÍ™Iz;X™”²€[öw°RÃ®GÈ(ıÄ&ÿ ÏJ›Y;¿cÀQfÏÑÃZüO˜·&ÂJÌfj£§/ùì#¦|0¸Rd©Â„Œ•™¦Ñ\ª:NŸqv^:ZO†Ùk#Ú"QŒ«HØîJéBTÂT	ß¹<ÓÃ…ã¼öà§L–S³0Z…˜i.œ¬@¨h}	ââHŞøPhˆşòãç‹‹¾>}àÓ¬µ4m0RœEµÚ’H‹Ö9ß1wTp*&&Ò¬†_L¤yç½ãj»¶Jf¤É B3"R´ˆ.vÖFªÑÎ*æ¢ÿóÒŠ‡Ó¬âü”L;±u‰æŒå-š"A’ˆfV6MÎ
Í*Ï5'šw.Û-Ûˆ¨1º‰Ùhv–Şq«M‹ì¿â¢šäìÄD¢Ë4œ¤t}ø¸0€ÔáHeU†8Æa³
Ú \õaPgš·=QMÄvN5%ÛcÌæl7Vï°][½ÈöøçË?1<„)ı‡Q¡üLœå{Pø¾…ÿ« ğ×ÛŠ¨]À±³Š$a "¶"@´hTi@>à$G…«ê0G‚Ã F!=ØR{§€¼‚_@tP¬Õ’LkÀ_j´BóÉàÀ,ÊY$ê@Ìd Ü’ 1D°o”“ÑËÑÍİÃÈ@Ä=),gÄò@çÑ	¦´ ë¬¸@” bVÕeÄfZ “›?Ôˆ0™+ ÁlR!Ú%å’²Y¤BeiHş¬i¢yK´l”BdëbÁFEc·ùÍ+Os —¨ùºÉŞ@ÑtÜBâ§öv.}'UF\£"gò %ªF…½5zP  ƒŒmršƒ
m AWgµ£„! "áÂ=q‚‰!Ê¨ ø¶º ­ÒĞö.f U*âÌCì¢ßVv7X…±QŞÍF!È¸8ÊCÜ³RqÁü(1œ03Í3SĞìLmfû¸´ùH‘ÒüÌibY“i0EÛ´f¨¯Ì*"MÎT,Æ(´”ÌuX¦‚DÕÄl~qcS=Ö	T}ËDïğ’UÜÀPÁ×-İØl-$;µÆÃŸy±”ZÒZF}¥Ä Øu–†ò°¥SuØ‹Â:ùWøhñf|ŞğïÒiÎØ“¦?0 óR.Ö<)í‹¨½íy÷=ğHVˆyËñ¥!!bbœ å†$Í’6–'­"§uÍkÀì`|àÁúô†Hgæ/Î­ĞÂVâùIæ*v¬!­•ĞrµŞ+*Ø7×®X'f4¼&D ü .÷†ÁíBğ£“¬îù
*„‚}ê¡¢ñCW}^"Ë¶BÚ'<•BÁç9ı-ì	ŞRX³dw1q™ËÚ‡€b^qƒÏ¦ˆ'¨
²"©±`¢+”-ûÑehõqÌ 2‰Íû½­o³'i¿y†*µíqóRå‰‚&”¥l!J?:\Z¯`*	ÄZèøˆ—3 #ô†¾òu:JB­EL¸á*2¢f¥}îÜ”Üqƒ-Ÿ½Õmi&á ›¥äTB¦ÉÉ	é” ^RÂ¢prx-!+O!¶„g‚W€K¡…x¾§¹ñòYİäªòä5ˆ÷|—Ã'=›<ç¥%\¢—uE¯Ãnz€ê~.9–›òéyºÄ’2Rl¹±ÕG\ßÖ;ÈßŞVhGP)æ{Í&"2ëåšÛDÎù‚T†Íé]²„[uÕ*omıIZ'f2e³2Ş¼2‰<ï•ñ)kh™6§è“ïk®ÀDAƒ½äÖ•ÕU«‡0°ú:@ÜS-vH
·Õ9FøŒ–yÊæúA<ß[ÃĞ™cj—i®¸Ÿ\şz :%2¼6Èğ"¬ÀD<}E±ô”håsŠÓ¬„Z×j©{s¼ìøÌ*5C$Ws×rµr×3àÁ~i?2NmiŸüjyù¢Ö¾’›><£êĞ>_­öÆ8d<cGûäÕZ/ÇêA„W«ño'”(*ø9UéL‰¼ÄÓ	v…ì9§S¹Å–5­w˜u?pÕÎ|+,7Nn‘Ö¤èÒPÁí°šÑÉÉ%°Rİ(ïG<j¶öG£Ë°­˜º5h<Æ^©¶hì§ü¬öR§…ıR×ÄvÈÁ¡Ã5Lû&Ú57œÒ tgM–c²[1*Ì‡2/ãÂÑP)ó÷!Óı‚GX6m£½¨Ã>¢~‹H]%¿Ñ^dœ–{Ñ±=4lYnÙ˜·W_ĞŞİø—š£5N¥±vvF8½0ú!'±‡Éƒ&äX†B™×ãcüQ,Ò•[êò¹Ø‡Ô´£Fçå,cjyFr²¡¿±ycæçåÃ­®¬M×v ğ!mBfgk(Ú:ß*=çi…60­Å	m„&ÄZœpP¡ßîûN:èä±r*Y ëP!Ï@`‚x§Òm8Û;ÔÃª\¤Nˆ³9dé¸nîL7´®“ËfKå¶bg¢z]–¿ùl7í	ªòùK- ‰vÄ^NÛec¶OÒww“‘LvY`Ÿ!ÓAŞ^ßYPÜëÓC1ÉÕvºÎº‚ˆzQmc/×ÅÌ·A^—êáa·AÅcnƒ˜
ùxËXÖ|ƒ› ê-Sö³èj¥ÑÄÙ½9ÒÂliqf»¦<ïæˆqøª›#.á!Üè`zël`äkqF?5:+Ùm¼¬½Wçúá¶ƒÓ ¶N!ò¹™\ÆÕ›£ĞètÌ#ÛQÎ¨İìº·,§iVÀ¶KÛ‡[ãõÔèäôq· «Y²'£Ù;N<«boœ\±÷*m¿@“KJÀs.Û^òs¸7Æö­Óµ¹ç"ò’[ŸÃQí‡°¬¬j®59ßró]1Aw6rS¾~¹I?|ğ`åøµzŸ’ÚÙõù4¢Ú(ÃN€FÔq	O,œ¿2s.šŸrQNşi^nÜv_H¼mXğÆ3‘ßÇçŒ[#kêU&Sõ˜»ıcú~|‰|ñç §ÛÊ°×²6?ó*UÁªÍ»_æœšÅQG	Õó¤iİQ¢Y&³kĞ¦gÑ ]ä[Ef“z‘ÄŞ!YéõÒó-ïÔí)ovIÅ+ îB­\ğ±xçËz-gå¨éàæ;U)t}#ñ÷x´@ıTêe™¨U³[ùøî¶]
_òñ£ÚvÆâ!mûR…ìéú~bŞyª¨Kî(/ËÜ÷¶ùøOròåÆyîá¶[¼‰.!Ïk,ß;ëş–vl¯ËîÕ±´”›ø¸
Ù¸szïçğT>7œtÑ:ƒÑMÚ€Ø}'¢ fÔè–ª‰½ÿ@ãX˜_ŞÁRº0t»ÕŞ«Zên;µ™I]½püÊ=põXåmmšÕ™ÂâÊîÜÃAe¤·W³É¨âê2—<}íQJ5Ui³JœÍ¯DĞİh6™ömn©ÏËI”Îè¤L‹¦*É¢0êLéz3]²x³¦¼‘Ø½¬¿ˆÚY‘ÿ-şØ/ÛH
endstream
endobj
93 0 obj
<</Filter /FlateDecode
/Length 2864>> stream
xœí\Û¹}ï¯¨ç ®Õı<·}N2@>ÀÉnŒìæÿºRuéR»U½¬gÜãn$’‡G”D•=éÃ×ÄàûÓL>:ÅgÏ½wÓ—¯—_.ø{¡›¤f~úõ_—üiú/ÈÕÌ4µq„ötä~ÿíÇ)¾ùõçË?Êéçÿ…ñ¬—çBàp?	Ã¦ñ4}z¿üğ¦&?½ÿù$ílzrzÿzù3cRÿezÿÏÅÀïßÿ9@¸¥@-6lHnÎƒ@]|¨8èëû¶ášëYpg‰åÜ.•ˆ…¾´|İbé=—KÁN‹=C…ã“€÷lT×{CPko&—æ.íg×‘L\5æ)÷ş+|ÿráÜÌ¿ÔÄ­®LBhà­ üŒT¹+gä*ŠïHçO\8¥üì½8¦± â;Ïgoa,úú­…0†`³†RÉékú ø°é?(œ‡%ÜƒUnÂÚò$“*ÈŒg¢´cÒO_°·ã–›0w³•ØĞ{Ä"J”T8Lw!d–+¡+‡ß™ÔÓ÷Ad¥…8%™ã0œ˜™’Âù$3ÎagFymsK0[‚ñÊº,Cöç·_.ÆÛòé?ÍRrU£Äht«‰2¯±rãÁ#¼"f¢LKø"î ÌkuÛxÀ	®>(ãN¸
"J$óÆ7h£TI£‰KAü‰Êr„c¯üi’ È¸Af”¦™WÙ‚h)Õ,tìœ
2-,õ<È¬1	·„Qzo&‚%ÈôÌ­¡¨™d)~9>AªbxR£(˜»a'!Ë‡!HiNˆ”G%Œ#ê	7‹¡•ÂÅBuây"2s
”dÌÉl,Ñ!³¶D‘Ìñ/—czpSüƒY!¿	‚å{Rø¾'…?TRøûm›Ø»@`gá¹AT8âf‹*ı$™E/aoıQÄ*ˆÍl¹›PæwQæfîaWa_ADã@•/ĞUØbË0€T4ìfQP* mT2 a,LàõÜR1Ù›YctÈ Ä)É4UB{g0±1LHà«¨ äÀŠ¨,yÛÊ0¡W?R"³SÕ„2Ä(” ŸŒ¾&ûQ
¹I M³£(;e%Lª¡Î V)0c]¥5(UOµ¨†ºÚ^)Q}Üâ²ù&ìLøg"ßª`•5®XÎ	”GÍÜ‡XI #DÌÀSè@88Ø9Ëy˜F“p¡ÔÏ–!J&¦.4UÀùNpYù„6òÍøÂ·,F¾YH!©f|Ğ€O£L q”ˆ|#v	 ™Ğ\4> $ÇÔB½MBK‘	$q…ñãRG@)°ÛbP³*pøhá²U(Ïy39€Ò@Š©zŠ23V¥Ê0WÊJ¸$‹
Ø¤
QSÂ×T"MLoø“\ÜàTæÛ-g³Y¡Uà…åƒæs=©…Ó%7Ìaz¾T°œÁ. ŸÈ5¬JÁëŞóô^À{?G¹rğ2xrİ–ãçğ»<Ö+¼X¨í§Şµ]ÂÂª#p¿BÍ;ìİ`rûö¥]ú[&“>¯MkÜFwŞbàX³·ÅX&¾×	ĞÖÆqÂ{ÛIÆÏ°˜Ú&Ø÷{“¤#è4	ªç#Ÿš.­ç=H	˜×ÛH±Ïù•Ç™±àºLk%¹bµÖÅ™€©g°öÓêì²Q²•®ˆ‡è%T+6{Ù˜0@C¨E,…W,‡4§¸ÕZ@ºÜsPˆ“] ÀìŞ¥Ø¥%LÜ0N°uÑ²¥lß6ª—Ñ²¢IùDh=œ7ËI'È Ï¸á[®=ã\á,[Ò3#×^İYùËQvt[ê¤»væüTâ–H~q
İÁe?q<â-œ:—A°Eæº•?C$p#‘CÛzuÇ¢uÈ(©H¢#j»ål£ú38{šÅ‡ƒ2×qVck!ÿpáù6ãFpèÁM2ó $^5›wp|ÃD'ôÊ‘ıe9¾›™³¸é¹iÏùÜÃe·ã+ËºBBnn«îàyÚ*†­¥µ<ÁêgX&Åò–jÈ†É²fh,Dó1€np~Üòàjtáçƒ&\Ñ˜[¶ó#bœán¡åpN`ÁUÛ<+]¸ùÛÍŠ¢ûA³Â¬›£fEz}Î13¸Ø±ÿjlİúÈxgüÂ¸Šåc^Ø§¸AËñ•U1] m©bœPaô•°k·.„åì©n©Â²õœ–ªƒ­YÈ~›KÚ¸=LV¸Üº¼æÚÆ=õ‘çaÖ–pµÃa–ÓXk”Jºv\%¬Ø®3oêl|ªVÕ•c2µ°Ë#¹]$¸õ0Jê\¶¶	ı>Îì”Kùï¥ÖÌB»Ï©ªm)ï‚<óNù«5d¥¸¥nwÁ¤÷Ä÷¸’«o	.SaÏQh‚|ãìJåıåË#¿­˜Uf•¾í´§ìŞiW5Mxe¥Ü¸çÛ¨S¨–áÂŠª¢mT«‹Vf· ÌêœÕÃ/©ÿSúIŒœåéOÃvTÕŞÍÊ¥”do; âµoÚûä	æ’Ù„MÁµ·
sAƒ¯CutÖbjÎyÚßvÖÒüè¬µkÕÆ¼	^§¹úr2ïnAƒ¦3—úË„ük%D r*ßs~Cz¢nwÁ$·-[«È¨‚,ÕÙe£Ş; l¥¿PÃüÀV?¥ò†jè²ÈîŞm¬S¤Öôm«|¬B¥˜£†ÔÉé-uª¿}½3ş¼[5wKĞzœŸÏ#OÚÕ§a×äö¡ugìõ œr‰šªéáŒá{×mçŸõ«îÁ×­SçP'ñ[Æp†Ü7´~œ{! |(Š,ÕvqHì<^›‡ˆ×T7.a;¢¿påÙjJ—éê·»«ºÇib«zË†Zæb#E¦Ió­·Bû$¸s•ÆÚqÜ„ãtœ$Aùˆ5KH›şK‹AfîQ7BUÓyeÕ˜z—ö`W.ÔóıªMË6.8´6 ”6ÊF¾²ƒÒ¦ewœ7¬ŞÈ5–NÀ:Ÿ*u—?J.õŞ±ä]x¶%ü}´#v±´cç1°|jéû´*û¦:ç˜çUœßŠ©\ ÍÁöü†ÔTãc´a&Ëºf˜tÊ%ãå	œ³.	ªŠs.	Z®œLúB¾L¬—ZUØ'Ş¸ËgÓBHày5'îˆœ’,—“ªe‡»%ë†o+ŞW)(·7|ãÊşDÃ7•ı©…]é½×¢Mİï‚Ënï¹PÏ^@yX·nêÎ¤-©—Z¶ª}»jâWKª8ÅJ›ÂÙ¿/O½d¨pĞkÓKÉß÷;}X¥;öjNŸù?¾:KuvÙ(÷ª³'ÖB‰ÒSj¡Ô©.ô^AøÁ‘WCÆ?FNìÅî=ÿ¿}bÃŒª4_óê”ÀÊ&0ÎhÜIz¾&ƒ«ÿ´U)z$‰†¤Œ·4Ïqw5dJ#Ëó».¬ıÁóÃÎöUÓyÅøÖ›‡=²O\;ã‘ıë^uÕMq1ákŒ:ZúÊ¦'Ô‰î±¥÷…Sz2áÏè'ó—^Zˆ¯Oæ7j»%úªÙı‹âyOæcG?™ßàĞ…›ê«]Ÿ2‹îSoˆndº4{§«{®‚Öiä(+«øÿ´u9à¶ŸR¾lMç–ä.İS’o†êA“³õÑe@IÒÈï¢4.¸:¥4~wå,ï]õßüNKŞÔ²>¦ºëÛõãùLGÈ½ğ?:ù?'yû
endstream
endobj
95 0 obj
<</Filter /FlateDecode
/Length 3297>> stream
xœí\Ûn¹}Ÿ¯èç îåı¬‘´ÏIäœì`7ÿ¤Šd‘ÅîiÎLk½ÀZ¶¬™^ªN]YMyV:¦¯IÀŸO3{Œœ£Œ1L_¾~9áçÊ1i+âôë¿NÿøÓô_ ›Y:êó
ı;˜('üó·§üâ×ŸO?ü¨§Ÿÿ—ÖóQOR*…Ëı”(‡æ0ôéíôÃ«™âôö,”8”“ö³RÙIééíëéÏBhû—éí?'Ÿ¿ıs‚
K‚Y|"øJĞ"ÂöR&‚®›§ÄJ0yÑ—·uÆ­´³’Á3Î¥_n¢›È%ç—#–ÒK½$lŒØbT9 x‹G{}6(µÍzÉî’q-ÔUfhö_áÏ/')İìğËL‘V,VòÖhV«g´ Ü"¿bÓ>I-ËvXÉ‡(‹ÏÑÃ$ş/Ì»$ÂJÌfj£§¯å #¦w|cĞRd®Â„Œ•…¦M¢¹(T'tœ¾àì ½ti=f¯q`Œà1…b¨H‚£+¥‰öS%|æÊLsóÚƒ†
-HXNÍÂhb¡¹p²¦¢õ4ØÅ‘À¼ñhh÷ôòËÉE_ß½ã»YkiÚ`¤8‹bµ%‘­s¾ÛÜEÁ©h›H³¾˜8HóÎ{ÇÅv°J†ÒdP¡ˆ-¢‹ÚH5ÚYÅô’h ?Ãô‡4ÒpEÊ?±ñH™Ú‰­›hÎXÎA¢ECdNhfeóä"P¢Yå¹ä‰æ+¸Œ5F71,fgéG=Ñ´(ú#ı$ªÉê)JÌ¤´ MÃIJ×7ï'f u83$Z•YÛÙfe´™p•‡™:“¼ùD…ˆyN…’ùÃœycÕóÚªEæã_NÿÆğ¦ü£½N”å{Pø¾…?TPøûhÙU¨tVj“IF#0a¢?‚Dÿ^©&Q=+`£!õ”ö@„’]ÁW"ZÅ‘ 5
ÌÉ°—3
Æ:€Ã™<)Ø‹!˜Æ2û(=£¢ná¥E¥°€ˆ(,ß
ˆŠe8itl)- S0&.%({a{bÆ%Í/Ô
áû‚¼¤
6B8ñŒ' I‘œ8IZØGªœ˜d“ijNB<ˆ‚rDCÅÄDkšhë7¥qNš~ÏÍšl+v„¦ˆ&¦à\úH™M¬JSuÙQa7°~°nPU€e‘håì¼Æ\ãà ©l21«gKY	Â:RAF¶ ÂD«B
¬×Q7³…_¥\¬fI“Êƒúƒ0İtåÁ™˜n#åİlT¶/Æ“òé¬TÿÊGÕv’¢g ¤ù…Zñ{?µùH£Õaj!ÍùyÆÒ cyŸ—,ì#did‘hÉ¸‘K„h9 êjcº†‡3›Oê`ÛTÅuU3Ö;»)"^Ú™Ù-ç¯€ùŒ¹X:õ”v"KçG	û™îi m)Ã»)œ!ÏAJÁÔ2AÒ
yñ%Ú[ë*YÖ5wL€ïX×`}cmĞ¥‘á[0Öò.
ƒ‚G™´úq{µSÔ¾_ÌL˜ç,†uğÓÀ÷+ş¬ûF'`‹µ (ÖM'Ü%q{_©İ&ç–’=Á¾ìXY^+xmáç¹qf€3q> d…%Çò¹ëG¬Lƒxƒ_×ÍUs1¢çßUš¬<kbn…uïÇ´ÙvøLß;œI¡ r¸°œ?&‘«İ¦Où\æ¸<Æ¤y(Ãkù|Í€n^à3Uö
…vÎsÓÓÆZ]Æ~.t_Ö3{òBöp¶˜.{&(h7`bì¤Ÿ¾‰×Áæ²3â˜ä¨¦Á–œôÜàÃÏ2M¢ëõµ*üa”¯=¹!I²*&ş\p@X‡Š¹Äbbá%kµZ‰{­s¨ö,Œà‚…ácL¿W…iJ—~úò™,<âü§ò™Ë|$•¯j;ï`fá€f($1èF †lKáŸ,¶™5%Ñ^Ì|ª>5”&‡·Æí tÚnRõ¿-®Vü&I]|1Í•ÌïnAƒ‡³’lq^Bş¥D2d™×)ÏÆÂ{&k®æ¥ı¼ÃWÚÑëÅhnvÅ;\‘¼+SŠ®êíkà­åƒâmUi›•Ï ğrÆj©bÁ/ëÒkãá¸eÏ%Àiîqd‹®ˆæDkYê^Bnbñ[‚äF`\K¿õ3ò­’·èı>Ø_òpr^@1^¯½BÁ¹‰ºVÙP˜ØªPğı®aÏ€J~Îêhæ¶jÒò‘ØLÔ-­V˜¼è-Ï¶hY5M°x–"à\SG¥ëË×dÕÕy‹%îÂn•šsÂA1Ü–h±-utµQ±RB¶W“tG`P­QëòîK©«yb)"m©kö±[*Zëj©Èa‚UíeøTè³,\m‹^ÓÏ×íÄ.IÁ>³Ï¶ìtY"Òš‹ú‰ûMÇãZ%q¬¬	³ğ!%%Ñ¤æ¶\OaÆ’Ò…Õ¸ikRø<bQ,Y=è5iÿso"ç0z=h	Ñjˆ²öÔáõ¬Bî®!xƒÚK\;5ç5¯0š&?ÀÜR'/¡H^"—,=nßºu¬u ‡gN'n«œÚ¬.:,t£º.ßsˆG½Ş…i­Nëâ4[g|î&¥Vç‚6Ô_b;Ñ!ˆ2Ä¹ùµ¹zJ?¢w'ôìDL'^.üXv«ú1å¨AÑ½ë¿,ÛYAl¶³ğ=F—äO†û[œ›Ç1ÃÈä\¤!üVÅ2·¤–¨—¬îìOJúM-^ÁkÅ
UŠ<nğX´{„+1L_9Æ	ü¶˜^:îghíjŸwªœ9úCÚŠ[•ãGj«m
hJšÏ-ùU-•€t*÷ê©UO+Z>FK^Î¹²@ï…U¥*@×<ÒõÅ™ïõ 6œÒµ­Ãu²c8N«âm%µ—T/¦ØmÄe…õ\¤<HeølÈ”GC…]Ï’xƒƒ'›7&ª^o|±XôÜªújí”Ú–ñë¹ÆNéªÄaÔğá²Ò¹õÛ„‘GèC_\ˆ¡ôüÁYÍhAÑ•ëfH—vë’óña˜GÓì´îÙ.UUry†ä÷[ç„G1¥`a@ìğ T¨³2Äz\okô¨Õ¯m'‹m§b¢É¤P Œ+[%a(É|PLI{}1àµuítù­.Ğ!ÆRt©áVçgğ©#Œ·ç‚Üëluå²Ô	QÆìƒñô–ïC²nJ EÁŒ½8’CQGtHjëÎÀ‡x¿”²İ¦i{'¿?â²N®—{¡nÊ‰ç¶(Á‰¢p}D¬ö£¹½RŞœ¯_÷:1ÎÌÁ;P·Äƒ¡Së#	j(`ä‹•ÙÌmgåà¶ÎÊß&~DÛüÕu'jö˜ŠŠtê)ó§ÖÇ„ö¸jĞµÖG%¿#O\6ÈÚ\äï^ÂsII!né‚wØÊA«n¼Ìâ7÷Ø¼!ñ~ôïÔ‡k¼Ïá˜.^›áÒÅ‚kwZö«1³r82CH*sa˜UM©lé×,tR›¡ûéñĞ¿¢T­ÂDCÛl>Ù±ÛGN­a²çÒŞ<Ä®•S³Q9r1Öm	ûìÆ…-ï÷Xåydí9']«;Äa£æı]‡Öá
R°Û{¶v‚] dıçMÖ­ò»¶&Fş:÷³¨-8ô¡}ˆŒŸ•Ã½ÈC…Í+GCÕû•¶]©Èøáêqôèy¢rÎ89î4ÁÎ‡I4¹ÃĞĞ:P!¸€ÃÊàH¹2w•¶Ğ¸ëâôÈE3#ÜrÛ!ó”cÇÛoTü°>g“D([âA¡ØIz¤Æªõ‘şò’ÊÒ&ùã;Ï’Íj¿ö×¡;¤>¨`âKL;özì±ıq*®¬4t÷•Ã1¦{ßÁz8±t;qä7¯èıÖ‰¥rÂ¯“`|í.>.¿•[Œ£z–±JwD­?"¿Ğsâ‹£øÇ+Òæ,Ò4zXnŒîÒ^(àŞö«W#n~¡ˆA§Š÷ıûtí^:ÜºëÉï“ÊÅë­{£÷N×~±ÜÒî=‘c¬N#Z“’NÊ–]ïè®}ĞUÔçƒRkjI±ÿ¸Iµv9cjÓ÷6,–ßÙ®Å&æÏãÙ/à0 ä÷SˆÍ-‰Û!]ØûzÇWª&r¼:¸šhÛ=Á‹aÓ®ş¾†ÄFB¹÷Y>·e:Ç‹¾¯ùh1µ-´¤ŞNÍ”ñ¾NÊ7ÈÍŒUÌÍkš£‹ìæ:UíS¦;¶çéw—«öîz3S—‰[ÁˆÕàÿQrÌsÛı§Nõ¹-Ûµq‰ÿ{Òÿ­'Ö•
endstream
endobj
97 0 obj
<</Filter /FlateDecode
/Length 3216>> stream
xœí\Û$·}ï¯¨ç [Öıvzfüœd€|À:vÌ°óÿ@H‰”XÕ—ªV¯dgÜ³]ì’ÄË!E²ÔÍågRğûi—Éé9ëœÓôåëá×~n\R“õ*O¿ıóğ?Mÿº›u€[cayõ„¿ûqªo~ûåğÃvúå¿e¾˜í¤µ18İÏ…¢ğÖún}z;üğê¦<½ıõdã“6~2vzûzø³RÖÿezû÷!Àço?M@0iMpkB,„ØVBº<‡Ö…`Á×!¹\ôåí<ã^ûÙèç:®1«EôšóÓ;ÖÒk»&\¸ã£&é)‚/ñ®£öÑÊ®Ù]ó¯®3c•¹ÊÌş+üşzĞ:ÌÜ¤QÓÆbh>ÀµvFáõöI[—’º‰_ˆOY€çaüãN‰0‡Q³‡‘ÖÙé+]€bÔô0!Eg`*MxC€{5Ñ€?¤…¬L»OÙ<}ÁÑIGÊ|:ÍÑâ9ƒÃÅ°g±L8ÂPŸaŒÁû¢` ¢%Ó™Y9kR&ZH	`*ûÈw»x'0ïbbÂß~9„ÛÕ;^ÍÖj×oFJğ(VŸiÙ‡‹‡"“`iŞÂi1Ä¤Ø!ƒî”ÑNèi:™Ô•ˆ«rÈm#ÕÙà°K¡ıœ°ÒØÂuÿı îGÊªÄ¼…œ—ZvÌAåˆ [“@…æM”’ZôF:*ÔœÃ$t	4?ë¤ÖÍ*²Û§P]5±’Ê„<Û.Ş ív$U N,/°Ùínò¨É»O4	Ïiª>&t.¼±YGxm³¢ğñ/‡axHSı£¿/Œå{Pø¾…ÿ« ğ÷½Y$-`ÒÙd¼ê ³*}ÔOÙ«€YË{#ºBCE£€˜•N•`r ¸„ü~¨êÅÑ	TêÀÉzN)ãÔá?$D' ‹£Å½>ƒF³†FÍaöh¦ıOy¹ 3dÈP^,˜1V&B’q j€@]†E\‹2Êp"v½½¯¨ 0¸ê+!ÑÎ	`"¸B¢GÜU1I ¤ÂRÁÆ©ËY‰)º©ëƒi¾(˜5×©h7ÖpßM!êf“<uö;„ ç°„xDœ…E\¨ŸO8ëÔOÙ2ë‚\€áøFgWˆ–‰HPKo
Â“©–U‚Ği€Áı<Ü©ñ_“ÊQWjÛ`Vih0©µ2&åäxÁŸA3rÃìLÁšäÈDˆu€Ñ÷&fÔ/ä$bl
)£‰ÖU÷~èÃ‘
Ók[†ÓB@àD0…D0‘·Äñdë£±œHÃkÖF½Æ`h;Äªnšni«_LÛµä Ur» 
Ëu=Œ¬Ê®Ë¾úC-fLKJ/ÄJÕ¨a=·¨ìVc<×¡÷¼¸Æœ½‡ÍB½‹ğ"?2¶¦qãâ”'6w|ÉZPÊáë	^N)}õ:Á{øW½ÀÖ­Z+ ÙØ¡,°ä-µ³¨Á/iv¥iÓãdpŸé_Ø¤İ3‰¨«Ø€û"®{­÷ à]Óçæic`õ$æ5yRY™ï™æTtız}uÜÒ&7‘¬'T±Ku ‘=ªë@³î`Ú3AB•ª×´+@ƒ-Õ(‹.&×FÕ5á• Icö”†ŞµŒ>v3,Lìi}2?"Ñ/4i1åS7K™çHc7`„æ¿´FÊ<©×»‚ÃÏÉg›V¢ï‚X¯Şg(`Y?o¬WsŠ
„¶ê>.­Š÷ø;)µ¦øjœÃM§ÄÊÒï]\_[æşé‚5XÆˆhÉxa[£ûû.|3"‚BÆ®%ØØŠ6FıR±»aÂ‡1*š€—„:'Î“‰ôeD<é`•2ïÒ‘ógu4H1Bf+öÚJO‹s¦òCÜf„·U¶]\çÙGÖ›ó·ér¯}ØzŒS=Åší¼À:Zí{ñjHá›{v6¶¼º¤S¤x¡È]ŠOö£øÎ¬c9ãzî™“7=¼ªWâKSØUb«NôY&~ƒ ]ËÔ(ÓÃûì™mZ	,¶iÛ¯Ë{¾çµ€OïØÔ]]/¦Æ¶¤QZ|BpEYÂ-‰‹•l}Şö²óQÜRÒh©†TX/±år¸G`Î™–ÃöiÔÜVñ€o»ßß–bŸs}ÿ5f7·ƒa^5Qøùú*"©øãqéÇ.“¯êê·.tÄyéëœ³²O³ÿq¬ 4Ìó}2VÄ3é›_¦ÿmGE±¥8B9s¹¦yÇ-bÖ¼¾Úc¯ÃJ'˜.Ç¦Æ÷¥*ëÜ˜!^gM¸]Š·®Şæ#àê½j¾Y]–ÌüLY)ß{aL1Ë“j•°—k^s¤fo‡Ÿ	J¾Î·İ@(²F{¬„†ÑfVÚWhÄÛö*Ÿ?²W•ºì›˜n«:v.Q—cŸÜAß¶£Ë;ÊÕ¨yk³b3O¦í,ìdÙµş‘=ÿ*‰oOdF½µ÷ª²¯0¬^«œŞ^oqF†ş;|EÔƒ}•¶ğfyÅÁÕxë¹		´ÉÚîF>HÓ°í© İµ×'[hÄb‹2?9å.4&NmŠ´ÔàTŠÅ4ek{_tHûœûxˆêtß×ØÎ¹¼+(]rµ/ÁÛæ0²kF‚e(¸³5rAŠiSõq*x~aÖf.§òÖÄkuŠZ,ÙOOŞYüØ\Ó0!Íë8®±LJkuéÏƒ"‚¦šVğ¾§mÀŠ»¤wy»Ô©:	¶Ù»KdÑ¬yª†$dx„„šR}	G9¯z^8ï½€1Şµ¡/602ŞUíi®q¥/?4äÎs{õ8:ä†ÓT%FZHÆ•ÙOˆ»ò>¿L‡9X?
•~â‡ô¬E?æ¬¨wG27i%j©(¡+âzríã¼z;çäìR¤íà0_›dghKælhÿğ¢¯44ÅĞÊô¤t)M{H•™†eAŸQÙÅ½fÈÛnŸn«0“Úw†åGúÚ§Ï FhYv™WrŞı|£dmbR?ğa€¬‰úšú‹%&‘J%/=`O7Â¤XÍ¤•ZvÁÅœV÷#6Êdó#¡Âb1AIÌ%‚9ÖRK‡òØ‰+çØ3ÇuÛ˜1q/¡Uø¹Ï³nu·Ö4ÎÁ‚h!ãg#R-gñëZâÍÎ¤MíT˜4Â.ÀùôáôƒüãLH½©£ÕYØÉr<­÷Gô±ñsïíZ>²b_Õ²™wä®PÇQùœıªõªè¤Ö».mßÔ?w„å‚«$š‹„Ç¶–ÀüËÎŒYûG'×}‰Ç$×}~îÁzR¯§Şusc>¤Ö¢ıØZRl!ğ¦ëÜ“ã÷1Nt°èˆÌùœi®¢Å¯ïÇ'Á}¥¦»HFõ£H“NDºÜ/Ú¯ßhÙCg`H×
‚îR*zº[[$‘ñ\‡å½‚ïó£! tDº<!=Ñßö#¤õ€} ÷g*æ¡7š‡‡ŞxZÈ½mşÍĞKÆÚ ~B«;Úİ%R!üCÃp?_ÖWÜÂ1·òäœ•®'Ÿ/7…ÛJÂ‘~(Ü…»T7DaÑö…Ç
hîømS—¾÷ÀMdmšaû‡w=[ëFÚsÚœ°;|Öï¨gœ2­§µBnˆÂd.×Ü'»K«(RœÚ¨Z Ù~FèöşòC°-‰°`q§HËS¹¡}H¤«ãâ•o3Øj°ğbÚ©¶À7ºs-×Üe)­ü%ğù?ø:‹;E2îøné€¯s;|ÚÉSzFvïÄö‹À£ĞĞê`úâ@ªÚác_­aFÇÛÚáYÑ™lã<¥-ÔÙq—º«Cú‹ƒ»ÏÆ c0–Õ‹˜Çv+Öû»ĞŒĞ£¢%¿À])F½æÎ–”íÚdÙ1ã4ï¹ë“ïm‡Š§6”]N'ıà²K,ñ²KÌ¿­Âq.ñ$HJHOOĞ–çÇ<¼KmUĞŸêh_P\~›¢J¬T'?©şm˜1_PËg–bãİÁH<ÉÈ	]ÇÔC%‚•^Ùj‚R·’–¿h#¥=—¬m¢ÊºÀG|KìB•Ş÷¥ò¥q¾y6RêDÚ¯%Ë»D´i§ˆÒ"¿ovbÓ«T‹ÚÓÌÿ?ÿ£Í—
endstream
endobj
99 0 obj
<</Filter /FlateDecode
/Length 2903>> stream
xœí\Ûn$Ç}Ÿ¯èç Û®û¬f%?'XÇ)€ÿBÖ•ÕÓ=]£©5ÕZ+§ªH^ŠdwÒ‡¯‰ÁŸO3yéŸ=÷ŞM_ßO¿Ÿğ}¡›¤f~úã_§şeúĞÕÌ,µñ„öläşùûOSüå_O?ü$§_ÿÎ³^NœÇı(—Æ_`éÓëé‡5ùéõ8(HÈ'igë¸Ğ“Óëûé¯ŒIıãôúÛÉÀû¯?O@nIPK‚[’‚Û>ƒó@… ã_*úüº.¸æzÜY"9·K&bÁ„/%¿\±ÔË%acÅ– ÂñÉÀ[2^WS€Qën&—â.åg×…‘L\æ)ïşüùıÄ¹™~©‰#ÒBƒÇ
@ŞÀÕkåŒ„,âodÛ'.ófFCí:° —w'½…³èß°ï’g6kØ)•œŞÓ@†MoøBa:¤pR¹	XËMª@3‰²I?}Åİ[nÂyÜÍVâBï!bE0‡@Bfø#låğI;-ì¸ÎJJ4Çá813%…ó‰fœÃÍ„òÚæ• .®á•u™†~Ÿız2Ş–Woøj–’«º)F£ZõH¤ymŒm˜*áiZÂQiÖXk¨ÚÆvLpEğAwÂU‘"Á+|ƒ6R•4Z»ØOû!-[8îÊÆ;‘õH™Ú‰œhFi*A y•%ˆ’QÍBÇÍI¡@ÓÂRÍÍ“pKª÷f"XMÏÜŠz I–ì—í¨*š'1’Âyn²¼x;)Ë‰#åS‰ÇöÄ7‹ Õ…‹>ÄÕ‰æ5&
D$r
”$Ææ$‹uHÔ+’ÿzú7¦7Åÿ0+äßCBcAFù¾'…ïIáÿ*)ü£·lªL:ÏAV.<,z'”O\XĞ
k–·BV‘Â0›€êw‰ªgf• *”ì¾"ÕÀÆàÅÜ¦J€ß:DWxÔE\—@u±vrà1ªH‰ıõÜR2Új+†!d b42İpª‡ŠÚV6! .ÕhT>‘ù%­ÔQ8"‘#–oŠ™áÜ°;qB"Èê b!‚’Çd—U ª‘ÎNUY$‚×¯T\M¸3†…ˆvÌh×İÕ.„M5"•¨œ_}ƒ¨¹ô,ôLô8Á°Ÿ3‘ùN( §±Å¨Ä²,%˜Æq¯"¤İj ¯ZD*`¡Ó-é(6~Á!&µpim¸.¸¬ŞI¾ñÅ×"=ÍBŞpL‘ÍÂB`(8(İŒ
$@?¡¹hÅ 0Ç|Ò¨š¨–âHäàÛ©nGŠ \Ø8!½Ãz"!=`²G&W“K“¦Hƒ+Áª©B’i1AÊêg‰
B˜ÉşlÂ¦X®•¨˜™Jß¸NÖsáOÙÏnéÇflã_˜ƒ±”j)µCı$fªé(\cA¬t¨×¿µ†ÎŞawß»éH‡_ÓûMÿzÉ/†1(ÕrİÙ¥$û¤TÏ 	ˆ¤^Ö¥Tæ)	×.)õ¸>`¥àç—$É9ÇŸÚÆŸìiÓ—-Î;2¸D ÚúŠREŸµ†	®geáoÈ¡è3KZ6m¨(!Ò¹ xjñUøœÔFzR/«Twiİ—ªºæQİàF’¨Ö $å½|¬Ñ&©Òú,éëkD/œù~fşza¤=¥suÕ#¼æ-Ÿ"ïSâë"¿¬C0w0ûÉ ÿA™nu‹l—³IiÒz•PhdÉÎKI¾Z$k®74ûLĞpëç¤EEa×I£ìZ/’É[´%^`Ï¤ŸòÉ*<üäX”dk†õ/$˜àçÙ½³ç¨„¡ÖBjj¬­'¨Ú]Ì¦KÚ^dÀ]ÑÚCùr~G®Şò(±˜Œù¨² A-P¶ıätB…Ó/ˆÛ,Ô^Úöü ±J.åb å–àyéVE3ìì146Lp›ï0\·eº½m£üõ³;°	s	-ÿ²—f¥&‘¹ê$^nÜcˆj{›&Tyr¨sMCìiÂ
.% ên„KÃöûĞ%)Qûeœè^W;øÅ“„;ƒÉUöİ˜óÙ;%İÂÒ=¡ è]óŒA)ŠDyå¢xD’‚FNzf„¾P„ºutíqöÇ…O·gå:Æw5”ß'ïenø¬mòyŠC—@®î)q9_-KåM+5ë>QÀÆ°ì‚D×rv¼­°?›××kÔ+…‹rY°Ye_‘ÿªmõz“u@pN¡yäè19&}ŒqŒ¨Õø{r¨¬r²&GïÆ8\˜Ky:Àôõ°‡xáı  7—ó}^ÔÏ˜ wáNq:\µ¯s
òÂéĞ oôyT¦ÜŒòzôAî.ç(×œ@3ûÍ‚¼ò~LS]‡99P¯ŒFßâkò_µ­0
ğÊéÈ oõyP€W¦C:5àäèş § t9Òß.Àï¸Òƒ¼¨W&§5ÀLªa!1n´Îtæ¹˜;†äcCú­y¢ŠÃ±<©.ë8™Bç‰uâôvd]ˆ&{¶æš[“îåô\rÄˆ©ËCı9NËË<Øp>g3PT20D.lÈF¶å³Ÿ¤™—›úÒ‘aëc£èÍ@ñ®‘nºvÈ%,+¡¨x]êˆõ!Èø+¶r:d
Ö*Bm±¸[?˜Néì‹ğ:jøAg­•İş¨œÌQ)"]® úLqÑVŞãê.üÚB©‹§¿)‰>¼\4ì‡ŒP°˜F—íÑ»^M¶["İéº÷ƒ ë^r%²Dú¶¶ßØõ¶ÿ{Íüë¬Xw>ØE¼™K ¥†ŒÓ%Så)Å«_ß×Q¯Ü€ËQlà{¹î–ÎßÖDZ¾ŞDŞá.æ›»KUjH^¡îBñêÂWöõg7¸Ëß»Ü…Š×¥Vwå»{oÅš«$øÉ™âdÒóØ§ÅTç.ŒìúCõñEcåtHÑØ*rlÑHx:P'`e¹_"'é•.wğ[-Ññ…cå=¸pl•ZKU!Å¿4•§+˜÷Ÿb¿WÆFéWòyìu>ªS…­ÿƒå½×A‘
0êy&¿¼t8D~6èA„”­w#@*Sjkjüp¼ï£/’)‡.‰dï§ŒÇÉ7ÜÊT¼.uÔÇº{jÒtÆóaE\UjxÍOñêÂ×ï©v‹ä[ÜÅÜÖÂ87¼…Ù­Iw—¢ÔğšŸâÕƒ/¤É?I‘\%9ºH¦:wa$Öû¢ñEråtH‘Ü*rl‘Lxõ@šNV+»›&«‘.WP}=årå=¸@n•ÚœÜX ,0i\…W`rQRC=}·Ê$U/E°ËÌÖgÙGU™”C—D®¯óYe~ÏV¥†—e¯|A÷õÅ6âu©#†7%£ØãÜ…(5º,kğêÂWï’bñºÔÑkJ†W™D’ƒ«ÌFç.Œìz§3¼Ê$œ¨2ŠZeR^×?5¤Ê$ìn©2Dº\Á÷5eT™„÷Ø*s¡ÔV×}Ôó{Â~ôó{zôÏï@z¼‚ó=ë.]É=a{Ìh²¯Kı±ªüşÑäqÏ—‰R£kà¯.|íğcàh²¯K?¼¤ïMé.E©á50Å«_¸
ş$Ec•äè¢‘êÜ…‘ğÉò'¯›K5ù“ÄŞiíŸNÉ½ÕÚ?Ÿ’ß;Ç÷·öÓt·uN³¦ç<Óq©ç)¶ƒ™önVñÙ8®ju[=/ÌeÑ‡ÿPÛÿ …p¬Â
endstream
endobj
101 0 obj
<</Filter /FlateDecode
/Length 3054>> stream
xœí\ÛnÉ}çWÌs ÏöıÖ’µÏIäœì`7ÿ¤ªoU=’-»‡’•-‰SìîºêËÑpV¥cúZüû°²Ë`äeŒaùòõôë	ßW&ˆE[—ßşqúÛ–ƒÜ¬ÒASŸGè¯ £\ğß_~Zò‹ß~9ığ“^~ùOÏG½H©÷s’lš_@ÓŸO?¼˜%.Ÿ†’…rÑ~õA*»(½|şzú£Úşiùü¯“ƒ÷?ÿ}
[Ù
|ø&Ğ"	Âå1¤Lİ6w‰M`ò Ÿ>ïn¥]•Y.ıV‰Ú(‘[ËÏ[l½—z+¸Ğâ’¡*È%@€/Ù®÷†¤Ro¡·æní×ÑB]5æcíıgø÷ëIJ·:ü2‹ÄH+ˆUycjõŠBùëöA©¥Zímø* |ˆ²àwFâ?¡ß¹ÆPF7A½|-±¼â…Áú(‘l
6pĞV™6Iæ¢P­Ğqù‚½ƒôÒ¥ñdX½Æ†1B½‰q 	e®”®2@#t•ğ+==ôQØÎkù)² a8µ
£UˆEæBÀÎ
ŒŠÖ×–`.¶ãU†¨¯/¿œ\ôíê¯V­¥¡Æ(qİ¢!Q­s¾Sî"¸àT4ÌL”Y_Ì”yç½ãn»±J”É %ZD»h£ÔhgËK’AşËÊj†s¯šü×k’B»°q“ÌË-H²hªÙRšUÙÜ¹8”dVyîy’yçJÜJŒ’4F·°X‚Ì®Ò;õ$Ó¢ä¯æ'IMNOIb¥k7ì¤t»x=1€´æHuT†8¦a³Jnş0¨3Ï©&ZˆXå´P²c1gÕØ²Ãª¶e‘Õø—Ó?qzKş³B}&HÌ(¿O
¿O
¿O
ÿW“Â_G7-°g”®*J°5zy‡v_™ğƒ´Qçº©B“…q…ñÜ‚Ò{·,5èFP …»‚¯,Å?–S£ ÷I{$<4vš‹Ôƒó2 bL5…) —ÕGé™³İj1-l b-
Ûé).á¨Ñ¦´€°:/@*E[õx#õmUØÂøÚ	\¥©wÑ2Øz­˜Q ëc`› µ+lÙ³ÕÓ$Ã<RHš]£×„˜Àç&¤„Ê·†òLv"È¿<!$jJà1Î¥·´)P#!D3ÄšÑ^ê Öáì§˜d4YŠ.:”:È¢²k]í}.˜‰°v’¬‚øBa~Q¡´ÅMº¡fPyçñw‘°VÄ6G¦By¨mˆO§Ly·U°ÆSf>+Uï†ò}¶½ËEêYxÒEÚ"ùz¢@!©u!U ƒw½äfE x1ªx RµÂ\²§ ªEUc’EyzÔk­"[œ©kMß×Ò’ÌLæÈ©®£©mü¶â10ÿÀ¹·P½„Nfé)à¦;GX¾,®İ¹Î«µU˜¿‡Ÿ |+«dÄ…qµu\‡<€ÖÂw€×?Â÷êƒß¶ÈUn#ŸÉË.s, !;¸•İ²V¬lƒE³^óßíÀ>Æ:‚ët°øEŞÃ‚	H€BÏtìİ
/Ó¢g9®@ó Îp@*˜¥ƒAüq=”„Kı ÈÛN“Ñ“9¡GÃôl8î²óƒ”É'È¤•=ˆ&|ß„òZêP†¯+ê¬.r3æßúŠ—‚ÊÚ®è­ã%ıEö³µ{.z~d}\E[Ñ¿Ÿ"½Ÿìc×¶ÚıRÆ37‘cå,U ½ÕÎ¤ë™b“l1;1“ìµf±ûTl2YâõÌüwW|x*ù2ı¸)~*Çko& ß¿à`ü`£ú0é¡°Â~¡¶ï¿Ñ<ü¨ã0ÙÂÓ¸¤×ê
ì`bOv)î(<¸õæ¸c„ŞugÒ|ëa/óœ@š’ãqBù|Ø;Âs‘óÑÔ\±Ód“(ôîúÊœˆÇŸèÂÆL*B5•T)agÌÁÑÂK§œ’º›S0tÙ	ø `¼ìC !¥Læì5İÓÀ!ñ`¿qª›õòı&ò&ß»V+Ø¡rõr*‹ñºú&*T(	ê2„
#‡PqJ îªåÍ’y3µ^zO?^†‹œc“¡3BÎXé”İäğ%/Ûm)®^=MÌ™V’æ®¦ºíü¿`#¸š:ó³¼ÍòÀæÙ>œÁÎÊÖ{I³t‡º³íæÇLôÌè°ç™)[’¹1ngŞ¸_5Y³©£/œShâ½o59¥wÀ2µšœÙÅ<¬_eğçsø”br^§Óê%ã¯.nNTs.ŞíC¯PlcØÆÔïã7-®—ÛK6ú°%s~ı9±sÕÄ¦˜¸_ÿİ&L\nwÀ<¡U\)%İœœ²êj˜dÛÎ–Åo$ŞVúIñŞ›™öâ}Şî†Z˜µ°CÜÚ!ï´;Mîáh"'§¬=M<~Cñ¶öh4mâı]h²oãb¬¿ÄÅ<æ¬Â¦Y2­®,	„Hí|št<W5µx/Ê‡4BùôKù0]–X[ÎüN¡}8C*oğ¥l{ •88ù8Ú‡tO¦}z§v÷è¸¼°y«ò˜ÎtZT¶ö9—®ş4m½À¿zƒi½ cévÓïY/pB-%ÂŒ~>M\ïèŒÏì¸ ÌYóúoU õ€Æ“?TúÛ(®™Ua5«
=ŸèòâÜÑ+gò‹'[|ïÓÜ“T•á#ûælÃ9FÉõ©TWÆ©>†ärzÏşi¶3ª‡Ü’+ªH}_’ËÚ=Ï¦’\A4Êd°¬îWR®}~¢«©d£*W}PMÁ1ŠÖ¯c*Ë9»çÅ4ü¥UÅŠÙ%åmHiøk%u›¾ÊÛ%û6ŞÊ¹»óV\å‰áñ¼ÕøÉ—[;âg‰Ù0…œœÎÊñøÅ[=·G·vÈ;óx–èx45'§³r<~Cñvï–·"Óç­x†¢îÅ[‘¦Cx«Ş‘cy+¦«ğV­ì¸U‰Ô½éV%‘(ñ8ÎŠtOæ¬z§.şİâœÕDÎ‡sVdì<Î‡ˆ 6úMâ‡òy‡`¤ŞË½MdÉ1÷6m<½ÆüÌ]ù½MdÄÄ{›6İçş¦¸ãÓ\êÇî@cŒXê‘7‰ùg‰9ó1~Ï§©œW˜xXAáHçFÌ¹ÉÉÑ]oÌ¿»Üä¤ÕqÅ„÷Cc.ÛÌ¡l­˜Ù>ØĞ2iïÎöp•C&úÇ³=‡Ÿ`ÉÉé|ßP¼ããù§q>„[;â]”g{G99áñŠ·~<ÿ4&níwöİ²=dÚálÂPÔü½ØÒtÛÓ;r,ÛÃtYFÄ‰w(q¶‡Ô½‰íá‚B|ÛCº'³=½S—øğÃ>˜Fê§0ı–¦ñ€ Â	ùNÈfÉ!äÍÖÓo¼mgöÏ¸ æ¹8gcÚˆ@îúASqƒÓåo>ƒ³ß<gƒ»{28Ü§ƒœÑªº_E9áêÇøyEM¹k‡n:ª¤œVõG•TâqÎ½˜Éã8Èë<şZIñ8İ`C+¦¹7Ó©2Ñ=Ç>	vÖyÏš³ ^99›¥êâ7o)ÏãŒ£‰[;äz<kr8šÈÉÙ,U¿¡x›÷Êã0Óæqº(EÍ½é°ïdxÛ1P‰7}äÛ/uoRweí2	íÓĞÌé¦}ÊG}ğ¹…UaCO{æ¿<O,MxŠø%|®W’iÚÖ¤‡^•[Tºgmû¸ÖVâEkrê{íùcå¹céZºO\·â¶àuyHÓ³föàiıã¦]{ÆùgÒÃ¹n€Ÿ¡P)¶›Š«˜ÔqS¾Sw†$d:m²uoÃÍVŸY¶µóˆº!‚…l™S5ìÃVlìyeã$U¥ï j©‹<ÎÍ
U¤œƒö¢~Ş_!şm»Kë~mï1¦÷ª’ËÍ¢9uÂqÏ7§ß]&±~h™ÿ?V&[lŒ•
2—ÂOBÿ/b/¸û
endstream
endobj
103 0 obj
<</Filter /FlateDecode
/Length 3651>> stream
xœíÙn#¹ñ]_ÑÏ¦—÷Æ²½ÏIä&ÙO€İü?*Åî–š±e2öØ–ªyÔÍª"©™…ôákbğıi&oâ³çŞ»éË×Óo'|.”c“ÔÌO¿ÿãô·?Lÿ¸š¹¦6Ğ¾ƒ|Âï¿ü<Å¿ÿzúég9ıúŸ0õrâ\î— aØ4¾€¦Oo§Ÿ^Õä§·_` €!Ÿ¤­ãBOBNo_OdLê?Moÿ:xşö÷	 Â-j	°`@² p—Çà< dèØÅ€Šƒ¾¼m#®¹w–`Îír±˜„/1_·XRÏåp¡Å%D…ã“_ÂÑ_ïB­½™\¢»ÄŸ]GF2q™§ÜûÏğıÛ‰s3üRGN+€óÆ¨Z+gÔ œ"¾"İ>q¥´p¼«ÀTŞy4xö:ÑßĞo„1›5ô”JN_Óà›ŞñBtá°r60Ğ–'˜Tf<¥“~ú‚½·Ü„ñ¸›­Ä†ŞƒÅ$ˆ2 "†.„Ì0ĞGèÊá™I=-ôØÎJJ0Ça813%…ó	fœÃÎòÚæ–€.¶ä•u†zŸ_~9oË»w|7KÉUmŒ£‘¬:$Â¼6Æ6“$áAaZÂ!aÖXk(ÙÆï˜àŠğaÜ	W™ˆÉ¼ñ·ª¤Ñ‚È%À@~ŠÈaYÂ±Wşû‰´GÈ¬È¸f”¦˜Wƒˆ) Õ,tìœ
0-,¥<À¬1‰o‰Gê½™/¦gnåz€I–ä—å *Š'	1‚Â€¹v²¼y?)Í‰"åQ‰Æ‘é‰nD«
zˆªÊ«MË)¬$6FxN¬±H‡Xm‘"±ñ/§¢{pSü‡^!¿„å‡Søá~8…ÿ+§ğ×Ş°¢é,<\†Ñ ÙWûÄ=×1˜y/`Ájvâ Ì3îÌ :€±øŠ@0¨€wÀQ%@ëõs¸¡aŞ Ípê¢
‚ e™­ç–‚Q¸ŞÌ¥B†  š"Ót2 zˆ–!Õh’SA›( ä y²@íú'pæá{å²šOu€±%€9Lt¥	{€AÎÙ©’` (ÒÌ£5<Îœ ZæoíUQG¯2£xTñVŒ«TÊÖZ„zˆú%fo&<A§Ã*”aÈFVäØ€9$ŠèÚ™™ã>Ê†CLc€ğ>*h9x¡`.0ZK€‚w–¸°€Bäšb°.‰~E´éÆWõŠPÔ.Â1Õ ,Ø2p¦™JX3+‘´«b%,8:ÍEC°‰Õ­	h)_Â 	œYø~ªıÁwsp…à³êD C$8¤n#&ôjgxŒª”é49Q©) ô†²hX:…Ëµs™¢ˆ­A¦H˜ M´¦·Ò¤¬c·d^³Ö°°[U~ƒ—Å°i	«ùXÈ¹™Àfiş¨`Ñ2’»”@*‰;şÌ×áG5Ùç¥şÒæ|ÖÀêÂ±f®0Œc_æà5ù]zÎœÅ>øÛ—ggøym„•çilõ9ş}–i¬­6¯uöZŸ<oP£ø<÷K|¸¥qË8çö"c-´/´íğÓ€/÷1ZÃVÙ%mR{MDÀûúZME˜É‘ŒÀÂçÛXÓô1¥-Çµ#³(?+ltU=²xpl|Ö¨æó¾
Õyº ªÒ‡ãæ÷—ÕÆBKü…±ÚZÉõ¸‘ba+”ä6÷‰œIib™2-[PÑëXà}äMƒQp0j(±,—‘E.À„#¶eöªDw0C{í‘tè]FpğºŞ©Ëız=á5F+.@ÿÑñŒ¯¯ã¦ë„]',íÒuÈW²®”‰bîº)LÆ½à2Fó!Â.VUÇŞW}Ã‹Ålu¢ùõ~ŸšV•Ï¡ıÏÆEiU®ö)¿e9[`ı‘Ğ¨iÁhŒ	PU.CwX€ÎßİÖ-òbí#,F3G,FØdÏDûI¸IÃÑ‚b\ZÊácŠ}‚¥„Å~¡Í›1S¶ÖŒ‡$Ïúãµ¬#M³Ñ.Êv	Ûã‹ÈñªJ|ĞzDüä«RÖ)6ØÙ¢²DYèêø ³0,ÙÅ‚:]#½àP¨OÃŒ]`ı™a|„¥Ú”Äš^Çá.íÌ]¢N7_ïAÜ`ö9}9Şñ;àÒö{+Íw¥•!Ò¯?ƒôØÚâëLyIúŒNdpœ¿ ê‰•§ï¯qä{øûÒ0CaE&xëp(¢yE´–c®˜}Æãû.…#FŸ0HZ>›%çÈlfwtZ®v©–¹-íÔNmª"+•…àTZE‰£ÊÅ‘Ëµ+WZ¨ÒEM(ïS% Âï”¸»É˜+Y€¾\„—Ís
QóJH&~¥ì¥_ñ9wh D43äÿnAJ—D“$¬"Å7a}ç•U/Yé
;y’İ"Q'eq‹‰öJĞë´ffN+3•ÛÈÖAcØsòË²2*ä$^m²5bÑ!Ö=¯ãÛÌà²¼’¹½lgxEP´ìêXKºßTç¸ÊE³b¡ZJloˆR½XÃÙŠ÷SùùìY-7çö4o åóhÓ£•[İ–ê‚NPœSg
Lz5KŸm³%ä)Å3w­ãBd­J¸PÅ(gLˆ_©µ<ÑJòRĞ(b”^ÃºA2§±zæøˆ V±|<uKğcÑaÂeØô |p5sÎÈ/IoŸKÈymE]îÃæªedQ­ó`Õj6DêÜÃª\¸fàGt%ÎfY4‡é’djV`Xk.ìy‘ğWàMZI|¬7Á èJöæMÂæAâ7RÔ ~Cü=ÛåzÑ·Ë‹xwÅ‹ÕîM¢µ—ÉÇ¹<§çÓæCÿÑ<‰7u.Hó%\” ¤² ×•˜#\‰dÕ»U•êJ´ÎŞ¹¡ù	.úŠ%~zNÇ¶Ä¿çJŒŞ@®Ï›Xn÷¼‰9Ì›ÉGêU³Xç&ÄªåTS¾<Œ—‘Ê£«ˆó2F–L åK ãF>|D6 }Ñìø¡µÉfGT1y[|±Ø¥ş¶jŸön=K(ö=*ØQïÔÊuwÛ‡xÚ³ËuÈõ®ÏŞldC”vïšNß¶`í¥€UùêµÏ_ngºÙ	¼ÆB‘Së¶<áGÿü¥ºûŠ¤~¹æ£¿ıbßìnçŠ1VÖõBÜÇJ¶j(ßzøaßmí%ï’ËU„:÷°²dŒD=]6Ê·<ò<AEdÌ†<9O@hJ	¼_•ÊÆD>#ªp6`ME–T¯9—œô&§MDpfTÑÔ^n®cYÙÓJ¥:\oï2ôüşi :CFÆßŒÑ6ÒT™Û* Î¹»4îXUÅä˜ã(Î¬gŠfwïi&Ãá-×A©H–›7æÂÆ!¹w²ÚôLŒ!nrÄ„ä@µİC&zC*}úä™ı&}zütRÔô©9.T%}jYø¨Ù¤€ PG¥?€!YÕÑ¥Õás:9&•Äİ±¿×‰ä€C^”äìÊ!‚½»lUÿóÆ´o?(Q}V×azH<Nšãÿô°B×¡z/°µÏ3©œón±¼97MÎ¨DNyß°gD<ÈòhE°“ Ó—”‘¼Ô¹ƒÏy™ÄĞ=ŒœË`ÆŸâÖŠÈ˜\†$„Æ¡¹ŒáJ‹ıØ\ÆÙ-*nÌeê¶Ì0É)^C2"¹!ÉŒ+™u¤05u¥Œê2s×[;úÖ†ÎĞ‘ÅÏøŞc<Bä1Ş‚…ãÁã‘á‰ñ(¿Gn„íVˆF¤]V$n*eXàÌcdê“ƒ3õ%Í3u:tg¦¾é‘çæğnØÈ’ÉÃ?ÁÚO‹ÈQ~>ÎËÖY¾ÎŸ2AŸÕ£½l\!ì‡ÛPA ,Û« «ÒÙõF†Ó*<êM«rZ”ÛÄû•äüv¾ÑÜ“Š­Ú¥ôJÓ3à‡§K—SÈu>ÓsğÁÅÅIßTC´ÌÒƒL‡’Føl¸tY’Ìİ‰«ï«O4‘¹Çîø,‰º’%k“‚ÈèJc×Ìš`5ìéÑÎ·¯`~Wñm%òˆø¶ş¨±-W%r;€0r<[FŒlÊûïT]ÇÆ¶,ŸÉm,¢Ë‚¤~Xµbrt¬º yd¬J†F	›
 ¥”Å6ûúÎÜ¿î/äcÌÆ+©»÷#…¨6 oªZ®{4õTê.l3|:ö¾Ï@{)˜d‘§TmdôÎı÷vóô¶ÏêÕÁÜ@í»JYÕÇZyÓÉ+ÔöÉAFXo¬’™Æï®@B1^¢çÁîŠà­³´V„ÇŞ;KN{Í«F¹sV÷-¨½("]öõ‚ğ¦3ù4ïÂ/·O/Š¾g;zÃšº¼‰¹xõì+g´Qç{•ü¨®dAÿX—\èp$Ç9™¯$P…~ñ,ÕÖâ4‡‚¯S‚p$%2—” §p²n:D—KqïŸQ;äş™üÛ¬düt-õ»ñ‡ñJßäC¯s9äZk½¾Nuo¨w±¢ø¯•<šs¡Ö?^	ò%÷•ô¸ÉrjËE7Ñ\S-spµÜâM°üéîu"µVq{X‰‹|ëœLñ?Pµ×'’™UÄ‡éùœ‹_µtO]Àü9T“½Ä3†{+¸r¥,Iùyg=8š±h
ÁhC6ùëUR:EZ_v÷Ú|Í¡iïÜÿó¦ÿÊ™K%
endstream
endobj
105 0 obj
<</Filter /FlateDecode
/Length 3829>> stream
xœí]Y·~Ÿ_ÑÏÔæ} íåçÄäÈ±ceÀÎÿRÅ³Øİ3ÃeK«h%­´SÓ$«¾:XUä¬f!}ø51øıa&/â³çŞ»éÓçÓŸ'|_(Ç&©™Ÿşú÷é_›ş ºš¹Gmœ¡}ù„¿ÿùÓ¿ùë·Ó?Éé·ÿ†ù¬—çBàt¿
ÃGã7ğèİóé‡'5ùéùW˜(pÈ'igë¸Ğ“ÓóçÓß“úÇéù÷“÷Ÿ™€ Ü’ –¶$w~ÎA‚C|!¨8éãó6ãšëYpg	çÜ.‹Eø’óõKé¹\Î<qQáøä às<~¼<”ZG3¹dwÉ?»ÌŒdâ"3wyô?à÷Ÿ'ÎÍlğ—š8"-4X¬ äÌQ­VÎhA¸DüûÀ•µJÎ0úªı
°xçy2àÙ[˜ŠşãÖD˜C°YÃH©äô9½ `Øô‚/: C
÷À”›ğÏòD“*ĞŒg¢<Ç¤Ÿ>áhÇ-7a>îf+ñAïÁaEĞ?Bf˜#åğI#-Œøœ•”hÃtbfJ
çÍ8‡ƒ0åµÍO»ø$0¯¬Ë44ûüí§“ñ¶¼zÁW³”\Õ‡‘b4ŠU§Dš×ÆØfqãA#¼"l"MKøEÄAš5Ö*¶ñ€\|ÆpD¤HæoĞFª’F¢—@ı)¢?¤eÇQYù/'ò<Rf€v"óšQšrh^e"§@T³Ğqp(Ğ´°Tò@³Æ$ÜFê½™–@Ó3·†¢h’%ıeıªŠêIJŒ¤0a†ƒ„,/^NÄ@ÊãÄò¬ÄâÈòÄ6£Õ„‹<ÄÔ‰äÕ'
DÄs
”ÄÇæÄ‹vˆ×-ÿtú†7Å?ò÷! €² ¢¼…÷ ğ¾« ğóœ!åieD‰NÙF	  jjø2ˆ£j% äÏm” * å/ IiÛb4Ñ8D.Øèhª†Fk@E·q"Pq"Ò&QŞÎq"½jâD¢5v˜¦l,¶,ŞØvb³ñ$Nã-EîÆ¯BÔıŸÄNºi<?é°Ä#I¤@h#…Â9‘iËH4¯e)”‘«H´e¤@Ú:R u)”Q«H´u¤@ª’ª	VB¾*¡"¾hCE~œÚR–Z]e€Úgf•˜q–ˆÚ{•8F‰úO“zZEúdÖõİ¬Gâé»ˆ÷ĞğŞCÃ÷~îm~Lœ@©³ğx•0Sh~|&Ä qØüx)T¨ø 2=ã.9$@ˆ€’€_‘(±œq™™=2àHsg S"ÎÖ¢òâ6h ìd¶ÛLB•z3kTE"Sx¦éä@ô³àà©#B2àì‡2DêÏ‹DñZbD"ŒOÔÚKKô³ÓÌLu!°~º’šğ4¢Æª¬°Æƒá·È$ÈbMW H4€Í"ª+[GWÔUª²(?U¯•ój UÂûADÓÛ¿&¼Åd2­JD@#p-	Ê8Ü˜™ã>ªV³ÔÉÌìahWÀà& ô’@•[áQ§…KFP—Ä´
|B_Í« ÜË1ÕL!À´4 Ó,&¬™•HfVù‚œæ¢‘AXâêFÚD´•08‘
z/§:ˆz¶\b Ë« l ÖÕÉÆ2ïÀ#‡…U'		4¡¹ÉxZŒ²XX /a22k‚,PtÖ°RÔK˜¦ö’…[ÛP6¯]Û»Æñ/±˜/µ”ZO…¦3»VMÛüDY	Q"·±/iØ.”‚/ÿÕ<Ò»ğşcn]ÏŞ0Hæ4î pŠÀ%1Ÿˆ¬¹à‰°YsÙ0Îp<ÎM-m:µhñhšöçğ5öá§ ­áËÁ÷áë¾ <¥]Äg(¦{Æ°GÊó«ñFß6ŠÙ9o)$hİ-~]x;İ…waSÃ9aZ4AÆå"£KÚyV9¸¼(¼–µƒü (8¦ŸK¡îÎ;SÙ8:lçÌ,$ä#¤CŸµ»•Œ÷$°©æ¥]è'AV+_#äMR$MírÑñÚSL×ØUµgÈ­`4ÌËµöøÃ5W•[6Õçá
öí¾ˆºíñç<M©ÙE?¦+tqT³oãèµ1ˆp^8Ñ2ššZºaé1½^¬½Ì®0‚¼ÉÇ‹Íë>Äª-‘©Á_Dò“à²>ú{J)…Lşó±úQˆŠÑ—ØÇ»‘Â´’»k÷W,Cê­tÚ“7ÙŞÇH`A°Ñù˜bJH% H|ˆc00åñÌƒr†*$n]còÔTõ-„AŠ0 ›zŠÿ†÷İP8´PP&£T:b­Ó+FSÈWº­¶ØÊiñlåı ßÓŞA±)¹\¨´Ë‹ âÿZ™`];˜ÓÓÈŒOë Û°z-ãN±,bI9…‘1‰!ÉÚˆŒCCì#ú‹ªº†&†ÎnIqCbˆšl\RH27¢¹!I¡+u¤ƒµ @u¹¹c»7Ëk© 4%;¥Ów±ãıw°w!Ù»¿…½{<ÍŞ]¦?hï®x¯÷n­ÄRm”3† » ]ˆèš»<¿Á{ÈU?A¿Y7ë|şA&wàõùòÌ›ë[]àŞoÌû´±®u®xZ„ààJiÌ{)®L²¯ûTwÈH+k¤ë sAÚ¡¦Xiç)u%Ì£ç´ıd»‚ìÙ’6Pè‰ø:H–5”¤)¯tFì“XüS¬v
¤÷uñdèmTê•“£+õ…Ì#+u2ug¥¾´±œg¯	^ázì¥­ş2V‘H‘<K³u¤ÁïuGßËŞÒæQ„à±6vd×:Æª9e!T‡CC³W½¡9‡Õ¬ĞøLeAI†(—õ…óÕs)<kÒ·ç·¡u@Üš+²]‘ÉğÒ¹#loF#â^Áe©6©kwò*÷UâF½J¼®=øLf!Ô…Ò;oC³Oz&S~&Cdì)ãhÕNáé²»¿Œûæê¦*äuSı­ÖL\•nŞPÀÌ± iW0ÈŞVXîw²âGt>»¯ó`Üm‡ñ¹måäèÜv!óÈÜ–L65u@O)›sõ)ıyM¾{}ã˜“6¾XE½–“†¶Gö~ZæŞˆVN2Æ!
İ5P*sFbûºÕ lmH×•òEL£‡$—|NWê*W³LIµÍ¸‰} «ú®Y‘bÖµ§˜¡î^›Ó€Æ¦¡ŞÌŒëÛTfÇä5L•—â0Hx{3g¹uúXhà’¾âh_«AÁ‡jP9_®Øa~†!m¦ƒ‘gxa[É0-†„2pnÙàÅ€dJÇf§ßOÄÇû/–‘éjKexÌY¼›â£Ùj^½îğ–=×é‡)^è…
w:î%v`¹©Â!,·TØu«uuıí_t÷ºë}³ÄÂÉÑeÌBæ‘e™Ë—„1µT	B=v9¯åH~V¹jø«ÒeTI®ªJµdûZI.3¬`ì15Çúîm‘4Öµ½!´ñîí÷ËÈuËÊü¸~~øoaóV›f²öÀCëÒ?$&ÉVWnl™9¾Á|ˆDwƒ¢†a¦t$È=Û”r‹»¾Ø!n»£;~›ªœ½M-d¹M‘©Ñ8ÒİeÎtÊdíŒewÛí®	Ò±{H.æ8w¢<´ÃJ«lW÷2¬™²EŠ}§lN}½S¶ºöÁ»™Zº}C»Yaş˜İ¬Áæ[ØÍÆãAw³j’‡ìfmXâˆİLí:}mv3µïôÕ™ÛN_ØÍ
'‡ïf­ÌCw3ÃöîfbÛEéV®¿ØºƒmŞl¶ƒUN#‰HW71+Šš}g˜Îöa²‡•µÇˆ4{XYçú‘ˆ–ù …"Ó…¤+‡m•“Ã=º•y¨G×©Ñ£işÉHşyé„wØçÉ§ã	[W?H3¿ïT,Æÿıåœ*ä—sZßjvF>Ôp ôCuúc>Ô@ğ™ŸÑ$R•vy‘Üw„äõ¾Î¹·ç:çÍíh–n£¤ºX‰µ—†¸gŠ««o&†ºğÛıØñ—êJÃêT¯ÂÇ	…^rGò´Çˆ®6mgâˆ;¢°}­åå°(‘ÓàÙaşü$‘·ë¨´9­¡Hu˜^æ~iáäà´f)óÀ´†Nà¸;‘¦—Ğè½ø¼3ù”şähğÁ­³ĞÖˆ'A”Å«)å1ò4u™•\×Ë¯4•8¯f£ãŒa¥” Ó_m‡ÑJÄ0@š\,ßs¯?>~£õ9›uT™æÂyÀ«7\äŸÖà3êâşÈK¾„ÜÅ!Lîãª…v÷h6ü«¯kxùÜPM“»ÌGéÚà'³t„AŠ&í´#S§Ò`“ù‹AÅ”ëÕ{mÂtÚ„9Şû‹Çy]bä¥³P3.dçÿµJ§üïî×|ÿ0ŸOå×R½÷ƒÔKÊ¯Q>_»ïG(·	)Ü_tzçö:½î7†C‚8}b¨U4NïÖ­­‘[~UÃ![ş÷—¬‚3{«U\Û
6;È*ª‡YY¢§@­!ìSˆØşÂğYé˜ú“û¥† øãur«„ÎM~„@¾Q.qĞ†º«ß—Ê4÷QŸR…úÀÖÍø\¥ÊvŞå§ĞËØÜĞÏU/#U.<+óxÊ‡!GèëŸõtí0ÓÃTåQø»lP5?ZÂÅŞß°âÜ™f«U9iŒÑa}¢˜³-Íƒ
İ1±ÍúÒ¿ "Mtñó1É=	H] ºs×^¿T9äß3U¤¡ ãÖœJXŠZÊ‚ëTŞRµõTlcM?ÚO©(CÑÿ{HôŠVºâÜe·]‰Pg}4((°’öG¦<ÒÄ®+@N¨sW€,8ÆF„‰4CsÊz^Ü Ö°>w·å–Ü}oŞ>`}Hß ¬÷•ÈÂî+„ß—ÛK^2î/z
û\®+•eüşÁÌÁ™
endstream
endobj
107 0 obj
<</Filter /FlateDecode
/Length 3535>> stream
xœí\Û·}Ÿ¯èç nó~‚ ’VösâòJì Ø5`çÿT‘,V{wgFZ­4RdmŸi’Åºr¨ìÎ×ök3ğû‡]<–`÷jk-Û§ÇÓ'üÜ…b6Mİşü÷éŸÙ~<ì6Á«¹÷ Ÿ ¡İğ÷?~Şúşvúñg¿ıö¿Ö_®~³Ö9ìî×†|µÿ ¯¾¿?ıøSØêvÿ+tÔ,´›Ï{.ÖÅÍùíşñôWc|üÛvÿßS‚ÏïÿµàÊ
„ÈÈğ¦åù>¬m€Ÿ@ìMêBïôãıÓ†GwgK–Û¼â–AìjùñuöÖ¯À3o<g¨+v+ààçl|ÿrk*·6~5wµß¼lŒ7î2cş¿ÿ8Y›ö„¿ÂfÑÓ.BÆ:ğ|‚>8kı„CôŸD³,$x¬»‡ægØAÊ—jGï5C_ò¿ĞîBÎìZ†ä¶GzğÉoø°KCÜ&áÉoæCÃR5n¾U°}ÂÖÅf›zvÏ.ã›µBÉ(D€,Tºs0¯Acø\ĞÛB£RğÅì3Äh`jßÁ`Á»RÑ¬3½	ã›	>Í…0Ì|úñÓ)Õ<Ÿği÷Ş~‘¯¢KÄjL)«ÁS-»K®a&bÑÃ/1ÄrÊ9©y§Zw(x„‡³ÅáG„¼©©*#|ŠNÄ¦aÃ bˆE¹·¢x8É÷öáÊ&ûE,…¨,@¬Fêk˜’ß]ìiFˆÅf>Ï±œÒğy	ÑZÓ&½PzNÊïˆy3"8#„hğa“qlXë‘Úµ$õóáá$s„^—¹DİÊ¬cd~’©"iF2ßyî¢0ÈI²~È™²ÒØë²&)>²v)¢Ò?şƒ$Q¶ş?äú¹Ñ
„xåF7j¸QÃwH¿\¡†=$c˜+BqW„bÑ‘Š+óAj€#® Í’+
ğ¡ò`Îkª¹’9€›tĞ KPƒš*]©¢a*úDıISEÇT".UÊÎÁUr3UŒé¨r¡i«ºş‘å7¼¨êıvi¦h‘	E1EprCq‚)0üš) 90b+S VCÕL‘Œ=0b+S vd
DW¦HÆ˜±#S ¼"ŠM¢À§IıA½.3iô*S‡—ÉI†Š¦ùÈ\ç™‹¢ ÉÚ!WÊ*cŸËz¤èÈº¥(Š*¿JBÜháF7Zø^háóåCQ;y"9³ğD²õ°Õ@lİj ÖóVÍÕBjxIˆ„dµë [i"YH‹êM Vì3ÀDWšhX§‰ş#ÑDÒ4Ñ1•…£K•¯8xµM™ªÆtT­Ğ´UQÿÈÚëNT5:½­ªyÄEUıˆßägK`ğ5K r`	ÄV–@ìÀ9–K ¶²bG–@te‰ë%óÆ.,èÂš,O“%úƒf	z]&RïUï2úø+M¥"‡iB2×yê¢(ÈG²tÈ—²ÈØé²)<²l)Œ¢È¯R7V¸±Â¾Vø|ñPjdšÈ9/4q=Ğb+M v<§Ì9.4ÈJˆ­4‘s8ì1[÷ˆ÷ˆ®4Ñ°NıG¢‰ş¤i¢c*G—*açà*µ‡™ªÆtT±Ğ´UUÿÈâëNTE:½­ÊyÄE•ıˆß$†œM`ğ5M r 	ÄVš@ìpFYj‚ÔŠ&‹Î«™#–“[hQ¢Ròeo¯4Øq‹èzFÙ°Éø4y¢?h ×e&Q·2çØ ™dªHbš‘Lv»¨
r’¬r¦¬²æõOP|dİRE•_¥n´p£…-|/´ğË¥·/¶ßOÔİU›Ú1Y»eñ(0lö0Ÿ±¿»¬İ«ÆÄì^d`a·~±jl#ƒƒt·	R+ø¸$pA„Îm‚„¿
dHh#v +½†=W›	Â0¢Ñı õº‰Ü5@uwÖTeƒóÜ	#¬ORq€9+‰õ,¢gòÎƒÂÒn)­¯Ñ?ßs İË–@d`&Áç>­ar¨f76@©ò¼K.Ô†éw,6O’—ÃØ+¹-{œÇàØHk8Šl7G›çwÌÌ3Ìgğ’YÂOÆ-G9Ó7ªôl±Ğ¬Ez7q7ÅBı[HbFbjC%Ytd«‡¾pd,°kÀVÓ7˜ïª*º‚/vG8ë)¦»œƒ¤è4İå\†º/&pK‡œ_êß¡‡I$qµ¾uÒd—+Î-Ê©,·é·vã™\ôpâv°ì5ù‚	Cı÷/H„%@7@·ÁÔŞã°9$ØÄúÚ›cf‹8“ˆ<fYMG…YVÓ›¢%9]0££L™qFsNğäyBtÍõ¯ïŸõÿ W¢èÑoˆÚõ5ˆÔ¤¼ÀÚWı0Ã~ƒ-|À›ƒğwÁ«o°œ™şwÃ!÷#ü$b"ğ¿™—Ûö€®?Ö~ER=ÓMÉãØ6 fpQY€ÃûÒGC+b£g¶
BmBŸaá°ÜŞuÌÄiázÆJoİ+½õÚÌê^àÍpık÷)U3¦Y‹äãxı†¿!í•ÿÑ->ï—¸}üÒ¸@–&S}³mi¼–W;O»e˜…¹›½×d@¿GEPğVÛó¯àóc8ãÛ<ŠÄ–W0ßY§-¿,®>Š¸Æ(ê*÷8‹÷Ù´ÃUŞXÔìr86ïs”PH%ÄoQC1Äİ†ªÔPƒ•ŠÁí!Æ˜•Áqyšk8,?md^é	‘‚ˆ0©ˆc}Áı³‘–°fa›YÛğÜ$Ö} uùêAa £)^è¢j°Š¯RUĞ­¦•¨ÔE‰$…l….B¬ÀÊ„.ê˜ÖE„I]ÄmÙ÷<GIZÃñd»9î<¿cÎuQBCê¢˜ÉNÁZíJÂƒó¹¦FX}MNÁ‰Õ7&!–(µ ¨¨´QLøÅ+/øıYê¢HU4ÚL}!úJD05‹0uj1¥©hêR©ÏFÛÊlWº÷;ÁÖàvP‹.*¸9-!%¡‹«mÌ¨]¡MÕ.X§ErµèzÆD1£'ÌÙ0§uÈo¨ˆâdvZe¿²PwÆ÷u0ª•ö¬ºŸƒ}áãÀÒX%<¯ˆÍŸó°=~ÃÔIb*gu^V:)^¹Æ¹À…Ø£İ˜İXO/[3UX4_´!†ëŞÏşEğ…«A0©ÏdÔò©òhá®Ç½ÔFvœ'Oåå”y÷J¹â€VD½h3qˆ‘ÊsÈÒ±Ÿé©ÅµWÚŒFE·ıëÁÿ|èd5…Q9á§îÉfêWå«x'š^ğÚÒ<ñ|.Õ#€<Ñõ—ÈC	·/ò°Âe–‡Oj«–‡ˆ–‡5û=›UVX¶!¤<¬cí‚G¬¦S±¸`50!³fÿB	K„t›6‰7ç&±î)ÉWrTúÀ
Ù]ª´ÇXˆSª‹BfSjŠB"ˆwÊÚ¿…à£CµDTˆ¢©8¬äAÄ¹¦4H²ñâ¬”§yÌ£LDM°/2(É´R Ù£×BŒß½ÓB±‚kB]„"H˜€Š4I–Jq R*HjEj6E—è{Ê3eÄrÂ\>@óšÊpz@ÊEr•”‹€ù½øãóœÎd–¢#€j¡¯#À0U”VB2ZßU[RÍÓDÏGŒ|ìèYÃòé¤h>O1Å8|Ş©lâ£Qa¿L”9ÓCö|C	™¦0x;	Éc^$!‡ iÇi´˜Å¹¾°½ªDtÕ´znÉBF£t¥ØJs‰#ø1Ğ²ëLÂXÅÑ–ğî­â€.=š{VªCy‘jKOˆ‡#QE"½Y$æ˜UCæQHß"lîU‘àfE"ƒHa^jJ’f9*‡ÃeqHÙ7U]>‹/|–H¥ÎhÿÇ¼í€>ôÓjœM¯±§m_b‡v‚Ì]_ègoŞh£Ç#aãf–ùk8¢Ûr[lê^Ê ¹½ùj_ªó_ÚâœIÖ‹¶?!â¥“Öa¿hûS<ŞªP×æw‰Rşâ 'Ê»!Åf”‹Õø¯D¡Äƒ¾-€ÿ¬ÓZc­¼/Ú¥”óóT“Eÿ<ÖäÍÁ8×ä-Äì\n7„!rk2–›˜9=Ò×¬Œuw=hFtøÏ»y‚øµTiÏø?}qz÷µ¿ƒ²Lróƒ~s+÷>[6?S»ŸÙVø~!Â$¬v‹ĞÏù²æ‰}Oiû1µí	s³!1?Z¼XÁúï2TPúJKãUëLöêò ìuÁ”åö İf:/8Å/nğŞ`6æ=„„÷ÊŞ›Ûy#fÉÛÀÛ±‰;î©-„üR²Ü ›‘™¢´\·ã°j÷Sğ¢Rl»ï9ÁâèĞ`:¢Ì/]„ËÊüÖE¸v6à!8VÂ*-³„&·fÎ7Üò”¹Dª­Eße®§i0ş×¾gàÀ/´ƒ`¯İ!ÑáSÓxİµXŒôŒ0÷ìÚfâÔ*åJ­RæZxØœ	ŞÛN‰œk·Uo<6ùlğ€=º˜+OÈ’C>¼êıT.¸ƒpqí¾Æñ|»§Ñ'?£ƒùùçİkì¶B<$¿t¸&ùÏîÑ²ZS'µæÿû†—ï
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
xœÕY{\TÕ¾ÿ­õÛ{öÌ030 †Ç æñ•ÙHj¾2T"Ô0Q@0Å÷Lñ¢I¦¤“¯<t2¢â#3#Ëˆ{:)ÛíiÙ›ìq-aq{3V§Îıë~î^¬ÙßµÖoıÖú=Öo­½  ú‘ FL¹«ğÅ«ß0ÕÚï–2ê	×ÀTî z÷¤>®şù´@É¡öÔ™s3òÁ#©|†Ê=g-p@nø *7Q‘?kîü~E³T†'geæƒB	Œ;©lš5gIöòySoğY`““•‘i¶İYOåQÔŞ?‡*Ì{•Ó Á¯S96gî‚Å¹«}VQYãğ9y33v~]¹ˆø ös3çK§uóBûQÙ1/cnÖö—?|Ê) ü“ü¼ÂmÅ0 |ˆÚ_•«òÁğû dU&Uğúmûş®¾/œíné|«-Fø>‡dbå=µ…—â¦SßFĞßøt”Yßú0_â[ôçtª*­úîÄ7ğ¸©~Êå‚_0p½ŒğÎ®İ¤fy0Ä“]K`l„‡`TÀ.Øûàœ€sğ&¼_ÂŒ3_Êâ˜‹ecX*›Á²Ùl6°•l#«`ûØv‚co²÷Ù—ìGÎ¹/åqÜÅ‡ò1<•ÏàÙ|6ŸÇøJ¾‘Wğ}ü?ÁÏñdšW>å­”«)¿€äJy¼6GnÚ¥ŒmLÖğnÂc¼¸’ğXc2º	UÎ3ş¤Õ#|—×ïÅÇ	ßíÅ''{ñIÂ¼øá‰^ü<áI^|špJ;6¥qïiŸƒyáT/¾‹ğ½^<pš1™¿J…÷)_%yŒíòXó”òàÉÆg5œOxŠÏ'<Õ‹h¼ûÚÇ³N÷â„§yñBÂ÷{qáé^¼ˆp†/&<Ã‹—éÅK	gzñ2ÂY^¼œp¶¯ <Ë‹WÎñâU„s½x5áÙ^\¬*øÓp—cÁã©@1ƒÓšã^{†ÉïZ&='<Ñ‹#å¯-“ŒÏh¸Õßë­ïK8Í‹§NñâtÂ÷xñıÔ7UëKŠ6ÿMõmÃBŠ3ÏA7B[€™Ÿ%†
¯ç£¹¶“æX'ÍÑ_Ñœì¤9ÑIs\£™ßIsZ£É&šç5š•Dsê&Ùü¢FCò›Ïj4;‰æŒ†6ŞT÷‚Öo·‡ûÕ~zß¯¶è½1‹8¾ü;ë~‡ãK7s4şÜÁ‘ĞÑ|@ã˜G½Ïi½7Ú¯õÓÑ›´ ¿«N²ÃïÊÎ¥CP{{[nÖ¨½½r;Ô™Ó¯Cm!ÔÑ’¤¶HTGˆ~	u´¨#vã©ô;_m!ôG-œâ»¨;ßPJÜ”¦ÁtŒ?“nÓ.S%èMGM§ÁÇ<Ö<læíæ
¶æYKÀNL4·$˜ïe
3…›"M}L}MSMé&ÕfLòe[A¦™'ÈR1¢ıÿ„lîO3ğÑ!ê%Î%øÕ“œ="ÜmôèlÂÆv)sÙÇÓµ}ĞÖéÄ†²~™ö– X«W[ ­MËÔÂ¡ê)½UPÉQ)[Ó@=xx¬……Tó«gx/ª;ßÂ¢,…z¬’€ªx›t•¥ÀsÄc³±AŠNi¼ôœ4Qª•>“`€T(5HÓ¥B–€ûäTùåAø2Éy"¡–} …p¿À<%—|álÀ*ø„FQ¥¯‡28 Ëh.6–«ø2>‘j^‘hÚyÔŞÀö°4»l4ÂN”ø(ØÃI®zøÖ`
§3&ğlšÿ+Ä«úï‚B‰öifÁ{PÍÆš¡ı†c/¹QKßÂ*9èju6%†FQ5vˆ½ÄštÛÁğ>œï°µRŒtXeíÀéPF¼w©}tÙl	É®¦e*w¾HšÎªàiº2ƒx¿¬JDc>Ç'’DÙpŠò"…dº•­Å4Sµ5”1RêO”$5@&ÂlBËh®^XeÄI“W7@ş‘zVJ—Hæ2¶…ÿ8ºC¶t…tM.A{8St²„œAO‡¥š;GgV»'¤9^Õ«ç¯Š‹â¨†äjóGm[[rš&O®–íÕèÔWKÎ˜KÿªñR¯c“ÓÕ­#†{¹˜>œê&¥TKTMõ#†kmê Õ²“şFO¯vÌÌql´lŒ¼Ñ’5¸W»_ë“çª¾ı§©?L…Çà"›Ä^á±|¿BŞU)é~•Öhé¬ôİÍI×™~úó¤ş›tP[y|Zí¡p¥ûı~C~€H-FÃ…·Ç_ëx_{«eœïdÃ» ÙÎÕ›-*¤lù É©@¨Û$]İu¦—WQ(èSw±©/X.6]lŠ°FYQÖ¨l	Z
1¬åQ¡øşô}®;ı­î# ˆ‡õ¬á,‚%KõíÓ? !0æ„PçØ–Äkè´ŠĞËmƒP:ÃñPLâ{¡X¢Š}ê¢¯6Å“Ñ‹üµš'G³ÃõU­?UÉ?ÏUg]Úö±TFëÅº@Œ;@çñ©Üs°ÁîöÀ°`ÿª:ûËW›,WâY4·Zü\şVïê«b¢Õ_¾©ò±Çèï±Ç®3ƒ¸vıº¸Ær²h¯Sn X?–à…b(…l[Â–²-ê.u‰¢ı’Ænw`z$î‘‹ğô‘:;B$ó±\[í—’vœˆİ'7Õµ«ÄuUU(	H‚=ç‡~Oe•	Ö¨À(ÁÆˆGYÖklLË*©pTí¨æÆ*b@+HCÛa»kHhÛ­²VY–’,[6{låER°93Ú»XPni[˜2¶:(eêØj[ÊTš	¶8™ìzæŒÕw67¨[şšUÛ-Ö.ƒhnn×=Rªœª,•–ÊEa¥!
ÅÙ)”œ}é††-°Ó1=¤$´$¬Ä~‡YÓ!İIB$ö‡CYb¿¸˜h’8”%¸¤@›NÑ÷[Æ‘2îzbİı/½˜ö9³˜"®VUU-båƒç>2zQEÒ¯÷u}~ö¾ƒùáâ+’¾’ì]HÒwƒ|wo0®3D®sxÍÃvİãØS®Û¸¿{= ĞbsXìh‹4èº«JJéß ÉO
¸ÚDRªÎÖtùêå&Ë§W,Z"­Ä3·!3"#2Ã‘%A:‹`6)*:®kb	ÒŸ¤êÁÛÁMâáíåûÅâói¯ÌNyuîéW<rtÇı;'.(<?ùSfz‘u[ßûŞé|©¯«¢ìÁ‡å.‹{ÎáøGÍò'U¿Î$+ Ÿâ`†bw83£ÍI€>ŠGfXl`&#ØuzÉäkywlµ	fÖ3©‚]R×ä²ªv½|qH“‹dÑ+'ãWMz‹Ü£`2äÂ"ú¼R‚Xˆc=°?Ïî6İmN¥¯¨…l)®ef2¥Ea‚•°5Æ•ˆ:Á™Hç[§ÉÎ–±¡%á°ğ°é/‘…ö…2iæá0Í#…*Öu–ğPbóX6˜¹ŠÍ›•]ìÌˆv0Zt–v£],êô½«Å¢®2‘¥îŠº€ÕLæuíÖ	 ÿ²ª:‡@ÜdÕïaH«§gZÏf+.Šo¦½”3åÌO½öÚSO‘«Ä6??qåËïÄG}ßø£••GcãHÛe4û
-ÄBš;6@æu&ğé<ö ƒiCt¹}³Óm°‡DØ1*2ÌI†œè²b.·\şÅ}Ü6:å°Ş€R½\¯#¹k"x:KgÑº@[Pû\Y`oÍ±C‡¢\AüÀú½{×Sf†q»Ç½zÁïÖš.1Y|û‘hWX2·o=±ïñ“'ßw‚/©ß‹oîMß|õ©øRP3ØÁ5B&oÊ!›è`¦;X¶räh•(^Èd”‘ItŠ¥åõ:«ºúü&ìªJ{671S@!YœìöOãL‡¡ò y”<«¡Z§·aX‹:ŒgZ?ºÀDk‚Ü˜Ú\,÷PÏ‡›H¿›4ıÆ@¸Ãí&ívÕy"zyüË#6wİlŠ½Åk÷3Pô¦îoi©kºZ×¤)¶c­j¥A´HoP¦³7ÅšØWd´å›Ø¯@yß´õàÁ­[KÊ¡íıDyñ¶ıâÚµkâÚQåkJ¶o/YSÎ_ŞUZºk÷ºÒ]©šÕÏ¾ñÆ³«kÑçÊŞşüó·ËÎ±Œ%%(“Ç“D¥$Q°æ11Jd[!ãAÉ‚"=–ò ÍNÅn
ˆ€èh»Ysš~Çô©ø¡Ã_‚êBÎ†	;c?~6¢.R©ò?åÿ…?’ÇĞ|Û?À—|ûAB»—DÇ±±H—ÆU%?\3çCqY>bÈ¬âñÉ¸J6ÔëK‘ä%ÌÌüSïc~_}Ê‚´íl¯˜Áéğ$5úXÔ{(-úá¬{X»puaV#ÁÊ)Úxtj¥ÁŠF½Ú@ñIÙ¡F'Ù §ó¸zÊ3ÈFÚÿêº¨5äòÅ¦X¤m2/ı×î¦âÉÑ5céî$?æÇı?½¤AäÃf0(LÏuh‚XOei<Ù4‹åğÅ¬ˆ/Çi‘²X_ÊÖóÕ¦üQ¬º´‡/õä€QÃO‰+Ü)–}Â½¹¾õşõ²okiîÁV‰b’÷<I^M’ëÁ
½İ°ÃPÌvXôÜb9Äì»Aò×Nä‡ÚZQ7Íšé4YfõZÅ¥½»3¶ı*Kd‘â’¨Il/«a"G$‹¹ÏõE,˜õf=Y—Câ±Z¬´´htZ´:hlİ‰ï€bıé)£Ì
ÅKÉDc».ÖÕ©7iššH3­ÅBo>Õ­¡ü•ÖAü§–¡j¨YÕúqU;w]$q7Áî~hUô
·2®W_ÈF™ÖhH2*õOë}È†d@Ù¨³KC4¸™oQwKÕ’êşÒåSjÔ{ãEM¾¯j¼TTgàÆ@nSŒq<Nq(qF‡±Ÿ’hÌåËù2e‰q5/QJŒ[yÄ|0€…aë‰]õİıØLÕO6dégŠôKÈ[pÛ6-ÂIi/¢0c9Ïz±lëõ²XU/VÕÉ-zü©¹‡ÙBŸ Í—¼V¥¨tjzÆH¾‰F%”­’„IôáˆRàƒm‡¹ØG’uh5€=ÈW6†„HÖÛmF»I
W5Oaˆ„¶¶[~ˆz|ó¤¦Ã¥vfªqGhî»4€É 3™V‘!Ùxv‘œàdN‡]uqJœ>ÎàˆèÏúó‘l$Ï‘JåEëuë•ºJdºvğèƒ½Y¦î¿5º‘³µ¯|Ü2lÙĞ†·_³iñ»¯±W´¬iİ ¶íØ±Ÿ
ÚºRä°U3Z7Èoıç–üîÖ+¥kÖ¬Õî(nMÑÙh­Ûa ;$ô8øÚËúÍ¾µìš"èùVŸáš·»\ªÇ]Vcpİ•ø£Ó#VGx"PóykL¢•èXxÙ‘÷ÕÖ~fy}´Õ/¦õ•'¶m;|xÛ¶'ğ(ŸösÓáÌ6œé)ÏõŸ}VO™¼”Nß¬Ñ0Å§ó7û.\	4•†;°6ìTˆE«Ÿ^¯K¶êı’íÁúĞ‘1šiZÈ5µ“ì!—¯jîéOşéˆMÍİë¡ôBì±m±š·ºİ’:Ûƒç !Pk”º8SòôéãË/X´åĞñã·W/Yú$nX^ôÃG­÷ñ=W>ĞZÊ÷ìÛıÂşÖRiú‘Y3–«ßRô}£Ìá ¾âÚ[Í|'{ï{~y&HÚGû§×¦_ßµü{õ{‡×gwRÊ—(WP®¤œIyå2Ê‡)o¢\üG¼ä%`éÀô%w^öU×Ì¿~tŸı¶].ûã>ÿî#Û`şŸÑ(õä'ªV'`
ô€Šiê®õ¨úE+ò z«w8¾p¤S÷;Ù^/fàÃî¼ƒ“ØÖ›Æê¥°&ö ëÀÈ–ª7\’ÅÃ/fı¼X½1èéÅxC½t–é¼`óbz1Ã!fC¤ÂB˜DïyPH8
èyTv€zC€$*çÁ7õqtöºƒÚòa	õÌ…Y¤›Ú]åLè®qˆ§”@hQ¨÷„¹Ô^H¹€xeÀ\š¹FŸ™4–†ÁJ˜ØÉ«P+eÑ[[ıf¥ñßµç¨)4R5[“k–6êó¿ñfégm†Æ-Kë‘¡Iä .ªæò‰fñÍ%:õÏ£Ñ3´6ãğ¬Ù©'eÌ+LÍ*(ÌÍ›çpõN”—÷@{‹Cmº#/IAî¬œn3»;\ññ	KI¹
deÌíé=ofoÇ°9sUªBÇÄ¬Â¬‚¢¬ÌŞÆßtí¯vMÉ(š;;oŞ,GRFÎ¿èè~fNÆ¼YY…Œ‚,Gî<GşÂsrg:2óæfäÎ3¶û­ö´­ÔşŸö›§–¯v·]ØlÃŸø“¯Uà¾øƒÀ«ÿÛ‰ßûâwø­¿Ù8LşFà•
üº›šñ«füRàƒñó$üLà§.üäò$ù“
¼L„—'áÇõ‘?nÆúà%
üÀ…ïÛğ½
|Wà;şø_+ğí“øŸß"ò·V`ãÅ;åÆxñN¼ğf˜|Aà›aøoü»ÀÿØP¯×GÈ¯¬À×\x^à¹µVùœ_Â:/	<+ğEg¾ ğ´ÀçxRà	+_ç”¬=vR®xìhº|ì$[-ı›S>šînÃ£néoN|Nà³X#ğÕŸx$ŸòÅ¿>é”ÿš‰OVùËO:±ÊÿB“şK3ø„ÀCúãû÷ùÊû]¸ÏÏD‘x*p¯À=™ä=3aåî¹2wï²È»Cp—5âNT˜åGV˜quÚQo÷•î†Û}q[3–o=)—ÜZ–.o=‰[WKe9å²t,sK9q‹ÀÍ›zË›nêIÌÃpÃzyƒ×û`)U”fâ:ÒÔ:'®µâƒ×”Xå5K¬X,pµÀUİm+W¬W
\±—gâ²”@y™—
\"p±/.2a‘
\ĞŒ…ÍXĞŒó›1_`ÀyçDág[“äÙ“0W`Î
œE…lY3Î8C`Æ`œŞŒÓL˜.pªÀ)'§åÉÍ˜fÄ{ƒBä{]˜*ğù$L	ÄIÌ"O
Æ‰6œ0&@ 0Ùï8ş.‹<^à]'p,µŒ8f´E€£ÃÍòh2ãGVàˆ
.ğŞK¾£“Nâ°±èx»À¡·ùËCmxÛ?ù6r«YânóÃ[Í8Xà ØäÍ8 ¿E`Ãş‰>r&ú`¿L0£«¯ìØ×ãûøÈñfìãƒ½{äŞìeÀ.ìq‹Sî‘‰·t÷—oqbwìÖÕ)w†]çô‘ãüĞéƒ±cFûaÉåLŒlÆ!"ÃÍh'Ú†5ch†P!D`p&v!MuD‚B0P M`€@"ğh%Y­IhY~™è+Ğl
’ÍMDm
BFê‰L/P±¡.%j”È‘jQĞ‘Ş"ó^È,Y-Ë\»…õøÿğÀÿõşğ	ÿ¢S}
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
xœ]‘Íj…0…÷yŠYŞ..j®Ú.D¸h.úCm@“Ñj1wáÛ7N¬…ø˜sæ$“¨jêF+Ñ›E‹¥¥Åe¾YĞã¨4K8H%ÜNtŠ©3,òæv]NfV Ñ»¯.Î®pºÊ¹Ç;½Z‰VéNŸUë¹½ój1+K8øNÏyé&„ˆlçFúºrëÙ{ş«AàÄI¸˜%.¦h;="+b¿J(ü*jù¯W?ˆ¯Î’úâÕqÌãr#¥	Ñ%TÊˆ2N”Şå)Q”yM™{wş›u\-IH–T!ó1d†Nü!„¥{‹`Ú^°Mú¸Yë'CßA#Ù†¡4?ff³¹¶ı{A
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
xœì½y|Å7\Õ=}LÓİÓÓsj.Í¡ctyF‡ei$K²d[–äS¶[òmÀÆFÄØ`"B 	s8K6ç‚Í¶Y‚s9@â$Æa³/„ì&Ş<Ù„e“]–dW‰É†#ÉZóşªfÆ<Ù¼ÿìûøığÒÒ|»»º»ºêwÿªj$„B:€¡õé­÷ò—Â
”¬îêşÍßyÎ¯AÈ}nó®Ñ=HA=y»àzÍæ}×GjãqÎ÷ Ä¸¶íÙ¾kßó]gòß†Û>:¶ù¡ÈQò–í×Ø¶¹ıªBñ¥-¾fÇ–]û[î>uí~¡úŞ[G·Wÿı›pİ÷7ï€ı	´ìpŠâ;v]¿ÿ«oN8Cı_»æÚÍ£ÿöÅPWg¯Ü5º°RüB_ş1ÜÙ=ºkëşÆŞ
çïBûª÷\;v}~ ôHœ\ßsİÖ==ßş78‡60o"–Y‡?88~9wÜ]ØãŸÁ3€R™³±<Ã26ô¾­«£¿eó°±b~šË~=AèÁÕ@XFd$oC,ÂP7‡ÉÆñ<æX–Ó¾Ù¾jŸ«~Û¹}K|‰HÎ_ º”(#P¡¨" i€Òud È	è¤h"Wş¿Y€rº)z7ÿGä¥èC¾üŸb  Ë(Q`Ã(A‘üïQEË)ÆP9`Å(˜¤X’ùwQ%ª ¬BU€Õ¨:ÿJQ¬A)ÀZTX‡jëQ`ªœƒ ÓhNşm”¡ØˆÒ€M(ØŒóo¡Ô8µ ¶¢¹€óP+à|4/ÿ;´ Í¼- l£ØÚ ³¨pèw¨uæÿ-¤Ø…v£.ÀÔÿ-ZD±-ì£¸õ.A}ù7ÑR´°-\xä¢pâ \WP\‰† W¡åùß Õhà´
p­\KqZ¸ç®Dkshà´p#º2?FĞÀQŠ›ĞFÀÍhpÍÿÚJqÚ¸mÜ¶î¤xÚÿwt5ÚxÚ	¸]•ÿÚ®¼–âtà^´ğ:´;ÿK4†®¼íüÚ¸]xÜ®<€>x#º!ÿº	í<ˆ Şøoè£èFÀqtà-è àÇĞÍ€·Rü8ú(àmè–üëèvŠw ['ĞÇ'Ñm€wR<„n¼İx7šÈÿ+ºİ	x/à/Ğatğè.À¿ xºğ“è^À¿D‡?…>x?úÀĞ}€ŸFŸ<‚şğ3èS€ŸE÷~=ÿ9ú<ú4à(>ˆäÿ=„>øWèsù×Ğ)~	}ğËè€_A>Œ|}ğ(úà1ŠÇÑ—E_Éÿúkô0àcèÀ¯¢£€£cùŸ¡)tğzğkè¯O¢Ç Ÿ@_|=øš| |}ğzğëŸEOæŠCO>OñèiÀo¢g O£SùDßB_ü6zğ;è¹üOĞô<àè›€g)~|}°`‰ÄüÌ‡–èCKô¡%úĞ]fKôaLô¡%úĞ}h‰.¿%"Ún§º-Q–©Ş*T?Uª“ªÕ4ê•AµÈIuÆ¤ºá¢ú`Q‰wS)÷PiöRÙõQIõSéP),£2¤¢ò¦r¡²¥2QN% Fù§ÜMP^&)ç*(‡*)?ª(õ«)­S”²5”µ”Ru”:õ”´çsĞùÿ–èoò?KôRşÀı °	ı(,ÑÿÊÿ,ÑÏ ç¢Îÿ=X¢×ç¡_å –è×€Ğ›ùWÀ½Ø†ŞÍ,Ñ…üK(‹ÀÌvb{şoÑB¬va#ÿ=Ôİ€=ØŸÿ.Z„ƒ€½8š?‹úpp1®\‚ëògĞR<°7ç¿ƒ–áyùo¡|à î Â=ùÓh9^œÿZûWâåùçÑ*¼p5^›­Á¹ü³hæ¿Öâ­€ëğUùgĞz¼+ÿ4ºïÌá}€ğüh#¾pß
8ŠoÜ„ïÌŸD›ñ½ùh¾p+şT~
mÃGò_EÛñçwà¿Ê?†vâ‡¯ÂÇó¢«ñc€×à¯å£]ø)ÀİøTşº#ÿÚƒ¿¸Ÿ¼ÿMş+h¿x=şAşËè#ø ÷áŸä¿ˆnÀ¯îÇ¿Èÿ:€ÿğFüËüCè&üëüĞAü[À›ñ[€ÅÈãÀ[ø1†ÏİÊHùO£3ÀÛgşt;ã¼ƒñN0¡ü§Ğ$SÿKt'Sxˆ©Îß‡îbêòîfÒ€÷0Í€÷2óò‡Ña¦ğLà_0‹ò÷¢û˜¾ü=è“Ì²üİè/™åù»Ğ§˜Õ€÷3ëò“èfà§™M€G˜mù	ôæêüíè³ÌnÀÏ1c€ŸgöåoC_`n|ùhşVôóqÀ¿bîÈ}‘9”G_bîü2sàW˜òE3ŸÍD0e¾˜¿	c<ÎËßˆeÏïGÍœ|Œy
ğ«Ì×óûĞãÌ7òASÌ·O0ßüó½üuè$ó2àÌß>ÉœËïEO1?|šy5-z†ùy~7:Å¼øuæWùkĞ³Ìo Ÿc~ø<óvşjôæùè›Lğ4Ëäw o±<à·Y)¿}‡uä·¡3¬™ßŠ^`=€gY~3ú.ÊoB/²å€ÆDÆDÆDÆD—?&">.:ÊMö6°¤œ\Aù<ıĞ¡nĞ£î÷ŸÿŸÜÈh|~ós°ˆoægØEŒHÎó×2?g1Àr¾•ŸÉÏ0ÇÈ ¿z~«ÑüMèMÜ‹ßb–Áıÿ	ŸíÈ©ƒ]Èt1;˜WYÏgG"X³Q‘>ĞµeÀ³¬€õY	¶d7èì°&#`!¦€
¯Bé èÜ Ñ#`Ë–‚møè{®õÂ½O‚İh¹ï„'ï K`	¯ÛqJwÃsÕ`#ÀyÈÛëğ¶Aô|<Ûv9)üg¶MĞ«Òk :PšReÛ‡W­\±|hp`YÿÒ%‹ûzõtw-ììÈ¶·]±`ş¼Ö¹-ÍMõuµ5•ÉD<Vöº]SeÉ.
<gcŒjºc=#‘©äÈ”-ëí­%ç±Q(U02¢÷Ş3¡·EŞ{gîÜö¾;³…;³ïÄzdZP[éE¦^êŠEÁë††áø®ØÚÈÔ4=î§Ç¶$=Qá$…'"İŞ]‘)<éêÙ·ãP÷HÔwB–Æn•j!—d8”áhª2¶ç®lÃô€©ìw‚A¢J^;Å&ºG·Lww¢Ñµ´-¤uMñ§ZWd'i3º+r¢æô¡»ŸÑÑ¦‘”²%¶eôÊá)v:Äv:41e¤¦ªb]SU7ş‹º¼uª&ÖÕ=•ŠAeK–_|âz,rè-MÿÇ{KF‹%|B‘CÒÅ‹d‚ë¥cmƒBÿ¢QÒ–»É¢Mp2uËĞpá<‚6¾†²õ©µSÌ¹rºtÅZE®ÜRºrññ‘X”°ª{¤ø»o‡wê–M‘Ú >ıMÀ/\L±É‘M›wıèÖC±®®İVOe»à ;Zìk÷‰†z¸t:±“ahxª>¶gÊë,Ü Âƒ+†é#ÅÇ¦\§ĞÈæâSSõİ]¤]‘îC#]…’ºbCÃ§ ^yíDc$p2ÌZÒ)÷B`J²ûĞğ–mSá‘ÀÏm‘á@t*»È·66¼u-áRLŸªz^¥o¤OAßŞwwéfÒs!!F†™ »–p
"= ±ÎpAvÑSÂÑÎ‘a@¥Ûà-Å;ÈÑ{ê6±°—\bÉ£{ÑµÑÂögš(¶‰KL‰³êÒ¡àb›
ïùo›V¸›4¨*Ò½µkVßS)Wl`±¶?İN†Ğ¢øbxB$ìì-]b ¹PÆ@5´ˆpÑ™Bƒ‘áØÖØÚÈPvp˜ôĞšòwÉŠØ’¡uÃ”ÛE)Yù³Âõ¹¯¦˜… €=©@‰§ô|=¿xÚû¾Ë}¥Ë‘CblÉŠC¤æX±B9Ô7…@d³ œsEıíóëEôHÏ¡Ñgò·l:t"›=´§{dÇ<RO¬oË¡ØŠáÚ¼åÃ7n$¯sB½degmŸÎ1<9t"‹'W¬>¥#™\9|‚Ák‰ô{w@ÁØuG¶â\»ãĞÈZ"ÚÈ„„_<…cmTÅÚN`†W¦¤ØÖÎ)9ÖIÊÛIy{¡œ'å°»q-ñ,ä;ä-"	kD‹?k ßÖ‹?õø&ü]æZæsÌKÌyÖÃÎeÿÁæµı-w#÷C~~îö‹åâ\ø¹IüŠø+ûõÒé‚üI%«|Mù…*«_UîÀw5Kûƒ¾Íˆ7:{/šŸ7ÿ/WÈõeëNwÜ}§ûïİ¿uÿÖcÀO5üüÂ»ŞûKßõşrÿÖ@(ğÑÀÉ2¡ìDÙ¿¿ò„&Cı!\QÀ÷<­-½¿!şô‡?şüó'Q—h.Äé?¼éĞ¿ÌûõFmÁ[ÈÇ¾AJşæĞSÃdÿƒïp™üÚüBõÓì·áÔ^ˆñ‰öÓáo3¿ı?+Ù»€EåTÿRıKXõ%øÓ1¢F|Òøé™2¿¾àL3‡.ì#5,‚Øú%ˆ·íÈB±¬.±öqİ&7kª›Åõ¨½ıg/cÃÙZŸ9s!}fNƒéâ…X¾gà(VljlÎ¤İÏ)öyve‹‡ãäƒ¿òÎ®®;W>wácÊÊ |H>Ñ<^Ç¼‹’H‚Ö€'h/æ \m 0úcöaO{C8Ä¨¼'È¨v—ƒQ%SfÉYÅîX…÷ØX…óbFå¼Œª°«+¬KaÕv+¬ÓoH¦Ğ%S*èv—å7ì.{8 óŸßà¼n¿Á{P@ç¼|˜«ç.ĞÀ¯~—á×üØ¯Øğz\š‰Íï9Àyıv×	Á¹Ñ©t²@™öWs§/œn ëçr§OŸ>—;“CßšàR:Á›õ3ØK.h°¦¿ç~øŞëZq›Ó€s9œiÉ+F?±úiÊĞO†…=.ûblelx{ùÀo+Ÿ„ã•_Œ}Ï<ıôâ“‹Ÿ~º°›Yzä
(ÅíÈµ£qQ”%›}j‰²tØi•øyL±·Øæİôœ«›š®NÏ§—åá+X©h4ÛióKÕc—ğé—Òï%ö.	K‹d|^ÆOÈø!ß+ã ¼K¾Yf5Ëk ‚[‘ Œà¥-¬mjÏ´g¡.äÎæè¶7­¿ ¸7MäÊíê0ˆS‹Ç]ÜÛ¹lãÆe½‹qê–Ÿäj7¾sï½ïl¬ÍAú9L~z»Ô.É²%loÃ÷Û^·½mco³a› k,Î³øY?Îâ[Xìd7±×±,b1;LÚ¥	ah—&K›XÛ–?ß®ÆdEK2U´á#¶]	Ü‚Ÿ9®AÏeew–1ûw8˜ıŞÉáØ3ù×²9ÍÙ+/·>áÃ×ûnó1¾#~œió[ø&ã.ƒ1î¿ª[BîDÑª©±ª«+B
kYuµ–‚¶„Ø
{ô3BE,–ÚÏê[á	ŸÏH²¾®OçŒLÎh­oÍL§f2„Ù¾úÙ¼õF†üfR ¹L.GvÅ}&5§ôC_Ûp;ö,„pu¸Â5\ÑÒ†[êÀë·xBØC­ jb¼§Š/+«£ó|\ŸÍs:c^[ç›­¬Ëøª¸¨­c«î¯r%ÌJV³³eM ç||Q2¹(Îg„XSk×Ø•Œ#éªê¯	=›PÎ3Q$£9Y?7Å
c4e·«
„‘ó¼8…”H›ÎÔ_˜¦Bı§/¤‰`gš2è‘kŠ5=?ø<üâ/¿<ğıï“š“ùQt2{ÕB<0Æå^±·ª‚$9´vu@eTGõ@ZëË@Í4Ğ§Åí*ŠBÆ×p"ÒëÓ1¾NÔÄö›æz2;ëT¯LŞàÇxXæÚl q:Çˆ\–¹ÙGßDß‡âl$Ş‹ C=Ê¡öÿÌÿòœ†9Úìç¼f©e.Xço @ò“8&:«(V/â•ˆÛÙÍ Ê{‰™Oí…¶Í2Èß(Yâæ’ı…8îĞçOƒŞ°¨"k1°û*f\˜Á6–İÂlÁ›Ğ&bÔÚq½~n"5q3X{OgmÄ+r§Ø©¿É¿É0ÌĞ0úÙ“A]Cı¾gòçOÂŞ„}Ö)•ˆ´;à@Œ Ø0PDn÷>rK5y’\Õ(wóÙ î@ı¼n8ÑR^W€Q÷İ¤ï'ábaÈşüärğ¹Epø¤õÛIkL8´¯1tØ‡Y²íoOM§È¨–‚mZ?GwsÙãTq3)-JÒDc+w0–+ÄdÒmLú¦]»n"¼[7&“aµ´Çë¿úÜs_%ŸÖmKkk—nk-î	7s {Á>(h0ÛÄÚîÂP¨ñayŞ¡Ş#|^`6
×
ã+ {u%¢4(ƒÊˆ²Gá…åV±«? Œ¹iPX*–r/ç2Ó­ î ˜Ÿ¬k½¦¶3§Äªj-&éîn¼°„i”½n—@ä	Zğ+à_ú×l=+˜ÖcŞ%°àSMÁ#xtÿİ
Êê@Ü¬h‚ÖÅWK7IŒt·^'|v¢ş8aŸA÷/f½po<,ÂiX×t´4|Xˆ ×—zÉ¿A™CÎ
%>¡C¼û„õ'ªK,„ƒ7NBUÕôŠL@˜D(–îUV¡öévÂ”L*ålm%ìJ¥Ò„[ú«Ó{Ï¦	ÏLÃ•úú÷8Wpª<ÖŠZÑdcScÓÒÆ6¹	JÌ‹ñß„ŒÚÊ nŸ¹‡Óm!_mÌ2#)o°!éêìñt[|×.Æ_ØÑ2êÒuÆ ¯põC½Ù·¾>]ª.SuËÃwJA¿s+P¹%ÿ&ş%Py.úN6ôHßÅQìœ ™hH£XĞ‰óÙMp°Vß©3úİ‡cÆ± v±ÔMIœKîJ2RRJ6]Åâ>v-:wO¤p8…),¦æy}ÍM­É¤t¯(†šÑá&RoSƒHˆÜ°Ækö…D#D¤@j:Mëõ™¼š&´Û &:—£äËåô’³‚6€2Àµ–t3!Y
7Ù/P//Äcb- s¬¼!òçkû#İqoÔ×TSæŠ¦¼=q%Q×llô·ÕÒ	O¸cÓBKC\t]=ó‰â,•üµåe•~¹L[$šº˜³°¢¹ß%†ê$jûçFDE±‰~°A`Ê	´ÈëÕÙöJ‹vX)Wrs9ÆÎaãÔ»ÉîÑ\xşF×µ®qëº!‡¹îUUá^»“Wi÷ÚlhTFŸ&Jd:õ—Óúôurú¹Ÿ¥§Ó _9 9œÑ+¸à&+d*ÍÎÖ._¾næ{¸9tÅ¼Œë§çk>rpÃLïÒ'ğı‘ÕëRDó;@"şÚ\Îê>bê0/‘ùpà ì+¿Êİwkl˜eD¶
ÅbwE®H q¨•±ò{#èŞ 5Œô%@lZ€ØÑJÎ€€Yí0«¤jU¤² ®AÖ“~¦
VôõÕô¹Ö‰T1Jİ l?s‘ï&	y.1õ"çQ+æ`¿ûÀ=áö‘NsabÿÜÚ+’†¿s÷J^àm^vÛl6|œß¿½nÙEŞ¹Êk}Éù•ÖœÕË‡j´LK#Pfç-ÊÍDÖé &	Ü]¢.hUvî^Ø­®èç¦k†´ )jı¿Ä×v$gÇ§¢ƒ‹2üà‰G×õ'oÿÊ³92zA´ğhaeP7vœçõñ;ij[€pu„ŞjÑ}±ÄôÖM
àj–ø¢§wßÍF)ÑÑÂHÇœz­<Z¯uDê#wiõ.­¾C#lhâAGñ7F08µˆTs÷>„5èê¢¶»‘Tc”ß-éÀ>©GÓ"®õ°›¸0bqİÃÅ×VæÈkeh	§“KabÁwÑh*pjú‡ÄƒÊÔ7•K}kÂ–Ò1 ğ¥&gtøÀ½?,ú¸‚‡K™Kmb’`A›Á,º¹¢›#‡°Ïœåı<m_¶®Û±¦Ñm†«<›B-Ëæf<F0áÚ7ó5’N–g"º·¶½²vÎÔ²šH¤ÌcyK²:ıDõ¢¦`bîÂP°©.á˜»+Ùİ.oÊ†‚™šruî¸³"êv…+­HCÜg÷-ÆZ<l¹Â	§»&²û‚îgò3 -/ ?ªE/gåøE%*L‘{°÷$ø\d/&ÆA÷ïf«Àù„ìQj£w#ÛgÙGYæ@zÀ;·ÂˆQ}ªøtŠ<eÀã)à 0Î¨Aˆ¡hÌ+AØ¢°I®&»‡m‡YrÈnM·O§ˆÆe¨²§¥Ÿ‹Á9˜U0;©4Ø–RÀA¢î
 z‹—CX"¤›[š›.òÀßzé{lûÖ¥Åß›¿¼ÑãoZ>·uÍüĞk±¶ VÂ•ÑºÚzùïñ2oÓÊ+-6¿¿:1ØY]¹t×ª*[rj`~¬,•ñv-‚¬œÆ˜ŒÈ$‘º(P<Œô¬Œ‘¡ph‹Tª"ò¥‘KˆG#Ù¤ã‘ñs6gã923Ä"ü8Ãº3ó‚Mâ¨‡“àˆD·‘_}î¥ÔK)®s¶¨ÂùìSˆh8!Ñ”ğ|oöÏâ)?Nİ×ÿôàÓıPG:‚óøy:êQ—õ³‚Àpœ]doGèq(¶=ŞÀgy†'™Á«¹B^bdˆø4áïÍ4“Ï8>ğmÉ–³Ğ5–ç·±.ËAC¤²Çi´Œ0äš6Ò+Ò?&ˆù[È³úV¯Ïîİ{g÷®…³¸ŠD“OÍúñfü<íÜ}Ğ;3ÿŸø µ[µè¾SÈ‚ò*Y³Á6
ö*ÛL¬Iù­•ÙÀÜŞÊJç8òbÑëe‡Ã;ÂûÃlx\+ä™•¡9˜aë¬hb3a	‰É4ÉÒC°z,¿<!¸ˆTûÏö¾LÜ ¸@ğ4Æ×xÉx˜å$û)Z›U†=1b?lÍújg»¿|UCk_áOÖ%ıx™Í¯Œ{šåRfÂÜPŞët‡æÊ›êªk›¢œÂ¹Ü‘ÆÚŠÊuÓ…o^Ì\ğŸÛÙ MºÑ*ôNö±‡»ğ,d¶·ãUíx¸	ß_…ˆ=cùğN¶3ø(¨r_ÿ¸YW_ÿßo>l2“&^mbóHÙ±2f^[†ËÆ?ÑñP3Ñµp#v¬Y1şŠüš|^fÈwÊG€rû’w$ïO²É–äš$›­?Ø‚[V÷Nè&¢¦>Òçé™àëÓu©ìöN–]Â®g™yğşä”,"Id†ÄQ¯B@n7İyµè~s{/@qnït!ƒçIÄQÆ!İJ¢0ˆ;J[¢<Y1Û6¸=†Ë})$+¥'tüd¶!F½ŠIº^Wx0"Ì×"Õw[¸a`^$4Usf•ÇíôWø”šåéë»qxNcn|éü~Y2ÖfÖ~a_w×Ø+—ß·;nì=o¥–áË­E=])§¦¡ù«[VµÇuqæåˆ?>¯/Ù~íÊ†9ëo[9|ûÚZ‡m1ïÈìüÒk¾xusÓÖÃëºv,ŠAïWş±/\´’ğÒ}æ0Dò¢ŸBÈv#è•®9TÅPÑ.É¼lózÜ¨MDqâ¥2Œñ²‹—9dÛiº,ˆ‰Z.Tp¿Çc†â2dXoøgÙãÈÿŠß¦ùq1éò±¶ŞÖµÖ¸Å:-§¥J‡ÜÁwÒ<¸àR©ñ&f;·W?k€ç¥Ù…—äÇ8E|ëîÌÀ?UL÷w¤¢u¸"*0*b=,W˜„ÒgÎ¶o­ìYØ_ï\ØSùB¤½<Ö®]S{b÷³G,Yräè³»1^ó¥%K¾DFVçÿÀ2Ï½ª Ï˜xr…ö‘ü	ğ>¦NÀ8ƒ¬
öCïsCR‡—º¾t	ö»ÀKºçÍ#¾¬Ìû}sÇ¸£­s›Êfõª*ÄËİşğAõ vßöÍ¨ø¾Æ¢˜Cÿ¤c`!r‰Y©8Ã–Û3+„¬˜F`Ãš3§Áåj˜Ó`-ØÙ_Ó\{Eï‘™¼¬©1Oª^Ì?§«úæmñl} lNg"Qmğ¸æ!ÂLgª'ÓÚçt.[´c'îûùn§\áG}™²LòWGBU>…{æåßdV€õ¨@¯gcUYÅÙ»ƒÅ!’Ù‰À†!GIÇtM+Uù‰×Së'”ÒFş}¹…£	>E‚²c•@Û7².Ò]İIÖkœÔH,IL³Fîğ‘;4‰$É	¤îr/)*“ÛÈsä k’gÃcôZ‘0Ñ`ßCB¿t!ëm§i0=ÄúL!ÖÏ¦ÓÄ»…Î¥p.ÅÍRPÇ¾×:°ø–¾ı«ë›ÖíïJug"|™½<•ñ··EƒóÖÌ[8ìö	ñæ^­áÊ‰5k&®lPtİ6È;ödïölÛ¶¾Ê2yÓÑ["…‡A
uD·fƒ.tÇ¥ñ\³ö»t.×>”µÓq›wÉøÕÑ ¹ùCÇÂş1ñhÈïá)ÏAUQ+İƒĞE…bã ÈÒq=4‘M¥HdP;U A*UH÷ÁR…Iæš$bf„0sxî¶{WUo­ªÚZ½êŞmsg&MNªªµÛkñúu·¯I	ó$¤ÖÜ>ó™{ÆÇïağ…_oVCGİ`›dÔ”
¬&…%F”T›8†*ÜAÀör'{ wa
š¦ cÀÖ¿º!wöe:ùb•~VãGf¾Ëg^Å™'W¼<t~*¼¿Kç`*³.•iÕR¡ê‹_ª÷ÜìJÕø‹3ßÄÁ™_@…?X>ó-*ï¿e6PyÿÁ“4Ñ ™­éµ“á»bgEÜ ×ğaş²ª*®ÊÊÀ’*L$’„Ëaç Âûò„BT€p(«‘ç•c•zxüä^ÿAcÁMdßA„ÙmŞİñb­d(éi¸1~€£"Ì$A….’ äºÄÔÈöÛ ÓgÓÅøg{¯|ãÙò/Œ*µó{â?Ğ]ß×åÃÁ‘tÓš+Êƒó×Ì¯¯âU3ÏÙ$Ih¸ò‹">dúJn·¹Â\MùŞ’³ò˜Æ„ÁT0GUÎ>&U¤6/‚¯`:QGÑ_”84³!wá4ˆ#‘‹Â¸ÅH££3âÌ“–àìÌiæÉ™*¾=ïaQüâÀ@hÄaî(cÚŠÕM.¼K‘m#¶zt”ÔB!Ëı<m¢§|pRm×±1f­#óWG-‹f*p*K¤P"Š§IX”\ÎÙAØ$ã%:Ú*qÄøp$ÅåD±¨uÄêÅ£¾Â—i¡\L&#ÍMFÉjZ»°¼µ®\JZÓ½£ÿ”^İ‘ÓŞ¯EûÖâ—J¾ÚîGÿ˜ñÑZë8à`Tİ…ú'UücÿXÄğXöš¨_ÈÎ^QöÊ•2+Êcv»äöù-?]Æ!¿·œöãïù±ŸCÜ˜åwY–¿
µ’<Î–J"âX7HƒÒˆÄJe–ásø;NëX¿é4üûÖ,lY†ÙatJ³ØšÛÛºwzo;e.è_.u6—›Ğ©¯ÏíMÍöòØÈxõiB¡Â\
±ÇV _«c+¨(€ïgÖ„—­Z™H\9¸.´lÍÚêÑÑØÊå}>æÉòkVÆCÃ[vÔ×o\³Ø?’1órtÅÊş`ÉR¼ãP «"Á6ÆåÙî î$&‚ÚÃ³s`2~gfãèÊ• (Â“bğd^|
%ÀÁ†pé>J$Àiùz·E2ïDğ#A¼-ˆ}dì.¯ña/ÑğV8¶[xÒñ®ƒÙéÀïØ±(zEæ÷"°é‘9"™Iïñ÷Ì„‚¨Cú|úI»Ô±0«‡ğ-<"2—ÔŞPù‘ Œ=\†o/ûT3 qyÕ>’’İ©Ñé¬NnLÂ:ˆ'<*i2åcÕî¬?Ôë>XUUî,ëtådˆâÆryÚòá¥Sè¤	Üúe8>¨wH$º›&œgZT[br ÏIı(•ûaîÂéˆhúG ğ¯§ôé\.]`&„€EÒ]*•¨ã*xæb8GvN3–d*œ€ï‘¢ÉT2*Én£MR5ûª@[Û<¯w^[[`U¹±‘sÈÅ;F¼‹W¯Êûf¦ï^÷ô‰£KjöüãÍÍÿøşš™3Ÿ¹›ûŒìĞúÕ‹½%­¹•jüıÙÈ„GX|ƒŒY’á1]vé²>æ¤‘³¨øô6ë6‹…1ûQ—Ùy—ğY¹QÀWx€û|›ş—:³I¿Ng˜¬>¨3.½Qg]4 –:ÄNTˆIDœËm,æ#TÜ@ÒÁX_ ÓEx#ÍXrQ 
‘t ˆ!3ÇİÚ¹¨§³lcıÕ;s‘‰+7oÛ¸2rVúö{&›ÀÑ.!±‰Ò^¯e¢
,<éŒèÔÓ¼FæHò›ÂCJŒ"ß„#ê“„btA÷Åá<rNÓd
BÄ…ˆ{
í+ÁâdŸÕÈ”±ŠÒ±ªóUØUtTth6(bb•Éûy"®«ôï¤{©0–õCE¾ƒZOŒ¼3Fâš	#c¹nPS
³¼ÜÅ£â,ÔÅ™(sVG,lË¬¡9âôæ5­?Ğµğ†uMMënXØu`}Ó¶ÈüUMM+çG"óW65­šÁë×N®¯«[?¹¶´oßŞ[QÑ»½½¸'Qÿ
ˆâ¨-'>èüI•4¼Aöd¸àIØ{÷QbúHèÆ†ìÆ˜|4è< Bê4´ƒ
äæ4C(xÁ·IœBüé	™Gs0)BÑ†=å‚QêvÜ÷ùÔĞõ}ı£U[ÓmÑ¾ô`K(ÜÔÃ<wíî«š¼3yæQIXÅÎœWÃÍÕ•a¥ '‹¨œ„PË§Z˜:¢"b”Dò{õÿQ,ˆÏÓöùı¨ŠÄ.UD6ªöI–õ¿‹‡rI<ÃÅÆpI6Âÿldh˜C¢úøAäOÃSş×A«4íe‘)4n¶êtr_İÁB”ÛM')ëA"hœ{IPô×ÉAšDI©ÂpxA\rø}²BÄıuì+1•‹66ãŠ‹Æıöö=ËşŒğ,»qm‹ä‰yuÛRÁ“œ_cË¬¿uÕŸ–¤Í I~T‰n‡®š|ZÄw‚K`°ß‡¼EFxKƒğ^2~æ%fªF’ÑR/Çm·MØ›«©ÆZpÌ8Z´BdäpèN«[ïä¨=ÊĞQ½éR2šƒ,¨>WœÏI¤6;…‹®—//Ê_aV—-…Çô9çU®ú†zS8Ö€4Vßw¤ï'mÑn"‘¡L7.wu¬®L.[ÔæÁ3o±Ü½«{®egş(•eª+C
±ÍQˆÆÈøtg[¹
,:°¨b)‰(Ç\B1'>âÄ“NìL (!K4$rQNE]¡¨
qf_‚ÈGq¢ôô²ƒœÏ‚üíIàD:°OÑ‰İó‚?VHx¯ë¢ÔÕfEGoíœOsø ‡¯àú9Fæ°x}w†0âBÚ¢:\·Zy°–ˆép-®­ì¹Á|ÀdÈ¸˜û “¼Å€+w8ïw278ñjh§Â˜!„çà(±4W¸®‚§Ï§Ò‰Sœ6Z[ß3ø	.{õ39êGy„Î*Òé…:¶0\8;Š÷	E¾P¾óé@İüh²+<¸«}»7l­h)kˆ[îÊ¦Hí’–Ğíªº›+ä gC÷HmÔ«¨ÑÚ¶šõÛú€êS¼	_Y2èUœñt÷œõ›dÍàÕá”’Jâ!ÍËÆíã$	BcvlÜvØÆ ¶ÇˆD¶óH,xá4¸¼srçr¹ğ@[1©X“øÉèO˜'W^x]Ij_ò µÙ:·"n`	0ô1Ív2¢ó¨ïAÆ¸£^£ƒïÒ4Y).oK¹ÿ4M ¦s4J)j=MòÁÁÉ‘ƒÁÃ][²áÑ+'®¨ñ†;6kÕ}[æá“3Ã;6x–4â£3ıó¶ôUCI´Ñ‰¾›­4ğ~owàu‘:¡²7(ø	OØñ~;‹{1ó#í_5æ¬†©48LsjŠsq.„8…Ffš"ó¯ŒÉ¼K†Ï÷ÉàŠ˜¼”# éîåÆxb¦ËHÙ÷yÌkrXfDÙtv†İ¸RÌİ^ ôr©©Ôrg!Ø¾¸¢.5áÕS"=a¢çŠ‰´‰®gÜNO³³…¹#ÙİÙQ¾¾¼caOâêæ--;š˜'/¦}aæ§·ŒãÄ ™eß´ˆàÙøÜ~#‚ÃÄvÍãı^ÜâÄÿæÄ7Øñƒ'0ş,ÂA:«úw}?A#åóÙU„AŸË7æºüÁ‡Êq¹ß,‡!¦ÙÀwØeàá2ÆPÈ…B~Å…]è&~Ö†Ø°H‰hUqL°¹Áv?‹éøİˆAÖàÏè¸JïÓ×ê¬KÇ¬®êcˆ%_ Û£â×T¬>$`º¬M¢¡Î`§¿Ã¥¢<yáıoCø¨¸K]©2Hµé†¯Cì:ll1º;wÚ ñmL‰9ßr{½?*Dx$Nåè8'œyõr{K!<öé?òÍM¯ïM]ÃŞKÜ‹X 2—1DÍ˜FÍ$ˆ®ÃøÕ«S£MC±mP$bT®«XYqe¥	‡›ãC£5+ñ¹;şåš#xå‹Ë>÷É;Zwşñ;ş¸sîŸüü²gşúÈ5ÿœôPD4ï'òÎ€gQôŞC.Ì’!¸;€¦äÑ§ìÑNivSâL	iÅì¢4vGİE‹œ²sÌ”à1Óƒ‘F°zÉêòuúÒ= ÒÈdÖ3èñÜâyÈÃy|ŸğaÍWïc´¢¨{=f‡³CïĞ:d’bI_"6ä•úÙRj	:^˜º=7Q:× €®%i7¤!Qv"ô@J6Àè‰ßÖªÓÍ>_óœ”vuí_İóè±kÒµ¿.Ô70‹ô…†ŸÁ‹ff03óüè3kj<Pm¨¦£»N!ú·œtJ”ENS4—¢iºóZåAåq…U@ì8Úg‘™ÅÜ˜»l_‹¤soš-lcD›±¦):Oç:l{Jœv}±³é‰YjíÕÁª52Eå&ƒ\u¸‚ŠH
ñÇî›¯KnHÏÙPqMó]Ø}õ+[–[¶ìØò-ß¿jæê¡'^è‰…ú³Õ
pÙ‰‘ "ÁÖ^Ã"#ŠSv;‘yÀÕ!â;4îBú…ö/d°şêY2rW yqúœİCJGæÛ8²ü€qx®èêínóá;fìVkGOwG`æsø™ş¾µ›·n©]ÑQ9²eÛ†åáĞ¦‘ü"ÜÁjğö`Ve8;;.ˆ¶	™@¨~šDË¯‚ë<M†vÀŸÀgäŸúgVëû¯ïõÑEè—¥§áQ;8õ÷<}î4T@Öê5eÀe~I>ÕÇ6÷‘5ÿï>Ÿ¿ãÍJsä/ON0K Á…• sH¿løw3ÊU$¾NåßÂ§²&ôã¬%ùKQ’]“9u'±á‘g“‰È*¢Uã.šsºèìÉ˜æ’E®ã-áœÎ-tH
ZšQnÓÃ$»pÃh?Y@6HÀIìn®ŠOÚ„¬÷Óä]‚ğZÈ¥¤§N¸E4MZş¡tıdF$ƒˆiò).p¡“6ç
K]Î¤Ò…ëBêôÅU~‰tsKS)äp›$l~ÿ¸â¥•NÄ*cHµ«¾ÂŸ­ŸÛ_ïRRÍíášÅÍ¡Ø‚ÁG(à²IşÚx]·!;W.dmŸåŞŒÒøï‚M}53Ï2Ï9+²µ©¶¤“½ñ{jc–*ôC Æ Áüï?+‚'¢É'‘BDüZ6>’øn%ëxúEr,ê²Š–ŠÆàîqıx¹s™éÔÕ’ÙR‹K Õ¡(Tñ4)Š†&©N¡«%Ë‹+‚èt]bó6Úz›æ”JæÅIŞÂz‹QÜ+Rå1£»vîšáD×È‚-‘œ#“\²N·V&³~SöVönYĞ¾µ'é´3¿Ô/ôÙ„Íë+{2A¿$:“ÿ~$,Š>…<…l“˜[²Š{öâº2©	ãuÅİŒµÇbL,«¹{©°)pëV
GŠ‘Š®_ä-w$Ú2ÈÊ(cR-Ì¿–Ñl]-dëOÁ%ßdğâ\ËP&]‘&;\$
déçRg‹ë5¸Y³°BqRõÒôJº}cG$–ÍµÆz"–Õ^¶Â¬ÊÖ%ªJ¦”ÊŞÍlé«RÔIÙ´¡º'pˆË8»ÀÑ.¿Ã@@Ç.R¼Ò‹ûwŸA8ÂP7”8@hßuÚeıxL$D Ãóâ­>zÅWÊ7i˜¢y¢÷ú-G%Aì$‘—¬½ 0ƒ™Ò„N4\Cú2°Ştâ…
ÍÅŒ”ìÉH7Uª‹êDè òòŞÉjü‘MV¶ÆõuK’G.²¥cÁHW"¼`ÍÜÚnÆáfz*×olÌ#úÁîLölm_°¥·Ò+©ò{?Š¡ÿ8iÖùûN•…ìE*	¥Õ£^½0pš®ìâKcAÎæµ&cnM$®M01¸B”&vë¥¹[%*ğP¯ïP..}4îÔèkà}Ú¤;6!	µ›.´T–9“Î²’õÇî¡âÈÜšäé ˆ1TÓútI¾€–ÓdhúL.}qŞÅ¤Şm•aˆêğ¬ÙıDs’.bÍTv®®İ¹Ï|_¾fÎBC5V5wmÎ†ñVÜÑ™Sn²˜íŞŞUşñ;xSZiˆËì®ªŞÍ»Û‡|•â1î‰3QW6j3±(8±ÂZ’¬‹K[¬NÈ ½"! 0ÉR5k
j’.;§õsgIT²!‡/ªDgh~ÔØŒUóC©‰t4¾øbn+*Ü //ZP»l¦‡iÙ²‹r¸ÿ–1QÕ¢_B•V9+r–Z	îß ®H~æ¢~œÏúà …jß§õ^O¢ÈC’F“Ü*A™ÉUâV‘Ş+–4D$³Ñ2Ú#öÂ+ÄGë¼I
ŒÒéÍåár0¸ƒµòDmõ$¢Hc±È¢ú¹‚]-¬·.ñ—NQ¡öÂ™KË¾ï_ÑAVĞ”æQØ÷X|¿Ò]W¿¢-^Ş±a~ÇhôàGç¬‰eC5+ú°£¾rÉ§"H´9E_¨}CGëÆî
SœiØ.ÉFg/ş´MØ4T›­vA‹|ÿğİ‡v“UFçŸ‚Î.Ñ±½´R¤“†ÄøË”J2¥¨|<0øM€|3À0ŞqtÜï[¬,öš“D¿Èº"~!æ‚¬7-ÈFn/év!o…¸5¶¡è\ˆtWcƒ9ÿü`Ûò9®œJ'´HĞÃ1ïê3oKr¬}¸iæ§Xoèª6mÏÌ’8¥!ôuæ5r¢LVG†n0¢qœ„Hø¸n#ê(+Î^ÛÒ
¦-&á'KK_H¿¾òÆÄZ¥åJ–‹,—«÷Åb>ø0â†hYY”|àMùçòİôM
 SÈ‘ã	«s“u‘±¾ dÄàqŸ2n²Òñ2:cÉq¯~§{ÑĞ›å…ÑÑBÎdŠmH¥„Kì&<oÎj§$UEòËU¹õ5Å¦=ËsKYÛüVœŸa¶Œ²ÑKí,pô¿€£~”ÏZ–h‘ù^à/zASˆ)¤Fİ«3™„o vİK‹ÒÒIÜN&Q\^¼”@èÅ[Ä¾p¿E§î]^j›†"P†"n/IH)2P•…Üh\·\º…t·U¸9‚Äi‘˜dËU½—+Ó•qÇñ€»O×‰WÓuŞêÓ–© Oübnñ¥Œ!Eç?OÓîl!g(¥Dt´oöÈ9),úıi!nğÊJhaÇ<×.«eA[Y.ç77íÜåi7‡<]C±XßÂ¹æˆÄ%½ó´X¾W\A¿÷6ú=ĞTFWdM!@!ùÁ ŞR•Z}]Tzå[¸qö¸Â-“'IA­âÿ«$b@¤I:Üm!Ã[ÿ±º7':Cn‰éYÌìÑ/ö„œv¶À?üªÅÑ¬#a Ÿ®õ¶"çV°Qâ¤ì_9Y\Á\
ıèP¸JŒeá×šÉê„×@|;	ÚEŒ/òÅÁXÂZW¬+Vm+×JL 9È¶€i¬?î;[F¾íƒu>2a-„ÅPj¼öx]Íâğbcq*™áÉ€wRF,Ë“vBsx™x[¢@r!
ÍĞån©t}aÌáíéŸnÈíM_hıi.5ıú{æDfm4<u{ŠKJv„®8šmTbƒ‘İé.ªi/XšÒrv_ª¼ş
Ys’/uD‚^[ÿ^tüœÓPcÙáFbjê:k,Ÿäo+/0¬Ïô]´›À%±›<‰
 Sfª„O|ÑEÍ"îÙ0Yí=^Ì=û¾éÃÖ¸ç¸×½Ø¾ØÒ'Qañy),/ÙÍ÷Œö™ÂhBÿ®ê~¯Ñ¤½™m2‹M'>ö?™ DQ&
£Bá‚O3 áT%§$à""®[Ñ£Ññ(ö—‚jÿ­õõÒ£Éü<Äx&µÁ`qÆ$X\Àœä†
ÑÎtq²«á”Šg-A§+éRBøÈâdR«#^Útu¶µm!Ó[Ú®ØJö[¯Ş¾}>ˆfR‹?ğ†DÏ7f‡Uu)„+Œ—¬ñj ‚NÂ/±_À“H0\ÒH/4j„´Gc¼gÜw¼œg'ıÁAïúwAšôĞk¨´T¶=Sœ{˜5G»vqÕšm)¦PV¬´.éÔº%Õõb<<ZŒsÑÍ4$ÆìúM¼mæwWÎ§!ğ+Ì	Ñ„ˆ¸$û¡ùÆÏ™Ä‚:ÁdòöIƒ«íé4YeZX ‘¾¸HZDš€u%òñºœ©ôgÄ\tc²ÇÙd™™Y‚«Xğ–Jˆ¸ Y©ÅóÈz“5È‰Ò|•Ò`/®ş±º’eòYH™ô’?AhY^”†òâ×ÅÈ9ız`TtÑôËdÑâR;bºh^£ÒïJÄV3EV×Ó°½Ó$~ÌI€Ä&…¥x”]"‰¡è8'º81Ê…8?;ş ‰Íø£õíõØ?.W×…ˆ+±$¶-ä Ëú­â²~4'…&«+†\IÓA$ÂQRCø¿q†õWÏ…<“ûß¦7ş¤}*x&úÕ©di’ã"fOrPïÿ7­-Ím¡–Jï¶awM2(Z¶¶b¨,KÌ«r_½¹{™ÃĞ{†¢å•>ÅWŞëâ‘pÔğ[NÉˆg½‹=ü O×,Î¿…oa‘¿pšÕÂ¾z_»5#„sŒJ=–êíU}>ÌzÆ­ã^ÅNgv‰tÛ'U]$3q:™TÒ‡<Ìê5~‰¤JSm
g@Öé×Uß¿îØhyä…oÜ[‘œÚ¦îj#ÇˆËÎWd‚Šië¬@ó@#~E/µô×Œˆ,4˜ò^hâJ›ãš¶Ñ:îù¦Kãâq·«ÏŞg:¨ ‘¯m8ÀhÒo²C¥%ïµ™dYR©=¥9’#ƒş`Áò´;·`‘)k©±Ì®iÂñ™ó—3,Ëà§‹óCøu†ŒÉ<û”FeN., ‰$ã	}È×Ièï'TL{rAg/İ'k{©(/6İ½ªSãd¬±ª(ØT›8^àw‘!SÁËRk{œÌ<é6ÆVÈ7}bŸĞg[Ì.&L˜=1’» ŸÙó"¥Y"Œ×‘¥ÆTÉÀzi¸mÁ¯Wìœ³rÎÎŠ-J4‘4Œd"ª0â}3¿»ê*¬Ü7çÚ]Û*+·íº–|÷ß	æôèœı^ÖMâ †qSßFAªÜ„$'=…E±ÅÀî|ÖÅå*ÉwoH¤ó¿#œµ“YzrF—Ù1İ?aZhiœh?á*9ÈJ@×l7ÆqœR²º7NB$Ñ{]gãƒñ‘8K‹4ÓÓ"ãÑ¸+OFÉíLŒÊi’ÍGˆ~ë’÷Å*‰V% ¼‘¯!2é¿º©Lõ^@øßş_?‹ğg 'Føf„7¢k³˜”ı-úGÄºu'¦dÈ:48¨„Êİ^µX¤AåîˆÛƒ–º!ò%eït¨–µƒ]qcY|"dxÀ«‹î€–4»±ÍßvãqãÜO»™}n¼Å—»qÿŞŸrcä¸ÇYäbQ{` ÀĞT,À
"4D +üÚ98pÔ…¨@Àó,d–Bèx³€òMcVˆ HÆ%Á%I_¤5ºv¨÷–RËM#ÆóO8]ôà5’R“ûŸ‚×¬ä1ÚsV¤zÏñø6ïãq¿…gh±	o±é,*·DµLœ”èşµìÃğËëˆ á,£X„>VšßlaÙÂ¿·ğÖ‹¹ßÂÛ-¼ÚÂ‹iÙßZÿhı»Å²0oéÖ8Ë»X¾`7²ßd¿ÏBP~˜ıË²YıÑÏëŒ•pqo"¾8Úés÷ô¸·è×ëLŠÅŸcñ=,¾š½‰et¹Oê !A—’ÖÂ„%+häŞÂ4Ù¥¹°Ü^º]wİ,¯@
R¥‚‹³hP–*İöŞé´?Ql¥òKuùôÁ£g'Ş_ßì‘$òúháû³,Bivÿ¾¬İïo+ª®Ø"•…Ë5#
Hıv(jhÑH™4R1\×{jË–S½Û±x¤~÷îmÉúWo¯­İ~õÎúä¶İ»ëÌ¼»½d=§ÁzxĞ±l¼ÇE¦Ütá”uOŸ;œ²†
³n*Ìº½w²m¼4Ù¦!tqºùÒ<ÛxaÍã»4©¶Øìsöé}ZŸ¼XºÄ§Ò¤š~öâŒÚû&Ôè|Ş«i{ç4ÌšK«ÈxZ2™K›#ÉJÓ¬LDä‘ØhÃ_ï<xóæ£[cîæÖ¹>_kk³ÕuOö§z³ã/º¡ßL¾ÿô;‚Ş:…|…€.£Q¶y1±›ÙI¢•ˆAHVn0GÒ±CÖozLİé1œ‡Bxà¼Ü¤sfî1EÈ@M28e*ª&i¢ÀÛùHô4RQİËKš4nç]vÓ4{ØÎˆöè+ÚkÚyÕxu"v2XNh%;-P‰LšxZ÷RJù^HOx/Qª¸¤Õ÷#*™g/MÖéÅi1BKb’uÚdYdÊS£œ5ÁË“ïßÓµ¦Éx›¯}W|‹NÖx“s}#ñáŒ+ÕØQ,4m£œ}NË~¬ªİ±{wfçË»>9óæ¾ÚjËñ‘ª8À	 ®:²	ÎawŒ“Õ\áO(ğ&2±¨Ù¤Mè}vŸ@.|‹Lë}‹LëmÈé¯æJÙ‚¬ óyôëÄø˜Õ= )lhfÌÛÓß˜Éãğ·=+·íÉ,k«¹jg.²±$òf²t¤Ôƒbh<;ÇkâÄ	‘Ù&b›‰UÛ-,fÖxÔs<1’Ø“x(Áj‰p¢>ÁŠt45N×9…g¯÷ÎĞ
wŸkqqxu‡°_`„Iv:9€ÚsééX-XM§7ärtàê\.}¶4£ş'Zß7¦…±´¬ÊÉ@aàìÒ+Úmƒ6û¥AØÿzwÖ°W>_ê-ÃãGé_›*êOÉQË	äÄÙÈ×$9ÖÆÓÁ‡%ÀI‚ ˆ</Š,â)Ú»Às" ÀÛ÷ğ<<Æ²<k'Ú8ç@j¹ÿsõÿ›  E.ğKD”_¼ üâºÁe%ÀÉ‚L¢üyÙüyAd¸Føœ%÷Ãc„_¤ûÂ/şrwñµ‰"R0Š³£?Ã/t
”Éng	—ì’(‰äì¿ X9à'+Øs)¿¨ş]î.~ 6 ¬æ	£xòíÀˆ	¢ìšH7¸,Úğ»$ÉvÈªÁæŠª¬ØĞ7É®9°†	Cyà'+ÚT»İˆİ W.w?PV×€_6› #Ê/ğÀ/;İà²İF€×dI3(¿$Â/I‘àÌN8Cø%¾_Ò%~‰—»‹¨M’¡Û	£
ü‚B~	İà²d# è²¬ ‹d….iŠ*©À=EÖ$­ğÀ/`Ü&I,k·iäQ0áç‡üúŸÜd™¦Døé"NÇ.s7ÈtƒË2G@tªŠâ%UåA³t‡¦hŠ<3­ğÈ$¢€ğ˜Í&q:yT ¹R-¼Ü]ü@mŠ‚\„__â—Dø%¾Ÿ_¦ª¿dÕÁKªäÔtEWeÉ¡šª"ôÏ¸YT¨€w*P-HåC~ıOoªŠ,—LewÀ)Ä…’Bø¥ĞØ©pD—êP5Evh<ä~À/ø¥P~)~É
LÊ/Y˜Å/Y’.w?P›Ã<…ğKÒàBpY…Ë®ÒØ©òìnMsèª¢é¼âPœ†Óát(ŠîğhU$ÿt
ö9TxŒç˜ë M•E’/w?P›¦!/á/H:œB¯8¿tv:x’GÓ4Ã¡êËe85SSC~9¿¤R~Áí¼*¸É£v°—Š©Èòër~ù¼*å—.ñKz?¿¼†®;ªáäÁº¦fê”_úE~AâJü‚j%Ê/°——»‹¨M×Q à ü’p*Øíª&Ø©ğ'Ğš@@ö;ÃÔ4§É;‡×eé–áp˜zÀĞ5ÈÒÈ?Ú—¦IºÆóÁ«Cµ~èŠåPÔËİÅÔf¨ŒòKTLTà—ü’uº;u€0†K×L—àpj>—Ûp;5Í4N’½ÙÉ¿D~éğ˜ h¢O7t€èªåp|È¯ÿÉÍéDÁ2ˆ4„‹ürü)~)e¦é´İtÙ5à—åqz€_.Â/byÂ/C5tÙ0(¿ì¥æƒ0årwñµ™&
)¿Tœ’?=o ¿ƒn ~†@@	ºLøå²ìà¹nà—©–0üÒx7§¡~éÀ/åC~ı¿°¿"a(–jÁ©(IšS”DÅI7P?§H@Y–Ëã4Ü»î2‚Ÿés¦Û
»L'dÕäßÂBâTLÓn7¤ ª…ìÌiøt]»Ü]ü@m–…¢aˆE»Ã§¢,ë&Ñ5éì4EjØm¹¼¦øeXFĞëwù-§é±Â–iÎâ—ZäyTÕTÓNırwñµ¿bQ'Q,Íƒ(¿wwÑÁÇNÀõxÜ>—éõÙngØ°nÓòzˆæä„Ñå€ÛíN)ì‚jºÃeòëtóxP"‘†]Ò|pjW§ürXtvZvZÌçõø-—Ïo7=f8ô=.Ëç‰y,‹ğË‰L-xÌn7¥¨åv#‡¡Y&hšq¹»øÚ¼^”ŒS~é³ù¥½Ÿ_qŸ×p»üÉôºÊËB×åö{c^·[…ìËD.·Ómin·$¹äˆø¥šÛ6]ÎËİÅÔüªLBdh— œJªjz$Œ#İ@ı<=ğû‚+P¦¸|Vy0ìû,o™?jGøåB–×ôºá1I²ärT«9u;ìr™—»‹¨ÍïGÕ•JŠ³N%‡Ãå%3\^º;½£²,ày=e!Åò»“á¨?êw{ƒşŠ€×ë ÿÖ¼›ÏI’[{}>¤›†×–Ñu¹»øÚTW‘†¬ša8•5Íí'3&~º;ı2³&
Fı¾pDñ½•ÑxY‚ÄH(ôû5È¾<È!ˆßğ+ŠW­ôCµNËé÷Æ½÷åîâj…Pº<—â°¢pªèº·Lq(fİ|®†h$Êcª/ì¯W„* è(ÕG‚A¢yòCRfƒªêw¤‚¡  ®` Âïó^î.~ ¶H5gÀs)š'§ªÓéAæd…èì©Ü™x,ZÆ“Z ¼¬¾¢:ZN,‘È”‡ÃU£ *‹ø"!+VÕ2G}ªµ¼îp ª,à»Ü]ü@m±š×FéŞ
8u˜fYÔát¸ÿ½ÁÇAÀÓ’LÄ«¢áŠ*=¥«kcµñpyees¢<
Y5
¢Py <â.jZHÏDËË‘Ûï‰şßí]oLSW?ç>(ÈÄt 8ªx(…ÑÅâdâPWA+ì1¡#RiÒ2ŞësüQÇêæìêŸM›CÇXâ?*$.Ëpßt_–}Ú¾¹oîÃ’ÅÄ˜-™y;÷ñÜ0îÃ¾-1œäwÏïsŞ¹÷İ¾ô´Mß»9Å«rVüß§øXI~>¸«ò€>Í­;v[³²d»u™Õf7VÑ¬¨zÆQä´¯).ÍÌ+Z]YVştyÑš‚’âMEö,È‚\X]ÀòmöŒŒÕ™í…`[µÂW—+ÿß§øX‰ÃØ¤qİ+Ó¿Ô[õöôSs»?ÿ#x	ïŠ}M¹M–¥°ÏC-;#vJ'w 7C#!†|VëàØÑ6Ò8¢ÿB¶µ„vBa=¡P-'½Ñ´¹D¼i[÷ x2¥/ š„TvZX/l`7IW²	cÔÿZ0p—b"dK©Üì'Òiäï0µğ-…\¶¬,;XÒ¤s°’í…å¬,ìyÈÅ:è0V Œÿåá¯úŸÆœÒÀÁÀ‹?€‹´‹•‚€—Õ¯/Ü‡¸¯Mq^|¥vòmñï5rQ<~…x¶’o+Ş«´2P+Ş†?Š»KdAdAä¿
Õ¯ñKU/#ƒ%0iÀèkV)´$Ë–? Ù¨qKàÊßµ®]&G°`±ÉÕ1»É%ÈÃ$“'Í‹I†Åğ»É-†]Lÿ3={LÓfr1£m&—`3U–94/&Ù¨7sÜbØPBõĞEñ~èÂ‚â~è¢l`È ÀnˆG£V†&’7Bñ~è§şƒÛçã¦¼}0@ÖŠè&›L•ßIU¾Œ˜›âCÆÈ=ĞiÌC6Ç.!&¸°É¯R ‹È .F×(_ğ‘9zŒ|ÚCGwqe”ÕÙìW{Â!ÙYRáÚìïÕÂ¡¿¿k›Ø +»#!-"7»"½ş~#Âäsw¸o ¿§«[“×:ËÊd·?õtú{e:ºD–·õtCj0 GB`¿¬udô„CÚœ»3(—•8WÂ}¶ÿÛ5w%dSn­N§N&8Qìfî¥¶ƒÀôëäö9Ï)–É¯!"LMpù+q‘ÅL^½S!)  …ô"ÒÉ¤“h½JQì”=KüA'HúõiİVèwoÚtëS[Ó¿MëÓÒäÔì«JÄc	iò

÷ÔåÔÅë¥±K¬ê¢÷bÇE©ã]ÀÏÇSùá³ñe|œ¥ğO™ÄÏŸµğsgŸàc¤?AÆÏb2ÿ“øG§oğ3§—ñOòÓ{Šmá'ÙZşÁQÿè ?q|‚GäÇĞÆb6Çjù{± ßÃpl8Æ&cX«¨ôÄãGgñwòÃtÊïŒnâoGóø¡(-]T:£’7ÚebÚßEi¹¢´VoÑÄ&GgG¿•Fò7G²ùÁı7ùá	¾oğ”¸<ŒÃ”nhÀÅ÷­çoø>VÌ_§áv„Ø Ëà¯iÙ|odˆ¿ªx¹FçÖ¡ö©ÌªÊêuUR)AÿPXye¨Oéöù”.ß.e¯]	øÚ”NßËÊn_«²Óİ¢¼äV”æxƒÒ¯WvÄ·*Şx²=Ş¨”6âlİ­:½NÚâs+_ò‚¯Z	Wã‹Í3ÓY˜Œ3¯Ÿ‘n7Õ'R½¾Jä7‹¶jG[Âr(J›oçUÄXëè‘#P“SŸÈiŞ™Ëi­OÔ©d„ä\Í‚šVúä®:U}ä1/ZÄ àĞÌ¾5œhtªè˜·âÃü‡Ä˜=UÓT@a#2‘Bü(õÉ²Z
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
xœ]QËnÃ ¼ó{L‘Áy,K‰ÓH>ô¡ºù Ö)R&ÿ}aÉC*’YÍîÎxØÍªúPí!ûtƒlĞC§r8W'ÎxÑ†‰”–ş†è–}kYÈÍ4zìkÓ¬( ²¯P½›`¶SÃ_Xöá:m.0;UMÀÍÕÚ_ìÑxà¬,Aa”ŞZûŞöÑæµ
uí§yà<;¾'‹É¶•èZsAVğpJ(á”úW_$Ö¹“?­‹İËØÍùêPÊ:F$vUTÚsAJ7Îú®ğüá‚H|M!ç¤Ä÷„Ä6%·”»”<PXlRò˜Ğk
U2²LF’ôZPrµº{a“ßl%#ñ­q'AÊ«sa†´8^›6øØ­ldÅïB¸—
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
xœí|	xÕ•î¹·z©êê®êªŞ»%u·ºÕZZRKİ²[¶ÚÚ,ï’eY’MÛ’-É6xÅ²ñŠM6ÈÈbVÂd–Ä&L0Nf2x2œL&“ÉL"'aY^¬šs«[ò“ï½ï{ï›÷ŞGµê¯ª{«îî9ç{nI-  `G0 ,íN$G&¿÷6 ±béÀŠÖÅ}¿xóÂñz€ûÜºÍƒÛÀ
í ŞV¬/_·k4äú“õGx½€:G¶­ß¼ë¥Ö3 ş›L‘õƒ;¶
@è1Æ²~Ó‘µ¿R~~Ëb†6ïÎ,=909-Ü0<8dúÁ÷°~?Ş_»ìOZO ,z¯£6îŞX(pxıG”éæM[×¾O¡Û:‰õg6îŞfâùS KØó¡-ƒ›‡—Ç/œÇëã(ßÊm[wŒj·Ân€Î?²úm×o»ãK Ë‹í~œ¾F¼÷E:†wÜ=’wğ™?c©È8å(êêÊ­uîâ¹ÒpãxmÔsÀK!€‡V b©DŸglÀÁ¶„mF“‰9N?gDO	õ¶o¨‹àş[Àƒ¨]D½1´€Q¢UGHˆÈˆ2Øµ¿€DEGˆpjÿœàBtÑ­£<ÚŸÁ>Døı@@bä#æ#ş	
  1AÄöí†0b!D#:F!ŠXEˆ1ˆ!C©ö(2í}(Õ±âˆq(×~å:V@b%$PX¥c5$“ÒŞƒ”5Pƒ8jµÿ€Zë ±`&âLgA#b#ÌÑŞ…Ù:Î&íwĞiÄ´sa.b3´ ¶èØ
­ˆmĞ¦ı½ºqÌCì€Äù°@û,€…ˆaâ"XŒ¸XÇ%°D» KñütÂRÄ.—A'b7t!.Gœ€X¦ıVÀrÄ^XØ§c?ô"®„>ÄU:^+3°Jû¬†k×@Fûw@ü7„Õˆka q¬A‚AÄaX‹8ë×ÃöKØ ÃˆañZXxâ¿Â&Øˆ¸®CÜ›´_ÀV·ÁfÄí°ñzwÀ6ÄQØ®ıì„ëwÁíçpŒ"îÖqìBÜ7 îƒİˆûaâØ«ı3Ü¨ãAØx Ş¤ãÇàFÄÃAígp3B¼nB<C<G¼nÖş	nƒ[Çt<
·"Ş®ãp›öSøŒ!Ş	GïBü	|nGüÜøi¸ñ3:ƒ»ï†Oiçáø4â½ˆïÀ}ğÄûáâp7âq¸ñ³pâƒp?âCğ âçß†ÏÃqÄ‡á³Ú[ğxñxñoàsˆÂçµÃu|¾€ø8<‚ø%Ÿ€GŸ„/jÿ_†ÇŸ‚ÇŸFüŒÃ—OÀˆÏÀ“ˆÏÂ—Ÿƒ§ŸGüø
Œ#~N „gOéø<§ƒ¯ÁW_„¯"¾¤ã×/ÃIÄÓğâ+:~^D|^ÒŞ„3ğuÄ×t<§µÀ7áÄoé˜D¼6ùQ$ú(}‰>ŠDÿÍ‘È†ãùÿÇHTñQ$ú(}‰şŠDlÌúØ¶è#YÔÇ­UŸ6}LJú”õ1f×Ç•¢"U3}„8õñàÒıŞ­{¹G÷i¯îÁ>İ_ıºwtÿËÓ}._÷°İ“‚º÷„t_	ë>Q¨{@D·wT·n‘nË˜n¹bİB%º=Juí—éºëš-×õX¡kªR×KB×B•Şój8‹˜„¿Õ¾‡‘è;Úw1}qœÓŞÀHôˆup^{#ÑÏ´¿ÇHôíÛ‰ş]û;ŒD´¿ÅHô®ö-ŒD¿×¾‰‘èÏÚYŒDšö¤	ÑÎÀ\bDl&¢ö*´›öh%Šö
´·ö2´“ â<R }:H¡öÌ'1íEX@J’
íXD’ˆ‹I­v–™ˆKÉlí+ĞIš»H»ö<,#´ç ›,Ñ…åd™öôÚ	XAVjãĞKÖhOCY«=ıd=âJr­öeXE6kOÂ5d»ödÈ.íK°šìÕ‡5äFí1 Ó¾ƒä°ö(¬%cÚßÀ:ò	í"ŸÒ¾ ÃänÄr¿öyXODÜ@Ö‚ä‹ˆ×’'´á:ò”öYØDÑÃfò<âò‚v?l%/k÷Á6òí^ØNÎj÷ÀõäÛˆ;ÈÚİ0J¾¯ƒäœöØEŞÒ>7óÚ§`7ùgí.ØCşq/ùwíNØG~£}ö“wµ;à ùâäÏÚQ8H&QªÁMÔ¤İ£ã•o¦í0ÜBİÚ-p˜ú´›áj‡[i¡ö1¸Æ´›`Œ–!¥•ÚA¸&ï uÚğ	:K; wÒ9Ú~¸‹6kûà“´]ÛŸ¢µ=ğiºT»>C»Ñ^mÜMWi;áºñ^ºV…ûèzmÜO¯Ó®‡èm§;?Kwi[áAºOÛÑƒÚføı¸¶	>Oh×ÁÃtñôÚFx„~JÛ CïE|”> ÀéCˆÑ/hÃğ8ı¢6_¢_ÒÖÁôim-<IŸÕáËô«Ú <E_ĞÖÀÓôem5ŒÓWµœ gµkàúmÄgéw´UğıÖÏÓsˆ_¡oi}ğUúS­NÒŸi+àı…Ö/Ğ_iËákôâ‹ô]m¼Dÿ€øuú­^¦“ˆ§9N[
¯pfm	|ƒµÅğ*'k‹àçĞÂkœW[ g¹€6¾Éhğ-.‚øÑ{¢r¢r¢r¢ÿşœˆmww§ş–›=X9«Ái^ßõ·áÀŞ‡Ûq—8^¯û-îï²]kÃúW®~·ş¿};†ŸChC@Kú ÚıR= åØïá~ûÏÖÈÕïº¢vNî83wìÄHÕ±l;Şû*¦ŒÿÇ6âEOù¿{Ë`”Z”­çÏ0¤›úz–w/ëê\ºdñ¢…æwÌkokmi›nš3»qÖÌ†úºÚ‰ÊŠò’XQ4Rô:»l-o6%PŞiÇÆ±HGG»bÁàeã!,j¿òñĞ€~[èÊ;ÓxçÈUw¦³w¦§ï$öP#4V”‡Ú"¡ñ×[#¡“deWßÑéOèç‹õsCL¿°áE8ŒO„Ú¼ZCãd Ô6Ş¾kÃXÛ@+¶wB´´DZ†-˜‰[D<ñl¼$²í)™CôZÒ6óŞÆhÇ¹¢¶Á¡ñÎ®¾¶Ö@8Ü¯—A‹ŞÖ¸©eÜ¬·ÚÈd†£¡å§Çn?i‡µqëPdhğš¾qnãÚÆÆŒ+ññÒHëxéŞŸ{±ËÃãå‘Ö¶ñx[¸lš€Œ‹ì‘ĞØï…LüúÊ’Á\‰©Èş{`§¬‹ÓjÂú©s@ÙPBì_8Ìd9z2kñbüPW_ö:kÏ@:ï§¬æôT«‡Õšª™~| f¦jÈıìÚà?´6TQÚ×ŠğëCã\l`íºì88<imÍêmyßxºOÒƒ¹¾¶¨JàıƒØ‰L]}ã‰È¶qg¤9{„˜6v÷éäw¶ŒÃÀºÜSã‰¶V&W¨ml 5+ k+ÒÕw
s—Ÿ¨	MaÓÏäw· Qbmc}C#ãÁÀúçH¨/O÷£úú#}ÃıÌJûxéO‘.¬3êOaß®º{êfÖssê£®ŸYBí‘æF¬°£¹ôKfÑæÆP	ÀÔmÈ’»ƒ]Ñ^pE-¬Šc¶tÂıáìöWD
äd2ó—µeÇ‚i™²<ÿ¥hÙ»™@¥¡¶áÖË¼¢QcNÀ\k.'eºÈã<3gÇTW„#Ë(6£1+zCãĞê‹Gú#èCéÎ>Ö7¦kİ¾»#»VöéÖÎyÉò+®²õõÓu¹³qÚ‚ØLÙT¿§_O_v\U=ª:4ÆGv±–#¹!46ĞeÓ88ëÕšÜømÇğiŒ„ì¡ö±Á“Ú¡µc'Òé±mmf²v"ó‡Æ"İ}]¼e}{Škì…Ë›+Ê1ø4Ÿˆ[»N¤É­İ+ûNÙB·.ï;AIs?ó~ïì »¶ĞSÎşşcıÌµÁŠÄ2N"spQ™s‚P“uÜn#Í¬¼‰•7eËM¬ÜŒf!nRÁf×;W83	–kD?ôÓy"û|ÎÁÅ©¹şŠÏòù&ûĞ<ü4àç%úcnw;~¾Ë}×Pgx?ÆÓÔç(~Æñó†és«ù!ó~>ÿ,ÿ°^xR8o‰[´œÅ=âkÖ<ü,µ~ß¦Ú–ÚşNZ'­“eyP~A~ÁîĞ3%xsß²Å›Ş^#7ş|Ü/YÉß}¥¿÷ª1¥­Ğ"¶OsßÀ{…l.,«Jâ\ÿzõ`†PZ6Ğ4/vPÁLx3g¢x=ñ:±Ÿİ~>şzuUJ	+Å¸'É]ÉÉ7é…‹j’]Ä´…àZfYÃÉ¸V,N;d9(SŞ`1s"t™%ÑÂ ‘J¤ˆıÜÅ³IûkÉêªÕ‡Óí1W’5µu‰üã‚Æ=×\Ó³¡q‰ï:×Ó²îı£Gß_×ÒsµnÄÖôÖ+Ò^‹Á,rØ.“Ô,g¹.Q¬ÎØÏÅ§X5±âºâršÌÅsÈÑ¿Ê¡àÚüæc
ÄNá’ötZÆö<p]Š`Ugí£.ŞH]L&ßˆWWéK”µ<£¦’Îø%¢³À±Ó£Bîõ:Í-­­ÁüæÑ˜ÉáT9Æáƒ%³ÈÔväv*Ëa¤`H`e%¨ğÌë$y‡8Â®°N'[°§pÅù#ÌìEö´Ÿ¶áÓ¶42YÓÂ!ş×‰ß~Şÿ_ÏiŠÆP½©¤ûGÑhÛ—V$¸ck~íwäOô5\ç.KWùÖ=]NÊ­ë’L©Éz¹>X¿¦ãÕBcİiq¤ªDácë‹Âz´CÓDÓ„ÚàKøßÉø½ºÈçÎ¢êÏÇ'ŞÌLTWy
+)Ó|*YËt'3RÉ9”F
™-¸T²€2³duøó@c}¥-ßßÕØ–ö”Ôg6»KC»/¬ÄçÌ°Çkf…g÷ÏÌ«,®jİ(›­’i¿è«)y„İ¼#ìsä©‚ß±ÙâV­ù3æ••.vº{gWuÍ
³Õ‚®7*Ñ:´-u`bGôıNíôiúX!jÒ¦vë½mO‚Zİ»¬Â··À¥
Ğ”šH²Ø''2öÉø„îzc¬SFì*¼X™CXç~-æ;wnß´Ó^(“Wë×æš²mµµ;Ëú?¹¡ş !»6lŞFèWî+7‹ôsÉŠÃh“¤öô Ú$sÒ‘pÈÚš•hwQ¨ˆpíî=Q›M	Ã‚P€ù’rI(µ!‘•ëıøÄYt|Rhr9(JW7#¥H$‚ö˜Q3‡2ÉØ¨#oôVuTù‹¤ãyûW-9¸²ºvõÁê¥E|E¨›ÎŞ³1Õİ¦Üï&}U×^Ñ{8SeSTãÅÇ|±5øk\{qÊz²Ä<y7m…İÊ£#75¡@/07N)‘ÎãÇéóæ¤ã“N8Ş$+’b-¶¨…€Ån¡glD´lÔb³-’§¤HN‡ª8ÊqñHD =c$q#‘A8Fã"ÅéTpwËnÂ?§Åh1ZS+¿Ûåä%j£Šb¨‰Ç˜ßÔÔÄ\ÖÛÄd{ÿâihh8ÀÏœñş}]÷ìƒ=n<`?™L†d2G¤3gìˆ×~îHÜ€5X
—*ª«Â•\±QRhòº”DĞ™=äß\-ÑãÇgï›qjŞK»˜W¸téü¼É·èó“NµüøÒ¶¯ïÈé!ˆz0B m³±•Ûm2PãÂ³Á…NØÏVW¹ÂØ>NV?|Uø=|²§°6|²V§-A(l8-JkÙI´B­P&>d'v¿ÏX)-¡Şèó‰…¼ÂÛy‘Z¨3D×oJ*©¦&]!‰×˜:Î¿î{;™|;ã}ıøD2iÇ½¨€óÌáêRxˆT’b‰3G°ÇØÑ–^M`hq'S	õÅ&îå,µ<^"m–JâåªÅÂİkmŠ…>Ü¾«¦f×öÁpÛ§^X6|aOÙÈH&ÎŒŒ”í¹0¼ì…SO´MùÆ#Ø3:Ó5`k•˜ûK»PìJHéT¾«Í†VÓn»¬›vG835Q#oàG­ÄÊlœÌ°n¥2º‘''’úPM2[İVØ¦ĞpËñ¾û†;»—E¸á—ë'g¢›wÖ’û˜—R]’A=6ø 6tµrLn_@Ôd«e·_í0™€çm˜>'˜&'˜ËŸ^‹$éÆ'®ú‡#„+IèG;^}<uı%l­îZæ*®§/mŞ`ë/éşJ¾UŞ˜ó99 („¡ôl«I4-R¬èñV1Ô•)z(Jä(1°aÂ+G«kwÄ¤,hÊ'ùùàà­¼È¼\ºÕ1Zè6Ïèqìâé7V£³³¨}öˆ=~äÀ™)©ÍºÉ¹âÈUÂÇHàø£-M®ÊŠ2õiGqi‰sññÔæ%`-ï[´˜¾´uçüU~Ëü¥±ÂöæYŞ‹¹ş¼X>#GûiïÒŒoÕ°"routİéâ\As±5ÆúKåµÚ•É† ™a&A³¯.A° ²Tpû0sÓñ.£44dØ¬“<7ÁÄÇË3´r‘>ËÄŠ+¹l´ÓSŒH6z
8›³3±…ã~KzIakma´yõ¬ö‘pEş¼d}µŠåµ3ü·ŞV¹ ¡T*®ºAtøí…~k0ÑRUµ¸6¿@İ'{‚!‡ß¥Îâšöäàu¢]å÷+=zcøóh±Æt±Òª²~©»}M¾¥¾§}/û!1£{UªPæ¼è?óŸœÃfrŞcd=5Åõ3‰’5ó¯mw„yó¶o’JçÏ&OO®.›Udo_Nìš=2¿„%zÎ·P7<^§:\nÅ-K6«hkİÄéº)¸‰Û.Ú)n§âö>¤|G¡Š™,¢I4p˜t5 .“â@elùœF¬CF/^tó
µ³H³á•¼Õh–sqßkG¼Ì¡0dê3J1˜ú~˜ñ=2U•+Í²5•:mHAigÇl÷“ÎDu¥Ó‘¨N8õ4vt–ö¾xò±æÆ£c7VVŞ8v´±ù±“/ö¢ŒNŒ‹ŸÃGÉXZ[*‘2‰œ‘HLZ!H‘ˆ`!N‹DÉ)J±ƒ¢&RÑ¸ÆMânò5÷·İ´ÔİïŞèæDT‹?è_äs;}>÷Yå"í.Rê"g\?wÑiu‘
ñ¹ˆè"×GÉŠèH”.Œ~;ú«(—Š’Â(qD	‰W4íP]NÕÕ/“…2Ñdòs™|[&ıòF™bA¾LD™¬ ò_Á	îk@°'í@P÷.  2NªìTe£¬®Q·ª;<­¾¬jªQ‚t<H‚>f_‘Ÿú¨1tói—‹ª2`°ç,/õè¹˜¿:“:¶b“€n­f¶{qmÚ0ÙmûÔqû%k²«©RVnŸªØ¾İg¿Â¸Xri1Q³>‡àä£SF¦ak~¸Ğnx=–‡#«fÜi…Ò‘;g¬Š<nñú’Z
ˆôºÒõ[¶$R»œõÔäıŸøÁµ×ş`àódä©YíNUoÙ2¢{üJ\%lÄU‚bi'5
²(Ïu™wó†íHLè1z‚-Në	6Î®ğJ"ßtÓäï8ù†‹±ô±ƒ-ù¦ZbäÚ2ŞØc¾ÔÒ9=Ø³ÑÆ4+2#L|“¿»é&"ŸºşXo	°¥÷´W1OŠ>G` 6KcHî€CU4M)• )ã=Nì§í(‘S~òŞ¤uö~×í÷ä—4$Œ—×¤Š¸.'³²soJNS¥8¾<TQU‘®à*¬]ùû’sQU!),”¹*dîqyÅòÒ
™LEÍK3©×õÃ¥>Q]<Í¢&¦‰,NJ˜“»,5¿"gt{r9.&îDv—X…¨ì*Ê³'ò›ûf¸C×wa®*šÓÏ¯*b[qej¥Û©Á(yÕH€<WPßY=ùwf‡ZÚ\U™)Fƒ«-»‚Ùˆ}mÇÌ7Áñ¸¶	ÁâtåaL‘EİM8«ï+¬*<THåÂ`!å½¦.ÏŞ°‘öúòˆÇk2	½nEÌu0›¿Ïf`L„Ù20‘#5LrEOÕëô' ¥.—¦“{®õTHb¡söœ{‹ÚGæf5Ô8ùjƒõ+fñ.«0ù;Ê-ŸÛ4ÒQläEı‰wòÏ¢µ¸c˜Y·B{—œCåCsºdƒ²[¡óh/¥ïr3K¹ƒ¡ ‘»a_KíuûDÁÚËÉU+‰óñ$ËØ3ÇU3–›	ìÉÚ¡¢¨}(]Öº’Áæ¹³æø]ş%‰-Abn^X.K7ğÖe-ó–XÄ½¢=¾`uZ:uçtº4]u›Hv4u…˜l¡½—«ºİûÂÁÉlé-×kÖ*Û³c†­.˜»0­:²â)LV"qWøJİksf;E©Âs-érÖ4Ì
Ìi/
5öÖ«}ÇˆØ¶œ£D¬“»L"oŒÍnJ¯ïˆYÅ^Ğ¥~—P§yPÌ¼~…ÄOMfÌ6_ÄŒ¦;Á~_©\J+&ÅVÔm‰*÷z‹bFsÑèğŠM8z™š'2M)æñ¯Û³ºNfİ"sFÿ0¥o–í„³ŞáÉv¤¨’cCÁ\o_Uµíc”L>e\”.]êsZKªëóæml“ÕDôDü¾¨×†9hûÆöèm·Ø‚ÖÊZYÜc²
¦²ùC;Ñ<UÉ+bogÚÑY¾Œ–pÁ¬t˜w3Èbğ€D$›ÒåØëV,ö	æ—§z6‘]¤¼9›Ê()&1™r‰æ“†®ˆRSKÊÊÚùÎ„3PäN<¶ƒÃTÿAıQ—ÿäZ6²[×j+µR?úBŒ¤ÓG‚dHüÆ®2æe{Ë«Ê•S¹<XNy‡ªîF™»Cûâ8¼ÊŠ6ÿ¡ü»òév4€Ãİ«Ê´R“ç3™äeŒ³ÉêÌTHÁu’Ã™šŠ+&¢¿ŒÈ½˜M˜SÇ¦×£¯{J$±À9k&™÷ñÛªJı‘ÅÕéŞTÁæÑhÛPS ¡>å$ŞVşå–L^¸é€"ìõåQ¼itæšÖ"62!«gjÕõÜ’.5DêYÿÄ½ÙC0eóPººÈ^·ÍâTz9!Ô„‰RS6v4å‚Çv¶ŠÆ™Rê\Ù(ábªÖ# Ò~LN¸Ó=)×±¢¤3"Ñßzÿb"é¾ÚÉ F³a’}…	êp}üotã¾§@Á¨ïFI”½®ËB÷Úe31ÛLèìMìÊdòb’-—S8%]şîæ­cÇ¤Ñè¶SéŞÒD¢wäĞNjótWÅÍ§ 9"È‘¿ÇníJ»e.ÈáìwHÜ“';ˆÃg²¢{õr8›d—:§ÿï1ğg‰=ÓÒ³M“ã2!\R×)û‘¼c#£SÒœ2ñ{Œ†²ò‡Iã†!nÍ”hY;4 ¼ğL:,È>™q’'‰;‰ÏID'‘Î~Ar
‚$™pJücºÕ‹£PÔ„ñ‰ÕHØú¾ß$8M‚É/cJFy'&y^Q ‚§N .‹ e‹d1±¯[5]Zâ³˜uñLfz‘¿:si¿F_Çgâ¸²¿bÕÏÖı˜èÙ'™Zá8«{Ë(/–NÌn,H7&•'ì¥•)ß±c¤Ó[“ªTfoXØÙö75Ítş=B_¼O*P6¦el|—i¯d2›l½8qlëâOâ
ßˆkœØ…xçv%”c&%°¢¥Œ¶x/¾ê¹%šón.Çp1ô<köR–JT ÁK÷úºä¼—óh^Q—\ür1å‹Í]ÂŞ’˜Åo1q\a°Õ¬8‰Y÷t¦¸¸Ïf~“o¯ÎL¼ÑßÓàL™uq\òq,_íûÏÉú¢
©@:æH54æ7Ìó„º#M]Uê±¢
k\2±AÀÑÉkÉ_Œ¢`Ìwzü—‡Uğ¤ò'ÿiz¤b_PŸ.´tñl˜ò{]²‹È® ‹òjìuªÁ¢H½ÀåæÌ¦ì<´=»Br|`lFÚc»›[úkÜÇb5ö¨tŒüEt\bgRåæ—$Î/ÌëÓg70nØ®
9SŞßmÙºÇC<½˜¢÷u{Md¦æÀìÚ>—HLÅ0³.AvÎ¦ÉhëšY–bÅmkêğxo]*U_ŸJÕ~Îúù%%ó×Ï™3ÒQRÒ12§méÒ¶¶®.=šGz„Áütå.ñ°H¡ÛÊ„»221ßãíÉ#.	glçÔ\ÅÙH—sÚ¦l\×åŞPº²fÉÏôD}oÁÌõÁZß±éùšpmİ¨²ÿ¬Ÿ=ÔQbÏÒçÙ|]<o$7£§>P (­:@a§š€ëUë”£¡›±ˆú6ór¢OºoéVó;kƒR±åXÉækaa¡•ŒE#7¹…¼+ù8#&…ÈRŒùÕ‹h«28šîôX‰ª(á<Éç‰Ì“¡¢( |Ÿ7ù~Ó_ÀûıF×fŠï+—Ë—–Ó’âbO—¸/î7ºJ 8*ª,¿E½d»ÒĞÀŒ‹C×^Ú_9bˆÛ	"‹«³Ë‚Q1Åf¶:ıMˆş¡v:a»üƒGß)-,¯ˆ4”¸·TõùışÙ±v“ôV§‹ä×µgT_¬ó:»G(¶¼âÚØ‚ŠeTŠÉ&j¤4^Òéå÷È
ja®öy>³ÚÌtÈâ ¼Íjµ{Bê1P·UèµÙE FÌĞYßHN;Âù³™T6ypÔ¹0e¸2«œ1÷Ø³Ï†“Ş”Ëh®šİYå Ÿô>°ÿT¢^àGE{xÖòdù©*úXÅl…iÖqÙXµ íœÉô±*~ØX-Ê²‰%›8¦¨ùÊÁªŠèÜ•µ¤hr¢#	âİ¹wyÈ¬ÂséıG€ì¶“õ&U	¨v•~F}D}Så
Õ¤JõU¤~YuâÏA3Ì8[>ã
øxŞ®f³—ú’Ø ú9pr °y2ÁqœÃ.eÂZ§8AµÈ8Y`j’ÖçéÌv\õe¦ßn¬ş°u/[ö›KR—VºlıûÃÔÆÄƒ–@~¾d+ÈXîOlLëƒÅ«2}Ñh_fUñƒ“ïe{Í™°×%p2½»,Ø–C$ª‘ØÑ""Šh‘ì'ş£.Òàšï¢®›œÄä$µÎv'uÊp'Æ’ôÍ˜]œjhÀôÔº	/‡,İ³P³YB¨N§~ù4|èwäŸÈdƒ0X8Kn.mØ¾=÷¦XQ0á÷½ƒFMf’™í~ï;x²íúI2ƒ•¿w‚w¶Î¿ìeÎ¥w:‘JB;+|£jYEÂıYŞáòXm>‹ßÄ;İ^›Õërğ¸quÔ‡QcÑİ‹ÊFo»oI´gåª²òkú»£ÑîşkÊËV­ì‰.¹ï¶Ñ²Ewg?H}¨±ü&ıøOTWg©ûØ›’ JŸP¿¦¾¥şJ5<¤’=*™­VœP¹ÛÜDuÜı.Õér©ßåÈ(Î3œ£pÏqor?çwqdG’ÙâÇ!ä•†8BıÀ9§WHÀØ
†§á7¨û 	¸¬¢èbªv…CÔè{XÊ©*ïF[å^‘—€¥+úHQ”T*³|6L¤˜7±÷19‡Z=ıæò—-ÙT4ú[µL¥nu•dúåŠ¯bíLWY²©,2Ëá÷D%q95RX”lyŸÓÉÉ÷T4•:lü¼)úÓ—¼õÁáõªàš¡ÑiŒ²ß¸€—¨,#H‚`Äî˜X‡M*Á|“—1ŒÜcÁÔÃæ¶¢Á˜ôF2Á&§7°£ğÊcÜÎ0û«•L†ùgN¹Â3P|ö6å{êìöyù““‹]³æ¦?%“/9[—­,Ûßí^¾4´ŸE§Hî­O:Òe%bÀîî2Ä¶ÅÅ¸ìKåâX/€Ã!zóÅ^»P%àè†Df"1¡6ÌN¤¼ú«œxæ<fàzJæ`kœÙgNZùDÿ=%ÜzA%ÍfÕHE‰;ÕÓäôUóÊÊò‚>gSOÊ]RAFjÊî‰·Tzo()»¥¦Ãïï¨¹¥¬äoeKü²šÜÛ¥Î)‰J¶•*áJ ëòÈb€I(†ŞXÌá°zíyUyy\Økaïœ2WHœÔ%>‹z+ÒÅ”²¿heÂ3G`bê”	Ÿ"ÿ•È¿ı«³-÷!³lı/&Øf0à¹A¿2eK¦j x 3û3“ÅŒ'f˜y{?&0™ŒúÇ™‚É„‰»¯,`21‡·ŠWqŒúI0çJ¦9Fc Ş,
ìÛÅfqšÃl6™ÍF³Ù`0,f³ÁlPVo³™/q +L†œØWrX³Í‚•ÁÆÁv‹7ó¼‘çŞ`åy0½Gi›qÈ2©¥,‡1'¶^2Í!²Xx›ˆ|DQÖujbİxA0	‚ç+« Àzı4óLûå¨H\à}8‡5Ë!
²õƒÂe’€•ØÆ!èŠ,\ÉaÌrX®æ°1´ŸE¶!™h«mŠC fò³Åb4Zpµf±`x¦K$Æz‡b¹ÔŒ¼)§šËÜ7‰Ñ˜Á&*ûn‚’MÑ}ÃŒòˆ¢EyQ4E“"ZE¦<ÖOÑÂ~ùëtüOrÈŒÆ’¨°¿7±YÑ’KV‹ÕÊ[­F£Õ¤X­VÀ^X§9\ñC9¬ÂÁ^.KV‡É¤)Ö†ˆzm—8l¶,‡‚ıcõõRKèt`L9õ_ÉŠ±#‡İæTbW<ºoLu’U²áªĞl´™]’$ Z˜.‘9¼—s Ó)Ë!]Í¡2ì’KeßÁ‰ârÙ*KIæMï–qŒ6‘mä`õ>ŸíjóeæË9TäP$ƒ}ïD•ı‚ÎaI¶É²(¬é:˜-æœú¯äpâü€ªìsb‡T;Îö~$í’İnµÛy“÷Úív@óØe`ç°>q˜?Èa¿šÃÅhxpØ}.ö;zäeŠ¤Ø­JCAcK—qäçËÿKN{Àr(àråóq‘™G•UÅª(¼Iá½Šª‚U²*ŒCf—sˆèÇ¼ÈçÜH÷´i7£À¥<ì[?Wr(È¡Jª*ŠP‘Ã&Kªİƒf³¢G„‚öK-]Æ¡^Íáe4"¸Õ|/’¹èõA`ãÈŠ}Vv‡CÂù\À	Òá@cÛeú*ëÃAåRK8@·êWáğ ‡Ç‘ïcßXºœ]À©8’“qˆù§sšCaõ‘Bõj!çF Óá7?€9¼Î Ÿ}Ê‰^_l¬Ú˜¸T—Sr¹Á)æ»\.Ğè•ÕE—ZÂ  ‚MÈ™øJ £±‚ÏÎcß³rƒßi+Ì<n‡Û­¸İV‹ËVèv»Ñ	T7ãp°úXô2Sî«9òü®p~–#ˆNs¸<[ñ ‡9<ÃU€şÍêKbÎéÉ"Ë!éíz®æÈg4Vx"ì;bÈË‹«2êÕíuz=Š×kµxlQ¯×ŠCõºpãde%®KÃ’31Û,ÓAFcƒ|oqˆ}Í‹^_lÙQ¯ŸËçS}>«Åk‹úühl§Ãç	ƒÛÅd¨Œ{¦'À  ¢,æLÌ6qš£ı‹&\eúË"P Á „Ãq`ãHÁ>ûò<yG `rq /ngÀÅˆ«¢G$¾éÉpğ€U±åÔ¯{Á4G`jn‡Â¼Š’¡Q"E	`>î@Ë+ğä»p<Ûòíñü‚T'û™çcõµ©À¥–pğ€M•rªÑ-4ÍŠ‰!GQAU)’Eƒ+Ióq'ª® ‡<¡]
*U¡p<~_(‡‚€‹½¦¨Ë¿Ô:6H=ä†sšæ@Å”¢L%áT9ö©¸Jãuºÿ¹ÑN¡H~¤ĞWX¨È…Ta$‚Êó†+ ”C	Zš
§  C€İ£_Åršæ¨\Ÿ9¡2Ö˜B¾ŠbHT7—>4UQIaIq^I±Ó^ìY\Zùá‚â¢Zˆú™e	¦‰h-gûª¶Bë±}:û—¶—mƒä=ö7´¹í·ğW72í¸_Ê™Ş…,GAŞGO¹j£õS®õ!Û‡Üÿaı'ıïô²ç_ÏÊI³eôIè¤)èän‚Fú^®ìæÜñ¬kg^†ç¯B;ı>X¸ç¦Â[®/;`eî¨/ÔC–½…^ƒı|*ğXA; ‚<Šm,ÃóÅX†:ÖNÒ<o„vn5Öa9]£ßß®·…÷“bò"ÌÅº¹4†üö,àô=ˆ odšŸYePô¹ÛñŠ¢õĞ©QÈô'Ô6«•à©iÛÍ'ërçL$“;§` ı¹s‚dfîÓf’ÈczK"¹s–{Ù·Ô,†}
çÎ	à½¹sög1×çÎ9˜5¹s:xAîÜˆ÷¸sç&=ôöÀZØ	[`±šÙw&aª ê!uEmhº¶ñ8ŠW[`1ÂzX„×C0ïúğgBÓmN•\~_–mƒ=(ÿFlk–…Ğƒªp<UãY2lÑÙ6Â:;”ã«dßŞÅsV>Œõ;kwÏ¯ÇóQöÑÈÕ®·7zÅÓëôûª±Õªµ;·Œî¬hŞºihÅğõ;6nİªª¬Oe‹C¬¸upÓèÖ-‹×/šº¬F¿“dËZ¶nÛsıÆõFCÉªêêPËà–­[6®ÜÂç*C¡E×oÙ1<Ú¹ehøúĞè†á©¶Ú·nÍV¯UWVÁô:R»…ı?Àn/€@8BŸ
†æÚĞE«pOãÎÁ â6Ü©vëkÚO±ÿá÷Ì£Áª¹^t1Bx¸‹˜¡‡˜ğ(àÑˆGê¬	K	Èì¯ƒà;ˆ¿!†ôô¦ƒÎà®-¥ÁÑmr0½ÍîmßÒn,®
·”×·’A,îï
öö{°¸Ï·v‘.,^ÔZ\Ğ1ìÀâöÖ¡`g+iÅâæ¹JPœ›˜Ëñ¶2¾ÇXF{´,(—AXfé1—™zXÇaİòî“u#9IîZxÒ¬-[8Îw®'·u3Lw­7İ:=+Wõ äı·Üq4ç/Ïïîÿ\~ÿÂñCxù'ÜĞÜC|j[½ƒÄã£zùÀQ?ìİÁ.XÙèÎ¸w5ü'Cw²
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
xœ]’İjƒ@…ï}Š½l/‚ëÏÆDH´/úCmÀè˜
u•Õ\øö]ç˜º ğÍÌ™=Ã¬›æY®ÛI¸¦¯
šDÓêÚĞØ_MEâL—V;/ê¶šVâÕ•ƒãZq1u¹nz'…p?mvœÌ,u¦gÇ}75™V_ÄÓwZX.®ÃğKéIH'IDMíôZoeGÂeÙ&¯m¾æÕ<*¾æ„ÏìÁMÕ×4eE¦ÔrbiO"â“=‰Cºş—÷VÙ¹©~JÃå-—Ò—ÉBŞ–)@èÀäGLa:€"P
Ú3è©Ğ3x™B	Ê@>èÄ´E.ÊØúêqwsü˜ğÈewú;ÖÊ“ç!˜Â®á PbTå#¸»ÊAw!ãl=*È*#È¼(Üí×`yYÃò\î;®®ÆØõò›â½.m5İŸİĞ‹jùş ZUµ
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
xœí|y`UÕÿ÷œûöõ¾}KŞ»ÉËKB^ö@ÉË¾“$`4„¥¬’@AEbTÄ¥îZ[µÊCv7¨…Ôv*ÚeœNE§Û8Ó¡µ¶:v¦äş¾çÜ—˜¨Ôşæßüşğ¾ÜÏYïùóİÎ÷Üä ˆ*€öùy…ƒv1 1amßÂÚ¶îßïúÏë°¼À}nÙÚş`‚z o-¶g/Û<,Ü.`y u.ß°bíæ—kOøoĞ„Wôm è¤ï2*+Öl]~¾fW@Êa€ÀM+ÖnI*ıi:Àœr Ã§+û´çşáCl¿û¯Ä
»Ùú_ 3±œ¶ríğ–üwÔë±ÜsºqÍúeıçşù½…8şql?½¶ËN÷6@ÓÏ±,­ë_;ø×ªÍXşÎoÓ†õCÃò5ĞĞ:ÌÚ7lÜ°±ø—·bùn Ám${A}_¢£ØãV%%ïâ38jT«5PäÕô«¶ª­
ˆŒ— “ Tx^– ^ˆŒ¥:z„Q­&ìRk4D-<ÏHS=§/5¿jo…ïë^å‹È7†0!ÁŒhâh‹ü°€Ñ
"¢6DØíàDt‚Ñnù¿ÁDG/x}àCôƒ_ş/@ 1	’“!1È1!D	$ùÏ)ˆ©ÃŠ˜aÄDäO!c¤#fBâ˜˜…øŸ…,Älˆ"æ@6b.ä æA®ü	äCbä#B!bÇ™P$³`b1Ç(F,…Ä2(•ÿ³¡ñ2˜Xåˆs8VÀùP	ˆ1UC¬†*Ä¨–?‚Z¨A¬ƒZÄz¨ClàØõò 	›¡±š[¡±Zäa.ÇvhCìàØ	íˆó q>ÇĞ‰Øór\äßC7t!öÀBÄÅ—@·ü;¸z{a1â°ñJ¸\¾ }Ğ‹ØW .…+—Aâ ôËÿƒ—ÃRÄ°q%"®‚åòoá°q5Ç5°q-¬B\«×#ş;l€5ˆWÁZùß`#Ç!X8W!nâ¸6"~†·À0âVØ$ WÃfÄk`âµ·ÁVÄíp5âupü¯°®E¼ãNØ&ÿn€ëo„ˆ»àzÄ›`'ân¸qnD¼™ã(ì’·ÀMˆ·ÂnÄÛàfÄ=o‡QÄ½p‹ü+¸nE¼n“	wÁÄ»ávÄ{`/â½pâ>¸ñ>¸ñ~¸q?Üƒø-¸Wş< û„ûâø0ìG|¾%ÿ<
 >Æñqxñ	xH~¾ >	"~Cü.<øâ{ğ4<ø|ñ{ğÄg9>ß•ÏÃx
1O#„gŸ‡ï!‚gÃsò»p …8â18ˆxñçp!¾ ‡_„#ˆ/!ş3¼G_cˆ'á8â)8ø}xñUx	ñˆ?ƒÓğ2â8‰8Æñ‡pJş'x£â‰tòø×èkOôµ'úÚı/{¢¯c¢¯=Ñ×èkOô¿ï‰˜µë¹m¸%¹İš¸}š¹MZ¸Z¹‰Ü®lÜŠìÜfÜ6œÜ\\ïİ\Ë=\§½\w}\_ı\;\ÿ’¸Î%sr}
qí‘¸®¤pHåæòNãÒpY¦sÉep	eryÌàÜÏâ¼rÎfs>æp~årîäq^äó•Àb!üH~=Ñëò9ôD?EœoËo£'ú'ÄxW~=Ñ¿Èÿ€è7òß£'ú7ù§è‰.Èo¢'úq|,¿èÏˆ•0.Ÿ…¡òëPEÔòO šèå¿ƒbF¬%¢üc¨#nùGPOüòkĞ@’åB#I•Ç ‰D›Éù´ù4´’BÄ62K~æ’2Äv2Gş>t*ùt’zù$Ì#ÍˆóI›ü2, ó»ÈBù%XHz‘+ä¡›ôË/@Y.‡Ådâ²ñrr•|zÉfù(\A¶ÊGàJ²M>}d'b?Ù%‚¥äfùyXFöÈa€Ü)ÇaÜ‹¸œÜ/€äAù9XI•Ÿ…UäIù{ğòâjòœü¬!ÏËOÃZrq9!?ëÉIù»°¼*®"cò“°‘üqˆœ•¿Ãä§ò°‰œ“‡ÍägòcğMr^~¶_ÈÀVòkÄ«É¿ËÃ5äwòCp-ùH~¶‘O·“ÿ’€ëÈ¸ü-ØA	âõT#ß;©ñj‘ïƒ©]Ş»¨ñ&ê—ï…İ4(ß#4,ß7Ótù.¥YòpÍE¼•ÊwÀm´XŞ{èeòíp;­@ÜK«ä=pmoƒ;i³|+ÜEçÊ·Àİtâ=t¡<
÷ÒÅòÍ°^!À}t©¼î§Ëå›`?]ø-ºNŞĞ!ùFx~S¾¢W#>L·Ë×Ã#ôÄGény<FG§{äëà	z§¼¾Mï•·Á“t?âwèÃò5ğ]ú˜|5<EŸD|š>-o…gèy|’¿	ÏÒ£ˆÏÑäÍp€¾"o‚8}ñ “‡àyúcÄCô¬¼Ó¯‚#ôâQú3y£ïÉëá8ı¥¼NĞßÈkáúïòx‘şñ%ú‘¼^¦ÿ)^¡ÿ-¯‚“t\^	§Šø}A#¯€Wƒ¼~ XOyÎny Æ¿¼~(å¥ğš"÷}}}ı±‹â-àíäo¹YªBïÁêYÈ2¿ù«n´£ºÏ¿?ÿy±·ñrızÄ?ÈãBÕ±²¼şB  EÏù±<.Ó§XO´bQn¬üşRøi$Ó¹Øÿè¡W ü=úT§\CkéJz^Ğ‘ËèË CoÖ:Ò„¶6eÖNLè} /Y‡6{½I~âÈ…óXÛ67-º}Y+ú†Mhï…ØÖˆ} ß¨@½ïÀ'oB‰?@è	7¢ï8µëğ¹,ôåX•X\ü€,€O0×Ï·á¼­H¯ïRPãÈÿûW/®W\GNsC¬²»kÁüyísÛZ[š›êëjkª«b•sÊ/›]VZR<+/7';3=’Ny6Ñj6ô:­F­(ìºp}ŸOï‹«ÒÃ9¬îÇŠş)}q	«ê§÷‰K}¼›4½g{.ÿ\Ï˜Ò36Ù“ˆn$9ÙR]XŠ¿^–“Åİ˜¿­6Ü#Å/ğ|Ï«ÒyÁŒ…”|Bªó®¬•â¤Oª‹×o^9Z×W‹ã4jÂ5ƒ†ŒÄFÌ1Ïo8H2+ÏĞÌºÙ)èÌŒl\ˆÔõÄ;:»ëj))=¼jøXqMM\ËÇ’V±9Ã-ÒÁìS£·ai_Ô4è¿¼;.ôãC£Bİèèî¸-Ÿ®Ï¸úW^\ò`<;\[†q°–y“H\ÃÒèÇ€“_øé5ı‰MDüX–-q’MØ>‘œÎ×—’ÂærËñ,ÅB|Gg·R–`iàyˆåE{â´µœšhqu±–-“÷…S˜¨êú?›Wzã;–J9ÙÈ}şÁl—âBzßÒe+YÚ?8®­Uø¶ ;«ÅL¬?±ÖºƒùyØ¿¿±Š±¡³;Şw†«•X!1¬šßÍI<wÖÄ¡oYâ©x^]-›—T7ÚW«Lîì>QËûgJCEÁô°yÄİ5(”ôºÑîåñP_` õs¹ÔH‰Çz}=áîÁ&¥°Ÿñ>’KáùS¸¶ÏõèÌV®è¤nz˜´°BªGW—cƒˆââE&Ñêr©›`¢RIô`¹iã`AˆÔ4²&=ZÓHéIQ®¿2¥@bNêH\7e,+&ç¤Ğ¹äÔ”ŞlB3¤ºÁÚ)œ6¨:1ÁÄh_>OÊx‘ ŒOè˜8'š„Z.ÖQ†W1)z¥8tHİáÁpOu(ÖÑÍÖÆxÍåÛ2?ÜÒ¹¸›K;¡%¦•”öÒÉ¶D.NkPë£	™òr/O?×Ü4Ñ,êÂ-óGÙÈáÄ€ 6ÅU6†ÆYjŸ™°ßztoáúş°$Jõ£ıÇåKGÆb£êúVÎfã„›FÃó»Ë|zóº·®fäìxÆnYP“Î§ú`˜ŒtŒ‘‘ù‹»Oˆ ÒÈ‚îƒ”T÷0í÷®Ä¢³«“s®íY9Ú×ÃTÜÈHü!q®ÀCU¸â ¡SÜ¬ÃÕ¬¾’ÕW*õV¯E±7Éa;‡€çŠç‚‘‹5Ò¦|NL|H-ÙÇ?cä×ÔpÉ4ñÖÿ>àç‡ÊGµKàŸgÕÏjnÒü‡¶Hû¸îyİóú+õ/fş`øƒ1?£S~Î›Î› ÄCo]3ãÌÛ_i-ÿ|Â¬æG£G»YúÓ¨‹ä¹ÚB„Wqåz%–UWéïZb¢úzª×\Otš]¤M»Ï.•*/ñüü)È/²¥Ø2ğ.${Çß¢¿»h/¤£7³q– ü#F	<ÁÀcİ§±Õ"´©´:£I0‘`²ÅLÍ”LNÁdÒ«E)>·ËnóÛ ”dQ<jó;m~¿Ç!ÚˆM
T…‚níQ•€ÊjONré-F•İh´«“¿ÊV-V›«MÕB­‚Jå²{ÊòòòlEâÅS§NÙŠlEEJ¶’ˆçzÇNŸÙİ&Ş}/‘#ñŠoaıéÏ×ä“()*)B„ù.áwI¿‹LÉÎ]0w½îö;æ.h{ ï…ö¶›ìwµ/xñÁ¹’ñcÇš5;¦$ã­‡Ù°]n!¿¬Oı,f´æÛ¡ÍêµA›á¸üá!·’v8¡U{y¨·¡D´aéıCv¾sÈÆÓ[Eh°Û!+iã)rœbÇÃ6;´bæƒ‰ŠCV~xÈm„¥vÂÒÙ©S¡KÁB&ëÉºzñy½Î
¦Íj¢¶Yô=ÈiÔ‡ŞgÇ
ò!Š‰~á"Áåt{´¹dÖL{	ùmåò†orCjúı÷Ò_VŞ¶ïáy]#•™å-z…4Ş†\‘ÏÊä2Áˆ\Ys¬¸6Ñ­¶X;çÉ‰ôÓC	^År-lõ"›«ˆË¡^ömvÒJt"®‹5™6ëÔ Z{ô|ŞcçÇP§ÌS[!Ìš™Q$.'ÕN™æmÓf9~œÍ¹Ï-Áy'@…|4£Šãäb6´iÔÆ˜ˆŒ7‚FfÏ-$ç_¾û:£Xb´BÉ˜ÚÎöV:S¼¢°1­¹¡*àÄª+lôEH/Y„¶‰¹Ô1“µ¬yXxC œªÉòĞÏ¾Ş{ò>ê@Å\ı‘ó#²h>]+ÿÏQ[‘²/fb&G£p¿Şªy îÌ„Ï]ˆä{RÓgÍ,.*t»œº#IŠ&%¥˜~s09-#´vºÂU’ª£é( Z°Á•ävcF²ÃâÔ@S{4:“ûõò
áezÏ]äÈ	è@^è‘)-:Ô¨T&>,,8.¿É4lAB‡1}'fE9vf:]ĞÚáEı®L´U²¾¨uLØ§8†µÅ¥˜›ÅÌ$ó¸|ê‹§ï³13‘§0-Ï8.¿ÆÚ3í¼,òôÍDû;Ì
Òã`úZ¬;¦•b)œÉÀ‹Åp>>”Êf–ÊŒ (a.èÅ’™u$K8„/aX¾„aZjdÈ”‘«i>İpClin¾Ç&â‰Ã&î‰Í¿G§+-ŠÜSº°eî~³(šÜuû)¨›mj3~Š¤ısVæìÏÍÚ_„wámôÂ¶2tmö²2ñô™‹§Ğ³å‰
™XÅÓ¶²¼âÅóïr'†6Ë\5|Ñ&¿äb–IÍ°0SŒ
Ššá4h¹E…tÖÌ\NµP—3ˆÅ%Z‹NÍ¥‰~Lƒ"…%3‹+I.Qº¹éÑJ¿§"Ü²8£ùµ3ÛœMj³3«<Ó‘T¹¼yÑ½ë*2ê—^6»İ¨Õ§F¼W÷Öì|éêÇã®Ù+Æ[œ®ÊÔ©Îhm¾?'¶ØººÊVwØuãoZ-&{AÛåÑ’Ë«#-Û¾½¸¦¯"hU5Z­jFç–öÜwÅcå}suS»Óæ1ş–ªRg·Î(.@›ÈG¯ò	úZ-ÌŠ4j­JƒÖ	Z<ëiuª}Úa æø>wîİ×'¸ø:šAğ&¾wm7İdW°6ıåÇMè¯şG~\ó}~d=< ìƒøòa=¸‡8ğ>œõD“PÜÄ¬i©üGÚDà‡\øİ¡P>É`:eàjûa,¦‡¶T¬6Á%!8™MXDÔ1K>ª¢Åka9´93ÓP³sz/>¯Ğ–Íİ&3öT†ÈõÚÆ´!âe›FJjê‡Óé`·®÷8ĞLb>³ØrG~ÖNc^jdÄ™±#8"˜ë3²ç#šN?tBå™ÊQÔÖ3¨¨Ç¸zë¿0f/Û-2@4á?·iôªs	×ÃIóÂöT½
ò™–)‚»¹8»2Ó‘³xdI Ñß¦ÖêÿšUî&jU¹Ú£/»¼*¬s…5Æ€Õ™™TX;£fÇ@…É2>æÉòxòåi^[Äñ)¥ÙMı³\Ñò¾Sş˜V	:pBÄ2Ò8?B
ŠfÆ*;sÌ°M¥È:#óÜÖ-Vnëèùçj¹#O¹ø‚Ìã1’²ó=Ñe€×çô9Gv§ÃîxÄN®³{ºÃÙîK±›;½#à:Ã?sq¬²ˆ…/½ïND)<jáF>‹¤‚)³LÆÇG‰#U£‚dÂšIŠ§<5Z•åÊ^¼{‰5-6ìO
^æï4øÍe—ÇÂzOù£Å™TP›QwıàAgÒÑ_‰ã¯¸ãÏRUNKÿ,w–ä@^ æR'X`ÜÊ¢½cF³…mÇ³¾<+«059l4A«‡q+´|ÈzŒkÉØ¥°H½3ìÒ`	Dv:‹a$±F|…¨€ÇôöÆÂœ+ª×Å³ÑÊö2¾^<Ã¸pºpÒÙ!3l?WÜ–cR•8KTZSñd´Äc!?™İWŸ¡µİá9ù©‹š½Ys74Ì¸,bO-méœ!Æà¬¨cF$Y£sö5r#z§Í,¨%¹¨6½~çÀe®´<_^U¶×¢¦:ƒà™²kFu»Ñ‡<òËµt.Úr*ä­ì…~¶r‘§ï°ÍÃÏ4DÙL>äŠ$2UiÀVÈBCfĞ"Û]¼¨O9^tÙL³¹"ú™bú½Œ·>fõ¾RŒC|™ØÓ+!X{+Š1“íKjâl#I×dh22¸=h\×zHÌC<înê.’B¡ÊĞ•¡õ¡ëB‡4¡¼¦B‰9€ ÙŞ(ÁHÒ<OsFÖˆÍí¶u„G4yúJ}»^Ğ7Ceï™•¸!¡¦V^‹2³ë-D•}½·WÑYFÔĞûù­'qyP$•dÊ&¤hü¸ÙğÀ¬íß1¹ÅüxFEN’Nå¬Më\”½ø¦Å–0jñZszõÊ¹ÑÉaOëöÌ{“Áo*^\•–·Æ™>3Åatw6¡ıÏQiMºñ²â…å)Û\›ëd3É§ªuK
ŠóYüÕŠ.¸ =€†cµ./‹ÌEñˆÙâ4›-f‹c§1édÒ{ITğù©ŸÒ#œxî"„œÂgşf³¨±6[š}îAÓAh; cĞ2û­DwÈÃæw{'m¸øÂë	·ÈÎEaÂ‚µB†¦afÁ­Çúc"NU¦Ãë½LkÎ.÷ÙVÒOÅñ?ë¾èœ´ìÒñO>IšíÏœ¥×ÏEíÃµEô}Œ%­°0VÚn»ÎvÀ&hwZÍ!<ˆ	ç/€S€JhZÉ¶J¡Cèö
*Áf¸Y%4Ñ&ÒÌWPYyYÊòª‰=Œ;ŸŞ¢°£(ã³€RóTï¶^›'”éóHYTwE’OŠ$ûƒdª|‡\Kºq66H†1W(†;Š9ÓÆv(Tr3Óbjv~LáQ”%a ¦Ãéh ®“‡œ6àm!ïÍv°ªmMb“~DgQÏS&c6Ÿò»?Q˜Ëf¬„D	¥+™T.×L_Ås–”‚Ú[Ôä2¦:sò,[zÅÄšœ¥í…ƒ®M««/#OYŸ¢9sQs¼äïN€½î„÷cNY¾#Ğ˜,’ƒ×>d­BÂşi¢Ìw…ïÇò-l‡ÇÃS²1ğa1Æ6$§$²,²Ç)1ëŒ;N9¨yuê°?@ØÁéTLï%HËIÚxµÕÎ«ß<dQ*™©ŸóøÍC>PÊ^Æ2À'b–DsB8&¾kGOc])ÎSÇæ©‹¥cÀ!I)Ğª“üÄ©ã×±‰ëØÄu™8î¤ş=Õû©×{ˆ	|Š"…36âZÎ>å¨·Ù¢w6;šõMº¦ÏL½ (câçF<÷ú„Âş¼·ğ3wc+û\|v²uª’DƒJŠğè<aP˜%nH©¯œe[çªjlJ”eYÃıÅ•Ì¼e¥E¬ªÜå«kkOí‰ÿEÑ¡w‚Œ+6ÌbÁ–¨Cî&'%	¡P0ôí\Ÿz{*MOß
I0¨Î1Gtz§N§×é-;ÕeÑ¬¬#9ÙÎœì“9$'}*›f—f¢?UÉ#ùÙÍÑæ`sr³¡Yßì-rŒ@"ˆP®vOÙÛÜ˜~ˆLõAÄf/óæõöâáŞ>é–XˆA¸KÒLø$¶½j´ìÄü¹*!ì`şËí©è“Ùs"¢VƒŞJmÖ»Ò“¤r'´jV6é’Ï—'~£wKÎê¬¬Ù6C8gurç¤º‹¼èÇ<eI4¿è3[fO‡ÕÌNv„ıVz¼‘üÉbKöjí¢)awùÈY|#Vé§{ìKŸ…¢Û6NŞPğùPâ¤„~}¶ß,ªŞšª;&\İ„¯æ,R8¤¸é«¦0¤HYæ4p?ıTï–ÜÕYÌKë4	7íËÙ„™‹F>á£5êDUI]èŸC°ÿX0†ò¡jhX€àag€íû¾;ñ’ƒÛD¢lQÊ±sÆ”ä‚äõ²7^/s
^ö¤wD×!²ø‹Õókb™£Ø*°˜ıê:¯¿5åôˆ¦ <²¸2ƒG’é‰Í˜8æõ¦4nìäX•ÓPàÏ.æhîïš½cM½‚í3;—æ•+ÈN9’Ü@KqåvÃÅXÈÇNÔ>æ¼1‹\XÎ‹ŞÅ›¯W–zØî€Ö‰µ›KyÄ­/EĞ±’…9–´ì¤Î\ìa½¿	ûğåMŒàMÜ½	.êË­Œ×ŒKêˆÃl	[Âá#¢Õ)Z7ˆÄ*q‡õë›VÁšfm±´8FÌîCgxT”&ŒS·{{§†ê¢—zQF&Ãõô-S«)Á:Ó(rMAC®'kÑ®%F¿!ÚûDÖ²{cÙâÊTC 7Í—…RH*¨É¬»~ œÒÃô›}|&%Ù‰@]¯JìMäŸÑFl0;Ôô©‰Úa6™X-N«Åj±[šÍÍ&~ÄªfË8ƒ0Æ1ù6½#F',&Ó²(,aæd³)˜ìÕœ3½®V4åÌË©ƒªÕB§N7a¦ŒúZù#òSúx`0–ç|ÄE\–‚A¯ÑMZ“V{D£vj4jµú¤æÍ{A#xMjĞh»uMNú;ÜN×R,+/¼{†[çù×{Ëò‹Txü“BñâÏ{Ï$Şp•8JøK[åMF1÷Ç[ê-«û3:–˜Ò²’K­Zk£¥ºrFŒ¼,>:÷7yá”d‡®]ïbï"_ÃÈ}&Õaä~<––Â^.Jü,¤öyõ¤Íc¹|S[}â£Çfv¤†D l¿¡ºù¥$„ $ûÉÉ~#ÛÑjPÑqñF ‡&moAlJnrzFüFÔâ<M“º	”—Ú¹PÆÆzÅ1[™/o·WŒîŞvšD'3Š†M*X$±oMtÒiFQP ¾ôŠ<IÛoÌ,kÈ’bMİ%Iùx4HuÍîL‹ä©¯$:«kAùõ›—Ó¯ºáæÊ¼ùsÂ]«ÎXš»•˜FsV3¹.—ÈVÈ‡?Å¤¶§e°P.ƒ½tÍ`ï22MfhÍô<òù0½Ï¢Lß9l0B+¯ÀNÖÁÊÓOc‹™I‹<X‘ÃfSaRrò+YQgVV4šÍÊôİ““™–îÉ´;¯¨5NµÆª	iòPyÔù™n7ìS;ì•19)*dåãÇŞ—ÖcŞgà¯c”÷h2ü¹P6'•çÜØ[g&÷Ã‹gÅŸãˆ&£Ç³…Ó^ãåàG–
á2¢EWhÅÃ‹²!²ñÍÏ2•¤˜½]ŞâNOv¨¢Æ”YmÅ*{ +äÖFÄœ,—M£Šª¬‡ªq®.ªJI'í¶@Ø~8·j†£IëÎí¯n¶Ûòü¶TÛ~‹[/9iSQ¹'rØjIJ§¨§çP«™HÙ	ÈP|[F"äï;ÍÊ{ĞX2İÃ<ª»ÓÏB:7’›UºJ³]™(>—qrÀQd‡L=;‘ZXLÊÖÀß®Š	jÖ5´	Wâ-«3á£™5a…òs>cV43gRx•¢Q3™2‘š
Œnwş¾hRr–*Mcw¨Ñ‡1ù-Fù)¯Óğô?Exyâ˜øÖÅ³(²IbSÆìbBvÓ^|Á+â¢xÎä"%%ìwÅ,Ç3À7>+a®ÄCz<éIŸI2iFÈ¥»„$µS%™.ıUI²+	ï£AÃZş[JİÂÔ?yáÃ¥ÿ$FÅ¾|Dƒ(Ğk°¤TƒšgLF…†?€‚ú‹4Œ_EC«e4´ZFÃ Å’Š}Û™Õ±v³‰¯€}aûÒ4L-¢J¥#£¡JÃjá+PØ¡Æ•Z5}¼,—¦¡¦Ó1Nèt*µL:,!ãX«BL´ş4¬_EC¯g4ôz5Ò0ë±” ¡ãí6‘sIaù¥hˆ=¢J¥‹BC«Ğ`ÄvEi8Ë™z¨5êécàe¿4eÂè±‘ƒFm Ñ`40á°VeAN‡BÃü×h8¾Š†‘Ó0šÔHÃfÂ’VQT…˜Ë©(&+S/£á¼4eÂFã¶	i‘†ÉÈà3—¢˜Ö	­fú<ñr}³™qÛlÖhLà0cI¯ƒBÌëVhp±2ü2îKÓP&<•†ó4|óWÓğ|‹…IÔbÑhÌà²`I¯ƒ‰·|ŠqÕa*¨Õi§ó/ß¥i(¶Z™D­V­Ön+–Š1(Jòÿ4ü_ICdUhx¬âçh$#vLÒĞ‘Fà«hˆœ†(jµVğâÖ‰8o&)4¸z_N#éÒ4œñ¸³?¾·iµ"øl6FÃ¤Ğ`íRPq®	:½nê¼ü*°?í·ët6Øí6¤ÀiXy{JÈÆûº'i¾H#ti
SìÓiØ™"³V…iáÅqõd.AoĞOƒR¾Š†ÃÁ´ÆáĞëíìÀ’Yq6ŞIUœûãbt8¨ñ‹4R/MCaŠÓÅ´ÆéÔërºØoD8;oO+4|Fø«h¸\Lk\.½Ş	!–,ŠsRhdF‡ÇM€¹ƒiZ„À‘KÓ0sÆcÔÌ¾¶á6\âÆ’UqŞ•¡8¼À_£‘qi
S<¦5Áà†°K¢BCaZnTqF\=™K0š§E!¼½4+gŠÏÏ$êó^H÷ù}LÉX«›·æ)Îˆ«3W“uZÂy—¦¡L8Ä¸”d2ùaFRR ™ÄÅìåíÅ…Š£àbµ¡­°·ÛS.^(¼40ûJ2gšÍI&3`­~öu˜]œÌû¦3`¦d±M‹tx¡øÒ4”	Kã¶$Y,AÈ—°äV.‰·×T(ÊŸÍ€© èœ…ğBÅ¥i¸¹‡H‹0ND"6[J"‘šWTIi'>!×@’ù˜Ü3~ÌB„àÃiÃô“?}9·èö7gÓ/2¶“9òÙÉŠO@ X„ií¥gz‰ë>_%<ëÿ¯Çù^¤ÏÖ<•ÿqj=•`)BçdY<M?Í„Vø3»å;¨š½ùÁ9—C+ÍÀ;
4ÏÆVÚÈ.Xûºçå×xZË•T>Çÿ¾°ŸPT¬ï¢±S~û€ZÒüƒ.ÖjçßÊ h"Ûy²%‘§˜ß˜ÈJ:y<.šD^&R’Èk°>‹}DÅÜäp_"OĞLoMä)æw$òÊ¸<‘W¡–¥&òj`¿ÑSò®}]°6Á:FÌ&Lûa¬‚eÈñ\(…¢i=¤i=jynõ`´a¾V /‡Q³±çôçæÁ ¶nÂşı°Ë£Ooê58êØŠ}Wás+±NBİÏ‡üHØÚı]ö{^JPÎeß—Ã<«Äö!Ä¬aã`ÑfßÑúÂëùxÃÓ^Æûà¨ù]K7­Ş”Ó4Ü¿fÕ²…ƒ‡V­_'åç–)’ÒPÛ¿fxıº¶şş­Ã³¥DÛ¼Á›Öôoäİ•~JCÍú[7®Z±rX*Ì/(jú×­_·jYÿ	Î•¤ÖUË×H›Ön”†WNX¿~İ°Ò¼lP*ÈÍWôä?â½‹ı/®/^'ˆ@èó!±ÊŒÊ+á· ˆ}xSù¶—ÕÇ„:B'Ø?ÑzşÉôÿÅ.<O¡*ÑÁ^¢….¢ÁT©Sr2k	œÄü{xËD{[ˆÅ÷Æ‰±g:é{Fè{š<ò4yyÛK]^<ùâ/
^8ùÂ/Nœ<ñÆ	á;OèBOâıí'\¡'¨6ô8B=¤	=ú1ô¦zˆ¨CUè’zàş×BßºßÚs½ûßGBûhaèŞ;ü¡{îØºû®'CwWèNâİA|¡½{C·ïµï!ë÷\·‡ØCb{J/«ßCiè¶[Ü¡[oÙº×(!G0İUºywjhd7²l·´;·Ğ±»o7e¿L¼°Ù´éŞ„s<°ëä®7v	»(	İ¸Ãºáº'C;ñ¾¼ÚA„t¹‡;p”Å¤ïğ†ÃT<,>uX8Œåí[‹BÛ®)	]»u tÍ	]“¹rëú­t+µ‡¶ûBßÜ´=´yh ´‰lãêû†6QqH:5$±qÉIòo?Öµqûú®«¶oè‚õùëéÊ%KºV,¹²kù’Ş®eK.ïZº¤§«»fa×¢š®®ù{ÛºæíméêÜÛÜÕ±·©«}ïÜ®¼¹ädÓ{Mr“Ğ°¤¦«~IuWİ’ª®õUdÁüã¹‰š'{[ÿ:¯%®ëX'#ñÈ|†±ÎÅqÍHº/é>HÈ]·İÕÉ-ñäùİñG’{Zâ˜‰±ÌÌ@òA7T÷D£0F‡†¦¾b2ŞÄKVª±<Dà”Ã„WD‡X1ñ:kÊ/k>+’¡!¤F††‡1åDp4àÃxáÿ Ï(!T
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
xœ]’Ûnƒ0†ïó¹ì.*åĞI©¥«ÄÅÛ@b:¤¢^ğö6m¥Eé³ı;¿1AY*İ;|ØQÖàx×kea¯VoáÒkF\õÒ­„o94†^\Ï“ƒ¡ÒİÈòœóàÓg'gg¾9¨±…'¼[¶×¾ù.kÏõÕ˜_@;.XQpïôÚ˜·f  l[)Ÿïİ¼õšGÅ×l€GÈ!¹‘£‚É4l£/ÀráOÁó³?­şåÃUÖvò§±Xúr!¢]±Pø‚´;"ùàB±@ÚQ.¡\,ˆND{¤4AJ¤,"Êˆb¢’è™ˆzfÔ3¥Ù	­¯“›ãÇ„G,Ô)Ú£Vœ‘Â‚%ÙŠi ò“†<P®N32²C§7tçò—}ß—$¯ÖúıàO‹YVÒk¸ÿ7f4‹jyş cæ¨Ö
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
xœ¥z|SUÒøÌ½7¹Išäæ´i›„Ğ-
½@
ˆôA¡iy¤´…ò(-´ *,ÅÇ‚YİE]‘T
u?WwDwu]¸¾]àŠº
½ùæŞ¤µ°î·ÿııo2ç3ç1sfæÌÌI t ­ÁàŒi×W{Š0—’§Wææ­ıÕn @¸¾¹®ô¤öjjçÔ¯j÷Ş6qÍhjï`XĞº°ùguO›¸ ü“ëÚZÁZ ½†Æ›.½~Á›/Ú~`0¸V75Ö5p·rS¨ÿ/Ô?ª‰šz) m#µ75·¯~Bm§jÚãD£iiK}İëO¿’Eãe~zšëV·rßpÏdØ¨í]V×Ü8äXš…Ú#‰Ÿ×Z[ÚÚ¥t80D/÷·®hl2öÜFí Õ„“w™¿c»ü~¡ìø\¥ıËúÀr'™£ ¢q;T˜{³u°€±hTÏkFÅp\ñŒ_9¼QzTf‰ä ~”Y<~ö;’ËU‰Ì	©dX•¨¼9p)x¹¢Q¨Gõ¤ÂZši‡k•ò²‡C3¯£±Ÿ+³>ÎÕ¥YÑï®äíÿçÑ(%&b:|ï o!Ãyø'<ûàU8=p4f ÎÓ˜à¼/üôª´Ó”êx>†çaëO“`ÑülÄ[àiÜ†5Ğ†6x“F?†nx€,x%÷ ÷úğüöáÕ8‚ÙÎ,C#¼Ç¬¿|-éÑ/i¥/q+•Ÿâ½2çªõl"D˜q°y˜©‚?Ïaf3ÓQx	ÇıZX¿ˆ/Ğk¯`/n…Ğx9t¥g¦E¿†§áüş
7Á&Ø^zïRWôÑ?G “ˆvÔÅ§ôôÍU?Ê¶2GMï}p'}¦Ñ§ğex½R3qwî—áz4`=×…™è‡³$Ÿfø%,…»à)xş‚3P;`cI4vbL’,|¤zHuèUÓ¥Ôè×ÌE8ğÒ«p\jŠÑgë!¡Wˆ~]=/}}e™¹DÕÃªªçşÖs×{C±¸ÿ‘ÖÁÍ¤‹'ÕÖ„ª«fTV”—M¿vÚ5S§L.,)8a¼X4nláÕc
®=*ÄğÜaCs23ÒÓûù<.›Ù$	:­†W«8–AÈñF0\aÓ¼æ`¿Ä_W:4Ç[âj*šSâ†#Ş:o„^\º¿´TAùë"Ş°7’N¯ºèpD¤‘®)ÆFŠı#Ñä-„B™„ß9Yì÷vcMy5Õ7ûCŞÈJ}šRçÒ•†>ÍP¸’¹õ–D‚«š:KÂÄ#v%è&ú'6ê†æ@—.ª	T‹dú[IaãP©0™%cºĞd²´Ó’º†HYyuI±ÛçÍ™1ú‹•.˜¨,QOŒğÊ’ŞE2ëp»·+çDç¦nÌgëüu³«#lÍídK:;7DÌÙ‘,q$ë†\´óÆH¿¸$’-¯:µ¢ŸÎÔIbD•fò{;¿Úÿ‹Ï/ÇÔÅ1ê4Ó7 W#ÌÄVTûäÇ$YwvıŞ`g¸³®;Ú1ßï5ù;»ôúÎÖ7”UÓİÑ#·»#ÁM¡ˆ)Ü„cBñ­+¦F¬åµÕ&-èmª#}‹ü¾«Ü>sÿ˜²×$IØç“Åp{·ó©é(¯µ½0ß} ÄÜìP„	Ë='úzìUrOG_Oÿô°Ÿt;µ²º3Â¥Mnğ—Äo¯‹tÌ'ëZ,+ÆoŠ¿uûü³· 7¤ŒõW“y#ªtÍ8ìFÒiRÆoc¯/ÜD İlñøiyI8ş]Õä¢¼$èÒì˜!Ì¨ˆÅTëâ+éK3êÂ¤°EÅŠ2#¹şÖˆÍ?¡_»2[%‹*«•)ñiÛÄEõø¬Hn‰r®¼%áâòZşòêÃˆ¾Û5Òë>€‘*–;&’•¥—tV7,ˆxÂî:w¼Õn_D‘†CşêÆlv$¡¬wİŠq„[™Q=µÒ?µ¼¦úª8#±y9.­äŠeüÕîØ2d€MšÆ[Í¸Ù4Â¤ŠB!•>MC`"+XÙp'z«)0ô&6"YŞ’Æâø8¹}Ù¢*Ùœ&–ö­¦–›´ÎÄR·/ä‹=CsêöÆ	Ó,ÔÒ¾.rSÔ¡!ûœXª dYºd£÷Vûı!“7"–UË{“Å£H9.Eæq]Í¸¬5@X$&ğQw_Cf$˜í(ÜÈ$¥İß,½¢{r_··SãŸZÙ)/î/Há/mrd¯2»_ h?ù^¯‰´r ;»DQ>ÌMcäEü“:ı•Õ…Êhò'kİ7È´,0§Î˜04‡\Û„.?n,ïqceMõaJü¼gT`™êL}Õ‡½4,#ce¤ÜğÊy¥
jh”ñîÃ"@‡ÒË)¥]ß à4}8„ún&†3Å¥+„DÊ­ê»¹XØ7š#œ&†ëPpÊÓ²ÈDJÔˆZQÏwÊ¨„9BÁT‹pPOØİE³*t7vtiEwlDcn¬ú‘tUMõA=Ğ4¥$Bä‡ÌÅÕDÊ¦°RâmeM¨©3’8H5ôÅúÇ‘šüãˆµ>¢ó7Nˆ$ø'Èø"_Ã«e<O&Š¤é¤û²ÊP[í£#éMzÑİiúBÖTˆœJ§éÃ¡rÈ§¡» RÖ)ç¥şÿğ¹fÀr8ƒ:¬Çw?‰îCÖÁŞÊ~ÆÙşÏÏäŸøtı›ÏÜªñªíªÕ…êê×ù +ßÃ÷jÆhš4/jµÚRíú¼­ênÓ=¯û>aJÂA½^_±ÌòèEywİ:O(ü†ñÄò×¾ÿÒ‹ºKi—zUwóŸĞXMÒÆPìzæ<É€‡TQ¯V£UQ2¹'sOš-XP`˜#†Ì>3ë3ûÖ±ÌzINÜÏ÷š˜ÉH9×}ìFf3­âut›P!	áQ(ÊVæù>;34îÂÿ‘şGĞx—˜@âçT€;kÁŸ S#Bf|2ÜÒiâ9ıœ[Aw’E=]!ˆ¼L¬PT4€G'0Äæpé´Mõî^YÏ+iæ,U$@İ,fˆÃS’õ6›Zjğx7ºE!Ù“¼%ywòñäÓÉj›œÌjµ¦ö–g]í!Ê”‹²Á%3®Üysç$\ŞOÑlQvgÿ Æl²øò,8rúÑnKÅ@Ş¨´ü€›…ß|ÿ5²?üCúhHuÅÌÙYÙ5íÒ±×™_Iû¤]dT30Œ³¤=ÒÃ‘“sçŒ<qjî_7~ÿ=í¼“Ä³Š²k#Œ=½šLPÏ2Œ`bÕ:^İâyZ€m!ºP›prvY:qõåûÌFôççM²µßƒ·f|Úqû[WÑzÏ°7V´¾vÃ’‹›ÎÅ‰bI,E––Ñ($kì‚=Õ#=Æ\ã<c‹Qea¢^(5-nKB{ÈÂSøq¯ÀB\^Ù$°¸´ÊWfdÇäL÷RóiãHL»MÍ‘÷ÙoÌ;ÜÕY‘;·¶fQúĞõÍ«•n»íÙŸ§2w<·ìí­Ëg–)­¨«3ıîÔïİ|zÉö[Š?–­NôS®‘8Î‚ÕbqºßlVƒ;9™WÛı~YÏC²y6İäö˜Í¦•¡"ótóónóqói³š5˜SÌŒ3›Y‡´íáYíÊŸĞù¼9JİR`.øq7±‚pÙlœĞàŒ4)¶–ù±Š²ÇQƒy©(oÒŠ\£ôÕ¹¤¯˜šøÊ¢Uwn˜?û†››kg¶j¤È¾ºí¶]wŞÿ$®>öÊ‹=‰GgÍšışœÊ©áòjÛÁgk~µäÆ=ÉœåQ:€“HO[É2ttp
Å³Ê¢fªĞJ·k3×Ò¨Œj³Õj$µY
r-€¬+4‚tÖ|ùè3ì8rÔh5>öOÒ…ŞuL%9*]Å3IÅÒ	¼=ÒßĞó*[yé7g˜¥£~f¹j±4^–±zâ$Bb“‡D—Õj·Ù4¼Qv+›Æ¦áÜnóÊÛÍÙí®¶]Í‘Õp—ËYyÑ;·ÿxõ}c&ë”‘¦œ+E²¼Ïê³ûØQd@\ıÚ/üS4­UKoXµxåéËìôŞˆsÁ}/~…ÏozıºãO9k*:V6­­e.‘Ô|G2\Kœ×’å8ÉÇÏ‡YRSÕ½ŞEF38Í`ìv7+»Éîµ³ZÖN…VP<ƒï§<C¼6ĞBñÚÔşA`6ñéTÉaWŒ^¥X‡İ&›W+½õô
—Î–¾K¿eEÇĞ¿+}ÔRWÓ¶jîœ¥ØóÆ÷Ø‚%8«x$íö7ÎL-ûôTó-µËwun&k(V¬!G´³§áyòô	zĞh5+CZ5+ÛÀ åË†+3§#í›,èË÷qÅÑ—¥7Ï!ô³Ïp¤=½ßF9Æ£?–=i3É*L²J„A0fŠÙ!Éšj° Kí'‘Ëuèt¾t_ú*Ê"Y“)yUÈÄ³Ù«®UÌ9õ3°ô¿úÎQ>™aş0¤WÜ9Ğ¹Á‘şAŠ°¬q¹ÉbKßûBúzwÇòÍß¿õşww¬Ø°K:zøéy¡C¾–æÆeo.^Œ?;úÚŸv°s‰,ÛóìÑÇïur'ğ½jÃRsã¢–ú³KÉVĞî*~´^­Nµè].:[ƒÓx^+¾¶ x„\,Aì¬İİ²“¿øÏ–`î?hr H9‰ÑŠ9ç$× —YB…ôUôÈ«9¨ÉØ¼âf&}_Ã¡wûä‚ôúªÙµÍÍ³kW1‡¥‡¥;v?v÷™3S«¾}ùÏ¤'wßpÏúeK7¬¤Ğ‹¯ÜX%ªgŠ6e9 ;Pq;kUB¨qŒqæ”ˆºÒÙXäeõñø{?Y×²®(“œŒŠÓpZ­Ş@v¦™â-l$ÌÅ~ÿ³´ç@>¬yÈÒÌ¾ûÙmÒ‹8úÒR-½¨*ùàÒÍ|À®•}I:éa3é!ÊÄl$»}vÒ…İÜ,ƒu¹Rç‡ å8íâX]]¨ƒGg)äÎ‘÷èW€ì«qùÇ"ç“}tŸÉÆ*òï;•²©·YzSºø™ô—!˜â¼kİ-ëZ—¼Şµ¸ ?z÷Ršô^Î±Å­£æl9ú‡¹¸áÄ›ÏK›Û<#4¡6iä´ğú²ı/uI94}ÊˆñCÓ†-ö½Ì‰ŞB’±‹ZVÂoCtPaŠ§ÔHÅ½öV8,çc‹i÷;¸k!F@X4æGŒ°…–%ƒäetGOˆ^“µ4ƒ#&°FŞÈ›ÁœP2›\Ã`XYÈ(Êƒe‡*g-¦“Ù—‰ƒH«dûU„}aŠò‡İ,[áh»‘•-ÕoD+od”³–‡îœyùlğÚÉ%éÍQxç^ÏîMMÌÌšº¸Q§.zè¹Ÿ×”Y]w“í7;÷îg¹ÑO.3âøçOH«kKÔ÷ªuj®©qy£eßä¢{ï[I;ŞD;^J™ÃUbŠËÊq¬ÇÀÒÒMÉe!«É¡TRëL”&ÚÉƒg<Z”SŒÊ'Ëå²_µ˜mŒÂ;¹«íÇh¡Ş¤ÁD†Éz¸åÈ:ÔtÿPN«6ä×…-l˜¿|c÷®´ê@mƒôWékI:U_ç[™ÄøW?êî>tì„l™ËˆÓ*Ò‚bºÀêl6-yÄ$µ¡,äÑ¡N§6Ídc¬Í`.ÉªP4!+@1Ï¡A–T“F³Iv*#Ã´~+]@ã?ÿà•>Ô‡«ßx»l©“„õ¯Ø0Õ¨Çì+ë¥{¤ÎÆCËóHuÄİø¸Çˆ)©:kµÚt¶´t+Üe!“ÁÄûÊB,ïPä#£-yòº~Ù5Éù¬ÌZ ƒ$ksâ.j²#¸.×’ƒ§N[òÀ†ÁDô~k}ÃÂEáqóó…ë3—„0YÔbfİÜ¸ù¢·a#3h_Ïou
=BÜ6·‹H–vH†*qh¢^ÏZ¬I		V–MIµX(…Ğ—‡„DO"cbçå!ŞB\¨ÿÆÙ<ì²pGÊö f»Oñ¬£Uj%;§-2+.I_®ÿòW_ ºwĞÍ+¦¬°¡vt"oàğ%şFf¡áÉvH¿“ŞÖÜıxÑçæûØ®Ûo\}‡läb¹ùª¿ï1ÉŠHY—ŞáÔo:¤«GV«0&ä¾sØ§ö¾dË§„6§]j
úìÌféùïoşq÷ŞíóçàoÙ5—na×ôT>±?¹ÛZŞXĞCR[#]ËÕpS)şƒéb&Ç²Y¿K§óZ¼¹Ã“{zYÈe7qœ BNYH/Ø/'gX .§ÕzŒ¯şÜj,ö« ÅbŸšü‚š¦˜¦#wc¢0w|cÃÌùìàó§N,z GEWG:êh­kX´tŞ‚féÚ·ùÆ_sç–«Û~N²5zêæúW[—ŞqéoïŸgßÙsä©ıO<zT–ë’kY°†‹N›Éd¦ÆìtYÀÌÛAÏê+B¬©ÿ†S4Àó±[‰6Æ¢,c³Ç=_·w¯ôIùìk¥ÉJÙùkZ_úSoÓü‹ëößÖ{Lõ’´¤¹Iö¼«ˆúD]:?©’®²*•QHĞUÖ&€†/iàXÒ/kïsıAÔóDiñ —ïK#ÇÎ&aİÅ‹x»ôsµL¿§§‡ééyîôi™âJi&Šf²¤‘¢Ûb0¾Àá´Z*k­`"{2	œ®"Ä¹ãW˜’*ç+—~šáågn›¾gèÆuËfK0kdº†õ‡ç'™_´¤™]¡GØGû½›¨'€(zÉyÑ­_	rªÀô:N«TÀ±²ÃÈËË#{v\ÒÄrHòŠÀÑ§E6,½^&‰7á0é¼ÿ>CZ¬zéÒxBªé]
*8—´™²+Øä¿ñ¥9íiéòGŞ…Ùát83¬ÈşòéWõ³³“œŒ,@Æî}‡VzçÓ£2Oò•/`·÷\Ü4Óå1ìöÊ¦E(¡µo"¿’!ŸGF@ªVĞh´TmjfV’¿<””du‚ÕÊ•SpÑmlwñÜ˜>J~Ú¿I%M–ïı¦å7Ì8íJ¬¡Ó·<_7~“–¸úCõ53¨éÚêYV&³¥jÕ‚d,s×=íGïë=ÂV²nø‚9á†Å5ŸéÍ•ñ=ÔûkyäSÀM§(“+:ÍÄ:¸´®Ä$3gç*Bv“Aˆ1|y.OàúŸr]8eæ¼‰È^5mnÙ¿ŠE=«ãèL`³dó-]z²¥³Zr¬{Ö´JáŞr²ÊÙä™—“ut)w4«(³wº´Æ²ÖÄÚÈøp™)ö'¶J0óâÀ\v¹t>ú­t£•şºàú5Í-ÍkZ™T
±oR(3P(Üûò‰ı‘ãÏtí—ÏÄ&i·”vï„4'z<:§D±Œt§`u›’”ì ’Ş40Ùt]É0. JL±„À)K&äFÄ]j-7ü¡%OŒ‡2éc¦Œœ'6.Pb7Æş³”y¤W$IúNz¢™4—û®acï;×=TÕótw7…3ÒÚó¤µ’š²D›Q­æy›İa´X˜ŠÅ” ¨•Ôå2ƒµ·$'WĞÚ°ëô‰;…Á:.ï±MØ2ëçÏHS˜c×œª¿işÆV³LñzÒ“l'™P-æñjŸÍd H²©¹¬!>ƒ“u¦–…ÂnÜ7£cİn§‰Õ‘Gá½<Cé²ãòtùßæË²ÜFÿ˜/3±™“—óYÉÎTò‡Rôı³_d|g_Ø±jé¬¦/™uîÍg>Kù^?wACÃ´Úuÿsİ$,¼ÿàæ{Ò¦‰…âÈ±öÜòõswîÛ~GÒ„ñÂÜÑ–¤Ñ×\G;z(ú5— šA–?Jt«É#¹\æÄ$Í¡E)d8dÖÍ?Zıùk@¾b˜SKlRBƒ¥¿~ª:‚ë¥u¾)×Ü|Ç*qİofQpÅ$é£Ş/«ÇúİGœÚ’»o•ÏÉµCÖOç²óph.Áb¡ógqì~úü¡’:+™¨ÍéKÏ—ƒhz¾UÖ¬”3¤zÕ’·÷<Îé}¨óî®Lñ¥îÎ¦­“>;sŠÙO”=dCeä‰NµšÑêX†Ñ%È?úiYÚ¸œTŠÙïşxyVâN¢ÏêpC«UKif®R}Ó‰Ş]y/¸NËÿ€äï{–¨8á1+o0pVVëpÒN­ò2‚Ó¡#ÏÉcŸó'ª¹şk»ÅÙÿR œŸMÏ0"ëgV‡}´•JçÈQÖ Ç]Ø’È m××‡>¨´Úîf“`´Í~_/sh§JNY÷N™‚_JyEã~ÉÔ‡#ˆÃÄaÜ)ÎÑñ	jä@¥D'µJÅ°	¬AÇ§ùxæWñ?ç™
ƒ<äÑÁãEÄÃø)2;¯ÇÛ¹kÉx8OñLTÍT-P±*!eúv6‡¶æ,˜3ğù×ù
b?õR„“¿n%Ô-–~ş)ı·Kk1÷«ótU^Kñn£´šÉe¤p~ï?{O)wZòjĞìP+Ú­•5-	:³Egq8×‘ĞŒò½Î-XJ£ÅÈh9£N«µ:,æ ªÊÄ€@ß¯arÒ;où@p*\F¾)=­˜ÂhbÉÁ•,¾&(œ^”!‰˜Õ“9V[ş$¦KbY4Ëğ‚ŠM¯^Äåö~Õü·4Lc¬7Ÿú%Äu&ßGÙP¾˜Äs¨eÔ¨Ö%¨Y¥„D@øŠØ¯¼íÇMBş‘WşEÉN™m'3¦÷[Şû"Óô{fï_ì}Rş{…úÑŞû T/¥ıpƒêîØÿ&xfr'å¿MÄªÿ×w‹	^£¹!‚•7Ì!˜DĞD°–àf‚f‚òøÿR?÷ÿ?KÿïÖ^ŒÏ[L°‰`AAC|_k¶¬Š·÷œ%(!Ø@0[_ãy¸¢ÃC§kqÒ©H~.‚R˜CäÂl öÖÿ_-#<Ñ¯Ÿ™øJ¼ àsñ:×YHÂ‡ãulxg¼®#Ş¯«ÁŠ­òêœ–ZÃïâu„Tx$^g@Äë,Œ„Åñ:GoB¼®¢»Mz¼®Väz,‚ùĞ+ Ú©ŞË`šR¶ÀPš×K¡f*#Úâı^È£ûÔpúƒüŸ\ÁÛ¿†·ñ4¿Æ-£º<ÚKë{ÿÃì¾¹ÿ÷¨bÂ,${n QÔ× Œ¬£Z=h%-®PF5ÖK©‡,eÃI«Ã©6‰FµPÿRšï…‰T_A³Z.£8Œ"ÍÄÿ¸ZÕ*â\”*³s¨6™æ×Ã°kÍo\Q×¾¨eÙ´–e-C'´,m˜Ù¸¢ÚŞ¼aÃ‡Ëÿq€Wá•GŒo«o\ÖĞ¸Â;Ô{E·Ü{ªxÑÂEí‹nhlğ6Ôµ×yë[Z¯_±haS»7³>Ë›7|Äpï¤––…K½[V´¶Ä&ÓM¼rX·‚–(­kÏñN^V?bÿHä‡“ ÿâ`|6Vâ4¨ÂŠø{&Î üÎƒUôöĞ{:ğZÂ_Coê‡=T^ `p,ŒÅBê)¤™cè}5µåw><ĞáñCq$˜†QO J1Öè 	bØ4o8a*‘ †Í%,½ÁKe˜€!ö‡)-ê?€PÕCŒ•_9¡ÃÓ1>‹å?ÒŒ£éqD‰ı	ñöxš&Ò[Œ·‹hùq¢»ÊÔ‹_=çƒQOÑ¹–sÌôÏç}Îä~Vôs³iÌ§«ş>öÓªOp¼³ˆ a¿Rz©,#°Ä~–èÀÈÇ¸î£-íşˆ=ı!ŠzÏ}€İ˜)ºŞ7yÂïã{ï&yşön¦çìØwªŞËV}Šã8DÙçZlÉfD8ZpˆèÁıïà[lÔ³ûÕı¯2/¾Pè^ğ¼Àüî¹$øœÕìFßg=İèµ'¨ó8†9µ˜Ò“éÉíÁcG“<ÂQÏÑuG·åNòL?´î#ô Šd£‚İûQ%&p/Dá `óh-÷ÁÇJ=ñNL†\¦S9 …`?Áq‚Óç¢1Y4§d#û
=eûÂûŞİw~'vcê“5x8zSD»^şæ1ê~,üØ»Œ{4oo±˜[vìÇq{M{½{ÙwezÊv‡w3ìty¼»Êv1;·î<¿“>Şˆƒ‰à`×`’û<ô“.Ö)å~ô‹ÉhÚÑ±cëvë}xï/2=á_`ËöÓÛÏng·nÇc8	K 6Ä’d6nºÕ!íĞDK˜h¯Ã•öq¥l¥r«‚}YiñQûÑ$:Xá¢{a
Ûr·m[·m÷¶sÛÔİhS6exî¾+Ã³•Şç6£°É³‰‘‹ÜM»7qÂQ4y30”é:Kpúœw)-I´^—ãYÕ–éYÙ–èi'h+³xa":ÈyĞ…9uÇ©¹…`7Kr°HL&;°‰Ãƒ9Ö`§…`Ùsºª®*>ÀV©É„æÏì©#Ì+Kô´A™›î)fnp°gz7ZÅDœLôÔÖäyj‚Ik¥J…l—ÇÒ1Óˆ>·×#°XI\U”—¥z®¦z®	ó¬›ŠSif73=¤x½Ø’`N	&{ÎMNfÊ&ãä`‚§¨tz)Stx&­!¸.x.rÉî*'Ú«yö*3
U¦<¡Š¡.û
P$ÌÖ	œ ä
Ó…a‹pVˆ
|áÎ	lƒÂªH€[»fTfgOíæ£S#Ú²ÚnŒ¤UÊ¥X^QoŒ@UMmuâ¡[7o†	)S#y•Õ‘pJhj¤*¢\é Š)¥ËBmímí+³c¶gg·g·Q™Ùí
ªMÁËˆÕûÚJÄšmmÔMÉÈö¶¶¶öö•+WÊxBÉÍ•ÔK5ªN^¼-[¡ÒÖ†Ô“­`i>ù"yih§6Èc¤ä¾Øº
gDÚ0¶H‡Êb}ßì>F] ÿÜ7Ã
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
xœ]‘Kk„0…÷ùw9]‰¯)¥à¢jû4¹Ú@!Æ…ÿ¾y8Sh@åË=çNhİ6­’è»Yx‡F©„ÁuÙGp’Š$)ÉíAáÍç^êÌİ¾Zœ[5.¤,è‡›®ÖìpºŠeÀBßŒ@#Õ§¯ºsÜmZÿàŒÊ#UG—ôÒë×~F Ávn…›K»ŸçOñ¹k„4pOÃ«î9š^MHJæVå³[A%şÍóèFşİ› Îœš±”UÒ:Pş(»*²@y)æ	Ù-ïşû„YÒÄÜ&zó[’ÿ\’°Yq3*Ó#7&ù£ûŠï½ğÍWI¸‡Ğ…oA*¼_•^´wùçl
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
xœí|	xU¶ğ]jé}ß’NÒİ4I€Ò$)–Ä°IXi"& AH@@FÂ&°ƒ0"* HA‚" 2(¸âl. ¨ã«n$•ÿÜêÎ†Î{ï{ÿ÷Ş÷ŞÿOUnİıŞsÏ9÷,·ªƒ0BÈˆªEåÙÙ£†ÎÍY^%õb†LI›?tÛx„°òE(.G:”ù9O0»Ò;Yx`äw#D›T>ù‡‹_0#ÄBH<<¹¸¢¹!
Ú›&O›;ikiòG™Kê|©tbq	wá”òÉPŸQ
ªW¿G(s äÛ—>P9çÄ¼L
ùR„4í§•M(Îù.o#Œğğ¶Šç”‹ˆ;…ĞÀ•ĞŞ;½ø‰÷¿°òûåe•rÊChˆÄêËgN,ıÛ•k _ıçA[=úóø-›XüzÿyÏ(ù]éˆrçñZÄC»-| Æ†cZŒ&‹Š'"§&„'‡î¸ºöÙIpq“FHØK&!|òâ€—|ƒàI ÀÚX‰9äRÊYjlTÔğçøsè·ĞÓŠ”g›‹ë	=„¶W•^WÃiyŒ<æNØşo.U8:Œ^FûĞNô:¤–Fª–£‡ÑSèT›æ'ÑYô,Z‰£­hêöO‡=ãÌWRQá?ŸïAehÚó.†ñ^B÷ãjLQªDQÌËÕr¯ÊCĞ|½ŠÕè!œD6›Ğ‡üŸ¹~1àz´ıGá¹•oĞzÒM'OÑ,´VXD†@ñ«0÷½h7.@÷Ã.™P H•¶+BËĞCšÕº†_T_‹´ßÄ+Ğ€d
š
ĞˆHõ!Â¨¿Šz`5Ï¡#JYMS_a/-'Ç‰ªá1´î¡p— ¼í@{äRyÚŠ³pZ+ßøw4Ï"C‘®ñ:ÿ»úoÑt4‡]úÕ?Çf¾sÈX×ø¹œiä÷j‘‹ SC;à¦97å"y$´1rş)şÿ*š‹
……\)²qo*÷¾¼ Öø!ğÅ‹€7$İS06˜Ÿ7jäˆá¹Ãî:dğ 9÷dgèß¯¯”Ù§w¯»{ö¸«{Fz×Ô”.“;$&Ä·÷·óy\6³ÉhĞk5j•(ğ%%{C¸(+Dã½æìb–¿8§s²7ËU: sr–?»(ä-ö† âü99J‘¿8ä-ò† *nU\’ å¤;ZJá–RsKlòöB½Ø~oèü ¿·éUüAoèš’ª¤¹%£‡ŒÏ=¨´Ş¬PöìÒê¬"€×j5ııı'j:'£Z’ZH…:øËkq‡>XIY=k	RéÙ´°Ò¬â’Pîğü¬nŸ/Ø9y`Èà T¡şÊ!¡HT†ôNa £omò©ê•u&4¾(IWâ/)¾/?D‹¡o5Íª®^2'…:ú„:ÎûÜ+ŸJöÈ
%±QhgpË”8ÄÇ›üŞê[–ã¿vµmIq¤Dˆ7İB,"ıCxD¾]îlÀuuu¶ß›]]T]\×X5Şï5ù«kuºêò,@7ÊÍ‡!ê_¬q‡²WC¦¢RÜ3YzöˆÁ!ëğ‚ü‰Ïö–C	üeú}w¹}ææ6¹ÿ¬Z 9€aŸ¡¡¦NBã!ªÎ{Ñx÷!$¥$C¤ˆÕœjª±ç±šª¦šæîE~ íà‘ùÕ!.~`‰?0^SªÜ5•Æo
¾wûüÕ³·GJPië¨–Lñ†ø@ôjİø†u©6)Ã÷áèš&H0[¼=ü0'ËŸUù›]ê‚¼€èœ¤0#ŒÊI !G(–U›š=Š‹€`S(Ä¥øËC6¿fê2°²¦ŒÌWºDº…lıC Õ#½B)YÊ¾òfUƒÀÆòÏ?†—j»yİÏ@°ÆşÀe	YÕù%“B"w	ì»IŞ|·/$ÂAşÄ c;ÀPÇKn…9‚
¯ŒÊ<Ò?xøØü»"€„+Øp\|ÖÃøóİáa€Cªx•7Ÿ¸iš À›	¿^ğ‰ñ*&@¸RÊ·_/o>v£¦Ö F¨£7kâ€H;–o3(ÏØ©NÓhËÂ8ısÜ¾ /|uN&PíL=T©9MU ¦ BüÙ?G)b¸t1¦÷æû'úƒşRoHÊÍgkcèQ°A†‚ó­FµÉµB 	ù º)ÃÊNr·Fnè%ßœÍ¹£z`Sµ·Zå<²šîˆ ò!ÄXXºËìVdÛĞ~½^lieCW×JÛÌ¥=Ù ş%Õş‘ù½”Ö O~ëÇæ² Áxğ¨~“A´õ«õãåÃk%¼|äØüc&°~–Ê?D0é_Ô/XÛêò	()¥„•²B–ñ²idTJ{÷1°äª”ZN)Pòê0RÊTMeM¨#á2Sx¢e"	l«	u\¸FjjÍA™*\V¥”)W-b(“4¼¤’Ô’è‰»³¢CPò"ØejŒ×a=v×B¯Jq®ªUKîp‹*h!…!\×2uŞØüçuº)O˜¨»€]\¥@lP+YŞÆ(óƒ¥ÕEA¶ÙH8„ı}€Lş> ˆ iüû…´ş~¬<“•g†ËV.‹b†îU@ûÜfPïƒ-é>ë®6]c”
‚P©6}Ñ™©|0ñ2#V'³Lü‘{š‰9¸†{3~ß"9d*©&»Á>ùíN§Óc\€›Å½ËßÅOâ¿†	³á~FøRt(w±xB£ÊSıNuAİ	îBõ&õÕßi²4‹5g´î±ÚÓÚ¯tÑº!p×è^Ñ}£ÒgèÇÁ]©_kĞ
Ç&c©q¯)Ú4Ê´Êô¦™7§šWšß°¨,––/­­Ë­g­õ¶1¶GmµkìSí‹í_üÇoş_q;[İ#÷ÿá÷‘ÿôıæ¿îİÿƒî›Š—¾ù´3´¡ĞØëñ„}â¦sƒ¿äÜÖÔÇ7<Æ-ş5;ÌJŸ ^’ë WE'é$RDUj¥œO9o¶à=Ìs kjÀì3SŸÙ·€’…2;¸Ş`!È6D˜¿HÎò”Q:IV*Š„ãTjŒ!â/à AfJ’Ù‚z¸RØˆæ€2"öÓ MØIíF×™×NãUôèÏÇÏ…Á°¥/€ÈFôIQ T`p
ÍRÒZÆR[¹ºÃ%Ù¾ªã%:”,hXH°5f ÄÕğYÈ<¨VšªŠ±s6µY§S[Œ-§±ZmOœÈ	N£(ÎÅó‚MĞøh´“º4.¯OÅéôºƒÁX¬A&³é`0Ên^ _£ß¡§Ãô…z2ÌŒ‡™Í7ÌÔ,yÚåèÍz3ï´RR™K0“ÆÍ7VdFlé‘XY€beg%(©´´pk£>»ú­,øÓ|Ö e! å>+İÕsòùÓGËš>êì§ı¿Æbpz>şMşôü÷¤,<µ?í+¿:M.Å¿caî=-œ’K§É¯âŞˆ&5~Ç½Å|P4ŠG]Q”°QHöJıæt	±±v.æîøBĞë>ZàM8Jíz!È©pˆE" ÊÌÌLJJB.öS^Y ÂJ~ ßÙ&øÛ%¤wËÀİüí»ÍHËà½øãut÷†úØ½~Õªõ+±'sĞĞ~ı†ÜÓŸ¨~QÄTÉ¡gÛ¿÷™½rèÁ¦Î«,/ûö%ãïIş¨ğ˜SRSB8^ÙE™†ùŠì°ô-¡A=j'5Z-G?EƒQƒ87,»™µÃLi²8ı	Äl²t„˜÷:qê™İ¯8µXäkò€«WñK <ÍøèÍ«r=FŸÕ4ºV£¡'"ÄF§¿6:ı³‰$:ë©S§ÎìÙsæÔ«»ˆMşJ¾çê×øe0uøå¯oÊC@BüHêéşM ï)Õ ×kˆ†MD£ÁZ¤£jN5K·TGT‚ZÇ‰´kÀúÑêùr±J\+R±®ñÔj](êü$¶N4×DTöPøÙÆ\¼“wŠZœØ=¾;HÜUå/=¸iÛƒ/Ë_uÆZİrn÷ä%ÎÁ¤åü8ğ‘ßà e%:Ìá¶#-²Ij¢ÓóÜ ÿ<ÊT	†5ûÍ¾tÌå³“ƒä|¼gŞCŠäQxÿz¼_µğHåGÉœtõJ&Š0ˆ*Çh[‡· 0O6	«ÚïÅjù,tÚÔ0Aÿ{ñ;ôaRı£$¢¬ï‹ÁŒ1JîÓ}v|/IÅïìÜÉúÜÖùP™Ó)i@/±ÉPJR/1 ñÍ+8Iş Ö9³ñ*Tx/FÒaºĞ(äaBGàsâ IÓÕ¿mã/ıìe¶ğ|è9Œr‚D%u‰ÒY,‚	(&ÖèÂF—ÇEô.Éå‰"vEÕjcEP-R{EF*ÙÎËâÂûÇEŸ¿$SÓŒL)¼åoÇ×—f¡Mé@š%d57ì§o¿ıî:jüéÚÑU»^·açrşò¤üœ¼OÀ£ğ8<V~R~·Ã´ÉÊ—åŸ°aûO?Áª7b¦‚$6 »¤X½NÀ¬ƒg4‰BEP©FĞa„+‚Lˆ0éb‚>ŒAg“è êœ?=­}wÆã£ñò•G6b±ÛÓ¸xm¸·rã¢	·‡¬ƒÙÖÂl½ S1¨—Ş#Ú¶Ø8½ŞlÖTÍ"FÑ­gS)l4í´@zÜ½NW¤‘˜ØÒv› °è³¯íúö¡+««f®Ò×Ù®Ÿşàúï6¿µÃGŞŸõÀÇ«S6ç·3Ìûşp*TñÅœİ[w¢* ß`€ªš-õMl¤K‹gûöŒ†IÉ‰³Å\4Z°“Z,Ôëó”>‘ª+‚lGÂ7aWŠŒœ”q3Â$ÃŞƒQU¡oË:"Û“mN .“¯í»;|iéİºà$œHû•õÙã07¸ş³?6"ç‹í±qùÖ‚mÅ“Æ^3béâ7èØ~8}áÊö›â™/;}ÜüóÃsOî¾­Gé=SœWf8pú¥gÅpæCÀÚ“îmÙR¢×D¥&óØ`Dœ«ªx£Î£KÑ•é8k3E¢ˆ™°ºlÖ–ù§Hi»ûèŞÃ3ÉC8.¯•uø;œ)¿‚3WÒyõËWÓşƒQ3Ş³P,Ê—:G¹¬V»Í¦õføxlQA›Íí6UİnÎnwUí<¢Rq
[mš0¢“Úp	ûc˜5`P]€Ú C­‚OPÜ ¦3 §ÜàÙ—·şşï=®®ÚótÍÀ‡3C)Ô×°4vÖsçnãã5ïUìÒşîuó·wéNş¼N3ö
ÓG›îàx¼Rš9.NĞiµN`•öñ6à‹BF6“h¨Í[İ œ£Ãf
ÖH}-;>ĞÌÊ¶—Ôš;„2¶€^« »Â	"[†‡µ0—óí…«2VİÄ™#÷§?ÿØ¾®‡*N}uô±Åƒ–~âá›ñ‰2âŞø><_şÔ³_şÇí‚Âko­İÙÿÁÁ¿;·¨°8¡3PA’%;X¢LN¤Ñ"Q%¶Â¨ŞBî@“:Af¿ÉbÑÏu–ßú¦ÁC×p/6ä7\Ç")Æ°ß)Z
˜ÊL¹QJCS¥.{gM¢>ÆŞN¯ï,ØenÈl2#õPbâ]M|§øNÁøxj6{˜D ©¿’á½`HkCó;v³Xº§w}Äğ‡#[ˆ61^k+{†ËşéoŸ5n¨|yÙ‹Wœ›V]¾hë'Ë<´¢z>æüÛV-ßºyı†µx^İß{qá;ç~®|üÎüàö‰3spöZ|«lÆÌéeóäª9kf.[UÍ8e¬?3Â)…Ò]¢ ÄZtN'² §½AÑè1î04Ş065©İdW$Sõ¤Y¤´UÙl~ &N·tg\O`ùoËjA¢p™ò÷ß=õ‡¤ıu[§+_şâö_ñÇgv.X´iSÕe÷’“òÓò²š­îv~?öÔxşÂ2÷ÄÙçjÖÌz¼ E«r=/ Q²
”ÕªVñÜÖŞØ¤`Ã6;LÏÒ°®½¢h[jŒèÜJ´l‹}ÀwK^­*ˆ*Œ8ğ™B™°@ ‚d±çÔHÀf ¹¶sz§­T²5ƒÄ±WÒËõOÓ±äîóx×y½¼î1 @%ÎçÆĞ«
¼£¥»9àM‚ã\·†ÛÁäøhÊIG8‚©8árÌåÂ£
‡ğ;˜7†ME¬§$…·m«éÁğ€Àæ¥—işÆ2Ú¸µY_ÉÓ´>÷ÌÈÉ2Q¸{±52¼Kƒ%Ş¹ºîéjœÎV7VwyËc¸Oß"ß>üVqç`ïŠ ÅGJ´„‚¶x‘`ƒ±j4ˆ˜hIaäÓX¬Â0;å€ÿ2Ó@‘×#%Ğ¢aÃ^£ØŠÙŞÇ@àóPNSİp~Å,ÿßjØ¦ËÚŒß>€–ñY?¿ÄI¼ ñwÌÚPUTzdGq(Wê uHVäÄ!Wk¶F­Vç-…A É]ä,¿²É[˜\‘;á½ÍùÁée^‰‡Á%IÂfe+C
”«’¯'wÀÛğÍµóŸ9*_ß¼ùâ§8yø¡P=Ö|
Ï?ü:Ÿ%›·;Êr_şM\$/œ9Gn7è5öële¿N”2Í&“ Š.¤Ó9]È`2£Ú£&zŞ`+šÍ	©‚$P$ä
;…pI¸):*j5-ª­†mÖŠºjWG<İÄç)è1ß…m\ÜóÙĞÄİ=v<*’’¿ .<rÁøÇ'?ûÙ+ßo¬X×W^‰§â‘¤V®í;c±Ìœÿ]®BfÔA²85 Úbåõ
~mğÛbm›PGÀšQ“‚Æ47Q>/&¯Æİñ@ÜÿÔG7æîºğ	ÉGä­€¶£òa¬úúö·XØb3‡µhŒ”Á«Õˆj4"¢à"¨
ƒ>…'Fxdò…üş ‘=”#s…AL‘º0ˆ,wÚ¾3pM~©rÀa÷EÂ.º¹¡ÙÖP6JÖ6yì9°í±Ó EoE‘R0Ï*"P–ÍbÄÃp!i“	›†ê(–ìs0æEEÊ[Íæ6˜|fËäÌšaÓ‚EcÇÉî†ûNÒ‡¸½²e{Ãe˜Ex…YıQÀá§ÛÄk5vøíÑnU]ãM)JoÎq9ƒ.Q©€Z­Š#ÀëÄÚ¤ı›fFm?ãğxP^ÀÈÖû°p	s³¸¡_üıgù*Va5[ñlî;{ŸÀyÖw‘?Ä—>†+ğ \ >ñ‘»şV/ÿ­á“N^œ»`}p„Jõb €¼¡VëôœJZ‰ªEZ mmv7Kğˆ˜‹¬}ß´»|÷ª?‹{Ég ·¿İ¶Ó3¬„¯Ò¿ÂL&”*¹Qñ‚Ì#ğŸ‘RM!ó)¬­Ì·'¶èìÄîq ¬£0ÌCÿúŞ‰gÏù_²Ì
¾+ŸÅ·ğîwÿvè”gvJ¡ãÀ7•uåH	*µZ|¥)å´œN½Zs5x¶øèQ¬j‘|=Â^rk
ò.¬¬°TeR^‘£<y’ôúTV‘,òğ^9‰Ïj($O4œ©ÿÍæóóÈ#@ò‚ĞÎLÀ8™ñòµ“d'Ÿu{Ì6è»ú2ë×°;¹T¢Õ¤×Vâ´Z£||Ig0çXU*‡‘š€g2;ìÜ;[€°¢í–‰‘úiB¢•­Âêpfb+hß½”Jİ+¶ÜËí¼vÌ|ìSZ²¬_É[yò üB—[òûõÛ`;Ó]‰ÿñóKMØí¤ÈñR‚È­ÕêxÁ¨]‰ñ<Œ§€Vèb¥Â“@µ ¶¡˜V—ÉÖÂ[Á¬ÃÎ€Â	éÌ Ğğ£iß'ÄdÙÏMİ?¢~#àeõÚE´ˆÍMĞ$Ø]“ŸÚÎ¤™Iá#‡S|¤æ¨µ0H­¿*ÍÂ'4„â#s“ä~üIşs?`ÕYùùõí=¹DéAy#„Çàá¸H~JŞGìWäo`w¹PD*¼eEİ¤h2	‚ˆD»7D1£2UTh-DZ­8â{("$»ù`å œ
üxü·“øÜuLOÉußË>Kk{fzƒÌg}pZn¸¶¾iîÇ"´PJGz½ëtÔ ¶ o«9§CG, Õ‡Y°Ñ’i)³œ´Ü°ğ:ğMÏ›yæ•6‚Ú°{Yü
ŒŠ‡	ÆqGE‹Ò—åõ×OâÏşşİKãµ?ÊïÈ7±kÍc$³á>ë•Ã‹nx–¿(wªbœ2¨U
ÔJFƒ¤ßÎ£C(ÆÁs»´ÓEÑ(oQ066Š£ ô%Ğ—DÂR`\+QØ£C‡ñÇù½TÌ+&‰](³hÓN¦%½v[qÆq\©üíOr÷AÇbBv<ÕwêÒO¬ÑéÛË.%w­ı­üEzÁÜ¬šy…ñÌº·ğ¤ø…³æÏÌÎ¿ËoîÔ/oú /mùÊ'~ĞkpW¯ÅŸÒkÄt¶!FD	’EyIÀfDÏ1ÜbK+‡¨ïë³“ßŸ³¸nÜŞÛc¸½ÛµpÃô“ÅKfµ`>¶XM ¤t-LhÃÄLF­¸%°W¸ŞŸ×÷áÉY[XtÿC¾õíŒéõÎíØ}²O,Á‹GÜiÅ›O“¢(˜€QkˆF«>OÀ, ÙœÍ“)VH0 XxØáÌèäìk²xKôÉ¸ÏY>«~ŞèW]D9ÚÃ{•ı I>* 5Çm	³€ñ/ª8•^‡ÔTà°Š³01œÉÚ=ZIø0iÙºš	W¿ò “ğĞóòPüÑy¹Z®9?’‡§n˜ßIz7¼J^!K"³ïQ¬›>’M¨À€&D£¨„rQ¢™ì¥¹0”sŠq&"Yz¤™›)Å¦3Çå˜óx6®<OrêHihxœL€AÂ\‹‹"]ŠæTDMA}h´b„şDX0–;ue¦C‡`¯3fÀ>nñí×hZƒ“®‹¯á¢·ÕÜş, -òú2ød¸x<B*5ænÙ'œ·‚à/gŞéDáˆ„·¿¼—ÉcÄY5?=QğV ‡m:¹$QL9œƒ¨¶'—<™î®ûM]bl 8º6ÁÁäE•š8  üOà`ú6 ë –15BaÍ GãíÆöÜ»K »¤¦<˜è%Xìn¬t'<÷ÇŠŠØùìz®–öäƒîtIZ4	˜+Ğ”Ù|@‹ãÓN;9!_øıe®öËØ6ìÔh9w/j‡RP‰Ô³³1*Ú¢JLôz£4µ«¥Ãğ Å¢‹1F•E]ŒºÕÅkiTTLŒ#7cÒùsaiÃA|«tåURËAHIvV×bFäP|Zw»b™ø•³¤tS|÷¦“9›°OãÁ·îE?›ípOI ô­]´}'~íêÔÊÙ¥šã]ğÜ×ÏvjøkÑÆ'fÏÏ
–‰å¦)ås§îß„ÇñÜİ‹+Få›qû—jå.¹Ã…û¶Œr$uÂˆ%L<kît²#;§á½ƒ½•ğÛ¢rƒf›I4vêÅQ¶,¶&Øm"gÈ‰~ò~&UÌ61Ğö| ƒë÷æËß%"yN8Ìqßâe/>´øÑåK6/›KÚÉŸË_Ö¥–ê2ör×ä`ßû^o8wéì‡Ÿ¼ûÆ»L-ïªD£R)NDA°ÚÍSnÅÈj²YË­UÖSVAM«ÆëË±Z].SnĞå šÜ G\ ®©(A˜ˆ¦ğ;â0û|Fk;R¦çÃÊ iİX#Z„Éw/\9eªš½}Ã†Ç§­6ŸĞ?xfî­FDâ€oÛÜh(˜ræÃOÎO}@Wôx{«¿ä¢ Çà¬R¬SˆEƒQ0úÛ[í¤òæµ*Î+¹	ÇaD7c9Ì-ÊÑ³ØÎ@"C³Óß‚­å’Şßu×Ü7NàåsŸìJÈaa?'4|úà#ëW.{tÙœç¦bv‘ŒÑã7ã'o[÷f+“ğ´OŞ|ÿË?yàTÎÔ Ó6Àõ0)l½ FY­¢ºc\êÒ˜LöÜ É¤¡¹Á‹ÂT4Eãkëcß¡r#XÄÍoÌvœî#¸ß+'oŞ|åÉ«òOW®|#Ç?²'91ø‡Ş
í<	NÀ¬Åğ/ºğ{Ã9Œ3ª;÷Ø¹)Úûœ}T´ÆœdZ‹çrƒŞˆíHaØ°<m&s³b(~;£µÇbĞ´ƒI'¼òiÎ3â¦”NíŠ¯Ğıõ£èşÕQç÷ëUëx]—ÒqšÕ€±5r>Ç†½“‚†KI¥ÌíœjµÇìIíê6ÚâsƒN›ÉìHÌz¹T}®â/-b¢4?ZS;a“ÏbN÷·àˆß-£{@ é 42²F}0™¼ç\LyÆ}?’®ÏÍyíè™s3éLUÜ³Âß¦Å+æ¦ç-Ì–ó«Fï>=y*¦Àn¬R·F—±¯şµË_Ğ·_ùøäÅÍs2L2Şµ×åäˆÕjÓhmZ»Ã¦±‹ÆÜ 'šRÜÆÖP¤‚µIDÔì?vDM§üßdJÅü‡ùsò¼»«ÏË‹RÈÑåKlmXÅ°ªœ7œ-©G½$V§ÃŒ<¸š‘A-R"UFÄQ 0µ7+Ë6ê$¼c"Neº/‘}yğw<¿¾~Z~ûúë«W¯¦q«ß;uŠíĞY ­ÀŒ&Xg†c¶ÙÒ	:»Ãb´ £!7h4R5L×¤·ÚøŠû˜éaË*2%péía»;oz¨ªZB¿şzÌKïE›W¶[ò ı}xnŒ®FV«E½¥X¬Q3'N¤å´:=s2Á¿4‚ÊvwfÓ»»ÖúáµÖîåzyı’Ã‡ñ‡ïËñ[øÛñr®¾˜èå”†ÍˆÇZ˜ó>öå=¬Ø=,7·Ç'$&$**˜}Ü•èLL§ıq”¼zF7•/â°ËŞc²éÌ~5gË{„ëµú¶¯³Ãª.¼¶º’­dŒZò#eIí‰‰©=8£J¥Swèèç¬@¯h‡ÑjÒ=je9°@ë7>mã|Í\cî–ê: ¼¤p†#¥4\M¬]ûJÃö

¤]é½ùc¬¤CYŞìI{ºöí7”<·å¡S» #_î´ uÒ¸¢’©c÷¿ìå{ö »ÜÏ3¸](Erš\äR»¢¢ `@«àş@ï„¼†@†-QØ[Ø‡	%tÊ×ö5±7ƒƒOî1ìüK§R€ó˜vs³7¼`)…ßíº¢Ô°·Ô&
²–©„_z£-ïiÛhÙ·¯}õCÃWß]yÅc[×®]»c5‰“o íÚƒrr-ÿ!ù§~ÿ½ÿÈt¿<†ëÇåÂÌ~¦ûãØÒÙ/¥ÚÇÛİ ûí°r•›ø`—“K÷û@õ;šQ¦R[°úÉs¾Ïã¹#ÂAb9mëo_;ıâ¼Å›yäÑ¥óH»†7êTÛe00öep	®)… ñåÏ^ùğ“^{ƒiO€2š¤hÏtÉkwRNk×úÛ[@s,­î¤ÀÊ™i
Œ­@£«•Ìô›»7ÉÒÖŸœóÂ-]‰Èp$}ûü7N–o|dî¼Åj¸AÁÂ¸ºŒÏogà£{~3Ga;Éh¸táç.~|î¯Œƒ¾²í¨£d3€7/ÚNƒÕJF­&­Q°+ßÉ´æ€ª™sŒ«I ÍÉÙËKxí°;êÙ*>­hIaé$ºÉúÍK2G^òÖ„êòò)éf6ã3À7íAó$ {¥N¢à±FGéÀ,·
\bÎA±`ND—G-v˜˜!Æ£é|¬åá/}ãæ³2/‰íÙ[®fß¸ Ëƒã×şïo½õ'ßëo7cÃø‰ò«‡\8z/z—vÎƒ·FŞ÷à“kFàô-ÖxF{VÕwPÙÈO/]`Ë´¹WÃÓáŞYl'oÒŸøQ€·ÉÍ«ÕÄf3:œfpŸCõ`vbJ±QùNç×”¸5=`å22†­étó‰}=çàœ›WüÈ“{ŸŞµ47–¿\İP9lH»]Vl$;İ8ôp=m‘}].u´Ûl·Ã¾·;ôvÈ_İ÷¸ÙƒVŒ0ÒdÀ›ñã^¸éHdã÷yrî¡§¸#¶Íí$õÂ{¿|\í9¢Ø¶YÀ7Ë ;Š8×”hˆN«&Æf÷Ú~‡{q°#şµgbğ9ßü@öÖ™»ù±í,L*¥×ÍšMNÃ,v˜¥NYçX©F£
¼ÖBµTtE©Ä(ÑM­åR‰F‹v–v©–hy€G™æ6X¬|pĞ
gË+qMdçƒ«ÅÑİÊ»õ! ?Ÿ[Ó#qÏ›Gó%Z—½²ÈëTéttbÿéš† ¤OÈ?öÙ™÷Èc¦L‹[8:ŠÔ÷Ô ÔZf°XsEZç	¥ E‡9o¤aép¶ù ‹èğa€òGwË'å—OãrÅp2îtV®À»ñqy I&¹ ?Õğ]Ã{Œ.ı@æ¬P~ÓØCr[ÔbĞ˜ÌZÆlwÔjŞ¤1">·Ù‰´EK0qp»°1À¨ƒÎîğ4`Ü~PZB—a5©¹Ó)¬*;âŒò]Á“òí2aöÂ®\JÃÃ—â¦SËí×®œ H6 ’åÄ@¤XE€%4Zr`sF,2«Ùÿé‰A éÀÀ¾ìmX@‡4Œ&o¯ 	5+êÿÊ<üË°Òx°üh´”fò;âTÚ8Oiûx`•x+hT¥¨Ö¨ŞVİPñfªR™ü&ó­ X}íÚxñ‘ÃÀæWkÍßğ`¶-@¤÷Ág|vEì…_˜3÷nl§1‹v¯_¸hİ®%XıAAnÕäIs>Çì}şf¿‚ŸWŠ‹V<]“ÿùéñF×†ÉòSSƒ ?±ÊcÈ1å„Â!©•o±ÀVlù‚mÕ O³CkÉ	¶Şß••ÒÕ.7õZÁÎôRo¯vÇ¸c`Éî÷÷A÷ÛînÁLİn+²Zn­w]üú¢a¹ÄÄCä+3{ƒ˜ñèv[·àæƒ‚áU“&UåŞ÷V/}‚!`÷"yLMp*.˜´ÑE¢6ã±SÆÖ<½BŞ9e.`aîTù‰e{~qÂ«D¬,àÛœp¤wØy¼şòïå\­íFì—a_š?lI`¿Ÿ6hö$„¬’»Í	¸Ì‡lñ8)Áß/Û’åõ-mùXKÛˆ‡»	p‡:¡)QtÄƒÖAnÁàNJFN—sx0FùVÍJÁ3F¦¹ ™»nPërLFm;POZgor%’”gøû¦¶öa¿8âüúÛøÄéÌŸØöÖ>1gen0ßÚ1–/àäÃ‹ëŸ›½lCÍÒÍÌåö×o<d#WIà!?¾øñÇ7şéÕ·>|ûô›€Eã*øÆÆG"ÃGÇµÂ²k•¶ãÂmq¸­ÚŠ:R5ãc7Ğ²h©Fí$³ŠRvˆ¹•XXÄŒ¢-Âì#Up+œ -yy·\úùp
W{ÃV]mcG”ÂŞ†Çâƒõñ?Ïã¿ÿ®¼å"+¸óìğği„ıÂÜéŒ¦²pŒ¿‡0B.”ı¡Ò¬í½nB~&„ù6BX¡
ÂäH¼ÂvK!¬bí#cW6…¶0 ]fDbN³|¤ş¡Hù5#éI,´aùa†@XA)o	†-W@l×5Ş†ôú¼ÏCX¡:3‹×@8‰gA¸
íµOhÕşùHÛo <áD¤O†Óû!ôƒ°ÂeÀµ•µû÷~ıŸ¹ØZş+Æıÿñb´ı”3Úÿ÷@ôÿæõ_µş97üwÏù¯ë_×¿®]ÿ.°#ÜÌj$+p;”ƒ
 ¶½	¥ û¢Ç¨9ò?‚è¹fÛr4^IcdÄ#i‚D</’¦(EÒ\«6<2à‘´ iö‹BÌ©!·ı.’ÆàQÌ‹¤	Ì;-’¦¨º+’æZµáQÜá´ )„† )h<šˆf¢b°;ÙÎ™†*Ï2°ãYyE¤Ô‹ÒP”
w”úBù¨ŸJ”V^ÔÂ¯æmoÔLF³ Êbhño· %“!°šyĞªêJ”–Åš -ÊÑ\èËZ•B©u€Ò
”©¨+/ºZ•Aı4èïEı!=z•µ™±XÃıÿİÑÒ 5"EÒ;R¡ÿÔeÈ”ñgWN)›>´lzÙè‰3+ éMë’šÚ%½oÅ„‰ÓK&Îôvö¶4ó²v#&N5­xæ¥¦LR9eŞÄoIqe±wBYùÜ™S&—Vz;LèèMKíšê½§¬lò´‰Şşe3ËËÂ»húßÙ,Í;†È)®Löœ>¡‹òŸà’ıhBwú=õMÀ#ÁÓŠòÇ)ñh<
ÙçAìx
à{¡|Ä¬¾7ê{AÜÚ÷„ønÈ³8w;TåA}»ànÈ(¡ÔPNCy¨
B¸´+ôK…R#<1„pi
”BŒ¼ğ,‚@ è.J 5îr£¼:ÜùPo%?=å}Í°A°úÀ ıa€~÷‹ä3!ßGšœ‡ğ­Üo²;x¾Îîä¹™îYs}Çõƒ×iÙ57ÈÉxçì¹Qx£ìEW¥«Ds%»Ñó·Ï<_~ŞÛóÅçqãç8öògÙãgXú,ÛáùôR¶çä¥·/]¼D¥KŒìKÙ.ÏqlC}°æµJºŞ4ïbïó>éıQêkÁ€ˆ;,ï <1,Ër!Ä^Æbl–FÒFÏÇø£<ïG¹U}úˆ3~„ß±<…¯–½ºàUzò4~%7ÁS~{O¤8u‚–Ÿ¨:AŒÇ=ÇIÊñÌãeÇ¿xœ?v Áã­K­Ë­+¯«ªãÙaBLµc¶é(öÍ=Zu4t”«::BŒÏg>ãyZ‡õRÒ¾OUhmˆ„B§Bï„hÊÁÌƒdçĞrêÀ;HÊşÌıdÇ³øÔ¾wö‘¾zlDià0æq@l¬Ä ¬fÄ&És·m+ßFÛ”àù]v‚'u³´™ ÏorÄd3XÔ›æì'6öòìì«ÆY¨ğØ=‘8gIJ<º=Æ7ÜH¥±]³¥7<tÆlã†”™l¸±7¾ˆu¨ë$/Y¿*Á³nd£çâZœº{Ö¦¬%ek¬%hiwU>~XãŠÉö®N]M†­*\U¶Š¦®ÄÆ••)+©´ÒdÍ6ÄZX…¥B §°öÓ›}Œ%¤\“-»fQ‚gÅ ^åËz{–-éåydP£gÇRlZâ]’º„¦.Æai‘Z—]ô)æš!»ò¢®<1@ó lÔB8Öx	‹‡<	ÙJBòXc²ï›ã¹/»«§ â±[Ó,y<¦y\NWq÷ò)>†£°ëPºGªƒÈÙ!»k¤xpD®Ûscxãp"O¿+[ß!ûí\|q’ëœãÉ­Ãni<ô€å@¸ÂÁl|1ûF6©ÊÆNlÏs¤ÙóÌØ˜gJ3æØiöWŒ»Äã1fŒœÑ˜bf,3®1^46ÅL(»a¤e„ŞéÀ<®ÃkkGLJ\'6Rç„ğòPüHö”†	ËC(olA~-Æ«ƒKW­Bıb‡ÒFæ‡ŠbƒƒC%X¢
¦ØZê¬¨¬¨œ•¾p$Y’’*+!V2Jû©uRÓ…Y'UTVVDJ ä*“f)Ï¤ŠŠ¦¬-$LÃWT"Ö©2©W A/6)ôÆ•HéV¦)a¤û+’ĞıJö~è#T„ai†íşŠ0¤M3*—¡ÿ‹õ°¥
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
xœ]’Ïnƒ0Æï<EÛ¡"I)m%„ÔÁ8ìÆö 41ÒQ Ş~‰ÍZi‘ ı¾ø³œ¸¨ËÚô3‹ßİ¨˜Y×í`¯N;Ã¥7‘L÷j^	ßjhm{s³L3µéÆ(Ë‹?üî4»…=œôx†Ç(~s\o.ìá«h<7Wk` 33å9ÓĞùL/­}m`1Ú6µöûı¼l¼çñ¹X`YP7jÔ0ÙVkÍ¢Œû•³¬ò+Àèû)¹ÎúnF|4çr—*ßUD%R¹E"D)QÂ‘öÏXsÍ~ø«uoMœ§T“c^~B%‰TZTD?ÛE™H†DXP¥N(nw$âqøN’øD!œÄŠ‰DJW±Z@-‡ÿæ|º:çç‚—FÑ¸İ;Úà
Ï/®—§4
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