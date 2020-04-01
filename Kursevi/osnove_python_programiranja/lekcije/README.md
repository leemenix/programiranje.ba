
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
            Tipovi podataka       |    python sintksa    |             objasnjenje
__________________________________|______________________|__________________________________
             Tekstualni           |                      |
(string - predstavlja niz znakova)|       string()       | operacije nad znakovnim tipovima
                                  |                      |             podataka
__________________________________|______________________|__________________________________
         Brojevi cijeli, realni   |                      |  
           (integer, float)       |         int()        |int()   - pretvara u cijeli broj 
                                  |                      |          (npr. 1,10,33)
                                  |        float()       |float() - pretvara u realni broj
                                  |                      |          (npr. 1.0, 3.14, 33.333)
__________________________________|______________________|__________________________________
        Logicki tacno, netacno    |                      |
         (boolean True/False)     |         bool()       |bool()  - operacije nad logickim 
                                  |                      |          tipovima podataka 
                                  |                      |          (True i False)
__________________________________|______________________|__________________________________
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

While petlja predstavlja strukturu u Python-u koja nam omogucava da prolazimo kroz isti blok koda vise puta, onoliko puta koliko smo to zadali inicijalnim uslovom, odnosno sve dok uslov ima vrijednost Tacno (True) ili dok nasilno ne prekinemo uslov naredbom prekida (**break**).

Dakle svakom iteracijom kroz blok koda, while petlja ce da izvrsi sve sto se nalazi u tijelu petlje. Naravno, uz
while petlju mozemo kombinovati i uslove cime dobijamo na brzini koda i vecoj efikasnosti.

Ono sto je bitno napomenti kod while petlje, ona se koristi uglavnom kada unaprijed nemamo definisan broj 
iteracija. 

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

Kao sto smo vidjeli sa uslovom **if**, takodje mozemo koristiti granu else prilikom konstrukcije while petlje, 
ali trebamo imati na umu da se else izvrsava samo jednom, ako i samo ako je glavni uslov while petlje netacan
(False). Naravno ukoliko unutar while petlje imamo naredbu **break** koja je izvrsena, else naredba ce biti 
preskocena.

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

For petlju mozemo nazvati specijalni tip petlje u Python-u, a za razliku od while petlje, for petlju koristimo 
kada zelimo da vrsimo iteraciju kroz tijelo petlje ako unaprijed znamo koliko puta je to potrebno.

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
# ukoliko zelimo da zajedno sa vrijednostima iz liste, stringa ili rijecnika ispisujemo i njihove indekse
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

Prije nego napisemo kod potrebno je kratko objasnjenje algoritma. Algoritam sortiranje mjehuricima, ima za cilj
da nad zadatim nizom nasumicnih/slucajnih brojeva izvrsi sortiranje od najmanjeg ka najvecem. Ovakvi 
tipovi zadataka predstavljaju osnovne koncepte teorije algoritma, a mozemo ih naci na kao zadaci na intervjuima 
u velikim firmama poput Google-a, Amazon-a, Facebook-a, Microsoft-a ...

Predpostavimo da imamo niz brojeva:

```text
[4,2,1,5,3]
```
Primjenom algoritma sortiranja mjehuricima, svakom novom iteracijom, svaki element niza ce se uporedjivati
sledecim, u slucaju da je prvi element veci od sledeceg, zaminijece mijesta, u suprotnom prvi element ostaje na svom mjestu. Ovaj proces se nastavlja sve dok se svi elementi konacno ne sortiraju od najmanjeg ka najvecem. Dakle, procedura sortiranje ce se obaviti sledecim redosledom:

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

## Rad sa datotekama (fajlovima)

### citanje iz eksternog fajla
- dosta puta imamo potrebu za citanjem sadrzaja iz drugih fajlova
- parsiranje teksta ...
- apsolutni, relativna lokacija

**`Sadrzaj fajla: fajl-455_karakteri_porijeklo.txt`**
```text
Goku - Vegeta
Krilin - Zemlja
Piccolo - Namek
Frieza - Universe 7
```

**`Izvorni kod: kod-456_rad-sa-fajlovima.py`**
```python
# r - read; w - write; a - append to end of file; r+ - read and write
# otvoren fajl
karakteri_fajl = open("fajl-455_karakteri_porijeklo.txt", "r")

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

**`Izvorni kod: kod-457_rad-sa-fajlovima.py`**

```python
# dodavanje na vec postojeci fajl
karakteri_fajl = open("fajl-455_karakteri_porijeklo.txt", "a")

karakteri_fajl.write("Bulma - Zemlja")
karakteri_fajl.write("\n Chi-Chi - Zemlja")

karakteri_fajl.close()

# upisivanje u novi fajl
karakteri_fajl = open("fajl-458_karakteri_porijeklo.txt", "w")

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
%PDF-1.4
%����
1 0 obj
<</Creator (Chromium)
/Producer (Skia/PDF m80)
/CreationDate (D:20200401053714+00'00')
/ModDate (D:20200401053714+00'00')>>
endobj
3 0 obj
<</ca 1
/BM /Normal>>
endobj
8 0 obj
<</Filter /FlateDecode
/Length 5926>> stream
x��]ٮ丑}�_���,�$`p-�g�<^`�����	fj���bPq����ˀ���H�����&�����翻�Ѫ.����/?���-?�6�7��t��_���_���v�)O?�/,�E/�[��?�����~�s���ݿ��)�u����-}���/��/?�~󓽥ۏ�ч�#T7��v7mn?~~�m���ۏ�yz��nԠ���½!L��7D���fjp�W��`��c�D�N���+��D�:��b=��+kr(�n �@#���"Q|�}���?��zt���}3}���'������M)������Li�c�r��o�\k��A����V�2�&V�)�s鹧��vQ����F����g���:�Й��afM�����v��Wv~�R�v��������u)�އ�`�A���}�]��j|���|�,��,����N�&$z%��W����Ĥx��y�DE���>�O#ah�h��I{���<bg��w�MgP/��T��>�3-�<�ߏOT$h�1k�n�c�*�y�7RK���wR�`XK������c�����e!���)��o}+ްalY���}R����ˬh`6Ut�G���s/��/�����7�1l�Q
�D�kI�FI1,niH������#���[�u֨�Z�&�R�.�h���z��鬥���� !3?�*q�J&9�֋g:g	e虫�OÃ��ZsH�v�7fC�ʹ.�]�i��N�B�42Z"����i$��!W3�A�w��}<�A��N�.�T1��/CG�)�?0#-�\�b����>����F�/���>�}#�E+>�Vb���V|	o���i|�9u�����n�a�!�*94�b9T����ԵK�'��ѣ�B;r�"r�e[~5�����bI���G$'���'!�d��u�׻j/�Z�3[��a��w�`C��m��}�#띘*�	�Q����C/M#�e؞�7�*��#�I������^���|��-7��$�<�r[�!o���@bo�/��Ԫ:�&�_z���۴���f��J���_/�tɍ��{����{[����p���{[��o���t������'�m)�~l�Խ;�cC4�CBѴ���}c�Q��2N4�r\tf����\t!��DI�'�4URđ0��
ʹN9���h�oӦ�yL��պ����1�}��6����$m��ܖg���0�b���dpn˓,&���_����5�s'�@�ܖ��
��<�aE�ύ����ER����w_�aa���/NL��ab�b,�c��s1���g2L_Pk�%Y�=T��j�:�a��1�XV���;���tR-��pGB�u(����� ���C�(����� �:�W�|�CX���+AA]\�0�d��1>�@f;�+���}�2�Ƴ�$���+Ag�@�\�j#�@���+�6���sW��+ԖUC�r�U�%`��`���q]j�c	X�5X��%���X�]���X�ò��m,�f�2�,�Lg�2�dF,3�f�RRyF,�z�r���x@���5d�my�z�Yt��Z���!�y�:.&�����%��AKn���� l�-�1���ʅ���/@ˣy^��łQ��R��`�~Z�+�y�C����RP��Jj[��J�
>�-� �"�@!:�Gk|��v�x�P=��$̂��� 6H��;�v)�'l^�^Ԡb��P�:�U� �|�;}|]a�֘ƨ�c&w�1!����v�(u����D�'�����vr#�����`ꌧY�ͷ�!3�F���>|���k����a�:K���z<N�fO�<���G�N���;݊��/M�a�]e2[�ˑ������N�v���PDBs�q��J�N}n���yc��<J�7W{"���kGN9Z�q�o�7i �he͎(\�=�B5E&M��cb��C�}���F�O�(���&YH"3�B���v���3I�����A�؎dx�8׷D���v��"F�v�s(i#�6B�un��"ءn�EWȨ��1�'��5��Q�3�؈����� *� �1����;��5��֑y�Dpg <��"ۧz��V�ɋYؾ/<�F�L�l��Q�����}�#{�����D9��)��3�`��Zg8F��7���!xd���2���+;����AUK69�?<��@�g��	lk���ƺ����l�(�BgADgG/q�P�&���U��ͳ�͜/��pGKM�:��6��'i�{`'�UD�k9���ڬ�"[��x>� u�+���4�T^'�m�Z�1QJ���]�EuO'ڊ	�O�y|G��Q���!�sGɽ�sh\�k$5jbJ���fvp���X0���iƇFh�N�p�p�1�	S@5��*$g�0���n7�u����V$2a���d�`�~.NU@�2,��f�m͆�p�||��{�zeO��5[�b�Z���`�0�w���ÖɻR�U��4;$�}��Aa����o4p�+���|)v�Gc�˥��������l0ٰ�p�'�g��f~���r�V�4��,b�����r�%P��c`1�fG����g�r3A߼��or܏�mU�ړ�>9G�Up|{׻)�3 �A�TE��~�
�OC�����y
��U|�԰��6�	S��$�}�<���J��0�@ї���i1R��w�����d��ӍN�'�W�h�]��X�W�8%I��R�ٱ����
\��k2�.�{h�� ��$�y��[���Qd��H*h�ip\�mw�"|����;�>,�|]�Հ�!j�;�O�P���/:�M�Dhݧ����vz�[F.>��E����O�I�w��%oEJ�����.����f_/�K}��#m{oh_�5Av�b���b����+f�ARj�
�S?�\� *������MYU+�bT�i�]���JH�
c�Sn���w1[�"���kҞ�Cu}��,�Ïܒ����YʏQ������-�6l[U=����"��EU��&��Y8<Qֺ
�wI.��=EUu0�e��I��X�$'+���ʗ�NE%0�Gm����!��/ �CдƟ ��b��Oʀ�D����~����c�Gn	��Xٌ�ɗ�̓�
M
zk�a��M���� ��l�Ƨ�`Bt�I�	%�WgD�>�cˋ�r��o>y[�����o����O��̄�ԉ� B>��a��K(gf�Q�O�}�w�/���+���ȭϙ?�Ϲt���.���쪿���y��i��=|P�P���l��/!�│�\�k+z��v{��U���$eh�4�5���, 6�R�RUy������V�v�:� @I�J��>����3��O�_yG��%�o�SP�]�xҰ�g��qJ������k��
h� 
�G)7���ka�zs%�� j)(W-�����u���1a�R�����H��am���A��&����լ��^�<� ��Ț�,�n��C窄�-���r)�y�"9�p��Q�&�u��D�+��$J,U����"��UAꚊ��7A�����_Ķ܊�0��q_�ߕ%���G3����+�8⚯*�>������3��s��?f8�km�'�s猪+%�
�I�j1��Pk�)�A)�m>-DE�F��OȂ������ IwA�)?����V���5����%s`f����͂��|���.h(�$'E�b���\�L���z��kr@�;�]@H��@UE��8dJ΂��� p���^�*�̎C��Ǿ1�H�1�������K�������G��%�H��'X��!�*X��` w�����|e���̜}h8���A~I��@�Z�ԉ�E������
�n��7�n������	xPl�<\�h��r����N�S�`��˳��7�x��!7�}j����u��A����J�0#l�:��h�JE��+��ν�F��t��SYJ�c�l)|&�b,t�#M�"";��-"���p���W�ႺE��s��0ڸ����u��1�� Zz���\.�Q�Ϻk�����j["�Cr���s8��\�P���m�S��H��	�ٟj�AU��l�%���Y��-!.Ad��ׇh���0��H�W����k~=��>��vt�I�JU�_����a;��C��>�ip�װ�{bkUN��肚Eu�_����P'	VF�2]p�E�����(��yz�E��,*gm��94��W�&��Y���bpul�G��e\Z?|�+{�*cb�6.�}M���ꇨV�4,/����8_���9��|�	����O�D��{A��k�|�ǐcA�m���"�tM\�`�<߼'��!�Cا&=���ء�4�m��c�.�|�>{3L�\W���3��5cB����EG&����j�R#���UaUlئ%v8;�	�#�@�_ևm*�Ǫ�%�/�G�jr��v˶$�]�*$㞯H�4ӷTZW�O�0���9�B�oXK̋�K8��4��{xؾ۩̔"u%.m���9�.DC�&<��(
����y�"p��^�2�B��/P�jTY�a����������FX��sc����z�_i�_A�W(Rwm���&U�U)`mV�xv�R]��oq���?L5��)���'�Jfa�⒣�Ӯ�EB�^�d�S\7���`P
��ï�(��d��%:����aM:��*��6��X��v�ml����� � �5ͷ�����+ݥb�/(-��%X�C��W���RG4{������\p��F�+#�_Zn=����ד[�������\*vlwC��b��u��V��ʅ��h��[_Gg��A�4��՛�������.|�'�PzI%����R.��$���Օ��sc�%��2M�ۯn�G_�f[�ͫ���Db��r��F�ц�jaI����N�i}���w�HyI�?��J֔�C���j�+�(�),���ch�^��B�b�!��
�J��C=xlh$Y6bV1�!?���&����_9��~jvl��OVl�|Ĉ8�O<��.�GW�����fv����b-�ID�%%3e���,�".���~��r�����0{����~eZCZթ�{Տ��
�^7�د�D�W(��*u��rUZ`��U�S��[�C4�p�s�く��m��s�&a�M�&�#}jV*;��gX�w8���9P�@S�;g)�H���6tAw̌�.��fn ���Qj���_A���ŧg�g��6!SH����6�Fy�O@��O?�I]Z�~�	�T��D��W�q�����C���^Y�QM��;6�4l(Ez���i�mX��	�Ff�n�a��� >wHu��卦�-�1�`zU9㧘�M6�����8��)H��0A��84+9�Z���=�s�`�8�3>�z�mG(6|0��T�h���<�ᓾ���~adG;ƙ��i(ƝPڌ��ư|C\|@-��T�3�2sC��,��K��fQHx��3�wB�*�qw�i�b��f�^ԉ] Xě����i�)�_���Ɣ�����2R*���<IHC��E�C,�-�����çl.F5j����T�l@�k*T^TG�տ����<'6O
ںR��x;��I=�5ƀyU�n�K���Z�q����K�7�|�� hh:=�p�}]I�*������zi4m�c�zc�!�Iʞ4ϦbJ�s)�Io�Umi�G�Y��ù���ҩ��@{2�=����`j�Ȩ<X=�$.��+3IeО-h�u���/�Ը��.M'�8�9�,pd+∁�i����%#��P������H+����kl���1�F��qzϪ�G2��؂)]ؘWw�r0�'��}�[��η��d	ns\���G����V(-
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
/Length 5307>> stream
x��]ˎ�:r��W�����0t��;�1��� �ƌ�p�Rʢ'�bee�o��;3%��`�Ļl~�s�����ə.����?����_������}���?���?]�[>w�	��x}��򠹌�����?���/���^���/��^���uy��z������/���.���/����]Lf��^~���?����r��__�|����`H������A�}`��~�1/����H�}�/��s�B�n0)37a=Ȱd���R����a���4�!�K�O������ǽ]�n=��`la�b츞������bL����]L�]?��e���`|�M��k���Ɓ��*���]/?w阋�{�c����n���bz7/�^����MC�e�^W�es��ו�k�/�e�oW��r�9�,�i���,k�}n���$���;cE*�X��ߧ/�!���E�����*^��uN�0���iy��U���p_�U��
N�&���>���d����e�o��(�]��� �r�Z5���>�ʏ;����p�x���D��1�K2v��p�܊���z9x�Ŗ�6}�$!ǽ��OI"�.c1+W���I�NC�>��ʝ�c|�'¥/�[�Ƃ��b}����B��ߩ����#��*E\.�J�fD����@8dED��,��up��D%J�,�}�Ȼp��t�b��<fQ=3�ׁ�@V����v�%%�P�
�)��j"���!e��|N��0MW'xt����>��D8'���<�kf%"�q������uי$B$a�PT�j�~��Cܺ^G;v��p�SY�����SN!�*��<-�J�8o!��|�'.ߋH��/�f��JtWD�~��Lf���4�
�E4�5x�2�|�u��,S�(�|Fgi�!�z+b':B޹f�0�w�W�<H�h��"�_6\�J7�y�"Y��	���LhC@C��4�ǒ��y����`�z3�2�
I;��B3 _�:By-��Qr�mC�(�9��mi�AW"�������kXa�Ò��vhПrZ�V%�K;U����[�x�%���8�F~�)�;�QQ���3��W�?�Kf=�NUg��ȔҐ�Ǘ�^�&�#v��|o�<|bU�����vA�+�Hc�����r�$Ŝ�uhӋ�.8l �X��&ፂ�2��+Sv|bP���16��w��;JSM,���z�ϸ��⤺IiO�B��Na�Œ
�����%to ��h�N�Ƣw���]���D�
�M�m&;��}���y���<=�-n��+fa�x�#��Jc�)��H��%�w��ΡL7�����C@�*m�`/e:੝��������o���@e��yihm�xy�g�\�����U�j\"�}g��Uʣ3�L̿�+��Ś5Q^bToo�G����rOGT��,��c��S'��^��7�	��l�ʙv/;�əx"��+׵ە��#k�ۭ
"b��Un}�Oa�U2DN~'�yNvϮ_5�:#h-��}��F�vX�<�c�c��`������3���H�	X��xݓ�0w�L՗N�_gڎnC��Yw��v�'�$�
g�0���
�w|���Z��*,U*�YȚ1f��]��)\��X>�u�ex�ʌ� �`0�}�U����y*|y�.^��� ]�T~h{}����~%l�1 R΅k>�O�n-�j��б�*»�M)3E�������_?+L�y|�~�aZ��m��^_�1q���;�B�,��� ��)��n���l>`�������w?a� <�:����N|���+X�('#�*�,��R%�,���N��
tc(P(Sb��b�(=���� ���} xP� ����I��@*����P/w+"��3�a�d`��ʍY��hg¢�ya4�9����)y<��T1Y�Ӱ!['S8ڥs�<㗮�/�Q�	�7Ma�*���ڀi*��1M����@�~̬8VR�OP�sJNa��A-` /�L�_��Z�����f5"+�O�c���B���hK~�i�!���� �n���U�̠Ji�We���+�{GسuU �#d�����RPt11�fś�>����/4�z���6ϑNHX���"�W�-����9��[�`� |̉OW���l6r��f���D��h���j4he��"�H�����NMW�J(�e��a�� ��k�����e��l���N%V�w�_���˓ꂭӳ��+���|�^�"��s�/<6���+3�����=�)uA��w'�ȥC!!
�0���ٕᓐmL4�K��y*
ۂީ���E�xV@9E<��CP�>٨ei�
N�v�f�!gCC���x�_a���@������@�*u��{U� ]v�a����u1:�����R 	��d-Ԥ�����Q9�R��y������@���U�lX6�z>�4�,�S��x��7,)� ���'�vY}>$L<�ahUTe0�d���a1�����2�4ke�1�z��4:�j���4�1]�n;f��B^�*�����:�_�z]����b�E�רf�X ���g�ӊ(�v��G!�ws�E�=��e_#��2��>�:�dnr��l�4�S��=�|�~����X!��<��K����u3oF)r�jZÊ`�����yozӾV4`�%$\��A*�}�Pzˇ�`וf!	���N�#ѹ�~��wZ�R��*�w7\b��t�;�f��YAs%�|��fA�����%�U��~mc�#D>�I�Z��e��/t!���|Ny�-����U�N�j�v�Ϟ��+|�S�c��\�;��i2sf �����LvTh�GEە���(�I���4��a�����,)
��Oқe�(3.U}���������m���Y7�e��#���C q�9c�N���;��c�d� eEz��y��*
\�>�˩�V��VL�ׇ���>| �ǩ���)�gO��yD����FU�̉��ӽ��2���5�i��9L����J�=�+�3�}�\@b𵘯�<�k�|�b�P�K��v�R*�[}�^� �IJYb��?̇Y��FK���ņ�����;�2n�g�9}Xm����vX��e�0��:�4 �h���"�h�5�3��O/O��6�`��Z�Ζd�y*�I�^�Ş5��S.�%G�n`�(���V����#��=�kZ�M���|�]��oQvyD�
U�%M>��W�AДs7�~�-ނI��5��@�~�|Ѯ�J�U�Y��ilׅQ?(/9vy�?d�����Rő���!��M2Z�k:��!�����=�э_Nj��\�r��#���V�Lt̹�2�����z�*r�K��S����8n;kG�=(�c~�]3���~Է � r�&@�/������N�s
�8t�>�̷nҴ�^q��i{�l%�7��'?M�6���gEW!in����u*��d��Z�2�JT��F�,����5S����Jad�ƴ"�G��� ��'P*u	�3�b<Z�ZU��f%M1i��#:��jT��<#��c�%�7��W.��6�)6̹��*�[�}�]���[����k���)'���0�;T��>[���tuj�����z��48��^ق袀��|�=<�����#�L�-��n�|鼈��6�{�p}K�i9̓n:ǜv��ІQ�|��#�Z7l��*E�i�(ލ�>����+2���C����]�	�R~�y��t����t},y���N�1�)Sf��2l�]�\�)�+�a����-m�l�XÎ�����0 �%�?ţ[��6+����菇�˘��YKg�'���'�D?h"TWFI'��Ud�?(��A��qt(���]�]0m*�j��p;2W|ox���RV��V$�lY�����Oյ��Ҫ(���V҆��B�|f��6��7t{�L��$I7-{4<g�M�
y��:��X�a�� ��(jE���ꚴ�v�&|���l�d���6��@6�k�ܥm&�Ӎ�V�U�7ߦ����9��QB/q���a�EE������pl��sI!Ѱ�
^9]��Ϯ�;�.�s';�-b��g;�h��P��$���7,���f�YC�}�����_|߯�&�k�I�-o_ᖟ+�
�I�(<�^q����{y����@]���_���9/幬.�����)���c#�Mw2�Y3丱v˫lH��W]aL���!l�.�K��n�.������K"/Ұ!����]�����񙔳/�:}��1c+U�a��9��@���xeo�Wi�;7�&S��$�$7���j:e�}�pf�u7�9[!x��s�P���i-����>����d�Mµ�ƸP��v�c�}�Ѻrg�K!l��nǾ5�5BFS�in3k]�i��N�Mݸa�qڙ!n��;���?���� � ���y�[�և��*�������>G�G�l�c��a_���wh^O���͕�;�mre��\mHnJg�F�h����8���~�3��uCڶ
ɝ��Ǎ��9�Vn	�Q��ӽ�K�m��r���ܙ��i�]�C6��$���;n*w���;"���c�q�V�Oh��_wܘa瀮�.�J+��(]�P�tX���|��0B��k�W4�t�9S��bd��ǃ�hcs?��W���bއ�6��^2�C���$9�f��*7�&�wgV��4�W]a������=��#b7�=�Wڸ����x�B�R+��`�������`z�5�������ʰgJ�Yk�&�2�rn�^d�
6�i�r�r�;���5��m(�E��nGs]('�#��ۼ��`�(���Z���DϚX@���m,TX����P��R�Ւ�WwL�Q��yFt�
�o���|���h�0��L�CF�*K4���Wcب�;�Q�oBҰ�OüFv��1��hg�kg���y���D\�FII�彋d��G��E-�����a�O����z��:�w�Vߖ�&�[ߙ�`�7:��
a6���A?/}t���D^~���#�l�Y���A.Z�T4��q�) U�;��<��1���u�nK�Bӂ�pU�y���!�x7dٞ�]x���;�Kw��{j�0V|f�
�� ���R��~v��(\�N$ĴkB��[kF�����y�o��j��A~_�v�^���9,��~ߧ�#�_�k��7�����b��VQ��(�r@�W��O��� w�
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
/Length 7083>> stream
x��][�$�m~?����\�K@�ޙ�s��ֱ�`ƀ���,]HI�ӥ>=gf7��K��.�H��(J�i��n;������ڒJ)�~�����m�o������z����p�)�����/xP������-����^~�'s�����ܔ�_������n�㧗��lo����Bu3aQiw�����˿�q�v��?/��� G��@8�� �@�ߡ����Hj��/���p�ۦU�r��F���|�ؕ���ʌ�p�D��������ig7�f�n$w��6(#k;��7��;�������{S�m�z�nZ;�[����M��fC=�/����N�i��}-֠�6�=�����/<7���o��ԗ�[��g�mqF"P��{c�ʘ��"�Ӯ�}�5��>UP�x��#ޙ��Y��M+�Z�����+������qc0Ĕ��| ��Ŕ1��F�\(w���m�C�/�~y�)�?>��1ʶ;�n7����]�>�M{�,i$"��ú�X�!���>%��,�b*��x��ٓO���;��r` ?��Xp~�H���;��w�o�`��.��BhTn�?�t�s��g,|�<��qV���C"��x r͍�1��,d�%�M�����F���P})W6j��e%�io��r�7�A|�TF��E�#�ʆ��*Cݿ��7څx��AsP�$��5�a~X�����QB�4����<�{�b��b�y@x�[��hBr�!��;���g<����K\`�����:�a�b��u�S��:���a�ҍD���+l��>��ԸC���Nb6�M*l�7�{��m��� ��Ā	�7�0�t�!Y�<�8 <��F~��6$�7���q@^m9�"Lo�Á5�U�wơ��4����k�ie#�����i9�9��!6h#��bg�Ɇ��&C�+��[�����m[�瓬X	�l�����t��	�f�R�jmΙ䜢TU�n�-j���%ߴ���4]�)�m6gUJ�.8U�؍K��ɖ&���jL��I���Ly��@�����*�Y�Q�.���K������ ��&�ڒ�S�MWy�ވ���A`�؄u��ݐ�X���UU���u� (I?M�w��nx��y�R�?j��؅Px�!Ǩ�ci������gS8#��{d��X��Pu��kj���si܂��ס�SĴ�=w�<�����`��\�����{�hJDf�G����e�{ȵ�i�R�!jxB�q�4�[�xA�.�'.�uUhz�z��L�ų(�B��CU(0a�2i�r!ᗤ-i�����I�R�%@��G�ˈ�H<w?�K=���E�����a��� .������^�|�<��"Atr"� vN�r���,���H�5��E-����[��������7xigv�<9:����u��c�B_/+�8�ݡ�ף�N�]�)IV���s�$+{Jɷ>^�IC׳^�}S
8���W��K��.hZi$u(vSj�*�+�.^���M�^|��O��qn�|P���=�êܕ޵!SS5Nj��ygr�iS��)Mc:�*
�������?�M{���M�ܴ9�H������/�l�^{\�
���� ̈�� f��Je~�g�?�w��<޹��Đ1x�̓3.f��,�N�F��&$: � V;n�7| 3�6Dï1`�={&Z�7�o�m)Bh�8Y��`p�����.D�w�mi�8K���`���6崶�g��A
�$���8n�_�x�AOY���o���gD��^�[G��^�g����&�F���u�2�v�s� *K�q� ��@HH�H�dq�l��~}��	5�5���5���u�:ȵ����|e�\>���h��JU��s>��h^��b^�C�k��Z�K��\q,}쳜�}f *�.2d9��R�E��YzvsC��: �(a���,��+:�saY\�z\�R�_uV�^�������7 &��X�����F���"�Cl�o����ѿ!6�7D�v@տA���7��,l{Yb��l"�l;�O^�w�����Je��`�TU��)�Q���hr�o�A]���Ŀ�&���������Cl�o��\bŸ �C9�S����~~��o��ѿ9L��LGY�67V0�o,�c?�o$>�v�oY���7�jŵ�e�[�4��q��<a\_z������V�jvNN"[��*�E�|$ ֏�Y�,�`���2���mP�X�[��@ ��t68�b�ǰ>އ�d�0�1[��S��p6��я������9�b�2����h�M,f�B�Se���lC�W��t��$[W��;��d{�8�̲��f`gH����}�	=w��1\�D^.K��W}6��[|6�]{��َ����D?�\E�SWM|���A�;��F�eW�K'�Q'6W�����Ӈ�,Sj�kX%�kb%�4�����k�'�Y>��≬R�$ǼZ
�vtd ���#{��4���C�֗�1��n�)����������'����N��j/SEa��.�\Wf���P�:R62bp��N�xK�=\�����Ο/��=��,���+��+�İZ"q�k�E��Қ�L�TK�G9�=��ʵ8�RՋ�2peiZS�q��c�*�
�99{e� .�,/������I��&�-|Z���	`4g��q�� Sz�������#���i/`'�����H�Jz$�!=Ү����M�Ycl���b��F>�XGY�����%
�X��1�%:�(�U��&H��$��iX @���IT9X�(V9�����$��S]��1��{��y �q �"?5$H�L�jN��F�NUr��U�����Ic���2>>��|$�i�ĕ��$H�%��fw��(A��\+
�®g%������rT f/�}�<ïa����8Y[�L�zb�W%V�<�&)�].ܒX�+og��u� ��bcz�9=c�~�'��A�Mw�4�n�M�;�ͳ*~�M�4T4����L��RF���R�5J2Y�� �ɳ��R��B���L8�)�B��'2s�����b���ڋ')��AlL� �m��AtL� 6�h�S4��)��DU�S4�iD{�T�5�t���t���t�u�T�񁍀�/>V�I��dOd��$��hL;�ɞX���� �B>P�(>�q����k@�U&/��K L����b�;�O^��ٚ�p�����y��踺�ظ���<}At��P��7T/��>�wP�����Ȣ���g�ɝU/Kh�@���g2MDH��+�Q&0��L����^��
&��^��	���q��4�Ap�� V$8T0�L�
&��*3M`�l��gL�
��sg.Ms�+U)�>��1N`�����C1�}w7�.�+m��OW\������&��<�O{�����aðOCт�V���^v+wE���L)�a��JU���Q��c����II�����؈�̒������:�%%=͒�f��cw?��U�ח�蝵���F�4��bes��6)\cs�]6�)R�'�rY��)��)��)�g3�X��8��T�~�t����4C�i�!�V�ŅK%ZLY�13��iC{�Ԇ5�����������u�Ժ��~�%���� ��*UI^�!%w�W��W�9����X^9|�Hl9�����j}�~�$Kt?r0�N�:C�yiS�+xu��b���͉�*���`�o;ʥ;�@܈'nS�i�7�Ȋ���C)��yNޛ(��6���*�G` L�j��\5bsnk�U#�����>
Ct���0��bBD�(�jf��0�J����"��D�D>E'���C(�!�Qd�9L1���e�v��Uz��#1��H�*5�sՈ͑�G��^Yb���NrՈ��j��DU��L#Ԙ��p��p]�d�Ϊ9#>���\5�,Uz��HV�J�Z$fU]�����U�P����Lq�[�����ux�WY��u��4m/l�Z^��y.��q�G@���ȶe�L�-p�rpɘ�TL�z:}#n
��.��M�3�!���n��fbJ�L��"����|�Y�u5��A3(?��`͔NL�Jl5㱶�.�����8�����գ^l;�E�b�֐�����9�4?Z/<^��Cu��\�ߣiɨ�ЍF�|�b�`����8�"5� IJ=�ڄ�e�{-O䖓�Lݗ'ܒ�W0������_�o%1��;�3>_8����ɯ�E� ?}�q�q@'��)� Q	0# ����������c�`&`[
"	`�A@���*�u��&�n��@���cm���SO�6��sݮ B�e��Zg;�2�xA�?�(���Tj*U�~¨��g|�������t���F ��x:�`��tc`CQ����y&����I���T���L�0�C}�;~���U�(P<���M�8lд�!�;�sT	ee<a^C3�o��1[^�a1�5�mFÛ\���`y�[�	LS��|���`T���}��+t�����1�c�C�8]:��R��X ��-X�|9��pc����Aaͱ�����%B+Mx2V��WV�feաm��!�#E�%�#�
���&j���	"97ʹ����Sյ��m�
��Ta<�G�C��	Y���ke6��M��z@0�h��msGЍm��G��&`��m7k&���-Ztj�"1���2���X�/fb��w��7�.�@ &���[��擤�,�=��=e�d���{�3X��1��_?�x}��e-��?�oy���[��X>��~�x���,���y�NzN�;^ʗ/�F{�f���x۩ϭ��gd�������er/��&��)^z��y�ⱎ��z`�d�U��˗�O��&��.m���DI���]o��]o��]���]o��v<t��l��T�
'��"/�E^cx)&be��m":��P-��v(ۥ��h����KycT�JdQ�*�O�4��TK,�R��8*����[�����]o�]��c���v�5ӮC��]���E����2!6˄�T���X�X��P��/0��E���S�D6�ҳ�]b�z3�:���#�N�2��R���E�X�#1�}ś��ܗ�֫t֋W��KKCO<�A�Nwg���t��Lh�{��������O<�y��w��FƸ\u�|)��N�XT�q�Z\.�'��������H����X�$E�r�w���GB��u۴0�G{>Lp"����I�����8�0�ؼE�q�b�-��-Z�����,��i���U�5�;XL�c�K#�E9�|���ȩ��EX�q,cf1[��r��H��9��~ڞ��|���n����#=���юn����#=��8��e��7Dz�&��,�j�k��#�F6�Q� �f7Gz�e|ts�(���,W�R��zn��Ql�վ�"�Bʙ��!YO�9%�����ڸ~��|��{��˻��#�{��_�|�!~Y?>k�,b���K��{cu���7�Q+x����H�W�����	8��BV��}~u�}å�gZ\q���s����>�u�|�*vl�ñ�׾x�Z��~��=>�����g�S����	��/�./��<��8�L���bZJBe������4�-����B\g\_�[�����k�u�ť�8�d�)q_�r�#fqe��'X�%�9 ]��m�ln��a���|/��OC&�g�4�{b��|��ro:�Z��Un��B���ǂ=o�x���n��G�ŝ!F}�|���Ys}��O:t�kE�h��Vi���X�U�Xuj?f�RՇlǝ(��1_ށ�����T���sX��sn߅�),��R�'��	��� �V�O�7��T.�+ê�S[4{��> �o^�|�ÁaO�����B��Bi� �C;8E��h�=��k��m��ܣ0��=�E �S>rS��=��"ݞ�r5��P�~��|�=�d��aRc1�6ڙ�>��Ѽ��U�jY?CC%F��Rx�<�T�w+�̂F��[u=��G��0}�l�i*V1�ہP�ف=�6�vڶ���������)�.���ρ��9��f��N�ع�Q�4��T��P,[?ԩ�1鈥�|�a|��|�{����!�q�H�D:Ә��-�f;"�w��@�N��Óv,(����o�ޖ��ܹ�`�U�Ī�Pc���u����OƣQɺ�.���ZC���2`���]�a�L
B��%ƅ�N�kM�{�Q�������K�jއw��S�=����]z���?u��I��a 5$2�iLnT����İw���6|��Е!%��P��X_��H�6�eH)��Ad,CBl.CBt��b�n�ːʐ��!�0|膮�B��*��Qi�E%8D>���RY���*�L�3�
�� �S���!�0����1�e_����N�Fl<%���ѱ	��	�������"��37�������(5�!�\G�>sC��:��S�9s�(�S�9�+U)�^��B3�ˇ�ߩk�~�������jZK̬�u'�����h�L��a�ro�-�r��W����o����]*��Kt�꒸�)�A^�e�V�ޯĨn�bq1�y�b�6=���mx�3%?�L������ۈ��ۈ���c�Ķ�4lӣ��ӴM�7��4]��g�E:�����*iܦ�̢�Ķ鑬�5jJ�6=Ħ�)�mӃ7o#6o#v5�y�bSԔN��!8EM�����&�y�^i�QS���Ads-=ۦG��Z?o�+���I|ımzY�w��Բ�W�]/O].6}���[~��=>��+��Yټ|.���O<O��>�"��.���L��5�UF�E{�ey�H��]��� W������Z�0��/s���Z�ڎ�����SO���U���)����>3빢�� Y��b(�f<�@����#_œhK4���<�Ox/�[�R���L�
endstream
endobj
19 0 obj
<</Filter /FlateDecode
/Length 5369>> stream
x��][��6r~?�B�V���g�}Nv�� '�A0^`7�H�EQuZ�ь�A��1�_�d�X�*Q<��1�l��a'��{�1���_����+Ħ���?���?�e�;�f�n����4����?o��{������K���7)�����������Oo��lq��W�(Q(7�w����ۧ_��Um�m���o���_ *s||�H@���2�67�0��?�rە�P.�qud������(�� sG�
f �B��l�(��B�;�+��8�M(o��;��Ǜ�nw�c6��V,VI�;�[��тp�|E��!/wT�C�U`�&z��w�z���v3}(��M0�_ʵRa���g_@�AAm���Fˌi%b.
U�Fo?c� �t�7�{��#̖���$Lr�t��"bc����8��k��X�.�8q0bƐl��,�˝@.
�7>m�\��梯>�]kiڝ8+t$�!�s~�Ű+��!$"f5�V�����Ÿ�<��H1T 2DH��"6�F;��V�3D{���FE�����e��A��!��U��(�2�a1��!�tEjEBF���F$�tm��"2�M;���`�Ѐ���R�t���F��L��I,�Nl���M�qCl���'C��2M�dny�Y�4Cfk�`��?�����������E@O�F^���	^����Y�J��;������,�xp�]b� K�o�2�]k�J*7�&�`e�|bG߀�1��Q�WQߐ���U����2D��uG�L,��H,��B��L�&�>���$�&Ӹ�L����P��9��� ��s��0~Hƪ�`C�jK�bV+?p�,ѣw�!�'K�bз�μ���S��z��fjBa�dpj��Lb��j�o2��謩���K��Ī:c��P�+�������|����`�[�܃Ӈ<��9�@L�)������=8����{@lr�cM�b0�<Ub�{@����C�*�!�C�������I7��7V�$!<��Ԥ�g]�!��D�d"7��	��W<*����� ��b�L��=x�L1���#�at�lD�Bе�BGl���,��Ä5����{�׃{h7j�c#��l�v��+'|���DfM$�_D�d&6ݐ�t�g�J���/o��߻7x:X�&6���C�rr��%����8z�����;'���; 6{D��!a�;����;d��_�n(:����c!qH%+d���lj�铮ɐ��,�c*Q�2�M}�!�~�w@�� ���1W=1���C�bJ%;T����ʩ�ر���=z��5�w�׃wh7j�c#��l�v�m�3'���P%DfM$�^D�d"6ݐ	�t�'�J��r/g�r߹3x6T0ҷ��q� L�!a��c¦�#�G����{H��=&����{H��zpC�P��{(�{(P���]�T:p��Nb���J�%��>��tڬ�2�ӓJ�O䮗>���GH
��!i����!a��c��T-S�=$�PvL�� 5�L"A�L"aH�����������5�"�Ӻ#fF&�H�v[!�M8����̗&B2����lZ!s�i���(��^~���c?�=�%H{3��6g�MKQw�����JA1}��*_(�3��dg!䱲o�ͻo���׶7��+�mt��@q�����/�)=i�}kK��	U��u/+hK�H�0�q�G���ǌ�c(CX#c��e��P��lW��9r1>��z�#C��[��ۏE$9Wh~*]"��VT_�q�B�`�����p.�@��(*��F����<}0Ġ/L(~pNV,�j!ZO��#C/^:ͣ��AV�\V���3;8߂e�0TN4�v5�iO���Z�*Q}����U���n�+S�F�_s&�<���F���wU����
�F��X�ΆL���.ul�3xJ�*!�2WL����앵�2s��C��|=6���LzY�DX�{iѼ�,<a
ˑ#:��ŵ�iY�&����?8'��.��EVרn�M����$~�[���a+� ��.G��l����Z���n��1ϝ�}!�z��H�X͹u�wqԅ;qE�7�Ƭ3a�s!Ԅ���f�C�������P���,��lW|��x����0xx}�����ب�����m��hXs���R�1e�|��K+ї���84raE�e1L�ؔ$�ub�Rc��=>Γ�Sv����Kټ`W�YޠV��Fg��uQ�0ü��:���K�8W���i���ԍ���"F/$CC��i�X$O�U�إ�t���7>HY!o#������O����s���$��!&�~!�D�����cCK�r�Fq<��)_�b�KN�R]�F�؅F6��>�����Ɔ�3f�!Uҝ�@�Z
VЧ�oD�"i(~���x7��x�	<�	_S��3C�ҟ��B�}�^7�o>���G�ۥ�2���k;��n�|�h���o2�]E�@J�S�~!�+wn�#��rCR܀��h��6�½"R� P�[Y`�۵Q�����%!��b����q܂�Ɵhv�ޢb��#�B#}������D(Q ��@�@h7���7�e��k��<�z��Q$e"��� ��2���#qXh�x���&mO�,@�&�F�*��$�*����lI�2P��@TW-a�� a�Ăpk
�x��ï +��AgD1.�i�nN�ޙg���M.���ঁC0.�Afɥ�3a�H��
�������+��A����������Ų2����l�0���DQ}+��pЮ(ʣߗ���e)[��Զ`MN��zc ���l�u������ 6���k�]�,���u%
S���J"���&��IM��q�>��i����RO���9[N5��g�a�,7�3y\���N)9��r�V �T��|n���,�Z?h��u����B�:}�S�,����q^����+�j���P*.#�J(5�5��+"�^,i}�F~��T\#�zVBAT����ѴG�E9�J��p� X��cr]b�]����=�u����]m �Z=
���R0*�]�-x�C�蚱�j?<2���#�M򻵐 �K;IXH��)J��OW�r��,X�rt��LB;��;�V,�J�Z_��d�T��<Y��Tt_�P�qK��S�o\s�[IWc,4%��:m�BA�B4���N��=ò�L��^R�?XI��~:u����I�>��B��=N���Tiq��*}'}�8�7AĹ�R����Ȏbk���^��j��A]^N��Ym~Y�����	㯩�5	��1��C�b]*䃻�y�����x��8A{Ѳr%#peݑ�۷�^�)/�~�)[�ѰU��R�0�m�|iuY�Ol|��H�7�;�x��� ss����=!��'�w��3�k[V��h&����ֽ�I�K�Z 5��n��BM��@:a��)VAʪš�0� �Ҥ� �{���� Z�J )�NIy�@JQ�VR��LQ��H:��*^>��<-x�R/��\ZRc���*�P��\i�˟��Y���&bo�z�.�D���9�s��:��5t?Թ �~Aq�� �����
��ƕ(���b�5�#�Z�ytR���w5�V�z�^7"���@O�G�{�p�k\EC�˝ս\�Ѳ�υ#K)��4ּ|�F9Z��ji�˟T��Iū�m:�CtmZ�^;��R*s��<Q뺐�>�wY;<�$�+ٜ�e��GL��A�>�U�0=2���I��d�Cc)�4�&wA��{yEگH����f^�7�?��<��!�X'	U��4�C��c�*�au�����/��>��7����.}2.�%23�š��$F
���D����]!*�����mz+iPb~4F½
�q� ��$�lc���PC��F7	r+{Ԣ�6�}AP��DȀЮ�O�!H�c�2�@�KAL�/a9N�rh�H�v�1��(5]�����߉���R��ǞZ�n���Y�q�pE0`�Ca��#�rB���g`�34�ťY,{�=�D�X���c��V~c�':�$E#b ���tpv0p�JSz ��CHhI�|�����OѪRH����	��0iUEN:o��hZ$S���Ͷ�kE����i���Gp:D�/=v�>��?� �ѯ��x�m~��{�D���+�{�F����+
Z"F�O�������
��2���+Cye(����jY�_?�XM��d	''�<�%�	�seZ�BE�n�T$K �C$0D��c�l�mҮN�$$l�5� �$4�&	$�v�D��W�I�߸�X����"�!Gm��t�1���":@��ࣨ!ExzYH5���!=�R�)-8��O�2:�`%�(�q3[�IB �;�˕�5n��� `�Z�| �pܔ9� zܽI��ܸ3�"4#�M	Z�Y��{N	��z'�G������C�kH	��c�Ð��9��=��CJ,�H�!%V��4%��X&o����M�}��&JNWh'�ZHep��_+3 �Zx8�J4��@��u�]z��'������R� |W�vwet����t������I ���]ȍ�@E�]yјv{�
Us8y!�xLI:�[�y᯳�t��_�(�;!�8�V�w6}q��J:m�*O�$����L�����b�|��4�n<�tetv����2v�GnS�qWY�;�YP���9[����G�?�7�m�?��<>���vصSg.%�v���EZN�g07�Z�L�܂��n��	n�)��޳��c�s��֑p��	�c%�x�}��gGp��V�|�����/L/��s�N맘�;�k�~��� k��~ހ�C��O�[=Ex���ϯ��9�a� ��M��'���~,�7u�qW���_xZ��Yo<t�	$_`�;�y�ߏ�yRwa��|��YO���������3��Y��H�L&����ȁ=o��.����I���(jV�HxܬBXʣ7��&j�_��Ŭ�ܱ�F)�V��?c�y���D�����z`��) �A}�/���6�^�^�}΍��87V}�?���P�	�l��}���q�S-��r��.nL��H���W�xr�]Y�L�KǕ����s�~���c����@�<"���fv���{��|*�B��O*վ/wa:�����4�-β�o\�߹q_�r����������)C~�������#\
endstream
endobj
21 0 obj
<</Filter /FlateDecode
/Length 6654>> stream
x��][�ݸ�~�_q��"�I`��x��&�,O�d�?�U�U�[b[��N���|G"��b�,�6�B�����m��b"���ק<��R������������כ�p�K-���F�������}������sA=����KDv�4}�K?~y����_�E
�C��y!�C�Ǘ_��}ߕ����ߞ,���� ���.�j����!DTL�%T@�F?9&�I��\ؾ�u2^ѳ2�ҋC��\1�\z�� �L��ⰳ�w�Sד������v=�U�����I�Y����Ҁ�Ja6-���;J��Ϳ�z�i��Ԋ%ؽnOf�M����Fڐ�f0X����y��?k�y��߭�J$L� �a��]K�����	��7���+C�Q� m-�,`�K�2�,��x�x���r���yazS҇�Y���2._	�J����gm?���W�|�/�RB�+�fW�5�X0ֺ�c�&�����Q�������نg؉�I1�g2DH���Fڈje�dz��O3�!��nʚ��Į E�[H�"f�Y���Dn**�B!��2?�%�1�h�ܲ���xӃ�!h�r�#�D$�� ��>��@�����O�.Č�6�̌u���Hv[a��8��PE��K!YL�lV���Z�G�����A�������C@G�D����x��u?�� G�����6�c0Z� �_@Hio9������/�z�����s�!6��%�c�_@]�
Cl�������E��>e���4~!A��js�DY�̘+���++lt0��8�ҡ�Ve��%�6�U/l��eO��n�޸ ��X�܂�����b�[p��p���bж�BGl����-D(���[��s���̂J���X��(+�d��f�oU@l�TA���$�b��U�4�W��w_���}�o��4P0��
��n��B�1�a�������7x߀X�}��o�X��S��K�Č�6�̔u��������*sU�lp���(�Za��(/{TnqQ��5 л����i�{Ă1�� 1�������K�w��h\��w�\CĀ
Ѹ����!A�5�o�5���5��d@�M�4�9�$�YM��!�|��@�1C����%NÐtC��tH#{!Lx������=����;�6��x��/���bO�s ���ϙ��X؅�n~A�@V�<�ٌƠ<�7 v��@�hĻ�&a�y�������s�p��].��E�B�F8~-``Ha7���mERw cN;`8谟�#aL����6(���{PG
�.��$�6(w���xe@Qzǃ�ʤ2v-F.�(��".�#�V�L��2�R��L��!�G��6�V&w<���4��Ş�3I~���h�p���9�SsN�X�[,_8�9�4�������0�������C�ې�J(�n���K�-	b��HgQj�%H:�##$']�G�>���1Ǆ��(	���+0� N��Q��6RW�Y��4�
������6��YT*u�wa,TG(TE��/�`�T�5U���^*�6T�k��\�|��C��S���)�<�{��g��ߺ�=�Ox��z�+��g��3�_�n\��`;p��C�M��@�!%;4�K��H� �k	��S����O��x���@��m���A�%;#���� �t%P�t��y���h�!@�]� nƨݠs��/� �O�0�$�`R� ��c}�^a������=pVy9��'}�;�t!~�]�oλ�y/��0��u�s��p���9��RW�0Y�b<Ǹ�k��U{N�}�,�]�`/�u���&DM%5mʨ�=ww.����F�N�TTӖ�j
�0��=��Wlh�������L��C|��F�ΫE�zFF�q>����p����������j��h���麉M7"1L�S�_vwڹ��){1���(&��!Υ[:�Y8h�Ň ,��m`��&B�2��fXXU>g���ҥC6����^�~�9�Af���~�>,���;F�a����;�0]\�R7	F��8�wF�����\�s��>O�蘾�$5�&�yb��Hd|���S+�!�t�<f�p>�O&�,���,2=aF�g�Yb�?:T��a�����[�tF�1>�fQ�T�gZ�����IW+��,�q�ur$f��v�f>�����p$ ���	��۴�I�9�}�I���f:�>ÂY�Jun�Ә�-���R��~�V�A}V�~x��u�^ʧ"�P���;��u12����i�˓��J�_�{LG�_�CTu@�}�S�m7� ���ي|�㙵5a��m��++��Ro:j���iS7.�.��0�	��7�i=�m�x�l|_�����i�b�ǝy>��/(o[PBD�i�ゲʷ	W6bi�����Ƕxi#v=�m���]����I��|���*}�I?23'=�"���^L_p>�=ͭi�0o����,x?���^�0���G]�i���x�7�B�9W��4zQ?۞����2n�b2��4�3U,/ͦq�|i�v}���
����R˟37����a�z۹�7�H������>� ��'�ab��
9�"p��&{�A\���p0ע�d�uČ��IIc�C��+���,���aFS��̛0*{��a�΅���ߔ�Q�t6�������7
� �0WoB� lo�aZ{kɄM�]�q�4����+�P;����ǀ	G��sagf�� -
���FL@���s�Θ�2=�@��!e��}�7m��s �	�y;��@۵��[
�ՙ���������8o_?+*+ۑ�
ܬ<pW�ا[j�q�3���]�d�=�a�����l�1��i��d���c����zQP��N�=��3M�5b�s��9=�v��l5];�������<��2������6�0_�� �\�n��빼��}����L!�M�)U�A8ͻ�Qu��X"�~�n��t�M�\/�I\2�ԙԅa��MT_	�|Y�LgƩ_�������v� }���[�q�*��9Q��/��#��
o1���4w�S�3�V�(_�,��C�Y��|�u�.��f']������UYoz����Yu�Ӧn��r���if��2�����ۼ{k�N��//��k7MW�Q��%i���7\7�����ƍ,�P���@˃����;��c:
�M)���_'��pE�0��Ӂs�,W�$ �&>#���%��#�{�u� T�n������i��z|{i�s-*]N�^?'_�����jәij�뉨�=6��m��I��:ק����@a>Y/�9�.of�v�سC����%��ћK��o0(��WN�f���ֲDCi��9�rj�|��~�l/��j�u!�M��|O��Ho�A��6���-z����fL�����8;٢��^�7֦ϓ�x�6�fO.�NXp�N?~}�>��MZ�U�6�O拶X�m���@D�����:m���bE�X-o�� 8a�-���B$>�t7�j���p֎�v�+m"�`�P|�P�0��v@׮dH(ҋWJ��VmM���vsJ�&c��n���[-j�*�v�z��'�u
��1����q޴�yКࢀ��Q�Df6a�Ԣ.�jv��HJ0\G�K�?a�]T�K!��m?9��>Q"�hZ�����M���)����\웤%�u��U�, W z��?ɬ;�MJ�:&��{��P'ܖ
9��
��:�An�E�ދ��� ��T��GZQW(ZĒ���,04r��D���[5�#X5�(����#��`�� r�?��`�� ��`���7�������7�X�������!�F�ų��ب��1T`�����e
�Uxl�313���a��җ�I�=	`�'�ԝ'	z�$X���$�x,^�i<	`W]�\5r�z �`�x�X�;��z����r/��[U!�[_!�۩>�$U����I�p�X2�'��
E��{��g9�]�����[���*gge�o�>�;+�Zg���F��
�h�Y!��� ��Y!�;+�zg���s`1UD{g�� j��Z�
5B��wGÏ�aJЀ���'��� �3�b&�S�a��җ쬌pȦ~4w9d�m�D=F��W!��*�F_�h� �G=�Q�}�cD�X���W���!��p��C�Cds3���D�������>⊲B�ቫ�e?�_��B}�k���r�I�����r�WYHۖp6��\�T�XmaǷaQ�_ �%֔�j� �M�6�
*,�ե�[)X����T�����3�y%gS5d�Nn�ˌ	V���m�"^ι��kj|ұj΀ᩡ�՜�cEn��Bū9�e՜3f�b�䵜�nR	�B������r������R�VP��h�^���
]���:����ac�����Z��(�S��)�l�Ė�j�F�\㚕s&���LpSЙ5A�YgTҙ�E%�Tә�JE�I.��s�!/�,�@hǊ:��Zs�(]$/�`��xQg��v4N�H�DSӹ���3���:!�1jH�D6����hK߭���	��*쩂�O{��R������~��ĵ��Tyƪ�7���l?��	�Ԇv��x���b92YPV�j��F���������"��b�>c�i.�(�9�'��'������V.W��j�
��o�޽��ٺ�3��/ѱ�Q�Yc�.w%�_]��X�Ӌd���4_^n��L��6��D51�V·'����)Zp��M������p��?�>/o3}�}���C�p�4�@i���)s�O��H�
�̄WJ���݇���[�	7�n���n��v��qk����o�"�o�"6� 
w	�[�����%0b�n	��nI��n�K����_�j��e=�6 �0�( hK��J�$ڤ ��v3�{u���%�8<\�v�v�K��a��~��q��~��~��a��~��E�H�6�%�fj�.�p�R�v	���Tl��(��a����%=l풺B����%��souH4�@���Yܑ {_���Wx��:�~1�;���󙖟�_Ot:��Zf��;�q�����,r���g���;��;�q�Ʒ��3v�G3v��<��C�f��+M�6����T	csUe��j�U6�U��y�
�ͨL�l���0\[�K���g�`�;؃�X�h��񼰟����;��0��0�q�f���M7c���q�f�p�2�a,������U���8c3��d���+->?c{�����د_8���d�\t���V}II�er�گ;D�Ί3Ӈ7Ξ��RJ��p_P����|~�;}�f��;�UNGy�r����/��ދM�y#�7l�z��;��֥���+��:�E�Rpt��
�������Z3���pB��.����J;'�G������K�K5#t�$�!�l�US��ubߩŢF���1/�!s�>s�qe�h�9�X�9�ؘ�h���XYY᛾���Z{j�V �;Z+a�� h��Y�u
	��3$<Z�p1��b��җ���s��!��!4n�z��]c����M���x�&_�.����U�B��	ElHrE�Or,�O�v]�~ ��{���N�MUr�����w̚���Wa����A���x�5��w����UwƠoQ��;Ơ��/W`��(ٛTg]Oi�.�oSӴ�j��)���lY�.l�½���^��'�ƞ7%SS���]��X�*#ooփ��4��Ɯ���?<�����O)�#��|���)���\��/ ~:� ����[ҏrl�9��a�-����	�3P*�/O�T<"&<�Ii,�Y#�tI qX��%��s�(��X���f�TI@�&�˔,u���
ĳ$+�s$+�2k,�Qò�,��r�`I<5�
�kj�=K�d�=#0XVȽM��o�s�^D�D�YA�Iw�
�R���J������S#��yt<5ܭʤ6�����Eb�}̽,�0�Nḋ�ix � �bY���+JY}�����ts�'d}��Æ����Ȯ������X��!��x"$�>�r!.d�����0Ti<!ʱ�1�f�����8�X&d�l�	YA�	��.*`�T]5�T�2�TG��n��X��8M.�v�yF�@`8�c_�{�]�.@80�:z>7�
[�΄���ή���{��	$��E�;�$u ��6>M�kڈ�8y�;��l�Z��fJ���${K)9\��t��B�x�W�D1��� W���^]C���P�> �6��c0߶��7��k�D�m��s���2ֺ�)�:d!f�i�>�s��#��u��c1�S��O�|�r�Y���\���P��� �,¹�����~��De�-_��`"A^T�2Ϭ+��J�)�B���zl�x�@�eG�%�G�����]Ĭ��4��D��䛖�.z�\�<�s�9�i�N�X������D|&(���ѕ5��)'�^]N�5r�o~�e�_Y'�ͯ�K������:�1yhWB5|����MKԚ¯fZ�E����!����]�W�]���8�768�_��~�k��t{-
endstream
endobj
23 0 obj
<</Filter /FlateDecode
/Length 3758>> stream
x��\ٮ�}���� ns_� �V?'�Pb��;�����Y�#��e�ޫ�zΰ�b-�Ev�Vcs�Y~�[�����u�i����ˉ>7.��z��_�u�ǟ����U4����;ܨ���K������?�����b����Pw?DQ�z���?��|�	�b��6~1v����g������?���?�s`�p{  ����}h] ; _o�p��w.��F�($�a?��r�b?��[���v\iqMr�ܒ��&t��8+�Xٽt{q���pF1v�K>t�W��r�:��~ܢ�_�=��5گ=��ڕ���W���ϊPw��~�rTՍ�ѕ�����è�/^{�|��.%�<ѵ� LhH���`���.k�BV�7S�.�ޤ��3�F,5�1S!<��ucl�p��f�OC�7f�'P�h#�T��C�:i0�r�B��fCb��ZB\O-!���a�����)���<ћ�Z�FK�W6���>��8䴚`�"�-~�T�!�J�9�/1�	���IB�Y�C��&�� �U
�96A͸��f��7&��:(�,8|ʣ,{ZWEL�*�q�����b�ånZ��V"��5Y0����)���:��[�B9��wdoc��Ӊ���>�����,�p]�����V�+��Kj�Ðm���6���x�7qBZ���~]X���0��0����#;hF���Aި�� qG�.)=aʙ5 P�OL��[�6�p�$5 �t��P0ĝ�#�
����5��J퍤�	��	7�"
�S!"�,�ih�cn�P'+[D񰊈�n��d�Ad�5 8���~Y�Nt�7��3yt��1���QΛ0\�-5�L�d$3���T9a��@(�+�������B���B������;�k�D�w�sՈh*a%t-pXE����=���p�|��A0�K'��)_�%+��4�귴���
��5l�k ��h��=-���[Z ���l�V�W��+TH8^�Mx�V��P����1cFC7mC�",��E ��@�kL@��P�.i� Ҁ�P�-lO ݞ
��5�l� �ڴ��i�R(�`g�P��B}�P�5bhג�1���M�.�b��a������ij����w{�G+[�#�����	^���	�i&@���kܲ:�*%���$�G*�̸y���S�b�(����2xy��R�=����*�*����^��>l�ǹ�6��\h}�z�hG2�C�.���z�ە6�/�_1�[_o>�y���	������^S�h�I�v�Ou@ժ!H^�P��V��p�[����O[	�
� J���Zx��X�+��re�="{���(B��Q����ʋq��cH�+%2PEKف��&�3�(���rwC�Ꞷ0����D�]Ut%b�P !i������#fW��>Q���ۥ�A�I�`�@����El1�o#�ZL�}BL��WQ0��E��C�Ѕ�r�X�������'cY�+T��X(�S��e�R} �&±P	4R�C�0o�6a�52��70�C���JA�I9y�� C�F�c�9pB�
d�y㵑���i�^N�aQ(���P���w �_p���F��p��
 �j�ѥo��ǅ�	.�U񷮑V������e�"r�a;)�0��_�Θ�%��v��n��XP�_�r��E���/0�N5`Ѻ��0\.�a�. ���R���4��Z�y�+D·/����$������8݆{��1)Q�1��ol,�����:�+:�ܡ3�[�l�A:3�����ۢ����v�N�*���W��t�HO�Ӎ���l��ÒnJ���A�ؘ���R2�;�[d��&�����/���U��@%��Q��\�$�ɖ]v�J��ڮ_�L��{���_���P�j�)���4�����e�>]f�(χn�G�,Cj�́���+��n�ln�3�|T�cϰ{�t�;�E�M��/�{��������f�xqה�|3��J��� ��B��!Q6�M�c&CO�vY��h�j�b6��h7�#�9M{mU"��2Z��d�1��b~!F6�k�*��������jÜ���e�Qn=S¡I��;_R-q��@�B�AX����"��x_3�f���DǗz�V{��
�q������PS�}d&m�
����=���GMU�)��Dh�z7��}7w�A�=�v����Gܷ���B/B־V'�foG��cvQ9�m� $�F��Ez���LM�.����0��.���ٴ�ڌz�L����C'�yG'�2ZT�d����$�F�i޻<����������0d�> ����j����۩�w��B	
ź��p��|�[�馀�6���}�no����_��g=sH�)H� Yd6�,j�A�J�A�V^�����`�F<Z��Yۡ���L$z�?~
���d�$�hxb]1���s̍��8e5�ر��u��&�$�tbn�\v��h�dP�(���l��zh�yD������Gl]�[S�������g WtmnS��i%�͢��_x�Ow��7�"9��� ���Q9X!�Wk]��[�MY�W7�m7K�5��>p��7:^�x�V��MQ�п|��J�w��dI����H�*`���{j_T]}�x�{ww�e�MA�-��ޔ3����j�
���P�P)QãO�Lr[� {���(f(��Z�2H�2PV2P�1D̀�F��EB���j�eCaO[0�ф$j,�YT�#��2���u�$��z�������u�$cQt"��)UhQ�2fv�g΋,����x�K��T* t�@[�J`f��8��;��-B�RA#jI�VT* �z� 
$�(��f~��cpA��kXl.2��q=B׃,R�%
 �y)Q� �|!Ky,�Ӿ;1�+<�i�
���-�����Mu� em��{�� \U"���\�I����ne	!E�k��eE�<v�=Q	��e;�����˿��ٖvИ�զ���m�R��pY&��(�7HGʉ�=J�H����L����}l����4q�ܶ����0��(���E��}Ϩչ�E�G)vg�,ᜟ��дW��Hj<7�Ŵe��ۈ=Dߡk%�Z����~��O������s	q�76�}#��2�l�������:IM	+qN����������.�S�x[/C]�WȾ�T�S �xj�I��\���בS}Y��Nu�glb6��WW��I�Q��]�I`�˒��%)���/I,ᜟĞ�/�;{�$��=U�'J�E�Xz�,a���?�hT��pm�*2�h��t̲����h9�}��w�(�M��(�<ߝ�G��e�,��-})�O�و>���Pq��RMM"k��$}�t�glbG���9us,�6~���};7��:��q�NУ�Y5%��߸�\��:����aBK3ʎ#~K���M��sЭu`�AG)q�eY�X�I旔�Z���3��c{����u睂���gq�����uǃJ)��$�KF}o�3ju_yF-$��02�ά���&s����l'���gӚ�������K~F�Oc�~�ke�}�L�?X��|�c��\��ke#B����Rj�y'A�A�)���I��V/)��.iw)q�&f���<�kr�['AC����.F��}��s8�J��I0"'�S5uӗ�˔=��CmJ��k�7
endstream
endobj
25 0 obj
<</Filter /FlateDecode
/Length 4521>> stream
x��]ݎ��?O1�2ѿD�(`��\�1�p�� ��%����̜���5v;�pF"���(�H;+�g�燙}F� ������]W&�I[�����/�oH7�tx�O=,�aC9џ�4��z��'=���؟=I�u�K��5}�[�����L0}�;��I���������Bh����/��ׄ��&�H�E$�qRF����@%�����ۂ#n���3ɥ[3Q+&�kU�&k8�^w�$W�L�B�{�f�f��ҭ�Wx�32�~-y��������nv�c&IH+�����ѼV��A�"}b�~� e���U�U���H�;�Ǟ��خ'bJ�vrJ��[�l���W�lh�"((�x�i�e�i�h�*�	��~��Az�bwr��i� �K"gä$�r�t����tե������h�D�Q�M� ��D�Q.��G��D>�?}�8���W�2k-M���IC�H`���¬��$����!�w޻��`�a.Æh2��$��`�5Q�F�J����ѲyS�l���v7�tw�5�^g�#Q���((����O�YiE�HÏ2�0B��F	�e$IĒ�i(Dj\��(��,�H ш�[�]>�4�h77��}6G�̛K61��Ve��s��Ph��a������u�q��2m�6������	aJ�Q((�cA;ay�o��-|�����A�0R`L	�]���CC��BC�u�����@ŃH�\�G4�`xh@�_��H[��H�1
���(�e�!�(6�O)6�/<6d��w��w����"l�0��P�شWdC�a�q�
��z9�ykh �/B �C�֡�h]h c��@�uh Z��uh �:4M������F[�cC���@�JlH������v�\��gNYm�[�a>��n����L��.�8��6l�V��}$Mx�o��-|߱��D���Kp���<8 A�,6D�6Q�>Һ؀��Ul���"��K$�ul��Ul��.6D�*6$ņ�)ņ��ǆLj�׺k��7�n"6�o��1�un���S]ð�N�v��.m�W�x�[�C�;DX�H[�H[$�up��Up��.8 V�!�V�!Һ5D���C�������?���nfT;e���3���6�-�0'gz��Pb�&�XEd�W��bÂC�a���X��b�w~���c����H�&mQ_���� �MOA�V��T3+D���!Q1�RF"�`#��D̺�1T��"�o�D�{��!Y5	!	+SDH4�`fW��m�A���H��]�'��s6+��*��L	$Jt�̬軤&lb���X��!A
�9#�#�zCnS��8~=퓪Y���Y��(ќ2i�D��^���
ȭm3G��LǥiVnr7h���D�H~�=�utE��g��X���lA�b�2T��AB4�Fi�64)��Yt4��Y#�A����3�8�$E�B�9.#�n^��rR)\o�>G��"�Z*of��,9(������<s+�Rx�4�KE3�3Pb�Z��zi�5J Nr��Ik��1�1��A�F���h�.0(ޙ�Ę� Bt��G�Ea*l���TlY�bƠ�k!J�-��KU���]���bHWS���-�JKJ[<�g��2��θs#mzꌸ�����K��x��+�ǋ�zE4g8bu��w��v�A�	$P�.�;.�e���z�쭓�x��4d��?l��k-r����o��|A��^����P<�~	^���$*���8�@�L��N���:Vg�"-��/�,���j +���p]뱰C��%�Xl��K��7x�.T��x�|�~���j[���V=���}�Ac*��23py���;S������΀�m����w�X�>^ax�UA�ˬ��ؐ�^�I
`�ܛ'y ���̢M�\��7�JxtTZ���;����T���[B�d�i
�B�~���i�X��?i�핹�����?�#�q���ץk~��9�Ciȣ��N��(�fq�6�|�z�Ũ��G��-qM��6��@5�V�"(ٶ�1m��Z?s��V��a��P4� ��T� !\�h��x`���OY?��p��+Źi��\I�����y����C������mh)>��술�G��qo����X�۽D8�D���s�����5����xl��X�t�����1F<T-���C�(��&�AM��3`�R)�#��rs�M)C��~�*���IM*��j�n<
�a�&h� ��^������'��to�Q[c�&�I��2�SS�[J����dQ��!��Z��\(a�-Y1��!���&�fP�E%�#��V�uh�ض:j&�
t&��s&��m�y����me���*e���.i��o��NG�˂4DށZ���@����4O�+8GڲޜI���Z6��f.K�c��ٻi�{J_nVֺ�C��V�(53H)5+4�k8��-�ps�"X^d��nBVb"�wZ��Px���x����Z�-�.�E_&r-3�j9���&^VFZ������u�dA3Y��P��,+#E�r�ii�7*�ו+�W�[�<cQ-��ڒ��=���y�K���+�9�R$/�5Fِi*Gg�hё�꒔|�	���ÿ׉�Cz1_�k��.�|��8��i���*=�TAܖ��Pխr��z�&��<9n�N���K��q�/Y��� 6o�c2����h��S{��������:��;`U�� ߧl���9���#�\�8��d/��r_w VY�84E-&?����P�'�Jo&,y�4�3!�����s��
2�Oy������>@��NE�t{�����x�$>�0�Y�I)� �s4:gj�3�U�'N2�̡11z�}��F�RV#�ƍ�Ř[�|_]l���;CY����xJ��gyD�S#�Szv~w>�i08M�W@\siL�fc5.;��qi�^�KW)�K`.Ͳ��3��:�i�G`R����S�2���6�h�dR���հ�隃ZpE�V���޾�R�s��,�����[�⚇i�~/�;���F凔!x��˓�w�,(K�S�;��r�=���-�J��80;u�K�6�b8iL>���3ҝԯ`�7)����Z���LU!��=��Gg�[�W���`A/���Z���Rn��j��<���Y!Eq&����5��x]�.�'��J�)uܻ�ۤy��.�� G�z��n��e���.�� {��n���u�}ʺ��>�?ޟ����_Y����qgB�le�&��˺��>@]��x��`^A~Ҥ|��.��r��{y���fX�ݑs�����%�a� ^�b�I�*K�L�{yɮZ�	s�Z.ϩ���ړ�sK��]�цj�l�k8��C��%��L�'z�0<���
���^>�o0fW������u�5���
�/X=fZ�e\uw�s?�d����&<����i?L��8eQ��z��� !�*U]��n�g:�S�Z�N��e�epx/g4)O�<�6�+�6���#��r��D�b
��U1�=�?��4)O)I��$� �ρ���v�E�z�s��;��wW�~����?���ͿgC�Y� :t[��-n'��;i�ĕ:<�̺����	��D��uu����� ��h���Y
:\��C�;��T�ٯ�E�n��rEj�~��g�6���Aё�'9�m\��睋�v�l�u|l��d(��-V�H7�I�7�ް�|�1��r=Nic��g$��ߘ�k7�B���k�G]�v�wE�-�N����tF�ٵ?��=����7�vd�û����oj�u�p_yݑ���cQd�7�0��m�At�]1-�&;�~;r����a4������X:�	��<�d��롸f ���,I�.n�c|x��)S�	����+8����Ǐ�v�%�=��C�|:;�W�����{���;��C��0b>D����`ۨ-V~��SL��O<^aɐ��
�cJ`���=񵍨�6/���kq��pC���D��c89��Xc>�>i�oO��g��n��� Ӱ��'7�&�{R�E�Q
?��Ws����მ@u�����#o0�q9��8�?�j�1T�qyt�t�aK��p8�S�-=�9�m_�ϓ�q����̔�l��Yص�䎜�4<�jW���ŰY��x��7�a��	f����xֹ?ϱ����}dh��K���� ���#�,��)�s`r���OL�Y&��o���U��HN���u�,��r�>d�%ս�q �4&8���o���_-��
�������Bi���
�
θ5^�Quӧ8���u(� ��3/�^
��ץ��=[�Ho[�Mi6Qd�:��~f�j:m��Ccy���.��1Tb�#�=���AGC�v��&�:�^����.�ΓO:'�����i��A:+�(����N����q}�_����t���y�0�<
endstream
endobj
27 0 obj
<</Filter /FlateDecode
/Length 3409>> stream
x��\�n�}߯�� ��$��sb� %v���?�S}��Y.w�ʒMJg�LwW��LwuS���|-
�Y�����u�i�����7.��z��_�}��_����U<k�'4����wK����ӷ�������b����Pw?Dѣ����x���[���tT$ԋ�kL������O��*e�ߖ��=�����I[�m�X�8 �
�.��u� |m��j����F�($�a;��r��V��&[:����$�InI`�	�����+��n+��26�Q������?���k�/�hb�xx��~能֮�A4D�;1�Z�Z����rTՁ�ѕ���A�a���R\~j�#?ҵ��KXH�����B֥@X���ǔC���q� Jof�֗�9#\*�AQ��L�5��VSMFa��%��fM�)��reۓ���'�]L#�oW�N!���>��j7�$ xe�莰�C���!�����0o�%T!,�äs�yE�k'�!L'��Y�C��&�����K�`>��#����iv<��z�p_OHЭ�*�K��u�`Cq�p�m�"��Qe�1I���s� Dm<�C���Z���`9�~*�i���Ix�xXx��T��^x�����#�\���0AS��Q�We܇ڸb��[D�rl:���BZ�_J���X
��-�傷\�g���0Ch���AJʍ���&9�t��&�Γ�OgɁ �����7%�Γa��@b��ɁP�+sC�Jn�W-7�Sn���ޛp�6��|��"@��"�5q�@��j��("ػ�Z2 ���P�.3��P0P����f��:4�S�Mf(.Ô��Mf(�&3ָ̪ۦ���P���Z��ڵL�Yv��L��b�ʰK�G 0=/L#G��c�-á�䰾a�����[�㦁���0��O�3��07���Z�x�[�^m�Z兰�4\��5��w���Z<@y�?���Psqqu�k̹t
 �C,���4yr4j(��[c;"3f�S�� �KV^��
d�QJa�s�,/0�c�K`U�ҴA���r+�Mv�! ����,�@�P��rMp�i�6��MS��������P����S*3�b6�$[T�Ϧ��y���QT�再ŝ�j5�q�[)h�PPIgrV$�a$�Af�1B#�jH�v^�����a�S=]��Ns���͋"b�¥�Et���?�Ml"��F�hp�Cau�Ұ8T.m;V�y<���)(_z�����R��v����%W�{L���A2�W]L���bG�����2��&��`-�~�膊*��Y�?�7i�3#��)a�)K��L��V��^�rw��񍌯F�zu��uoa�ܷ·@�:E�V�<�|�v�V�� �߉6��ʶk�>��܇�&�vw�9�|���Q���>�&Kh�����wP}�c�L��M��'Z!����d+{�����W,�3l\�#��3*P�Q�nCc�1�Bc�ά�Y��[_��`�(�VnY�],a��y�~t������	�=�m�ظ	����=��*��������U;eD�}�-W�pKF�o���ܗR��/9�jo(g4e !�.N��{��Pݰ+�9�W�d�L/I!��_Q�X�n�V�]����bJ�I�������S�PfVŮڱAe3ɓ�ݒ^1W�35y9NF�/�i'?+�<dsl��\���/8�g�sW�0CLY;��ǆN�Cݧ��M�x׌�t���)������������=f*5����5�KȽ,��t��9Ll��=����/����Q�Y��}�N)��E��X�_7;_a���n����}�m�ˬ#s���v���������X�|�~��2����.��|���s`y�Y�����n��֕�^��F=��MQ�`�F�1��6e͇����ˤ�K!�����#h�;duMVo�x�=ʖ�`}�*\��fr0�q�Nl����o�Ch��.�h��qY�w��X{�!L�aL2��nl��MQ_���xg$��3[)�D�א�Cf!�(Ŝ�#τ�E!2�6w5�(~J��s.�oKk�?���w���p�w2u:�~j�R��o�6�7Cy����S���J�ڵ��>.�� -�%����NK�4U�Ea�"Y坛
�����䵬`�N5��*� e{�� ̃��H�YxQ�f5'�"�ك���X�"XyO�Mk��g{��;��r6PupFT�}���rig�sm�y�\#f~�5�Ga�Iyؼ,����>�E�l��V�T�F�h&A��l�� .�Z��h�KN-�e�IV�-��aSҶ��Le�L��M��ޒ�b .*O�pZ�ͥj�!��;��=X��n�~��:Q��1u�&0�孛�ܾ�JN�}9eU��t*
6׸$+ܢe���v�&"K/骝{��V�:}�J�g�on�o�V{&����(q@�/��-���R�����@o�퉍��m��P�ے]� ɹm��(k�y�;��i�y��?Jy��S��۱W������n����s[�>�mm�|��u%hz:V�k�[}�(�a.�HH�'���ڮ��v-i_8B{:��o�[�`m��E����=>vג$��%n�۶Z#o���E�8m�~5/.L��6C�z~�{��_�ѲZ%�M���&ށ�E�KnsU�����	�ۚ/%�*�r3� �J�GI�����tq�n���Z?}��k���~�߫�-��,-=�K�9c��r�4�%ʘ�)�I�:�v)�yw�2%ŵ]��R��M���v�y~�sc��O����VO�Wmt��M�w,�X����/\�i�*M�E�;HV}�o� �Ol|�����X��	�{� x�x>�]�r�3�!l��-������ݚj����;>m�SۇÜ�_�,�� /��ӻS\+{&c]�hmd�}��&?����l0�o�B����}����o��%H��,���P�=���e�"�?�7�^3�T�=���������CR���z���r�8���ֈz[y�̋Y�x6)�5��.�{��4NTE�QC�@_��2uO����������m�%�-��ީcD��	L�	9¾�t~B�]��×�I����ߖ��1�����c.-ɖ�&�����rs�q��~�[�B<��6��y�?v�+�tJ{���=!��>2���8��bWHzl��o��Ud�]�{���>$}��G�[�Ub�]�a�Ο/�z:�MZ�|/R�Ü>�Q95�	��IKw���CWn1>q�~�/�E�}���i~����[O�w�T&��!�+��Ҟ���m�S�}G2j��M?U�6:E���p��K}��Gm4�Y��|OR0�UV�lW�C�Y�����-9ސG,�ƺR6�����V[�h
endstream
endobj
29 0 obj
<</Filter /FlateDecode
/Length 4525>> stream
x��]Y���~ׯ�s �}@�;��/�����;�HU�QER��Qk����H��]wu��ŝ���gR���Y�MN�Y眦9�v�ύKj�^��������W�ݬ\��w0PO��o�O���?����N?����NZ���D��K�����ӷ�n��ן`"�PO6�1i�'c���������������� 0i�5	�����?����2$w��I_��g�6���\�5�"��b-�v�Zڮ��+�87�M	4^�~�|qV�be�ܭ�UWh�3
�q�y��_��o'�����t�3\�A�ƃ��� 3����	�Wb�7�{������؀߻Uq�9G�J��mA�è�O))7�R^G�~���0!`��4���:�d]
���L�L9��G�tԁf3s��F�AS ����X7�V^8���P�j���h#X�`I�r�j֤\��2Q6�W��^	������B���Տ��c{�ofL�+^�̳!�}���Y�l��N�����GȁX1���!g���Pb:�$��U9䅪u6x#�B�α���-c���N|1(��xR�@N�'t��T�'�t�������Bp��e�j+*4`�L�I�4�R��0���fB���^ŀ��E���^���-���<<%��$��lv��°K�{ �z8^X�YR��lU� ����aBHS��@{M)�9�3|���4��~��.��M��@�	�,� n�Z���Yi@�^�8-��N��uZ Ь�a��@�&-
�z�
�y��*y���y�B���t�Ka�ϝE��] BfJ];q]�"4Y�"��UD�7��\�{2�V���ub l�[' �:1�J�m�n�Z%¬J��@�*1�&zSC}-C��݇�dG���%���]�p)uVG��CKꛃ�-ñ�举�>���y�3��n���~=i�_�a�9��+L~�S��x�Cԃb�M�Y�U�Y����Y�C (XG�^��Ah��z�)�N|��ٸ��ø� ���>�9f��h����AN  �RV^�7�T^�e��b�
 ���Vv����]�oK����81!���T*	� s6ZI+���Y;��kr���U#+jn�� ���G�=�
�N��Vf��X�3ބn��fn�����h�B!�G[�pm�U	�8�LV2��(2P�g�����8K���;�B��h|��M*�B�GV֖��@K���YE��"���r!ˀj�L��S�Lpe"�<��B3
��V0
����v��x<�F�*�81!��g������V�*� �9r�&&`�3��i
�X��h��U��Z��5�n7�M��`[xMo�I��n؍���T���˦%��P���������]�T���������A���� ���炁
�
����|�c��s�2^CcC�ԗ�O=;T(�?�o;�ۗ[�a�'�!9WH�~�B�Wj�$�����P�6�ʢE$��;�.��5M�Ģ�f���@��e����-�ɖU����Z~���c}���^EN	�~���^��;m+�S��	��^�{(�����׊ي�0��L����q��B!x)du�湪'�o�C�wX� �v��#�D�|�-�j�m�g%r����qeu���P�k���*�`Q�i(_��[�א�
EDP
S9�5粫���ћ�g�N���� �k�B��i�jӆJ��>Z�dN\�(gەg�2�e�v�w��_�
�T�ubn�p�0��BD�.�=7b݀�)��w��C����<������_�=k���%�j���H����I��l/J�P�j@pwH�1]�ist��n�^��@��YA�i_��{��d�dj����%=�CGڋ��(R"���\~Hi���-(��u���M��w�l��zO���Z�~��}�H5Q�"��;&�w�f/���͞x����X�k$sxL�x��3ìG7e.`�0�CWx��\��ϵ:�kBjq�dE%�����󗪬P�_���ضڧ��k�Q)����W�M�S��7���x��EБ�eO��>�Pc}��ɋ���i%���q�^c�PZ���0�sT\�9�򶵡��	�-�g�����M����Lܬg��Z?d$���� ��}�T�E��F��"N�8�/tT�1�4���k��T5m���8�9wSQ�C�x�u��9��1��7��>ŏ�\���Õb���qͥ�*Ҡ��2 �Q�ָ����P�J�U�u���־>��r�@��ϕ���ŵuS����.���V
�w�:_�3��J����������5x%�����t�=q����@�p<��8��s_��n�%��-�C��C����b��f-����C����`-v����ӥ�y��M[�Q�?P�L���	N��L���(�ҡٖ�V�h�zul+��w@b�㦕r�Fyľ��	��|e�4V�
U��e�*w�R
�8�I����;*)ĵ�2eg���
���k��b��Y�t��,	<�+�W�Lk�W���ś�=��m�#�̏l���v`:�r�)%�����)����;><����-��?W�ن������9y���`_l�a��xH�:�ݹ��#��'i�p��I9{+�|�O��+G�J۲�ï){�#|n{�3_�c���U�u�URYp:�]�T�-��I�������!l��+��$\��B�ᵜ�YKaQ֯���2٭e�NU6Y�G9��Y�@��Y�ؓ�j)b�D�^��V!�4j8� f�[�S�oY����a������j@��OUp�6x���<�^��2P�N|��!�l��}�n�}g��q���>�=�S0j�O%�l�g?�Oa���@=�80�i�6eȶ�?Y�2��>k('�te� �]�.��T5��Y�����daۼ]N�(>�����,����\�!��2lm��C�Z��KBB�!��w� ��22��ݤ+J�(�zO%ǈS���T�q��[ϕ_k�R&0�5"[���=��f�ۣm���e7]��r?�h����$"U?5�|Ğg5z!ܗf���{�֏��N�Z��V�����K1V����=�ȅ�@�,�� �XӢ��8;�D'@���~����s�Z�pf��� uH�ouP�ou�����IIn����͍W,�Īd�VW�����$ڶ ��(��L���PD�a��(ڶ*�l��l���l��ƒ��U�s�>Kx�w�m[֞i�28oq�h!�l�����c}�� [� �0O4�c009��=G��Z��Z<�w;	�-j�Lo�l�F+!^���z�mZ]c�M���ǔD�`���?�QcԲOPj���O���~Ŋ�l��l���� �D�Ԃ�nS���.��s��6�|�8�;���6��6���h����w�wl)R��8I4�ѭ(�u��W���˟{��ء�Ea��A�����΀���$O篅ޯ�P ���H3�"؍R��M�>�ץ{�4���*v��d�\�;��\ds	V�H����A���^�ߝk�VA��"m�j^U?-�G��#le�;se�F���ޫA����ۮ���}���iv�N���:a����),� '�n���q�/

�]P\`���p&d[�E[	6�l#*��ڗ��D�Z�/h��V�S+9��ٟq��zT�f�iδv�7����q�,T�>�u�g���U,���߻���x�u,�8��]��^�#ʪd;*�J��U��5)hh�j�2��_�dջ?������z%+ѝ9�^�k5�^y$�^d�+Y�B���p�n�zH͒7�\����+��+��re�f�+Y��+�Ü˕��*W$�iX�"Y[��Ӡretq�r��q労��E(L���?˕�+7=L!+�8�G�+<���r�q�/�~���r� ��A'�M�m�}��ʇ��߆����cD�J��0�!]�T�l�fD���T�8�V��zŖ|W��ם%�J��
�r��K]���,�Q����j���ҟ��Y�<�dɷ4�f-�(󀒅��#�%��%�]�\`�2�c���1UK���`K����vX�/XJY��<A����a.vX��;j�E�}���wX˃wX��i���;,W9��2Ԫ0]r�g�2�\�7=�-k���tT���#�AY�<��E��t"�� c��8��99U�:5�D��g�pw�?Ua�R��>���J�8��@�Jl���tN���jDt�6�@�@����:���m �L]����m��@�48��6�U�n	��8��m��_�T �gj��������M�-�-���n%�u������2ԈE5�{+��K9�cI�F̠����ޘe�:֏����x`�P\1�_ד�e	����P��Ϗ��g��l��nz�n6�ɻg~���
g��P�Q�XY�L���ܿ�ri����o�ç��G�]�S��LX���,�sD��i��^{�ײ�Ok�/����
endstream
endobj
31 0 obj
<</Filter /FlateDecode
/Length 4321>> stream
x��\Yo�~ׯ�� ��� � ��}Nb ?��n������UŞ��-Q
ض��&���x4�v�c��	���ξ#�(c��ow���ue�شq��w���+��.��s�7h(7��������_�~�Io��;��ޤT
��9Qޚ?���_�~�l��}�:J�M������������Oۗ�9����T8̑��7���}H��ln��N��\�+<�\�#u`ry�Q��&GsH}$�I���X�}!����ej-�Qܣ����P\�9�����;)����٤�;����������zG`!���5�A��~}�
�D/2���+��]�%v���}+���3~6�a�*F�(lx�i�e&i�\��&�ھb� �t�a��i�1F�L2�Bb_)]h��`c	W]n뱍����Ll�0�*�LsL���/w��hx���Ph
���;}��_vR�;��Бu��h��c�
8iV��
Ҽ��u:;4�P�0� M���Et��F;��W�g�yH*��m�ן���@@ȍu�4���ܑ6���,f��O'�ƴA�s��]�Z�P�
m̐H��79Ҵ�qsR���9Ń��J�0~I������E����uɀƘ3H61	�U�p�5�B3��fFZ��,�gX�6R\��'f������C�O�D���y�{��=13(��ԁ���$̟b��vt��i�x�A&
#��T�akc(=d�q�V�^&*-,OHu�����AZ�"2х��L�8/#0"f��1�����J#,�>	�B8��"�iEA�����!3*E,�?�6s%�i���5gd@�(Ǭ����^$Fk����pL�x�����]�@rܸU�;�-|�$^d�L>��B,�#+ɣ~�كn��j�r28b��ڨ �:��f%T͞<���y�67�ne9��l�{���4�'��I�ש�Am�de��ؐ����i/F��L��#`:���� �}��?
~,�H!�n���O�n�^��
M�����O Z���n]����-<�=�gB���(����؇Wmm���w%��v�JH��!����J7D�K�`�� M� ��`����0����A�S�#"�KpZH�w#�@! ,&�4L���>"\��Y���*/}�e|.J����	D$;�$f �t�j�ԺR��{b܃���� \w���i����$:��HLE�ͮ}j\mQIh�f�JD�5�V"sC��Ƥa�mr34�� ����'5��\D,6p1�ӄ 1] t������£(F��p�0�a�����BK���!����HT��@����MD44��ٚDEdyH�A�^y�Cv|�w;Dr��Q�۬TLn���&S��<3Dj\��f�w�G�0�Ȩ\��QV3q�jYs�Ep�Ұ i;�*����j�BKQҬֈ O3/k]���4ou�4�2�9R�����:����z��c�=�8��0 s��S���nmIØ~!u���~���Q-� �)i�{$��?�� �����X��$���2���P�[��hX��{q��R���Ŭ�p�5�i��+��+�e����`���[M�ͫ7[c)]�R���*�iw���!�R�)F��&l,�ձںO�$gQM�/q6??����6,/��q��⣝M,�;��~g3��%ҭ�`t��N6İfS��%�G������}O]���=u�f`�@���:k5�l>�ٍe9T��٭k���&ɗ;�$?�lj՜�[����Q���.͑6*���!(�g�:q���1Y�4I��Vz�m0� ���������'��� '�ê��سx�#����=�(R�����x���"�@�)��ҭ�P�=ĺ7iq?�s��`��ܣ�$�X�o���&^��}%�
(�v�$$.��Xa��豂Xʇ�cu-�;�L��c���X�ZM9[�ڗ���KT�>����;��᛭Nka�#=X5������U���ֺ�a/vޜ����z�ۏ)������ n�P]-z,�d(2sL��t�ʊ�\Y�W���(^I�5E#�9_M�K�Î<�s��i�cs2^�ڰt_<�p���1�x�x�m7�v��c��ʛC�~E�:����6�ǂx=�\.64'�˰��'���!g���8d��nK0Y�H[0��Y�8�	d�\�#r7��q�i^3go[���������l�K���| }��1�8'`|y:� �i�"%p��V'1�Ե��v���OL�%���ϳ>&���[�8�˗���,~����}�
�9��~�3��-⳽V&�l�����M�_����Ti�\�~}xm��[���~=.�}&���g-��oo�*�(�fbk��h�bN;~ȹ
іw �)+��҈����yi����h�%��e#q��m:�ԋ6g���3ŏ4j�xb�dcF��F���q��X�(�ù�����lsJ[�6X0^��[����ZT�3��h�޺�3l+!Z 9��OS�i�����xZ-��Ypʏ�=r�b8~8����IOpuɑl\�O,���\w�"}�Ԅ)tdK�<ԝ�^3z���P&���r��Z�W�5TuW?Zc�$��a�l�-��mé�T��R�䔺E�Ҧ�uMr�5)�N�ȑH,��&����T�\��&�a��}lJu3�<?b����龬���l�|���.�׾x#�:��y$�n�i�V�$���Ū�ycO.;�6R9��a�mQ��U�]8�a-
w��[�^XiWt��]�FQ��P��)j�
w�l�7��B`*h��~�G��J��j*R�\�kl_�7FF/�D�4�2l#��$ 0[�� ��,a��'�or4KH=�F�'c؂����2�y9��yd"��dUfn�ʝ��0�|�dB�?L�'���ی՜Ԇ5�E�iH�چ	.����>��a� �Q_o��R�	.��:jq��X�0�e�ܿØ�d�FBøTwygzx�5��>������Љ�4�*:�>_�O�����ow�B���9	#nQ�6-��ǽ��{;~��}�68��2����|P�A���8gp8U����	�)�@�#v���З:B�g���G����f�7[�d:F�Ue����ҕi!h����a~�S�@_��qd��
�T�`D�Ô��X|�.FF/�F�/�|��P�
�a���Ld�WCVx�]>��n#-�,�u�y8��x��Wԃ�\4��SQ#����s���<:5���F���
xF򎛜x�Б&]��NN���G��G�g�a>�GY�e�x��{�(xE�&y�� �8�`��#��D}�c�bl�Q<�w:�^�{at萡"�¡��=�!Lƞ��ʢ�R�W�w��̇�dj��E?s�_���E-ěRL���Sa H]���2��8s�s�i��;�������iK�w,�	|�t~�,Ϋ=7Ⱥ�,	��c�y��Ώ��ئ�ȕ���ԡ�-�WL��M�OTt5��������¤�o[W$:�Hd>�/*�;G�4+�����1wu#���;��(]q�V�[��:4��y�p�1���)&��ajGy��<���AƉ��\r���W,��0��'�Ȟ���p!=j%�G�f��	ɟ��:k�/���v^��&��z�aY��<�+��7�r:�S��82W��=���P��]k�|������Ձ��0ZD^.�O�=/+��E����\rNI^iX0��3���
\%vE�*�Rk<X�5&+���fEܚ~���X��L����J��*��� ���Bu�v�p��I#%+�h��v����p��k�Qk�q!oqyȯ$9��4����"p����b��"UcD�(����讬Xj^9^�k�+Vh��+g[Q1V�,�k�BZkL�Ԉ�\��Pq6����zT�ځ��k�%��6�B�p@�qY�p��$ԗ�3ʧ�.��R:�J���J�5"/�ZW0&�W�8ͫLp����%v�[%�`�pg���A�~5Cю��8��b%�x�+O�J��<��ϣU{�՗Q��?Y�����8
%:;�ڎ�ю���������j'�G�r
�����d�ٕ'���u��.E;J{k�m}�c�7��P�z�NAF���U��T�X�/����{;M�ɋ���-/"c���
 uR5}�]S�߆����Ɨ�9�����4skǷ�����s�Y�7�[	�N̛�x��w��&�V�%S�FE��itCh9�~����xE���L�˗�RX �Ыѝp�S?�
endstream
endobj
33 0 obj
<</Filter /FlateDecode
/Length 4050>> stream
x��]ێ�}���� j�~� ֮������A�2`���T�I�a��v�f4���l���&YU��x�����\�L�����29=g�s�>}>�~�ύKj�^�������7�ݬ���+j�'���������~��N�������6���� �o]�Э�N?|tS��~����z�q�I?;=}>�Y)��2=����L������� �rZ�v�/Mr��釧��f�S�uXbV�l�X��m�6��k���$7IO�,^��H�^nM,Kke���W/c�Aa�Z�N�_���'�����t�3ݐ� �ɑ��s��ę�̎�-��;�s�3���[
��Z�zΑ�����>��iL�c�>�m�����2$�Pq��uVW̺X����7*��O�<���!�u�o͙B�b.�<��ch���^�ǡ6�,h�5�HlU0iO}њ�+R*�I�}l�z6;���EL�ho?�B��꙯fk���	^ٌ}2�=[g?�4�`�CY����V�cr&�1ڡ���$4*cV��3�l��* q�S��K���'��6���g�ˣf�U^� z�)Ơ'�#0��j�f0�V�k�[Ł�JK[a�ag��V#���;m-���~�|B�i��g�~�A��./�6� �C�t+aPu{b���1V;MԝP��N������?��}I8De����4ޒ�[Ҁ���k��n�=d�g�@��Y$�b�!�0f�
�`P9��"��1��,>Fd�޹1�[��Y���ØE)���$��E
�d��m�"�՘E����>㣿wY1(�V@` �n,��nT`�?�z�
�B��f]�;ĘE2[t�E$��Y�A��*�dc�Y��Ma�ޯ�H6���C&aL�i<�I�d��L�W=�,c&i��w�~�A��./�w�L 1ӭ����q`�v�0�;���Z��%����<ޒ&�W/E���l�&$�*�d^Q��A2�N$���I�a�Nۤ�b�Nr�32�B�?f�d�7٤�K6Y޶l�\��d��l}~,�>�d��*5đ�?�\3g3����C�7����(����ҳIq�!�0��&\oh
���hڧ�AԐM
譶h�n74�u6)�:�Ъ��&^g�l٤\�lR/�l�o�~�Q�Z�W���q�&��kAl�]!�Y��[��\p�R�-y�%����<����u��1=���r�s�����;�ά�q�s��VD"$�2�H`V:1�&4��KjE4�w�1K:yb��a���$��TN�g�����_:��E�
.9"�9fZ�̄�0{vA yXV#�k�*����d_�Q�j>���� 6Ӕ*�|a;e�)e0��������	��U	�#�Hm	cB*�e��7;�L6�C�%Db	頂�({���Y����rz(���O�wV��~��I9
>���)298V��6��O�9z�l��,��w<�O�����]�@C1��u���W���Bn��a��H�%)7ta"��F�`��S��2|N�t0|�	��`D˔*v|>Ig��J�u,���C� �$Օ�/E�D��7l��tm	�UI.�2 r"���:Lru�c���8��9GЗ�����9������gk^�����JE_S_n��;��(�#���4{OS0%|�_�K�k�}S�R�����}S����2J9G����@�y��_��=.׎���K<�C?����=�o�� �~���7��u�dt�e^u6���_��d
���,������䡊k*��Y5��k�uU5-*��]5�nZ�)���/�ex
7�(&�oS--b�ᣈ�����q�����i�p�� �Î�-MI�j�vlv[7j����}}͕7&��讅�X?ö��G0�K���<�~���Ê�Z��S!���㕐�dv�B�P�o�Ei���אt�;tQr�|�E1����V��MՔk?��y|:4>���-�4�
��,a4o���o�����nѲcy�E�yGK����!jx�Y�� ��Q��S�{��J{\��!!o��4-\���8�R���4o�٥Us;$֦�4��������}�q�2��~��1�������h�[��A�k�hhv�����GX">��<�;q���]P�LR��l"�+Ƹ4;Fe���$�H_g��῱Ib����C�W�;��tk�ky��6z!�ob����1�޺��9�kՎ����wN5w�)Zk��*[�`�ݰ�:�>/��S�~�]��zW�e9]v95��]�_�lzZJu	�VMz{_[��Ģ^��L.@�e����%h[��/	�{<�1ǔȡB2�"ǧ��6��*l�FEd��29�6��ی7`�����מ6��RڵXʐJ�������e�u[B<����B(.tm�D��y��=�?��c�͍3�P�f�̇\Q'��H2
�����X� J2�P0(I�P�h���
�M�<�z�c�0K9��`]$�/��P� ��r��s�u������A�yHk!DF�P�Y$o�xӶ�a(⫣������̓b)��so�"?%g�&Ќ�bHX� ��ĂqP� ��~�	9�k c���:&5�A.�?�R� m��a�r$p�"V:?s@��t����\���s�*uBI���9�b)}4�T,5�b�Z7F`��� N�G�i
n����6����*d���k�,e���>W=n�����c�:O��vf���Q�]�y�����b��n��z6z�u����_��`��e���3��ZV���{�����#�AU>�z���-��V�vF���h��f��Q�;Q!#��K�^�82e}�*1�b�s��^R�j�ȼ�L��Y՝'�{"�e�	͎gܽ��#)�������J����Nvˁ?�Q�_�.7wEN� �wG�Xt�"5�yk�]Z#/�m�Ghv�Vw�D� ���諝���GNV�b��n~ª��p��f��1"���ȯX.����OoRs򹜄����<�U?�-�q���[��A}����9����_�G'�#j��|�}�j�.~i+����3�|��6�i��������(	�Ʒ����gP{e�g]�]o�Q(5��̭���ߖg�dtC�������n}�" ������#��"��o����+�0��*����6_z���%z��A������{�9�H=���mvy�����/�ʳ3�7��1��*d��߷��ݳT;� kL#G�_�)eXNun�'�7$�g���f�u[~7��ܿu�Bls��^��r��Z������Q��,�ZR�TG��jl/�@1���1`m��CI���9�Ͽ%c�ʪ!�f���*a�����j����A,�vJ�}(^�4P��rC9��7`��#`7�� �"I+��T��L�b1�0KZ���J(�3>EV�`S+�bj��*��E�By�W�\��x϶�jUrձ�"f� -�h��PI%��s(�Ѻ�z4C�@��(���A�� ,�v��Xʏ2�*Q)i��R���Fj{Z�n1,���sy���B}˓�M�2?�Z��IN(-��|a�N3D��n�A��J�F љ�霂��%M���|��)�H��@��?.yZ�;�H��D���l;*�o.�Ը���]�55�t���OT,�_���RU�������{�c�:�]�M�<����l�b�c$�� �ݑ�EM{(���d��P��	v����E?O�*�:G�������US��t��5�j?OK��-%A�[O� �5I����o)	�8�Eq�I���I��&	f�O����_ćU����?b��ڹ�t�骂�6��3��p�9���'1rs
�?������aڌ)K�@+�7�-�������$�o��66��=�f�m�.{+�ՠ>;K;HM����J�p�*'#r���S�*�O���r_M*|����W��:ўC�֦`�URT�8J}� Q.�9�#û��\�芴��}�N���
��¾�E���{�%�C��/Y�B
endstream
endobj
35 0 obj
<</Filter /FlateDecode
/Length 6630>> stream
x��][�$�q~?�b����H�]?'����#v�?�*^���p�9ӫ��Ƕ���t�Ūb5���ܔ��?7����.��[�1��/������L7mE������_n�l���>��_������?�����ҷ��_*�G}�R),�/	xk��������[���((I(o�o>HeoJ�~���_����n?����_7 T�f�x�H@��!e46?	0���?���)<�\�}%jW�xǾ)�#{uH�&w�$WA�h�=H`��4X�=-�^ܽ����h��0~/�����m�cnU�,���vsPFsc��Ka�{����64ܡC+�&z�=z������F�Pb�:��_녆���{d@�G*������&8]�nF�~�ǃ�ҥ}ؼ�o�:Q��3P��ί�� �2���?����$��;0HВRP�V!Ѕ`�y�E��� 4��PA���/o.z�zǫM�0�fD�:�2��9���"4ũh��Z��B�;�]� A�BIÕ��*p�"�Et��?�F;���65̦�U��ǪC����Au�/Agb/��ZY�+��v��x��`�N	z�}�bU�q���U�����,��>?۬���6[�5����fǫ�8�.�߸��۹gQ����cI^���&�X�Y_!-�NE�������U2��dP~y����Q��N��4^A�4^A��?/�9ʸ���oQ�갋"���(��E���n�"�Q�1�Xm�(��Et!�� wE��H�Y�H��HƸ_R�܇Y���IV�)�U�1��F�b����;p�?��d*�Mk�@��(��G��E��cq:�Q�!� x'�8�(�cAP���"Q$�E���H��H��{�˽���=��e��m��5����T�O����y_%3�NMe1`i��
���
�����#��(�xiwQ�K3DĆ(��E��CAl�"�Q�K5F�(���(��E��H�Y�H��HƸ_R�܇Y���IV�)�U�1��F�b����;p�?��d*�Mk�@��(��G@�(��E�H�"�(���RwJ@�N	I�M�p=F�L`6ڸ.�$��H(��颏"�v�YT.��,��G���6��w �t�WHK�S�>y�c��}���;5�ŀ���+h���+h���sC4?E� ��Ha�"�Q�1����(��ETZ�>����1�G��}A�w����&0G���F�|�G��u~���E�\�EH֮S�Vu�)��lUY�WV�v8�_����
Ŧ7@�-�`q}d�"Q�1�D/�(��E�EjĭZ��1� xg��EHQ�(��>��۹gQ���wJ�2�.�F� �鬯��x�"}���T��*��wj2(�KC�W�x�W�x���
��(��t}Ģ6##	uva$������a`��fq$a��.�$.�)�z��$p?�I�8�I�~
��G��G�UG
�<��ɼ���<��ʺEk�B\��5e�~ٔʺp5@G��X\hV-�#�I�.� �] I 8�K`��$��!�$pH8�íS+����s��Ik IW5���.���k�r;7l2t.[��w=�5�w����WU}v=0�~H���~]������7^q�7^q�ƍ� ƳHT�-�2,�&l?�I�0�tX�M�~���At\�M�F�1	�Oc2��H�Y�H���HƸ_R�܇Y���IV�)�U�1��F�b����;p�?��d*�Mk�@��(��G@�iL�Ә�@�x����m��>�x��Me&A���2	"I)��E�|�G�z;�.*�{b�a�$$/s��.��
X�!m��Ez������Y2��dX�F!���
���
<x���'\eȑ��{M�)�I��z�aQ��g�=�C���Y��IL��b��ѹ	z�T�>%2Y�v�.���W���X��+2�S	��1����<�a4Nԑ�c��|���Q����1j{,����!��T}���p�C��ʙ%�ۗ�����N�w��(1
�]�cq?MT��g�x��J3l�'B|B����G�U>o`���6��󀯇"T ;�{�5�'��7#�'���3�8%n�^�F���J��>���n��9���0hs�D�o@���9�y��ίxQ��ZFc�H5��v�m����n�dƢ��γ�0�����5��<(.�{�ِB:��T��٦-�dV�����8�:�:�!`9��-u0J��+�����������Z2<2,�:�����o�Yw���hǺ����3�������7��	Z�ï�	g��	3��-�S��'bj3 >L$��`Z-��}�.f�ˀ|<L�nД&0�)
 B�_��j�j��B4��`����0�;H���%��!b'�����K���ZƱ���l����;�a�QN0*�-���|,�������0Hw��!r�
*�����Z�*�bM��f.I�d��Y��m����)�ۖ �o�(~�0]�w�a��,�� �,��`N�����:಑�����Y�A`&����/>U����X��e �3��EB'�j�AzLyAFteô�����#e+^"�.˛U0O�O��6�г��K@�[��F�*3U�!ֈ�K,r[�x�q���8�b⒚�� �j�k���Ȟ��fE�]:!ȂL\�Ԭ�K��,����%�_Ȼ ��#;�D��I�|��^���A��Zh�a�-+X�G�k��{���宙��jm(���o7l��[��)T�.��b��bƷ6���eEh��g��{R>�Slg�<�p�p��{��R���j��ė
���\|�h�].|��*N���Q\�J����^xcq�z���c�1JN��m�b:&�M����M�����g��V̋\~��'t�OK.Ϧ��y�Gr�S��I�ү$ḏ�3�b�rS�nE�>���F8���[�N_s_����)q��}����"xUG�}���8#,�l�����i�Ɔe�1�+=dڎi���_�W��6��T����5],:�_ZYS�o�y���ӈ��Z�<�c:�X�L�X=�W�O����x�뇻��{�?�ޘ�`��5��۠����`�ӎ�6�U =#�K�Qb�+����q��b�5o�7~�KҘ�&sc�[�8F�U]�w��y4��q3��g��b��eG�l6Т��	����H)w�8��k�g43u�4�2���YG�Y�,�G5,@�eɆar����X�Z��)-������͎��{�?-��|��ߓ�yA�2�<�ֻ���g"[ϚB�~m2g��j8ӏ�MnZqJ% ��C��ûO@�Qڎ��"���~�I���� �8�O ����Uݼ2L/ِ�Ν�Z9x��1�t���l^���>�)�g܉ �33�*��̈́W��Nw�*_�L[V-��{���z��ތ/zC����x3I�絇鸢��E�%����F��R��uu��?O6]J�V�r_��з��(g�L�솯S���g(�V̋r~Q�'t�>���8����y��Dt�S���$�e���ڧ����I��zg���c�ݽ��YH��'k�T2O!]fd�u,���3���j��M��L��x*MUӻ@�h�S�!�n+?��'W9�IT0Æ�GP�	W�{�z���H��NY���~�]�����v�N��oN��͆���<}`������4�w0�P���#/���@w2@��6.���C�y��h�T_
�*��=m�����(�n1y��R��Q*D֝P�/]XǴ��4iy9=�"svb�����!����bN�KS�fD��i��Y�F���v���ѷF�c�TG�Sk'�d<{;��"�g���+���V#��0�o�3��5��CyJ��(����v:1&rq<���iv�
	����y��0���I��h�uD;=ɔO50;1Y�I����Զ�k�P�޺m�X/��Rv�٢�i��g�V��tT��b^�$;܃gh��e0dr����|;��to7��UҨ�N�F�3���Z٘����|/J��w��t�{�.h.�w
�����g��1 9$i·/G��<}P�t۞&�J���4ͮMl�'�y��|��}�;�-ʶ`*���)��/CY�#i��7�;Z@���>���g(;u�*h�/<K������-R�ʯ���[��	��g=�h�.A\�1��[i�*h��g5��Կi�3I;�Ӗ�����>�偤A�4X�I/�<���]�i�JK��U -%���Z��dꏾ����nf���Z�x-u���4%�w��>�b=�����grX������5]RX�?���ݣ�7�nb�>]'�.[,��6������]Q�1�ϙ�ʕ:�ֱ�U�
��`����Nɽ�i9���?� �p�+���eDλE��,:�-Z	�i�cݢ���#� �^vt׆ ���LFl��Fr2��6��*�GX��{��=�X�<�U!k�p1��l
?�ݱl
�.�:l�OXϲ��l�ɦ�VC3���I���Z7��H��lD4[$b�a�3��e�H�ļm�7���`�:�Slx\G��JPG�U�����FT�:�Ņi�W�qdԺF�Ŷ�FŪ�8��F��1zM�}w�N���R�hD��3~�C�-�i� N����p�>����	Cebs���|��赨�Y��S��㔾N�ij_� ��3�T�������N�����|Φu#�V��dJ����DT����On������~�vH��V�ޢ�
RB�ź��M���	[�?���/�<m���X��/���`��d���0۫5�̚�{_A�O;B⠐�O� C�P��-���	�y�I�ҏ_h4�\+t:�;omra+4~a����R;x�����g	T�'��}��*3��:R�@�lx��TqG�C����R�`��F6��&m���Asu�����]"�S<��0C�`� �	��O���,�@�ʣ���81�П�T2ư�r�ƻ�,���E��<<�Ɇ��7^fe׿�<n��.�g$�2sN%nv|�e߲.�Szw^Ōs�� ����zhֳIs�w���i�}f����r�r�=p�#s*l��?�S�v}��ռ�N���.�lޝH��tS��zc�C�xb'�}9���N�}��c��R��- �=�D¤{�?�+���=ȴ0����7hƕ[�,g�ϓ���������﹨t��VF��O<���M.ܹ�(�>A}����8�6t�l�}�?]wYn�<S~u���1��qY�|:8k�4���6�&G���=�����p���}��N��mC��Ơ�xӽ�;Y��}���&'��}�#��H���~��n1��"���j2�?7Ȟ�3�?�{`,tݖp׽R�~z��.�q���ũ�ڞ��UU��o�{��	
��<�%��aa9U遢�YN0�P'�W��&�y�L[^���f�N�3��SG�]�	/g�^��{���ӎjT?.�Zx���Nf\�����/4�,Ű�ֿ�pG��J�=�p��s&��db9��ۧ��;����T��5uH��e��� *��i�=��Γ���)��3 �TN*�].���� K<�.=���$(������)�x��<U�@��Fu�9&˥#�Y������He�=�e�{1��e��|��.c/��������2]�^�s��]�=�l@�0k1y�]Irfj�﹓��;�ܝ���+G4��=��QN<%̕C�x���t(����䩊𼽊�=z�����[����5�[�]kZK�swN�"mu�{!��%�|����t�S9Ì$��(��B>K*�̽�;*]�^{���
o��b4K6��oԆ���a9{#ѣ"�鱜���`_�o]r�0C\z�;�O�\��p������돾�X�|�(�N[��#�X3����v51��,�Iw�������	��kw�_5U���&��˓f�뀲r!W�S�c���Y߉��~xuϾ��]mh�9��[%����Ww�ύ��,����Jg���G�'����nJ-.�K��s:��"tϝ��;冮[x~��p��S1���">tp��B�w�����=7Pg� �κ�/jW�.��딬�+�5!E��s�y���&J�mʙRFJ�.��r��{�ʴ���CĴ�
1��L��<��N�V�n/ώ�V0u�Υ�����;5ZF�����������:Zb�F� �]����
����vv4���]�f�DS�:���'��ރ0���(�R	`��5�(k�0#>o�E��t�y���(z ���	�sy�Z�T\�f�&w�}k������P�����Rģ6��<`�����lG:C�@���T�t�;D� �)�뎑�O�s�[��i.H;G���ΑnMk�H+��VI[|*o\��ڰ��Aj!°����?��<��G�T����/a�'x��y�dU=��lԉB�dB3��ƍ>�q�y�N]��-.wg��T_�6�?�~��Y��f��Ƚ�e�҈����zi�$Vy?�Pע�
endstream
endobj
37 0 obj
<</Filter /FlateDecode
/Length 3478>> stream
x��\�n��}�_�� ��}� ͌��Lb�ƀ��r��jRW��(��Y��a/�ww�(�M�?�ğ�]F�DR)�������m��q2-���Ͽ,��By4e��
�B���R����凟�����x!�E)�i�_2"�i����/?|�KZ��@�B�� BT�-�,��.�Ҹ�-���xܿ��@�5`�@�@耑���P*��tI�e�����	�b`�+��D�&ٶX����2k�J�k�먖�W�7��{Cˣ�4kr��˧�1Rsb�����������cE��&��c36�L��(�X����m�`S�ŞE
���~[ch�ѕ>.�څ�qy�K�3@R\��7֨�=�>I�J����=��|Ћ`���)��*f�Ř
���i �Y�p��)jL��*d�5f4:�
��נ.���::@�aCl �C����S�Wt%��	�N���$09��<�OQh����~8W���S��ra���\���|��O�5�i��B��锰��ҭ�Å�B�P�@o�L��9U�����UX8c:h�����B��W��$K��h'-hd,����Ɩ�M�ĢSTOW�xL�x�p�i͹u�q�%2�j;�̼_����tiq��r�~�T�}���;wW,�_/��0��G������<ރ�{�x����A�>��`�A�$���h��:���&n�I$٬�	a�hB�6���$�h���	�Q�9��H4!xM2X�I�ڢI���I��m�1�M��iM:��9:Wܑ� ��ua1��B�\�VѤ��G���?H�=�d���	!���IA�DD��s4�@�R��$��@�Lޭ�I�Sv�.Y`A���2X=�i,��hR�M�U�&�b�&�9��1.�DN��A�0��s.��3CZ̹�\�r0��b�=�b����{�x���=xL�����t,tR��Il��!�b:b�X�qb�
�$U$c&� Kĵ��ۮ$��"a(�ߍ��pʤ_Qؔý@���",ǖ�����	��
�nD���]�t|���i&�JQ5ST���S��jg�b{�����ue�9�	u� �įQ��J=`C��L}�3�`4f>�<
貀��Fzk�e��&�4CkICŌ�a�э�!��iIyj�ox-�jաb_H�f�h���D��:�$j��	1��O� @����F
bW�=���F�LN�&aS&�,* 6Di[�p����������)�I�!O��T��4+@���e�D���M 0@��EF@��u�J�����C�2x�D΋wt�"��FTA�ԅ9:7��9�rfz�9��(:�kKi&�;c,(_]��hJ;�g���V$�)�mi�5����F̖�Ii�����))�����ܷ�b����Җ�CE�~�c�җpyG������`|&���Ze���X�J{���Q١�Lv�`��O�/,Yl(��K�u{ʴ�_9#t��!1����@�v}�ھ&Vi����y�/\T�M+��q�yH��:�#�O�G~y�#WtB��k1�3�1�؃yn�>���c�)�_�uc�׎��^L�i��!g�Kq䜿Ƒ���kL�R>O����b��7B�7z�sW��*>�Ĩgi9��o-
�h�Ǧ�I�	���IР����ƞ��<.Gu\��?S��J�hf�����j��^[Q��gof�ں�`w��+�kW�f�jc�v���G���T����Y��.ywK.�Ι��ʛ�s�AS�#�5�U�G3�����g3�ھ��%�=n�M��V:�cĪ�8L���5�齺��r}��c���3W�>����^�vO��'�	��8��'k��}��Nܨ8y���Y2�12�&���l�5�S��Jx7
aΑ����Gם��u��{�p�F4҉��\������j%~�Zp.��y3u�)� ߰�;qY�g�&1�Ꮛ9;�xl�F�z�jĝc�#��?�	���;����r'��gR#:�tr�z�f��`Ѳ���i��:�&I?S��:���щ;�:��/dc������5x�mD�_�s�m����C��}�z�p�m���pZS�O~������!��}�T^u���.�ٷ���]�N���6>ǟ�Y�5���Mj�$R�f&?�j�td�!״$��9H��h��٧|��n�ĝ}#>���;%l�8VJ�)�/����HxU�{�eG�.[��)SdEL�R�K��*$�	<n�+7��z�Hc�r�Fy�Ɖ��n��T#�b�a�,c?]�ш
���z�F��6i���a!$��z�)`S�%ƺ=��R��>:*"�ɠk�1���PՑ�V�������mtXw!'1�}D?a],~�����Ñ��v��m	N5���Ķ�c�iRޓ�1,o{��T�Yͼ���a�����1�RՓ���T������ͫrT� /��X�U� ��$^�[�Rg;�� 5T��XENƲW������>+a԰J�N7+�i�MP���{�@�ór`O��j` 1՚�F8P��eb������&��R��Z��9��85C������#����q�QըX�E4�	����
+��	�{��=�"X�PV�����8��Z�|�Kq2�+qJ�Q�2��/|�Q'3�5��QvӸ�8]>� ��Ʋb`�t�uAX��Jq�j�z�
q �,^�S���a���m�3�)NJW #�[Dcnk%߫
'���w-Gt�J9
���r�'�U�r2G�e��k����M.GY���('���Qf�^��d�x9ʊ��*Ga�p_9
�s��3�3d:}�)w�h{���9���V�q}i831�;;1F^�sɟ֜A���e}_�r�f��3(7Aԇ�/G>6--�ȷ'�i� ��lyI(��Y�J'=6�%ެ�p3�a��߼�i�\����Ѡ�+YX�䏥
S<TJ@��iJ\���v��Q��E�1�K0jwr��+/]lʝ$�C���;�0[�7����瞄�JĨ�0������=�yg��~��D�M��m��á��F&��&�m��R�v[8�yڧcُ{n6�g︆1�Ϋ>*<6�9p��A�yj/$�糎B�a���q��x�w�g-�ǃ�`L���pl�T��٫�����O������	Gb0�K��K}e�S�$Qo�u�L0�b�ߞh���kM��}����'y�L(���dS|�g�^e�3%��T���s�YCϪ�+�b+J�����Z����
��T*z�F���ןQFw��������v98F4��G��T���Wc�m�x�h�"P_���w>F'�m.�dL��k2&�7��Ч��qVD��|
��W��'���������� ��Օ�бq(ל�n�ӺF�v�Ҫ.]���}V�m/�5L$�S���YOY�͗��X��N;��ɮ}����r'���IO���?��
endstream
endobj
39 0 obj
<</Filter /FlateDecode
/Length 3754>> stream
x���n$��]_����� � +��,����u ;���g�Q3��##���5]M���U�~�>��2�FcX������W&�E[�_����?,��Y���>�����r��a�~���?�����|ԋ�J�r?&����}����/f���a�D�\�_}��.J/_~����y���'���c�
{��|��"���	���)�L^���s�An���ʥ�#Q;$�{V�S��z`Fp�� � /D(�ͷ-��B����/n����x�����_��t���H��`�J���݌��&�(�'2탑N��k�
\�D/�E���$��w�J��� ]���B/��xa�#C� *,8�i�e�i]�F-�pz�^�����������
�8kJp~�t*-,Ηpە��9�C�����T�Q�Ѕ��+�.Z_�Z; ��C�Gԏߞ\���;^�ZK�#�Y�c[Sg`����?�ª���Ҋ@��r�@�w[�W��Pa!P�P�Et��_��F;���tj�NV���U���D�#�!�BVN@�kCDFۨ��ԭ�ƌ�0��V�B��;���3�,��
A�S-$�>�oK`��[�b30-Zg&�����1�6�XW_�X"��Xm���w�8A��.-�\]���
��vu��%���ӿ0��%��ѣ~N�������{��=x�<N���F� (�@ǫ�ҁ�0_=F�� �@"A�ht�m � 4
2���G��@�B%Zk�ȑ@�Q�:�k%:�F�B����L!�94D��(}���#�Vz��P 1
��P�ơ����b��pP�>�7o�I8i��R�������#�	�0�8]T��� @�C�����`�
�HT"ɸ�-PqU�}VWD_�+����)��9;�Z"Z���t"�����>Hd��-P�A��I�UM�:�h@��G(�U��5�ޅ>�eaVD��	�hUH�#�ZZL_�X�f��M�B��<č �v��jA:[l��jT2�i�C��Rmq!�v�t��.��@VA~�ӕ��AHKD C�jQ ��bd���n�9VV��.���X�׀@N�t�\5BP4�m�i�&d�i��Z�DC�bC���qk�-��x��_7������n�_��\�x�~���xm!טP`/�� �~��:^<W\�@� ��7Q6�u/�H��@��(KH��mKH�[�B���,�rGBJ�Չ�wT�	*�<�l��Y��yL�wI���$�����Z(� �ý�5��:��P�u'����*��������X��/^ƦuT��2��%ɜ�mm��O��u��uE/��Pߤ�a#�1;5�B�wgd$����oua�!���(o����s�>M�������ױ����]z�X�UAn~GRÑ�:An�k����.ۃ~ 7A����\Ҕ�^_�Or��h�@�s��R�X���|������2Ǒ.��JL���^S�1�N�tZm'�Y�)����
Ja����ӈ{�4�r?k0��޵MG9H"t�Sヸ�R�������JA�T�A��\�*�����s�/�$��TsE�7��:�P�k<l����������3���UL'����ʅa	«�3�j_ki�k�fh1_����G�3 }�vn���*�+��Ү�R�k����u�58�f�L�_�gjmo>kdLM�)K̤R�k�z������$g�Θ���Y߭̾���'�~���ThO��^X+(9�0�����٭�^�Zh�Qm� ۝�R��;�Ʌ:u#����
_�n�&ER��߽��(I�s��b�VJ4I�T��� �Q�����i8,�ז��1����6�*� �
����Uح[��������� ۣ!��8��i�TP��#��i��%���z�����X���1Hv�K�x�6������A��)����d�m�ii���|dY��#��;[M���]pg�!��~����,�{�/v/Z_@I���*��o7wT	��@�H^{���P��HD���O��Nx*�ί=�K_��m�4_�i���������Hl�b�ũ���F���F�R$�|�=Rݷ�;	C$!g��Î��q�F�]|���䝎Ԯ���9z�#�˹�#�=�x�v5?�Hm��{�]�9R�s�NGj�F���+�Ԍ���I��Ή#5J�X��W�3�0Ayi1j�7�.F	�C6s4wݱ��b�M�u.UEԏWE�{UԢ�7WE���"�pE��am\�jr�����6�H-�b)��2�N��p]^�Ϝ�+v��b�M�F��1q��$��Qm�[���L*!�q���oYl���͵�Z��K����g�d��=0�`���,!����ׂ�Ⱌܵw@��5=��f��b���*:@Ak��wt��]�F�ץM��굊"W�*�C���#m�K�ֲ�۽zm� ��Fo{�:W`nU>D�ߝQ��@Egl��'!F�	Y�N�X�)����`��Fk� �,a� ����H�1nt��X�B:�^脗
;�K�Z�3՛*�� ��p"�����+���b%㈽J�^_��*7�	N��%+�n����F�@^�I�ޫ�J`1��x�4�+З�z ��n,�4
"
�X���S��YOfԥ �lM�%����V�I�BГI�����3'6�GC���TC,n�4��u2C
�;�%'AG��k�=ٲĜ�6��[�:�Kq��]��` ��PO-JҐ�%p��vp���^G���p��LC�
)V�.�lW���$9���RU�r���`vo�/�eّ� 7��h��S�c�ƃ�
-p��`O'����+sDa?�-�5x��z�§�W�!�	#�6M�"d���`WbE�ꛛa�ˌ]�T���˻6řΆo�Q��A@0�?|��GН���K��EQ��N!�/or��q5��}%��X66�s�����A�N~�s�N'��\O՛Ҁ%��d>�� +�X�6�_oH>V���cq�	��b�͍�A�~}��ob]j�*b#J�^���8[罃&�hUf�\'F�wƸ�G��b���'��S��T��j���ϼ\��-%?��&���ˤ���+J��f,��&�<��`C!_��KMW���ܼyQ1���4Ue�DT�D�6.�]��M�b�AK,q�D�w\IueLe��t��Qqh����nXh{Å7�XP���8T������[�;�^��=c�TX<�i��/��l�/!�;!��W���B���4�B����3惛��������+��{H�ԇ�>ë���O��%Hn�G>]�;u4臁�����	���l]>���)�+�����~EA���{��W���x�N��CA��!��x����ƺ^��b�`TΎ+��[s�k�C�Û�ʼMw(���
������ěػ�S3��7��3s������:��}QRu]��="�O����t�c[`cv��*=�1�Bc�>���F+�
�Иyq|( TS�'���D*���)%�(�f���~���>�C�}���_o,��\�!��+��$�¸q'0l7;��pR�y|�F��Qk�#f5
�21`!�HZ��	�}�
Y7�řa�i�D�OR2tث��S�)3&��l�����&�h��,��D*������g*�zj�)PZ���J���;
endstream
endobj
41 0 obj
<</Filter /FlateDecode
/Length 3702>> stream
x��]ێ�}���� fx� A �J�s� %v��� U�{��lg�I��S�,ֽ؜5�*�_��?1��k���o��\~��}�=ߔ�a��ߗ�i��	��ġ�ņ����.���������"?�&����H��h��G�>]��Qoa��0�Ŧs^H�I�}�r����u��ߋ�����A�=A�	.\%(	~�C�HP�`ҐP	:1���6p���;�\��$r7����\ًC�=a����b� ��
�}4h���jw���FqI��=�������/BXf���^0a)�����bhR8E�"�~��k�`�=K� O͂N�owM�3��X�/��6*l/�A�C�H��o��UZ�LS�[$��e}�k�}��^8aC�e4>�P�i��� ߗR"\i/���-�uʁ�2��)aF%}�D�����ʳ�u����":D��|���O/��) �F�5\���X���m�LZ4ŊD��]�u���!0BSa!Qx�P��x���?R��FRUE"�T�"�h=+�r!�#�!6�9��Hƈ�.�*
���,,h�
!��f)f��%ye�F���R-D��>���d�L�XVl"B։��������B��>N���%�H1�mx�y�uG�"h>ӤE��ɕ�!U�٦.��M�$|��È��=�u<�<�<?�Ǐ��#x�7��?nչ^��M_�q�h��+�\&�pTh5�Iة2��FW�.�	N��ZL5�:
��>�.�'�k@ℎ���E� =���x��y�>�LI�>��p
X���hG1�7L�a;;�*�ux% �!&��f���1.OmQ ��~Ϋ0�6p�<�!�U��^���y	�`�i�9�%�!$�@�6FX�V�?a��e�G�d^��X���|Ċ�Ҝ�f"���a�T��O88ed�*hq�
wh�dH���~�����Nv���I�gw�k�3�!��P�J�ɘ�0�x?R�y)�6�>�ic��ˁFdvN��4n"�Lp<�pU�r�Hk��NP?9E�R|Zb�Ԅu���<n��<(�-e��S^���m-]:�K ����k���}0��7(2��>Jx�й���Ҡ<2���va-1��狆�l�.+H�
���A�i(�[O5����O�hhʣ����?��ye��4��'}�(H+�R�`�V�M+�QZ�vc�?~�W�#wZ����H��&;���0�R�z;Q�v�a�x�(�.��"��gZ�|Ei8,�h[c�[��
����4;U�kߧ�  w3��P�V�XV�=��]B4z�^��i�jXMMt��F�Ļt#n��:HA<����%���ЂtF�[��G�͵�AE�y�h��X@d�u�t�]���*=h~@���vU����[��A�� ��q�z>��^܅��O�ZW���(���0ҟ���[Ȩ������ݸb��0~xx�j�C��$���{Ì��
ϯG*�gZ�i�����α��~�S	(o�̮�ɭ����yy�6ǯx�0��0RC�ᖛ�0������[<ʤ5�5�a��G^}\^=�m5Ϧ��id�+�a��θ>8/�oh��e�{�1�ޘ6>�\�"���ެ�s���1	�����P;(
Ě����7h�<�?x/�к�76}�׮̓|��������8y�p��"���+��@k<��B�&�^*Mo '�!�i�3{�9�A� 6����h`q _�o���
�j�\@�x|�!M��8�U㼙�n�f.��G'$��s@�֚�_ƺB��!� (4E�h�q�(k#�,�86Ӫ�^z�d�@��&A_ �T��H�*p�J��֖i��q�*�L3Q�E^���*bm����,MQOSiC�T�Vx�n�p���x���[�d�jD��)��7�@����[��R�塞�t ,�2������1�|q��U�Y��	(p� 3	����<�u�t���΂���:�a�����2tY������L�rz���@�B�=�I �]A�%p0���x̪�ׂ H�Wi�tN�"�*�H U�dT�8a^U���J$��U��][J1����_�������;_$n�nڝ�/krx-��C
�P�%Z��㿹Q�$�\f�`�dW�5�\!�'W�wi�D}�4��o+�@w=�V��l*�^|�ݬ��H�2]��	r�9�V<��0�`.๩y&���R���h�096|ȗ~~���L�������W���\y����;�;QG�nr���qC�c�޼7V�Kp�����#��wjn��	!�����C=�Z`��5��G1��� OA�n'C���9A����gݶ�&�)~�y���+E6D�Sdc�?N�I9�E��������6�$D��Ԓ�ts��瞯���^,�!Znɍ��H	G��ɴ�vz3+nSNB��-��M7	�_�f�`P��=Z��6�����,��K���d��Tޡ
��䳘>fQ�*�e��)1yɉ��M��1��EMf�QV�:1�w������S��X�n{�{7��/�oQo������8*�KM�}YFXQ�+Ǆ;	��ްS٫xI��h�ԛ� ;}eI����o�Ƶ=i~�b��&#�
)m�G���L>A��R��+�9�+KL��~Yޣ6(���u�$�O��4�6��Ȣʢ�"�0���sz)��py�oU�)UŊp���s���s�p�t�2�B�jy.Z�E��wLS|H&%�gR���pW�%�#��B��G��~�)4e��ַ!;����sv��f�:�n1M��(�6�V��lym��H�C�.�o�9�W����r� K��I�BB�sG���FL*�)q3;�3���K����4#D�$4E�����z��8���_@M�<K-��й����*����2g4A,2�ai�*����޺����h�ѣ{�x�%Q�}��)I.��,i�o�V_�4a�$}$e!�A����<Y`����Ő�5��:}��9��n4��B���/e]o�(e_������"��؎��̻�.��*�Ғ�I�r��l��.�����a�E��Y��U�.4�i�o��J�̑0��B�1|nl�(F���E-t��^�=�����@վ۠n���jH2�m������ D�� ֏9.D�/=.� ��E����c���B���B���}\��}�q����q�=��ǅ��nǅv�q\�N��k���׫x�<��M�����-ۋn.i���WV��e>�&���q�� D�m2tR�z����%���%n�߯�N[2��T�Y���z�:0�~������⣬��K�MZ{ʃ�Ǹz��V�w�J����ڌ�3[m�bNPW[t�G�D�]�����{y|��}ދ;�j|&�W�uO��2}���J2^�' � ۯq�� �C6�;YWy	^_7Gy�W����,���V����+����|PЬ(�>�<:8Yޜ��Q|Ց%�ϺW�w�������l�i�jU����9P���e�:�����	H��ԓP�=��"i��|[�+#ww_��I#ٮ���Y0��w$ǙZ�Ze8׋��cO=����7��۽�C����}r�F~+�mSOBuw�Zg��J'f�6�$���F�;�i�u�Q
�t��,kN�O��N1гoK�rd:����f[�X���h��`�s�?��
endstream
endobj
43 0 obj
<</Filter /FlateDecode
/Length 5192>> stream
x��]ێ�}���� �y� A �쌟/�pb��;���ע�5�5�3k��}Z$��")��c�s��7��\��1\~������LmE���χ�����f�.����4���o�_��~~��{}��?�?�EJ����"���.�����gs��O?AG�By�~�A*{Q����ß���/�O�~p���\ Pa�5���E߇�	���Il�ɝ>}�N8�mQ2xB�t�A�j��kV�M��z0Wp�� /$^��P_nZ^���_�L�����4%����AJ�8�c.E�,���vq�G7c��I��i�X����ֻ��L�"[�=tE�� ���cZ���K�b�����ŠG�� *\�����&8]�](����̓����u�5xi��D3�@��_)]A�d����]i�x���T� �O#jb]��+�.Z_��Q	Ȇ����.���3~[4�/F�Y�#��h����.�E9�A���
A�w� \�Di���A*TĴ�.�G�hgUUA������ܬ��r="(y!='Й8��h�,�ezE�!�%Ђ���]�b��.˫H6a2HG��@-Bn�4�`�m�XQla�I�Oߒ�����1�v9���/�DJ��No7��q*��3]ZĹ�\�R���"��Kb����0.�_��s
<�<�<���=x����q%x�0���<&���u-�ب�M *���$a�����c4ԭ�I���$��h��D���I]�h�`� 5��hR>�hR�Ѥ`�6[�Ԏ������9Wԑ� ��5a�lB����O}���F���?P�-�$��	" 1D�]	�֌�P�6Mh��T	���1� ��$a�h�@-�*�$�h�h4�`�&�[�&��M��ĺz��)�j;�ݼ_����ti��r%~HU@|���8wW,�3��{�x���=x���T�+գ��R����&	[G�n�	�jh4I�:�$pM�qM��&	�F���IS4)K4)߆hR0j��Oj�d|j�V��+�HD �隰�w6�RG��>�TE�C�i���M�A��%	�T
)�I �(H�A�O�_�@!�;��O�0���4~d,�ڮƏ�e��rbO�[bz� b���n͉b���M8ċ���i�lz!.\�G�}&�x��=@�����\~y >%���/��7
/���Ȇ����B��8b ��H%#Z����) ����`!���P2��L����,>J�ATft����� ��Da�@ ��"(q JirD�$ �<�SVG0�UEPf���Q�����ޣ0��!Fg�
�>$���t��r��
�b��*��
�@]���%JEWh��k��5�ZZ�x���B��̄HE�bC�^��@A�����/�MV��"�D�D�Sm�@��V�|)�E��Gw#���b����y� A����bA�P
D`T6#B�i)+����J���"�Զ (������Q���m���I��PQJ
��&�]����Im�m��	���b@M�-i[u@�h��i�%di�vS�i��y�c������H_5�Ss��ù��U���s~k���/�/�|��?�_S~3�;��dL����3������xN�4��s��)��t�������{,	p���}dY���x�h{Ut;��V���[��`E�UI��Y�����(d^�R:�Aڔ�����br�a�����~�EHV�����<q��[��~!*��b9���
�h��%�����K�B�iӐ�a�w�2�(���h�`U����<��� �o�J���G4����&)`�h����5�!��FE���>�lu�.C�*�'�&>>�"m��e��� ��1E�f����2�3��(����8��0OL(^�<�� jt�o�����\�m�a��8;�?	m5ؖ#74f���6��u8k�jH����P�a\p5��wP��BAG^�݁����뽆�4�N��z�4zX'�(7�B��%I��i��EX �jW�V!��w@zyF��9,z�&]eE[X AWF���i�V�|�5�k�>Ze�՜�o�������ދ��C>
^��Fi��Rk���C(�
�����n�2����!���MNJ�	QMw�h���<���䋊,�=��Ռ�6#�v7�y,�5�{��f�����'cy@"\�����υ?c�;Ɔo�=V�=�����\�wx��/��N�Ļ��Z�(#G/��K��k��`�|�A�XB��j��A�>��">V5A؎��m�2���o";���Q��d���9"���L lp���]�����hbǖ����J�N�c<q
���v�>U�F��q(�|�6��1�kn�{�\@\u�pN�^{ݝ��4��H��������s� +N�HX����I��L��տ�Xك��Ձ4e~�N_���K.���������y�H��n�����[�,���L��+���C�
.�ǫ�b	I�L6v�%�٤2D�7�&���Lav��['�*d�?6��7]�3ͫDh>�I��4~l5ā�2oT7d����!�9�â(����{feH�[drb��� +����-A�DX�Y��
�$s|SS��x ���3��ZVQ��|W[D���a��Кu����Zn;l|)5u���d:kr�� p<(۷��}2~��B�}����Ð7��&��[��e��\�6;�[�=��O������(���4<o��{�n[��	��s�ޟ�Yu���bzco~���v�K�Y͞��6���y��//]o���;	�L^:��:��G�Zl���V)� #��I;�ߝ\6��'��3f�<�)�,x~c��ch�Nx��R� ��O'�����y�6eTo��<{�}�J��L2��~���!a�?��^�ߐ�Lo�+�Z���=�ap~S���|fz����M�����$�Xg?V��3��62=���v�����'���	��K�S5o_g������t�x�m�s@�_�m/'�A�Ǜ>�����ɢ�́���~�Ȍ1�k�Z��q�}�C�ߨ8���WpL�<�Xqr�oS�����a0�әI��j~�X�n똵�#��@�E�7���;M��LX���s�U0�؏l5q~���.m���c����)����;i�������1�o��g2؞x�����	ޝ̼}ޘ7�iQM?Z2o��>��\=-�o�g�w��
��_=��y�x[t�	�*O|L���%d~;u>���=�~�g����;�D'>�����ۚ����T�9�`���%�˃%��S�I���w�N��ՋKN�řuX�C���
���)�UO��,�S�߀���9����I��ȟ->�����=�/�s��@}���O�:�H�,F�ʢ| ������(�s�?�6�Qz�M@י���Щ�;��ƅ{&��V�'�"6���e�*W���]�)���w7��}R�[�}�'����>�%f˞���y;$��L�p�wG��mA7ʰg/�7��cEaf����3@�4ޝ�����Qʡ���Ί��s�+���?�yK�R%�/�Z��|ڏK�����\)@���T´��LA�h�P�P,�j%�U
�HC����JH+�6�W��c�ڠ��^E��ݫ�6�(��V)m�<��+)U
"Ԟ����"���(�R9��_�B��YQ��^ii��޺���ҕE��j�w�w��ζr�Q�����JA,�5�/W(N����Y,�V/&i5)^
�ªխ
gh��ђ��Y+�I�n%B"Z1QBn+:ڹjuI��Xi��X
 ��'�A ��FiJ���(k��
��`<�X
��Xi�J+�&��)���I�M!��Mu�Lj���}�~eJ���5�/J���4s���&ժ{.՗��7�o'��\\S��B[�[�W��9|�L�M�%{�&.�ʳ\��`+�i
�R�o��RO�^��y�~-�pK�_�5�ԄjGW�?�l!Ơ�d�X�]+�������Ut"T���*Se�T��r��0*}��~�(tVv+CY~�U>���8�&'z�bsORj�TI�Rȃ�TI��P��f��y����0X��Y)�f�a�J����X�YiiV�@�ܵ1HH�!	c��$��?�������V�<ܖ����d퇴�bIzu�R@=�eIKm*h)IK6���iio�u�G�ڢ�t�vʻ�;�W�g��ښ�ӴT��SP����'7���z�!I����衟!/̥���� 43�MM[˞���{2H	�ic'���������w��e`o`\�ӆ$��[�Xg��0*��S@A�qa�b�{e�k�26VӯMSI�*�>B��@J�&!��Genk3�[��9Zf�/΂���ɺ���Y��&�Ԫ��t�Q���B�����핕1:��딴Cنl�o~Y��8R">�[��!��J�;Pӄ����{��uٚ���X��tx6|�DP�B�	����)�a�,�R�p��<8�T8r�c1��hk��3��*nE�<x�m�h�8~tO�v�Kn}?FnM�n�|�T� +^j�yQt�t_<��1�z.��6ݸ����0�����5c}�7�h�LI3e�z��8�Xۙ�]��P_}@�=v�:a&IḾ��0\�����տ��6�S��#��-ow9���p��a����(7����+g���>e��P��)��l��y���3'�Q�4&�N��G΁�W�Z�+4�x��Nv�8�^+���Z��z	a���)�LR�WK;4�mEw�2/e�%� ݯWy��=�@�=<�:O��Y����隃��iǲ��@�!Үu}�G��NNHH�$>��@)TJ1���jU����W9���^yD�8+^��ț)y��|�[J�ou�q�뻴0������ޕ��g,�`�QrsB�1�sI���I�s���|�D��ܷ��	�����T�;��Ǌ��W���]��Ż���"Iq1�Ӓӯ�:�W=�  �� ��Rw��p����La	��;k�D'����ÿ����핃�ݍ�ᰯ�<����9�>��o��b��5����
endstream
endobj
45 0 obj
<</Filter /FlateDecode
/Length 4262>> stream
x��َ��}����]�V�Z?'��c�ʀ��B�EV�=����h啦9�śE��˫�1�,��[�e0r�2ư|�|����+Ģ���o�:��/�/ 7�tp��#�W�\��?�_��~>|��^~�o�G�H��S��5�[�<|�j��|�	J�E���������Bh�������� F�>|h� ��R&�n ��`�>'�*<�\���l�Y�>2�C�p�S�� � /Do(x:�4h��z$w�_�'Fŉ�#1M	�?��t���HoW=Iʂ!+iW#�1��O��wV*o��e�V�&z��z����s[ ���
8�Rn�\.����2$����78m�,0m|�(T�Q�|�ǃ�����1xk��Jf�	�����>/�k�+!H��k�,� -�� �V!����
����{-�����~Q?~:����^�����,�����hQ:~ê���ӊ@��s�@�w� \�`:J.,ʠ*´�.v�G���*����S�U��ǪA���q,l��T
,Z[�ʴУ0�S�Yݱ�`޹"�")�����q`.�����]�*3,���d.�]����ۙ=�a��1��6Rɚ7����M8̋���1i3�lza.\�������*��Q?��Z���-@|���m���\��#e��}�^�!b ��-Y��� u���m��K$��^t��^yt+�tZ���חGW�}�HP�X��(��(�U(
���2dg�	y��D#����N�%��Ν�|��%)��=Ñ Q4��ߋ[D<>���� �1> h��ć��&> l��.�!����z���C����W->�>>�۹�a���2+�̀�n��3�*�4U�ܽH���^���1�*�����o���~����r nV%���nU��̠�J-�[��+�� 0
��hh"�U*�A H�k�PbW�T����6���ٷ�ID&H�d
�?��G�95�j��� H3
ˑ{r�uG�����=c���<g�VѤ
����C�Ө���8U�: �k��- T�!&��L��~!�TXL��$(��
��'�R ��tM��Q�Ǭ
�-N	l��Ƣ����]��Y���6� �2��2n,NR�hKe���#X��>ވ^P�	lb
�h1>��K��n�V���\����ho�G�����!SޭF%{�t)�o��x��CbXa���rI�0	��@ @��`)�0̭�*N��B1�J?�z�̭2��3��H2!�I�̭B��&k�|�	CӴ���H��SY<bQ�ڮ��`�q��X�)�aTg�V���L׬6X�c-����<d*L�67��~_��� �H�������>�?�1�+^��V���Ҙ2.�k`��黐�?�&�����N:�d��0[�4LY@q�C���H@�E$���L�5�+&_g��~0��|�a�(�IYDi�=Iġ��}�3�y��O�&g����M	"�*\/"�]$S��r���Tk�q�x
�$Ѫ��}��&H1 �oX٥]+��LB�����
�X�� q�w2	��cL8��I@w4_L]�{{��,�;M�X0�/T��
H�uO�>ں��k�_�I�L,��W��o4�<.T;��Z�}W�'=�^�7%pڢ�gDkV�e�D�.:)j���
��Cc�`���vJt�g��9"N���S���,?�4Yv���Ky���(����B�d�[Mr�ܤ}�k�_Ə6�?�3�W�V��c��n֍�^��)Wt�`���tcB�P3];J��)�b�����5Lw��
�/���!:�n`'.��a�%�d�심*>*����[#��5�"�y�н��0��a����y2�>�>�Jxa�|��x�~7�`����2�=����rM��[nc!����%2U��j��ԨsX'�70�%A�J�g�e��
��ٕ���܄иKMم�P��G\뒝+4;��3���{�V͹r3Z��{&��xf:���jO��j���O:�=�c�m絷�D�+ݓ�|a6�ƿ����rHbݩ��x�2�|�+D&:��x�z�0&Jh����DyM1���\iK�\�p������v�*U5��T�����12>S��*�1lܱ2|J�AM#bm�(�uo���}��	s,��{w�c�� o{��ΰ��,�g��53l�/��ni�^r�4)y9Jx��9���L��q���6�>�K�U� wz�JpGA�T��jLmZ��%Q]?�]9ѼRw��	���`6��9#e"�gA������U��9��k��f���Om��:	'�y��O�*6#�Ց�6\ׁZ�̳�w�~��n�c(o�$p�)�B��}{�^�[ff�V��������Y� P���b��qx�z���\�9��k�lu�nJ�����61G�!���� �Z'Obg'�z[��X�
֏p��g8-�E�P��,�,}�²�H�'2�U�_�"��E.B7u����A�\��E�A+�Y䚨��5��Q�\�����<`�k�j�"�U3}����%0��}��1j����zG5���-+����1�NM���us�����Es�A������Zۺ�M�:
�l����*E���'c�1��0�ڶ;i����6��qt�c�-Y�Z���\[ޣ ��{&�j�|�c�l8#�B�����ķ"�nS���{q�3%:e��$L�U��U��n��E׶�r���o3
�7%iݓi�gy�g�RZ�KQ��͹m��9���vچ�9���G
EA|��\u�P��tF�b!�-�>L�{T
��+&iU8Q�ȼ_��E]�g�n/�|˓.�[:Q���N)��>��}�'}�n/�t(����{��ę���Q��W<ᚳH-���I{����=!�k������UN��µ����Wu��0#y�IB���sB15M�Js������2�[�@�)~�9��rq�n�3�Kz��ej����*`�x�H����B���R���ɬ7�7+��qԤǲ\\Seps8qq��de4�ö�a�#�����v�aO�,��Ra�1�}d|ݓ�D�*�������<yi
�m�5�qW�.��uy��,�|�f�B];C�Z��P�^��lOW-j�n����N&�}j����;]��E�ok�k�]��ˏ'�1�quu�Kv��~�����c��r��@��L���AL�;���>�e�Hf�wOi���������D�C��nj{���a��vv{c�ˣ�����z�ޘ�������D������������v_�u����{�7�̇�7���F�у�������c�u��䅷7�v�ho�Ǧ�7dx�.ᮽA8g�7zN�� �W�7���v�zIpGО��ؑ�_\OY�-�-�{�/:V(�e���քp<��m��������JvjX*ź7
}����G�H�m�N=���n��wO;*�,Z�a=���@�q6��� U��dG=zW�<?�`ax�&;<�+�mTw�'@H��F� ��y�s+��IP~�'A٩�;^����l��;�F�����C������O��w(��4`"���݁� L.Hv�g�;���?	����I��t�)"��d��1+��iL=���<;0�C�����S ��x����Ez�;�Mw�' =����Y� sY&���'}��ɞ�s2	���	��7�t:��qH�yz:-��$6~�'@�����	0dxN�I]d�Cw�'@#�5Se�C��Ya���G|��&������\F:�����]���H����>6���ܮ-��#������U�c/bVx�}����$v���y������q�r+���K/Tf��q�b;��:U�r�]�d�����f���<���M�~(�n��rZv券���#����)��|"ɽt©���'2��m$?���"���Qa�`h3A�2A��[+!�҉Y�<��X����H�RM��p�eW�.3���f@P~�'0Kf�hq?38�F[A�j
R�H/Ăr�[��]F`⽍�0�a2�n&��N���~��
��U%���e��yõ�K�.�[��}ǈ�=_�.�O�'٨�fs�a�t��m��#���it�o �q0	�o����̆�	�E�ǐQ�*yG�a�W�
endstream
endobj
47 0 obj
<</Filter /FlateDecode
/Length 5015>> stream
x��]�n�Ѿ�S���"�I �c�s�d��6'� I�H��MK�Փ�]Ϭg�?I�s���"U�.+��a��^�%��姟���ץ��E�5\��������?	׋�t�K-���Aq���%}���~�{u��b{.��Rrs��ʷ�t�/�y֗p��Wj(r(.�-�i.R]�����uU�w�/�x�t�˟/H��ppPk��!"�*`�#�:5���m�Io����n����;��\?�U�P[`pǈs��œ�3�W|z�i�r{zU[v����3�V�̸-3����z�.���pf���$9�f��Rsf��c1��	��hV�_컵�@���ɯ��)������.D�y�.?�/�����>"����Vi%2�t�lXe������O{�M�S���)Cڪ��R����ҳ���������r�ɌyA�\V���>��U0��i��$�v�`��O6��텿-J	�nf���5�X0ֺJ�ǖ�"��d�(��0�sŶ!��H�A?�	/}բ��Z�E�Z䇵�FV��x'�P�+6NO�<����.�,C67[`,��ʜz�pA�3df��1g�ފ�<��H߹�N��v�6���`�3]�cf��_^�;���E�Y��� zfa��A'o2C4�`�%bx5mc �`�f�At���wN����|P>�TBV�\�>��G:����?M��X#���m���@�����懈m�CĮ��~�"�����H#�b~��&?D,�(X6�������ǜ�.?d|�6	�
���+���U��&6�S�O���EO�7r��{�`���5?D�w���M~��&?Dl����䇈]�B���߷�!bW�!������ⷒ�.?��ыJ��o����*80K�N�d�h(���)J��j��@,v�����.|���t�~����Å��t��>?�Pv�S��* cix��� � �����m~��_��H��^�]M'"��K�!},�!}��C��K�譍8�ua}���QR��p*���+Z��l��@.��x/,�m\�C4���m�CĶ������M~��#����#��0n�!��>EDTG%U#&���������K�vp��,�0 �Y8m.\�W�[LTA�TUB���!�u l�!�gI�#)|$�_IR������d�EA������׋r��Q/�ۅ=%z�V�#H�n�r��EH��)$�,���/� 41�zKJ1�$�J�2H
Ӊ~S�a�q���b�0~5H�@^����/�VR-�H@X|��P�,j��g�����HĐ�4Z�E҄�[�E�7%q��ٴ"�h�hj���b
DTxQ#�lƢrh��5;v�5���9@ܛ�Ů��'W^T��4����6�:�VP������-g�2��%9v>K��U�Rdp�(Bi�GN�����ȗ-{�P��2���&��*���(��UwMH�C*�IgI����/�:Hc�����i�͘C���3Z|yh-LN��,dZ��&��9_�r�b/��v�+���YX�8 |t���F75L|U�c�6@�Z��Z%@G�����z�/K�8K�h�G�<,�j�Q)�q][�4LnQ���i/��'��T*�}/�m;Wq(#C����ӏ���a��7H����.*��/�&�~<KJ�.�۠��sW�p�`�X��[s�d}�����P�~���[�����q�7r3��ּ�Y�����V���Rُ��~%u�ň9�ҏ;I$��[���)�7�Z��Y��U�v�F���H_��������`(�?~6�Ҫ����s܂&V�B�l캅6��p�-h,tg�hX��t���P�ܢ���[�0����d$��4gf�ƨG���8��N X{"i����N�H��c1b^�KN ��}w𹞹7�!w��ݡQ�6�U����*�;��P���`�CvU!�oם��)�c�?w�s���ɚ4��9W�$>�L+3�~J�ꧤe���9�ת5������^6+�2\�	��g�u�wW���u}�ѦZ�-��s����Ό��zfH�g��м��D�	�}�1����dW��Mx<f57�rF}�	����Zl��F��i.�D�KBSq���c��Ӳ�vѩ3��������6N�s��٦�z<d�/4N���f.���0A�0La�$���4�r�3\��h�r}�G���T;H**^+�K�rM�څZ�e_���Hj�]���l�W�(���*lM7?,�F�,���	��,���}k�"���P�xQF��K�d��ģ��/(�3�����W-^,�������pϽ���ŋ����W�W2D�ĺ8#h��6Ϛ��Vȅ�ƈvE���ϥ5-L0���i�lX���(��Tb
��ڦS�4�}g�/�I� �V�D�Q��`�ٲ�d$X/�rs��`�Fe�q���S�l����BPf������6YfM�@��
�/�6��;����ft�1sk�A�}1��,�+a��,4L��Ӏ�P��
GJ�~sKn	.��)Km�}���.-ؠw=j��!�Sc�#�2y;�.H�+)�
�Oc��CG����������������Musȝ��.�u8@���B�-n+ݫ�J:9FO�ueɰa�'j䓏�#r�3x<�=1P�6����T�X�Cv���5�S�G�v���_�pÂh{�����Dc���F�+������SC��
{����;���ubx���c��J�ɼ���ǐ�8��Xhn�����ӡ^�XN� �T8��*<�sG漷3*աu�$={`(�)�hs[�'��c����b���)M��Lc��8�=2��1?|��棌nM�F#����G���ѨÚ�y�h��S��������
{��^.y��ڐN���������d�V�O���X��n�]~2���yL;3~%55!86K?/YM�����'a�����Z�:��{r�n�=�H�nP��;��u>J��>h��zC7>���q?V��XF#��P��4�Sf�t���w4\��#�G�󓇝���Е��������f��Fa1��C3X��������u��aS�W�Ü3/�(;����މ�w��:��ԧ�!���԰��~C}LU~0:�B��Mz>Ա���8����3����v��f;��sG��Ķ���p���r�0b�S1��7\K>���v���7�(���ք
�l����8��t���[��6[J�S��~���.bu�p�p�uCq�uCa�r!�����\9��E�ʚ��Mk/=*y����j�4Mu%��&����vWJ҄xzP�Pr�Y��آ���nkuCqgu{���i&C��q�����|�zO�,[��-Ղ�V��C���	Q�Rl���;�Gx�MM"�UA�fj�誉�0�M�í�ŝ��|ۄ�����P���Xo{���m�tUn�nJ�Ԅ��k��Ir>#�������>M(9���L		���.X�6O7�N���@�Z�c��XGo)"���ٶi�Z]__��$&@�A�j�X2#���c��r%Z-����hJ�l����r�RY�Ni�B�F:��J�<��G��2��.��UN���mՓ)��j�XN��nkXnT;)i�m��C�N~���6W3�K�Yd��*�`�RTX��J�Z,̪�E�Y�Z���*Ņ���GjUA�c�u�/J���y�x8�c�Z��l_]����QO�~�{jک�~��m4�ܮ�Þ6)��{�eܝz�SN��y���p��Cjߘ
�_��o�i,�'6њ*�^�ޭ)I[�˸�Y��EBox�M�^���ﭦ�����_��Iv5�����W��r⋭C����'.rOWw�WQ�eyW�͢A#8OǪ�_J5՘ơլCUz������Adv1��x49ڼ��̊�����t�M�%����|'�̑ʥ�yu5V���{UZ��"�ap�n8��3��n��Yf�L���_�*1���m�q8�!�[_!ί�6U+'���me����G������gz���W�<2������[�6��|��ӵâ�Qe����9&���8�'�Cӧ#c�����tzh�k�|�W�Oܛ4�ߠ�骧�q����)�Ӟ���ߩ2�2_S�}M����~s罼,�K}Yhn�֗������@:2�)I�1�zk]�k4��_��5�[�0g���G�bI�^?���˺�N�'�w�o����p��ή�@Z��u��*�8�~�BY��|\3����V�e��/8 T,>�-��p��B5,�W��e�B������C�@�����~C��^z4�qn��Oo��б”`����8`��#�TW[5T��8h(V��%�f3�Y��޼��xˋ�+(Q��a��l�,��	K���ui>��QP�
�5f�Nw'���k��"�vn������Vb+����r��5~d�U4�[�@��Te`�ASV�2WPu@X<�9�������B�I�Xu@X:���UŪx���T�uU���1E�^������������[�X�j�]�������Hһ�'� 	8JE2���ؗq�W��3�����Z�T::]�
��-��sv+O��D��l!�Sw!�|���`ʩ�(�'\�~�I��p+��?���w����͗���ο��d�����J��r����{�������R��7�)DP��=��˙5��4�:�<�/�I~�X�+��*-����xH�7�c{���v�qb�HbS�gu�+����"����Dۢ'�gi�;A�Q�8)K�@��A���P��K��)�Ν��U;q�M�x�1GB��|�"�<Ƣ�'\�7�S_mW�{w���}:���7ԙ���v������^��z�4��>X��3P���n�N&�ڿ~2�;�C��*��#�P��^�9�|�HH�f��]��/�H�';�g��o�������L�vQ
endstream
endobj
49 0 obj
<</Filter /FlateDecode
/Length 4144>> stream
x��]ێ�}߯�� �y'X��ω���A�2`���T�y)v7��w{�J�R��93d݋E�"���g����`/�U@��|}�����6��8	�o�|����_�By�h�g�_�@5�߿�0Ϳ����w?�������I)�i��"��/������d'�>��%�d�Qi7i3}���g)����������	��]!�F& ��P*�n�󤏟�G�	�b`�+�$�D֟X���T�2K`���:�)��3�+>��Vn��Y���_�f�H͙	Kf���}P�O줂8; Kڡ#k�Ǚ�3A�E�����w.酶~߭5�� g�p*�_�q-�i��5����'za).cB$15���Fe��H����U�UP>�@c� H��LZa�km
�n�c���Јc<}.����XT�i�et��y�k�
\(�tDE#�цX0
�����z�W�eۇ	��Ȧ$���#�!
�5X�&a��&a���� }E+��C��i� #�C�oB��N3�$-h�	+6�G�?=���Z�ش	�y��@���<��)�I(a��$OX@�f�e%����1��+=AF��|�<	�IIՈ3�&,�_mꋧ� ��̑����9�ͅ�<�ՙ�-&��X�TU� c:g�X��¶�����Qz���?�
���P�V�Qޒ�[RxK
���㉚!�y�hb���E�%	�F�%��	[e	D�"K$��\u��.M �i"a�4��U�H�"M�XJ�ל&�.Md��a��{l#�]���C��Ã���êh�E_�#Ӧq��6<�Kf +�<����Y�	�����3}��+�wi� �����u� t�&���4A�:M�L	�i�^�41���D�8w�2-w�� w��)s�"��&9��";Y�<Ț�y8���&d1~�txK
oI�-)�1��=�_ЪB�B~U�V���e�;�%��J����<D�~�U�*�0ZJ*�-��?j᬴�M*^{E�A5�H%�G���$T�F��ؙ�� �������S��)D��81�Gu�i#�T'��"0pq;��&M��ǧ�B�F
� \��B������ ��P3�Y҄yɛ�R
I�E�%e���*�N3 �ٺ�ޜ�ɸ�U��qZ�1�O�9(��wΙ�q�D�@1���\�SjG���7���p����F�;E�;�pQ���¸t:�G�Ɛ��,�T���o��U��-`��vS�`�C�t�t�d���q�h���ҝ��T�Y��\/i|����� J ��QB��fL!�1=��S�� 0�$�����*�!w+:)X�*���Q�5_l��T�uUC3֙�T7<�xۉS]Ag��(SU�#m�����e��iK;yg���HwNJ��U���|_��%��`�ޣ{]��X��P��8�$��A
���#��3E�X�����޳~��~ğHc+G0�J�(����l�_l��e�R�fv��zvv�y�V.�rbJ�$��X�y�P���~�`�c�*i�Ӭ9�ɾ0k?i�h6�M�����=���Z��V2����nR�6�m��*�	��8��v����&m�V�I1Ci��&�c]o9�|�6;��~0����>�bTc��46;Nrz�	b�	W$�,�D��S�%8�	�$��~�=4{��R�H��{�n݆ڎy�7�~���K�R��N�Iv`���Yt.Ζ�i�ǜ!6�xC�X����QK�H��K]$W�+K�E���z���`ì����r�Kb�3�^J�zz6�d̒x�\�!-������,��u��蘩bxQ��"f��脳C���g�E�)6p�eC�����(9�ڨC:�*�[�qc'��������*]�
��=�{ذc�^�����޻�h$�Sj����R�	�,5�K�3�+C����l�!F�MԖ�nz�7�^�0��\�,��*C*�B�5�����l�/�-˯W	o��X�ҧ���O?����FLKM�ø�!{y��z��nWhLE�L������ΫTh�ܧ+�+HzI*T]&A�%2*�eO��,�aǼ��7�%��W�1�K��فD�[�*	b��.#��.���ŭ7��d����W6�9�;x��W˚���t������F+��s������b�O�����¹�`����)����RIK�`���xQ�إ]�{DS����J�%���%a��Ό�����v�T�k�mO�H�gO����X�~\��3^�['&�=ΘU����H�n�h��X�7��X^�ן�\�[�RZo�Н�RI�	���_cg��k�@�:�J'�� ��9�;�S��w4���e�ȳ-���lé]H��w���*�.u�K�(�E��O�!1�Ԁ�է����蚂W�=�f��B�}�fC�c4E7��t{�,?��0>��c��!Y��v:	Q��p��J�W$�2��;�9�Oũѐ!�9�x��A��aQn�x�F'p�pZFس���)�K��6u�S�P�r8ī��z��r�I�'�u^��R��A����H̓^Rt���Zj1b0�N�<�G�'G�$4 �5�>f�2��X5-�D�H�����TQ+�r�{L ����[�����}n���f�n��!�!{�'�8�?b�[��-�g`�/�-��=�e8a)pGʑ��t7��m|l��
��`-��zC��.5���0����G�H�q$�u�*ч�&x㷦�
'�m�)Δ��m�FN�^�E����T�eW�oX������vW�Z%c�5J�84X]��8�C�ǖ�N� @:ѹ�#W�p�eʡc-
[��k=��.�ծ�p�v,��B���zk�FAk)� `�ي�BM��2�pevҊ�9c,���Ńx ލ�ڷ��g��;K��J��\:tԷ���w
�v�y/7���K��k��Q�ϢA�<6,��T���.�y]��J�v�׆��;,�İ��&�Ǒ��� Tу���5��Pg��1X�3fv�7������1�[��$XsU���P��y���͐��F;�հ�W�#�q����;��>��1ڻ;�Sw$�� ur:�[x����q�����q<b���q>f��ޏ�O�\�V	-q㱔c�t�[�qI<Xd��߭;�޸�n����w@�G� ��:��X�����)��ho��O�w��y;�}y!6���"f���n�f��z:���A�Uա�C�8�݆�O��+�+T�7,x�v�q�}�[I�|�ԭ��+��b���y����nx��~l��TC�+��>��C�t��ïN��<:�wn݅�sS�N)�^8<Ya��t;��±#�WX��r��_�V��A�`i���t/�į�b��b��⡰�r�
���Vߖ$g��Ɲ�d�KM�2�L��u��Ԫz����=���u���o�̐.ӥ�r���ax~O$K�S�)�I[���H�Jr���%G[I�,�~:���u]?$D��޲nH	�.�5-�|�{!5��Bjhk$Tɴ�C��֛�q�z5	;,��@jz{�Q����HV�)5�̄��a��@B�e��E��h��P�����N��Y��޼�ɸ�E�H�{��PL�M�Tj�W:� ���XĤ�a�hi���[4�լ�b��*k�0������_{1:��P�P�G�X�}�����QS�{���!��Y�#�(�jΑ%ɔ�}�#K�B��fpEF��d,�h�{�P����/�`d��:��u��c��^���G/5��>]���:=#q���\���T:/�>/u�v�����.��k��;����;�Կl��c��5�7�W��h�<��mMu���W������囟׵"�� a7�_�'����2��e�8l�݋�@M�c��ʞ�fƇ�s���*W��i#����l�CO�S��E�ǔ���z��`e}��/~�|*��w�F�>������U��F��2���>`�>���Ls�]��Ij�^�
ͱ6��Y/���Z��<��4���Yޭ.�QG}��t��!J�~, ��[�!Xg�ic�Ďgy�J�c���-/
�7�]\�O�	}��A⹪��{.ō��Kq���R�FS��K#=�F�{K1�{��;��
endstream
endobj
51 0 obj
<</Filter /FlateDecode
/Length 3687>> stream
x��\ێ��}��� +���3�~N<@>�����?�ú�,��R�t�xv=v�t��[�Xd�'cs�sV��a���)����/�_O��qI��W��ۿN�����n�Cc�0>�E}����\?���������z1۳����
�hh���_N�}v�|~�	�
��l��6�l������JY����N߿����%��@,@��
��ih] ;���g�U��^���&�S�발�,&����:�]#�87I�4ޘ��mX��Vv��u��UF2���F���z�:L�����~����#� J��v"Ǣ��'�򇠲�S�z߭��QU��r)�o�w	��Q��ɦ��`��J��e*HS�L�uV7̺����<N9�Ko'u������9c!5��K�g�1�cx��5��]���6B�K��d֤ܰ�Oxـ��c	�i$�w1u��C���)�8?���d�v<���aFA���C���!����`�0o�G�CX1�A�3��h'4D�N&	=dUy�8��o�m
:aCº��[�^Or<��,�\ ,{�H5N�Eܩ�<y��	�!4�uJn'u���A�Y��f�ꊎ؈+�{d�����$�����J�c�s6N�wy����bQtɵ�4)k\.�n�l�	����o
�\����?��S!�������PA�r��w
Fp<G�l�"Jd�(��a�(A�e���.�A�(A��c���\	-FXHi$]��� Q?� Q�� Q1酝��W�\:vgS.�.�\*��rMu���׵(�(�[.�n��{T �Q�/cDA�Q���V*���1��HZA�bff�+C����A�b .�^1�1D���a%֢D}jQ�?�(��ٓ�,��d���Y���%bg��ϫ��ċ����Lj�$ۇ�lF��oH���{Xx����m���/'H4���V��	#��CRT����;�ݔ\��K�Y�T@pe/<�-�!�;�(��C�&h��aT��)@->z�QS8H0�kT�� ��b�Q�d�&�c�$ «��r2�T��[c�*�"� @M�0Jq���h�P���)`6w�� �<1�$�SGN�T����/�U�6q�-M*�� ��+R�dʮt�y�dlʁ16��D���c��FQ�8�/]�������,द�2��=i�`�*מ64�$m� B-^�M�ZU@�A��<�7��Xb��w�ݯ���Bn��0�_DL��$Lt�����T��������k3�`b&i��aQꥼ�`���S ��"��y.����m|��*�n�0|æ�~��[���b:Xl�j0��U.Itۈ�f+�\��HG�e]��z7T}��]жqƎ�jֵ��LV����P�v�a{�l���%��^����]�EM2"�5rI�7�!�\Q�����H�Hj�+�/��	(dG��R�D��<�}�����{�z~]���he�H!-fRi�F?�������X+���C/b彠W�hal�@����H�l����<i����j��A}�i-47�ta)��k��Q'��ZY8b� oo�R����?W�:W�K�@�*ҼDȉ�L�����d�5�hW�N�bV&��FO��͐�"{B���Sؕ)�/�3r�BU�U�.4���y	=<U�Q�n]=���f(�o�D�f�O��ؾo��sc�weLn|�Jυqn����۳e�]��O;n��"[��w:Ճ�v��{-|�� �>�Udٌ�t���������ژ�;�2����m�^��*�\��+��yp�|tz�S<&�"<8��|���)�XS�U�~H/���,^�yq��3<bN�x�|v�?s�j#W�H]�oc�st,7�&��Gv*�b�E����8f0����&E�O>���)��{��Y �o�dx�#KF����e���dX�[�L�-y����=i��v�l�މz�����6L6��i�}7;�NL��Y���<'�#H�P尌q��55}IKi�t�R�L�(�������}j����ZQm���J��U�n�6e�w[,��]��[jg,o6�)�L��}V�pڹBާT�j �Ǻz�[So3{/mt3�~����v�6O�����M��j��[\�}nSD�#3l��)���#�ߠ����>�r>�sS_NV'w��"�Z�������c[���i�g�ûyj'��������~���U�`�..�'�j`�F�K����N�����\�궕����{o�Sg7�<�޴�ߗ�7�8R��h�D����� �N>�E��<!8�?qȆ4�R�#e�M���&`ѵ��D�K2&�a,�蛱��U#[o����ƾ.o�p�,��+`����v��Q5!i�u+X0ɉ�[���scT���}�
������wv
�qͫ.�mޗ6i�8�$�_�'`e8,"'�m ��筑m� �b��6�8�:�e�`Ռ�6�f��e�M��F����Z_� 2p�LH�m5֌춱e��{��9D+zm���X���+`D��i�dc�6`ei9�h�X�l��6�x�EL3�o`h��`]��,�O��6����O��aq:�u�;�N�8����O�_C̤F�P�U?Hiq�_+5�}��2ħ��o��@FWaf���u�Q�eo��M��m5����'9ŷ(>-E���$�#�C�4�jK�ic�u7��KOb�������$}Ph�=�۶��=ۏ���y���o�/Z��r�x�7'ƛv�p�_��b��g>�����3R_�7�a���]�����U�T8�[E߯|�/�E��EV�މm������4�̻��-����{�7W��iP�1�����`q3z��,�����-�9�l�J{�����߹ra������3������V-9Y4�߰=!��qA��fVz�oo~�.7�Á5��}�[�P�܋0�8f�u����^,�.�q�S Bny1�xAx�zRC����q�
��q���`��"���*��WoH{F�;^e��'~���nО�o�L�x�!�aPn�˰�y􂇾��R����{V��?}��ےN��%$�}��Y��C������:�"Q��~�f�!��VL��Ǭ���p���ӺKhw�g��	�|���[���n�@�s��A�9�#J��/u�|�Wi�9>�2���FoĮ+���W��o�'i���z���Ϊ1�����;~z����K������5"�Hw����K�K���iM;��+7��pL�q���pR��r�5=\՛��v,ƻ��/��#�Bʙ�sCE�ܘ�A�tuGX��#A�y�����q�������?��{��̙e���?�ZT�wd޸�=�����%V�����.�q����[�C��lȢ��ee����yܺN�,0y<�����5����V��s�
J��T9����G	��cnVkz[E��Q���jou���Y�^��	�4���n�Uy˲�o�p�$�����#�p����b��Ktsn���v�e��;���P�!w�jY(��;�%��_�/�4��A��Z���2j�?�@�S<�@����Á�3+[s�=��������?�պ����u�W/��=ՙ��ʃ^�����1��Kr,f���d������7`��"+�Qq��w���;�Eo��G}����R\��FO:��yc������b�� �+i`
endstream
endobj
53 0 obj
<</Filter /FlateDecode
/Length 4673>> stream
x��]Y�ɑ~�_�����,�Z�~�-`��X,4����F�QU���Ԍw%Mk�`ef�_Df��cs�sQ�����MN/Y�.?����ܸ�.֫|��_^���.�[t�Kc�a������/��?������������hmN��BQxi}�~���wwɗ���
��b��6�b���//�����q���/>���L�ܖ!�U���9�.;�Ƀ��o_�3z[�N�q��v�Yd�V����:���+$�MҗoL�F�ۣ��4Z�-�[��mf�2���ef���/Z�%�w��/0{��G6�/f"g�:.T_��?���\���@ �U��%G�����D�è�C�.��7�_���q�
�!S� Xgu�Y���2�:���g�tԡ�g�h^�3R#��+C�c;��j�,����.��l��a:kY�r���p�����J���1u�C��K�q����k����<X�M���C���CN�	&;�&Ҽ�?L��c�b���W�vL?H��$�E$Y�C^���o�e
,���m\Gu�{���p�i+)�i+��}��p�ĈZ��@����$y����Vu�Ԅ�.��J�ə�+ب�k��T`�BVl����qȰ��ͷ���<��%���w�ÉI"rv.��
R)�k���C�;�Ȣ���B�H���B] ���~��X�:Q7�ڣ͐@ɿ�7\��R�'*m����	��5NT�'*�p�@"���M�@Z�k�!-���J]E�]���Eǁ�Ӹ#�)����ܹ;�<�8<\HnX]C,��y���yHw����6�؀V&�@X#P�H��-R m�ɩR m�H�#lW(���-J m�HݢD���w%�5J�˹�i���5;�̃Q��$3���6]�<�H�<�]x�6��>U8� ������y\���,&k~��r� Q*|�5(��]!���bV�풌�}Br�6���p���A&�B ���<a ��1E��:�V`<f�YGNFg�Z�� -�SV�/D<����2V�j���@�{��&6Ŕ	���mEE�Etѱ�4���좣m�6�
[�\<�
�b�"S�I���@����i<ل�!�q����;��xͧ�;�ߌ��lL��߈
j-Z�"b(�}�'���pI|i �6���1�zMS�<Ra���B֓iĺq��n�VM�p�NFw��I9>��n��R&�ř�n�+A��J3
�W�6b�z)42)���P�l���R@��h��UqF��^�l X��ݺ�@��P�ơ�!H��n�
U���$l�a�C�Όu�=]�+ս��y���b����e�Cis�ձ�C7�ٮ���!�p} ���}���K���5��~������_�5`�����YrPP zL� ,�&e��%��*{�tT�ҥ�b�iZ���ĩak�B�M�����3�xw��c��_�m|��K���ߏ�-�oR�i�$�!������)�{ܤ'�? ԁ�7�'~?������_�`�Ipu���@v{=�(T1PZ���\d��d)�PF�y�Pd+4�/������>5({��V �AX�济+�c�9��O욛�l�y,�/�cH�>[�=�@U6�@q�`}H�  -���,y[�E�jWf��b$t"ޚ*�<���G�$��9�|���aEs�˝ �A_Q������ױ��47������A=Cs�OHs+�v�B1����rA-�����X B�G�ǣ;���MK<'����f���Ԋ#�+`k}�H7/B��v:x.`:mߤa�݅L�A�$�R7���,�5-U�x-�܍��IW�o� �<kJ���}t!�����A�R���A�ak�:�l�k�M������oM��pW���A�X���Z)�`��m�[����3�pR�@ذ�����s��T@����]cU�9g;Ĝ���xڤ�T�y�v"��v�lL;an�a
���i���=�%�44*�2�xk�'���W�2���]Nb��v��D��9��H����I�i�5��%٤��A9��DR������?�ܕk�!yb�z��f���>��=&��)�g����s�I&7�L��Y��Nm�)��dVEՃU�$��?я9q�R ���˱�f5ٸ.Q�)�m��P�mڵ���N�;g#:��(�[T�0��!�m����2[���g&0욞[�)x^�c~��Vi�v�<`>V�i������#����_�'3Y9]��^R}��n�R�|>R%�zD�UtH��nU:@b���Y�O�\��yg���98[������,�	�]o{�x/��{D���M��a��no�܇�k�z��GS�����s���\�\Χ*�Թ�Va�:a�������i�AI@MEB��*��&$-�в �gV7�{>�f�,Q^��f"��e�ژ�7�8�[��k��sCw]7��m�#�������\͇�����AOxB���z ��un =��X�Rχ��x�P��;9���U�<$��~ZL9d߹��Rg�%	���c�t�:K�����9���Th��\A�o ���񭕒�b�k��c���4��{�^w5���Op�1��\ �� 1�©̀ƯI�q����.�����] ���l�!%����(1�2Ŷ2fWr��)��bKd���B�Y��1D���v��ɩ��:�J��cʵ�����Y�^����3[)�Ն�-4�v�����-�V�O6�w}G�Z��%:�#��W ��XJ��E��+	�Ƞ�M0������4Uov��-���������I���romDP�l�����c��$o%i1�稩	J���9s4�(��jzt�,6��ǈ$,.�*��3|�S>�xWI0"�����/�È�i��& �Ef~���
4-����X�]E��T�d���1ݟi�TW�# ���5�ɸ��!��|d��{�1 \�������.T�/3;m�%�T��p]�����>�Y����z��w�Ӽ��v��6���[��l��TSW8N�����a����y�^��
�Xu�Yq&����bk���:<���?«�,���A�����S	b��p ^�2��ߥ+��X�TJ�=��u�OV�B{$��ȯ��!Ke)ȸ��S�0��O$.�=	J\e���by*I#����T*����W
���JDv���IH¹������rW���9���+Ź���!(OuK�G�(�y/�AQt�CH�r81��9��}�yŶ�����
�^�9�bA*ldW�@&�s0WU��EƆf'���%��l��jb�*v�ڒ;L,��R�g`������#� ���W�����|����O{$������$�N	;�t(I���=n��i�9�������W�qΧ�q�M��T���-�K�KVZ��նXeH'�8�����c�
���AbL�*��|pά9��&�՜r9xz�"�;N��&���	�;�%3���!>����q��g����MO�������Γ��~�&֠b��;����[�l�"/x�P1���y��3�"��J��߾��5�#�گ��O�,N;�f��>��
M�Pl�}�+�V���-3�*�F��)��V�]�@�#�ѐ�BZ��y�x)�r�X!���ӡ��.?��D�B�J���v���U���t�=s)b�YP_�y�A+r{@1������f:_ተ.�W���!?rk�=�QF_ٷ���½C��E�Ӫ��
YV�:�D.��ik�O�ĉ>p�z(�D���x��{�}3��5���?���%�n�KG��@}��C�~d�3��������=1ҿC��u�񖚘gΗ����\�����e8����X6ࡍw��#�BNt�^����w�W�縋����������a�!I��(��,.&����ۊ}�mke�T���q���&�P���"߼	��~�Tf���`+��CԘ�hɦ4�-���\��fՀ�qq�k��'x.��mt4�}����:QY��kr��a���m��pE��ӃJz���j�hH���:�����'͂`1�ڮ���fm�-��X��N[�]'*o�N���ٌsD�%��H�k^�o��,�<��ΆX]�9Ճ8��:P�b���i7$���7\�e��lX�u��n�]���v�D����xjVN�P[s�5@'֩Qz��E�6�4�f���y�u���1r~��\�Y��)��%Z�`Y��N[�Y'*o���wC�e��V�2ֹ�t�x�Gڬ�yf�~�u�������;��n�!��xR/���m~�9���2MK��f�����:=Ͷ�<���8�]Ч2�ն��r
�·҇o*���n�\��v�?�&�x�۾[�a	�Mik\�%h����r3��h���&I�z��%��:��Y�5�6��RElg-]2[����cJ�֭�7=���g݅�ԣdw�i�[ew��愌2���NFS����XkW�L�ɌE�U�n�3�Y:�����}������j�[p�c���&�JW����L���i^?�`Mf��"0�{8h�뛞���SS������D��T�e��`�%&�V�������9%?�����'���M��
endstream
endobj
55 0 obj
<</Filter /FlateDecode
/Length 5720>> stream
x��][�不~?������X,�鞓��4�0�,=������R�]�sLWwfN�TO˖H��(�kQ:�?7X��`�e����//�|��	⦭�����Ͽ���f�.�����(o����x�o������Q����=�MJ����%��K����//�5�x��7h(q(o�/>HeoJ߾���Bh���/�����/�A��`f�O�Z$B�oC�DЍ`�-�Ln��/ی��%�'�K7w��N�W̢�o��!�Lعb�s�-��ӫ����a���B�������h�(3~f�����H���M��V�.��f�4)�"�#��༶��Р���^d�^����pߚm(� o2�x��~0.޾��% S7��i�e�i��P�:a��g�;H/]n<G�2Fp�B2�K�|�t���Y����4�a�
-H�FAgZ�Xh���
؊��+�a��Ax����۟_\���W��h-M�)�
I�H��9?t�bX�S�6�f5�!� �;�� ��q�  ��dP��IZD�#�hg�D�14d�VG9�U���(��mI�4[@Z��4U8F�nT �Yh*:ҼEqUI�oT�8!@Ãʑ,��k��T`�F�0ђ��}Ȭ����j�rjF�Yjp�j��Ub�(5�.3��6U������+�q�.[�����/���!����L`� �|����~3�Oo�J��[@�{��BL"�H�iڸQ ���� *ڄV4B ɠ�RաQ�1@4�� ���FG��$�)@ u��D~[D�4�Ll�49Xk�|����`�E��K�؃;�P�+Zܳ�{p�22����ǸŇ4�C|@�i��6� �9>$��OC| ���?C�Tቤ��C��@� fZ�S����ĈZ����0+��|�,�ĉ���j��4�"�&n�F��k<��oI>��G0���`��T���z�@QstH�):$�*: UN�!���hSt ���C�M�!�V�!Q��i7վ�ѡ|�C�&X���u>Xuas��"��#U����~��-���=�q�����x4�8�ct ���J���E����#���dUG�:8 �.��*}\$�R� �h-@� �1@�˩�f��u�mN�Wy��wɉKTQ�)��.�5N���u�2���ߔ0|�����~!�OG�Cn�x��\T��i@�-��N�F'i����-wCb2$"4�A;
� �ᮢ�d��j�$R�"u�.�✅>уTH;1������}���p<�[���D�օ�� 7�D8RZ��~(�@�X��T́��eURQ�ׁd�-ZP�# �фH��ՁtQ�,aa<�B�H��X��j"����
�����u���D�����#��Z���)�1(�q���~P:/�(ɈE���:a�����I�x)��d����8�m�Xp���/�*�+A>���͖1��՘
�Ƀ#a�ە�؁vA;R�-F%k",)��J5p���A�B�U��B
ݺ��K���G�#x��tQ�9b��������"a�fҞzSD�`���4३��Y�4�Fj`�*a��Hm��jPoج]p�8��Qs����Hi�Ǥ��W~|��^���Š� C����s�/��tT��4m�i��%�0���^^h�uy@��ne�?PYN�!�[t8q�v�OY �@����e
7�����Ȫ��"l��Y�1Q(�i��h�2�>�jz/8FrP��D{�ApZ���<&N\���g� ���� �df>�>
�!L�rV�iI��h֡GAda^A,� �:�]9�Z��\r����&c�8�iֈ�ZͣQL�����x�f0���D>E�1󐥔��Y�*Q!W�,�.N�Y����{��Ʒ�2e��2ntu>�)X��A��пt2š��k�]5K��[L�9ȧ���}���p�RD�2�	�)�tH��^�w�^�w�����O����a�,���}�7��^k�Y�Gdau�.��Ch�PB��y�]]Ǌ g_ ��9����H[�S.�|�!���d�TNC&��EA
�f�E�`�i�.��S!´�����!)@oB(�Oz��$��9r��5}a��/���|�.p[���Y�8�Ep��4$u����y�nkC*:���v�O;=�tP[,ރ���K�������_�����
�XI��Y4"W�~�%���+KԺ��n{bׁ���o^{b�I����>��}�CQ�1�}���D!eɨ�D5nŦ�	����]pf�}(T�Z)�0ܶ4#MW�|}��L�v�[��2���c;��2�p��OCNpw:Q���z-���w!��:��c��L'{���t�1��z��kq������'�=��Zz��	��R:���0�+��V^w�7�f��4�+ڱ���o�u]O�F�-�;O�����0AN�������)p/	�hbI3}�2�M���	Z�"e¦Tt�p��'
�bM
�BM
��5z��A����oG�t�Z�TtZS�ב�a���N4n��)�hg.5�L4n�[�p�&����	QU��;6�+Kwp@Wi��������Ӈ�sއ�K�a3kȉ�AA'�E�TP���8T� 4�DWt$�0-Ŝ 1-+5��(h�lnU�D#Q�I#R�I���6H�10Ӑ ��!�5`IU�4}Q�	#���hH�X�K��@TQ�K�q������	�`�3��*"�F�I�Q�	���t�j`�)a��Hom7�t�����f�*%��7[�s�,�P���2i׾r0�w+���,��@ٱ�@�Z��dQJ�::�P���j��G��Q����ky�FE�X��6�5̮���kS���Ľ!]��y���j�e�ֳ���q_@�x��̐c�����#�Y�a�Ґ͍AQW���Z6�L��O��ٴm����ƝFl0|h#E�i3�ȋav0ur���l�C��w��D5`<�D	Z�E��yt��L0Z�����Q���c����G��̻<�VtM�	2�u��<�Td[��˾^e��m3.Xb$b~�g[>*�/ 5Sj�:�����@�>��:���Lۍ7��+�������昀LXd�zP��a"����'yH���1�J)�iSΩ��+���;�g\��E��Sˡ�D
o��{R%�"VJ���iխ����A*��kiA��x�N��4�E*���f�%Q��Pr��v�^��ꤞ����5��h��gd���zꜳ�2�ځ�r����$G5X�T��p�]C��x9����	q����&�g��2q���5���D��| ~k���&v�
~�x{�I�G��1XҟK6^3�XV\6�v�o�����*��UYQ�	��x�I�;���T��\��S�)���!�[�j����h�#ߏ��B�]�J�tH�.~,-����j?8L!\�����Syk3���l��=6"��=�3��`%^N��.S�x�Z^j_���Q��}U�X:\�,�]���Ǎ!�[_��˲��)O�ouig/�Y]����h�h�n!iŪWN��1�Zٵ��U����%�YWљse�Z5[��R,뉋kai�_�*���X\\��?���b�H��ı��/=�|}IUsH��=[��������G�J�ZjM�wૌ�H9
�"���PO �����1�@�t	zT
���o���2NVi�M��k��F�@�F�P�F�Y�I��u$n�#v���T�hW�}�f	v ��we(���3�}��U`	�hy�0Ϧ�V	6�4�*APW"Z�>$�pC�ەm��n�m���Ix(�ՉRv|-%➀C\mÆ� �?=���HeZo|$�U�6����T$�o�H���@Q������6L����R^N�J��M~
�m��0���R/�oz~hTz@kIo��^;>Y��`,����s))�7�F�o!Q�/����{�MY���4��&��^�A���t/�B�Ӌ�	�%�m>׋��&��<�����%�[P�M�W`yeTc/�u���ٰ<�˻Y�����jA�g)�m[�V�}\�ؕ�ѿ�.e����cb`2�n۩ϲ�YϨ��ѹ֭��e�>�����|����3���֒1�gͽC�'* ���0����!p���8����Gn�t"�L}<�`�Ȉ(s����=�_�n�x]o��R�v�k-���+����cT�\������P���@Zg��qmK�B��:��¼��>�8Qhe�TG��̓�+[��(Y���6$�8�t��4g97�1˄s��::�J݈�x���A��f'��!�xrr�|��썚���wh�n�l/k'3�.��IߋDgc)В��{9!?�c�d�2Kq�t�.{�����tҧ���5.������Ci���|�A�UNҠ�ئi��=Y�Ӡ;�_��N��v�����ͪ�g�A��DҠI�Ҡ��S� �xL��A�NN� Fn{d�i�a=�A� ^'i���_������[6���5K��܂������ݫ	�,�^�i">�>��"l%oN}$o�*ys���H��SC�[k]���sr�v�z�u������]�z�M�ͳW�d��Z�	fzHNo��x��yÓ��T��xZ�0]�� �����Y�G
��^kO)���ӳLk[�����ٯ�z-��dG���ɔ�|J�s���5�
���C_�{U �����"��K0�I�wˀg�PU�XoIpB(�~p���;��q�G�'��9�Б[�3L6.A��v�1�0�6���6�l����s�Q~|�M>�1YǄ3�|��;.α������6���x��F�t�YG�Gg�d]�0J���5?)��.�t��8�e�>H��Բ�:�͏l��6X?˶��E[�l��jK>���NV���I�ZK���xNŖ��/�dl�d@��,>�[R9��O������-+i8
.�۲�TpI%)N�1�c�-���Q�R`~O��]�c�q����q��w�����U��sG<�����p��L¦�"v��;�}������mR#z�XߢFī R#ڐ��FԹ~R�Ȳ�<��FY'�R#b�׈Z�WԈ���~���8��8_��upu���Xz�����ѝh��fd�FjG���7���5S�ʣf�u��v��:c�(^t���Y<�>����ҚF;i�H0�l��м��!�[�p<ơ��ޱ���1��{�jGy2�A�ѡy�y�%�3������ǌ2���M\S��s���W����W+f�ƊǬ���7(6��O3��w߬��;�.x�G�oP�`V@/xl��V� \?��A�a+x�FY��\���<z�<f��*x0�x/x�8[��wpq���XZ�������Z�3o��'�
����v�'�Η
H놽T��:_����\*�P�҆U'�I{�P9�b6�32{��b6ly�ᅃ��̖��[̳�7�ρo0�S�o\�:|���� �ߘ-�	��l��qQ�O�ZZ��8yY�6uē��/ݙs�<�W���� _m���-9��j��W�{O����gQp��=*�z��Ш%��^[���;P��l��Q��Ks���f��c*���(�T8��L��Q޲ņ+s̃yI�k���ۜ
�¾-���~ڒ`�<U��Ữ�?�	G]_�f}}a#��(9�������:�? ���V~
endstream
endobj
57 0 obj
<</Filter /FlateDecode
/Length 3848>> stream
x��\ێ��}߯�s �}� A�h%�9��|�;dv�HU��4gv�#qF^hW^�����Tu����jl.?��oV8LN�Y眖O�<������b�����~�矖_	w�tj�=�G�P/���?.���??��]~�_�/f�hmw�SA�Z?Щo?>���-y��uT$ԋ�kL������/V���,������Z0i�-`U��}h] ; _��������'�V�S�u�b6����U�ɖm��g<%�IzI�x��ux�5YYZ+�w+�z^�
��#������uX��E3�Ɠ��@}�ە]�����ٛ�|H+5��φf��QU�^s�������>�ZY����K?��.����L1,��'�n�uY�q��y�ĭ��:�����3s�� �b4M|:��'���Bk�m�m$5,iG�V�I�a!%n�Re���Ga铋�c<��O!�q���Vk���	���.�>�8rZM0ف��yK?�c1�P��J�_;��1�L�*�<�ͨ���L�Ȃ,�X�qm�����'�XX�[�B��X���&)WbaA}�&O�3I�J[��Qv:�2f��i�!�b�ް�κmX��ao�67v|~@�解�n��D ��&)xp�=]4�)�)Ә�)&��d��I�L3���88����1�.�LE��5$���א���\�/����`��#(5�Ĉ��I�`l#;�I�m�`h#�ƈD	oqZ�c���i�`t#
VcD��cD=�cD��{��28:v'@W��P�T�f^g������[�|�`�
l�#�����&F(��,{?�������y23h^�� Q�M� Lo�D�N�DA7A�b=H��$��$���H�[p9 ��K*.<�W�eN�`�*a��0�u`�v#��&qx
�A�5(|'A��S��dya}�s� �m�D�6Q�`��9JJ�s���K���M� �l��D���D��n�D�3��Q�MQ�a��.'��O��Ĝf@Sg�+]�iR5~p�5�I:���s��4�G\�����l�C��E���I#��(��7qҜ��&J0�9�\&EY{��c�a��m�(�|4�D=��D?=�w�>'�wvQ���F��;̊NN�N&N3a'd�N�fF��W%�a�5,����%,�cﭒ����j�f��$�0!Л@:�.:��kP*م��t*�_U�YH�a���,�'���&h��굋|n *�Y	L�̑?�D�����ܽ�y�����Ys��b���e�q �f�ʳP�*b�� P󴋨�VRJ�6�>O�}�>J�4�\*��.Pd��m�Z6�C�A��rfS23V��|���V�X�Vډ��J"���D��ad�2<QB�IVW��'�R��yI�sE�1��l�3�z%
k&óc�LRN�u,�6'����S�f�7��Jb��B�ïT�՘��[�nBCa�'���P����4��au�xJd"�6��$��������Hi�����i�]�M�m%�@.�
l��r���,iK���ٔ���fN'�bE�AZ�H��.��V�!��&a�iAl����c�KnK���>�0�ҩܕ�ԍ��K�B���>��_���oϿ^)�H5��EJ�U�(�2��֦��^�wt���o��Ϯ����=ݵ?���|w�<�0�t�Y�5�v>9��_��_~ߝ˕�����}yF��5�|�֔UI����f� ����.L�'�Oa�x/SPYk
ʖg����k
\N�M����;���Y��G��}�ɞX�c�:B���	S_-��d�YJ��?�(w���7�>u.�� �XC+6�����4�5��l�Ǯ�z�kL�=�ӯ~w .�BT��L|%����d~�(Q�T��	�{.�E�^��N�_�7�܎?����TR��H�.*i��ǣ��q�ׇ�Y�;�Lgi�۠�Ե���9>R��rʣ�x�����)�����Wd�H�.Z��T��T���dr��`�)게��S�qU�i��H���� u��-��Ǧ�S����JG�:E͵���c�6UKM�J��+5�@�?"�T�D'��
�I���3���U�
�����(a$�sf�0Zj�*L����Y�4l.2�L�ZX�Q�>(�XR$���g���d��͑�ή�JSt�>i�|G5"ڴf����E���Sq*3EKA:+.��:HllH�$Ҥ�gR}-G��՜I�Q��G}Te�� V�SX["Я��jK������4��F�ε%��^}rjK���c��R���R���-;�0���$ʰ%��ѕ;��/�-�H�wԗҸ���9�Px�Zs����/���ӡ>�w��et��Q��頵Ӵ�MW^tS�KEo�]��Ͳ��4[�L��Lc����(�(Pst_җ3��ؓ��v��5r�Mx>��ڲz�ə�_���'MY�������>�v���H�5Qvmg�/Pk��^��51��"t�;�c�]}p�r]�x�]���F�5l~�L����Oנ�a$��o�d����Q�h���Jn�m�)��o�p��=����Avr�O�	Dw�)��;t�t(;H�
����wD$��5�5ͩZ��	V���4O�x�o��N]�p�춄q����.`(��W.?�-/At,��b�{(�t����X�(�Tͅ�[E�u��\��Q���L���2�"��~���������kP/�%��9�ԃ��עC\�����)�"_̵t��O�z��c	0U�P:F	�c��3�5'�m����3~��<�C����=0�����Uɾ��&ɾ��l�D������tF�i���d%|�t�?����W�U	��Yx�Xn�M~���	?h����P����I�xc�z�ss���|II?�}���^�~t�]����Ø��e�n�~U�k�o��t��|���_��lze���e���|i������|�d� �Y>���,�-�|kn^��1���e�/��6Ǘqv��i�/�߮����$�&÷���t�_��MIV�В>v��1��vc���ľMv|/�=��.w��l����=����"ϡ������8R� ���->�MC��^�?�	t���s�<�3��?�ɘ/�6�|Ez���X�h�N�c�2�UDi�����ʘ/e�"_��t�w�7Q�Ӣ����r�(�U�$%�:{��w��׉G"�C0|���/|{#�jewFޘ�*K�!�̏�m^�~��Z_�P_;��v��*Z�/L�6���u�ηӍ�9j��eמ�w�q>�0���p��	����y��$y�%u��Nd|�x��L�"l*�D���C��<�����*��(�U9��_+"�F���kE��|B���Wq��_ʫ�q��ֈ���FC�$�4�yA�M�߄��L�!r��J<� A1�i���S�6H�Vm��6�z������C��5��$�W��-�?� K�4`�!7�~�w�7��#h��yk����AO�S�asav��5w��{��5|>���������.�y���戎���rl2���v�I��qD@��bp��#W�9�Ƭ����#,���.@�97�4o� �.�>���x�8�Ѱy{� q���� b%G�)���>��#v�h��Hؠz-ʵ���:P�dF��,Ӱ�-5
ɸ��	�+��ˊ�';�%h� ˼�~H'�����HZ�-Ҩ���U͙\�ly�{�����W�ˑ���l�b^�h�'���ߙy;�A��?���7��&�4n[2Pdi�g}	��qH8���/o��~&.�����Sz�׹�;�"�c�4Vn��H����:S�c1�t���`E	����^G(k
endstream
endobj
59 0 obj
<</Filter /FlateDecode
/Length 5056>> stream
x��]َݸ}ﯸ��p_� ��m�9��|�dC�	0��Rŵ(�j��r�ɴ�6��d�$K�M����}���`�e����O??���q�V��/{��on��٤�[}�a������[���?~�}��R>ꛔJawO���p�����dn�����Q�P޴�|��ޔ�}���wBh����=8���_o@PaO0{�O�Z$B���2t#��$6�ɝ~�|�q�ۦd��s����� �;�����!�����q����xa���i�X��z���43Z(ʌg��#���AJ�9�cnU�,���vs�Gwc��K��i��k̦���C+���E]���ݑ}(��[��zaa�/xa0"C�d�78m�,4m�E��}��ۏ�:H/]�Oo^�3F�B2����WJW8(���+M�qx(,ThABw
��*�Bs!`c\E�P�_��Av��0��\���^mZK�oF��BG�%Ңu���6�T4�M�Y�8H��{G�v1n��� M���Etq�7R�vV�$X�"��8�����@�
h�F�E�+�V�m�pHdÍ
�4�� 9�<�y�[�R���.����àu�i���}�j���-���
eW�]|y�Ro��T��>���YY%N\%���e'QQ�D��*��Y�:�j�Ō$�|�'&�p��0/��)��� �������~ei��놲��=il�l3�5�q�H�v�H��]�Q�MHڧ	��Ř'B��<��}�@�1O u�'-����|5�L��t9xl|����E�!Z��C\��+z�i|��l�!�[f���d�!O e�'i�'m�'��@4M$�U�
�hRא&��i��k�*<р�1E$�I�i̴�"�UM�bH�v�D�[�n�☍��I��D�M9$h�It]�0lV!�Z�Gb{e��ޒ�[2�?O�_* �W��QB��(b��H4m��N��F���[�D2�Ts@�m)���!тܙh.�1;$�.;d�M��kv(WCv(��K������.l�_����=DS����E�]�4��eh�W�|�6���?fD'w�I�t[@Z�v�V�}v@�+S���]�e+�����v�H�g�Dk��Zv�cv��S'���Qa`��(����P�"�X���!STHc���Fa5
��b;�K+��\��r��u.���i�����ME	�b����'B{'eF�*� �l�U���(dHT�6�@4�T��O�D�5F9���Ix�0�D,Q=��}����P�.�K6�o4�(0m�wCk��Ea����Gr���/�!`@Ń@�o~�w���`�T��e�A�"mq�(#�kt�Ƒ� ��Y�½0�@ӝEN'���`�4}d�M:�z�44]�po�m���v��tw��3t��~�����C/�Y/��uڻPV�a�BZP[��"v�F�G�)HT�"r�s���!R�E\fGj��G��̔��:VcS)�cu*�!�[*o6�P�m�a��!�Y����(�$,D_��JUח���c�-0��1,��|��;����-N���.��tg��0�ISA�C�%f��
	xi:%-��� �J+͠�i�M���ToZ8����8��y�E#���ٳ���p�lp��h����29�8{�`b
y�=��5�v0?D��&��'�y��؆����RG�=HӅ���~������.��̅�P�C�j�����Y�@���L%ܽ���0�.�q�����%��q�}�C��:�^	ED���Ʊ��,/P�L��(�}���g2��}w3��\��Q܇�Ql~�8��0�(ar��STS
���u\����]p�~X/� �nJ�֭��kݓ�E7�9'�~�{,J�y�|,��Hh�HUGq�����D�!�in0��F6��{��U��W���W$n�[]�Z|<���[�A�q;��_��S�������աz���+�$N;���s��Z�5r���:{tAw�F�ɉ�����.7�Ӳ�v�O�|�]�H�\O6g��	�"{�7��� �{��$�B������6�g#_�� v5��^[��SV�l`3$�)G�:콝��.�m>�ZD�`/۾�� \ym_ 7��X�` k'椶JOx�Rr��	�J�	Q�7c4lO�غj6v���/�pgB��Z���{� ƶʞ��ZB�)�c$�[75ߕ�܉��2�l���o��©_�� �F�^�~0�h�=�u���kH�fs�Е�Hy
?	ۤ(l(��aC�
�(%aC�>ѱ<� b��l�0����iijmb�P��(�Zi���w��r����sGM�l�V�x��V]}h��7�f��D�E����pQ�t2��������{ �+G�5(�J�uݓ��f�E	���Dģ�QWh��������+,�`��p�P��5�07)��E�T,]#�:J�۬���xE�V��8k��!����i7����PR"JCS��a���+�ܦu�|� @D#�c��
��@V �Q$��Q��
h$
�6"Z{�n:F3��O�!�:E���)�k��A(,�H�ɺ�.�ö֠�@r\@!C��	� ��n;;��֡��m�|���]:xA��� ?�a]/؜i���{3���v�u�N�MA����c_�>���_XFt�ײj���{j$�KH�0q�l�H���E�OE#�C�06����M�~>:C��#Z���v�eg�8��:2�${�	���a.�~� a�;O��Ӆ$H������(	v�� ew!	�fsFj'nKI0��������K�+��
�}��"Ҥ
֎Ȍl'D��F��o�	|J�~Ä�0��C�T����.ꆜ���M(C�.�$�@���R��jؤ
���V��
sE�
� E�o*.���%@Uk ��w�U-}i����@\@�`�@.X�`)pT�T	~��[�h
�J)��h#�UH��-����<��n��u�w���+GtK�\�F�-�ₔ��$���m����s�oC[��V�vL&،'즒(�Ո��;j��� e�cQ��Z5�:�\+����,�wf����W�U���A����� ���`]�5�Za�rSC��`W#R�����'�4C�4�Ʃ�T^�͐.��)��&�[W~�ͅ�
s%Ӛ���}n��8�l,�3�	�8Ϥ��tj���Y�~3�56�۝���Uv�u�z��s�z��1(jߔZ�j�D�}|�G�WS�v�y5��X6��������Ұ�tu�N�
�H�g���x�q^X���ղ�=We��Q���]�Gf�|9�42`��\� ��Eid�ӒU��]�g�jf< �ݻ�U�xj�� �i̦�C����������\2��{f/��lؒ���O��\���g��Z��Ly�x�d�j����]����g�]xf�Ǐi:��3[�k��AW�
�T�y&e�J�4�-�_�3�(��3	6/�.�����gR�Ly�1W����L�Х����3/{n�zf%�N�&O����j�r/ux)�
3��)��ۧ�bm�w�Py����h�L�%���� "M5��jJ�լ���zdܬ��U��_�%����d��`�;�s2�yty8ϑ������EfVĠ�	M�B�VD�(=љ�M���E�`�#I>�A���~)�s��(A��c���E�3�<S}tU���T3�q`'�Y��'��㺰I��5�����_`v���7����4�j����3<g�r��MB�Vw������ˉ�[mU�6��)�x�r_1��	���կ���΄/���:�*sJ���ևq����+Lsf)'����$'���f�_:2����x��)�|�����h��ɚ���pm�+E^���xd)���3�ސq|��n�������+�X~4�����Z┇�/Y�X�/����KI�'�X��"��0��zU-���pEl;���мثtu)ga1��'n��=�:��8�7'a1��: �0��I�7LmmA�}��aED�t�บs �>�8�
�vU~?���U/�/;��j75� �C���Փ9!��q]�|Eں��k�*�Δ��lwہ\{���OǮ�,>�x��XD�-o������=,�h�Ⱞ<v��>��-���3)�S�i�Bo�1h�<��G�ўX��V>sq�͌���Ê�ZoWf�������Z[.��U,��a�]~����>ܿ*ŷ��(�˨Sc�V��=�E��5�����t�l�q��������e��t��_��9K6n=��Y�]��
m�@����y���rqH�nfս>��Ke�_v���/;��a��r^X�^��x=�;.*���c=�µ��}F��l�*�έ�Y����Z7l����ݞ��.Nlp�'�B��|2t`��x�U������5,6�Xƶ���>�]8�.?�ŁQ��b�),v����ե����πV�g��H3b\�^���gf��7g͙u7c��rnfq�笜��xA�� ��A	��$�yw| Am��'�{�o*6|Nߙ���ٚ���^�^fe�<��Z@ǽZ�Ș�[�$�MR>�U��\=�*�=n><�Cb`3�u]�֗=�9�v~?>��ɶ�>���<W�?�|���J���M�R�"���3^�x6�x��/-c �a9�[����ذ�z�Q�����)��9x0�E�f�7l�-~�tƧ�lc}�o���0^�8�x"�i�VW�,�`wy��
v��b� ��Ո��z�ݯ��(W���4��)_���Ĺ5���:r�:��ٲ����m��LN���:��"���=���ȫ��(..�<�Eᗽ���5PG���ۣ3y���D�~ƚ�H�u�@�e���kî��Y_۬�����2%���Z�oY.�e����>�1Ź"/3��!��d�6����53����^X�<|R�D��
endstream
endobj
61 0 obj
<</Filter /FlateDecode
/Length 3871>> stream
x��\[o�~?�B��px'P�z�ync�?`ۤ(� I�?�^��������ٍ�I$����*U�?��?߬��kX����?]~��s��X�a��ߗ�e�q���W]꡿Æ�П|���_�|��Z~�_��� HI��A��|�����'�����(R�r�� �"�����B(�����ϟ��  ��ppP"~�@TLj*�S����	G���c���� �7FV�MFq���3ʥ�ţ�3ћ���֨��Z��ܑ~�:1JHN���J�;���`WK?z�4h��j��f�j%��!�k��sH�uc�h�:8��y���b�-�}H�"]:X��Tn�3^�F�7��H"h���
2��'�!�{B��Z{p`S�:%���}2��Z$��K�
�Ɖm��M�����BI��y@��R҇�Y�1Q�+o����������\�{��U)��eB�*�.	�ZW�'�J+��J&aF�c�0g���m��ɇ0��3)�D���[��X+kdՌ�o�
5� aEǩUQ�˅��Ja��dQ,� 1��L)>"),�!���sN��>˭Ȉ�����N�)��j�J/\��u�#Z��7/n�unD�[nn� n��Rf��7��1�"�2E�ܹ����pw��c����
~I�Q4(�1���0����`�����r��g��	-:Ln�耈�CĆ��Mt@T�5��CĆ���!bCt�XrP�؈�!a1:���]2�L�vɌ�ά���,���|��͜�ʧ�\�"sN&o��U3�۫s<�:��!�����!BCt���D����a㜰Mt0Vtс��N�!	}x�(��C�L
�:�|���q*]r[k�s�,d2�%N��7~�'�p�)��$͝��;kV��[��P�
�C�:�9M�l0Cl�Aoba��r���������16X�}C�]l l��m�����!b)6���]��_�:xgә���3;�C*�ܕ�|��)r�l��N\4�}�h�D�q�Q�]l d����L@ĂQ]l@Тxh����31�$u�!�!��U������Ц���PG$���ć|�Ň�:���-�8F ��Bi����t�ys�*"�9E��Řę3V�0�-*d~K���C�{H�S���w��rz�Û
�ihρ,�ji[�� ��͑��6��*�	��2�� ����~�b���*������cP,�ۇ���!)ۃ�g�V�]9�bޕ)cklm�P?NƨlX�3���#�3wh��z&@5ab6t����0����r7�T�s]|ʖ�TW��[�[��}���P���·�8�ߙ���x��pN�Lsmp��u�e�g��'�~L�w�-���j���ێf]u�ծoc��b���óӮ:ssn��D0��¡`1#w��n3��Ϥ�P`���M�(Ct`�"�H����^���kj����x�a��6���&=�7[�1g�Np$R�O���ʤ2�ɴ�Ԃ�v2���`xH�<s!x�����Ƙ38KU�4b6�rg�5"�)k��a�8��}�w��ى7��F���v�_��1�)0��꼗�R/�6>���c�/:'���#���b(���'��i�n	�X���L�i1: F��>(]I}�'vµ����Gb��G�Q����7�Z~�`Q�� X��� ��⡪��i��6��@N��0�4�������H,U`@����hIX�VNȏ�vY�pxO��&��,vd��b0���k�!BI�0�{��ОR��e�#T�;�ǒbیE1�� ֋�R�6��4x�j+1b�AAb.�h�U�t7�ĒK]�u�h�L��
FZ*Be����0MOIM����{��`5T��1IA'Im���KV0Bec����f��Vӥ�(��6AcB�`���j�_U�:.�Z��lK]O/��i�J[J I��DSJY���B�f����[�Y��(���b�D|�V�\e?��X��˥5D@�}h���@�dMiY#Atm�J=f����	K���*�i��J!���*�
"QU��y�=�j���*���ͣr��L1��g;W:W�����=2���f*�t:�KW���1Ĳ#�k��h'��ڸ�3�u�،�j�D��ʇ����ZhIg�2)�ؼ��J8���?�8�5��n�8�eY������.h�⃦I�f�`��Ar�O�v�Yhzd���,��&;��l��H9�!��P���j�tT�������Xkc�8*��b��SǦ��f�n�{Q�9�P����G�|b$<^���۝ni��N#��E�3V�$��6�̊���DR����Y@���zw�C"���)��l'�I�R�F>G
�0�|PR����x��И��H�F"w���h:�i�֤D����T�Cܶ��\sSI[[.ԍ�_}/���`��C��=�=��:��L�2��Lx�\Sh/_�S�a�S`^����)���6�����U
�y1������	��?���,��
@�Ь������Z�^K$(y{��� ���İ
��j��"e�KP���cf��xV"��1��4j�++dW"�I�����^��fa�J)r��YIE��U�{뽩��Ѵ�(njo�m�e[�I:5�LW��}�G$`�	�X�#$:��E��X}�x�G�

@t��fM�xXA^�ƭ�b��«��i��V�1.[�'�*���h�*�-�#��b� �:v٘
�:$&.=�KKM�%`y	��!��:b�V��F*{����;��]��@o��&?-.�0��1ƻvml���r��y2�%�>%���T���WJQ�TJQ��r�\����K���H���䚦�Lׇ<��Y9��k���zLbᦢ� �ʜxf$ϔh<��M&zrQ��?&�-BNX�0X��{Ń���!{qV��� t+�nq��ܻ9)����ނ�Ud���0�iD��9i�.�
YQ�~ ���Ӻ��}��vW�'�g`��7A���k���a��H�i7l��������T�l�X�Z�.\a�M�O�+8�tQ�eFq��� :�A���NX�d͎�B��x�EkN�_=f0Ep1{a�rm�`�Ô����ׂ�>c)3E���o��1Q��O��h����ļ��K�>����8������a�0�Kn��s�A��+a�u}PFR��N�����0|G\��2_"�����$���b�%k��z�f�ϓH�G��6�y觬�3rd�O�� eb�����p����q$�~kap�\�wk��Jx]C>�5x"�es�l����X��-n4>�X�x�����q?��#�h�H#;à�	�a;����I�dZ�1˿a��*an���#�HC`��i�̶�8���9~�bc�Z�e��� W�!E+�E���;��+���2�ԳN��l��rb�\u]�d���A�:;���}�$�G F��'I�3w[q��6�?ð�{N@����~����?"F�-����u����5�0���A���M���}ؙ/���O����<}�9�Ntgu���EU�����t����h�0ښ�e��-��4��~���!K�p�O>�ꂋ�~'����-�W��=�d�ƜJ� �A���ѯ �����C���}W�] ����v��j����-ÇO;&c�O����ž�R���@����GIz�����Cs��@;S ���sSd��������,�:��o
Ê��k��p�<P�턓�l��e��ӫ�(lsʷX�֍�S�晜S�RBP��9��)вRI�~ꙏ<�~J^"ZA��D��Y���Ǥ
endstream
endobj
63 0 obj
<</Filter /FlateDecode
/Length 4058>> stream
x��][o�~ׯ���px�(`Kv���p�� ��:��r�{�ݕVV�J��s�,9W~^�d��Ϥ��w�x-��q����ow���QM�)�~�����4�Jt;��GC�Ga�?�a�/~�������R��5w�S�(~4��G������p��u�$�Ʉ9D�n�f���ݟ�2�/ӧ�y���?&"�&�5!$BXF%B��f!���͝~�t[p�۬!!9�5�b�}b�ʶ��`ք�#�u�)�ŋЛ��xk�rk��Zܵ��qa��R��fq�_��ow ~��c'`�kG!��͞�half)f�_�f�EU��hMC�bP9�g�H�K�D�C��d�*����yt�~cyD�D�,��xc����Q��9ea�̭#�?3c�IDB�d�C�����4
Pj��/M5���\0�<Th�;M���Xh>Fn�I*t�>I���!�J�P_~���w_��l��0S�SE�LC�}�{�����i�ЏP�i����q��V؇iuVd�Q豳7S��N�$y�
2��8����r'�g
Ya�&�/�]�>KJDOV��>��4J�-�H�l�D��A'LI�@}K�'�Q!{�z'Qm����LK�v��6˛/w">��E-݊��ج��^��.4oCb1�9Ւb�	�����F��B1�?����!N�?Ƅ�:�	����� ��� ���B�9J>�#������5F$�
#���aQ5YQ�H$ˣWX�i+� �1"�V�h�H�FdZ�`Dy�aD��(�]�xm�e`W1� ��ȡ��-�T��yՊr�6{��\=#�|�`E�q�v���@�L�6v0��1�l�V�@�i��,5gZ�q>b�~L�S� �h@� � ��2�j�2ܚ 20��"|Y�Mc1�i䐩&����Z��9\����>�0������~<��1�z�0`�"hh
a�v�;2���`b*��
qV���xD;���)�9�Gp6c��)cj�ܚ G2��V��0$�)��-;)���>�7dTN�E4�8S�qդ9�|Dκ�УѲ��e�$�|�	�E3���hf��q��BD;[@Y�"5�In�>�R�""%���U�Lt�~�<���������N��>!~�Pt^6Z�^.�萗��X��;A���қDS�C���e�ڠ	{ �9Xs�MC�C�b�>v�8@��^��`�eJ�x,�+�htGU�?�١���3V��$cM1�h)�����EU
-,*�������&.�,K���<�6a�<�Q��c����:t8	�t�mS�,��&P3�n�iv�{>�3�L͉B~��}���9��:�n��ё�����;iC�C�Rn	[^Gg˞��@�R�������Xh�~�_�w{O�=o:����oG�{�mBoy���/X���G�s�y�U5�U`��CQϳ赟iA9�z�Ndw�y�&�ӕ�)JN�������F}̰���"@����6U~�K�'���CS�{��2������<O�E�8�O1K������҃�_��l�>�5�9^�s�b�8���c��|;��:αXXp=da���s*ʵ��^��@�E��#K�CFs;�~1�ep&0�|ڽ�W;;/��'�&fvI4��/b�vU����*wADX浼�{�q���x�uӞ[)o�­�JĆ�ʯ�b��5�b��c.~D�#�N��*w��]��&����&�
1�����Q�sϯ����"�I�]�=+^`S>I�2OI�E��{fd߯1��y6�V(����L��u=�MF������v`�$�pk�=1�S2�j�5鈏~�ת<�.#Y���<\�&�$��}��?)�*814�ۍj�O:D7���7��|��R�Ƹ�Ll�<��HG����Q�6��3�ޓ���vEB*�!��.> �^Aŕ�?b+��OYϚ'�_���y�ʔ�����D�	���e�=�j�t��� �]O�X�9!n����8N����2���E���4��6��Sd�ߞ�ܻ�)P�΋�M䗹(7��1?�i��@�DS$�̂m���F/��c����Bײ�|!��2��/,F=�0��J+��물�F��t�ɳ�#��~`���|��y��d"�+�{_�2 @��i��`"�ߵ�i��(1�ɕ;�i�������0�!vq���1]�ͨ[?�ĀQ�Sk���3����D��&>a0t\���=����<T�A���A��=�u4�rD�סL,�� a�-b�I�`6Q`�j��ϛj��qW�n��a1�b��-����H�,s�ycw���Es;��g�6:�������olڄײ+Uu��Fw��utx�� �:����C9n�k�t���3���C�°����p��6�s�(m	� *�����îN�+��A$�m8��p��,�b,�Y4���5��q��BZJu�>�BFaܳ1BC�|c|�X���]`��Q�7x4q���T�N!<b�C���v��J�hmI�@���WtC���¤���5�ݮ��#�4�	��'�7P	0�x8���.���9�C@r#�A��9k8=y�źnFM�c��j���yi���^sGU��[�b	;Z ���ZD�{��<��)@NZC�98f�9�C *1z��i�	�(}:��8 >�)�u��5lr:��]���~lpF��7��'8v��=.���nmλ|'��$��4PKe؉u(��w�K%��T���8L΋;��jH<0f�T�g�Z-ǚ��vv�D��e�,��m��~�u���@����w��H�-9������Y~��pz3w� ��B;�1{����������ơGǲ['w������6y�[�C[]�P>�\�T�3��!������w��&
{'�+��EB���ˍ�<%�9��3"��ȏ��;��4քt���e{��X=��� �u�C 8��q���Uw��j��-��#�	Q8�>�C��z8��P.�C�p1�a����Ӗ=R���s�QO���N����߆��a��&����������~���#���?��Y-I�h��3���}�z�������W��r�ܝ����t��|^�A�'��#�5T�޴�S�s�UY��!݌�5�D�ߢ(ѥ|?�>�(�Ai���t%�D�3N��-�$*Q+I��.DY��E��C��
iDi�"�����u�lY�[�����IJ��a�XΖ�4���J�,�5�$���`Q�h��3(Kw���-$Y��Z6�7�OR���&us|�n5۲]C�R�'Q��֗x�v�у,�EK�'�(E��bW����.pF��ac���L�
x3���-�Z9l�U�J!Z�m�U�6�Z�n�_��VC�R^��9��E%��;�4�A�C4������D�PQ�Ҧ�x�XY�[h}�B�U��u��`���gq�\FGUp1�V�K�{����kx�c7[�9U�ė_��Wp���W�|�a)��Z5��'\Q{�[6���t/Q��-����
_�~��z����z����])��P�+�=Q��uӞ[�n�̷R�+u��w��'�w���xP瞏��j�D�/Q��	/"��
\\�+{>Q�{3�v�����w�t��]�ډ�ݭ����w� �E�w����*�g�M߯������
.��wo������`�V�{�~wc�=�Ƨo�+��6q�����X��fW�(};\�z�
�h\v/�v�3��|u'ȼ��=�Biv\N�&�d����� N��y� ��Y�`5Y��-m=��4M�^��7&�7�D.娉@jSǾ���2Ϙأ�#�%�����v�p��Z�?4JƩ;e�����Br�X��jW�{W�����ʬ���Z�C��̯t��m����{,}�>x.O=��-��`��u�W{���Ln�l��J��_�>�f*�"
D����69�Y�3�zo=���7W�,XE�m��/ъ&���'9�ӂK�0`�ڌ��Sv�u�`S��f�8�ͅ�b���P@
endstream
endobj
65 0 obj
<</Filter /FlateDecode
/Length 3719>> stream
x��\ێ�}���� n�~� �j��I���A�2`���T�Z�n�wأ �ʒg���{�!����>�,�����N��s�������^ʱEj�?�y�ǟ�߀�Vn�Vgh��@��������z��'����0��r�\��@axk� �~�|��E-~��L$䋴�u\�E����˟��/��_\�����%�@�� Y ����,��BPq��Ϸ���;K$�f�Dl�\߱U�z��\n	�;z��OB_����h�r��Vܭ��ma$T��8�����f5����BXp�����\1��E�D��ऒ|�n<� �-��z��0�s�j�������xH�W��0!]�8�i�ʔhR)��gQ�c�._p�㖛8$�x���A���\h'���&���.�4�� �7Zi�C��8��ʔ�'�q�k����F��NY�i��㗋�|{�o��\՛�b4��L�4���s��*�@���H�~�:H��Z��m�_!��"Bw�;"I2o|cq�*i� �	4�8чH�^��r �^��H3,d�@2�P�k����Ͱ}I����fM�[�P�B��a^j�@�,j]\�J��80�|���Å,_^/$8��$�ʴ$܈ $0��5|�.$Ɖ�5�iH�$
�]��:�y������w$��\��u�-�?,�s�$�#(%߫��j��T��߀�	Q�HD�h
`8��%�#|�+`o���4�*�X{o=�7�*p�%20��"@�:B晔��W̬\�p�[:�&FXou��^�z^�]+�Â���o ���a#(�Z�c�� �.�=Y0 �*Ԁv{,�lޗ��VO��Uf�q�ZZ��{��=t�X�@PSu���qF_��H����#tT�
VK�(�/U7v�������9lۮ��LK��m��q�?-�]��PZ��M�H�#d��h�%�?��^ �m�#�~̩Y��T4a���C���c�+�)`u���U�fD�&pa�9`]Z<��S���iX���3�U7��	-����lڤy3�6S��H��Wԁ]{9�O'e?�c�Oy�#�}'������J ����:�)���M�;l�~�����]ͻS�����ׁ���#�m�����F����~7=W���q��=��](t��C4��ȁ�U��;��`?�����nv������.!&�ٱ�1�MM�P�?�3������x8���(���z�=ނ���w@�4}��c5l�!�}�^(Y�Xu<��a�ͧë�w@Ю�AH��X*��$]��3I?o�Y�{�{1ݕ*=�~���qz���<�H��H'�� z��۵�n�v7��!�U�?U(���aզJEN>}�pb�.<j�n�܇�[02�? ��7Y�5�&�gLo�q�O?����f��vy.�}Pu��6~�������,������)�׼ˣ�}�� (X���[G)ǡ�<|�7bw�kb0t���M������rE��� <���W�ݿ��6�l{:��~�v��V�Z�ĲdU�
?���"擥�ܶ�3����	t�-�
��|(k�+R|�Acx�OL�K��9��׵���"|�5�0l1�/�:�����4l����ۅ;�
ύY��p�+!�Wi�F�)�����4�"ifHj�~���8��/0X�R	Á*W�H+����$��AK�0�H��B^��0��D�����|��4�hxȖ�Fv�eH|e*�ȚQZ�@�h�T�-R3�T@s� �J���xR�G��@�0J,U�@sV��M�fs"�)[���֯\���<աU����፨�,P���o.)����Ei2�pp�+sO`Y�j� T'CDY��>.���'��1V�e��87�7�ɸ���'�O��+V阊w����f>a�
y�[��b�傊�u�T�D�E�06ъm^/u0���p�)3Tk����8@�p5EP���]���Z�yĞU}����Q�D@�b>2*[�L^�шQG������8��W��_V�K]���Ҿ�mO�֨©;���3�v(��ئ�E7�P؟b�g/i̧x_�f���Dz(�.����q/i�I�U,�a�̇ȁ���=��B�wnTY�2F��a�t�ޠ�k�h""�yAM(w�E������CUO&�=��;�N1�u��
����B��``K+X�#7��$w��e~|!��gq��ҟ�R0�LYX�LT=�J,���T��#�U��^�ׇ+�T&���(T�VXPB������7��V5�N�G'���$-KZ��F	"&��l�%�5��Ƌ��NB�߃�\�Vo�#�	�0$B��=;���Ã��q���d�x���s�2�N�A¢�E*�s[���#��楥e��C�!,�ȑ�L?&���v�9��(%�:$�5����4�=�֘���<�H�(*r`-R�|N�sF� �P$\��eB�x`>�U��3)�/5V�h��Y���H>��������d���kM��rN-����ʂBv��/���Y��)�%�M��4�[���!�j�K�4|���j���#��Q�ȥg�@r)��?���IX\w��`���Π��s?(1�w;$g�hT�!hq�~[�	F��(nc"�. <�"���-��[5�@+}n���[�[h���+¥���tm
u��~��^�D��覼�g���,ɱ#K��Fr5Kri��$�^�u[��Y��'J�n��ײ~��f��A@,��V��H��ӑ��+�m9����+j��4�@H��������je<E�?�7�;�'w�����Q�� �j�).�tC��K�i'�=;�*�ǥQ댴kU��OA�q|�<I��
�@74c��1Maxc7�p����3$�;g,��k���q)F�:#�Z��b�q��3IL1�Q��t?`��H��V P_9}�L XNK	�Бt���݃��|��Q�^�@�����
�R���OK	��o��N��kU��|T���r��-,���:��s��e�c,��y����_+�����x�U�x�2�nң>}e��EA�8��	f%�����k�R�.Ռ]5���B_)r�q�<�O�'g�)�7ߋ;��{Q����6���]���^2��X���!���G䁇���|�;8z�Cj[~}0g���g�ԢC��QyX8�����7��q��#��e?p����a�n^��Dn�%�z�4�������\wT�ھ��F����g��R��z*�������GN�"�p�SG���Nhl�eؒ��ܰK�=���!�c(z5Py���Y8a��bU�MO����J���h�gb����ּ�k��y�)�ک�NC6p��coL�5/&͛��'�tZ�W�5��ik�0Q:�_^uȯV���rWܾ�6��{U CD�!Q�
��g��!'<	��'<7�<��d��	�V���𜭑s=�m��6NVDi}�F���
�����oE��-�;!Tҩ�K�ɠ��8�EN���f#�J�
��5*Ӯ�O؈�,�m���*p�\�b�]�	��<��~Ӯ���fc��xq�݊sv'�k��13��Ȥ<Fy����"�7�X�z�8��Ձ[Kɨ��tBwͩML?�*��MW�_1VN׀�*5d!ήo���7�|�`��bݘ�܆��n��a	˯�.�VU��:��z�Ϭy�>/:9۟��u�_��_��$
endstream
endobj
67 0 obj
<</Filter /FlateDecode
/Length 5520>> stream
x��=َ�����l`Ҽ`��H������b!�����`�fVt�Y�=�5SReT���A2H.J���&࿟��\��1�~���'�]� nڊx��_������n��U���?AAy�������?����?����/�磾I�V�����^�����/�o_�
%�M����M����O�!���y���O~��� T����W�	�:�L ]v-+���>��8�mQ2x��t�FԦ��[R�E��z`��0WA�p<#�+���� �VZ�-�[����h�(2~�L���x��-���D�+*��]���X/�R�����)��nA�*�0ыU���*�7���%�lV��=?�v�ZdH��H�������A|W�=���,��n�,G+|3F0�2Nߔ�WJ�RK���
|�k"ʰ �a�
1�\XXZ����f����P���䢯O��i�Z��2B�:�*�s�k�Ű(��&¬�?��y���v1.� �!B�*>"H��b�q��"�I�3:�V���*
�퉼�`ÍT�@����V�VL�l�zȂ�	�	�]�[�@����^���b���&A�67"�S���W�>|{"�Q_'JT�%�F �Y0m�h!:N(n�PYCl&sPQ�ʬ�k�b�Y(�F�Ȏ�/O��~!������ɓ����|x�o���=��'��i�th�!h�l� b��!��qCQu��f�h�L��; LCG�C�m�C��C�n��
K�!��!?u�!è
�*���ƩV4��r��T��1��+\����M��H�{�`q(��P��s ��9 h��s:��l6�Jx��n��=V���@��A t� �:|�b}�Dy�ӣ�w�N7��Az:M��S��,�,g�dgb��1f�tF��@OE.��%|���p:l��>�nG ٍ*l�#l�q�>��F	��������G���"��>��+l��*�S�#�vPQ���j�**�� 
9�T*�Ԧ�nLQ�HM��s��yۏ)����H��|B6>"�0|%$��6LSDLJ�͠"�v��(����b��ә�*�d��Xa�C���!�C�!��D�j�D�D3+�M�5D�	��*s��T&�"�&�X�B���X�L���>���;�ͻ�?������t,PTF���	�'e�[� M���7F!�
2���"�A��\T���*'X.!�yȀ�c5*$k1�} &6��,>J_a(�&*����Eai3 ĵ8c���.;�(A�kK���X��g`bܷ ڢ���� �"c� @3�(�JeF� $]z7�	@h�6����m�p�[���
�I�&
�L[�R1A�)!t�G���^J�"�K`@�; /�\��0�;'�|���t��BR/������A3A(X���9	�gUH��B㑺iW���bկE���0]ʛ�O���w�Q�����f��(P>"���5}�J*���wߞZQ �ņ��\ R�#I�G�yz�1#`���[#�fѩ�
B���e �T��
Y�6��z|��)�Te*����X�]�r�ܩ��)R����)�FK��t�Ѹ��=8����p[�0��_��=�߿�sh�Y�~3ЫCރ寮�YI�q���ۺ�>�k}k��K�_���Oy�/�-��6�^�s_�Z�[����B/o�ѡg�>(�X�+��#�e�2�;��7�=�r�?gRe�����3;4!?�(�E�h�f�.E5*k�����g\iH8<�w2/l�1��ʅ\wX�RE��*��+ֿ0�@{�!%)gO�kuF`�M��-	1El	U�ْQ-�AҐ��~��t0�dSQ�̣-�SB�|"��L����9��^�&hkq"&�'ͽPV�$Ea(�=J��RYb��*�p��m(����S�?g=Y�?es��"��Q!#���6�K������<BBl��/����+�i�G}�ޠ�	L <�7��`<V���W�4�X��C��|Sm�vS$rX���H�*�4%wq=Ҙ$
���W�FP�h_5�A�G~9P��_�8;�[EIO���c"D���RB>#��=_`��hn��aes�xw�!�ڭ��?�H���Qৼ���ۣwlw,��^i,V>��뒈U��J�Eb���/�[=��J\*E��Ry��kbh���&�3�(R�mG�~��0�m|�T^"�_֏tŖ�7��,ƴ��o��c(��:�{��A]!n�;��L�}��0|�iLNI8T���fW�'�K�\�N 
'na�-ݺ���ń�Ok�I�弌j�U#�'2��w0�)�I��\H����C7��W�u�mLt�D�Ȉ`$��dQÎ�!�(�1�"�v��&��K�9��۠����6)����oi5�'��he*��iC�9`F8��w�tM���;����wE�=��i�-U\f?2y�4���
j��M$]�Q��v$�������u��a*,�˅KLHt�w�����*,����A���F[���:�M�m���+p����ld��hѪ0o����C�kn��gL�)��ս�+Nq�DJ���ż�o�Ҹ����<yo�a��6����,"XB��|�_"υ��w $�]6.�C��vgfW�����/�e���U�Ϲe�A\��-���C+�v䍇���gG��P�QmW�ۊNaZ�y*XlY�X~0D�� .:�49�,;�S@� k����)0Tt��M3�3EvNx�q�A�	򮵄�K����<�`D"��m�m��l��g�C�V�C����j3�Y6}Ɲ.�e%d�A�Ry;�h#tl�����N���2����g��:F�C&S�lt;��k���0~+#�C��P1ߴ�Mk�=.v���,��Ba��V�c�Q�E��Yy�>���kʧ	���Y�q�k"�$>zk��U˵��u��שy���b�Zh��RF�Py{��	fwЅȟ�=\	��<�(�L�6�g��đ6�<�㺪X^��~ICU�Fy��L�S�$q��pJ����r	N�F�'~D���Y�k(�+�pX��&�Ǘ���	K�;��+7�H��1Cu���2�'��Њ��c�>oS�°M]�:+�/�v�o4��b�z�P�Cwc�;\�<�#|W�E1l\w]�x"��ǌ��m�q+t�Щy^�mʵ0L��&��!>�w�����r0�8�YعC�m>��b.t�t΄�0����[8q��wBCt�n����`��~�x>
���g�^u�A[��s���s1��G84�z5�wl�bѝ��� �Bfu��Ȑ뙣o>⹐�1+{�0�#tW'��Y��
C���(M��(�p*�?�X��U�^���b>�9��N���}\]��A�:�n�Dh�rw~"����)�8ɨa'��q�\�/0!�[. f�q4�9�������>�5)R6��,�/(��_�X?>]ՅsYӗo:�2E���&���=�b��X�??����D�4=�va���'VUf��4>���6�����[M�筜붨kŔ��^�z��>g���lo����XT5*�1��Y�κ6f�n�P��օG�@��^��h��/���7[��X�b\'UEp�8�ĥp<�;\&W��E zh�k��f��LiMIw��#߅�j�b���P��8eY�Np��}#��
�������� c_��<=uJN��Lσ�]�̃�%t���q�b璎~x=$�B��E��=�v��1�0�iΧ-]� ze�s!�����q<�CF~�;��"㵇�m��t��5%�qf��5�L� �k �4��;,n=�����dU��P�,m%9q��(�s�
��V��ĵ
$G��6��frZś��V��@+�Qk�]�z�Y�ˁ��0��yn��T��om��#r�Z���x�֟�V`���V�����E�i"mx7�7�vZ�?dM	���5�����Ґ��Gp����M�ӺBh������V�#� ��3�V =[-���j�X;���ݎ0�H�����X�FV;;��OT�|�G�sp"�Li`��@�
����V$=*�[F��<Ȱ�<�
�穑҅�*��*K�8эJ�V_��6�	��(���(q�3^���N�
�y��ǒ��G�H���1��wޮu'�~;��~~�k�0)�_����rp��l^���l�;Kǉ�ء<�.^䂼�9�!*.���N��o�ȪTB���@�����l���39�ܜM�\�M�p�W�u��W�3�N$��'ݴ	ϓ@���0�b�'��Μ�b��{]���+?��'V⦓��dsf*+�z�§������{(VF��
���|�1dcaKL;�AWE7�^����)�o��t�䅛����׏���{�����i����I�&y���i�s��ǘG���"=9M��'�����1�4>��3[�×Y�7���:�?�D��n�J	�c����ݮ u��Jr7���7��3�����t"�,�G*�@r����u�N�+�`���Ň]��H���I��E������xd>i�s����3#��L���W�%:����zh�鉤�0������T���ua~n�>Sv������2�磤��B��!7�M�����փ����=Ń�}[��>�m����8�ch��P��PL0�OGVjU�����{�-:;��4},s#[�	�����/�"��x��y.���ț�~�O2�_u���E݄1��,Z���;0����c9�F�2����dӚj��4�
�X�4+y�h��\%i�x_���f�I���~ss�|�"i��n��K� ��_��[��`z�dWF}�aqB8�l����Lu�2@�d�&�K�3�O�@��J7ַV��(>M��&�F����д�N$�Ӕ����k�q�����%���5��8HC�$)�bI���V���J���Z@41�ijp+ܒl[-�"�w�-�����MI�n��/�@<�Z�00k�):xq�����T?iP�`o䦷-��>9��hn0)[�O���ꐩ"%hS)����������tm^��w�^����0v�����|䜇��o��;����&��C��^�K�Hs����Jv�ՇЛ����1��s=�S�;�q����=�'�Ы����z��zz�r��W���.�W��s׮�hk:�X��)7o߹t�^FTn
Ϸ-}�K�<��᠞|�P�:Ⱥ�[��z��Q�qc�{^օS�v��G���_�������-���A���E�kJ�u��:�r7�>�Z�Ϣ��׈���pl8��їlD���R_T������ǡ����{��������k�<u��o�M�qvP�tυ�Ņ���|��H!dLwn�x��n������+-=�'�T3f4�\��#iD�G88������$
endstream
endobj
69 0 obj
<</Filter /FlateDecode
/Length 4230>> stream
x��]ێ�}���� j�~� Ү�ω���A�6`�����ș��z�M�+�4}�I�N�՜�tL?���w+�F�Q���?�~=����h+���?O���p�J�[}�a�BC�П�}����t��{����ԟ�z�R)��Ǆ�5���>��{2K\>�����r�~�A*�(�|���g!������'��?�c����	��"a�)�`s�� �;�����۪d�Lr��A�4���TΛ��z6�ؒ\�h�}����ְro-�,�,�xY-���4#�~=I�VG?f��zeAa%���G��^�R4D~Ś�18���tVp ��|^�GG�o�;ч�]E)��s��e�ta�CB���N-�M�\��'t\>S� �t�?��Vtg�p��%��J銁�h+�+M�8��k�,H}��hb�\�XA�h}���(
��C�����'}�z��Uki�̈́8K��]�s~�Ű*��abf5~�t��{ǧ�b\���0�&�
L�i]�M���*f�����Y��j�ܪ�����'ZXX�	rP a���U�`$-,lB	�03�y¼�z+:�Tfz�k�k<a�̠�&�va�X$�k;V�v�|b�h�3�nߘ ��M�N�4Fr6��M9�i��{1m3Glva[�Ǽ���_��xP_�P+!�����p�� ����k���->D����9>$Lg���	#�� TA�f�d�M�:`�@��on`AN�BDB� ��E��k�(WC�(�@���@�6�@�"�@�2��Mڼ�*�~W�88h�����6���� +�A#�9B4G��"���,B6G�<d#�UIU��Zt>h� -�$5II݊	kA��Z��c���s&�n9� ��ER��:N�>s�UE�y�*��u�s����[�ȼ����-,������G	�7}��9��$�℧�'��a�q�K3�	���E¦�0h���Aش�H�y� t	�a"��a"_�a"c���KN�>8gv�{@���6m�TU?�����v}sw���^_-X�ٸF�l~%2F���k�d,Zͣ���cA"Cc��ؼ� T� ��� ��9@dt+"_� Q/x��w�n;۸ ��M���<��p>��
]5�c�yp���C5
�v̵o��b�[,x�������C�_N0䊬|�RC��бw��aOګ�!^ D`2$�F`�`V��C�C#c�62W�����n�R��b�!?�	��)�g�|=�'��v����N@`O��ǉ8
���ʒ�(��<�� f�����{1��[���nE�&@rبe�g�0T�[ӽe� ��fY�Q �n�Z��bU��`�wk�t�2�;���D$n)Aψ]zG�̭����n`�pHK��M��d�����C��$[arP ؐ� ���L���n��&�.��˺�p��ʭ���k�A��������aJ���%R`��R�+i�v�g}�Hj^����So,�A���m�p/.0�.�й�"?`HD�>S�L��XUR�$S�]!T�2o^���i�ejV��sⴙ����l�#ݕ(�(�R�4"}甞GK�d�'҆����4�	�����nȯ���|��?*3;5�/�=9�n��������ڧ�Z�sx�D�����4�`�����"�~dэy(�Lo�[�o��<�u}Of,�vY���ڷ���j�m���³��eK0���<�h|�I:Sf���p�)^��;�l����=_Q*Ia�H�3�TV�8��fت֙4HQI�I1^�2'
��KP��:�-����S%*a��~ɒ���/�ݥWlP����yEvd2�P3��v2Ɇz6�i�gY|�g?#�4�;�ɇ�O?Lm���/ŖCj\�lѩ�/g��v�B��b��P��NK ��GZ���)Gt�j���H]y�ґ݌���+JK�fwX�����X&ݵ���OK�p;���,�acNG8a.e�_�VZr��(�fwY��{�%�ߝr�o��N��l��������e�(�⎆�Żǡ��S��(��Ɔ\8�:��e�ceQ�*��T�Y��FԔ�t#/`"3��GL4�9�/_�%{�wj��b>d��{zJUm&����nT�P-VAdE�r�ԵV�*�Z��*C%�^S�h�|��G*��n�j1`�:	�Y��@V)N��J� ^!N ���NY%����]XV����ZSlXS�������00�je�@�<f��i��G+&��0�����T� ^n /7�+����å�lbw���]��yqX��=�K�j�St�VJ͊� �w����0@ފ`yq��n=d�eKp<]Yy�B�6�@^�{i��˰�<�d�d��]6�^ֵ��1ş����[�^��u�����L"`���q�����,��'^N�X.����l�f�A�fW&4cJ��9{�Q58bn7���l͵�
A+G����[�c����Jg��#Aa�*֩t h���^^��`=�ܣ�ͮ�j-�k�t�젒�t���!{��`�n�+C냜�n]I	I�);���QOjGȎ�wG��_�\�\wGn,=ٟ���	Wb��j���Pb����.B#�x����1c�3�����w}kS��P��d�)�g����B	g-9�}��O��iJ��V�l��6��)If�wK������LS�x����{0�~�c�k( �q^
�)!g��kU0쨗�ve,�������n�	�x�m���u��RY������V���"����Լz}H�C*�g�\�1TW	�5�JW�m�����R���C1P�>��X��8���fJa�����|}S:TK-�@c?���C�e�W�M�_�Z<\��l�47=�ډ���z�#o��j�cƮ,��D�}�6��u�{7��bp�)��5��.�oz�uL���a'Rn�E�C�i��5/T����O]�ͅZ�<�%|��t����A�{N���F�W:�	J�A`Y��ZO����P;u�o{�d��7��<��������	��2�[��֭�L}�x�ጭ�s:�e1��M��,��6�ms�V�XV�w���eM_s��V�Im��GO�������ǲD��5�,�]蝓�z��_��mC��9j%�����y�t�T���8�P�TZ
U(�yr��{��ߚ2X5K����߿Y�K�D��J�Ϻ~<6O������o�(�	n�=�G��Ks�%�/���HI!� ;D��X���Dn�ܶ�֧�Jۯ8��Ʒ=KW�1�![:3���H�{�����Z^d����S�l��D�l�'��1�wo��\��V����RB��ܥ|+v)��>\��Q^��*�oPv��!ާ�XE�W��IľW�8�jl�A�<��|F]�Ƌ]��시�z�J��,�/ܶvb�?���z��ika�6j�����kۯ����ru�v�����}K��t>����m�Ώ��Z��(�ݩ9�bU�c`��&D�'��=�{3�`jW�!��oh�aA��� �L��wC��Rv/�[&�;�qQ$�]}s&ۃ��A�%�X��y*�xM�V{:ۜe�H:����Gٜ�+Z��F纼6[+ W�љ/�jc��6l��}}Gj��=��C`�{�zc�_�E��Ѱ���X_B�ߡd�� j��T�Z��F�klS`�!�����1�/Sˑ<M�%��ӕ6Z1����y8V�"}s���3��HC��fW���'��b�?R	L����"�`e���ʊ�#��v��I�N=6����6��%�s�IE�# ��ٵށa��Q19�aFG���J�����:m���s��W���?QY�������[��ܭ��6q��4���IJ�$�1J �BK�?b� ��sy�lX�b~� �c��Y�9?`e3�N6��l ?B��S�l�v^q��ldb��lz�d�?;����M@^�a�&���>29��aWF���I���iz@p��RVl<8�@~t�����c4�4[2�9+��F�|�S��U�s����y'�}�qkW�]��xVlس)�.nl�,���?v���lO��h�Y��L�CZ�W�����3�,���������s��]�ۀ����!|-���9<��O�~l���u�z7�;[��G<�������7��f��h�������:M��S읭L�G��~�7�2��fk��V���b������l�տ#�l��˫�d��F�����4
endstream
endobj
71 0 obj
<</Filter /FlateDecode
/Length 4262>> stream
x��\ێ�}߯�� �y+������(��`e������=��z��V;}�ɺW��&�u��,���S�2y�� �����{�^h\~���?���J�W&Э��0_QC����������Ïn�����n1�Z���h��|�[?=���/�|��:���E���X�|���W��m��߇@���B�Mk�������3���0&�P�`|����e�Ioʚ�&�����kQ�M��0n�ܱǹMfI��=���&+��ڭ�]�ޝ�V2��t#�����`LP���Ű�-�[*PÍ�b�b�h���)�W�Rx��x��H����nRV+ �B�˗ra1������Lfj����T���X@m�}ڛ�3�N�:*�y��;)�*�[��ȷ�5����.Ԧ��x�/�H�X2�Y��l�D�-q�۝�T,q�|L�@h??��ꅯ�sƏ�	��.C!N�&e�e�;����?B�b�1H����7^�1�lZd�i8�Q�Xa��!Vn�k6.���_��!-,��Ch�gN$����<���`1����"F�2Ԙ��_��Qd�U��g�4�Us�z����_�<���o���v�-���P��4hEl5UCi\��%Ga��n;ڟ��Y!-�'��9��%��\��r��!�t���2J�%hɁ'fJ��Ur(��a�16�L�F$�Eh��99lN�%ji���P��Ҕ
:'��-�]�C��ɡa�[��Yq�ՍM��M#]lLM?"�el}�(n����,����'�l�)90�JZ%�����a�2���!��!��㹫���L�2DƜ�9Cd�g%u#�e�|�2D��2D�]8R�V��`@8ggu�p�H���}EW����KdB�"�uD�6#��e��ޒ�[R��$���.o,�>�E�EáO�U�"���k��t�3H�M� j�2H�`��ze,�!�X��{��0���(��|D�5�*��f0E6�I�-���`�y��h� ٬H51����I�@^a�8�d�&m�I�	4<L�R�	,*��+ؕ�2�A�s�J�0�H�OpDz[Ĭ���O��Rf,X����d7�u���T<Z[*�j��a�����!�?bWd��W~su�������:R�K\ThҔ�	Ay��r�R�"0*KRg�ib�ÅP�M��<���N�yZX=L���ͻ�Ξ)=$�f�-�ٿ���bǚ8�T	,;qm)�NR�
ơ�ܼ�]g/����(�}�ѱ<�4��&�%���R�;�F���Ф$�U��l�(XI��;V����XѶ�_�薚��Fl?��m}���벊ׅ��ay�4#c����姅eϓ�D&,+�^O�����Ԋ�m)��V���Dw��h��@i��{���@5K?V,��P�����F�4N���/�9�|s�g/[nM��F6��j<8b�����:��\ֹ\#��&���)�˓����u-GA�nf�S�1@�\������;:��ܟ�3�79�hz�)��#:E�>=<�)z��t���)9N8���mNћt
��� ��h�A*���Xc���~Cj��8Zs��X�����<f�����NQn�,8;���!ǊYk�+���[]~�j���z���9����ڀ���}<D��#���?��x����z_���y��n���Z���0�g�Y�7�}�wӐ�j��=�8��t��&�F��>�� �0�Ʈ��q-���>[T7rW��L����J���yF^�k[A�Ҁ�p�h�k��C� I�q���%3�D�T�Haþ���Lw(�B���_R�گ���O�n�?����go�8���(E��fZ�x�p�,e�;K�sK���H�f�Y�Ӳ����+X�/��I��QAu�A�T�0ڎX���O��E�t�w�;�����O\��O��I]GS٤�����j�}ݙ�!V����p˸]:cBbq38m����uW�II���" �$�T��cmo������r�V��9|�*�̛��B�>��e!B�3�g����l�S�b�L�h�|S�6a�6e;�bo�g�w�q������ԑ.��X<:��x��C��kD9�{s��m
��W�N�����z��,�!��ۆ�.���;���g3�F��P;���|~$4�sZ�\i�%�U��΃��#���S���DY%�J�����.���kK[
���a�X����.�X{A��a�k�΂.{8D��{G� Qj�	.*<^��158B��P�NvX(�;���,�Ϊ;�j�7�<R%����\��m,u|GY���n��EԹ"}���aP�Wsu%�J�I'8���=/�N:n��Se���<�� �s�,���zW��|�	/�q�M@�Kr\��~��V�
�`��:	ߢ4�jNP����$c>��Wl̚��:K�-%%����4t�
)i�r��4��SҐ�.)I�䖔�n{F&�wJ$z��:́��rEx��Y������b�m�Ppmzqf"�}-�.;�5����۵5����4xܛ���p�Ğ����`�ZX�IZ5��m���t{�ޞ��g���yq�`����*"�6;�����wz)Aڪ 4�h[3����Ժ�驾���w�Dؔ����ks8�@v{���W����mp!TNյ���>�!� -u]�ۆx�Wn��?E�����{-�wJY����E^�z�Lm=�s�>ǖ��7���+u��'�����>G����;�zȼ ��yI�����5`���7	�/�І7�=��ryYc��z�LR��-�W[����a	�
򏍼M�>�hS�pE�Gp�Hg�>Unz+���.�5�h��p��MӖ�!���zl2��w�u��v��7��-lLH���SУ�`�H���[�_��+ML3$���_���)�^�/��FŸ�q+���!/nvt(����R�(����ݫ�._|�ۧ0�7�-�y��.&1�|� ��7Ry�Q�tF��f	�\1KAA�74�0+۰�6��Y������K�b�ۅ&�1��T���J)���B��xsUŸ��Un�ԏ���:(OS� {	<i�tz�U�Jr,��H�J	@A��`����\��
(�ST��e�Zof=���U�j�&��������sC�mJw3	S�?ϼ��̋��f�q%�d�P��V��P%[X�U+� ��2��?q��	u���0%������(�&��3�_e{��.���E��W�MA�4;ES5�u�T�M�G��Y��7�INv�
��f��.|�R#}0n��E;���q��)���(�:iEE��Q4���C��RV��zW�c�*Y���qyC$���������D��j��k�p����)�<�b�U\ �v��5h|�"���Z��Y�B���/Ʈ5�A���æ*��Ѯ��u�����A�6u��u`[	���م�|�Ԕ�$)�2HX�sV#(�-�S�#)�O9��^!��`�Z$�֋�փ�L�1����NtAe=i�u�iN��cYʚ5@��^�n[	��@~9cS�򦭹��GN��Q5Nv]��U$l]	*�I�ߖ"6Y�6�u�_I����L^e75�q=yi�o�窉��Ʀq�`��rN�l�kEP�志��R�~uܫ�o��~����x��T�Ҕ�y]k5'�/�E@��:ܣ�Z���א|���!�4�@Y�w��ON��n�����/�'�I_4��|�*�>��Xc�$�ig%E�׺(�;���@WSޓJ����[N-�����"gL9)r�RCϧ�㊜��D��5���H���tZ�A%.��$����f?p�!򠢆�s�6�����$'����8ch�6a���e5�� �	-��F��d��v���4��zVk��Uph��D��� ���
6M�0y2�h;�>hIn�-���C���lO%"��O$r��S�$�c�qD��EyaZ���<��W�H�|n?3���>���<����H�Ѹ��#h��&f�9A��~���<T� �"ʚ��@����9D�1�Ir�1��4�CD(� �9D���Q�l�����uP�D$Z7�"�J;ݞ�q�M��_�����\=��� ތ�϶��|!7�W߮���V���V����^�h�O���GޙXT���|�?�}G���]���#���]�Ks��]ui��nw#��lWw���
��:��,X
endstream
endobj
73 0 obj
<</Filter /FlateDecode
/Length 4342>> stream
x��\ێ�}߯�� j�~� ����X@>@�kv��)^�졦G;��li�t��;��U�+��&���ξ#�(c��_~����i+���?����7�f���<���F���?����?�����|ԛ�J�t?'DЭ�n}��ᇏf�ۧ�1Q�Pn��>He7��O�>�Ym��}�����O�� �0f||�H@X�!etl`򤏟.��J�(�n^DM��Y9��!�,�XQ���$�"�|y4��G=�;�/�L���gb���?�?H�vG?f�$zea�J��a�n�z'��%�'6�Mt`a�����&z�z�3�1�b%v�i���~-_�|{�/�2$DM��Ѳ`�$�E��}B��3��K���q�Zѝ1��2NoJ����}b��5W��qt��
*X�݅�*Ă�h�U��z��U�Ƈ��ԏ�\���}۵���L���W���h����.�]Ag��I���a������b����0�&�
L�i]�M���*���A��i����<�����O���i�ʴ���E[�ϔt����I�U�3�0��؊�JF�D	���.�iQ�WՓP��Ԕ��4cG��n_����ۙ!�i��1�q6R�7���3޻S4!1ߩ�dN�d�ܱi��mU"��������E��9(�{P��������9C�;�JB�5JH��e�@�%��� a��1J U�aQ"A����09G��MQ"a�(��)Jd,E��D��m��fX����]��.P������^U��|�J�;i�7w���U�5.��[�H��!S�H�%6G	�a�	��2c<aޅ1J �<B�w��<a�`�	5I@M��"}��|"D��Q���[!�����Db��8c��B�s�*B�[L���R��V�1׾%c��ǂ��;�t�������(a/�~̮=�':�F���㩁�@�+B��QȐP�ke,�1
?�"U3�H�����('	'� �J�JAZ,4&d��L� C����>J�ARjD�%=��VJ���i�Ii��Jr8?p;�Y0i�6>��ۥiβ0P�#
H�FgF�G�$���0�Lb��`6ɸ�����*�>�+������Jn�wk��]�%2G23%��K�l,f��78_e+cN>�oJ��.�D�xC�(m5�FH�16��<XV�c@59�J���ٿ�Z�N���@]-��,�:�W;^x�� �0Py�[�cXBy�E�ŉQ�KY�����簀��"�.X���CS����2� >O!��!:�<c!��Cz�xF��DM�D��aI7���i�ec��MS���SF4�����r�Q�0���O�~�&r�4c�ؔ-KLg��ˆ�!���*¾ÿ�|�{���y�G��/�����W�u��F��������q����W|���|���v�?qc��{�+�3��w�T������}͙��"���7�&�Ѵ��zo˺$Q����'�B�E�k��A�J���e ���)�}TD&青����wk�B`�7>�1�脭���Q�u�})yDĨ���*縵�����s΁�8/2�</�2٘}� Tv�nK\uW.�6ꔀ��nv�؝�|��c��,Ɂq/�r�F���_�!3�GJ3����:�A�&o���ą�;�-�]�PR]b�,(��s<x8�jm'U[lWeUw�α�}���1ƾf:q�Kpn��}^��_"\��ĵȶ�h>���D ��I�8���z�9�m^P�5���-���1$���[�$�K��RQ�H-���,IU��e�ۄ�oʉp({����i�HZH��?'W��ݫ�J���N�'Q�{�J8��Ы��-��c�tC��+r_-r̒O�yՃ��3|�5�8c�R�W7V��7��s�nH�青�9��wH�q|m���%�|�s܆��S��_��U+�z��-qC�F��9��F�	{�~d�x�ƽx��)U;=��J�q�R�Ⱥ5���>��p.�{n�׹gH��5�ڽ��I�'�L(�{�{� ɠ��)���=^�挩ju.�I�n�����W������F�#7җH���Tg�)��39gk~+�9#��K�E����*X�vM�bT��M�*��.G�{��ɬ�z��5�d3Х�^�^�$�U����~��Jl����>���EL�K�T��U��"��&;����0�@�O̴\�<.Y�b��F��Q\J��<���e���>!G���5��m�"��֜�?.�_kx�Ǐ��T�T� CUA�R1����H�F	��0U�k�2����;zIm�}�SN%YNo������0��`����Υ",B�;`B"���Fm������^E�����!,��.͘��: �6��/��x����r�Ӳ�GE��*1��%�R�V�9���;�
=A�Vr�`W���r��]Z���la~�V�F,WY���M]*�vZ�岲�b5��h&V'��Ƀ�hTZ���f��
*L�J�
 �0�QO���f�3�%nĭ�셸���+�3�_!{����`�Y���NR%;xSQ��uEU���J2�N2?oH;�k9j�t0p/������9f�4�g1��?��)jP�;U�9�᠂�&�>��Q�\۾��eGJ�&1��JO��p��z�J�_!���V")�E�
�eo�8#`	.{�:�\|(�c#��9z�vh�vT'x������_�8�K,E�����V��$w��\�m�>�Y�t����A��!�PԊ��T�8�+�5��Qo�(�	bͻ�7����:�qA�W�c�.\/��KFcYB(�+
o���sjGgsj̪q���P2gv�q&�Sj�/�]��2;�^�3;`2;���1�#�ev��m��e�X�Yx���J���4���t^y�T�³�*=�vu9��(�r��/-����399c+��G͙����؜����cf����3;@9�b��23�&ZԗSb�.1#�ù��e�]r��U���v��IAp˯�|$\H�
�,�K*��ص��e°��V��z'ZF�e���[�zC���	>�ڹ��<��}�$��Rz��i�Fp�#8�v"8aV��I�wS�B���gs�P7�oB<b'wH��I��.���<a5~[����.���faq���R���B?p�O	�DX�l�c�����˕U���m�8Do���M؅�#5c�6Goj�:Fo�Ǌn���@B;�ԡ5�o�њ�w�%|�8��t���:���ߕ�+�<~wy�.���Jlp�&����!�7mŦ�+�
������(��J�3�2}�����ޫB|������S낹�\��{���l�Es]�s�e��JW[���x�A����X���,ܴgO7�z{^���o�֋/��h�`~z��W�9mZ+�F\�'M�a~�RO��Ny筿/k�(5J�^6�Q�MJ���B;�ґ��ҙ}�V�fRr�]k��VRE�#R
�I�Q_�, o"-o!-P��s�NMNEo�������׀��Qװ&����ɱ�Q��ܵJ=�`
L������x�X�(0��4�5�llm o���*]I����NyW{����;G�*-��sT�֌�1��R��Q`z��պ�)L(���"
��F�.���	�A�o���u�nݗl�֦9�:٭��:D�x�h��5$/ud]��<u�rr�/LX��N�em�������g� �e�@�c��rgS7D4U2r�mT������'
���Jz��7Z���_<�:�T )X�Jȵ��M���겾ιz'kA�z�u(���}�i��:/!z�U�XUi_�$y���R��\aijH���EQ>�B���'��z@P�j�$�A��FZ����q����@ݳ���(u"�۶�3�x�f�����O��_j^z~�����ӕ
&;ʾV:�0x�|,��龷]����;�3�Y��j}8�2;��+Vȯ���r-2�ck%���C���}���^��d��*<�^W�ht�>���$�>Q��=����~�)2���Ǯ��j�,�N�2�=���L���R�:K��L�1�GAY���2ޣh� �6{;#����_'*�p6Wj�RI���Б�k%�&Ѓ�q�9;�!�%�wq���Q�n�@����ꎞ>�^�K~`x���߷',Ϭ�R���:'���x��W��)��m�4��.�b�-� �Â�r�Z����"Z�v��T�>ְ,'���U��9�5��4��sN�ƾ�圶�~q�I�x�%�2��}1g-����T+�/Y���cK�ҥ_rCϩ�:S�
endstream
endobj
75 0 obj
<</Filter /FlateDecode
/Length 5158>> stream
x��]ۮ�u}?_���\��@`�I~N, 0��;�dm^���n�֌���#�ZUE�;77ɚM���\v��i��hՖTJ��˧���}m�~1nO���������<���
/�����?_�/�����l.���^H梔���_3�ˣ�<������K�|�+���	[�J��6��^�}ߍ�����_<��� ��=!�f�@\��TL\y%u��F�}�N8�iQ���}���đ��+Gq(sO�(�Q]"$�"�}�mhy���#�G���cv�Ą#1]	����|Q�o^�؋�k��mm36���tQ~��~JITg��M��p��^,zKM�x���oN����^(��?ʅ��1B�E��U1c�`>�?�[u�Eގ*(_��[0V�L	.T!��Z��6���]�{���X��<L��*�����*�c��5�J.�'A�<�Bl�8B����B��(W�1ʎ��n7��,9��ԹOq�^'Kd
��;��g�}J�_Y��`*�HR��ɧIނZ�&�d��A����[M�_�yA �5�!o=�����R�"��!-�����h���Z�e�g�5�d�fu,�(�{�pm���2��8Qo�̭��6ì�^��ff�ĉ��]6�2M��[$j�®�֦;r�_^�W�B���I0h��8!���?b��X�{�y C�YFm����>�u:��;3 �hj
@!�)8d�z5IN040E�I�2���%��~�=D����P�ѡ^Mѡbl��I6��9�u#�M���N2�fwj"�krd�g?n�awo:lA�<��Ã@�� �)<8w
9�&���);���s��X�e�z��B�z�(s�h��!�f��l��R2����������}�J��lH�ݱ�ݶ��|����GP�~��GP�����W���!J!�%;F	��Q"8�Yq_��`�y0��Ѳ;	��AB�c��X	��$��$
�Vؚd{��a72�;�*�m��&�&Ev�!ov�����D�=Fd�O1B��� �1oS��c� 1��Q"cNf=c�(��6����ƃg�g��n=�����{-Lԋ)L��ɔz�dtD �g'uXq爬�xnхD�ӅI~FR'���!��z$?$}�~���w�r�
��/Pꦓ�jW�|"��&�Z;h4��wHI����A�����*�M!��������ș#I������C cY������H�>�-$(ZM�z�d��N ��ܞf��aC�0"&��*_`6'�$�^�*��3d1kp�{� D�bRD@/��F6+����I!?[��`�9dv��e	7�5L��L/UP7CmIC�D�0b�dIb�bbz��c�O)�la�)Z_-l��(u:h&�$Jrj��8j�>����n�2*	�F�� H�S�����Q�O�nb�gW+�X@����^��n"���0,���1E:�{+=Q�CF��gÐH~��Ep_ƻ�&�9�N0u��%r@1��vS���������e���nm氉�`%6�5�t�һM�E��DLW�z��`�`;ͦX��d]��#�UR���,�Ж�����B]�v�h������W��ذ���;��zϖk�g�xJ�m������?��c�C�[��K����3-��i5p�h�u&���bz��X�$��"����N�,"u��X�$��b���7��
�%�M�яX�zt�]�Z�^�K����TG������{Y�z�����_�G��6����w��ϵg�5�o�U����Fg���.�;B�B��u&aޣT�k�ڭ�~�͹�5q"�N6��:����`����(=������i<��'�o�����N2��`z���[4Ƕ_n��D��w#Iw�D�9b���=�,�
����
���=�=��[v�ܮ��x�{�]K=�}A4���en�5Ľ�E�~(��ʶ1�5Jʃ���(���4��T�R�bR�_gC%'ղ�h&I�F�j!����wrN�͸��1>&��vR[����@�w�6V��]�>�~!�.v��$���ak���̌��_!ؾ��K�J�I󦱳�*'���~-��+�^�%/+�����K�Ѭ����� �@����jY�}�յT��}`*�I�OJ\3S�z �� J�.WvFAEf��%D.�Ȍ�v��6��S�jf�kf�Y�f�A*:�N�@�Q1kOe���֐@�&��3�H�zt�n��@�>|�S�(�se��,H�4R�,cs��B\-o�������A�0����~Ε2	�Ų��Us��)i"D/K&���d7��r�L��`]t\+����*r��HU�|�%�p}����K�h/E�����ګ[�U/�u��2�ŵ1-�E�ƴVbf�ku�0Ր�@a*{
T�-t��c���x�	���Ꙉ�$��6{'{���c�}e�#ɞ�s������4�'�V$�gD�L�t�N�9����^r�t�cu��߯Y����{S��gLg�HcL9�&��Oӕ/����M�s|��}�q�F����ƴɺ+��N8LO�_5�MRBK�_m�5Ʃ�L�Ғ\��v�Wm�>UuCS�>u�F���r�d�,�x�g�������o[IcZ�n���$��t�M�Z ���'�4Mq�ԛ�H�y����\�m~�y����� �N���)J�4��O-�Z�u��\�q,T��p��b��óH�`x���b�s�X�W=��q�K2H}v��S��T��W�Mht'v����}?%7�%%q�)�;��Q+J�2k�޹�6�c���{���TnBd=���k�))}	� ��M��Grz�.�I����7S����E|�z�|7C�m�{�2�ӽ�Ѻ��tXU�׵8�0��ү($?��,F,�XS��b/9_�S��fX�S�u�|z��c5ɦՌl2�Ԟڜ��E�s� ��*� �ٷ}�O�]�����B�Q�J��1��y��B,0DCł�Н3.V,�4P8��h�N���IA�b�biJv0Z�YmC4|�o6$�٨m�QsnK1�5��ƨ���E��y�9@�N�T�d�u�y�r�����p�PXiq��z��Ϳ�h��B�.dE�v1���o1�2���mP3{r�.V�A ��^&���R�h�k �ˤ(�C�?��[d�u6��[V%��Qͦ:�c�n�`�o�ܤ�vr�����Rע�騑���a���2�U��My{w���4�j� �IH�$������Ǡ-�sl/��<��w�x&��A[�C�]�=PK5j9��|<-��zJZ��@����+}�k��U�<�,�[w���Ʋ�6^Y��M����J�i"*���)pM�6B�{���ZR+�>�F�BLl0����鸅%>d�Y�$c�&ɱ�Ú=\����Z{�㚍�]`���$-�`	zu�V$�1^��5|�#RF��
}wݨ"�a���K�r�5M�_i�d��;٠,�^U�M�6�S	��a��3��{:o:�cN��1`�tXMxDr�$<r;�c���c@O��S:���t�)��c�L�4ʷ۔�V8i�qv�(�,�q�����3�&΀��8Wr欪iı��EO��~Nǀ��]��16mr*b"X��w��dc@O٘M�l����1���9��P9�c��A{�f�æU	blt��٪�(����&7鲝�jar��ұ��[���U"��p�Kne87��)�Z��`�ԯ1��p4%��ވrHb��I�<�;��
��`��Ã�`�0��l���?��"��y<rbO�>,�lrƼ#����`g���h �4�G����A�M����Ak��ѭ�A����3�a�I��o��.b��M��U/�P�y( v
��6u
��_7��è�q, j���`�ƃ\Օ� ��` ��P9�[�:��ɰ*E�V�'K�<N6]�1پ:C��;��p�4��&o!|��2���&�����d5;�FǕ_-�����.!����߮��e����\�iU�Y��=ճ�4��惓��d�.ӑc�7g��Y�g�� �������Ҩ�ig���i��ʔ}�I�7n�=e�s-fЪO�s�Z̲R��ji����B֌,�d�/*�8�c^��9/��<���l%���V�Nu`W�$r��X'v���5�Sf��93�g�)3�v���
gp�?��e�68{�r�٤��h�ޡN��|���Bz��i�^��X�f�c`�e+`W����~N���$���I���$��u@�U+`�U+IVC���[l�jջ�˜�$���R͵*I�d�U^����ٙ�yͪ�*u�ʊS����o�=��r4X��j�����z^,x4[�&�ɇS�e6�욣�l\��~]_��-W�JZ䮬�����eumY����߽��^`{XT���ߕ��{��[�$�s(��?�^[�㳩Gnum)Bً�������?�$�S�����i-���tt�ô ����9-�R�te?�]>�:}N���+���|��C|���|���t��A�V�:���s���	;���8CR�>{���m��N���7;���?�gh3��פ�>B�0>C۰!����S2�9hz��l�|��s�֜��|~`9iJ�g5<0I���=A9�ʇg�|80)g��Ο-'Bۧ������q��~ĭ?m�����8�:�G_;�l���V��Yl�욥c����٘`����c�@����,��a8>7[���l��,��N�t�L�t�d����|ɹ�;���qv6��˾E�g|_'��y[�lզ�#ck�+�m�$a/�4"�{����P{ݧ���gs����M�O���S��ǻ8������������Gms�'p݁| 5����|�}�Ǔ�d�����{6.t��S>}o/������o�o�]����3���{w7?W�����S��Y��l~�<��X�����|���{��T����u7��Fѽ�MO�-�}�z�e��3,&��P�v�&��F���K���q2��]���"��R���W^����F�}�z[��`z^�2~3���<�}J�R�m*x��vdO�������? �
endstream
endobj
77 0 obj
<</Filter /FlateDecode
/Length 4765>> stream
x��][�ݸ�~�_��F��,�n;�I��\�'@���*�����E��n�8mO�[%����")���1�Y��i%���5����/O�z����h+���>��-��Y��G�VC���e���������K���)�����(�~�G?~}������ߠ�ġ\�_}��.J/_y�o!�����O�����'�D�E"�)AW�݊�J0[���3z[��p.ݾ�k����(�E��zO`��8WA.4�1�^.Vn��޳��_�̌�2���T#����IJ�:�c��*8Ϣ�GVҮjjάWt,lh���I��(�ƨ��ZA$�����k�P�?��%BJ�v�Z;���/��a��3$�G�|�i�e�i�h.
U�:.?c� �t[}n�Z�1�26�qzQ @)]h�PV�=��Z(c�9�=*ӂ��jF�3���p�/OZ��t >�C���'}���W��Ҵ���,�ժDZ����qê���H��aM�A�w�;*���EIC�4T ZD���N�H5�YE,�h1fn6"��x+U���<��t��z�K9H�h��@5حp�(Ѭ�T�D�(.+)QctQ&Рr��M�l�b�D5�,Č-�X�a)��ŷ'�"�q�J�Z�t�➕���U"��D�UI$z�2I������!�[�H����E���"C�=�
�P�ށ������C�?r� ��z� �DER�H4mz	�v�@�H�b��T��P��bQq�҂t�͐�B�"Qw@��P�_3P�(2��a��zlk��va��@�FK��U����D�M�4��]h��d@7�78p"�D8p�� '�!N��8q"�D�p"P�8p"�D8ĉp�� '�N��8q"�D�q"�&����w�F�p"�{��I��É�i:	�v�1)��DLj�q"��'b*��DLU�8��[���N$چۯ'��'6��R%���8���&��"��*6��}Y�4J��i<�и/�+�k���N ��(N$����9H�=N Ѣ(N$�ՒJ�h78�#�*�
O$ࠇ�D5:P�H4�D�}�|�D��UW#��,\6�Mr�&Ҷ8�j!�R�G��D`���j9�3	�;��;��@��e��O`�UE	Kk���B�?i�*3JF�c!$��\�T
�Q @G2�E��?@t ����Rk���,�9	q�Z�z�DB*�Dp�q����.���S28�U1�#U x���ƀ�w`ڎ1����
D��Mj����jR�L��'�Չ��Z�֊U\bm�Rj8d��2I�,.�*�r����BP�E����,J'U4�ƚ);ƚى�A���>����2�tS�ꀍ�Dyu���נ�� ��|D�i�cͭQ*�����2 �P����%��U5��@���2q�?*d��d�?���Pެt�5�<��J�G�R�Ru2(Q\�I���j&U��D�ߞZ@6���&�rc@�RZ��e�*Mi�@�0��,.����b2sS$!cU鴊b�V5d�W5:��:S���Ê�ͬ��/���1��)m��ֺ�!q��mpU �Pe�����n�*�[��i�^/l�i�}��6�sio�� B�	�/td6l�V�cZ�i�d'��Z�Ac����.Hw�B��̅���P�U��ohd��s����� ���_�#����u۵�Խ�p[�G4;߾ړb��8q��j-�$
�o:M����Rn�h�z�\�[ݠ�n�)O�b=t?��"�hm��[J�����;�\��%���x��B⠠oj�x����+q��2���{��W��s���e.c�a���.���`Di1U���-�;퉼�4(/�JD�����S���;�Z|�G``���3���e���Qd�l�j�����>d��z�K�B�.��67d����c����7���0ԯ��ZB2��2�0�/%>f���V����%4b�D"�kuʚ�;-��3��8lW{��x"��S�[q�*�	�e��mW��% �9B�z#N�l�?-:�j�T��@,�LRo�����67��P���Sr�M��@b%��!1c�.k%�}D�hRh�N	��%q�}��[��9�B�ֻ�n���K �3�j�;�ԝ�*��@r��V�V[���z�3ZUtN���*W���42ZsC�&i):�o��5�Fd8� �����͠�u�W�gR*�}��~�����D+��d5��n�?�+��ӌ�� ]��%y�-�(����,t�.h�.�ZP@��Ēԫ�}zc��;���zc�j��u����U�/��وo.�"��W��B����]Ϭ��T��+O�����|Ot[�n_I����j"��w\�F����q#<��3+��\;�^��$�C`���߿=�z��z����Р]�����IK�
�"7xq�V�u�� 1��Πu�ڞ0Eh ~p?P�fJ�M��V�w�Q��� %<m�g�:壷vo�[M�*d�`����|Â�D5  [�.�uVFG�~�J�TB<�����84 nN�Ĺ�OYN�ӊbΊ�I11�)FM&?��i#@����;�Ʃ&�c��hܖ�S0�3�4��q�^�,XpJd�n>�����Z��GUVU����5r�/<��@�e�s��_r	譢��h�3 ��ꈐ�Gc�o��wDζ|_3`(��@R�����#�U��d�юx�A��洮:CuU%[�-ތ �����pBt:�zR��-bpB'ͱ�\$\���4Fb��.��2�" �t�|�zYZ�=SVSeω�a&��ӹ8��,��t0
�fr��X+���M	Χ潓�|�|���ǜ���l���[|�6���g��Jd�@^�o�Btmq3�2�)���e^#�vb=�U�|�;�$����C$^�i��Hs!'m�I������P�/s���M�~�fz*p$����{ ��� ���F4#�Hw�m�b̏^�#�~�0���������a�9���؅+U�'��:�<�� Q� NG��0����͝�����<>��0t���i�u�w#��^&���5�5]�����1��K�X�Gӳg|	Vv`X�]�D����-Dg[�0⫚wv
��zJ(9 �AX�Ȏ䀸�j����H:O�^쉺Y�!��|z�s~�wzu��t~1x:������*�y ����g��W�/|끓���~��>�g��ϗ�xg�o�_���
��e�+�������x��i3�F~�D�ؔ�H�˾�x��[�e(>ؕWV�C�=Cr�;��j���a$��_���C~�D�u~���4�tW��,��CCY6�+n�h~.rv�s>�>]�V�����L�#>�Wqϡ�Zb>Ŧ�������c�*h|�xd������l:S��}�;V��ӱ�	:���C��nBy�e�+�C>���Y�{����q�@ECN�Q��5�f�$�@Îh��PLow��O4�$��~�v�w|���wL�Qdw��W��9=[��+r���uh��25��!a��/L���f��G2�_Ϙ������֕�w�����X��������f����ف���)�8qĩ�CWz�ʵ�����y�^6�|��F�����l�&Y�4^���u���ͼv�JN2Co�+Š��S�#�g��4e����U��)~^h�������������Iه��_�����_p�Nt��[���eH>�7�x&������OL�2�r��[.�5�[�>��ok滿������ӳ5W.2�s^��v�GM�}�p���o�Kܷ��;ƹ,���7G�3�߃����9��2�N��l�J���"�l��������G��c7fbmld�ss��;^�|d���/���k�����8�-��p?����Is�+_������J�܆1`(n���U+v5t(2g��>��N�cB|'t�x&�?ߢ��01�Uo��F�?yIKW��jу��u
b����%�
�Z�S���xT����4�5��Rڡ>@ukp霞r�O��,�ĥF�.5*=o�Q�IE��v�娝�xo%U;R�=h���[G�r������ݫ锛�� �E��h`/r�R�9�9a��Bw�R���Z�f��N�a��q�|�Ix�C�+�~M�FU6��_լ1TT��Z=ڰ�$��|O>�� �����>���)r�R�����D�׃�H;�̢��z�Q��D�'&5U�s����1J@Ms*���4<O*xί��;C	�x���%<W`�c�*��Bw�R���H�b	�L5Y�P�-a��K����:9ipg��ӓ�o;S㎫e3lW;�����k�쌫�Ǽ�ʤjo�/n��c���5��i��|�ж���H<�m�W��(��;�����c�
{��v���6�!E�(������6�.��,�>�x�\���ȉ'�}|Ӟ�'u�{���2�>���F-��X|�*����l��[��;+�&�[�xY|�,~m|6�U�!n���N�����k`��� �t�?&�ĽͿ��W�>�.Ӟ3�XrOe,��ߖ��N�y���d�G|��z�P�����2��d/��g�O)w��gp�^�g�I�G�۰�&X=41a���	i��ޱ2ĺ:>ɐa��@���3g"��&��!ڶ�#nu��g� �5�|l����<�E?�5�陻�^�w �����9
endstream
endobj
79 0 obj
<</Filter /FlateDecode
/Length 5233>> stream
x��]ێ��q}ﯨg��~;�ճ��+K�1#@����[�L���ٽ��g5�U��̸3��fl..����_��[�9��/?���Ŀ���z�/���������w�th�#���D}������y����/�SƋ�^�6���sAZ?С��=��gwɗo�����b��6�b��ۏ�U���|��@��Ӆ �V��@,@�UH�ch] ; _O�puЯ߮NvیN$�a��,��XUٟ��C�88�Hr��%�ŏ�~^oC^���]�]�W�c�Aa�0�N���I���.:�M)
��1��h�I��nX<Q�'�N+��ڂ����P&�U�-G�M��Aè�_���]~�/6S�|�/�3�l,���a�,de�q���/|v�Q�:�ޢ�sf[T�����7�v�&�S�����s¥�OK�0��Y�r�BJ|2�}�G���"|r1u�ӡ��)�8�}�o�������jɐ�eB�&9m&��@LƼ�?�c1�P�3Ŋ��ØN&��*�<Y�Qg�7����������zVw��'8�2����d��`�����z��*��5/X�٭و�j�fG�N��DT�u���zds`���g�;�|��h�B&���RJ�= �A[ɃaȖa>�+�3d��d����/OeJH��?f����9�X�>���~�D��j�V_�����q~fB[��`��54`l��ڙ
�0C�f ��9��`I��]�혡�3T�0C�ؘ�}���a~}HT�#���Q����jc"u�@�5#b^Vk���_&f��\�f`���@�F������#c����5>M���7qҜ�=3x'f��+30�gFWf`�3C�ܘ�~���b@}H5���I	��z`x����,�-�|�Wbg������9��J�"� �"����K���B43��w������!D�0#+30�2Cy�����X�zaFWf(Xe���3C�63C�0����29Ft�����1��D���|kFļkcw�`�w�u.`3��gf d���'	��<��g�Vf`l����n˔(�b��ΘU~�F�u=����Q����H��b̉ �]T���Yэ��Ӎ�Y&V�|�����~�,�`���Z���Zxq�@U�Dvzቲ2�=lY{,؞'��O0��c+Od�v<�����o,]y�`�'�������8�CbĖ�w<�����`��1��} ��1K�ژ��/�����Ã'��'�`d]{,�rcQ��'��c���ǂ�x���Ƃ�/7��Xt���u�(�:E�/E��!�ưn  f�T·�!K.�@�Bn��!�W [�� �)>���>��7N|�c��'r�f�&��o$��h g��Q�}��HQ�3����x3$�����S����2I6��	�Xg8��uR��dO��yU�щ"ŕ��I��3�O�=�ɲ��(aG�j=��0n�!�D�*2)��N���:6�Q�n�X����M���m�R�RX�(���r�T-��)S���Etd,X��G�K�X�[NP�Z���/��y�k(��Wd�8��G$ǘQ�S�7�G�	��~�R�%R�*
�33�Y"�	�2]�)'���\9���dg$��R�$���m��`l{��+6�#,S$5'Rt�'��4���r�$���r^��G��
6,�)���}��S�T�k_�o�+���A�R��u�RDO�$�+G6S��`���|��n8AI�ab8�;����%^D�+1��둦/�a�`��]VR-�VLn�J���������
���e����f�~���q�[��;O4#�=r?>_���~�E��@3���3�����I�ݽJ̮��q���w�Y;�k���q<A[�k�*�ԝ���RkV�8���h���tu�b�.�.ҿɄŠv�`׸>n�ڹ�Ո�U1.vUC�����M�f�qL�c�9����4��Cs�O5';/��c���'8�y�C<W"�i�s��ݷ/Q���&�4TtLc����y��LL��:�Q\��S���:��g�]��-e���~��xב"i���e]~��U�D��:���j�Y��{����u�l��Xr���G�D:+�wի����i&W���k޸t�6^_���7����Ϻ/�馩%����%q_@
��-�*��Na�L9WX��J\R���DC��ħ��@���+��mU�ĵ�v�*:?v<��}�Ɗ����^g\g�\e���8��Na`*7���<�)������4��Ҕ8rg]]J�^E8��y�pg@���G{:�z�z$uE�	q�Et�|G.{�����Q���d�k�P�Z4�;U��^���rڛ>4���t\��يf�^�h�t�v�>�Y�B���]�����=��A���g�6�-� ;���U�*�DW��C�������<d��]&�\
A�O�m1ҵ,�B��3ړp�����E(����W��`�#a�������.Н�ws�Lp�0_���ot�~�Qc�	�s?i���^�b������������f/�^�Y�%�i{A+Xk�ue��Fו`��@�%�|��j�F�6a�b�*P���1�W-e�@�e � ��z�L��'�d ���PwaqZ�a��ʻC��l��`emB��!��QO��:J����5ͦLa��ci�l7�|�ʘ����C�kQ��l�)�q���WV�VdG�x�n *܌�g�`�AѰ6����7T�d�4�8��[
vl`�A��l:��� sɶ�$��;��� ��΃��Ĉ��@(�2�l=�xMԢT�y[�l�)K�=3�b���$&�<�;p���L#�y��"8�NW�J<�����+����\�EϸsHa�n�E��ȅd\v��9�U���	n/�B��h�̨��(�u��m��)�uO�یwe���M�1E7X����|��%��y޴�����:���R�7�vj��/�����xY`�vP�Zy��hE��wx�wƝ>�U�z7c\֡�y�� �:N.W{�+aYL�[�ȗ���8�]�����W]"��u�nd�E�Kt��(Q����Ra,0�@w)�#ar�"2W��_�.�c;N��&~��|�G�߄�g����Dz=��pmƫl���'M�ݮ0�����;���yuR�I�	�T��ψ�)&Ef5݉��)t���Og���&���B Cߊ殽3�����p!����1c�j�e}!m}F�97<�����3���1��E�ul���c�����h������t��2��]vK�b��.	��ܸ��c��^�w�}2z���}��y��/�{Xb�5//��Bw+&y5�g~s��[�&G��(��7)�j�����PA���:~��ڐ�3w�u0��]?�tf�ݡ����ׄ\�ʫR��xr��K��'R�p`�eӏ�<a���}�b�fs�Kw��a4m��HXP���s��F_��ƄP_��ӹ������EG��t��԰�xE�P�6Ȼ����gFz�:?�í����asD�G	|{����[N��%�����P�����+�#'�5Z�n���<Z��Lo��z�3e�W���<��e�K9�|dU/�y�i\f�A�Yִ�"M��K�g��4����/v-bT��X^n�@?��B_�.�(h�O�2�"�
4`�{
ա���S�7�Miҍ;�S�w�Yy����;��%�G�Zj��������4��l�J�$�-G�#L�%�s69�����ʙw��⧱�`��R��٘�S*ј��G��{���}<��#�ԍ��~��S��1o����b}=2⁛��:r����t��=�8��0N����m��SmGz���e0�i�B�p�7����=�M.��`3?n�TqS&f���q���'�&�C�W��!o7�\��ƍ���/mnK�� �#ST��t��G�l��=�աՏ"��r'�}�"�05�#��dݬ�8��T�Ar8ǡ1g��u��L�^�*o��<�{�Ҝ��4gl_�͝n*�#��z���:F��9cke�XyBK2�¼`�0Z/���Y��1
�2�C.(H��P���P��@-<,E3������j_zY��a.�Z�r�veyP�k�Me9c�������~�R�3���-e9C����	\�rU\����@?�E���ja�u�1LEC�n�n�)EҾ,^�r.�����FY���2v��t��\�f�|G��k��/��n�{���+�\��-6Q&�k~T;O}pBkY}�"�/P�P�C_z���WM��b��r��y����߱XGմ�GzH$����e�-"��W�;�ˀ���7tCƅ��{��/-�,��h�������aY�ry���ᄞq�[���q�T}��2N(�(����.b���<��7&�m���'�r���]�`��Tz��fqA�W\P鴖y�'%��m�]��E�	k��.q����k�'��BqTl�ĩIܪ���&q�4%+;�ѱ�I\Pl���2�8����(���[��a�A�aZ^��Cܐ+��.�cLPy���pw/�)X�[����pA�7���0�h��"���G������l�N�!1B��p�ܖTp a�v�
'�j�0u��b[l!v��]�p~wL3<��ς�-]�+�+w�G5^��f]�2��������]��+v˱9L��w�������Y���}�C���5d�S��2Ҁ�ڜ�"�O���ϩ5�r�A<�y+����T	;+�V-�����$��nc�=�ʳ1�Zs�$Fٿ��D��?U}F�b�ʢ�k_��������iiml��%jZ�k���ߧ0���缨��$�Z��[6�һ)�k��
��X�tL��1�I��L��:����W��c��r�S�ޫIZZA�7#I~�U}ILw�$���5�<�I]o���(��7C��g�.���,�n�۵���4��/�t��5 �zo��r�=�"�$�`��=h���4�0q����ge��#��-�Fƿ�l�e�_��<�I�w��T���5O#%k�u/`��"%���d7)	��ל�l��{�ߕ�|z��/����`q-Q>�EF�-R �M*�I�������^�+��Y����h�pϢ���-���;Gs�?^��_�*ܰ
endstream
endobj
81 0 obj
<</Filter /FlateDecode
/Length 4126>> stream
x��\ێ�}��s ˼�vfv��x�|�&v����@�x���iV���u�[�y���#v��B�3)���,.��3h�4}�z��D���d���������ݬ6�e��
;���퇩������?������"�Ikch��2��iy�M^N�?�	���p�,��l�c��O�N/_OV���L/�>���&-�bb��@�<����t��A?���6���\��$f1ɺ�R�u��9�]Z\��$=%��%�����e��Rܥ��0V)L\
ӝ�W���I�0��&���d��@6��G�`�3MTމ��iڇ�8s;�f���J`�q,�/�[�8�Q��CA�����+]8J̔5�H� XguŬ�X ez;ea�B���:��,��RC �EA\@�h�cl�0L����B홰��v�F�SŒ��̬�5	*R���[K�Z�15�ҡ��r
��+]��jǍ		���!	B�@��l�'�$�[�#�!,��T; `��}��$6"!VA��ڄ:�~���	��<\z5翞D{B�f�f,�Y�ߤ/�"�
�P(c�j�y�b�n�F��Iؑ�q`i���u�5u�M�0e�+r�����$��7Aԇ�&��$��ͺ�s.tӈ��&�%l-��{Edk����/�QYHS���A{�	:	+�G1�(��Q~ܱF��:�ǥF��T�"]IV���"W׀�Uu��P`;Q2��Ci;��1ʧ �Cƒ��[���.�C�ry�oky�WCy����6��V�\�uS�~SG&IW[fS��H�fE��lo���32ߛ[E �s} ����m;���0��X<�է�>�MT'l]Pӡ>���>d�_�B���0_�Cy_�C��C�d�!e���2*��"vI߬�H�f�/�|2���2�Gd�6ω�޵P�(���?��7/���k�GǍ���ReQ[��ֵ�G7n"2��DdlY�A�MD�����K��Ґ�R��V��X
6�_r�>��U�!�:C~4��D����V�8�e�����/C�W��ZW����2���K	2��D 藕!c�ʐ�Ue�h+�Ֆ������[���.�C��N"_�Q/�ћ�H�Ê����rw�D��9+��D�tc�,V���#��Qd��%�GY�(e�S~��Hd�儮�h�8��҃���8z�����94�`�D(��'6&����1�����@��D�k�8`�8�T��-��Y�����1�hn�(��t(����-E�	�� FO��jMj��1������Ƚ+ʖ{P�T����Ā�K�NY�qs�kI(JV�cĘ�9>����d�X�K:��QrZ31�gW�<�4)��e�0�*��"�G�0��q�ψ��(Ml����K٥0��
e,k	�F,̠�/����!�"Tv��1��haL(��Lm��#�(&e��+b�HjL#�=�F�*#�9�c"V:����[M�C(X�(L�{W���z����l�&�����@�J�%�.b�%�1���a	�r˪b�T��ՌQ�"Q7�(Q7���!�����x�*���_{�����>��	�;����U~:�q@7<�vt�U�=�v����2�����LO��?T�i�i���96�a�U�|��pF�ʬ�,}�rf�o{���0h�HZ��VI�x��T�"��궚�q��P�bH)��b�݊��l���,��v�|=WU��^
�BvC�͎�W���aW�����a�' ��P���Tq��/��*���jSS�Bf,�+A�=��>\ȅ�,k��>�t+����<r5J��ϯ�"QV�>��Ņ��ber/�80����b�\�|��>�JE������>;,$1w�ݬ�C͉T��
G\��2٧���N�앫1	�lL�_�4��]��^�����;�9��,�cox]٥�+��sw��ɶ�j�v��H܉���R�j=�r	ep+kl��j_{w�F<��U#��{T#S5
峬k�-�T?����ܧ��=�b��^�Ȋ��V�,�/�R�'�Y�p72�2.W�sN��.m*^G-�1h}RT�s������>�\t���6����Z:���W�����a��Q�[��3����r`Xn��c�/�[��}"J�&�51/�Ng������y`�R/��Ӭ���W��) 1�mk� Ӡ���7�i`q_o��cXD�G�D�
`�����Y%!�35��4��`q����,"c�EdT���2��0i'%bz�eg�u��0e˽���]�AЈ��˥D��YǨQ��j���h����ai��4"�g_�<�5)��e�8`��њG�I�c��daj��/xD�]�	���O�4le�+}�ف<"P���GdL�JQ��dO�Y�A���	�;(�!V���l�GD�k�b�GDu�[l�f2��Ԙ�F�&1 �<"=-"2>
�ai��<���	]���_)s�,�������yD��#�,���v��o���G�C������>K3�v���X��P��B��}���������-2�,[�'V����W�f)���P#u%�6,�-L��E�(��GRؠv����-��v[U�o<X���Dx/U��=ب�ťD�j�c�ް�j]kO��v���[�~W��dK��r�a�7��+�]�?�<��lI�n2��9�B���U���R�-�aP5�+����=����Y�������X�\-@���Q�qc�
¤PӁο��:�)H���b�ô�~0-~V`�H�B��x�����8Z��P���8�0���	'�C)T/���"w���
 ������hڸ����Y �e͍;��!	5.��4+�}-�P�F�}�4'4Nآ��_r�ix��A���0��h�L~у�C4��%�x#B�XtR:������?`�\����.c��x�z$1ǐ��m���p�cS�æ�.�}[�{w!H��#�19#VP'�� ����r���b���FDQt�����)ȃ�J��|v<��4މ��~pUay�	�~p�c��ՎW;*��y��U!S�,;SƬ�u�Kg�{�0G;PΈa���D�n���8[\��i`���J� 熍�3��q���
���&ǒ����r��\�	g\>�a��;&�%��'�� ���� ��/�(w�pF��!g��C	�83&gF%�,�w�V��	�A�N�;e,T��2CR�l8I9���P��匘û�@9#����8PΈ�مh���AP�)gF%�,�7W�i����w��2b��g��M��Zl����w9����*��3�fD��5�ǰWiGm��Ƶ-��{W�$�uOҎꄲ'����&y�t�ѝN��nn��C�*���p���%��$>^��W�'�d�lXyr5V'|�0š����氺�T��G:)o@�\�����G����~����l�JP!|��C(��у��C����L9)ސ��|�N}b��D�"f�گ9��+��U�k�神7M��5�c�B
�r\���Ս�Y�
�Aj������R�g��͉�騪JǼZ��z7+��yH�k�����NF���^�)�姷�evc%�|�����~r���O<nn�k��O�v۵�Czi�m�r�^��3�{f#l��y&_��m[�������@�MA8za#tڳ�ݶ9)�{�H��;95Ƀ���oM�X��W�'�l�X�Z��a�ם�6�2���=�E���$���d��>i�1�)�A���?����;��z;n���6w�}��d/�j>ؽV?��9�6"�g���O�՗B�8��ǻ�n?�,�k��%���^�g��AU�mr�!����4f���;�T����7�����+ C�m����	����g��7f����M���k�{82��F];
Un��"���6����<S���u��쩶L�vS��ޚ��m<}�͗s|B��;y�e����9��[Ƃ?�=��p|�)'excR�dsj����V��C=�v=��&W%?'���ωn��ﵭ��z��>�~ '�5Ti$�*�8����
�����X��þ�E�z�G�x��B��eݶ���\zf�_|
endstream
endobj
83 0 obj
<</Filter /FlateDecode
/Length 3793>> stream
x��[�n�}߯�� j��DR�sb� 9vP��?���Uu�w��Dɔw��t�OWw�6)�Y$�� �e�J$�R\�|��~�﵍r1N��]����7��Pne��
T��ǏK��ǯ�~4˯���d����~Ɉ�[�������g����(k�D�J�E�����R����?�?�� ���02q�2`:��#����q[q��*���=	Y�1��~dv�23�sǞ�:�%����N�?Q����՝���+c��ʄY������/Jy��]TpBJH�Ek���F�d6�O����&(}���*�� Kb�`,�/<�a-�[���._�s�/Oxa�0cF@o��kTŌ͘OR���I�|:��|ϊ`�Ɣ�������6�4�G|����x_0�T��`8-�5:����aJ%��(��w��6Ća9��_.>�~��W�e�fD�C�hHĒ�>�}�B{�,S1g�3������S�\��2� ����DD�L>�F��4�K� ~�����T�Ӆݏ� �.l܌y�K�i_4�	���ՠ�9���W�Ue4%�0_�
�{=cF����d���(,�؞ç��O�!�v�I}X�sL��]UJ�nKvf;UEw���LVe��{|X��8�*�r�7D\���s�p�;-���;-|g���}C�=�ʹ�^&;� P
��zf�- l���'22�D�&� L5S$ �ʏ1l��x�`��_7��WOTl��:䐱]���U͡�9C�4�������W�8Ti��P�5.C���ufH���	@V<�����xB9��	�f�@l���<�\X�bk�@t扌u�����b�v;Ϥ6,�9R�ggS�%q��';�Ϊ�9��Ns&�2�:��^�-���oj�i��i�{�����Z��'TpO(la�eFƦeF��<���y��'�yB��	�f�@l���<����c�r5�D��<�Cۅ�]�j��3TK3{(��^}ŉC�vo�\�2�}�_g��:O��s���e<Q��'
6���|�2�(���y��#O f&�(��y�b�'�U�v�y�n�L�a)����jOb�����ޫ��D�CΤ*�^�z��P�RY���>���;-����C?�v|��v��
����2�C����T�x|�����`c��\�$UDTK)��Pp-��?E�5h�"n�i(��1�'��@��2
�V(QE�a��"$+BRa�1ܠ��0qPH�$� P<ٓi�O0<?Z�����m~�cT����Q���x(EҌ�"��if�Q����
�[ ���^ļ�!c�7�*{�y�P�g�:=O�!9K�ŝt�!�r��OK<|����=���!��7�VXq�" =�J9+f��X.��+�tF#�~����8J�" <p6�����`5�2=��H�Բ�p�>�L�vE���4Ը�s��A��M�!��n4��apR���ҧ�a8&�I3Y^e&l��
imʘ�H��Wk��Dp!�^�L�r�ɏ��B�����ң8��#�g���Ȯ�y��,��25�\#B˱|��`0;�ۼ؇i��;({礴��?0�Ȼv.,� |�ʫ�u{�b-��J�v.I:|� ���U��L:~�U����,\���~��{�=�q���s�F��n���Xc,�ɚ��-����f3>f�<V�c÷
O���1�H�ᩡ�a�,����3ݬu$��Z���Q_�3/z�c�C��:L}P����Zm�����XbU���f-�s�k3&�Pp4Lʬ���͎4c�;By�A(��$�fv�� �;�
d#ǚ7x�A�{P<5���d�>$�49"��^U�=(�lZĐ�k5*6���V���P�
׈�K�St��h�i�z�j�oZ�q�N&E�eX��$�N��NP�0�����Y���q]@s0Z�M�"a�� �w��>%��>w��Y�)޻f`���� ��n4�h��u.���݄�TQƧ��pɉ��Y�R�ӫ��bS7A(�&��-LLקG�)N�BndЋ�	�@.,�@�<k _�ر�B��봥�t��iC��<W���⤓������[{��/T2�o����q�ϗ��$c� �27Ɖ�=d�"���a�_���'nb�剛�u�q`��ؒi�x�����ȱ�N�乧	�D����
`!!	~�oD�7e�[mD��3�nX��P���<ł�PԸF_ҝ�l�ʣ5��w���x��z㧎�L���> NR�<΅8��3E9{`�:�w"��7�����ILgK�M�U�v�_f^'jr�or�oD����7`�va
!K��F2Hq�F{ ���0�߄r�fϷ801=^�B=�L�![���'8����$"�
�E�gNί��a�,��9��L�����XO	g�YpCu��b���)���C^�H6��$N����4[��U���W�*�xC9�ti�j�C^������ޚ�m��P2��e ���V�
7��/�9�'��[F��@[��O����pwu�|ΚTR����](�-���_�h�(6�`*0d�$�Tר[������Wྀp�:���\o�e�ގ����GC; �� K*_^O��gr�̵8|��^�:x�W=\��P
�XH���̰�
���(y�H�k?�(��4��E��mYT&�F���vU���˄��m]5ʪ�g�m�q�(x�p�Z�̝��6Y��f�F����<���p*�R��	7�m\9�puz�m��<��([��"�/��*7���wP~��'��s/U��ڦqb)��]���v:1E�f�k���cH�t��K���Xڦ*C�٬�oX
�q6cl��ˡ�Z�^K��ܐ�Ľx��&�x}M��y&q��tt~G�7�]W�e
&ԕ����yOd7u3<P��&������f�c���)As
��&o�3w\��wO�
i��
up�π�K�gB&ɳ�%���/z+��3�vq�y������Z@�c�v^������'�(:Q�tfD���3@���q���i�`�=��7�e&�OӚ��4��v��1%ȍX�4������Tܪ�UM�-N�zn>#~����~������n��ɍ�lZ3�i:�jυ�ʰw@����5�:ϼp�*������8/��j�D	��{\�C���j�$͵�Y�.��ܲ�ܵ�"�������㔤��7�7��)�k9yЅ<Ww�P���=�h.�75�*��}�L�����,�x�yճ������ۇ[C�]��C��rf��x.����ښ�F��愩v-	mL�9�Iu(	���懶NF�$�������{uF�L�-ώ��$�J��9�i�^�r�)��y�e�^n��B��}�6Q�Y���R�`/��2v�_���MZ<�ޫE�:97�g�tP�֯l(^�C3b�ժW���i�� `�8�z���_73g��к�7;"os�L��[ֱu�78	����)3�OK��{�A�\=92�nYq,;�vOy����#�����ۘ��؋�<c=��Wru�T_qs�on�8�n{�������a\?9���mE[9{��a�{���&�I(�R>����vN����<�c���xV�N�޸cM�~����� w�m�����W����=W�H��Z�Ý��'3wV}���������������7rw����f���K�>ejg�3L�c��7ڰ3R#�95>1:`�?m#����������(��l����9���erS��;H����e��n�
endstream
endobj
85 0 obj
<</Filter /FlateDecode
/Length 3049>> stream
x��\m�ܸ�>�ħ��8 �ݽ�m�H{W6������hQk���{8$��f�c�/zH���Y�~&>��c0r�2�0}�r���+Ĥ��������/��nf��R�gh?�@9៿�4�7��r��'=��4��z�R)���Dxi~�>�\~x6S�^~����r�~�A*;)=�|��Um�^~�8���_TX̚��/-!��2�B�yH\&O���-8�mV2x&�tk&j�����*�C��zM�\ѓ\9�xO菷G�*��B��]�/n������0�"���v����$��� �LJY ��vv0S��X�(�c�?Him�j�
<�D/2���a.��]a%f#��ӗ�A;�zz�3$��8m�,4m�E��넎�g��.ϧg�����bXE��+��0���se��1����:Z�@S�0Z�Xh.�@�h=]	�� ��h�����E�|z�O���ԋ��,�U�DZ������aVNE��D�����A�w�;������a�A�*T#"E��bcm��b�h�~���h��(Z��K�>Qf��T��4g,� Ӣ%铤HT��ypV(Ӭ�L�L���ee*�(�i��1�g�e���d��f��XhiF���^>�^*B��Iuڊ9.@Eguqը���xE5R��j��e�����T���ȼ���? �b\��)��rAL�����a���/����vVQ�� ���`��0��$��5�l��8Т�!�4��"$�
~��$2X� �Hv���D(8d����	 8�(D��>J�ɸ���W������rf@Ą��F0�`ŕ �TfYۖV��r���
����8!-�A3����,�̪�
��=3-�U%�M'K��*׏L]��5�|��q��J/�W@T���D�)�Ş�ߡ��*����hk�4��M	-ȘV
=2l :(;�s"{��D�Ї�
��*��UAb�r���-UF��ڈ�h�h��0�
"��4̔w�QmL.�A+U���յ����e��\��z�3 6�� VH�3Bx
Ibq����D�I��&�,�@`�$�-m͋�*�Y,��ӊT.��qi�E�R7�)�m���vO]6[�\�᷉)�Z�j��*L	���4�{PjV�U)�P��{�	��K V�3υ��w6d�����6>}G��<Ws-�m�tݚG�F�x4UtOG�?������3�2������{�ʗ�Lwn�/�����S�7ـdA>��*h�ǖ/ɔd0YNc�&3v�/ܮ$-��O�v�����1�2w���}K�UCl�`xs��� �[���`\�1�$W�C��fh$!�yM�[:ϫ�Y�VU��"�>E�VLt�������W�>�!ko�U(+MH�i�z+�
�	Ԫu+pGQ�T�.��I��5�/;n>�S�硅[f�Z<3��)x��UO��X!�V�mu��;��:B�.��o��&da���kQ%w���n>�!�r�H��$3х��1� ����>@H
Ѵ�� 38�l�I�-)�b���y���.�	tfO_��u/L�!3E�3�|@v2���צIt��'2�kOoH,���?b.�[�ͥbIdIH�h#J���7�*	��8J �ɴ�c�N	�9]ЙvZ4%$�Ĩ1�k��]�������v�甞�չ���B���`�����:m���w@]T��oP�{>7�����j.W�X�2S(+ �%EӲ�d*V ,����ԣ9:q͇,�\�Rכ�v�f��<�d�#cri���U�8,��i2�"H=}�Q�aF	���Z������l�WTN&@ۣ!�j�v�� i&��R-�G��ìc�WZݕ�Eǰ�@��Q���g@IJY˪�;�|D�&�e�Թ
.!7\�s�m�ҶZ�)a܁�65�q�C�2�������ӡQ\I5��3UXyD�Ga���f�+���.�N����.�蔽R��-�e�)󾷁�i��p�$Z��+��!8.���%UL��=j{���	E���ޞ0y�LݖMG��n�nܮ.Op��SB������҈�\v}B�8[O^���WT���\׃��N}]��Ru俹���d<�Io,�y�5�+�s���
i;{�)�J�4�m��`�^Ц�����+���zZ�x��ѡ������}��Z��W�蹄C��&���(�s�Z�\�3Y�+���=W�\�W�E��02W:��ט���n�r���D�4�c�P�s%��(��x�l{�Y�lBI�tC��T�,�N�"6CSR��1� �o�j��f.q�J;��߫��Rm�MҺ��r�B~w�5x8e�.���H@.�{)�O\�!3�ޑ�y=z�sDFLS:=���q���g�4�ÐD�{��O�^����ɘ�{��>%�J�l�_�VN��ڤ��ӑ�gc��a����U�����E��a����ί�+Z�΁N*�[��;oh�8�@@��Y��P�{��"��eۃ�
˽\�ѽ��N�*�㛆<�U>�mC����-3dI���B}�q���qNp6;Ib~Ğ��_��6��y���鼶j
��J�؍u:_�SY�mp>ps^�d�Tlܱ{�[��t�*�>1���a�,�dI��e�I� �OA�n��9���z������8o�I���h���Y�$������Ò'1Ɇ<)����C���;p�:$�,�9$hU�	p���X�����q��������(�x��-��T%��R��	��z߄`�N��k�3_����he/��&��\�!s�ރ���{���=ٳw�����M;���Rݻ�܈����9d~���B��m�^������#����򌽊3(�{��,�9$c�ugO�2���B�RF �z�����	r�m䍒CFQ����+�#����1�-lI�Gc&���$D}�-I7cPƈ�)=|�j�����vC�6;�U�3N�5�Wڼ�-�\�n���j�o������B�X���#�}l�}��{ݙ����;��Z�ڈ7l�`li��@��T��
endstream
endobj
87 0 obj
<</Filter /FlateDecode
/Length 3206>> stream
x��\Y���~�_�� ��> #�������F�
`���꫊r���F��F;��꫻�ѬtL?��?fv����1L�>_�����1i+���?/����o��Y:��
�+�('���S~��o��~��o�I���')���~M�C���z���Lqz�J�I�����������}z����篿L@PaM0k�O�Z$B�_C�DЍ`��&/����8�6+<�\��&j�����(�S�pH�&���\9@|��۳A�4[�5�k��mf�P��f�)�G���EJ7;�1��v�gRʂ!+ig+�1�7����R� �,}߮x��^dÞ�����0�k(1[�i��>����/:fH\�	8m�,4m�E��8���	g�����k#b�)�*�_)]i`�0U�g��T0��8�=�Ђ����*�Bs!�dLE��H`G�ƇJCw�o?]\����f����HqŢ%��s~���aVNE��D�����A�w�;.��lEI��A�*�H�"��@�F;��^�g���V5�gU�]h|��Z����4g,� Ӣ��'N��fe��,P�Y���+�e�2�b��Dx�w�LӢ��'S�6i��Ҋu�R�]�]�Bh8Y-K6� �$V��Dd�\����I^�Q'$��ߒ�����"L�/ƅ�>�PĔoa�[X�������
�_@���8���
 ^������@����&�Ae�Eb2d"���Z.��$:�I�P�+p $�9	�|p �MDBB���lM� a-���02�9�٢z�@��|3 bE,.SZ �`W\ J0��YwI,Ф
�p|[Qњ�D[!b��\!��T��- �f#h�"��h��J	� QQ�l�OZ�}H��#�5�NFA2nY�'Z��������
�jY-nI�s��0+Ș�� ,�;���&��~/��Xq	��q�C�kZ�P6 5\"�lp.6��d48��:�XBA4���b3�����<�A+�B�#�k���Ȥ
�`|��
H��MZ�l��8��,��k���*�,�"2P@s����&�+Tਁ��W��m��5M3��SDܰ�joG:���Fd,����R�)a1��4d� �k�뱗�BX|)x�//�=C��K�HBJ`@"(FRs�&�Ӑk.��|'���̖c�` ���1M	�0K��nR�!��VC�l>A�2�k�>�RJ�`2�J{� �Ё��'@"�g��8|���DB���Y�HB��2D�3�������K�N�Ë2��X24$�ћ��z�qCgh�NIt�B�gCqDy�`����5@��ŗBө��P�C�i<��%W�}��PV�u]K������$��%��kSB:��~F;����f���0�t�h/�-��@<���8U�0��&W��)����d�a"��qK��J�tp����Td&Ke�Y��������0����qWt��������x�Py��E[0���W�vq�+�Ph���9V�-���j�i5��*X���d�)M�`�0[��ƼuB7a+H�1vts�\�v�Ӥ��à�nx-�ǴI;|��^��ӌZ�pG$�w�9�O�T渒�YPÀ*^n�-XQ?S5�I=�K0���^%�D�����Ů�f��b���+���F�-9�#��b��54��wrP�?��ՓZJS���?�U;p�X�6�Ek����Z�P�,��e�t�c�r���8.�.�GZ��X���\)?k9��|��^y`#T�%$q膠���k�D(l3kJ���,�6T>54�&�7�vP�(:-�.W~��.���J�wG���,P홐&�H�,�:R	OL��� �����0���.�/7��n�zW-xM`޾�V>(�֔�[� �x��R����\ץ7ǻ�C��4��j�N��7A�I`A���5�&�%H�ƭ��>��U�V��c�7��a�t�w�t+�WQ�*�&n��]+�#�Z�sVGD��X5b�^5Ҭ���D��j�ɋ��Y��M��R$�U8������}������[��\�pP�@4��u��کXkRm�%�zt���F�[8�ݷ��6恥�iK]�SD�T�ֵR��4k�e�T�,�l����w\w!vI
�d覝�Kĺ�~�~��q��x��	3��+�� ��r��{�|�����Q�mI��E�du�פ��&��Fo��TC���S>'RN�8\C�j�K\���7���#�q��K�_$�A��[������i�����W',���S���q��� ��g;�&�f�G�ks�K?��N�ى�:^.�X^�U?��z"q����8+���,�N�^����s��3�L>�E�@l�R��|2�c�Z|О��v3����-\�a�F'ҽ�L/�{��D]mAyT���!mٽ��=�E���&�'J~MK% ����zj�ӊ��ђ���
�gVy�� ]�L��|�;��n�:\'�qZQt��Jj�k��b���+��EʓT����ob��Y�/ؼ1Q����EOT�7k��m���atJ�3��qV:��0�}��JO�Ռ-��cmH{mH�ǧaM�Sړ�)uV���_��	g<��}FC��2ge�u�}�y��@���c��b�ɤ�P��[%aj�y����(�b��k�����D.�)ƞRt��V���SV]���|j�}�+��Έ/���#�S�nJ U��N/N��P��u�����(�����ur���PN\x��?�6pڳ���|��;�qf���`��heޑ��{X�v�R���_'~D����f��zS��z���Z�6��B�:��J~gv\6�v���>�!撒8 C&f��v=��JA�6�Y��=6oL@׻I��|�X��O��1�49�!$}�2�;��*�TZ�e �O<7=�Q*:	a"��w�l���#���j��x��V��HU"�nK�gO\�r�c�瑭�����S�6"� ��
t�6���_�;_��>@�ΟwmXS�wkM��m�Gю�Ї�?�g��W�"A���{n�v�"[�0đ��ާ�`�7N��&X���L�;�C-Wp�򭪔+��_���ȃfF���C����ۯT��s:�*&�P��F��I����vK����&��;ϒ�f�o��6�~���/=R0�W���}d�����g_9M3�?U�$���
endstream
endobj
89 0 obj
<</Filter /FlateDecode
/Length 3285>> stream
x��\ێ�}�W�s ���<��}N2@>��n������u#��Rw�J�n��QS]U��HV˳�1�L�|��e0r�2�0}�z�償+Ĥ��ӯ�8��ӿ�nf��V�g�`����_~��_>��~�O��G=I�N�S��5��[��N?��)No?�D�C9i?� ����޾��(�����ur����' ��$�%�'�o-!\�C�DЍ`��&O���8�mV2xƹt�E�b��;��\Y�C�%���8WAN4~�����`e-���%��63Z(Ό_2ӌ�g���IJ7;�1��v�3)e�J���Lf=#�p����82�ިm\+����������0�s(1[i�������/:fH\�	op�hYh�$��B�������.ϧg���Q�bhE��+�+`
C%|��Hc��;Z�@S�0Z�Xh.���h}���;�y�C��;Է_N.�v��W�����HqŢ)��s�[��0+��al"�j�a� �;���XQ�0� MH�H�"��i�F;��]�g���V-�GU㿟��D��2͛i�X�A�E[�O�"Q����Y�L��3�3�;W��u��UGY�H���i=Ӵ(�+��T��DV,�4c���n�'B�NH�i	s�B'��@Lع��+HI�;�L�2�u�G��-ّy���?1@�)�ŸPߧ�悘�=,|����YX���0���� ����ȟB�r�+Pg%�DG��ҜL������O"�Y�,�`A�
�#��V��:Ћ�"1���"@�T�`�f�QzNF;G7[��� �(,_��RC=�1�� ���@����X�'դ	
�)�}Av�>�[C"0�d�!1�A���@6b������v"�T�
I�U�����JgS�y�bdʎ12;� ��]����.�N �A��U �d�a7�
2&�Yp���U6��&�Of���?�*��O�*�[F"Q�Qe����W�?� t��BAp���n1�3*Ï� ��J�EP>�����=�K_�L��'����~����̛n��n����y�H�3��a"i�
��U3��!T�*k:�ST��{��ɹJM�5|U���f,"�?�1��)Tϥ=�tU��;JIU�WW�^�-��S��_acT���{8��R�S'خCV͒V;3�9o�2�^gxŶ�\[0o�[,��X|)X�~ò��{�gx)lٔ���[�{^�8��D�m�!lw�ZY����aߺ��(�l��΢g�a��]�%ғ�P[�X����
�'�wx���ri��Ne������i����)�`��s����D�`WA�UXF���C�g���[�{P��\�g.c�3��zϊU�=�U�d`k��A�a� ���j�
���iq��\Ѽ����% ��I�na���"�����sAtY��oOzL	ב/��y
�Ӆ�+k��h���"���H��� g��G�W�'�sI�f��*J;��m$��
��;Gi4����@��Kj�.���,�hVgn
(��!�ho��c��~#�qR���g��|�JҠ��ѥ����K�*��P>�ɲ|n�<m�/�eT2�-����IW�.U��{ٛ��7�Y�LS�'S|5��Qi��x��7�Wm��ac5���Q�5P\����[a��de�Uwr�lS8���u�g�p��mʒB3�\���
^d�.C��N9h3S^�;1���&��?���� k�_Ri��]�S��
��}	����ih��}c��테G"��������s�Q����`���+�*ѓV�ɥS����L@F[���X�e��/�����B7�v~<lh�EllE-�}����c��*�8�5_��ˈx���UZ�ª�� �J�D+��� n��*�..�l}���.�ɽ��c�����$��bs�`�k�W;�ܓ����)�*����.���]�@�+�j��L��U^[�49k�U��Y�)L�[-!���+۴`:�iM��}�������TS��^�j,�[��-�!��XG���(:����Hn)i����{���6b��i��xL<��[y,��2#�����ږ`D������v�cF�u,u�������`�;��,g�>]��Ɗ���z�~%}�}���1�(ւF|�.�{$�A����o�d=z���'�8�9Z
���ƌi\�8;p;݋���2�W؇���K3?����{eL2˓�,��1�Ҍ����%���n $YU�G�GBCIՎ������>�W��웘n�:��\�c���؎�B�QnFͣ͊�<��6�Լh�#��J�]�8����>NU%�0�^˜��	���)���V�*m#��M=?����sc��&�ɍ�<��."�����-4b�U2?>�.4��P��DMeң��lm�]����Ƀ��7��5��d��Kd��&�� �!�� �t��I��lʬ>����E�$}����Gǜ�1i^�q�eRX�K~d�i�{��
D��+�T�x�S�	�����%2kG3�l��$d�%�Ҕ�%L�yE���݀Qִ��.��C͵Z�s��A�<����!��`�+� �e���]�����,�B���!=k֏Y��H��&,DMU@}���<�=x�z���^���0_�d_hگ������C��j`�i�D�QI0�iX���ʮ�5�Ȁ@^w{>�.l�}ϰ<��Z��b��y�y!���)kc�ځ��&�%d�/��T��*y�{�*�t6j�Y��(�y$����.(��P"�s.j鐎�j��)s\���S{ڹV���Y��[k�~^��k!�g#R-��K�7;����F��(��ӏ�+!�PG�X�ɲ���G������{" ��U�ͼs�
���կZ����r�����sS��pXs�౭�0�Ĳ1#c��-N�i��$�4��ڢ��]����!�����%�fo��=)��+:�NtX�f��h	����$�Vj��ŨvT���ԋt�_:�_�Ѳb`H�
�n/U9�M��e<�ay��}��GL@1��>xBz���#���G��T�w�^��ǆ^��#B/�3�����@@=��ݎv�c�����a�>_�W܎�>��d�J7�c����Q����(��Ga���(�Iu 
����(<\@�$�M���7��i��֔l�3ҞGR���.�uk5����Z)�.k����:�[s��R�EIN�_J/5N}F�xOy�!X��1bq�H���|C��H77�;�K�f�a��%�����/ؔP{
endstream
endobj
91 0 obj
<</Filter /FlateDecode
/Length 3097>> stream
x��\�n�6}���Qx� ��[��k`?��I��,����⵨V�(7�������v�<E�3������w3y��=��Mo_O���s���f~��?��m�����q��\�'������_N��(�_��^N����$��0����������3L,䓴�u\�I�����Ƥ����ߓ��_�=�@��@-6lH����,/�E��ϯ�C�f��%�s�T"J�G,]9�d.��#.Y.�D<mw^Y�W3�4wi?�>�d�1%	?���N��������3c �I@\�f�`�3�W���ཐj��n�Z@%(oY��-�E���΅0�`��+����F�zz�7
���܄�T�'�TAf<e�~zë�����l%�c%�@T8Կ2� �p)��L�R�5�Yi!OI�8��̔�'�q/`��6�sq$���2,����d�-����,%Wu0J�F��(���(7������(���;(��ZC�6�VW$>(�N�D�H�o��R%�$/A�S$(��W�俟�� ��PS�7ʌ�Ă(�:[,E����G��LK<�2kL�[�Q���X����(�,�/�'J�TS�b���ux������"��H��V�Q*:���գ
v�{���Z;5���h�k=��Ժ�y$U�v�7ſ�.��aI�t���mY��,|[�b��?��/��Yxs�9�PC��1p���(�{��(Gr
�Q�wQ�G������ {�94$@@9�P�G~��*.@
 Rَ "�^��s��1����Dg)��3�h)��Z��di�X�H9`$i̞/�)Na�$'a}oŘO'��I
���P�W��	�a=� ��4
1ݸ��e�u!�9�D�y��'S�De5��aĉ���*��G��4�C��p�b��9�����;C]��@���G)�j"T�``V�-�F�p|!\l��A�$hR��4f9���jg�hkV�QX3+��H��K�8#�G�u�x��&La�$'Q}?�IPl ��NU
,ZYb��*��&OPi�x�ib�q�e�p.%b0�D�N��Du���v Pheo�������q¢��%h�RV;�Хr�P5}��M�u��^Ø�4~<,�N���Я����pA��$�����Sy�g�ζ��d���h�r�6@�m���� W�|�O@��#|���c�����,�Oq��a�"]cb�K �8^=�p�|�%������هݓ�V%c�ջ^^�.:|�&�d����KP�|�B�[�$�9EXEy��K�B��ܖ\���(�?]��dCȎ��t�#��>$0>�$�TkC�-\׃&!����^�0/EAz�$���o>��'�LB�S�QF�N1}���c1�!�m@с#)��o���,e[����Ǧ�����I\z�
y���
��Հ��g��
��,�T�;�E�7Tilgf�s�1�Rxe�r�Çhj&ɺa��:蒍*����b/u��E2Q���AУ�+����C��ύ��+�r���A�����@&͌hM	x����
M"�am�`\x{�_�TI��ڑ��.TY����o��l�zvi��&w��M��4#��N����Č�{ܕ\���U��7��V7T��e�T�I٠���R���R��}��4g1}���&nv]��2��J+(KMl����bfy���%�j� K[�>�`�y.�*��m��g&�Ҝ_*�츤C��K�E(��+��)�>�.�+�8o�[)3����������ӆX���$E�׌d�3�>����[�/� 9
� �+�p�}��W^���.$�+L�!��}��>�H���<��8�����w�eX]ao���qX��l�o{��.���n�ri�_��U��uV��YV�����uA�2X��jq�)q�e�餩"�a��"�on�����C0��.d�uf=�_��B�X�<ޢH�Q��u����+U�Q��1��r�g3o���Yیy���P���X�K�M���<���(�[�����n�4<Wؼ����vB�B\F������k��l��_�US` /��j����Ǌ:sm�]`Vy�&So�8l�K{:A �z�#
��O�S_�8�P_�x��{������*y�"/�-�Ɵ{�Z<m=����;�\�����"/��T�f�N�ME^'�+G�w�5�����{x�th�7�ܫ���!�ZS�u�N���q>�����8�uH��	���i-�'Ն��<c�p��H�<��zH�<Q�ñ|R�<���|��hO�/99�B��t�y�{yz�1�Tz��*�c�
D(����r�Zذ�V��r$ͼ��s9җn��G�v߀���p��a���܆��u�c�A�o�U�!�`�#4�����)=�"��:��g�UݮXhD����nL����x�"�©��U�<�S0�E�~�
�iD�l��D6�n�>TX�� �:J��S��j�H�����k�_�b&|0D��sT�����g�]&���꾎ze\y:j����q;v8j^�;v���.�ǐ>.ũ!�J��?���?��E|o��?o���㘿i��uW��b�$?�@�Az{����#q�G]��CHc�ȱ���:�@�0��r�"�;�4*]pP}ϨA���ıujm�
K�Y���
���,��c����N5��g#�n�Dj���q� /���!e�Ů��3���� ���GI2��e��}�xIޱ+S�z��_K�7'Ms<F�S�9?�WW|��j�$�5��5�����å85���xu��|��O��%G�d�sW��z_4�$WM���֑cI2�u�iz�Z��:Y�邂��)� �U�`��:u�d'AH0)A�Ǝ#��+o�o�L�zi;`���,� ��h�H��v�8�y�>K�M˚xu�W����Qlc^�;vxS�y{$\��[<\�.����6�����ǚ��,�Xr0�l|\�t��L����p�P�Iu]*j�$����&"]P�}M�,���2N]꺏�Oԏ�O��q��	H��'�? �\t
endstream
endobj
93 0 obj
<</Filter /FlateDecode
/Length 3000>> stream
x��\ێܸ}��s k��X����d�|�7��b`7����TE��͞���cϸ���O�#�G0)
�|��h��tJq����ǉ>�`�Jß�:��/�PnG�qh(�wx����ʋ?;��~�o��� u�f������r�����+*����1Dn 3�|=�U)�~^~?y������,���,��:���\�$-[�>�l;�yA� <�~mVF�G�C9�d�mւ�{�C�CČON�m�v��Y櫕Y���_]v�(���2	�?�����/;��F�<�C �v�GMf3��Py%.��!Z�Ɣ�:�+���
��P���םQ���V��kyc<z=��K��ĢWq��X�'��Y擂e�2i�BWG�/��L�rQ$�cV4�?��eS�T�g~��O�	8O�,j������&���.t*�0�Dwi$:oC�eT��/'����ލ�h˃I���*I����2�S�C��M�9�_"���a��+����t��I$�Qɧ*�$��;�e8V���.W͓�z��Y2��-2o��Ȓ��Ϟ�Fp��P�9"�"�Oy+9*�9G%�$��^d�Ȍ��o��"��<��,k�����,o^O��Hb��9� ��]]@�1�e�KUp��v8�\e2�\�<?\�<��ʿ��M"�/���un)8]�S����m�{[�?k��m�����F�5�g1DL6�.���|�r[�vč{H����ԏ8A�����*ҀH@�}A' �
�q�l�����Y�P�P� ��$��A�cH:Tr���GG�$��񕔫,��6�x2���0�BJ5bd�8E��Ny�:&�H��J�:�����p���ӥΑ�	�4	1�H�-��s��
1��}��'J�Y�c� -"�M�x	���4���Gc��kyTcPs��Q'[�蘶$��)&�:�K#�J�bLd �h�^q��4I��H��ѧ���Ј��ek-�M�a�j��h��Q�Gi ��B��]�$U���I.��zb%(&��=�9�d�	�7\h��)c 	xs�$D�`�8CBH�,h\��ؒ}�b�'ik��گ 2	�%�-��`��l7����^N��Z§�|B�J���₈�e�3�-����\��X|@m��U�#��-)�R6Ł�@G��_W>Ǘ;���Q�ڬ�k	�-�-����{���p�Ƒ\+�㘼�-��}B���|�΄�F��+S攃�ܵ rG5�j�R��Ք_�z��w��t�)�'t��*�G�e	j"�:�E�)�xvyO��=�3��xT���l�u����h֞;$�l�V�s�ʳ��P�eƓA<����s�ys�|�w�lw{z�1-�|�>�����3��K��U��R�;��Ư)�k���z<��ȍ�=�'�6Cx%�V��Eݗg�P��里լ�?u*��C�WbG6?�y*c����ѱ5�9�$�sm�#��# xrC\��O��uOS������F�ѥ�9_��Z��|t��'�þt~����'Թy�&�ij�~jF��������]��i����h���O�?����ΈfC���#J�@�\E�;��m}��d_�Fδx-�5ϓO��s�>���������ޜ?(����Ƕ��~ʍW���1Z���"����<���.���.]�Kn�{M��mM�~�H�JO`K9��ae?��s�����<7�|;�zy����PhR	�����P=��:��Ù����&�%�
!4�p{�h����[lw��x���n>�3�����2�� �2�M��** NO��	iBE��ȹ�=��G��z�#�:	�cN��e/b�D����T�m�]�z�y��ܻ��)t��X?ڹ���{#p���3�9�����KW��?7�: �����$=�����q�jrvUG=/�S��޷�<��t�&o�@�/F�y�RL>�|Z�s�����̊���C/�F�7���Ѿ�oZ\��=C\xOi��E���<��[��t��>a �ޖ�� �ܖ�&;�le����z��<�љ�n�+~f�4$�mSt�7���t�&�д�箅DS��&��o��Ռ�kw�n@���):x�=�c�*�Ͳk�ܤ��๩Ƭ�{Q>l�ʧ�X�G�r��J��#�6y������Yi���ö;�>uP�{tZ>��5�4�����lݧR���z��rk��v�S�w���S�O�;>����;=�^�j��*����&'����(��Uጨ�؟�
�<�g�ݓ-}��w�af�ؿ>�p�Q�+�Up�!�����!ׇ䊑+2ޗ�rn+��$=�9Q&�eu����M��Y�T�
�Q3W}PM�1�ׯc*�{�E7�Ѫ��]R^��_*���U�.Ie-+f���V�d����U��Wz��<Kt�n@�(dwVN�)����h���Dh��,��h� ��r2M���,oŮ�[�,4e�܋�bK��Vu ��V���[-ewģJl�G�dF����Y��ΜU��}�9�������~�B�U�G�e�`��g�ؓc�mZEz����g�؉��6�"���Mi#��ԏۀF� �T#���&�x�ǆ���r>b�aEO"�;��!'�O����򐓁㊉�?:�F_�'�C�V�����e�L��l�4��y<�s�	���·��5��=�j�C��Mхǳ=ǣ)����_S�����Дnb{P����׎f{�,4e���KG�=�@e{�-'���	%��s��=UF��`���}ٞUP{|�Q��&����4���_L�҄
���7Cțu�o|l������lL"P�~�#L��T�ן�Y������=�ANkUݯ�����ˊ���?tTIy�́�J*�8�Q��q@�#y��RI��8���S�{�8��&��<N�I��):�x��� �
"��,U���|���87���Ě`�=�59M�v��ͪ�?���:�
endstream
endobj
95 0 obj
<</Filter /FlateDecode
/Length 3420>> stream
x��\Yo�~�_�����,Y��$���;�n�?�*^U잃c��ǒe���_�l�J�����aeo��k�1�����o'�\� mE\~���Z�t�JM}����i�/~����Oz���i<�"�R8�/�"�i~M�>�~|5K\>�%���TvQz����g!������'��y�
[��|"�F�"��1�L�6w��`�/�3z[��q.�v��d�b+ʾ�VRo	Z\�\��xaڟ�bo�2�z��q�-�Uf��
߿��t��/�HT����J�����zE��)�+����s��M�V&z�]z�:���ߞc(�Z�i�\>�7�!�������b���`�����M��(Tk't\>b� �ty<�z�c�*��D"_)]i��U�g��T��a;�=X�Ђ�Z��*�Bs!`gLE�kK`[�ƇJ�@�/?�\���'|�j-5F��(��h����.�U9ciV�i�y��.��_��ɠ))ZD;m#�hg�K����Ҫ�s�j�O'j�(�Vf�q3��8ȴh+��S$�U��9�iVy&y�y�޲�2��(�i�1�g��~�>�j�YȊ��F������ͧy5'O�a��8��jsb�����ޢ��D�Cʤ(�Z�x$�PܒY�<�DX�?��uJ)`.�)������=-������B@.`�UE�'���0�����+�$*rd$F!C!��P���L��/,h\��'2x1�^�2,U�(��/�2���SV��$4jt�Ec��@���I���ʎ�!�H^ę�'�e1{b�H�_�Eu�z̩�[h/"�9x�аL
1Y�*p���V)-����RP�Uc�����4� �O�✐]�gr �m�=�~�VJ`%��N%�"(�V.7Ta�k�]E��d"ʆa�=e�[�N��)F�"�
�h*!�
�)"rX&�f^%2LG��H�U��]��u�BA����n2��jT�.�Ky�pV�N�#�k;i�3Ť��Z4��D���
���4@�`G@�
ڥ�^x�OjX��\�����Qh9��_��4-���4G3[�L�0c��Lo�G��V,���a*���R�(a0�Ռ�)��y�A��S�KXa��Uh�.dƶ�����I�ፂ��X3V?&�����6݀.L�0���ٗ���}퍸�=��]��������l!%:+E' U[�*�g �R	�%^��` 4�(���L�`)�E�����Y r " �@ ��bڕ��G����A�Hʲ�-H*�y_h:�`�Ld_D����<���Z[�+f5N����Я_�o������|�.�~�?��yڴ�<��5�s9V���)��$@�>|Ӵ�O�/	��c�'Ƞ5N�9cQ���yD���5�˜���"�ƞ6N��d���QsHd0���܌XE\تe��=<Bh�A��n+<��S����Q��r�hN�p?nCO��V�������7�B�&����>���8��?*n�	w�����i!N��BeQ�}���%�H���ڼ�8�>��L+U��_����S�$}��e�at	43����
�-3���������1k�pҮ�`��1����4����������8��+JV�{�:�� �}���E�uw_=c��ځx�_;�ط]�a�s�fx��j�qD��A��TaZr~��<JY@M/h� �G��S3����:�"F���3���h�����K�>�"%-�o>��j�V>4�l߼m[9�%���kg�Ȝ2���ڲZLM �v�iU`b�����t��^Jhԧi�����&g�A���K�dz�ǻ��~�:���Cl9�����7�$�rO���H�rB2�O?���_��.�ٟ1�L����D+�q���jg���/�2��l�n�vﯘ֋̌�wx��vJ��ѻ	
�^�n���d�
�kO��!�R���Nǳ�(��BJH��"�Y���5JЉ"[��p�˞�ޗ��L��u�a�������Ll>�ZP&�4�S��?�`�Y��Q�,j����(�&��T��-������9Q��yV��.��+�7bh(ֲ2s��İ�{�a�K^֤�T0��Uk,��}��۪඼8V������p��.n�~�>�U�D^+��а�cN�z��9�_�������ڞ�l�<��l����^گ�sh����0�U��A�
�y�
9"[��1�(g�' ��'FI]
:UF��&ٜc#f�����[��:g�9��4�m�z0>���V䗬�K�uEC�C�t���Zϓ]�;����nH��1�_m�؜�KZ�vK��­,�~�����;���&X� �����I:�<��N��ϙ���;�E���E�kM�&9����҈1i�-�Om�G�$��:ݘ��K�j��T0�J��D�h�rSS��5;w2?b"�E߈�̟�
�m����cn0�xu+���	M>ӯ��@�#���0���~y�,����k���2NS%��%�q��F5�#y�|}X�Zؑ+�l�/6��_�ۇC�fI�}O�6�������<��S��>�fc����tA�wԥ���>��j>�-TX��;���uh���cH�Ҿ�Nl��������s�7'W�X��I�9���p������Jn�.G�"��Ӷ%3��t9(Ϥ��	��9��>�q&�Rƶmcf���*��KQ-5��-���e3���i
n��n`YM��Υ��K����m >�G����-n�k
���c��4�Zqr�u���3�{�m�����T��H��Nv���1��)WLX�X�y�Ğ�ʠ?�/}����IE�	9��4�|�U��դR��ԑ�U[R�ۖ�sJI<��{_HN�dC+ή\"�uA���O��|晴/�(A9k�2���.��
��~Ya�R.��u$3a��ntF�ݽiv��q��N=3�(G���A��XQ~@���N9�uf��0�2~�Z+��[#sj*4��Sk��%�����L�礸���c�i�3�A2n�)ŌR;��0�t�5�zt��K�n�!����1� ��Q��c�#��0����=� GزBػ���wmeh߶�1�Rg�\�oe�X��+�-D�W��+�7a�(!����ZDE��:��W	����	�]��v�y��a��[;�����pbY��4�eU-��As��|%��]�h)�v�Jye���˥�%侞���A7��Pf��_d:�/i��e�aI6� �vlꈢ��{��J�t �f'>���'>\ơG0Y���3�#��#���%!���4��b[ir;@0r��"�[g��;w׹�V�;�]DEP�U�����F�X��v0R�b[s}�3o������E���JQ���N�\w
�_�����n�8�
endstream
endobj
97 0 obj
<</Filter /FlateDecode
/Length 3924>> stream
x���n��]_���[�,Y��$�Nv�����B�E�1�5R�=N,{�NW�"Y���tL?��?�f�19Gc�>}y���W&�I[�����?L�����K}�a�	�	����)���ׇ�~�ӯ�I���')���~I���7p��Ǉ�^�����D	C9i?� ����>~y����i������ � ����E��sH� �l��I�?�#|���a.�z�Zd{Ś��5;�^.\q	s���i��)�h����ב�B]E�	����)����LY�,���vv0���Q�p���{'�	A� =Th&`�Y���a��@�C���H#��%����ZdHH�	/p�hY`��\�]'t�>�� �ty>={��T Ɓ��8���0�O*�;WF*��:�=�������*�s!�`HE�땀.^	�*����o�>�Yki�b�8�dє��9�X��0+��ah"�j�a� �;�'��8��K���0T &"D����5�Y��` ?�䇰*�<�
��]� �Vf�y3��0Ȱh+�	S*P�<8�aVyFy�y�
�2�2��(�a`�1�g�E~E>j��H��f��p��������4��%���v�M��"RvN{�
b�1���s���CvKrdV���� ��_��Kq�O��~��n���-��7r���:�(W��1��� �Ԡp�eT��`7C��(d( ?[� Q�����H�X�@�l��(\��/@�����0	�撞�Q����¦  (S�/@��!�X �� ��:q" (A�b��(�%/����K���a�u fgZ�P���)-����	� F��8R`6�r�Qv��4�B���8>$f��(��&THT4%0�s�+㊢9
�.{K0t�2f)I�£�;�1�ͪ�IT2�-�M��9�qK0E�B�. ���)Z�!�]$=�PT3p�:��+�8�XH�*ZF8)໲R-�W>"�vAizΕ4A7~~�	 ��iԔ����FR �H0MY�((h�Dt4�DԳʑ�nQ75�0��񘍭�`K4�-�ifhs���m5�*�i،i`��n�%���EJ��,�H{�F_��[^5Ǆ�� ܊&��BFd���-Ҙ9�28&�
a�e���i5;l*��o�?���]^-S�H�l^=�Z���������H-~_��qJ�_���]o�a�*4��e~�ߥ9u�Ƽ/��r�*��B�3��1/��|^+����M�^�5̦�p�O�U�'�ĥ��h����5?���A��/�h4[�k���)��ld׳��J��M�:����{����X6q��Z�]#d��wF��|�İ��&`���!�.��_I%LV���'UH�UqVc�e<�6tX��'�T'������� q��:,��k�m�а��>?���T�Ө�xY�{�F�j���������7
��!T��d�Ä�`��tQ�s��|]�n�Y_J��)���rU���M��kڽ����7�~E�����JV�u$�;\�p$�9���_=֟@8����]�ߛCA���)�a6V�^t�,��ѣ.�b��r�kɦ��S�%\��ޯkYXCt�s�����C�sqg8۟6zI�X��U�_�7�­��`cO�\�3eז�n�q7�֐:k��;��ou"����k�U%%�捪-��F��ԌU?ߍs1�5ć���
�f}Rq;���������I;�����9��$X�g1~6��1S�,�->T�t�-;d��<ߏ 9�܀�(���p@qd94�� �W��Ű�#ū�����%*�T���pJS����?�[8^�'SE	uU��<�e�xQ���
"rL4�Csx�]�6���gd���j`
�WD=^6�� �f�x]�!"GP�6��ÊƑ!�2�Um�|��-^�QQ$u����^�M��"�q	��.�w�!���F�:-��N��o��Gl|�.�|xF�	[sͧ��v���`E���'�K45؋�����*�������r�b���6��jO���T:�)�cu�`��(-b�8��%U\�����'AblQ���:�Z*M_S��>�:�������ȼ�g�\�=Vd庾��"AZ{��0���h�ʁ!�E"�����840tj�1�"&���a�{T�"0\�L�=(d��ܐ�P���:�A�8���\���o�k�)��k���n"�{���`�>�|���ٻ��{��NBl�?�ۋ�y���x2���3���z��݀�k��k�w���:��Cy7^^�|��\�[1��Z���z���Y%T�i���O���C���m�A�����g��ٙ��摙:��3S_��^���([�Ul�a�������������Q�k���Z��Ʋ�
B�4q�t���4/����V�@�5ɕ���T���7��ly������6�u����q��3�V�c�oFC��c�⌫��>$�t��.���ɬ���zSC�)g2���3FcOǳvΞ.Q��q�]�DD��7����3IӪy'�f�	͒�&gZ�Sױ�NњK�EtY�y]�a|lK��ۮh۲�QB���9W__�Ļ����ta�D�QL����ԭ����6L��C9FA�m���V�oa���E����F�F�Z_�n+@���BLZ{p��"���� ���aht�c��~��� ��Z�K��1��jhK)�U�J�`�=��*����D�1��`�^��6J2L�)�,�{:x�!�V�v#�x��4����czfU����b��-;z��	ճ�{�G����{"�:��[���H���践���	��Ә�#�65�1��(UID}`�rI�H��R�M�2*%��0��R��̰ac��پ��S�ƶ��B+�^��-	�q�2�)�Y��^�f��'���V?d*)6-G�,���|�D���Fzņ��m*�l�Ů�w���螰M5LNߦ�4ݦ����nw�R��2V�5mS���XŮ<]ɔ9.�(����jŶýs�����S���)�}�n7�n��n�?Ԅ�f�|��x~�݌T�݌��K���śN_�Y���5�ם������w��#w36u�n��Mt���'�h�Y�坍�v0G��a$nb�H��.=�}g�g�a������:�G"V׃Ι.N�{9l#LN��%�C-�.����O���k'���Gdw�3��Gd�gT�2�އ@�_����"��%�5:c75��~SM�M��#�3~C"i�ś��0���ե���;Z�n�����Ԁ{!�:t4��d�@�� �_����V��F�n'TvK�#�Ӟ3w�[V&����cC��E刘�����ޮ>Q�KX��T���;)�1LNk�4k����C�S�>oB�}�ug�%��7h����T��'A�����y�M�3#�6_~��v��q��l��r����U�%�<h�}����>�J�����r�<`H�T�9`��j�'}���5ap�;�VҽE��i��$��n��Y/�Y��O<CЬ�v��ӳH�Ɗ{��T���V�p�:�η�F�y�OK�l:K9㊆q�OY:��V�~d���|I���}$^�~-�3���~�p.e��Fo��Fo���T�`F߈��7����-��pʖ���U�p�Zq��\w�V4"��
Z�'Ae.��T�12�߇0��A+��ʸ�Ԑ��J%ln��ڐњ8xA=�����:�K�P?�m1�f�z9��.�6��k�+X���:���ŭ�;�峞�s1<�Y^��n4p���7,9n��aV�clX)�bI�Dw�o��/	C]�?&�'gRS���ׯ�car��D�P&��\RXε:5����_�
endstream
endobj
99 0 obj
<</Filter /FlateDecode
/Length 4235>> stream
x��\َ\�}���� �� A K���X@>���;���[��MO[-�A�m枹$������|m�.�~s�c	����r������s���h��?��/���M�j�=�'jh/��?^�7��������Z�����qw�4���z��ۇo�zy�u�$���\���/o�?���vy�߇D?����@؁܀� oP>܇����I]@�~��q�Io��%��6탸m���T�MvuX�x�C��b/�4>��{��������]�]~�0޸�	�w������H�+\,��Erag㑨qc�K��;h�����t��z��5���G���K�� ����e0��?�����!YH�r���̇��j�z��z��[�m���#{~�V
���D&�������RSK?K���6���>��V,a�0��R�J�Ǝ��1�7I\~���L�a~��C�y=���{�eFR�iI��՘RV��Z�\ &c��/�c9�pکփ���c��"JdēWT�mF�Oс]F�`?Ʀ�{�i�w�~C��E��X
$�X�S�&)��p�7��Xtfޱ���[�QG���.���	��1o���}:|���z�����݃x��.�$݊ϡ �"�rb��8;�}E�(IbG�)Q�Z�x�H܊!�~�'�r�8/��[J!sQNyI/i�%-|ei�x����H���JΪ<����D�t��؞'��.���P�0�(+[��N�EGu��ŭ�D1�0QLL9��R��\9�S���
�9mWC?~C�*N��UD˨�\��Y�l~�)"����홂����ͺe
Ƣ�j���L��)"�p���3���DѠ�(�i%����|=i�.'ãsNA���|��e�SE;S�e�s��i��iE����KZxI/i�kI�>�X$O�`�<}=�	��<��9OD_T�ё�Va�H��ѓ_T��c�nF#���	F�<Ѱ�'��3O�'�':��pt�v�\{��B`LG˚�
��!���F�K�*��eT����	6����
��<�ة�H���c{��ع�`t�)�S�`���	F�<Ѡ�'�i�����|=i�.'ãsNA���|��e�SE;S�e�s��i��iE����KZxI/i�kI�>%O�\�<Av=�<E�E��3>ny"��	F�.e�Ny"�x���y��s�`t��y�;�D�y�c�G��a��ʵ��*�tT��y�����jTQ����yXF������@�`��<Aȩ�`l����UW��E�	��<��9O0��	�S�`�\f0��S6l%
~Z��?�D1_GW�ݢӉ �ST��9#tw�;��TF�T&ƙh#r�#w���&�^�Kb�zß�<����-S�e*Q0�u�`�'��G�_
!h�4;%����Ύ����7*�E�z����Dџt���C�t��ʷ�~�)�QѲ��jh�o�Q��Ҹ��n�݀+3�6��:Or���y���>e��'��c�}JF�<Qc<�	�΅�[�Ѡ�&�i������|i�'ãoNA���|��e�SE;S�e�s�i��iE����KRxI
/I��H
?=����2��e׉�b(I����U9��!R_�$�[�K���:���pˁci38��&Ț�$�D$�؆��<%���A_I��f@٪���CP�x�D�@�6l��yÛNVM�@K^0��S�@�(-y "!r$G�1x����X��fVJ��>�!yJ�(�b{s�0%7�Wt�Xlʝ:��kjVډ	��J"���dn'�a�c�r��'���ݩbvui�X~aW��)�v��J3�!vn]�NE]����5�+\te�Jy��Z���ؽ*U��[eJ�Յ���5�����\���Ssp��t��� ��Jk<���w�4���J'2F򉜮��$�����ᐜB�Ȕ�ۛc�)��]h~5�ѱ^5M�M��Y���0Ĳ�f��oY��=h��-���������I#R:�[�TyQ��=����Kfݻ�#}��O(��}/X�U��al_}5����~x�����O�H&{���<?�q���M�THD��������|ٴ�>��!����ڍOh5����L+��#%>k���4��z�F��;ht�އ�����=��l�fsO{J˔����{ʑwR�S	޹���a6�J���g)ا�ޏ��s�GRn��P�x��t����ռz����������Ʈ�%���gX�5��ey{��G�۳͇q�Z��:�IP�"<0[�;�t�H{&`��8{��5�{�g��A��a�үpb�@س�*,[�X�:��w�G��x��9�w^qtI�VH�-�����5?��bh�n��
�mYᛢRh.����LJ(�(L@LS}�oΜ��K	H��Ț��`�;��<��e�'�68�T<Sw&W���G��p��d*֙�����Z.��/V�Y�D^<����� 2��)��ƃ[�t�o�#!K'����S<X�B���	�p�����i:6���1���<˦(;:ɚ��s� [k-�{��-��m����9��W�������H���Gk+E�g��L�W�$Jn�zq�E�<a2W�����}�Եj���6�Z�	B���}^mv��c풨*7�S���;j�'p���D���&SHZ��8������Eϣ�Al�G�a���yv��ڸЌ�<8�{_u;Ku��K2�G�%Jym�x�HT���l�b]�Zlɔ�cUk1ٟ��ƙG-|]W��W*dE9�EV9ae.s�B� �X@ d7Sv�Ak�ֵ$�T�bQ����,*�.$-�(RH�zV�YM��Ր����l`�{�SRj��BM!���P ��A&��=�`#ȟ��SXz*�P��BR�0�\�V �"�M��E�wY�ĐE��BE` �-J�8 ��!��Ц�ť��<x�@�n<�8�v�c	��Qn�Vs)���7.�ʅ�X�RHX�N��B�eEL�$���2k�g?��l*�Ua�П�=us�+�U�*z3~�J��Xa<T�X��!{�+�ű`*W9�ɱ�kq\�c��J���f7��筷�
�,�Oɐ(2oz���)��E+G0��DFj�Te���3����N��1ߚ>e���6/�ΑՋ��������~��VڌFD�Z�7.I����1������k���F��.ډ����ڙ�b�67��x_suZ����e�F�J�hb�6�,�І�VF��lִ2��x���o��VF;Y�bG�ţ���[^&� �C���-ف�$�աhem���2���� ��v�_7>Y��B:Y�p:��SuX���<����`�5�
��N���kv��<B#�gcHÝW6
����Q��%��(d���(�����I.�K��\��F3a_й05%��:�Y��N��ԃ��u߆���=#s��0�x��s����	�#��G儵�ي����h�
��J�{D���AEp�9A�3_�.�E>]�1�E�h�ns�s}�+tTt�]Ы'E|�;v>��*��l���`M��� ��e	�}.;��:�{���A�`h���%�
�g�D4�DC����%,!��d�x�%��*���D���|�	�������������d����vp���2�����2�t�L=��:���˕5Z��8��|
��< K�Ov��?U�\q�g�:��금��~L��|��ea7O��d��}�R��!#�7c	+�t�W���O��P�4L�9�2gbX�LL��_�
�D��Y�����������ws�
-�8��j�7�|)ש����w��!�?W��A�t�3 �p�%(~� &Y��Kj0����_�U�i�!L��(-
Đ���"Ŏ�@d��3�3a�8�)X�8� a�X[踛���;�!���U	H�U0���P¬"�^�
LoU4CX�Lea�CX�K�	�����s����:���v#�9�q����s�u�^��A�P(��TG�<y�,u�ZUI1n�v�%�O~��VFs�i�wMd��^]��c&G)7r����Sr�x��p���ZN}6�)+��W�G	����y�t��v����$�1v���q�ɋps�}���UV���`��Z�e�8&���M���
endstream
endobj
2 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F6 6 0 R
/F7 7 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 8 0 R
/StructParents 0
/Parent 100 0 R>>
endobj
9 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R>>
/XObject <</X10 10 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F6 6 0 R
/F7 7 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 12 0 R
/StructParents 1
/Parent 100 0 R>>
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
/Parent 100 0 R>>
endobj
18 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F6 6 0 R
/F7 7 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 19 0 R
/StructParents 3
/Parent 100 0 R>>
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
/Parent 100 0 R>>
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
/Parent 100 0 R>>
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
/Parent 100 0 R>>
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
/Parent 100 0 R>>
endobj
28 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F15 15 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 29 0 R
/StructParents 8
/Parent 101 0 R>>
endobj
30 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 31 0 R
/StructParents 9
/Parent 101 0 R>>
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
/Parent 101 0 R>>
endobj
34 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F6 6 0 R
/F7 7 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 35 0 R
/StructParents 11
/Parent 101 0 R>>
endobj
36 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F6 6 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 37 0 R
/StructParents 12
/Parent 101 0 R>>
endobj
38 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F6 6 0 R
/F15 15 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 39 0 R
/StructParents 13
/Parent 101 0 R>>
endobj
40 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F7 7 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 41 0 R
/StructParents 14
/Parent 101 0 R>>
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
/Parent 101 0 R>>
endobj
44 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F15 15 0 R
/F16 16 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 45 0 R
/StructParents 16
/Parent 102 0 R>>
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
/Parent 102 0 R>>
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
/Parent 102 0 R>>
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
/Parent 102 0 R>>
endobj
52 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F6 6 0 R
/F15 15 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 53 0 R
/StructParents 20
/Parent 102 0 R>>
endobj
54 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F15 15 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 55 0 R
/StructParents 21
/Parent 102 0 R>>
endobj
56 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F15 15 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 57 0 R
/StructParents 22
/Parent 102 0 R>>
endobj
58 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F6 6 0 R
/F15 15 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 59 0 R
/StructParents 23
/Parent 102 0 R>>
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
/Parent 103 0 R>>
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
/Parent 103 0 R>>
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
/Parent 103 0 R>>
endobj
66 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F15 15 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 67 0 R
/StructParents 27
/Parent 103 0 R>>
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
/Parent 103 0 R>>
endobj
70 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F15 15 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 71 0 R
/StructParents 29
/Parent 103 0 R>>
endobj
72 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F15 15 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 73 0 R
/StructParents 30
/Parent 103 0 R>>
endobj
74 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F15 15 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 75 0 R
/StructParents 31
/Parent 103 0 R>>
endobj
76 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F15 15 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 77 0 R
/StructParents 32
/Parent 104 0 R>>
endobj
78 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F15 15 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 79 0 R
/StructParents 33
/Parent 104 0 R>>
endobj
80 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F5 5 0 R
/F15 15 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 81 0 R
/StructParents 34
/Parent 104 0 R>>
endobj
82 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F15 15 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 83 0 R
/StructParents 35
/Parent 104 0 R>>
endobj
84 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F15 15 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 85 0 R
/StructParents 36
/Parent 104 0 R>>
endobj
86 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F15 15 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 87 0 R
/StructParents 37
/Parent 104 0 R>>
endobj
88 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F15 15 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 89 0 R
/StructParents 38
/Parent 104 0 R>>
endobj
90 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F15 15 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 91 0 R
/StructParents 39
/Parent 104 0 R>>
endobj
92 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F15 15 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 93 0 R
/StructParents 40
/Parent 105 0 R>>
endobj
94 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F15 15 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 95 0 R
/StructParents 41
/Parent 105 0 R>>
endobj
96 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F15 15 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 97 0 R
/StructParents 42
/Parent 105 0 R>>
endobj
98 0 obj
<</Type /Page
/Resources <</ProcSet [/PDF /Text /ImageB /ImageC /ImageI]
/ExtGState <</G3 3 0 R
/G14 14 0 R>>
/Font <</F4 4 0 R
/F15 15 0 R>>>>
/MediaBox [0 0 594.95996 841.91998]
/Contents 99 0 R
/StructParents 43
/Parent 105 0 R>>
endobj
100 0 obj
<</Type /Pages
/Count 8
/Kids [2 0 R 9 0 R 13 0 R 18 0 R 20 0 R 22 0 R 24 0 R 26 0 R]
/Parent 106 0 R>>
endobj
101 0 obj
<</Type /Pages
/Count 8
/Kids [28 0 R 30 0 R 32 0 R 34 0 R 36 0 R 38 0 R 40 0 R 42 0 R]
/Parent 106 0 R>>
endobj
102 0 obj
<</Type /Pages
/Count 8
/Kids [44 0 R 46 0 R 48 0 R 50 0 R 52 0 R 54 0 R 56 0 R 58 0 R]
/Parent 106 0 R>>
endobj
103 0 obj
<</Type /Pages
/Count 8
/Kids [60 0 R 62 0 R 64 0 R 66 0 R 68 0 R 70 0 R 72 0 R 74 0 R]
/Parent 106 0 R>>
endobj
104 0 obj
<</Type /Pages
/Count 8
/Kids [76 0 R 78 0 R 80 0 R 82 0 R 84 0 R 86 0 R 88 0 R 90 0 R]
/Parent 106 0 R>>
endobj
105 0 obj
<</Type /Pages
/Count 4
/Kids [92 0 R 94 0 R 96 0 R 98 0 R]
/Parent 106 0 R>>
endobj
106 0 obj
<</Type /Pages
/Count 44
/Kids [100 0 R 101 0 R 102 0 R 103 0 R 104 0 R 105 0 R]>>
endobj
107 0 obj
<</Type /Catalog
/Pages 106 0 R>>
endobj
108 0 obj
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
109 0 obj
<</Type /FontDescriptor
/FontName /DejaVuSans
/Flags 4
/Ascent 928.22266
/Descent -235.83984
/StemV 45.898438
/CapHeight 358.39844
/ItalicAngle 0
/FontBBox [-1020.50781 -462.89063 1793.457 1232.42188]
/FontFile2 108 0 R>>
endobj
110 0 obj
<</Type /Font
/FontDescriptor 109 0 R
/BaseFont /DejaVuSans
/Subtype /CIDFontType2
/CIDToGIDMap /Identity
/CIDSystemInfo <</Registry (Adobe)
/Ordering (Identity)
/Supplement 0>>
/W [0 [600.09766] 3 17 317.87109 18 [336.91406] 19 28 636.23047 36 [684.08203 0 0 770.01953 631.83594] 48 [862.79297] 53 [694.82422] 71 [634.76563] 80 [974.12109]]
/DW 0>>
endobj
111 0 obj
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
/DescendantFonts [110 0 R]
/ToUnicode 111 0 R>>
endobj
112 0 obj
<</Length1 43136
/Filter /FlateDecode
/Length 19496>> stream
x��y|Օ?znUWWuUuWUwW��M�him��by�Z�dK�eK^e����ll�̈���Y��p6� 6I��� ��g�����d��l�D�Ʉ%�����ݶ����g�����J���[K�{�s�m	 ����3[���/kGV���'o?��Wx�n޵q�0�׃��6��P�>���� νm��]���9��5�}�=�@�!�)ۯ<�m��>q ���[vh��� ��rcߎ���W��xݍ�;�B́-�\�'v��Ё�+����c���Wm�����{��O���x`��Bz	��Q�?�{㮭/��֎�9l_힫�}�0K�|%����{���?��6����Z�q���0�q[qO~���k��[9�����ttA����
`&�%x�p�*$,'q��O�[ �V+x��$,_�ʹǹ�-}$P
�neP�#���@t��������h������&�	DC/�
C?�� � +��1!���-�bC�d�J�$��DL1��T���*��A����ېfXi�z�Cl�z�Fh@l�F�Є���� ˰2�-�El�����3��f"΂v��0��{�������Ё��NDʡ�C7t��1�y��Ѓ8z���`b?ÅЇ��o�bX�8 �� �C�@d8K�� �r�+`q%,+�V�r�հqV!�a�V#����o�2X������a���0	#�q#�M�q3� n���_�V��`�v،��!�dx9l/�
���W�N�]py�?a7\�x�=p%�^؅x5�.���U��=������j�k`���A�0�pM�u� ����#��\�8
�!� �?�#����7��
��Mo��ࣈ��1�[��o��o��¿��p���
G�0���V�O0�nG�$܁�)8��i�8�]�	Ļ�N�{���G�S���O#~�B��]��<܃������?�}�YĿ��^��~>��%���^��>��~ć�����/!>_.�/�
<��Ux�k��#p�����'�aį�W��">_C|A|&���O��O�c��`�4<^�9<O >���$��)�Sp��3�6|�;�4�w��O�4<��|����)���w��H*L}`�>�DX�,�%�D�DX�,����["��6��2�a������t��4Pc��3�2�9�θ�n��>�L�=LʽL�}Lv�LRL:�L
+�̅����<E��D��ĘLT2	�3~'w���)ƹ*ơjƏF�ZF�4�l�c=�T�N#�E��x��Oh�~P�	Z������%�x�p-�?~����3�����5�Y🅗��q�Qx-ћ��N�Gh���������Ml���yĎ�C����x�@�{����H�p�Iq!�A\D
�a1��8@Z߅%dV�۰��E$]�Cd~�,#߄�d qYVxV�U��Ț�3���O�0�X��![ג�O�:���$\F�"��~���`�1�@�G!7"n$7!n"�����	�B�D�J>]��m�h�k��|q���Wa'y �rr��0\A��x%�z�8�"O �&'��*����|q/9�x5�A�˰����!�R�K�a���O��5���_ɿ#^K~Y��#�)|��!^O�D����ga�L!��ďp��g�FN.���㜅��&΃x3@�O�8WY���U!�jw­\C�p�A��kE���U8G�ďs]����;�����InI�6���p+|�[�x��0ws���6!���3�����n��q�?��/|��]�x/�7��>��\���.���;��݉�e������g��A�^ć����1���ܱµ�0�H� |�{���_�Q��p�,|&�� �྇�u��Q��Ǹ�G|�;[�Op?E|�{�p<��Ka7��^C����+�i�p�C|�{�p|��Sa'|�+ ����6oE�/��wyGa��]����E<�
��{|��	��W"~}}}]���777�{ZZO�@��66ԍz����������p��������y�*�_x"Z�7S�)���W/,�56��	� }�Mn	��_�m/j��t����^�%2�{$�fQF�Qז ϖ��
�%�QgO�5A1�TxkQ��F��-[���è��և�>�v����9�9"�%�m�i�ݍ�բ����-(o���w���َKI�R6a�Fh���HiFq�u�\�|����%�-��[0��g^wW��c�ٳ�g���46��U���xe��6tͮ�6I�
�#P��?�H�LXR�zz߈�U�LD�j����ۢ�3�wn{ϝ�❹w=:���E{�щ�{�ѧ�ڡa<��'�&:1Ɏر%�N�x���^ߎ����N�߿�p�H��"ϋ��*�c$.+x���Du|�	R�A�W�;���~���ݸebph��'��au0��k�:oBd��m�[�'�N��)6���-�-/��7�C���Ç�&��DM�g����a��N��{z'�q|٢e>�LI==�&`�㓿~w��R�5��	��v���z��m�B�_,F�r�S9؄'7ϣ�)�u�5��Lp#�ʩ�s%�rC�ʅ�G�1ʪޑ�����6E����7��x=:��F6m�A������bx"׃������hj��7�`'vR2O4��L�����"Jy�s�0{��؄{��l.=5���C��=<�Sl }W|h�$�+��h��b���c�3���=<�e�Dd$��s[t8�ȭA�o]C��'j^ŏ��OdOa��sw�f�s1)E�� ��r+����s����b����s��$���SJwУw�O��>z�������Ċ�4)Xj������KǊm*~�۴�ݴA5�ޭ=����
�������QZ�>��(;�ʗ�$j.�q�VE��N�`t8�5�&�2��}��f�]�<�hh�0�vIJV��x}�k��	n
��t��Sv���_8�{������a)�h�a��x�=�?(�9TΙ����G���1գ�o|�pæ�'r��{zGv̢��o9_><'Ț�l����㜘c/Z�]_�Ƨ�D���ȑ��k�O� ���'8ҽ�J�ov�]ot%Ρ5;����$$��	���*�q�pVuB�o�P�ݴ���w뭴^D������|�ü�`$Ac�X�g5��z駑\G��?��\w�q���c�[�^�N��k��kŏ��?��n���=#���ܣ��lu�݊?I�G�v-���_0�4~������}�W�>���ZZ�g�g�W���{�������1��\�T���J���HS��Kѡ�=���6��~>����ObYbm1N��u/}2ޠ�y����������+dk
������S[1��g �w�ߠ~����&I�4>��<�_yg4e��Q�[�|<3�c�7������0�~�m���2o�-����.�fitv��b8����gN�hr��b���%Y<�W�Z�[��3�m�M�b$"���V���sˊg�$X]č�#͓��;�[/"�`���p9�!�S�o���$�٭�g���]v)�*�$^��E^�z-�*�g|�]�9�>��n��w�D�CviA]v�A��6��m�u��0�'`X���5"4
��F �G����M�b��n�E\Q����t��e�s�[�滐2���O�?��
���O�:u6:��:�����G/hXN�߳?~�u�Tf4�|�d۲b֌�-�ƶ�,۲<�I�����핷܍{v��r�W���L=���G>�dq7��Q�+�8C�������$)�Ŷ:�g,�Dv�e~Smm6�{'3㊖�+23��%�d.��6�-�V�l29*�R����*Y�A!��B�S�
	)���^S��_p#��ȉE��[6Ag�3K	u>&��ތ����+�Wl (Nm^yxa_���t�-$�~�����w���>��/�0��V�]�iIZ8���ey�����XDE�I�'O�����'�����'�0m�&F�]�"o�-[�z��SUmaB�T�A���v�@)p1P`F. L��#&l6��a�#V�4��4��ONf�O2&����eD�%k"��xK����g�,ᅥ?�}s���L�'�Zx5gJJ���,;�N�R;g�Иm̳�����d�3��<�R�[�#_'�h�_'�jI�:�����l���	� �ђ�� �'	9��<߂au.�胻ѰL��hX��0�i}ޅm��6Y���e&Z�o�A�@�Q<�p*��fXը����(z{�YJ�ŶM3 �,[�ֲ����u��{��<T�Lw_#��p���[�-d������Q?;����7N�6�������},��q�s؞�������¹Gq��}Ά���B�:�@�"X(pXEo��~zK-}�^�(��Ys!2� V�p�b��:c��h�ŋ�=�����-��	zD�x���Gl�5.<��6t�Gx�Ci�LO��TKc��ϲ݌&�{�.#��H�ln���t��l���\�k�ut#���T�9b/�ɺ�=����־mq}��m�=�fa/�es-��V1���5b�$��a�]���m�GE^�;t5�6��ꈺG��*/��W!P��|Q,��_�g'�Q�;H[ֈ^̷_YߝW�5�&���6�_�5+>�[��-�O�_�{��]^��U���D��m*�t$nN�!A�+��dN�M�OP>;a A�g���s>�7��4�k:,�����ާ
�3�Ѓ'���WM⃏�X��<f��dm��x�����ZvEa(L��w�+�s��2%�N;��)��������3��ӓx���]� � :;���13�jni���:��7Q�yd1��PӜ�Q_$�S��H�#쯏��h�jJ�["ӑص��$�uu���L��Ԫ
�C}����1S������-�έH���H���\���+F�b�!!B+Րf���r��`��S��ێ��?�Q����R$�ڕ�䔜j��'��t̷��I$Mi"�g���-�|�$�[�H}oK�D�ܴ�g�%;*F�J=0��d�:�����I_�PڭG=��3������YQP�Z[���,MZ���g-/�Qc�M$s������_�D�{������K���yj��%�6��f��Hצy�����4��̟Mg�����(�ɥ+��Z�R�aN�~`fTRUː@����Q�a]���d��H�0S�l��~�(ۼ������=��ݷ8<��n��e�v��"�Fe�I�T�A&3D!�O^�>���Ef2����N��IEU��R�����vu/�дfٲ�S?$�ṳ����MS}�O� wE��Z���߅�+ls<�����
>
n*���A�Wy��xn���I|��F��h0uث�wD� 3�A	�%HmZ��Ѱ���A)��a��W�%&�j(���3]�z���dζ��KQ�zd��|wQ}��8�4��q���o�t�tZ(f��M���+���%��b!ǭ�7,��;we�?5�ڜ�j�P�R-�֌����y�q3�s:�I�p����c�M�CD�`��+���b���-h��H�/Z뻗��!'c�����H����4ۦZx�0Y�%���^�~'�l����^r_<5=Ԅ��
�������mH�wr1Ft���Ѩ5�G��hc��V�ѭ5vi�mX=��(%��(A���n�Dî.�͐�k���d�'�״hTh?�.�Z\�pU�c���cl���Keb�w9���PNO��z0T٢����o�Y�:AD�Bz�qZ���q��=\��\fS�ڌf�#��ex����y?o!�C�fv�n��"5�M�%M3�^#�t���=�IUf������~��u�h=��ʶTm��-���y�PKC�1sW��9Rْ��u����Ϊ���6�M	�Ϳ�4i���$���T�柇��-L��<��rJ�����=ܿ�(�Rb/������j���m1fc�����<wO�b8�;(�"�IИ.=��O�x9��3�b�4����|J«�#�a���[���i�qY�l�i�gТ���y4;�ږr�AhX�Tos�2c(K�Lk[ks�xț����ܺ8��㳗5{-�f���~5�"j��:��w��^���ײb���g�&�k���nWL%�tv�"���,�,�Ř�ĥ�@]=�0T��X�N7C1"_��Vɥ,�,`}D���U�3<�G8���Øm��<��G� �@3mc����i��s�����S�h1ْ�~�lL�� I�9������8J
�Y��7��(r�`��G:a)<�ՖG��9+g���+�b^��6f1F�H�����p��n�/%����ٖ\%�]��#�m�4h@_����`nd������d�z�cZ����a{��޵	�P�l	���� �L�e��{�*�9��V=�yl(�(�p�5l�h�r�ԚT�X��쫮v���H>?�9�#��R��)���!�`FQ���)KhL��8������	�E�;�����G`1&�Ƌ��UI���������Â�����uw*W6����TC*@�X��ꄷU)g&�5�}NO�iv������%&���m����Զ��օ̅C����0ҤV�۹�>�Cn�wt�����$�-�rw��8w�Ov���#�*����"w�pq�.��E\G+�Up*Ț
R1������.�uE�8�k����W�s
P�E9��۟�9uW��J��V����m��6Ҷj`pL�3s�#���c���XCz'������xn~~sJh��q�+P���tf_)�����X��;Y���yq4�qȴ�(�rIV������p{.�d�����-5�UXM%�����h���iZ:+���5���q��jݲ��_;<�9?�x��"k�k����g��+�ݹ;i�;g���V������j�g�joZٙХ���Ĭ�T�U+�f��؊���;,����/���+Z[�Y۳cAb����+�2<o�
�_	�F���'AC�nF��5�]5TQ�ɊU����&�:�b�Y�U�(�N���x���<��x��P݆
�iZ� �����}�-@JI����m0�2GM�i:M��V��.k7˃�.�oj��{�3z^�]�h~L�Է�N�F�K�la��H:�@�b"��a��㙃�\��Sg:�VϟםX��7���hge�3R�����:�h�ч��M��/.Z�E:����Gn�{�U�y���MҴ������q�� �=���~��L��bOї���!�OzIϬYԗU�Ȁ�>���-�W����*���!�C'�og�eL|�BcQʡL�1�y�ƋƴԀ���BVMO#�aΘ��v7�h2���k���wt��h��7=0+��S{��D�1X1�;��5���>�Lgz~����\�`�N��{�]D�Ï�
u����k�*��f��������r����������X�� ��#��c��U�k�룩PJ�H��~��"�+��Aٱj���9��]ݔh�k��"�h,IM�F���;4�&�2��J������s� ��F�ٵ8�0���OC�L1��di0;$�T1��d2Ի��ΧI>-LS�����:����[��I�f��
[e:hf��5o���}Z�ec�W�]֤�e��p�R}�s���+�AAs�To�A)�!7�Bn�vǭ#����u.�~��ظ�;t���h��T��X$�Oz(�J�������ޠA�b�j�$P�	�Y"���ʠ�V�H�t���B	d���5E�����mw���ZS��v��fN�?\So�ՓukoZ�e�>YL��i�3����Α��VaG=h�hɅD^�#2'�v��R���Hl�n� ��,MAƠ�e}��l��,��"N}�TN�B6p�/a��r(~y��T��"��W��W_x������Rc��[$4����M}�����L�_z�%T su(�6:���T�#9� �5r������!�kr
���P���r��9ȁ�~�>�R�ʩ�E�y�X��݅� �7p� D�P�wPa��wFoU��V:��$ޘ8ĉ��,f��biP�r]fje�-��3�R�A�����[��t�&�7����'�"~����9f��F2-��V�f��];�NVN=c�e�鲛/����_p���x��C�$h$ Dx����p�@�,���_˧逳_�q#���E�i	��/��.8xx���}�N�}.�t�!�d�*2���Bh2�d��KqP2���!����5
M=I*i�T!���F��k�E��b��bd�͖5�*�*�9/�׽�eVu%�e�b�k��sWa���H��|�㠃��n�����'y�J������R���f�=��`�Hx˩ �a����ij���W>� 2�F|q�<(�ȼ\a�}·���S:ѯ;���I4�����2��"݋�{��N��dj�z�O����t��{�ӽ/1�>}�R�j'��>8��Wq#�^��[Y�rE2=r�P����kj7n��X����\�zE"<�eGc��S(S/Ė��5�m�� ��D�>�!+�%$�Tu��:3�)��5��S6�X��r/>9�O�5d�IH��)��}�J����m�=�ގ�Cd[���*^^�'>�y�xl3ɸ���A޶I�I�$d��wT:&q��)��<�20�1QǴ���(w�c6��aUd_��dB���+�Ip�䦊OWpK1^��OS�[���1���)�QG��G�}�B$�X�'�y��TD�+��]FW%��x�R�g�4�d�HD6���~	��]2��&)g���KG����#�r:���������(���|>Sd&�f%��]:�l��܅0�x��r"�]��ҩ��8�ٮ�V;:f�|�::�++��C)�1�[�j�P��?5y��'O<����G?���я��:1��ۈk��Z�j���572��+s�(O�Q�`��OWܺ��s��YR�yHz��1���}��ܮ�[�ϊܵ"�B$kE�/���ҹM��:���A�s��:'ꒁA��%uC1P��j>���'0qCIG#z�M�,��ǐ*Tґ"(��O{�����ؙ�nH^�yۆ���H27�>ނp��4zz������3�3�*��Ii.��5h�dHl����K^��K�l����&V��oS��_4��;�>�ѩ$j�c5�j���@ؐiH.��*���y@]����d{�8K�������q��qo�ix?$�����0��}.�f�.����V�¶M2��hV˺�=�Y�Ҳ��y=׵l��^�Ҳbv4:{EK���Q�n�����u�k����}UU}�;K{]!��bt�
XF}йG�l�u��i����g��Ӑ�ی}�C!�Atr��R1gf�{1~x���?О��-�&(�[)�.ǝ�O}�`c��LG�?3����瞹j���-����,����#�����('���!C��`/N�01�"�y���Q,����PCc�*5�e����C�(͑��_�,��F6�,���v�Fc�'��|�!�<eҩ-�l6����C�賗M6�D����у�^��aꢸ��{d�:�ǫ��Vb�lh%Us&���m�{�5��Yr�6���Ţ75�Β]w�ʿ,I�Q�P7a�(M��-�8�$����_yp�Gǵ|�L��
,�	�}�-c�bjGj��g<T
2�p8t�٫w�e�h�d9I�cvҘ/ͳ�$2��&%�k�,�_q���.����Y���ƦF�=�X��X{����v�z�D�����ݵtUujɂ/�z����]��H=?�'�"[[�V�m�a4FǍ�H$�.T�A$;�S��J"D0s��N2�$�$�(YbaI�	Ҿp��I���'�|�&0O=�8����F��=I����:�{>��*�Uj]Ԇ���諟q�@
d�0 p�@��Iw�a!�-h ۱��꩘ד���׸�vqt��s�I?��+7;�rr�8�*l����D��(���<�G+�	�9[��Nq�hoנ$���O����c��|qozt�}�r@��=��ٱTO&thW�v_�\�Vє0=�-��Em����V)!������O���;��m�K�~՗�W�B>ՙ���X�I��=J9����xH�Y��m�&'��=�o�r��XJc7�M�i,x������g���a�E�8�T��K�t�O��W���۸��}}f^��5���"nR�)p�}�3��$�C�{�D�'<�3��]�!����eJ9'�d	�d�E)%�g�7:���=rpd�gK.��ɹu�����Zm��Y�ѩ��M���CS����bib}3��	��Վ�N�;H�}�}��_���d2f#ld&�#��ڿk��0!i�q���T�>� ��"3MU��UݧX�
n?��)�
�� ]�>a����
Z�#+�jJD�$���*�	嘻�H��������3l_X����i��0�X�B#m��Y����l�nN�vwU���7?yE뎶�-��G��0��FI���
��oBZD��\bf��%j�fF�is��p�kld�#c�|H��6��}(Dc���JJ��������*Ie�����a�� ��m���6�A�ᨛ��&n��B����"1"Z$��O��E�rOظڈA���gtR���ktޭ^�����_$�c'�ډ�>���Q�w��]n;D�ɣ@ ��n;���
;v�n���.���͗����߱��Ȗy������{���8��`�x�ӟ��-_��د��;�+]ߛ�0���>��8�Hd.��	��i�@�K���[����hԨ^[���j=	;6'��7֭ go��+���_�O�ܾ�O7����3o���|�+G��7䤗y �y���}~��,��w�Mx:4v3r�%{uéxu�S���Z)�(��1Aw�*�����1���������u��^Tipc ��zG�7x��
^���D�7�9�$�>o���٥wi]
M1K�/�J�L9�D/N��+�kX�VҴӐJ;z$%��,��$oi��V��uFZ����y��y��U?�9��_�4_��?<��Y05E��g7>��fE�"�t��$(ؿe�S�"	�>Us���;�R�UQy�N`}��Y"������^6'�Y"N��h���qn���u���i7�:����>��#;VRn:��@�������꽶����̌�UW�^�C<W��eٱ%K�-��˧^g{�Þ�0��U��N�H9���&E$N��.���Aw�"Jmظ��:�?�%�+g�Z��im:��)���� �������'7O������]��ϑ�q;�k6o�R���zd˶��"˱M#������C9;'��QQ��Y�1��I-�����A���?>�ϼ����������������>{
_@�еd�eI�>�Ϸ�ӵx��>W���Ʉ�/�q�0!F�g4�~Y���˗��:]x���L�Z�'9%F�:�:4��s�Njýf��5TjF�,�t�Q�1ͤ�	���"m$��Z�UX�Uo��#4�p��� ]�5��i�i�I�[Ĝ���]��Z�Q�d�N�E5���P�q<�����JO�d������L1�:�>ua�]2���R9<.6�w���
$�b�5����X�5�ht����H���p|�`�#t[�@}���P�+���
��f��߇Z�릞�D���է;RN�&୏�vq 1�����8��ň��\�4#��H��H�X�;,���ݣ��J��g\��͖��4�>�W<I�b�q��S�*�ⲁ��J6�ϖ��E���by�����kq���(�U��~��9�d�Ȝ�-Ѽ#�Z�VO�W�ryC�U�m�ӹu~�i�~��﷈��U�φ��l���Y��<y��l��[�K{��|>���(�u���wƗƹxN��1aS���*�>�)[W(<\�0h�e�KƸ�8/2X��u{1[/��C�@��2��H1ݑQ0K?�>SZG!L�K���=2����\�=>?j�m�%�]5����.�Si��o�9[�kT�RYݴ�v~&萖6Q`+O~OΣ,8�:_�@�J?)��yLA=(C=X�@!`}�Y���q���K7��9�da������p%�e�q*/9[Q`
�?
�2n���%h�ل�)ݟ?U$
��N�(/�D&��Tu{B_�(�u�[���$#sVϬ�5�g�Pv~��͢�{P?/ڜ��[;�l��)%��%& q��IL�Ε��hIY��Q��X^��Ӌc �؊+ky,ȹ�u��so�N.M^���x�*M�Ƌs7#�x��w���>�pj�c��qO|L�js�a��.6�I�{�J#Ox_x\d@(Z�PM�e�BZN�q����̅�q�z�YA0�#�fݓ�)��4[ݽ�~�2�9��3�vcek��\�l%]���.���{*?z��%�0�%6wM��ݝC��� �����Ĺ�'���$:�ʛ���[[hSP{%J@q�gj����$Sv��g�Шd}�\P�ɲ����kf��Z�j����xI�ʂ9�K��sm[v1���q.C=��I�.r����x���J�l�:uE�S��\Ώ��>4���iMs�$c2&W�%v�T����Tw�h�ԇ!=���{�P`�M;.�T�����'�kǁ��������]-���,�M�f���˱��]iAW���Q�wYr���и�#Qٵ~v��ء���:jT�-�'���ECުl0��l�����]�z�\�TӁ+ueH1���=q�P}�֍,����w?즫�=��]�[y���&��U�FQ�xp4�� �4�� ��F�x��P]�s�S���}��5thQ6�{i��y+ƭY�%�B���J��f�:��p���LR�����>����;�[�~N���Z�E�rS�4N��op�Ґ�9��$�8��q�B�QQ�}�[��\?,��'K˜ϼ���,�ZU�eD����|����q�������
�z�'i��'�Qx�1�Ps�sӱ����q�:����l���>��r�=�7ˊ���&�ΖڐN��M3x�kZ�5eW��T�_WWj��Va1o��N
Sܖ�|�b;��3r4 ��iJ&��E�Y%j
5�̨�Tz������h`Q^�����$��G���&��A2`�)u�I�ԦA� ����ֲ(#��2�����M�=:��#P�N��|t8 Wi���
]uz�u�z5]����;ʓu���bƐf�XHw��3�S"6�7}�V�G�����	�,ze5<�k�{��6��"��͚�q��ΚM�ޞ�C�x����?R�K�f�i3�s��eߥz��4U`n�E���&?$��[lgV_��>�a�?�
K�qB0�x>�
��6��@Z�-tx�׫��3쑹��=��#ް���ǣ_�z�q�l3ZtnE�(M����GK+�ˡ
�ScY���u�e�:�5�F�vI����`,�{�Pz�Pz��t�H](5� ׆����l�ѭ����0��D
�G�7�-�,4�S� ����y+m'6ǪPoKH)F�Y�-�i,�9�5��������?ϧ'_{לȴ��S����lG�J��F%>�ٛ����Ȝ�i-o�+�*�����#�Y���3��=�n�������ˁ���	�[�T���\�R�i�Qv�A�L;哵䢦��\���-�����s�{��Yh[h��P\^��v�]�}(C��`4�����h��L7���S�_\�(D�#'!R��AjƂ4�����tB�}#<��@9��(3? 3? ?����KM�w\�fLB��5�qa��L�&��N��d��p��-�)��\0�E'����ƥ==K�F,[�tÖ��[�~����ۇq�I-��=_��ӨK�\�|t�U�t����B����%��BcFH{8n����WZ��@hзHd�]�ǽ���*/a�̖��M౮]XD�f�J)�/�:�vQm��o,����f~�&�e�)�V�f!���	ɅqY�`�M��ԉ&�j��ڙ��՟�� i��W�E�	DW#a�UW�Ձ���m�\� pCE��ߩ&~J5F�w��ԓYt��O���dy�Jm��V��(]������L�h�����,ICe�k\��}m/&�ي�%�Xi	5],�������VQ3EW�����E����M�K��$!�±QArRL~�^q%n�l$�Q��!L]a��%�ma[no��ۻ�9i��r{�]*���V�&�_9K�t���������W�R�I�l�>������Z;�mվmÞ�TH2�\}�,{��"9��s���%C�?/�����ʦx� J��dDbF�tʎ`"��[�Z����7��1��2sZ������(�gg������	�5��T�٥�m�����餒>��Ơ��y6P�.O�a*�EYg_#}�z`����S}	_mVv:�׷��yNZr�*R]���.m&/��������\���&�P�kT3#&'�ǽ��yT:�q���]&h��4�움�Py�޻m&]�TnOy���Ȓߠ?��,���Y�E+�Zjh,s�[Hb�܆e�s����y��c2O?�1�S�h"I�Ĭ�>�kl���vB	���>�O��1Q^���ٝv�9J�ꁷK��n�F��n:d�~(��G�̓n�,��|��_��-���	�'F��q�>/R���x5]�Đ�����6�Z��+f�ڢƒ)�H%c*'�9���/'�3�ڵ��zۮ��wȝhN���'��l�	�a�m,d�MI򨷸X�؝˹Pq�j��i�}����lt����eG6����LX���O�Jr2�5� �	�`���K0�M�]� ��`b$��*���KD���X�K�b�v�F���cA`��!��}��F�2�N?��y�N����F��}��
�?y�g0'r=�ppi���π��N�ȐshxP�/���*_�z��؃�/�{�Qw�j9�5���� J�|�R��ؒV�x�[�or��I��C�x�2��!�'<<A�(n:�K�Kł�(aCD��Od��黱��d�H��R�"��R�~��HCӁQYt˲h-Q�]���+���E��s����4���?���J�Ԟ�*�w�J>f%���Ǻ�ʱj~�IIg��rS���Ge�5� ~��� D�p�N�QLJ3��o5�b�?��1���e��&Ye�����̟��2��&���9�[ݼ��_�o����Ǡ��[��s��:7���9='����dba�?����	�l�?�si�|�'���
�:��yLH�~�_Ą.&$��	-6KV�Ƚ�i��sa���\}�4�@+���hX�.���鴿�
,������/�g�����#I��c��L���	��@��b�a�j�\�ԌX8(�ᘡŢ�H�pC��-[N�m'���ݻ��w^���~�;S�v�n<:������D��c��|7�rӽ�Sѽ��p*g�4(κ�{�m�<٦\�n�8�6Z�g��/N�-t�;��~�_Y(_�SyRM?saF�=jl>��մ�3��ͥUe�mY�Υ�)�T��U��*#�M_�y���5m�{Z�g����f���x⍮O�b��B�_��(�y���-�DQ�����q���AiVn�@���0�wy]���r
^	���J��p������N�T�&k�h�Y�)��hUm�U��Q��m�
�f��8�{Q{U;��U����G��(�dt�E*�Io�^F)�s�1�EJ����_f�y��d�^����!&]?M�E���1�i�V��x��å`2���ܕآDRu��L�Hb8�N7w� ]���mF�b?\�c����v}r���]�n^�rT�'��t咂������6���E$��t�6���똈�p��tZ��tZo}^%_��t� ��c_�%��ޥ�������
���m{�K:�.ߙ�.�F�\���z!��>�F��m����rO��9�O�$�$�K�Z2�lL�MM�uN���%����^X^�!9q��N.��|f2OV�#V����<�:�Ϝ)Ϩ�Ł���i�`<�ؕT�8�J>rq���l�A��� �ߙ6�U(�{�Y���U �'يQ/���Y,`��bep�)�(���*oE�l�M�
�h����X���[y}�"V�V�?�'6�PDT��/	���_��
^y
�"J�$�/ɪؐ_�U�D�Q~!g�����d�H�e��]|_I�*RF	6�+�RQ�P�l�S.�dI���v�_X-I�$�h��e�b�w����*HX�!QFY�FC#���
^�,��,+6L��JvE���o�͎\�� Q�Zm6��,v���n��+����輸��5��"*P䗍���
^�Y(X5EV�*�/��KVe<�Q�P~I��|�_ҥ�����2��2��/d�(���eQWY���\�T�lG&�hŊ�B�m���6�FE)S~~���ɢ(�rɔ_�� u:�7(��eE� 9��Pd;XQ�t��j��<s�4Z��d�����":}T�QC-��]|_U7�`}�����e�#��/���tU�+�����(�QU$U�Ze�S�ע�T?���t���t+�Q6�
4���RYAv��mw�5Uq�s?���2~�E~)*L�/E��/E�/u�W�� �W���5<��a�� ;�V
6��9t���Uu�N��p:TUwx5�]���P�v|�jUEd��:4�l��r����*�>�/�(�x�q<8(�� ;V
�W�4�aב_��6��K�����rP~�`g��ۭv�C���T]����'���3~p�_�{��3t��`EK�q�4����_�� ��/|������Rw�}Ut�A���S�M��r�Oi#;5��p�KӜ`u���M��p�AC�0K���]�&���}:��]5��Rw�}U*�$�E~��/Eg٩����i�u��é�����4�+�ٛ��k=䗎���&�uC��n7���?Y�NU`�!�u~�.��4t�4��uz�_n�/cy�/�n�a0~(
�K͏aʥ�����\1~��x*���j���g�Ԑ��B~��_h=�/�n�����/л9��KG~���������Ft�XvO%�S�%��
��S�`����4<`��F��w�݆�cF�.'f��ߋb�T].�͐CN|-fgNï�ڥ�����&�"J6�O%:>EGt]� ;]{�c�}.'��0��/��N�׌�.�4~�K����5��N�Rw�}U�_�*��"��t���
�f���y���������f��2}^�F�y�2�x��)G��Z��p�B���?Z�^H�1ҰɚOm�.��/��
�ӴQ��~�7`��`sy]�`��M�7�5M�/'�0d4�1��%�L��f�PӌK���U�� �`�ҧ�K{/�~�/�q@v�ܕao���|q��c���n��cj�,�������q�����輸��NadhS� ��v;xe�#+�~^���
�!���7+C_�o�*IT;�/7�>�σ�ɲ�Tz�S�z"n��Rw�}U����PV�x*;�3\>V��>��Q]�}�
P̀'�b�/�
�|��Fл����,{�����e�<hݗ���BCF���SE� @gL� ;
W]$��P�!_u,Q�� 1N��//�0	8�U�٫�Z���>��Rw�}U�a�4��RfO��>�P����M��n�E#�P���H�>Q� �2��t������
��G:a ��~ߥ����D�КEϥj���1Gc�d��Fv��<�D<V	%@VV4V��jщ%���H�jBE�����^�h��kM�'���/u�W%�Ym!d���S&�1���)�h��A�ۖJ&jb�*�C�p��>^��TVW�&+c�UC�ʨ�2�ia=��O�ՇC�K���UI&a^�0�����Y�@<��z �
�S��ҵM�D=�*k�g4�4�&��;j�R�@�U��d�*�t�]sR�US�͕���������h�K�yPa������S�/��
�=�����X��~��>K������X�['�5C�)�� �g�
�c]�<n3qkí����sJuYz��|
\�����QX�]	���~6n~��Y��vX�m��c����0��	�e�������Z@�&`��8���Bwx�U`��B���{_?�uy�ׅ?�6ɐ�`��Y�g�FȒa�����0������K�<^� �WH����]x?�&T�;a!^��ۻ��6�(�ެ�P*�U��Q%R��i$( �$.n�$��0%΂��&�";x׀)�(`1N�G�G�Դ�6��\�c�c�'�v�A�ʁ? O��߼���f�#?����?!���X� �uN��˾�˾����Q����B�`	�_�� �������Cp��\ׁ-F�q��'<��1�yط���/\��s�gz.y�g��Ό�<��)�,;ط����p�!h�|���q2��n�qf6�|A�-�z!����!��]���{Ǆ�w�M���$g�g�fFa�O��S�p�!�؍���l7�6X������%�c����p���5t!�5S��5�l9�2��x|��2��j(��r�79��g]�X�|65<b���f��3�T">*yt��]�D2m&�Kɬ�F����L��1'���1��T
��_{�.j(�
�=�Nr	���(׃\De��O=��F���k�$t6)C<Bm�b5��
�=���[�W:O��d�ͥ�E�l�Wꞌ8�7�*��"�뿯Wֵյ�5�j��E[[���y�V��H���MѺ]\�o���a����|�t��D}'4�v!@�,<L��~���O_�����G_��ϯ��<�^��3q�>���O����k�t��b�a-�Kg裒A=%̔&Kb������EJB��L}83N3|������h��KW��PQ����E^�"��{<���fᗂVH�N��;W~��'��
ޣ)�HN�$�M�[h����Vޠ��8���.�3y�����^�M�k�A9'��m�3EД斩�L��ȨW'�Ԉ��a������}@%��ՐS��ꥰR}�n�[�T��gU�ܡz��T�9����th��������Me��ž�����;7��z;��n��x�S����6���b)V�����N����^��u�g�:`��ߩ��r7L�ۼX9@�������kD��`:�(>�I��3-�� N7��.���?��cr
endstream
endobj
113 0 obj
<</Type /FontDescriptor
/FontName /Ubuntu
/Flags 4
/Ascent 932
/Descent -189
/StemV 109
/CapHeight 693
/ItalicAngle 0
/FontBBox [-167 -189 3480 962]
/FontFile2 112 0 R>>
endobj
114 0 obj
<</Type /Font
/FontDescriptor 113 0 R
/BaseFont /Ubuntu
/Subtype /CIDFontType2
/CIDToGIDMap /Identity
/CIDSystemInfo <</Registry (Adobe)
/Ordering (Identity)
/Supplement 0>>
/W [0 [500 0 0 231 276 418 667] 11 12 324 14 [564 246 299 246 384] 19 28 564 29 [246] 31 33 564 34 [404 950 663 643 620 713 571 537 672 0 269 500 629 519 871 728 778 608 778 629 532 565 688 656 929 631 598 573 329 0 329 0 492 0 522 589 465 589 559 386 578 571 253 253 522 273 861 574 590 589 0 386 446 402 574 502 777 511 497 471] 428 [643]]
/DW 0>>
endobj
115 0 obj
<</Filter /FlateDecode
/Length 315>> stream
x�]R�n�0��>��򪄐�H�Pi?��Kj��8���.I�Z�W3�3�פU}���,�p�l��N�`�N;�E�DdLi�g���[��A�L���6ݐc�gȎ�Ml�W�����)p�\��jn���B�3��%S���־�=�e�Z����2h_��!ԍ����Zs���a��8�U&`Կ|N�s'Z�W�����D�:E$�Ut:p�N�fwsx|0G�`�8:���;"_��$Ş�#�|K�J(�WHfd����Z^Q���F �^�n�6�/@-ǩ�׻�\^���'�1�k���6����9�j
endstream
endobj
5 0 obj
<</Type /Font
/Subtype /Type0
/BaseFont /Ubuntu
/Encoding /Identity-H
/DescendantFonts [114 0 R]
/ToUnicode 115 0 R>>
endobj
116 0 obj
<</Length1 20892
/Filter /FlateDecode
/Length 11421>> stream
x��||Օ��w�i��h��,ɒ�l˖��N�X�+΋�q�	J��v /��Մ	8�P �B
-e)�mB�����B˶�v��ݶ�nڲ�n���;w$�q`�������~��c���̽3��9�{��2 p  Vt%S�o�@lXڿ�ey�Ͽ�Ώ��: ���[v�� �-X_�q�H��G��z U�wlں�Ŗ� ��L�M�v���c�e�u{�_}#� �,@�|�����+��@�' ��<40h�^G���7c��˶� K�b������?��F�n�n�Ɓ_I���Oa�٭�;L<`�a�o�:�*����ʷf��]#ڭ0�=�3��q�Ў��� :
��C�ћ�`�{_�cx�'r��m|�OX*��D9�����,\��n�-�:�x1��jT,�s�8 ض���h2#��笁��IK����2x��� h�Po�`C��h��"����� Q�Q'�T��A�܈n=���^�!���� b 
 �D�#B!bB�a�ۿA"�EE���b1#�!�Xe��ʵ��L�rH &�B�=T�X	��U�DLBb��5�BLAZ{�:�B-�,���+��q�!�A=b=�E���<h@l�ڻ0_�Ш�!���q!,Dl�f�f[��Z�ߢW�!.�E��Ў��h��%�q),C\���x\��+�����:���.�D\�x�a��kX�{`5b��}Ѓ�z��x5�A��Z�W��F\Y�_��0 �7@?�FX�8�C�q6"n�A�����0�5�	�Z���`�V�q\�����"�m���v ��N�g��G�����0�8��^؃�n@���`/�Aا�|L�Cp �0D�QǏ��o�C�?��p���|�(܄x+ܬ��� ��xnE�����m�O��0�xC����)��]p;��p�=:�;��i��>ķ�3p��p���܇�Y��p?�C� ��߂��	ć�ڛ�x�x�/�s�����u|���8<��%��G�_����!>	�#>��C�/!��'��/#>_A|�B|���0��58�x
�F<����v�_E|������@������/��Mx�xQ�>��o ���98�}�^F����H�kE��"�G��H����8���D�E��"�G����H�ƼE�V}$�����Ӯ�IQ��>�����Q��cƩ�U.��ݺ�{t������կ{g@���為��ҽ'��JD��"����c�u�u[�u˕�*��Q�k�\�uB�l���J]SU�^�������9����F��h��H������:F��G���0���7�~�}#ѿh����0��}#�ﵿ�H�'�F"M{2�hga!1"6A{��]�&�Y{Z�[{	�H q)Ծ�H{���,!e�KI��<,#)��d�v
�"sW���W��4!v�6�9XI�h�B�J{V�����MVk'a5Y��CY�=�d��$��M�k�5�W`-٪}�&;�' K�h_�ud��8�'��~�q�0@�h��2��l$���Ar��"�"�����&� �f��l!_D��<�=ג'���u�i�l%�!n#�k��v���A���;�9��p=�6�.�v/���Վ�nr^���7���rA�F�?iw�^�ψ�ȿhw�~��p�����?F���Cd�0���HM�m�qj�0�P	�f�Ԏ�-ԭ�G�O��Ґv�J����m4��c�����'h
�v:G�|����t�v �M�~�m���]t���+��څx��h{�^�V�������ݤ������ ݦ�t�g�m;<H�k��!zH�
��7i����Q�Zx��!~�~R��л����>�G��0|�>����6��/j��%�%m#<A��6���3� |�~M�'���zx�����q�������v5<M������������9z��M��F���)���j8M�u���W�*�:}����^�@����/�	�3����9�v|����
'i��,�Ԗ«�W[縀���+���[\��D�D�D�D��9�(����}0z�rV�Ӽ~�oÁ�w�!r�^�[<�e�֊�/_�n��v��hC@K���}��� �w����������=3j�?��?;0R�a,ۉ�����c����x�S��޲�VAe���s� ����U]+;;V\�|��%�����47-�4.��0on}ݜٳ�U����X�(�Ue�d��l28J��5���������Jv����
���X�6��p�~[x��s��;3�;3SwG�*+­���k-��)����oo����/����sC\���E$�O�[��[��?�:޶g�Xk�wR�6G������[<�l�4��$)]@�Z�:�$��hǹ�ց����֖@$ҧ�A��ָ�yܬ���d�c�g�>q�������ս�� >4Ƶ����eі�}?�b���+�-��(6�t�7;���
���%�S����NY�Ԅ��瀲��ؿH��r�T6�������u6��L2�7N�Y͙�W7�9<Y3�x4�L�ڟ�ٳ�;~xC������ևǹx��������X��%��U��<����z�:���c'�05t��'�;��hS�,3l����?6�6�C���S���&W�u��%' k+��{s�����Ic���w7�Q�c������ ��p�7�������C}�JQ�x�O�.�3�Oa߮�{�f�ss1���Y�mѦ�p���KfѦ�p/	��mȒ����h/���vVűG����Hn�OD
�e2�����)�r<��h���@e�֡���Ѩ1/`����2]��	���}��+Ƒ�e�ы���q��F��}Q��LG/�ӵnߥ]ѥ�kzuk�dՌ�\}�T]�l�6��%�6կ��S��WT/����ѥ]c��h�A�-t��:�6?~�0�E��aG�ml��vx���LflGk�湬�����hWoC@oe���>F��{骦�
>M'���Γrkך����zOR��Ǽ߻;���5<Ȕs�o�Xsmp�"񇌓�\TE�$�d�F��ƅh+od卹r+7�Y��T�������L���ݻ0Od���<\��������l��+q?I_��q�q?˝5$�}����n��½�s�y����,~�KK����k�������qö�v���2���??%��Ԁ�q=S�����}ﭗ~>���ƾ��>�xŘ�VkQ���7�^K.��U�p��&}�`�pF2�/�S���f�D!�Z�5���Bⵚ��K�H�;Sߧ�\RRt��-�2��zNµbI�)I!������,
V� �t2M�/�K9^M�T��:U��\Ef�Ξ���/i��}��ݛ��Ğ����?v������Y�Fl�Po�2����2I�R�k�b]�q>1�⬍��)$.�d.Y@���2���c>&C�4.i�d$l���)[l�l�Y����ӗR��5�z�"e-Ϫ����G��:w{B�}^�\���
6��MNU�����#�P���ة���!��Ք�³�e��mF���">R4q�l;ʞ.��1���v|ڎO�3p�d�Xs���F������x�)ZG��S���b��XQ�LV⁭��ߑ?�Wq��2S���T��mL1��ꤺP��:�W��s�8�3sH!J+�Tb�lB;4^l��������~�.��s������^���UQ��tj6�M��J�Pv-b��ҩB�̒��OuU�����5�)����.;���X\8ˑ����7���d��p��lM_mE��c���@���[�n�����l���_�9/�|�C�}��6Bm���fg���A�@�{��fY��Q���4�/��A����E��zG�Lx#ʋ�-�։_Au���v;�$�Jݦ{�.�1{���Om�;DȞ�[w��5Gz+����\���>��+=���L4���$-�ͽ7f��Xp�D���R�9��O\<�N�L.���tsf�e�DQ�jP&]�����j�x���ګ�����P{͊�b�2�E��ݒ�j�P�w��꫏��9���ˊ��c>ׁQ�׸�� ��X�y�(m�Q��aQ�K�0wM�ю'�s��柤�*��\'ɢl������a�g�D���j�/eU�EթȪL9#.� �g�$a$�1��h\&����[r�Y��F��j1��.���ʲ�BM<����F��F&����@}�A�x���o���	�A�Y�f�$�=*�=�`@���G��R�����Tq%rTN���E�N�!�t�7��N�����Ew��z`Qъ�&ޤ�M�)slު+Z��+��������n�d��%�g���8WS]�`�44Qs��T��dNU��d)��XCP�U�rK�)�B�P.<� ��X-+�Q���	E��;x�Z�
��7��tc����L^�J�����z�b*������,���#ZEJD��cG�XJx%�!ĝJ'�OZe�`���Z��D��U,MT(V+w�A��V�\d`���=;"�O�~~��;{ˇ���Hvx�|�;C+�?�D�o<�=��#S����8*���r��]�h6��F�n�����D�����q*˺���F���҇j�ي�¾0�F�O��(�ѵ2����41��ߺ{6��R�K2���΄\-���5�b�+�&�}	��E�ɋ��Ϭ�G�rc$KW�Ã�z$������9��~���t�t����8���	+%ߪh�=��GQ�`f��$���6�x�n��;#R��0�倳�55�K�$'o�>�]�ҭ��B�yV�c�μ���E�sG���NJm�MΕD�>N'mntUU�+O9K�J��'�[k倭�w�r���݋���͋Wċښ�y/���BŬtB�������!S"�(L~e���[�{�����3�׫P�2ân-L�ycf�5�h�V�E8�L�d��kZ#'��dA��Em׉e��擧&֕�+v��"Ot�^\��̊Z����3��-�%�n�l7Q�177q;�2٭�n�C�wd*�y�U0	�z��B���1�A5�`d2zx�����1�C礹�ürN���W�z��1���$f0��~���;:Y�/�}�M:? q$�²����/�ɚ*ՙ�I��z�;�z^8�XSñ��UU}l�XC�c�^�AU�����XF[!�r��I\\-���JD��Q��!A�`\�&	7����nZ��soqs���/�U��}�EֺH�����Y�O]t�EZ\��E|."���1�:6�Kcߎ�*ƥc�(F�1Bb�������$�T"�D~*�oK�O�"Q,JD��j ���_�=i��w1 �0x�+��HFIY�lW8���)F%���	��U|�~��P��g\.>�H����b,�##���l�ڊH�Z?������ar���ϝ��dW����1Y�s��1øX2_MԬ�W�q:id�#E{��>];�hS8���1km�q����p@�זmڶ-�=|hޓ���{�\��ϓ�'�:<��ٶmX��5�)o�L��J���P��4��n�H^���E�(�ѓL����"�x���8�K����-�&[b��2��m�n��h�`
�!����x#�N�@����{�+�CĞ�F0 ��0\���j����И��� �3�ȅi/yo�6� ����{�Z "��ՙ�b�SeVV���t(�P��+Օ�J���ܟ2����HQ��U#s��+T�uWJd2�ʲ*�~MO��fSz����,���Jļ��d��|�������]j��$Wq�#l��_߉yT�xAG"X)V�Ǘ�����fJwR�Q�*� y����f��N����*��1^%XG��چYa��1���L�L]�8��/�.:\D��P彦NϾ����
��k2Yzܲ��`.s}��N�$�T0�!�LrYOc���+���|
K>}��R����+n^�W_���խ�[H�;m���Qn�����#/�菽l%�C̺�ڻ�<Z(M����L�J-���,��CD���.���,��H�Ȳ/$R,��f�y]��%0�u3�=9;T�f��"!W*Դp�����U�}ss��뇖VH��me󢫬�>��X2�:�D���:]���M {	�:�L����
]���P�d�����Mi��1�2o�.L�Μx2����_����j� Vz�!�jm������pCO]��w���8J$�mb�I���EC��M�q���t�ߥ�i�0�_��S���q��J��_&���JH�u[�H=ޒ�Ј�\0:�B#������4���9]�rn�=���'��2�H�;<��Wql(�+mk�w|���'��2e+|�����`і�YGO��y혟�mi��v�=d��-	{M6��|��.g�@���,'@g�
Z��2^%<g�����v�ӹ�-[�"���r9��\�V�\:+���d�9D$i]Q�v6)/osդ(vYN�:���4��E��\��h���j�~�r�d���^��������UTW��RE���NEE����8�ʋ	�6����A��t�(���ԅl6u�'�l�.;Rp�Tӓq�D�y~U<�0��O��^�B�:o.Yt�m��e����,o�p�H�u�1P_�V�����rWM�s�AY<(:�*��p����-�ldBN�Ԧ�9Sf��S`��y$�<!婫��sۭ��Ù�&L�s��1<v�&�ȴ<Ǖ�.�j=�mǥ�;ӝv/N�Q����g�%��=�w���`6L����\;��N`ܗ��4���(����uZ�>�d&f������D�H]J��d����_�y��8+��*�W�L���)m��!኱�4�#���[g�-q!g�����I�>�ݫ���$�"����L��#�LH�6M�˄p�s���sF��LJs���5�K�&��������P�v��ә�E�I��J�U�P�O%�J$U���"�&��-���1��\X��،��}�L�d1�%L�(�b��,���i����j�%�h5��5N/Y̺t6;� ^��^��׸��zg��ٚ�=�$��gs�t'+Jē��
3)�	GYU�w�8��֦������vtD���s՟�G諀�I%j���$���4�Mf��� �m]�)\���Y8a��!ޅ�I��I�ğl.���K��a�H���q�@�3f)c�D%�l��S*x��wJ%/�P���i�W���&�+
���e��uO�a��\�7q�uًoe�w8S�\�C�W�~!�s���R,�;����E�pW���Z9^\iK�f�q68:q��Q����?=8lO:8�S#�℺L���gÔ��\Dr�\�W:a��X-VY�.?g6�桝���c3�mj�u��:b�q�g�9�Τ��/)�_���e�j0n���)�P��e����xz0E�1������s��|"1�̺�9��b-��aX�����������uu���/ش��t���KKۇ��X���٩g@�hR��aX���#(t٘p3S ���ў�q�V'��|(�%@��S6e�zN��+g`��LM���]]��;>5_��U������Km�9���K�g��2g'���p=��6�h�f,��ż��Ӏ�[��<�&uvH,�/��l+**��1�`�&��wEgĤYJ0�zmU�2Qd9��'A�H<,$J!�B��yc������B��7z��S\d�T������x:��	��U
%1Aa�-��;��zf\������QC�AYdX�[���i6�������ccnNf�"=��kj�{����2Z_���_�������LJ�[�)�v_ۖU|�k% �JfǗ���#��"�%�-KE����{%��P{�<H�Ymn&lu�n�9<a��	ǉ�f�; F��Y_OM9s�t.yp�qa�03�����3�DR޴�h���Q��>p�t���ȼUi��S3.T����
Ӭ�jE۫N����*|�X-���%�8��y�`Ugl�٤x�b{�{��0
�Y�g3�u�M&S(�ޣ<�|_ኔ�B�E��}����!	3�[>�
�x��泗���`1�q�r`a�d��8��BVZ6X���Zb΢X%�,09I��tv'���So7�}غ�-{��%��.[�� �%��5���`�zrKz��,Y���z�kK�xo0�k΄�.�S���PWF
�pxv�ď�8PL�%?�s�z�buݨ�Jf�m*U%�cI�f�.���1=u�.$�Kak����R�[èN�~�|�w�K$�,`�r��\Z�sg�-������65�Mew��o��Nv�'�,Vf�ދl��u�e/s���D�9�V�F��ʤ������}���v����p'+ʈ�Ʋ{�������b�k֖W\���u�]]Q�vMw���6R�����Ȩ5��d��B�<e?{SR��ו7�_)���W!��
w��(ϥ�.��]���<�98��,�}�N���H*W�#ab	��ea��pp*��
IX����u� �M\LծHb�� }K9E�ݨs��#�"�tE)J��Ngw���%R�4�&�>&�P���\��%W��F�b����mN�z���0�U�j,��s�=1�4!��+�C�� �b:9�����2����7%�|`�Q�Q��Q�2�Tc��6�ĄH%�A�q��Q#v��:lrV;	曼�a�nXL�l>`+�I���lrz;
/5&s�v�f��p�+2�goS�P�-
NL,w�[�	��<L����\S~�7ֵjE� �N��[�8�g�K����i(���sq&R�$��tZ=A��a�����d�b�R??���r����)���Qpf�G\8i���:�p�Ut>�U����tw�����*}jcw�]ZI�k�?�h���PZ~Km���^{Ky�ު�ħ�k�o�:&%�/�Qz��+�"��#	&q�z�q���qT�pB���s�ΐ8�K|�V��)�~�Ȅg����
)>M:�#���J̶<̲��`������t�ߧ� f��&��f����&�Q��8��b2a�n�++��F��m�����WrX�x�`a߰��0�a6��f��l0�V���`6[�lb�v�y�Y�`2�Ş�Y�,f�+��j��Gp�n�f�7���l<���(r3I���q�1/��M`?��v��Q$]�&�-o��,�W6����O3�dp\΁��އs�r�E�}��r�h�"�sXtY���0�8�Wr���*ّ{e�OrX�����l��V\�Y�������)[�Rs��)�����h�`d��}>�e�7�(� X��Q0ɂM`�c���=T��"��h� 
2���$�4��j��6��h3�6���)�S�Pۇp��ˢ��@2q���!���4�ݞ㐱���M8t:0ZLy���P1�p�Uɐ�!{t߰0Չ6ю�B��nv����t���὜�L9�J����]
�v^]�!�$�*J�I��.��&�݉���_�a��8�E��}���o�u;��]��v�恀8́Nf�9������r(�OE����"H��9���{�y��sX_�8��p\��b4<8>��^]�!���&�9d4�xG0(��8TG����r���Q$E��2o�y��(`m2�G���1/�y7����\r�þ�2�CFET�E��K���`��G�C�� {�r%����V�^$�^y<!`�Ȇ}V��S��܂�Ӊ�vHN�	T �GB�4P�m���C8<��q}�[;�s����U�!��:�!��h�r%�%�F37?�9�j�Ͼ�W�" =����*�\�*].�h�	��ꋣ��@�A ,vK��3� ����)`�5�+?�mzXA�n��v۬.{���F'P܌�����80Lr���(`46�"�G ��py���A7rx<:����՗����B�uϕAFc��'ZȾ'�Wq =t����^���ڬ{�����T�.\������5́A 9�y��B��AoI�}��K��#���s�|��g�z�1���:}��]L���gz��  �$�M<s+b��W���(2�H$l��g_�� ��B@*	�ӭ|1��
zD*雞,p��M���?s+L�PTPG�^'�!B_aЅ��t$����<O�Y�c��Ӂ���1���*&�Ņ�eH�掗������+�"aO8�Cru8��%�0����9��@���S��+9P1e(Si$]�}*��{q��=�h0Z�+*��"g�(E���"�����X4 �!��ѯ�Wr� ��T��7����j��K���������Du��疔�B0RXR<�E~fY�i�#Z3ؿ��ֺ�w�����m�����4���J��6<�S�LV� \�Ѻ��u����[��99IC��~:h:�����/�9���eϽm�o��=;3��]�&���5�C�~�z5��=���J���Qlc%�/���!�m��h��a�����mz[x?���`!�-�q�w�xh���Ay�S��*���}�(�E�05
����f�"<9e��dc����d���/�A��͟c�L��sLoI4n�r/����ų��H���ޗ?gs}���P�?7���ύx�;n�Co7l�ݰF+��}o����3j�S�-0��#x���� l�ex=s�&<��d���5c�؋�o��6cY=��S�5#�6�mlԹ�y�*�V<g�CX��q�v��z<aߚ��\mz{#3�ި�W��Vwoؽmdwe���W]�k��m�ꪺt�8̊[�پm����e#�s×��w��\Y��{�߲i�H8U]Snض}ۖ�ׅ�pxٖ�C�v�wo�><�yh�����Fr���5U�0���na����`!�O�����xd��qT;�����N��c�����^t1Bx�������ӂ�F�4�������:���b��No<���l+��B�o۶�@h�@Yh��`h��,�q`0�}�`q_�`��{0ԍ�]x���tb񲖲В��P;���:ZH7-�C�����B������r�m��!���rk����M�܂u֭�:E�71�S�Υ���ʥ�|��qr�xq�L�qӭ�нfm�IB>�w��CSp�x��w�s������'��ԗH@br[��$#z�����kd�`e#��u�? dtD�
endstream
endobj
117 0 obj
<</Type /FontDescriptor
/FontName /Ubuntu-Bold
/Flags 4
/Ascent 932
/Descent -189
/StemV 172
/CapHeight 693
/ItalicAngle 0
/FontBBox [-170 -221 3475 962]
/FontFile2 116 0 R>>
endobj
118 0 obj
<</Type /Font
/FontDescriptor 117 0 R
/BaseFont /Ubuntu-Bold
/Subtype /CIDFontType2
/CIDToGIDMap /Identity
/CIDSystemInfo <</Registry (Adobe)
/Ordering (Identity)
/Supplement 0>>
/W [0 [500 0 0 240] 11 12 356 15 [246 340 246] 22 [568] 39 [737 0 0 702 0 316 0 684 563 897 756 0 644 0 667 0 0 707 722 948] 62 64 371 66 [500 0 553 604 500 604 584 422 594 589 289 289 579 316 862 589 607 604 0 422 485 444 589 550 784 0 547 500 371 0 371]]
/DW 0>>
endobj
119 0 obj
<</Filter /FlateDecode
/Length 338>> stream
x�]��n�0E�|���"�	!%��X���� b)R1�!��f.M�Z2ҙ��0�ձ��(�w��3��i��4�7+I\��j/��j�eW�w��i��t�{y.����h'�ګ�BO��f�V_��<;>ߌ����(�(���Uz��kݑ�9m])�o�i�r��!1�P#{E��%�Z_��w
���)<��?\�.���-��.<���)�0�1S�1%	h�@%h��J�*q
�@ϠS���tb���Y��1�S����aD[�NLac	�x:�1��x#�ISI@�c�1]�@d�vR<��t�[�B����͸�Sެu������k5�7��fΚ�/����
endstream
endobj
6 0 obj
<</Type /Font
/Subtype /Type0
/BaseFont /Ubuntu-Bold
/Encoding /Identity-H
/DescendantFonts [118 0 R]
/ToUnicode 119 0 R>>
endobj
120 0 obj
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
121 0 obj
<</Type /FontDescriptor
/FontName /Ubuntu-Italic
/Flags 68
/Ascent 932
/Descent -189
/StemV 281
/CapHeight 693
/ItalicAngle -13
/FontBBox [-167 -190 3585 962]
/FontFile2 120 0 R>>
endobj
122 0 obj
<</Type /Font
/FontDescriptor 121 0 R
/BaseFont /Ubuntu-Italic
/Subtype /CIDFontType2
/CIDToGIDMap /Identity
/CIDSystemInfo <</Registry (Adobe)
/Ordering (Identity)
/Supplement 0>>
/W [0 [500] 6 [654] 11 12 317 15 [246 293] 17 30 246 35 [931] 62 64 322 68 [544 555 0 0 518 0 550 552 249 249 517 0 828 551 555 546 0 372 0 389] 92 [478 0 326 0 326]]
/DW 0>>
endobj
123 0 obj
<</Filter /FlateDecode
/Length 327>> stream
x�]��n�0�����.*��I������@b:���^��6m�E��;�1AY�*�;|�Q��x�kea�Vo��kF\�ҭ�o94�^\ϓ���������g'gg�9���'�[����.k��՘_@;.XQp���ژ�f �l[)��ݼ��G��l�G�!�����4l�/�r�O��?����U�v�X��r!�]�P���;"��B�@�Q.�\,�ND{�4AJ�,"ʈb��虈zf�3���	�����ǄG,�)ڣV���%يi �<P��N32��C�7t���}ߗ$�����O��YV�k��7f4�jy� c��
endstream
endobj
7 0 obj
<</Type /Font
/Subtype /Type0
/BaseFont /Ubuntu-Italic
/Encoding /Identity-H
/DescendantFonts [122 0 R]
/ToUnicode 123 0 R>>
endobj
124 0 obj
<</Length1 21052
/Filter /FlateDecode
/Length 12331>> stream
x��|	xŶp-�̾o�$��$@	�4Kb�$,��@��H	ȕ�C����� 	�����nx7PԻ�*�F��O�LB�������{�{��S]��UuN�s�,�=A!dDU�����ag�,���:H1������u4B��Ec-.G:��3�>y��J�x��p�!����>Q��!nB����ȅ��T��4~��q�6v)@�\�P��c�K�'�p��3J�B�z��e�x�u飕3�x@�o!�i=�lL��+��� ��h�rq'�{�{'?:��cV#�O��//���PBv���Sǖ�uk�*��>�,�c�G�y���=�y�~gE:��9���n3�����qĢ�ȩ	�	ǡ{��=��FR�_e�U�C�!|��@��|��J QH6�b%�K�gOPC���	�?�~=�H��8����1h{U�u��0\�G�#�����P��C�5��@oAia���z�l��:�^@��1��@���Ga��Ji=*����nT�f�] w>��*zWc��P%��jv.Wý!@W�A�V��q� 8l@��>�ŀk�n�\��u� ߢ���L��Yh)̰���7 ��h.@�*� X (��+��C���P���	?��i����U��4�!��	��
�ټ�+u��
{h99FT���8�Y�J�\��K�h��Yh��}���,>�D����o�n��h ��o�����"c]\÷�2p��?�EZ�L��@�f4ܔ�����9�g���h&*�r��ƽ�H܇���� � ݐ�@��`~ް�C�zp������<��էw��Rf���������SS:�On�������q��&�A�ըU��s�`��᢬������Y�����,Wi���Y�좐����K���(U�␷�J���YuQH����i)�[JM-���uc ��й>~o-98�+�����5�<P)s	ʍn|>�`Ű�f����Vg��F����=V�>�h�P�B)��_^����J����ZC�J���L��KB�����}�`��!�����V�	�C�2�wC-��$��^^kB���t%����C��VӬ���!sR���O��/]0�d��P���&8���!>���V�F0���-k�#5B��6b���C�}�pg����������چ��~��_]��U�g�Qn>Q���2w({y0d**�]���g��.���loi1��_��w��gnj���# (��12,���h�	U��{�h�A$�$C��=9��ĞǞT5>i�^����_��������ˊCU�A�&2��M!��n���b�vI	*m��Uߒ	�� D�^�;�ܰ.�&���}8�� 	f����a�d���"�K]0����a�!���ǲjRS�Gq0lB���y�����]�Vք��J�H���w�z�W(%KYWެ�>a�X���GQ��RM'��� (�`����,!�:�d\�S�.�u7Λ���� p8��dbj{ɭGP��a������_��6�u�0�|wx��*^��'n��&��fC�߫\Cb�
�	��2���͛�ݨ�5�j���'Ҏݷ�g��;�q4���8�sܾ�/|�O&��=T��9��@M��g�����ńޛ���K�!)7�͍�G�r�
�#�����L��o1C�I���=��7����o�co���h5��}C���t�٭�����{�&X�ʂ���$��K��A�}K��C�)�A���=��������^�A�����%�k$�d����&�~��?H0�]�+X���PRj	�e����n�HC�F��w��R�rJ�r?�#�N�X�јZ�3�%(�$���r�'Rck�T�*�N9j#���%���tDO�5�U��W�/Sc��뱻zQ�kqU�Zr�[TA)�ᒼ���F濤C�M��^� qq����dyK����V�bC`���� 6�{ "�.�����{��LV��X�"��W�sC�I@A���7����t�q*J���U{f���#Ȍ0x��3�G�h*��|΍�M|�䐉�����ϴ3�L�rn�>?��Z$L�� ��,�\-^S�W-P�^M�A8W���5~M��斶#�K��蜺����|EwS���������������pŘi�h����i���gs's��U�O�Ζj�'V�u����G[�m��]m�b�d?�����#��f�C�������������}N�G��!6?�Wq����6�c��}�?������o����f��P�s�uЫ"��t)�*5��RΥ�3[p�.�9�15`�����C�\�m\���Ge",^$g�>�(�$+E�q*5Ɛ�Op� 3%�lA]\)lDs@�i���f������
z��cg��`�Nҗ!d#�$�(*0�  ��f)i�Pc)�-_��l_��H���%s�3��Yȍ<�F�����s6�Y�S[�-��ZmO��	N�(���M��h���4.�O�����X��A&��@0�n��_�߮���z2Ȍ�ڿa�f��*Go֛y��jx��X���4jʨ)0�$3bS�����+�8�(I)���s���}�oeɟ��(K��Y��ޘ��ʟ<\~r��ag>������#���?�����޴���$����I���pI.�$���#����w��6�h�:�)a���'����bc�:] �����}���y���r�S)�,��D@.�������\��6L&<�@D��8 ��M�JH;%�[	v�#����z��k�uu;�{�k�cOf���zx�7Q���㮝CϿ�o��{��c�N�UY^v�5��AH��ȘSRSB8^YE������싈�.���C=j%5Z-GA>E�Q�87L�I��Bi�8�	�l�t����<~��]o?��X�kr��W����W��0z.�>�qt�FC9ND��Nmt"�3,fI8,tڳ'O�޽���7v��7���������׾�) �#���w��c�T�^�!b4�k���9�4�BQ	j'�Ѯ��Vϗ�U�&Q�����j]�(��$��N<��TvQ���\��w�Z��9�3D܎U�寏>�a�c��k���%ܮ�����I����Gp[���Fpې�$5��yn�	e*�Ú�f_�`����:9�^�w�"y޷�:R�Ir'_���"���1�Z��-(,������{�Z>�6�OD��A�}��C�(I�(��J0c�RF�;C�t�?HR�{;v�>7At>V`:%�C�%�$5�C߼���`�S�rAE�b$�H��Eft?'�4�`ݻ6���^�φ����@!'h�aR��(��"萀bb�.lty\DQ�(b�QQT�6V�"�Wi���̰..|xT���A35Bd�H�-+&��4m,�,񠫹A?ݺ��u��ӵ#+v>�fݎ����+��Ey���Qx����n�i�?�/�?aö�~�Y��LMl@�I�z��5X�h���(R���W�a*��}���F��8zZ��L��G��+��c��s�x��r��1w�h�Z7�T�&�F#�7Ĉ6�-6N�7�5A���Qtsh�5%B�ƕH�;���6{�@��nD}���=�}yu���Z��S]�����}��i�~�rαe3~3ż��'C_�ص�/H'����ڡ�R������ظ8Qp�n�x���h1[�A�;��B}��>`���"(�r$�rV���H5%��0�]W�ޝGdy��	�e��ubg�/-#�S���i�2?{���}��|�56.�R��x��᫆,���:�a��.\ٶt�<������~bf��v)}`�c���O���c��|D{<pb,�]�-[J��z��Ԅb���qAo�yt)�2��a� `fH56�M�2��M��lWc�s�~*y����ղ�3��q�r:�n�Jڻ�?j�{�E�R�(��j��T����-�"h��ݦ�������]�@FT*N�q�E&tR)a���H`�U�	��tД�?���}�}�����[����P
��/�����;�ز*�=c����:t&Z#�y�٣��wȋ"�)�'�Z'�J�x�E�#��F4�f��n ��a3�F���+>�$ʲ��\:�2����^���"	"����0�s��U�n�̡��_ڴ�����;�i~���~b�F|�����;~ϖ?���q������;z?���gw��$�.�Q�d�BԂˉ4Z$�D��@��;�hN��o�XA�s���c�����U�+���ױH�1�w����Rn����D����^���������D Y�2���H=��x�F�.�]E0>����h�/�dx-�Z����<���`1�����MN���̟����/_R����g'U������9�/���9��K�l\�n5�U��^�{�ι_,�#?�m����.�2ur�,�j��eS��f�����B�>Qb-:�Y@R�ފ��h��o�����n	�+���zҤRZ��]���~�FI�tfRO`���قF�2��{��I�2j7�'mNU��՝��OO�3oÆ��$'����˶�C����GQù?���g^\��@��(V��D��U�<�V�����Fƴ)�`v��m���R�bs	.�����h�R4�X9^��+��*~KF����sUf�@6$�n^�*Cx�;���y.��s�Bv���x���)�	s*H{�@�<�ja/�{J ���[�1�3{%�\�I�?�wn���k6+q>7�^U�.�ρ�cP��?h�ʸU�v� �GSN�8r ��LŹ��c..U8��ü1��(F#%)�����K/����e�~=j1�.��q~���m�e�2&)bsd\�S�wv���8��n$����M�O�,?|.��qgA3�`#�J��/ ���W�h1ђ� h��*�_�:�@�3��M5�KJ���L&��Q���(�jl���r���sKOc���v�V]�F��~��<����U�p�9��c��N��
��#;�C�R���P���p y�Zk�5�0h�r<o)J�� g�rw	)Z-�98?��,��0<I gLQ@晫��'��[��ճ�?"_߸���8y��P�x�>��%��+�r_~�@.��N�!��	���`���J�f�IE��.d0�Q�Q=o��f��TA(r�BH�$����ֈ�T��6*��#���N���������Bh�.۟��?�_:gw�S�_x��o�7���)/��PR#���2_f[;#��
�Q�f��@j���+�5���]_ބ�ռ��2�Y���9�y%����'?�1s��$$�� َȇ��;���� ��Z4B���jD5Q@T�A��#\2�B~��ȋʃ���� �H]D�{=�)�ƨW�>��"i'�X߆l�/(k�<r�����)���bH)���Fˠ� \�A�d¢�:�%{��yQD�A���n���O���.�%;�Kv�?t�>��-��/t�SD���n���5�G�nUm�M)Jo�q9�.Q��Z��# ����[4BF-�
&��`A�/�U  %,��~����X��xd����y��Y�A�_\�	W�~� "�����N�k�g�8w��6�+��"��dC���9��-T����ܩo�5a���ig�4�Vww�O=��ں��3���ҿ $X��"*1��b�3R�)d���s�d/=���q�
Da�C������_�L�/������z�gz��L���w�y�H	*�Zr�)崜N��Zs5x���4V��|]�1xs�.l
�\�Z�^���9q�t�\V�,��9�Ϫ/$Oן������ |y$�Y^zW�# �$3Y�v�����
}�B_�[� w�!�J���z����Q�Vk��6��ts�U�r��y���[λ�E،w��L�4!��fau83�l�J%Ϯ��Y�v\;jO�N>�9-Yܫ�|������a�VX���#����j#u�)z��� r�k�:^g0j�c<�	`:_����80-�-(fUFe�K���V(�3�pB:s7���h��1Y�q��[tY�z-b�	�k��ۙ63)r�p�A�����W�Yx��@���P"pn��Ï?�?c���:#�-��m�3�A����qxnγ�^b��"�˅"��P�-+�$E�ID$�m�	4*���0��Bs%�lƑ�FQ!i���3�T�اk俞�g�czR��^~�Z�ӓ�e>�Sr�����7E,h����z5��Am�VsN��X���`�%�Rf9a�a�u�"�7+�>,+-+
���l�+8*�+��m+J_��^?����w�>�W�(�'�ĮU�Hf��|�뇞<]�=wQnW�$ep�����Im��#6F�P����wh���Qޢ`llGA�K`/� ����f��K3�ӏ�{��X�M;P�/�9��Jz�8��R��Or�~GcB�?�s��>O/��������V�F�*�`fֲY�}����x\��i��f���7��7���Wׇ|�c?�ֿ���O�6d2�π�#��"��$�3"��m��Y��"������Y\'nϝܞ���Z	�a�Ɍ�%�Z0�[�&PR��Bh!�LFA��=�V��_�}��i���w�C�}�
��Ѻ�g��@��H��R�
Ҥ(
.�@����Ԅ�	����#��	�Ⅴ� ���Ό�8@μ)�g��Io��{���f��yt�h0�(�A�|T@j���@h!�8�^��Tఊ�05�ɶ�]�i�0k����)W�� ���s�@��9�Z^v"<G�\?�>�t���ND��V����T	�@�QTB���L�J�\�A�.Ȩ@#�,]��M�b���19���+ϑ��Z�C��"c`�� k��Q�Kќ��)��V�🀪�r���Ҹ���u&��Ϳ�&M�w�Su�i�*.z�;_��YA_�ς|�n� �GH���� �@�v���{C4q��f���2y�8m�OO/|+@�F6��(��AT�}Q�Lwս{���7F16 ��@�"��n!�O�`�6 k �˄�e?wZs�7, <쒚��r�WaF����U���>)*b��k�ڕ?��%i9W"�� �C��؆xz�i'������|{����I-�D�P
*���7FE[T��^o���v���Xt1ƨ���Q7��x-����q�cL:.Lm0�o�Ρ�K��Z���u#z(>��]�L��NU�)�s㾟��MX���wǢ�@����y��@z��۶�yub��Rͱx�[g����h����gg��rӄ��m��x�����͸��5r����C��9�:fȐf^�9�>ّ��������y�mQ�A�ͤG;���(������D?hy?�*f�h�����z��F��(⸂[x�+��rɂ��g�V��׵����=�59����^:��g��>�@� ���+ѨT��#Q�6dsǔ[1���E�rk���UPSū��r�V�˔t9�&7�爫D*J� \DS���]�0�|Js?Rf��Ơq���#���w/_�9i���mݺ�&�4�?vz��D�@n[Xo(�p����M|TW�T{���梀����R�S�E�Q0�[[�����*��/���aB7Q9,-�����@"#�������&}��Ιo�Kf>ӑ�C�>N����Ek�/~r�'bv���7�g�X�d+�������?�>x*;v@i�z����^��VQO�1.uiL&{n�d����E�@�� �bqG����1�*��f;I������DoK���U��+W���m�IN�������g/�	؂����E���&��$�Z�sς�����	�GEk̹Af�x.7���؎���&67ֈ�3^p,K���t���<�.�HJ�Ď�
�W7��[un�^���u(�Y	[%�sq\X;)h���Q���ʩV{̞Ԏn�->7贙ɀ����ܠ�K�؏@��E\��Ksn�1l�Y����t�w��@;�{��QL��>Sk��Џ��3�<r����S��p��a��Y�I�ys����Q���O���)H�k'ǭ�e�{��W���?=qq���#��G��Lvmu99b��4Z���i�17ȉ&���5�`mTQ��5��V�	���P1{�!��<���s���rdɂ�[�W0�*�g�J�Q7ɣ��0�'�fhP�T@H�q8L�MƲ�9	��HP��Kd�5�Ϯk���_Ƿ�zk�ʕ4n�'O�:�U�h�yfH1f�!���;,�A2r�F#U�F��">Pl`8�L{V��ϥw�j���jy���[1�~m^�j�c�wa�]��V��K�X�fA&�H�iuzdB|i�*����7��_�wԚ��k��(�����r���������Z����fl������p:����t�G�+�trP�"���]ƛN��Wr��E\��w|�Vuᵕ�l&c`���(Kj�HLDH���U*u��M[?g~E;�V���Q+Ӂ���Oj��k�s�D0���3�)����ڱ�4h��@Z�>�?�Jڔ�M��c�^ɋ�?���i:��vsRǍ**�8r�� nP�{7����q�ۅR$��E.�+*� �����A�^!jd(��E����PB'|�o�x3<��.�νz�>$�Y�� ��?O)�������6Qе�$�2������{���~���w�_[�i��ի��$q��]k0NN��?��x�O~����Gp��\��g�?�M���u����3W��V9��l�L���a.�D��<��<�;,���Ӷ���S�̚�qѢ'�"��߮Um���؛�Ƹ&Ɨ�x���>z�mf=�h��b=�%w��Iu:�]�om�i�8�n���(g�)86C1L�f:�o�ܨK��B�s7w$"@8̑�m��>N>Z�~��Y��-�����2������~d,��v�Q����^���_�}d.�Q[�f�h^�;���	ZMZ�`W��i.=�U��$$�T�@�����<��!w�mT|Zт��qt���We��6������	�f�y���`yЃR;Q�X��t��[.��G砎Xp'�ˣ��FG;L���Ѹ?v���/c㦽2/8���;��ظ�˃�������ѷ�����0z����΄>�ީ����=�̪!8}��<�� ��ٯl��α����-��i��46��7�O�0�[����jb�N��ϡ���vbJ�+�@��׌�5=`o�26���t��]g����W��=���	�G�_���4���Kד�mz��@�Ⱥ�.�:�m��a��z�
䯮{�A+Nit�����O��p8��{<3��\��![g�v�����_>��,Q|�,��ŀ���E�kJ4D�UcSxm�'��ؑ�ڃ31Ĝ�|$z�̝���v�J�Ӧ�S �Pj�y��:`d1��k-TKEW�J����`ЊQQ.�h�h�ij��|� �`��9C3$�w_�3\h"�X-���V�Aة����.���9rp�/Ѻ��y^�J��cC��o/��`���c�x�<b¤���ãH!`�0`�(`�e> ہ1�Q�x�P
�Q�p�S�F��g�O, ���o(t�|B~��.W�'�vg�
����db��������t�R��]$�Em �ɬ�h�v�A��M#�s���@K�t	3�
;�;���Wƭ��%t�,�"�;�Ub[�q\�/xB�],L�ۑK��R�dj�����:�B2`������F+P<pΈE�U"�?�14n�ב=�s����ݥ4a�Һ���2�4<?.����8�6��S�:DC%�U)�U�wU7T���T&��|;^_�Q|d3���Z�B�-�#�=0��]Q{���,½�i̼]k��[�sVT�[5~��܂��{��Gf�K�Y��h�s�����dq�/?;1��<�Uv(�Z��|Ż����slS��e��_��ʌGJ�j��z��gz)Ϸ�W�c�10ew�{����]��`�n�Y-���{�.~}�ΰ^b�!����AL�D�N���[�?�Q��q�r��>��k�<bYp".��E�6�F.{n��c�L��̉�Ӌw�b�f-�<Y^����H���x�����ۍد±4Ȓ�~�m��qY%-v�p�;��qR:��_�%K���c�w�F"�@�8��H��#�r{wR2r����1ʗpV
�y42�����u�Z�c2j[�y�:8{c(��\�_O����ő���"&Ng�\��7��9+��恱|'�_�����-ܸh&��.�D�!��J����O=5����o����S� =���cx�|���mSԌvʪUڎ
���h+�,H�D;��������*J�v �`ae3���f��BX� k�k��ҿ��'p57l��6��J]�S�	!>X��,������d)w�}c>���_�ۡ��X�����Cʅ�!UB��}�M��
i6���VC��4>�o���BH+��qQx�pj��	iJ$g���<R(R��Hy�#m�� H ����Է��� 3�����@ymߗ ̓T��� ��� ]��Z��4k�R����t<�'��ÐzAZ�2�����{����l.����x0����3���`���������a������_����7��R�
�$�woB)�!��Qj��"z�ɷ�WG���H� ϊ�)��E�2׬�xH�,@��bsj�ۇ~)c�)fE��N��)��fmxg�,@	�h�Ƣ���N��y&��ʵ<yV_���4�������P?�OF%J+/j��F�6�7��G� �bh�o��5�!�'��U	<+QZCi�(G3�/kU
�^�j�*X������hU�'A/��Ы�����wGK�Ґ9J�d(���cP�F��Z\9�l����e��N���7�Cjj���c�N.;���{����2v��I�S��3a���	�ƖxK�+��c��gN�0����fL[oZj�T�ee�'���.�Z^��A���fi�!0DNqe����1��D ��G��7�A�g
��@��$Nɇ�aȆ<8r�P ?� gϻ���ݠ}W��{���N�<�g�	� %u�'���P��+����R��W)\���#/\� @��rG�w8�Q^-n�;˒_B��fX XI=`��0@/�{E�3ᾇ4>��۹m<�f��|���s3;ݳ�����Ӳ�n�7���s��F���JW��Jv��_&x�����/�<�/q��/�=�/��E�����lωK�^�x�J�ٗ�]�c؆z`��J��4�b�O�>��I�i���%;L� \1Lˎr!�^�bl���ϧ��<�'��T}��3~�߳<�o��1�z�~=7�S~{��?y���:N��<�Hʱ�ce��x�?�?��M�ͭ-�����vBL��m����=Ru$t��::L�/e�t�%Z��R��OUhu��B'C�hʁ�d���~rr�{�Iʾ�}d��������zlDi0�s�l�� �f�&Ɏs�m-�J7mH��6;���Q�H ��68b�.�s���yv�T�,�d�H����6%�'����O����؎��z�.:c�q]ʺ�us��X�_�:T�u���]��Y3��sq5N]�=�SV���sV�ʴʻ�*�?�r�d{W��$�V�([AS�c�r���TZn�f�N`-�B�R!ц�X{���>�
R�ɖ�l^�gi�n�%��{/��Yԯ��}!6-�.H]@S��9�4O�ˮ ���pM��]yQW��yp��B:�p	�=	�JA�Xc���y(��� �[�,y<�y\IWvw�)>����`�G����&�k�xpH��scp�`"N�/[�&��\|q ��韝�ɭ�ni4�����@z ҁl|1�F6���Nl�s����ؘgJ3�Xi�W����1f�s��јbd,3�2^46�L��a�e����<�ūk�MJ�_+6�R���P�Pv��	KB(odA~�+�W�@�b��҆懊b��C%P�X�

���������>p�X���*+!Wn�'��I�f78����"R=�2i�rM��h���B���N�I��z1��W"�[\A�HW$��+�ۇ��Pƥ	��+V4BTB���s
endstream
endobj
125 0 obj
<</Type /FontDescriptor
/FontName /LiberationMono
/Flags 5
/Ascent 832.51953
/Descent -300.29297
/StemV 53.222656
/CapHeight 658.69141
/ItalicAngle 0
/FontBBox [-481.93359 -300.29297 742.67578 980.95703]
/FontFile2 124 0 R>>
endobj
126 0 obj
<</Type /Font
/FontDescriptor 125 0 R
/BaseFont /LiberationMono
/Subtype /CIDFontType2
/CIDToGIDMap /Identity
/CIDSystemInfo <</Registry (Adobe)
/Ordering (Identity)
/Supplement 0>>
/W [0 320 600.09766]
/DW 0>>
endobj
127 0 obj
<</Filter /FlateDecode
/Length 319>> stream
x�]��n�0��y��CEB)m%���U�?���t�F�=��Kl�J���ٟm�$U}���x�����;c��q�z�c�L�6jZߪoK����	��v+
Γ�'?���Ȓ7��{�_U��:�=؉V�\C*����'h[�:��4����9;�)��iԠat����B�S��N����\�N}��w![�tSF��������H�5���dJ�ei��=��ۿ^���$DN=�"Ij�fD�$�Қ�d{�qr�II|�A��,E���J�ū�+��A]�+�����[7n��\t��n��
endstream
endobj
15 0 obj
<</Type /Font
/Subtype /Type0
/BaseFont /LiberationMono
/Encoding /Identity-H
/DescendantFonts [126 0 R]
/ToUnicode 127 0 R>>
endobj
128 0 obj
<</Length1 11732
/Filter /FlateDecode
/Length 7991>> stream
x��z	|U�x��3��g�	��\$$!! �!�H"��I !��K���+�*(�+2��P�suW@t?]OXo�\Qׅ����Lb������g���z�Uի�WU=	 �Xh��fN_Uy��\AH�Q����=. � ���`Ă�+��Q��&�V�v��0O�oY����f n&�����p� V��M�����w��G �	�ail�s�r7��_p|t#"�u�0 /klj[��K����Gǒ������Syz��+[��p�I�K�MÏ'Y��y����MN�� )=t�eyC���6�#?�?Gw�w�N�|���\��p�I`�S�1P��T�8qH��a>cѪ�F�0*����k䤊�x��2�A�8�  �ĹQ/�TET0�A`lx'ʓ���#+�#�W!��J;ܨܯ��q�r��JY�Ux^�-�
�x�l��K��II�o���{��'�"������<�����s>�K����T�^,IR�g��^��8O���󯰙�ϒ�Z����O7<���=ȽH<�c��'ד��Nf)1̆�i����!�����J����A����G�J��`�2M�W�8�_��7Q�����V�W��V����w�,��?�;p3l������t�/!�(0q�N��%��kՏ�-�1F�w/܉�����z��ED�	�;	w�k��H�MR�Ρ~��aX��g�	��I�p� ��(��HD�,|�zHu3Ī��+�����s��o�	�1���>>�}xe���C�C�e�pq�GUU/*�m�V��{[�����F���Q�����T��*gV���θq����O�L�$�O�0��qc�3:odvV戌Ԕ�aޡ�e3�x�!F��j�*�ed�!(
�I���y��#2�"Wcሌ"�/�b\���XAy�!1 �����$�9���Rd�40����0�����S�^��T�Ua{k��/��V�ӕ6��t��xp�"�V,
�:��(#��x�#2�[��l�R�-h��Di0�E��([�iQ�>TZVUT��x�#2����Be
�!uAH��R��v�;�dז����{냳�Bl�v�E]]�B��P��0���c�!��-,
�S�%�|J~fIB�$�W��p;ޯ���b�I��6CLA��Wy�������|^���
��;�yE���;6�����UH�'|�vwȷ�2�8t�򒐵��*�$��� b���\�����wÀjA堆=���{$���PgYU�/�<�A����!&@GN���+�Hg����m[RQ�⒦�{�P�C��лQ�xM!�n���b�f���"J5�~�R%��p���7tI�I��<�v#�d�E�E2�N��(�v4�����.N�8�̪�T�)�XQwv��`c���-!�w�u�XE+��%�e![A�ztU(�H9WbQW�0"��-�:���ݣD��\�B:�Q�^�\�UU??$��x��UnOH��ު?u;�P�y��~�WfV�TxKʪ���
�两�k�x��2�!m�V�bܬ'�!���<�!M���
W��q'��01��F1BibQCat�_ETEݩ�����v�NA����D��QƸBK�Z�?�a
���
���E�^��6x��F1$�VѽQ�(Z�*C�y�V3��R�	<8�ߡ���݃�������O���ޒ�.J�%��/ij�Kי�J,�ڋ�W4�VtW�$���8��N���VT�Wfc<Y�^MyY���̜<"C��n/�\�-���UG��7Ϭ:�� 0��=Ǫ���4,C�I;"�PJ���*��G$�Ne�SJ����������0�)�(Ya$amU��EF����\��S�n�*��*I+�X����	ED�QL�:�b1��qU���!��:��щ3����+f]Y]u(p�rGF����jDccZ)멣��7v����M�_"މh&�DD�{&�b��)>���#x5�k�E����N�}i�P������_qw�����cP�2}2��|,�| XuҺ��o>��L�<_y�<�$2��Y/{{�_~>�|dV�Vp��ܪ����Z�s�K�\M��MX������;:�n���>K߉��ct�챎�k�[Sˏ��"�k��v�e���+}��4��\�@��`���"�@�R�4,�Z�
�)�:�u�l!cǚs͹#�s�3�1{ֳ����LL�l�5׽�ff+RqHz|�P8�'� ?]Y?2��y줐�y�.��7���d$�wI1�~NdWX�(7dd&ob�;R>����_q�T���~0S��k��cA�Ȼ�[���m	{N$�IP؄V�3��u����z7?\�<�ue�Νj����EFx�2f�œc!�2�w���m�$7gtR^����K���a��w���U�7�NK�.o�����<"�w�:,Bd��W~4tj��S��N�}g�O?�λp�X#a�$b�DObY��M�Z�Q��5�:� i��k�	����,E\E#�ܨ�<f#������MnM������Czg�5�-o�^|y�Y�9V�ƆPm�	1�	Z;oOx�`�2���*k�b�b���Ĵ�-L"��A"D���
�j+W�RA&�1��Q�ޡjM�DT��nSk�D㱯�9��U�5����(����w��n{�?�;^\���e7�/.M�?���6�Y���Ϩ�	�5��i�R*L���jp'$h�v���yx��M6������7�0o3�1�0�1�Y�y��1pf3+hmA�����s��e�y�ϻ��g�>`�C��$9�踵t�i({=,7'��M�	� {�S�;'I�{}aǝ���^���������o�x�u���?MV��޸c�f��hNEI���v��G�ٛ�Y�]7�gסg����@��j��lZ��I���i9����w�9���귫9�w��>���������$ś��h<V��ÎF�qu�~���D�h�\��cQ��7#�}!��{_�����'�qV�w�7��a.���V��`J^��rb|�%eZՆ�X�jX�����n�f��.�YkǛ�WΣ��c�5�.�͈M�
f��N��]q5�b�������^���W�I�L�ey����?mV�v̝�����i&Ed�z౤��>[R���5�5�vw�6�Y)D�!C����h0J�ĂV�m���,�D�kע�(<tf��B<y�0����}����|yo�a �%c>�٦	u@]��P7I��!ޚh� M�E�ef9�zO�'�+0�dJ��4lzǵ����Ar-�~��5zL^&�G�H���Qޡ���Q�Q��.|-��s�֟����;�o�-;�l������a黋�_{���:ڹ�ǖ�}�ؓ��99�S�ÃkrS���sK�������Z�h�u�0�K�ht<�i���g��	<og��6�O��s�Q�sr�h�Q�9oH����o�G�� ڔ��72���@��/���]��4���9"?*߱�ɤ�Ξ-�����$?�g���.�Ԏi)���	JFL�l�� �@��Q�i*"1N�Vь%��d-6V�]�G���c�����r:]��L[��X����#ǁ��A�V���if����2��2F~EU��̮��Ɲ߂�쒎UG�9?t�P�`Vqo��ܿ�vw#$�HH�a��#�F>�e�@�9)=ᓒh��h$�HbX�ƨ1�9��o6�2!��/��se
�hn5���qF͇������O��)fY��L�6�nd�e�Fb��7����Cg_;�qj�V~w4��o�e��q��#5������e�Wo��n׾,7f����F2饓�ʚ"�=j��klXV���35��{�q�[p�KT�����!.+Ǳ��5$%�J�V�C?�ԯ֛�$���ϥv�M슘�F硥5�4Y�6F�����stUoђ8�I{����>�x�N�6����[���;/w���ߑ����uAO{<�]�������4.EI+�6.�I�<���txj��ՆR��'z��6��1�6���OM�X� K�9�C)��@����D����0-?ȗ��'�)ʟ���~�t����^��$�&�$���Ɗ:�n������T-�1��M��q�4$Q�b�V�ޖ�l���o2�4�R?�q(z��o����R^z�i�EE�MA�ڜ��#=��#�.o��C��_��p�!qZ��������R�Ia����$[/������{�;�s��J[��.D]�!*�q����ce�!����2?'�1&6.4G�_c>���&8���厢� f�G�DcTj�E?�-2˯��l�摯��o���7,�ݘ0���ȫ�56�FO��S������'�';���v߾f��0$q�TC�s�x+!j��u8�(��`�̡תxQr�9�7;�LT'�%8�T�C���l�?������=�vvΛC�c�^��]�[�ԁ�kY��^��Z�F��+�|�	3�T�e�,^�^/ZĬ�ޞ\�w�M��Q���)�������o��\��2ƫ� ��<j�jvPXg���M����fΗ�^:}r�*|MѫÎ�`��%�����3iڝۮo�q�G����]i]rǕ�~t��`��g<��1��m��R�`dKN��dƔov�,`��!��-����:<P @�#�.�6""ձ٦!{�>�b�>�����ɟ����ֶ���r��7+��w\������F�������G0�)�I�2�1����jJ�Z8�����@�qF"QR4!�y�0���$x�2�]��������ez{_<s�rl�g��hFO%�-�N����
&�'�����;��p�+��%d�R�,;{ی�#6�_:[~�YK�6�o~}��&v��~��]�=$I���o�:���5�3��5��tZ^1KFNN��s��%@�����p��6 �[EY��I�|���m��H�ꕧ�I��o	��\T�f��V�ѿ'%9�I�)�Cwav8�+a~[~�nvz���
d���w��N2�*�Oi�|vg��-7��}�>�'AEH�f�+)�|8RR u�V�u��i��2|����V+W��%�t��EkI�(���&�������5�J�uڕ\��#�y��a�}RN����Ϫ���7VͲ2�͕�?�X��w����([q|����s����<ۗE�=��[��M�p30�dIN3�.�+.��ٹr��d�#_]�F�������"*�G���mD�W������L�Rf��[�7�c�g5gXֶȁ�2�������x��2�c�v�t�R������p�+�J2���o�|1��|�eF'�3�ڦ榵-L"��w1�0��{��Љ��3�E��-��;!	&J��wqJKIv�V�)��5����`Q�1.�\��d2U �HAचI!�j#!��:.���O���2�3-2�Vj���2n��WCj�˯˲���&f3y.�c��V<T��lO�3��Kh���5�I6�Z�������-�^��.WYl��'9��-��˟��?L��<��q>[j��y�����u7���b�W�����B���Q{l�x@�Mͥ���3��p�-�=�v;M�#�F�0�!�GhZ�)4�C�^�B�w��1��J�d"o0N�W������G�N�Ѿ��cɬ�o�u����S������k���)d����ޝ4]/��`�*�0w���w�O��;>k�%~̴�����q1�����%�#��e������:�,�cx*��S�7/ךKKr�bc�bQL,hH�o��
��z�k7��!���,L�$^���	^�Q���[��C���ơ������[,x�,�]�/�?���J%jsz��hM�3����B��Z���'�q}u�ս�)���ո}ʗgO3���>�8r�C��$�V3:=�0��Ӕ�ōӢ"7?7��ݟ_6���F���pN$V��C�B�v��N=�<IF~��y�u���`����iR,VL2Z���YY�É;��0��N�#����:6kl��k��9��Sn/��b$��͵:�c�xw�m��K��b����+������m�?$o�:t%����n ��cs�'>�Q�d����v��l������٢�8�둅���yK1c�g��tV����AU�h����������+̩�;)y�bv���1n|C�pP�hZn���)�D�zS'�ʞ&ɲT�+�2��b��rY}�6�5�$1��[O?�_1R`�'�k8�c�D��Q���'Д��~�dT��;�{���.f\������̾?��7�T�d��}��]I��j�]��t��N�ߍ#w����__�)R��ft};B��9Q\#�:��M����o.\��v����a�R� B}t_k�!tD���!!lB�M�Ei���
�蘀K�vW,1��bԓ3�	�`6 �6k��_����M��h� O^���ȉh��x�h�́��m��H6F�j��J��ix~mH�Ǣm��@���(Xms�1&G�*|7H�����a4�rB��a)LW��0�5�������qr�}$?������ �I���-�6�-"}�߬�_��g"fY���q�^��V�h�U���jD����4e�0A�)8�Ǘ�z
��W5_�1#u����������lM��u�9mἆ�����K�7/m1�yI�M�[�/�dfgg��<A�3D:cRk]�������a:z�pႅmW7ԋ����X�ܲj���mbj]���=2[��ܼ`I�Xм��9�0S_p��I�2ĩK�2!�cx�^�F���I����<������H ���9rɍ���O��x����	0��Ǒ�r>��>}�Q;�4���@&��B1�A�x'�H\��X�!��B,>A�{ �A�3��$P�CF�@��S�G
��&��2�(��h.��)E��H~��4��o}ㅋ�����3�گ��/�d��t�3��ʿM���s2�L�P�;��]�{)B �E��$	}F����=��g>!�'�0߅�II�\���G�����_ϧ
�&|P����2�@�+��Ć�n�C�C��%����ǆ�=ox�y������2����E���C<_/�Qҝ��$p٩�!��BV/9~,^��	���v�;z$^�qx�a��%*ԍ
�  *)�{����l�rz�X&9Id!00��N �A��FЂD$�_h�x�t`����sRI<h����O�!�=����	~"���'.>�=���EL�m{�i(�L��}샻S��=�=��\���t7ӹk������IF2CuC��/�b�r?@�R1��y�������{~�*~C�w��yn'�}'9N��"��������6n|+"�C�0�^���	�ނ��
�5��Gg &���w����;�#kG���;�츰C�C,Ґ-)�]�N����V�o�0���e��?F����G�.�⛱��ތF���+2���T��5NhCh-���%݁�H .�8�!�?��m{Xԃ�`\��M��e-��a)�s<qU��*5�l�]h^�0!�@�-�Z�=���f�o�0��X�82�'�T�վx��c�T���a�i%�[x�T�T�e���Da�/SX_BJpe1�
h�X�9���� \��ʔN%S}1B~�b�������[�����zw���+9�J3�+M9|%�'��
���k��<��Y����Ɵ�ü&qx�0@�NQ��wϬHO/�ф�KB�Қ�J��w��:����ꚪnB��ߺu+LRʩ�
��KB�ؐh��!���omkmkO�\�-=�-���ަ�Z<m@���W� �mm�a$D�m���mm����(�m�Qlaq�xk�¥���H�����(ih�>ЅVt,BW��A+��P!��M���� ��
endstream
endobj
129 0 obj
<</Type /FontDescriptor
/FontName /LiberationMono-Bold
/Flags 5
/Ascent 832.51953
/Descent -300.29297
/StemV 76.171875
/CapHeight 658.69141
/ItalicAngle 0
/FontBBox [-481.93359 -376.46484 696.77734 988.28125]
/FontFile2 128 0 R>>
endobj
130 0 obj
<</Type /Font
/FontDescriptor 129 0 R
/BaseFont /LiberationMono-Bold
/Subtype /CIDFontType2
/CIDToGIDMap /Identity
/CIDSystemInfo <</Registry (Adobe)
/Ordering (Identity)
/Supplement 0>>
/W [0 93 600.09766]
/DW 0>>
endobj
131 0 obj
<</Filter /FlateDecode
/Length 296>> stream
x�]QMo�0��W��*�v�RU4��>4� ��"�����_��NZ��g�gc'�n�	���I�`0V{���W=^�2mT�!���s"��v���&Q� �{���/�9����z���l>�m��չo�HEU��!:=w��m�&,ۨ���XBFXr7j�8�N���E��SA�O%���U���:O�y�N�,�V��	펄v���n���ý�L)MJv�I+�W����^>2Y3Yp�Wa�^YL��9dLrw��[[�����N�TW��iq4�ul��}�nr�j�?�&��
endstream
endobj
16 0 obj
<</Type /Font
/Subtype /Type0
/BaseFont /LiberationMono-Bold
/Encoding /Identity-H
/DescendantFonts [130 0 R]
/ToUnicode 131 0 R>>
endobj
xref
0 132
0000000000 65535 f 
0000000015 00000 n 
0000204339 00000 n 
0000000154 00000 n 
0000223780 00000 n 
0000244617 00000 n 
0000257323 00000 n 
0000268777 00000 n 
0000000191 00000 n 
0000204591 00000 n 
0000006188 00000 n 
0000011723 00000 n 
0000012715 00000 n 
0000204869 00000 n 
0000018094 00000 n 
0000282198 00000 n 
0000291266 00000 n 
0000018171 00000 n 
0000205149 00000 n 
0000025326 00000 n 
0000205439 00000 n 
0000030767 00000 n 
0000205719 00000 n 
0000037493 00000 n 
0000205989 00000 n 
0000041323 00000 n 
0000206269 00000 n 
0000045916 00000 n 
0000206539 00000 n 
0000049397 00000 n 
0000206797 00000 n 
0000053994 00000 n 
0000207067 00000 n 
0000058387 00000 n 
0000207338 00000 n 
0000062509 00000 n 
0000207629 00000 n 
0000069211 00000 n 
0000207900 00000 n 
0000072761 00000 n 
0000208169 00000 n 
0000076587 00000 n 
0000208450 00000 n 
0000080361 00000 n 
0000208731 00000 n 
0000085625 00000 n 
0000208992 00000 n 
0000089959 00000 n 
0000209273 00000 n 
0000095046 00000 n 
0000209554 00000 n 
0000099262 00000 n 
0000209825 00000 n 
0000103021 00000 n 
0000210094 00000 n 
0000107766 00000 n 
0000210353 00000 n 
0000113558 00000 n 
0000210612 00000 n 
0000117478 00000 n 
0000210881 00000 n 
0000122606 00000 n 
0000211162 00000 n 
0000126549 00000 n 
0000211443 00000 n 
0000130679 00000 n 
0000211714 00000 n 
0000134470 00000 n 
0000211973 00000 n 
0000140062 00000 n 
0000212244 00000 n 
0000144364 00000 n 
0000212503 00000 n 
0000148698 00000 n 
0000212762 00000 n 
0000153112 00000 n 
0000213021 00000 n 
0000158342 00000 n 
0000213280 00000 n 
0000163179 00000 n 
0000213539 00000 n 
0000168484 00000 n 
0000213798 00000 n 
0000172682 00000 n 
0000214047 00000 n 
0000176547 00000 n 
0000214296 00000 n 
0000179668 00000 n 
0000214545 00000 n 
0000182946 00000 n 
0000214794 00000 n 
0000186303 00000 n 
0000215043 00000 n 
0000189472 00000 n 
0000215292 00000 n 
0000192544 00000 n 
0000215541 00000 n 
0000196036 00000 n 
0000215790 00000 n 
0000200032 00000 n 
0000216039 00000 n 
0000216160 00000 n 
0000216283 00000 n 
0000216406 00000 n 
0000216529 00000 n 
0000216652 00000 n 
0000216747 00000 n 
0000216847 00000 n 
0000216898 00000 n 
0000222822 00000 n 
0000223061 00000 n 
0000223428 00000 n 
0000223917 00000 n 
0000243502 00000 n 
0000243689 00000 n 
0000244230 00000 n 
0000244750 00000 n 
0000256260 00000 n 
0000256452 00000 n 
0000256913 00000 n 
0000257461 00000 n 
0000267808 00000 n 
0000268005 00000 n 
0000268378 00000 n 
0000268917 00000 n 
0000281337 00000 n 
0000281579 00000 n 
0000281807 00000 n 
0000282340 00000 n 
0000290419 00000 n 
0000290666 00000 n 
0000290898 00000 n 
trailer
<</Size 132
/Root 107 0 R
/Info 1 0 R>>
startxref
291413
%%EOF