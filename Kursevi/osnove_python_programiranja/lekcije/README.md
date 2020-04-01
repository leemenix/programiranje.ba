
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
xœí]Ù®ä¸‘}¿_‘ÏŒ,î$`p-ígø<^` °çÿ	fj¡–“bPq•÷¶»Ë€«¨”Hƒ‡±±Ó&İÿ»õôç¿»âŸÑª.©”âí/?¿ıë-?×6ö7ãútû÷_ßşü_·ÿ¥vÛ)O?/,ÿE/ª[şó§?Üù÷ßß~ósûûÿİ¿’¹)¥uşÜßî-}şéã/ôÓ/?Ş~ó“½¥Û¿Ñ‡î#T7º•v7mn?~~ûmß÷»Û¾yzşãnÔ ãºÁ®Â½!L¦¿7Dü¥îfjpWÒÔ`ışcàD·N«Š‘+¿îD¯:Ùşb=•í+kr(³n ¿@#×ÑŞ"Q|´}şãÔ?îÍztëáö}3}‡õÈ'šÿ‘şüëM)ßùüŸ½©Liíˆcµr§oÌ\kºÌA¹‹ÇßV¯2®&V·)ôˆsé¹§ÿÑvQŸÜçFã‰ËÉÑgüÈÅ:¨Ğ™ŞöafM÷õñÀĞvô½Wv~ò˜¼Rv¾·÷¬øåñÄu)ÆŞ‡™`îAš¯Ó}ï]ÁÏj|ÒÓü|Ø,‘ï,ÍÈè¸æNê&$z%ºŠW†ÖêÄ¤xü†yìDE»ÇÛ>ÓO#ahİh÷éŠI{”Ø<bgûw‘MgP/î±õTßÅ>Ò3-Ú<æßOT$hğ1kçnìc*Ûyâ7RK“¤¦wRñ`XKİÙËØïècöÁš¡£e!¹ö)£Êo}+Ş°alYÉÓü}RóÀ¾Ë¬h`6UtG¼˜s/•Û/øâÉéí7¿1l¾Q
’D²kI‘FI1,niH¾˜ÃÀ©±#•˜¼[ÔuÖ¨ä•Z&ÒRò.¥h‹†âz¬…é¬¥½»Ùî† !3?ô*q•J&9ëÖ‹g:g	eè™«íOÃƒ¨éZsH vÚ7fC»Í´.ğ]êiÚÚNÎBÿ42Z"Š«×îŒi$¹×!W3íAÓw„¨}<ªA”ÒN.ÅT1/CG­)”?0#-Í\»bœ‡¶Ë>ïˆÀ‘F /ù²Ù>À}#¾E+>ˆVb‚ºŞV|	o¾‰Ói|É9u¼ä”¬nía¿!¶*94Æb9T±¾ü”ÔµKà·'£”Ñ£B;rí"r°e[~5¬êëä×bI‹ÙñG$'½´Õ'!ùdæÿu¯×»j/öZğ3[ØÇaøÚw‘`CÉmàÊ}¹#ë˜*ø	ÒQ•½µ‡C/M#åeØô7Š*Ä#¨Ièíöó›İİ^âó¿é|âô-7êü$£<£r[´!o¤Üè@boÉ/ëµ×Ôª:Œ&æ_zÌÖßÛ´öÄÔf•ÕJİÛò_/ç§tÉù{×÷¯„{[ş¶¹ÙpïÏÅ{[…Éo‡ûÈtº·æñŞ™'Ğm)›~lşÔ½;ßcC4åCBÑ´¾ü©}c½QËŞ2N4Ær\tf†«¿ë\t!ºÅDIÿ'â4URÄ‘0™õ
Ê¹N9­­šhìoÓ¦÷yL«áŠÕºÿışÃ1Ú}’á6¿•Ûò$mñıÜ–gùøü0•b¤»dpnË“,&–›ò_Ããå¹5¿s'Á@ªÜ–¿­
¢æ¶<ˆaEÔÏ÷ÑŞæERµËÿw_ìaaÍãÒ/NL²èab§b,Ûcøs1»‰“g2L_PkÚ%Y§=TĞÚjÅ:¥aõş1›XVÍ÷ô;‚’€tR-è¾pGBƒu(ùúİù ûéÄCÀ(¯¤à Ã:„WĞ|â‰CX‚ÎÊ+AA]\€0¥dàÃ1>‡@f;†+Úö¿Â•}¸2™Æ³˜$õº€+Ag¥@ë\àj#Õ@š¡À+Ô6éÒ¯sW®Ä+Ô–UC©rıUÅ%`¡Ö`¡¶üq]j»c	X¨5X—€%·ÑáX‚]–ùáXæoÌ€¥ìm,ó¸fÀ2,åLgÄ2ÓdF,3ífÄRRyF,óz¸rÁîÿx@Ô²ä¶5dÉmyzYtèïZØßÊ!÷y:.&×ßÿê %·®AKn£û´ l¿-¹1×İÊ…êë×/@Ë£y^şéÅ‚QúĞRŒ¥`½~Z³+Øy¢CÁö½ŠRP¶ØJj[ŠµJÃ
>‡-Á Ø"¨@!:Gk|çëvïx†P=°ñ‰$Ì‚£‚Æ 6Hè¿¶;Úv)ö'l^Ğ^Ô bÙÓPã:­U© |ì;}|]a­Ö˜Æ¨Ñc&w‘1!™­¯Âv‘(u±ªƒï‹D•'”¶Ìívr#‹¨ì’Ô§`êŒ§YøÍ·!3ãF¯½ş>|şÉk»şÊÖa‘:K¬¢üz<NÏfOÿ<ªÁãG‡N¢ı™;İŠŞ¢/M–aì]e2[ìË‘€¶Ää¡ğéNòvıÆÄPDBs…q×£JN}nãÒÜyc´´<Jë7W{"¦ÍÊkGN9Z·q´oç7i ëheÍ(\÷=ñB5E&M³îcbŸàCŞ}ÃÔFåOí(­õ§&YH"3óB¡´èv˜—¤3Ièõİî¾AêØdxÚ8×·Däú÷v¤¬"Fğvçœs(i#î6BÅunÅ"Ø¡nEWÈ¨Ÿº1Ç'¡€5€àQ¢3„Øˆ—ôäü— *¤ Ø1‚œ€ñ; ´5Î¡Ö‘y²Dpg <€Ñ"Û§zÎÇVúÉ‹YØ¾/<ëFL¥l‰ÚQ™Ÿ£©ò}Ÿ#{éñ€Ÿ‚D9êã)’¤3ó`ããZg8F¼°7ûŒÓ!xdÔû2’+;ùÆòãAUK69›?<Ğú@ªgÑÀ	lk ¦Æº¯Êúl…(„BgADgG/q¹PÙ&¸»²U¯ÎÍ³èÍœ/¹ñpGKMµ:«Û6‚À'iû{`'ŠUDäk9¾ÔÅÚ¬Ê"[Òäx>• uÌ+¨àù4©T^'•mÚZò1QJí•úŠ]ØEuO'ÚŠ	¢Oáy|GÃQ•…!€sGÉ½¸sh\æk$5jbJ£¯ªfvp„à‘X0¢íiÆ‡FhåNİpŞp³1è	S@5½Â*$g 0£Îôn7üuÜ÷ÙèV$2aŠÀ„d¡`Û~.NU@ª2,¤ fÂmÍ†Ìp¸||¸ {zeOİ5[‡bÄZ…şÌ`Ÿ0•wÁŠÃ–É»RU‡Ú4;$à}éáAaƒ´à§Øo4pú+‘ÆÊ|)v–Gc¿Ë¥±ïõÆíÄÙÎl0Ù°êpê'·gğÓf~›²rËV™4ù‘,bíâàƒr%PÏğc`1¶fGŠâÎÙgşr3Aß¼û½orÜ­mUÆÚ“¦>9GĞUp|{×»)¸3 ¬AÃTEèÕ~¶
å³OCü‚œšÆy
ÈâU|£Ô°„‹6ç	Søš$˜}ä<˜ÙöJş¨0—@Ñ—ÀÁ‚i1R³™wŠëÔúƒdü§ÓNğ'ñWÄhğ]¸ìX¤Wº8%IõÉRÜÙ±ó‚ëÁæ
\ëk2«.ˆ{hÀê ’à$³yµ¼[­´ĞQdñ¥òH*hàip\³mw˜"|µõß;¥>,ª|]êÕ€ğ!jå;ˆO†P½“Û/:ŸMªDhİ§äæÑ‚vzƒ[F.>¦ÁEÀ¶¿âO±IÂwğğ%oEJ£›½Á.…ÆÎôf_/ÔK}ã‚÷#m{oh_ø5AvŒb§±Îb·†€Ä+føARj¡
üS?ß\Ö *åÎö‚æ™ËMYU+ØbTåiò]ÅìÀJH“
c‹Sn•Ûw1[Š"¯ŸÊkÒ‘Cu}ß,©ÃÜ’ËÁ¸ÂYÊQäÛÖØöƒ-·6l[U=ÄòÃñ"±­EUŒâ&‰şY8<QÖº
ÕwI.ÿÀ=EUu0eŞI†şXÁ$'+—ÔéÊ—ÚNE%0·Gm¶œáÎ!¦á/ ìCĞ´ÆŸ ²b¤ÅOÊ€îDşâÛ~®°÷ñcÙGn	†§XÙŒÉ—¢Ì“ò¾
M
zkøaĞÈMš¿ ê Ÿ€làÆ§ `Bt„I	%ÚWgD•>ÆcË‹€rçŠo>y[œ†•‰ oº ªŞOŒÌ„‘Ô‰ì B>ùàa‡õK(gfüQõOÊ}wç/¤´ï+ìóüÈ­Ï™?óÏ¹t˜ÌÀ.¦Ùêìª¿ü¤Åyôşiñı=|PÕP”ãŠê›lÃÚ/!ââ”‚ª\”k+z­„v{‡U¤÷Ê$ehâ4¶5øË, 6ÄRó‹RUy÷ªœÀŸáVvê:¹ @IÒJÉ>±¢§3½ãOÖ_yGƒğ%‘oğSPÄ]xÒ°‚g¬†qJ™…¦¾§™kù©
h® 
ÇG)7úû—ka»zs%ƒ j)(W-”ÿØìu—âú1aøR¾¼îù HãÁam±‚ÕAøö&®“æÅÕ¬âØ^Š<Ï ¦ÈšÒ,è–nğòCçª„½-óòär)Ãy€"9¿pûôQ¥&ßu•šD†+ğ$J,U”÷ó½Á"²ÌUAêšŠ¼ö7AŒ×µ«Ô_Ä¶ÜŠİ0ğœq_áß•%ŸîG3º´ºõ+Ö8âš¯*¨>•¥èì”âû3ø÷sñó®?f8÷km¸'ÔsçŒª+%ä
íI©j1ÿÊPkè)˜A)è´m>-DEˆFòOÈ‚¸ïŠÂùèÜ IwA»)?Şå”ûÜVœÈø5Á°±Ñ%s`fÁ†¥ŞÍ‚Áá|¿¢Ü.h(Ÿ$'Eb†‚\è¡LĞãâzşùkr@±;†]@H²¾@UE™Ã8dJÎ‚›è× píŸë^ã*ïÌC€ÜÇ¾1íH¨1À¯¤±æ¦çÒKû¾ œ¼ÉG²Ë%îHŞĞ'XêÔ!„*X…Ş` w¨á”¸¤|eµÙÌœ}h8ƒÁ´A~IÚã@¿Z’Ô‰ÄE˜ùïÈÄÅ
¶nœ§7n¹¸íÿÔò	xPlÃ<\ä’h°ár£ëù×NñSÛ`ßÜË³«ò7”x¡éµ!7‚}j½ÁµŞuÉÍAü’ëüJÜ0#lí:°Ñh£JE‘ş+€·Î½ FçŞt‘˜SYJ¤cÎl)|&èb,t…#M°"";¼-"ùÅîp€áÈWŸá‚ºEñùs â0Ú¸¾À Üuà1ÁË Zzç¡æ‡\.æQŠÏºkšŸ¯Ûj["ÑCrÚõ›s8§¶\ŞP—”ÔmğS²ëHñË	ÜÙŸjˆAUˆ¸lß%—şÈY£à-!.Ad€à×‡hÈÊâ‡0ÃÚH‚Wˆó½Üìˆk~=¼ˆ>…³vtãIÆJUñ¡_‡ÇõÖa;‹åCæ²ó>ìipã×°€{bkUN†è‚šEuÜ_ØÂ—Ìü˜P'	VFæ‡2]páEóıŒª×(ö“yzøE¯ù,*gm“ü94“Wò&¯YòæêbpulÉG´¾e\Z?|Ë+{É*cbÈ6.ú}MéÁƒê‡¨V4,/Õ¦††8_ ÀŸ9›ì|°	ÏîÍáO“D¼ñ{AÑÎk®|ÌÇcA”m¾Ä"ŒtM\¹`€<ß¼'¢¿!ÜCØ§&=¤µÃØ¡ãš4´mÃõc¤.Å|Œ>{3L¥\WÚƒí3 Œ5cB˜´ù™EG&©¦ˆ—jªR#ÌñªÜUaUlØ¦%v8;µ	ú#ù@–_Ö‡m*åÇªÔ%æ/â…Gíjrœ›vË¶$’]€*$ã¯HÎ4Ó·TZW²Oê0üŸ½9BÆoXKÌ‹K8¿è4ªÃ{xØ¾Û©Ì”"u%.m¸…¹9….DC½&<ñğ(
ìà£Ãàyÿ"p†Ç^Â2åBÔÆ/PjTY´a–¼‘†’ÖÌğéÑFXŒÀscğãºøøz‹_ié_A“W(RwmıÊú&U÷U)`mVÓxvüR]’´oq«Á¾?L5¾÷)’Á'®Jfaİâ’£‚Ó®»EB®^›dÆS\7¶˜¸`P
ÛòÃ¯™(èƒûdÀ¸%:šĞàaM:Áå*±†6×àXùşvmlô’‹Ôı ¥ £5Í·“¼¶ÖÛ+İ¥b…/(-—£%XC²W„òõRG4{¿²£ğ¯ğÅ\pÇ¿Fô+#ç_Zn=ÃÌ•¨×“[±õÈŞğêæ\*vlwC˜ÿb¾¬uîÜVÖàÊ…—Öhƒ¬[_GgÆ´A›4ÄõÕ›ô¸¤Á½ËÒ.|ü'—PzI%¶™ŠR.È$ÄöóÕ•˜¼sc•%ä2MÙÛ¯nëG_áf[ôÍ«ÌØÛDb›r¼°F•Ñ†îjaIäõÔıN—i}Œ€Æw¬HyI¬?¿ÜJÖ”’C™‹ájë+¨(—),™Èchà^öÙBãb³!ßö
«JÖÅC=xlh$Y6bV1³!?‘ƒå&˜ÎÇÎ_9—¬~jvlÌÈOVl®|Äˆ8ä»O<¨ú.†GWõ‡öÿÆfv¥²—¨b-ÚIDñŠ%%3eÁ°,¹".øØÒ~ÛÊr±¯ ¡0{üÁ²û~eZCZÕ©Å{Õ–
á^7ôØ¯±D£W(ªÜ*u‰½rUZ`êÁU¶S‘†[¦C4äŸpÃs±ãÙÔm¾ùsÔ&a­M¬&ä#}jV*;„ÎgXíw8Ëá“Ş9P˜@Sô;g)¯HÆøÍ6tAwÌŒë.à—fn ‹åQjœ†Ë_A–£õÅ§g±gÈ6!SHİÑú²6İFyÑO@ÁÏO?¥I]ZÂ~³	·TŸØD™°W…qİõ€ƒèC‰¤Õ^Y•QM¿³;6«4l(Ezˆ£i…mXß	›Ff×n™a„°Ö >wHuå¦Ş-½1ï`zU9ã§˜ÑM6¿³Ûö8ø…)HÔÒ0A¶¯84+9•Z¸ĞÆ=²sª`8¼3>€zõmG(6|0ùT§hÿº²<Ùá“¾³š”~adG;Æ™¼‰i(ÆPÚŒ‹±Æ°|C\|@-¹íTæ3¶2sC…á,ÌãK©ófQHxºß3ÒwB¡*àqw’i›b”ğfä½^Ô‰] XÄ›ˆæ¡«i´)ó _÷½Æ”ˆ°¢”ù2R*£‰±<IHC¤E²C,õ-Üˆ†ú÷Ã§l.F5jŒ”ÙÖTäl@Äk*T^TG™Õ¿áü«Ø<'6O
ÚºR‰¨x;§áI=Œ5Æ€yU™nÉKƒ«ZÕqù³…ã±K÷7Ø|ü° hh:=µpØ}]Ióœ*¹”æŠÎÎËzi4mãc²zc„!ÄIÊ4Ï¦bJ¤s)Io‚Umi‹G½YíÃ¹„…Ò©Äß@{2=“Óé’è`jÙÈ¨<X=‘$.›á+3IeĞ-hõuÂíÆ/áÔ¸²Ö.M'ƒ8¤9‹,pd+âˆiÂ•‡«…û%#™äP³ô˜¿†­H+öÉıklüÒî1ˆFú–qzÏª´G2Ô¤Ø‚)]Ø˜Ww¸r0Â'‚§}ò[ËòÎ·¾—d	ns\¦ıGúóÿ‚V(-
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
/Length 5307>> stream
xœí]Ëä:rİ÷WäÚÀèŠâ0tßî;ë1°÷Ï ÆÆŒÿp¨RÊ¢'‡bee•o÷¦;3%’Á`ğÄ»l~ùséåïºâ¿É™.›œÓå?şöåï_Æï—ú‹õ}¾üã?¿üÛ?]ş[>w	òÓx}Ãòò ¹Œÿõ—ë?şñ×/¿üÑ^şú¿/ï‹Ù^Œ†ñuyù¤zı‡üôÛÏ/¿üæ.ùòó/ò¢—š‹]Lfğ—Á^~şíË?÷½õÿrùù__‚|ÿóÏù`HëÜúƒøòA¼}`û—~‡1/ØÛşúH¾}à®/ıñsâB·n0)37a=È°dû‹õR¶¬Éaìúğ4ó!¹KŠO“ö÷œûâÇ½]Ïn=İş`laÆbì¸ùæ’¿ÿbLèÂøÇ]Lô]?îıe¼ğí`|äM¯¼k»‘Æ®ÿ*şƒí]/?wé˜‹á{—c—åín¹°şbz7/Ì^©ºàMCÁe¿^WÜesŒÅ×•k’/¼eÃoWŞîr¶9¯,í‡iŒÁç,k¼}n¦Ïå$åà×;cE*ˆX°Åß§/¼!ç÷öEš†–ËÑ*^åçuN0¯Òûiy®—U”³«p_çUˆÔ
Nñ&ç¦ÙÚ>æÌúd›¡“ùeï‹o¦ã(Ó]ÒÖı ïr¿Z5¤®ÿ>ÍÊ;òñàpºx£óÀD¤º1®K2vŸÎpàÜŠ­ z9xêÅ–ÿ6}á„$!Ç½º¾OI" .c1+WŒ± I²NCÈ>óŞÊ–c|å'Â¥/ä[îÆ‚±âb}²ÇäÅB¯ƒß©Å‰Áì¯#•´*E\.¡J¼fD«¤Ù¼@8dEDşä,ä•òup¸D%J’,¸}±È»pÏÑtùb²Ó<fQ=3”×@Vë˜’„ævÌ%%šP´
éŠ)‚Øj"î•÷!eˆ¤|NŸÀ0MW'xtˆ…À>±˜D8' êô€<§kf%"åqŒª¸óÅu×™$B$a¸PTÎjŠ~õ¦CÜº^G;vãğp•SYÆÀ•÷ùSN!¥*®¦<-£JÉ8o!ëí|'.ß‹HŞâ/˜fĞÉJtWD›~¶ÿLf¨Üå4ê¬
äE4â5x°2Ï|ıuš­,S†(ø|Fgi!Ìz+b':BŞ¹f¬0çw†W¢<HÏh€"•_6\ğJ7yú"Y“ı	ÙÌÛLhC@Cëœ4ØÇ’âíy½œ±`Üz3¶2Ï
I;¬ÚB3 _å:By-‚·Qr¡mCõ(â9¯ÄmiÈAW"Ö©•ßÓôkXaäÃ’†üvhĞŸrZV%ÕK;UËÓÁÃ[Èxå%È¨¥8ÍF~•)¨;ôƒQQ¼Ã3è„œWØ?ğKf=¸NUgëîÈ”ÒìÇ—^ó&¡#v¿|o<|bU¤‚¡µ¬vî«‰Aö+ÔHc´ŠÙïür×$ÅœìuhÓ‹Š.8l ²XĞ‚&á‚À2­Ÿ+Sv|bP˜œÚ16Ğ€w¨µ;JSM,àˆÿzãÏ¸¥â¤ºIiOÉB¥ŠNaÅ’
Şó­áí%to ğ¤òhéŒNğÆ¢wöø‚]ŸòûD“
½M÷m&;“¢}®¥y…à¬ß<=ê-nºØ+fa x×#ïŸªĞĞJcœ)íóH…¨% wøÙÎ¡L7»À—¦C@ó*m¸`/e:à©•¬ÂÀÓÎ÷ÉoÂÌù@eüĞyihmàxy¼gã\Äß²Ñæ¹UØj\"ù}g¢ÑUÊ£3“LÌ¿’+ô÷Åš5Q^bTooÃG‡·ŸórOGTî†,Áğcí¼ëS'ÄÅ^™÷7Ø	´ÚlğÊ™v/;á°É™x"Ëå+×µÛ•ˆ¾#kÏÛ­
"bıUn}Oa»U2DN~'ÔyNvÏ®_5:#h-–ò}ŞÃF—vXï¡<åc·cŞÚ`„¾ˆ³¤3ãà›H×	XËùxİ“Û0wƒLÕ—NÎ_gÚnC·ÑYw†şv„'×$ô
gó0Üø„
ğw|€„€Z‰…*,U*ÇYÈš1fŞï]…æ)\Ç°X>¥u°ex™ÊŒó ë`0à}¬U«£‰Ûy*|yŸ.^úü¬ ]øT~h{}Âô~%l°1 RÎ…k>O¼n-äj¨ÃĞ±Ó*Â»÷M)3E ¿—§íïÇ_?+L«y|ú~†aZµàm¹^_óŒ1q‹Ğ;´B‰,­˜Á Ûü)ôÙnˆ–Îl>`…¼á‰¼Á”w?aÂ <•:°œ‚æN|âô—+X('#Æ* ,Œ´R%Ç,ˆ‚ĞN›
tc(P(Sbšòbã(=Äçññ ³ñ} xP  ŠˆÔIø¹@*ïôïĞP/w+"”3Æaöd`¹ŞÊYáÅhgÂ¢İya4Ò9‡¿ºó)y<²ÛT1Y¨Ó°!['S8Ú¥s¾<ã—®Ü/ÍQõ	èš7Maı*ìØòÚ€i*¥ğ1Mˆ£“@ñ~Ì¬8VR…OPçsJNa”åA-` /ÖL¯_äÎZ™­ãößf5"+ÃOcäáÌB ÉãhK~—i•!³×ØÛ §n£ĞİUÖÌ JiœWe÷òŞ+ì¶{GØ³uU ®#d£Ÿ¬‹¦RPt11ífÅ›·>…ÑùŸ/4¼z‡¯º6Ï‘NHX°ø¹"—Wª-©ÃĞØ9èË[è`Î |Ì‰OWàƒl6r‡Ğf­¬ğ«D”ƒh·áj4he¶¬"ÃH›¬€¥…NMW¥J(‚eÇ­aèü ½ükèÍËÒÃeŒìlôƒ‹®N%VùwÓ_¾ÿÏË“ê‚­Ó³û +ò”‰µ|Å^µ"ˆs¥/<6”Šô+3ñ½¾¢=˜)uAàÀw'íÈ¥C!!
­0‹ÑÁÙ•á“mL4İKÍí‚y*
Û‚Ş©ïóöEÓxV@9E<ş¦CPß>Ù¨eiç
NÇvéfú!gCCğÕèxø_a‡ë@úœ‰¥º·@œ*u¦{Uà ]v®aÁ¬¬Ğu1:§ñüÉÄR 	‚İd-Ô¤•®õ½†Q9ÑRÓåy€ÑöŠ˜@ëÃ›U¨lX6“z>Ò4Ô,µS–xäº7,)û ‚ğ‰'ÕvY}>$L<á³ahUTe0‚d•·´a1÷Š«’¾24ke‰1»zºÊ4:ÎjØåê4ª1]Ön;fäõB^û*¸µ¾‰Ä:À_±z]é¯›¿b›EÅ×¨fX ôÀ¼g•ÓŠ(œv¡ÂG!ÏwsÜE˜=ä×e_#üÖ2¹“>õ:ëdnrÂöl¢4öSÀ§=Ú|Œ~ê”ñí·X!¡…<±¹KîêÎÆu3oF)rÎjZÃŠ`´Á¾¥yozÓ¾V4`å%$\öÜA*¾}ÁPzË‡Ù`×•f!	„§ËNí#Ñ¹ƒ~¢ˆwZîRå*éw7\bĞĞtÅ;¡fÓãYAs%„|‡ªfAÉõÅìÕ%ÏUÚê¢~mcä#D>˜I»Z¹†e™Æ/t!íšòğ|Ny£-È­Á¼U›N±jØv€ÏÃá+|ÕSÊc\æ;»¿i2sf ö éîÍLvThäGEÛ•œäí(´I‹ÇĞ4‚ÿa¯ÕÅô,)
ÚòOÒ›eù(3.U}†«û‘‹ÿŸôm²¯ïY7¡eÚÚ#šóàC qò9c˜Nïçé°;Îùcüdö eEz¾y¾*
\ë>•Ë©V„œVLÒ×‡æã‚ß>| ´Ç©ÈÅâ)¿gO¢ÚyDÁ¥ê¬ôFUÚÌ‰ÿÓ½ú2¾°¢5iƒå9L£‹¸œJÁ=—+Ù3©}Ÿ\@bğµ˜¯ì<ÀkÔ|Ùb¶PŸKÁÎvÅR*Ü[}^õ ÑIJYb„ï?Ì‡Yü‰FKø’áÅ†ëàïøÄ;Ö2nÖgé9}XmĞñá‡ĞvX§ÂeÒ0ï„Ç:Ğ4 Ÿhçïƒâ­"×hÑ5Ä3ËO/O—ö6´`«ïZ¥Î–dÃy*¢Iß^­Å5ÕıS.›%G»n`ï›(ù¡¬VÍÚÂÑ#À„=¾kZ…M‚—³|ú]Ã…oQvyD§
U %M>ÖÍWáAĞ”s7ê~Ã-Ş‚I§í5´‰@µ~ñ|Ñ®ÄJ…U¤Y³‡il×…Q?(/9vy?d‚¼¯ŠòRÅ‘ÃÊÍ!ØùM2ZØk:¨Æ!¬³¡àñ=ÂÑ_NjÑı\rùÄ#ÔÇêV©LtÌ¹œ2ÕåúÙÃzù*r·K×“S¹Ú÷Ó8n;kGÌ=(ªc~ã]3í¬‹İ~Ô· ëƒ r÷&@‹/‹ã€ÑˆNæs
8tí>¾Ì·nÒ´‚^q½Ói{íl%Ê7ª³'?Mœ6£´çgEW!inßÆu*ª¦dŠ¦Zƒ2ÿJTüßF‰,™û»òî‘†5SèÜÆ†Jad„Æ´"÷G›ÁÑ ˆ'P*u	ù3¥b<ZäZUÀŠf%M1i¡Ê#:ŠöjTøĞ<#ĞÕcš%Ğ7ì–ÇW.‡6‹)6Ì¹å®*µ[³}£]ÑåÑ[Èóş¼kˆ·ğ)'ÈÙÑ0¡;T¹>[¹‡tujØôıÍÎz·Ï48åİ^Ù‚è¢€áß|Æ=<îû¨Ôû#ƒLÅ-Şğ¶n†|é¼ˆ–‘6Ï{Şp}K£i9Íƒn:ÇœvñâĞ†Q˜|Àñ#úZ7lÚØ*Eºiç(Ş­>ôí£—+2µÚÕC©©Éø]Ù	áR~åyæít”“õìt},yôË×N 1Õ)Sfêû2l»]è\…)Ó+°aŒµùÙ-m€l˜XÃŸ¨òß0 ¹%„?Å£[ßå¢6+€¸¿£è‡¢Ë˜—–YKgÜ'ÑÜÜ'‹D?h"TWFI'ŒùUdã?(Ÿ†AŞÈqt(ÑïÆ]“]0m*³jøâp;2W|ox¢¸RVªÖV$«lYª°î•ÛOÕµÒª(öËçVÒ†ùŠB¼|f†ª6éÅ7t{´Lùù$I7-{4<gÒMÍ
yÇà»:èXâa°ê àŠ(jE¹šñêš´Øv™&|Ø–íªl d¥ûĞ6¿@6ŸkœÜ¥m&§Óé˜VŞUÂ7ß¦»éêñ9óßQB/qÅñâ¼a®EEæ¼ªéÁépl‡æsI!Ñ°¤
^9]§‡Ï®æ;¨.³s';-b‰›g;µh§ÛP³ø$ †Ú7,ô¬²fúYCñ}ƒÁŸÑü_|ß¯Õ&ïkÙIé-o_á–Ÿ+Ú
ˆIí(<—^qí¶Óæë{y‘Úøêƒ@]ÙäÓ_³•ç9/å¹¬.†˜³ë)¥Îôc#ÌMw2ßY3ä¸±vË«lHÙšW]aL­Èè!l¨.ëKıÎnú.‘«ÛúŠ®K"/Ò°!îÎğğ]»ï­Åˆ˜ñ™”³/‹:}¿1c+U·aà9ã—ı@“†ëœxeoÎWi–;7ú&SĞì$À$7Œ±íj:eñ}Úpfºu7æ¬9[!x»sì¢P©ô„øi-ÁúàË>¬Ãü…dÌMÂµÌÆ¸PÎøv²cÌ}¿ÑºrgœK!lêÂnÇ¾5¸5BFSÌin3k]iéÉNäMİ¸aä¬qÚ™!nı™;‹û±?€ŸáÕ À ¸Åy¹[ÜÖ‡¬*¢Şôû¢‘ñ>G™GálÓcùÎa_¿¹wh^O¶Á¸Í•Ÿ;ïmreìê\mHnJgãFhÊ··Ò8ÄäÊ~Ä3‘³uCÚ¶
Éà¤ØÇìÎ9ÈVn	·Q£¶Ó½íKúmŠårƒç¾Ü™Ô÷iç]îC6Í$÷¬;n*wíÌö;"Õßôc¤q›Vï¸Oh¶ß_wÜ˜aç€®Ù.’J+’…(]çPœtX¡Àâ|—„0B¾×k˜W4®t™9S­¹bd¶·Çƒßhcs?ø­W’ƒ·bŞ‡”6Š›^2óC£ëî$9ãfúÄ*7Ï&¦wgV¿Í4¡W]a±ü„öœ =áí´#b7Ó=ØWÚ¸µ˜„œxÇB—R+Ÿ×`›âÆ³½ò›`zÁ5¶§×ö²î—ŞÊ°gJÂYk¸&ò2•rn¶^dù
6¹i§rr°;ºº¨5¢£m(èE–ÊnGs]('¿#ê²àÛ¼¦“`å(ƒ»âZÁÎDÏšX@¾‹m,TXªá¤ğØPäÆRãÕ’WwLÁQÛóyFt×
˜o…¦í|›÷ƒhÑ0°L¾CFŞ*K4±şÂWcØ¨;…QoBÒ°ÄOÃ¼Fv—°1“hgˆkgãäëy´ŒËD\ûFIIåå½‹d—ŒGÄ¾E-¼ó›‘°aÚOŠ¬¿z›³:wòVß–¨&ã[ß™Ñ`ç7:îÎ
a6ºÌ®A?/}t´ÙÒD^~‘ã#íl­YáĞåA.Z¬T4ª…q¿) U˜;ŠÚ<Ãö1îûÌu‚nK¶BÓ‚ÜpUûyş³°!Ìx7dÙãŒ]x®š;êKwÿó{jÕ0V|fµ
ÏÊ ºòŠœR†€~vãü(\íN$Ä´kBİî[kFÒî­şy oíÌj¶şA~_’vÆ^¤…ß9,›Ù~ß§Ó#–_µk´Û7©²™î÷b¿ÃVQÚá(´r@©WøOò÷ÿ w
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
xœí][¯$¹m~?¿¢Ÿ¸\ºK@ÀŞ™õsâòÖ±ƒ`Æ€ÿ„,]HIÅÓ¥>=gf7³ëKŸ¯.¢HŠ¤(Jµi“n;üû»ı­Ú’J)Ş~ùòò¼®mÜoÆíéöÏÿzùÏ¹ıp»)·†ü†ş/xPİğßÿøÓ-ÿøçß^~ÿ'sûÛÿïÉÜ”Ò_÷×ÙñÖünıã§—ßÿloéöé¯ğ¢ƒBu3aQiwÓæöéËË¿î»qÿvûô?/®úË GÀ@8€Ğ ³@”ß¡Ô˜¸üHj€Í/ıøéœpàÛ¦UŒråÇFôĞÈ|ÇØ•ù‘‘ÊŒ€p‡D¹öãÑâÍig7ïf¤n$w¿Ó6(#k;Œ”7ÿ;üû¥üæñ{SÁmğz›nZ;Ğ[­ÜæáM¤»fC=Â†ò/öğïàN¿i›Ü}-Ö ÷6…=«ñ–¼Šÿ/<7ƒğ½o ÆÔ—ú[¥ÛgümqF"Põ¯{cÊ˜±É"æÓ®ë}»5úö>UPşxŒã#Ş™ŒšYïÍM+ìZ›‚Á„+¼šŸõøÌqc0Ä”±¨| †­Å”1Óñ°Fº\(w½ïúmˆCİ/¿~yñ)Ô?>ã›1Ê¶;ğn7‰½±ä¼]Ã>ÅM{,i$"æüÃº‚Xğ!ø®Ï>%Ğ­,ãb*êÈxˆÙ“O·µÆ;Íär` ?Ëä‡Xp~¨Hşó¿;îÈwão¸`»ö.ÄòªBhTn¼?€t×sÀàg,|«<ŠºqV¯öÓC"²ğšx rÍË1Ôá,dø%®Mııù…«F½™«P})W6j«e%”ioé×rê7•A|ÔTFòñEç#±Ê†Ø*Cİ¿¼ü7Ú…xËÿAsP–$¦ä‡5øa~XƒÿÖàÏQB‰4ò’µÍ<„{ób˜Ìb£y@xØ[‡ıhBr¾!†¿;ë¢Ãg<·ˆÁĞK\`ˆÍÖÑÑ:Øaò¯bòuÈS¿ö:¦¨¬a¦ÒD¦ù­+lŒ°>³ÑÔ¸Cƒ®ñNb6ÆM*l¸7é{€âmÆåŞ †Ä€	Š70ÁtÆ!Y‡<Ü8 <àıF~úŞ6$ë7Œ»¹q@^m9Ï"LoÃ5ã€UãwÆ¡İÌ4¨½”ékie#””·õ‡i9ë9‡Ê!6h#Ùèbgã°É†×&CÛ+¡Â[ğÃü°¿m[ğç“¬X	l‰»¼ºtÉÿ	¶fÆRÎjmÎ™äœ¢TUÎn…-j±°£%ß´¹ºš4]ø)çm6gUJš.8UÚØK½É–&Ì’jLøà°I‰µíLy“¶@”¢äœËù*·YèQğ–.èú„K‰áö•¦¤ ¿ğ&‘Ú’åS MWy¸ŞˆÌ©ƒA`•Ø„uÒëİX—¬¬UUµ…Æu¼ (I?M¬wÃÔnx˜¹yÍRÁ?jÁ¥Ø…Px†!Ç¨úci€‡‰ÛÎûgS8#×î{d¬úX©ÚPu¡kjéÂşsiÜ‚œü×¡ªSÄ´¬=w«<àı ÓÂ`Œ\‘í×ôª{•hJDfÉG”Ôúºe—{ÈµÁi¶Rµ!jxB›q×4‘[ğxA«.¹'.¿uUhz¢zŠÃLîÅ³(÷B¤éCU(0aÉ2i§r!á—¤-iÚÃı®ËIçRò%@ıëGÉËˆ¡H<w?K=€¾àE×™äë’åaœãê› .õ»¹ßíå^ˆ|’<¥ø"Atr"¶ vNÀr«Á°,ÔåÈH5ÄÆE-–ğŞè[®ÅÈÜ…˜Şğª7xigvè<9:ˆ«¯ÒuŸ’c¶B_/+®8½İ¡ä‰×£ÎN²]Ô)IVûúÖs•$+{JÉ·>^±IC×³^©}S
8çïóWÖêK³È.hZi$u(î¬ºvSjó*×+.^™êâMà^|µÙOŒ“qn|P«À€=ÙÃªÜ•Şµ!SS5Nj‚İygrëiS»ò)Mc:ƒ*
ºùåÅÆíè?€M{¸„˜MºÜ´9H´­ìĞèÛ/øl°^{\å
Äûü® ÌˆÖŞ f•ÕJe~—gáª?–w…§<Ş¹«İÄ1x¼Íƒ3.f¨À, NïF§Œ&$: ñ V;n7| 3£6DÃ¯1`¤={&Z­7ªoÌm)Bh¢8YÀ„`pù–‘¬Š.D×wÔmi§8K€ÑÎ`èÒç6å´¶ªg°ƒA
Ò$Çå”ÿ8nÄ_ûxĞAOYì£îßo±—¥gD‡Á^º[G¯Á^ê¾gæøŸ&€Fƒ©¾u¼2øvÛsÕ *K¤qß Á‡@HH¦HÏdq“lñ“~}–ë	5Â5ª’Ã5¯’Íu”:Èµ¹²‚ë|eÄ\>Šªøh«âJUŠ¸s>ƒğh^€Îb^–C†kåZÎKœ\q,}ì³œà}f *Å.2d9•¦R¯EşíYzvsC£: ƒ(aõìÃ,ïâ+:ısaY\Éz\ØRä_uV¹^÷Ÿ¸ÃÑÜù7 &ÿ†Xïß™ı›Fµîü"£Clöoˆş±Ñ¿!6û7Dÿv@Õ¿AØÑû7ºÚ,l{YbŞÙl"‹l;‘O^€w”ü±„üJeùÎ`òTUË)ÿQü›†hrôoˆA]ÿşıÄ¿ã&ÿ†Øèß›ı¢£Clôoˆ©\bÅ¸ ì¸C9ØSïßò’~~¶óo¹‘Ñ¿9LóÙLGY™67V0o,ã£c?ño$>ÚvòoYŠ¯û7­jÅµñe€[ä 4Çä©qŠ°<a\_zûáİŞèİVÌjvNNÂ‰"[¥Å*ÙE×|$ ÖÀYÕ,Ğ`¾¼Ä2Œô mP·X†[ÁĞ@ †‹t68ÌbÂÇ°>Ş‡İdà0Ñ1[„ŒS³åp6£‡ÑÙÂø˜±Ã9Äb‹2„àÃÅhİM,f­Bè”SeÑèÅlCâW³Ñtš½$[WúÖ;ì’åd{í8ùÌ²³f`gHñŠ¸–}Š	=w‹÷1\öD^.KàW}6Šİ[|6]{¾šÙ®£×­D?ö\E×SWM|Ç—AÇ;—FÇeWİK'—Q'6Wäé²´ñÓ‡ú,Sj„kX%‡kb%›4–ºÇ»òkå'ÄY>¢ªâ‰¬R•$Ç¼Z
£vtd ı²Ô#{“å4¿œ—CÄÖ—×1ºônÆ)ÙÜåõœŸøªå'˜ÿN§Új/SEaª˜.È\WfÁ…P:R62bpˆ•NÔxKè=\ŸÀŠ‹ÎŸ/­û=ŞÏ,ØâÛ+Ùî+Ä°Z"q½kÃE¦¢Òš¸L•TKÁG9·=òúÊµ8úRÕ‹¸2peiZSµq¥’c¯*¼
ğ99{e¦ .°,/¶½³úäèIŸ‰&Ç-|ZØßğ	`4géˆq†ô Sz°“ô ğ”éÒ#€ëúi/`'éŒ®†ôH¸Jz$º!=Ò®Ò½¾ƒMäYclÊßÈb©F>ÀXGYº¡±„¥%
ãXú‚1˜%:š(—Uş£&H¢$¸‡iX @ú©†IT9Xê(V9¨êú¦Î$€âS]‚·1ÁÛ{¾ªy Áq °"?5$HLşjN°F¸NUr¸îU²¹–ª³Ic×úÊ2>>ˆ¹|$éi€Ä•ªï$H %®¬fw·é(A¿•\+
íÂ®g%©ËÎÿ“ğrT f/–}¼<Ã¯a¨÷À–8Y[ëLízbãW%Vÿ<±&)Î].Ü’X¯+oî’§gĞÖué ¦ôbcz±9=cô~˜'– A­Mw™4ˆn‡MŸ;ÜÍ³*~ŒMÈ4T4¦ÎşëLŸ®RF ½„R¼5J2Y”Œ òÉ³ğR‚ƒB‰â¥L8‡)¹B²°'2s·²»»§b‡ùîÚ‹')£Â”¢AlLÑ ¿mŸ¢AtLÑ 6¦h›S4ˆ)À²DUèS4ùiD{–T‡5Ât¬‘Ãt±‘İt–uT»ñ€Æ/>VâIŠ†dOd•ª$¯¥hL;çÉXû·ºØ ÖB>P(>ùq³ËòªÅk@ïU&/Æ•K L“ÄÆÉbÁ;ÛO^ŒóÙš°p±Ãê°À±yú‚è¸º‹Ø¸º‹Ø<}At˜¾P¾7T/ÑÕ>·wP˜Í£€œÈ¢ÀÈgÆÉU/KhÒ@¬£ég2MDHË+ÿQ&0ÆÍLˆÄæ^ãæ
&ÄÆ^Äæ	¢ã±qƒØ4ApœÀ V$8T0åLæ
&Ş×*3M`ˆl®§gLÄ
®ùsg.Ms‰+U)¾>»1N`¦¼ÑòæC1û}w7ß.Ë+mòOW\Á÷¸ÿïÛ& Å<óºO{‡­¢’¼aÃ°OCÑ‚¨Vëıû^v+wEÕûéL)©a¦”JUéÒQôÃc¿¤ÎæII÷ËØôËØˆœÌ’’–±–±:™%%=Í’’f³¤cw?¶ÛU”×—°èµÆâüF›4ò™ûbesŒÆ6)\csÆ]6»)R°'²rY’ı)íó)íó)íg3¤XªŠ8õ±Tñ~Æt²ˆè4CŠi!ÅVˆÅ…K%ZLYš13¤ãiC{–Ô†5Âô«‘Ãô°‘İô•uÔºñé~ã%ûÙ©É È*UI^œ!%w×W¯WÖ9–æ€X^9|¤Hl9¸­§¸ä˜j}~±$Kt?r0°Nì:CÄyiS˜+xu¿b½üáÍ‰Ë*õ´õ`¹o;Ê¥;ë@Üˆ'nSãiä7®ÈŠ›ÑÄC)·yNŞ›(ˆƒ6©ñÌ*ÓG` L¹jÄÆ\5bsnkÌU#Ôçªÿš>
CtŒÂ¢0„æbBD‡(ì€jf•ë£0ºJ¿½„"ŞÅDÅD>E'¼£ÇC(Ş!¾QdÄ9L1ÉÂÈÌe‰v‘˜UzŠÄ#1ÄæHÌ*5åªsÕˆÍ‘¢Gæ¡ã^Ybíø¬NrÕˆ¹jÀŠDU‰åL#Ô˜«æp«äp]¬d“Îª9#>ğ ¦\5ç,UzŠÄHV©JòZ$fU]ö½¸«¶UşP‰£›“Lq¯[ñÌÕ¿¯uxÑWYĞÔuî4m/l™Z^–y.œšq§G@õÇíÈ¶eÛL-përpÉ˜©TL²z:}#n
â†À.å­ñMù3Ü!‚µ´nªÅfbJÎLª¦"†¨ÙÇ|¥YĞu5•µA3(?‡‚`Í”NL©Jl5ã±¶€.§ı¨†ñ8¡ù¤ØîÕ£^l;êE®b”ÖºÍİ¤å9˜4?Z/<^­ıCuõá\›ß£iÉ¨©ĞF­|Ÿb¾`ë¾ûˆ‡8Í"5Ê IJ=ï§Ú„õeí{-Oä–“•Lİ—'Ü’¼W0³ú‰Ûß_Öo%1œŠ;ğ3>_8êóıÏÉ¯°EÜ ?}qÀq@'ü¹)ÿ Q	0# …¡Ü®Ş»í¶‹ÈcÜ`&`[
"	`ğA@ñÛñ*ÎuŒç•&n¬»@ô»cm†ˆÙSO–6ûsİ® BÜe¶Zg;°2æxA…?÷(ĞğÈTj*U¿~Â¨Šèg|Š¹¯•ş´ÆtÔ¶F Ôíx:ñ¤`îàtc`CQ€×íy&“Ö£ˆIºÑÎT¢õñL§0úC}Ó;~¿ÏñUá(P<ô¡ŞîMß8lĞ´ã!°;èsT	ee<a^C3àoª›1[^Âa1š5¨mFÃ›\Àƒğ`y[	LS·¢|ªêÖ`T·€}·İ+t°àŞö¾1cèCß8]: íRºëX ì­ã-Xà|9¯pcâçö‚AaÍ±«§µ„§%B+Mx2VğçWVòfeÕ¡m­Ÿ!­#E%Ã#ÿ
«éù&j†„Ç	"97Ê¹îÔèSÕµ…¯m¦
ùğTa<¼G†CÕ	Yü€ƒke6ıºMĞ´z@0Òh×ÕmsGĞmñ¿ëG¹æ&`œÛm7k&†ï¢×-Ztjè"1ÎÀ¸2ÿ„X¼/fbğÿw‹Ï7¢.°@ &İõ³[Œ²æ“¤§,Ğ=™Ø=eòd‹›º{¾3Xü»1­œ_?èx}‡še-¯ê?ñ¤½oy²õó¨[¯ÖX>Êò~°x¹ºì»,Êø†yNzNš;^Ê—/ŸF{§fà­xÛ©Ï­»ïgdë‡ÅÊÙıå™er/­³&©ö)^zÕòy×â±İç‚z`‰dùUşÄË—ÏOıÎ&Ÿ¹.m¬¾ôDIù”Â]o‡Â]oçÂ]ÄÆÂ]oÏôv<t‘±l±²TÃ
'…§"/ÛE^cx)&be™ˆm":”íP-Ûõv(Û¥«­h´½ƒŠKycT†JdQ¹*‘Oë4¼£TK,¡RÙÊ8*©å¦â[…ã²Ê”¢]oç¢]ÄÆc™›‹v½5Ó®CÄÆ]‡ˆÍE»ˆÇ2!6Ë„ØT´‹àX´X‘ßP´›/0ùÏE»¼®Só±ƒD6×Ò³¢]b×z3í:äÌå#ÉNÇ2‘¸R•âëE»X–#1š}Å›‹ÛÜ—‹Ö«tÖ‹WŸ–KKCO<ŸAŞNwgßÅõtúúLh¹{¹´æş„çò©÷O<ìyóÕwı†FÆ¸\u²|)ÎíNŸXT®q÷Z\.'ºÒúÍ¯—üHÕ±¿XÓ$Eòrãw¾„GB§şuÛ´0ÛG{>Lp"ÖÀ‰ÈI¬çãëù80Ø¼EÑq‹bã-Äæ-Zˆ±,ÖóiˆõÚUŠ5ê;XLÂcÑK#‹E9|±²È©±„EX…q,cf1[„ãrÊÔHÏû9Òó~Ú…Ø|¾„÷nô¼›#=ïêÖÑnô¼›#=ïæ8àÄeÜ7DzÇ&ıú,×j„k”›#½F6×Qê ×f7Gze|tsù(òÓö,WªR¼é…znÙ÷QlûÕ¾Ê"÷BÊ™¾Ç!YOÜ9%††ë¡Â¿Ú¸~‚|´Æ{„ÑË»³ß#¦{àë…_å|À!~Y?>kı,b¸µÆKŸ†{cuş×Ê7ŞQ+x–ÈÙéHšW«ÔÂÆÏ	8…ÓBVŒö}~uİ}Ã¥¢gZ\q‰óñs£¯ï–Ùó>ªuß|ş*vl¿Ã±ß×¾x²Zƒç~õì=>ÑùÌåÙg‰SüĞãİ	ñõ/¶./Ÿ‰<¹8ÉLŸ¬ãbZJBe€Ÿ‹±Ÿ±4ù-—åĞB\g\_¸[ÿ¯ôéÒkÇu±Å¥°8°dÜ)q_ŞrÄ#fqeòî'X…%ı9 ]€ëmÈln¯Äaº­¯|/ÃOC&ûgß4ı{b¤°|ù×ro:Z”ÆUn‹ÕBâıËÇ‚=o»xúô²nŞÙG€Å!F}Û|Ôö¶Ys}ç¶O:t½kE‘hà÷ViŠ•§XæŠU¦Xuj?f«RÕ‡lÇ(ù¿1_Ş•©¶¼«T«â½ÇsXİúsnß…÷),­ÅRÛ'ìĞ	ŸÇı ´VÏOµî€‚7Â¤T.’+ÃªçS[4{ìö> ºo^í|ïÃaOÙÖÂøÎBùÆBiß µC;8E´h§=ÔÇkõümœûÜ£0Òû=€E šS>rS£ó=€â"İr5ÛóP±~Ï¡|Ï=ÏdÑÚaRc1ù6Ú™´>éÑ¼çîˆUÇjY?CC%F®µRxÀ<ŒTìw+šÌ‚F›ˆ[u=€´G¶ß0}şl£i*V1¾ÛP¾Ù=ß6°vÚ¶‚ ¶ÿ€‘Şö)°.¶Ä¾ÏÇ÷9è¤Õfğ˜ÖNÒØ¹ØQ”4È¼T·ÑP,[?Ô©õ1éˆ¥ã|£a|£¡|£{¾‰‚š!™q‚HºD:Ó˜ÖÅ-úf;"“wÙé@áN‡ıÃ“v,(•½¡oâŞ–¿ßÜ¹ÿ`•UïÄªÖPcÕÓØuô›Ş—OÆ£QÉºÄ.¿¿»ZC»Æ2`ÁÜÒ]Æa¹L
BÿØ%Æ…ôNŒkMŒ{ó€Qİåº›ñ±K¼jŞ‡w­¡SŞ=œÔä]z…éšĞ?u…I…÷a 5$2ğiLnTÁš½ËÄ°w÷¿ç†6|øĞ•!%üøP†„X_†„Hğ6õeH)ŒºAd,CBl.CBtüĞbã‡n›ËÊ¨–!¥0|è†®¶B˜ö*˜áQi‘E%8D>ëğRY±„Ê*ã¨Lˆ3˜
Šª —Sş£”!¥0æ±±à1ìe_†”‚šN‰Fl<%±¹àÑ±	±±	±©àÁ±à°"½á37ù“şü™Ş×(5•!Ù\GÏ>sC¬à:¯¦S¢9sù(ÒSÁ9‰+U)¾^†”B3Ë‡Úß©k½~¬ÊúöäÌÙjZKÌ¬Šu'«©ÊßÆhäLóòaároª-¹rîÎWŞÕäğo¢×¬İ]*ÿãKtòê’¸ş)®A^ªeèV—Ş¯Ä¨nãbq1¥y›bã6=ÄæÒmxÅ3%?ÇLéìëˆ¥Ûˆ¥ÛˆÍÛôc¦Ä¶é¥4lÓ£«äµÓ´M7Æâ€4]ƒÈg‘E:ûº±„Å*iÜ¦ÇÌ¢ŸÄ¶é‘¬ò5jJó6=Ä¦¨)mÓƒ7o#6o#v5¥y›bSÔ”N¶é!8EMÉùÛôò&ÿy›^iÄQSš¿­Ads-=Û¦G¬àZ?oÓ+ÌŠ·I|Ä±mzYŠw¢¦Ô²Wƒ]/O].6} êë[~Ùã=>´ô+ŠŸYÙ¼|.É¥ O<Oşö>ñ›"ëå.”‰•LËÇ5ÈUFËE{ßey¸H­Ö]Öìì W³·…ı±êZğ0òç/sŸœ¬ZõÚûÉÎÁ³SO•¨ÒU€Öâ‰)“ÉÅõ>3ë¹¢ïä Yá”Öb(Óf<Œ@©‘àõ#_Å“hK4Í§Ó<ÎOx/«[úR²ŸÿLá¡
endstream
endobj
19 0 obj
<</Filter /FlateDecode
/Length 5369>> stream
xœí][¯ä6r~?¿BÏVËû¬gì}Nv€ü '»A0^`7ÿH¯EQuZìÑŒíAŸñ1Ô_‹dİX¬*Q<»Ò1ılşıa'ƒ‘{”1†íç_Şşñ†ß+Ä¦­ˆÛ?ÿûí?ÿeû;àf—nõ¹‡ñ4”şû?oùâŸ{ûãŸõö·ÿKıù¨7)•Âîşš·æ¸õ‡OoüÉlqûôWè(Q(7íw¤²›ÒÛ§_ŞşUmÿmûô¿o¾ÿô_ *s||´H@àû2º67‰0¹Ó?rÛ•P.İqud¾ãÈÊÜä(© sG¹
f ñBôûlª(ÈÍB©;’+ŒÆ8M(oÄü;üûÇ›”nwøc6‰’V,VI»;è£[­ŞÑ‚pˆ|Ešı!/wTÓCóU`ğ&z‘íwz¢ÿ‡v3}(±ÛM0ü_ÊµRaûŒ×g_@ÀAAmø½ÓFËŒi%b.
UïFo?cã ½t©7·{íŞ#Ì–çô¦$Lr¥tÁà"bc‰ßæ¶Û8¼ÑkêÉX.‚8q0bÆl¬,ëË@.
É7>m¾\ıüæ¢¯>ã‡]kiÚ8+t$İ!­s~ØÅ°+§¢!$"f5üVóÎÃåÙÅ¸Ã<—†H1T 2DH‹è"6‚F;«ˆVÚ3D{ˆõæFEïŸßÈİ¨e½ôŠAÒá!ØÒU¦Ó(2ğa1å!¸tEjEBF™çĞF$‰tm¨Ì"2çM;ˆ¹Ñ`‚Ğ€“ŠñR«t½şüF£İL¨öI,Nl²‘ÙM·qClœğİ'C•™2MŒdny“YØ4CfkÓ`ŸÙ?¿ıú„°åÿĞÔëäE@OàF^àå	^àû÷YˆJ„‘;°¡»«äè,’xpˆ]bÂ Kƒo°2¢]kâJ*7Ä&ß`e˜|bGß€˜1¾Q WQß°äòUñùÃà2D¬¯uGì”L,º‘H,¿±Bæá™L¦&>çšÉä$Ò&Ó¸é…L÷¦¿âPÁÍ9 æç Àäsğı0~HÆªç`C²jKbV+?pÒ,Ñ£w°!Í'K½bĞ·¤Î¼¢ï æğSõùzğífjBaòdpj••Lb¼•jåo2ª€è¬©‚¤ó«KœÎÄª:cÃàPÇ+ÂË¼¼ÁË|ïŞàé`Á[×ÜƒÓ‡<Âé9@L›)ùˆÁÚÑ=8íî¡£{@lr¶cMİb0÷<Ub³{@ôè–ÜC¾*î!ÜC†ˆùµîˆ¡’‰I7‰é7VÈ$!<“éÔ¤Óg]“!™DÚd"7½	ßôW<*¸¹Ôüà ˜ÜbÇL±É=xë§L1‚¢œ#—atŞlD½BĞµ£BGlöˆš,£¦Ã„5÷€Ÿª{È×ƒ{h7jc#Ã³l„vë­ì+'|÷éĞDfM$™_Dâd&6İÛtØg÷J°ğò/oğòß»7x:Xˆ&6÷¤İCrrˆ%±©è¤8z„Ş±É;'ï€ØÑ; 6{DŞ!aÉ;ä«âò‡Á;dˆ˜_én(:¦§¢c!qH%+dÉljÒé“®ÉÌÎ,ìc*QÔ2¤M}Å! ~›w@ÅŞ ¤Ş1W=1‚¼C´bJ%;Tš«ÑÊ©êˆØ±êˆØì=z‡„5ï€ŸªwÈ×ƒwh7jc#Ã³l„vëmü3'œ÷ùP%DfM$™^Dâd"6İ	ÛtØ'÷J¬ğr/gğrß¹3x6T0Ò·²£qô LŞ!a‡²cÂ¦²# G÷ ƒ{HØÑ=&÷°ƒ{HØäzpC÷P®²{(¨{(P·¿Ş]·T:p·éNb·ıÎJŸ%”ç>ºtÚ¬ë2ìÓ“J»Oä®—>á»ş²GH
®î!iºî!a‡²cÂîÀT-SÄ=$ìPvLØä 5‡L"A‡L"aHÄàŠä÷°ÔËäÊ5õ"ÆÓº#fF&ÙHìv[!öM8î¡‰†Ì—&B2³ˆ¬ÉlZ!sµi¯Ïë…(áå^~àå¾c?ğ—“=¸%H{3íš6gŠMKQw³ªóÚİJA1}§¬*_(£3Ç´dg!ä±²o¥Í»oı ‰×¶7‘¥+¡mtÏû@qŸ§Şö/Œ)=iá£}kK†á	UìØu/+hKÇH¾0™q·GŒëÇŒ³c(CX#cõ¶eğ®´PáãlW¬Ô9r1>—•zÙ#C®ô[°ƒÛE$9Wh~*]"‘ßVT_qÁB¼`ëšü’½…p.Û@¾¸(*üƒFÚä˜Û<}0Ä /L(~pNV,¬j!ZOŒá#C/^:Í£¸¢AVˆ\Vˆ¼¬3;8ß‚eĞ0TN4Êv5øiOô±®Z–*Q}Œ»øU¨º¸n†+SêF¹_s&Ã<øŞäF­åÖwUÎã¡ö²
·FËëXÇÎ†Lœô«.ulØ3xJíŸ*!°2WLŸËëì•µã°2sêàCÖî|=6æÇàLzYå¼DX—{iÑ¼’,<a
Ë‘#:õ¸ÅµÉiYş&ë°Ë×?8'«ú.æõEV×¨nÊM×ÉåÂ$~™[×àa+Ë »ø.GÀìl¸Çìë²Z¦ù®nœË1Ïâ}!Úzâñ„HXÍ¹u“wqÔ…;qE…7†Æ¬3a×s!Ô„ˆ¨¼fıCºÛìö¸ÜüPñ‘,‡”lW|´°x°ŸøÀ0xx}Üåô¥ÁØ¨´Üû²máĞhXsÂ…ªà÷R½1eÂ|¾§K+Ñ—•ßØ84raEÈe1LğØ”$øubÓRc—Œ=>Î“ÖSv¢±õõKÙ¼`W“YŞ VØâFg¥ıuQ¶0Ã¼µ:­ÔÚKË8W´ÄÆi‹õ²Ô¥©·"F/$CC‰Ûi÷X$OäUëØ¥Ùt¥èö7>HY!o#ë´åàOëÁÖús…Çù$ú…!&ï~!á¯D“Ïú…÷cCKàr­Fq<À˜)_¨bñ…½KNäR]èFªØ…F6Áî>µí·ôíÆ†¼3fë!UÒé@‰Z
VĞ§ÁoDµ"i(~ÔÚ¦x7ˆøx‚	<ù	_S„Ï3CÆÒŸÄ„BÊ}ƒ^7÷o>æÏØGíÛ¥ö2·Áïk;‰˜n–|ıh¥íïo2¨]Eé@JåS”~! +wn˜#˜¿rCRÜ€˜ÚhºÁ6•Â½"Rî P‹[Y`ÙÛµQ¸û÷Õ–%!Òçb¼ËĞæqÜ‚àÆŸhvŞ¢b¸Á#ÂB#}¿œÂ’şÃó»D(Q ¨İ@š@h7İà7Še¤¶kÂú<‚z½õQ$e"¼” ™Î2‰¸İ#qXh—xøˆ•&mO©,@¢&àF×*‹Ú$Ú*´¢¶ªlIó®2P××@TW-a Û aõÄ‚pk
—x¼œÃ¯ +ÆÕAgD1.‚iônNàŞ™gƒ¢ğM.•¦à¦C0.­AfÉ¥½3a÷H¶Ó
º±¡‚”ÁŸ+Ü¥A÷ø®°®¦•”»‹Å²2„†…ûl‚0­™ÂDQ}+ïÀpĞ®(Ê£ß—Š’òe)[óıÔ¶`MNŸßzc ñÍõlçu©Àìœ×Æ‚ 6¸ÏÜk¡]¢,µ¾u%
S™˜ìªJ"ƒ‰¦&°ŠIMª´q•>¥éi¤¨©”RO¤ñ9[N5ªëgÁaè,7à3y\èçÃN)9­ÉrªV şT‡•|n’–‘,ÚZ?h•ƒu­œóB€:}óSù,û‘¾ûq^ÎŠÃ+Üj¦À“P*.#¯J(5“5ØÉ+"ş^,i}‰F~‚íT\#ÚzVBAT“ş‡ûÑ´G¤E9ïJ±p‰ X‹Êcr]b]¥‰Ä=˜uÌ°²á]m äZ=
€ŠšR0*³]İ-x»CŠèš±àj?<2†à÷#‡Mò»µ ìK;IXHÏã)JŠíOW„rª©,X­rt‹‚LB;™í;ÙV,İJÔZ_ÇòdşTë¤<Yú²Tt_åPĞqK¬’SÜo\s½[IWc,4%©¸:mœBAíB4¤æôN›œ=Ã²ëL´¤^R’?XI¥Š~:uÕìÁŠIÌ>–BÑÍ=NçûªTiq±›*}'}Õ8Ä7AÄ¹â‹Rˆš²ÈbkÂ¬¯^¾”jíîA]^N¹òYm~YÂõ‘„	ã¯©—5	ñà1‘ÁCèb]*äƒ»Óyƒıî÷Ÿx°½8A{Ñ²r%#peİ‘ßÛ·«^«)/ï›~â)[á¶Ñ°UùåRÿ0é¾mì|iuY†Ol|¿ÏHØ7Ë;x‰¥… ssñŠ—÷’=!Üõ'wî–£´Ü3¥k[Vèó‚h&ïüëÏÖ½üIİKÚZ 5«ân•ÁBM¯@:aîİ)VAÊªÅ¡ò0 …Ò¤ô… ©{¥´è• ZñJ )õNIy‰@JQVR³êLQ°ÕH:æÏ*^>—<-xùR/¢ù\ZRc¹Ëç*ÔPíò¹\i±ËŸ»üY±«µ&bo£zˆ.åDéÃ‹9©s¹“:—„5t?Ô¹ ƒ~Aq’º ”»±–Ğ
ŠÅÆ•(‡ÛÕb‹5¤#†Z€ytR¼©­w5V¼zã^7"ƒôÓ@O¯GÚ{åŠpÙk\ECİËÕ½\©Ñ²—Ï…#K)ò¹Æ4Ö¼|®F9Zòò¹jiÅËŸT¼üIÅ«·m:èCtmZº^;ÑÔR*s³õ<QëºÌ>®wY;<ÿ$³+Ùœ®eÈÏGL»ïAò>¥Uú0=2ı‰ßI¤ídûCc)ç4Ò&wA¤İ{yEÚ¯HûÂØÜf^†7¾?°ş<¸!€X'	U±ğ4ûC®¿cÂ*œau›ûúìµ÷/†ì>ÒÕ7¢¬šŞ.}2.†%23ÄÅ¡­Ó$F
ÑîÒD‡¿·]!*ˆ¬£âñmz+iPb~4FÂ½
Áq‡ ¹‚$Ğlc”PC‚×F7	r+{Ô¢ª6}APŒDÈ€Ğ®¦O„!HÁc§2 @¸KALå/a9N«rhHävô1ºª(5]©î®ûÎß‰åÌñ±Rå¡çÇZñnˆYĞqØpE0`˜Caˆ#ÄrBÃıûg`Œ34„Å¥Y,{ß=¥DôXµ“ÛcÚÎV~cË':Ø$E#b ÁÅÈtpv0pÂJSz óğ­CHhI¦|«²—°˜OÑªRHÆÃ	 Á0iUEN:oºÈhZ$S»¨ŒÍ¶òkEÃÎ×ç·iÏÃßGp:DÖ/=v±>˜°?å üÑ¯ıéx²m~ÒÖ{¿DŒ—â+Ó{¿FŒŠ„˜+
Z"FÍO˜‹şöà»
¹û2”ŞË+Cye(¿õ…ëjY_?áXMûëd	''ÿ<›%ˆ	ÅseZèBE£n­T$K ÌC$0Dcé¬l£mÒ®N’$$lÜ5Ú š$4&	$±vƒDå„¿W²I˜ß¸£Xßà×Á"¯!Gm›’tÔ1¬ÑĞ":@°–à£¨!ExzYH5ÍÆİ!=˜Rƒ)-8¤­O¢2:Ñ`%“(ºq3[ÉIB ğ;ÔË•é‰5n¡¤ù `·ZÒ| £pÜ”9ä zÜ½IóÀÜ¸3´"4#¨M	ZËY÷ş{N	éÑz'¹Gõµş›–C°kH	‚ÁcæÃƒª9ÁŠ=­ìCJ,èHÄ!%V§Ã4%ÈØX&oàôÖMú}®&JNWh'œZHep²š_+3 ’Zx8şJ4õ£@³ïu£]zƒ³'ãâ˜õúáØR¨ |W–vwet˜ğãètäë¤İøùI íò±]È¾@EÜ]yÑ˜v{…
Us8y!íxLI:ˆ[Íyá¯³÷t—à_×(Ô;!8†Vó¨w6}qûÄJ:mÇ*O”$ÈÀ·L¯íàúb¶|•’4ën<ôtetv›Øú¾2v»GnSÈqWY—;¸YP÷‹º9[ ÷ÂğGµ?³7ò™m€?²ß<>–ÁˆvØµSg.%üv•ûEZNá¸g07îZÎLîÜ‚µünûú	në)ÙúŞ³ûÎcà¬sõºÖ‘pøç	Üc%İxÀ}Çò±gGpÙñVš|˜¼÷ç”ò/L/Ÿ€sç¹Në§˜­;°kÇ~ëŸ kı­~Ş€ØC»–OÁ[=Exı¤ÙÏ¯àíŠ9Şaı şM¿'º«~,€7u‘qWìùã_xZèµóYo<t	$_`;ìyÖßÛyRwaú›|€ñ›YOŒ÷ƒ¡ªÕé ©Í3óáY»øHåL&˜ûéÜÈ=oÈª.ƒğãâIáæ(jVøHxÜ¬BXÊ£7“´&j«_ğÿÅ¬æ™Ü±ŸF)ÈVÆé©?c”yàû®D´ßà™Õz`üÈ) ïA}É/¸ÿÏ6ü^ş^Å}ÎË87V}Ç?Á°şPó	¾l‰œ}ÛïùqµS-éórïÌ.nL–ÏHæ£ÙåW¢xr©]YÃL›KÇ•­ŸÆÆs¾~ºÚòc‹ÿ´@©<"°âòfv´ã{óö|*ğ¯B“ñ—O*Õ¾/wa:©ôıˆ¶4ö-Î²¿o\ïŠß¹q_‘rõÈúßÙş¨õ¿Å)C~¬¶‰¶şöù#\
endstream
endobj
21 0 obj
<</Filter /FlateDecode
/Length 6654>> stream
xœí][İ¸‘~ï_qˆ"ŞI`Àöxò¼û&›,O€dÿ?°U¼U‘[b[İöNÚÇç|G"ëÆb‘,•6©BüóØá¿ßmì«×b"ÿøå×§<áïRûı¡Ìÿüï§ÿú·Çß×›°p©K-´ßàFñÀÿşóôáŸ}úıÕã¯ÿÛsA=„›ûKDv¼4}€K?~yúıÏú_şE
ÅC¹Íy!ÍCªÇ—_Ÿş}ß•ùÃãËß,üşåÏ ¤ïİ.®j€Ÿ·!DTLº%T@§F?9&ä¶Iá£\Ø¾Ùu2^Ñ³2ŞÒ‹C¨˜\1£\zığ ñL´şâ°³‹wÕS×“»ŸôÆÈúv=åUæÿÿıãI»Yü£Â™š–Ò€İJa6-‘íªí;JŸØÍ¿Òz·ièıÔŠ%Ø½nOf¼Mñÿ‡ûFÚûf0Xäã×üyòñ?k„yùÀß­ÒJ$Lé ³a—åº]K÷øïöÂ	›Û7§¬Â+C€Q“ m-Ü,`°K©2Ş,ğ×x¯xÂr ¦„yazSÒ‡„YâÍé2._	ôJ¼è×Îgm?úåÉW¾|Å/›RB×+°fW5‡X0Öº¦cü&­š‘ˆ˜Qğ‡±‚˜³ÎÙ†gØ‰šI1á¥g2DHíÁ†FÚˆjedz‰èO3ı!–œnÊšÿúÄ® E[H­"fÑYÿˆDn**œB!¤®2?ˆ%ç1øh³Ü²Œ„ÓxÓƒ‰!hÚr¡#†D$åõ Šä>˜‹@ùö¡Êç¯OÌ.ÄŒ§6ÇÌŒuÌ²’Hv[aöÍ8¦PEÃÆK!YLÖlV­°±ZµGãú—§ÿAàéèÊçèC@GàDŞıÀ»x÷¿u?ğ§…È G©·‹êŒ6­c0Z£ ¹_@Hio9õˆ¥šÖ/­z¿€¶Æs¹!6ø£%Şc¹_@]à
Clôˆ½†û…ˆE¿>e¿¾4~!AÌğjsÌDYÇÌ˜+‰Ìæ++lt0Ù8ªÒ¡áVeÈÆ%“6ÁU/l¤õeO€ê­nõŞ¸ ·€XïÜ‚Ûåàëİb£[p»ÚpİÀıbĞ¶àBGlôˆ½Ü-D(„ìğ[ñésãêÅÌ‚J›ÌÔXçÌ(+™d»•fäŒoU@lĞTA²áÅ$ÎbÕ¯U‡4¶W‚„w_ğîŞ}ÁoÛ¼4P0ÂĞ
Âûná½èBı1aë¼Öõ¾±Á7xß€Xï}¢½oˆXôéSöéKãÄŒ¯6ÇÌ”uÌº’È¿²Â†ã™¦*sU†lp’°Ù(®Za£½(/{TnqQëÜ5 Ğ»†ˆùiÖ{Ä‚1–» 1ô¹†ˆåKÆwÄà£h\ ºwë\CÄ€
Ñ¸†ˆ¶®!AÅ5ÄoÙ5äÏÜ5ĞÅd@µM²4Ş9Ù$‘YM—¸!ç|×Á@¢1C‚¤ÁÅ%NÃtC£•tH#{!Lx÷ïàİü¦=ÁŸÖÎ;–6„µx‚—/ü•¡bO¨s ËëªÏ™¤ŠXØ…Ìn~AÀ@Vş<‚ÙŒÆ <„7 vàù@ÀhÄ»á&aœy›‰ıö¢±sÂpĞÃ].€ÀEíB¯F8~-``Ha7¬Àğ˜mERw cN;`8è°ŸÊ#aLñö“ì¾6(˜ã{PG
Ô.¢‰$…6(wå›™xe@QzÇƒÁÊ¤2v-F.â(˜".¢#ÕV„L÷“2¨R§ˆL´“!G–„6‰V&w<¶ø›4ÕÊÅ•3I~…¶½hùp—ı€9ƒSsNãX²[,_8·94à¸„Ãí¨‰»0ô’¡² CáÛ„J(Únİù½K¸-	báıHgQj¡%H:°##$']ÂG>„±˜1Ç„ïÎ(	îëİ+0ç N†úQ™ˆ6RW±Y°Á4
éà’Á•í6’YT*uwa,TG(TEÌî/š`İT•5UååÌ^*ƒ6TìkáĞ\»|¤ÿCŸ‹S‹Ğú)<ƒ{íğ³g»ßºœ=ëOxæÿzø+áïgø«3é_ün\ú½`;p—²CîM£¤@²!%;4ßKÎÃHŠ k	£S„äÈğO¦ÆxÄŞâ@œËm ÏÃAÕ%;#øƒİø Àt%P„t˜¿y›ÃÓhä!@×]¦ nÆ¨İ s’Ä/¸ é‡Où0ä$ı`RÚ òï‚c}ë”^aÇî‚õ¢Ïö=pVy9¹Ÿ'}Ì;Ÿt!~Ê]€oÎ»Îy/½Â0´šuís×ºp—ˆı9÷¡RW˜0Yæb<Ç¸˜k©èU{Nú}ˆ,¨]™`/¨u®¤Ÿ&DM%5mÊ¨¢=ww.‘™¾çF¸NîTTÓ–¦j
¹0¯àµ=–ºWlhüÌìú‚÷ôLãËC|FÎ«EázFî”Fêšq>••ù©pÀ¬ø½¤£½¥jÿ€h¨òûéº‰M7"1LˆSÎ_vwÚ¹øğ){1ğ€Á(&’Ï!Î¥[:‡Y8hÃÅ‡ ,øm`œïŸ&Bì2ÜìfXXU>gêÒÔÒ¥C6ü­Úé^ê~ƒ9ûAfëÁå¤~Æ>,­©;FÆaÕ —ó;¨0]\•R7	FÎù8ë¼wFŒ¥ÃĞñ\¾s¯¿>OÜè˜¾ç$5÷&³ybÊßHd|œÌÿS+‰!«tÅ<fîp>“O&ì¹,¦Óò,2=aF¸g¨Ybí‰?:TøÄaÃÁè»º­[ætF™1>’fQãT´gZ˜ü±ÑIW+‘ò,äqšur$f¹àvæ«f>×øçÍ÷p$ ÏûÏ	éÏÛ´­Iò9ã}ÃIÖòàf:Æ>Ã‚YÖJunìÓ˜à-Ü“›RæÖ~¶VØA}Vè~xëÕu“^Ê§"ÿP®¸;¤¿u12ù«‘iïË“âéJÆ_Ü{LG¡_CTu@í}›S»m7ò ª‚ÜÙŠ|¦ã™µ5aÿ·m¨Ø++ˆùRo:j¦ËÉiS7.Ü.›0‹	šÄ7i=ùmËx¾l|_ÆÿËøi¸b„Çy>û¿/(o[PBD°i¯ã‚²Ê·	W6bißÁ£¿ôÇ¶xi#v=Şmüş•]ÒÕåÖI¸ò|ÈêË*}¾I?23'="–·º^L_p>°=Í­iÙ0oİÔçì¦,x?ÏÆ÷^ú0¸ñÔG]„iŒ’Âxƒ7àB´9Wøì†4zQ?Û¼¯‹©2näb2äç4í3U,/Í¦qé¥|iÉv}çìÒ
¬‰‰ùRËŸ37İçîšÏaÍzÛ¹‰7½HÎ—ÕÍö‹>õ ŸÆ'Êab•
9û"p‘à&{‚A\º—Ñp0×¢ãdˆuÄŒ“IIcÊCğ+¹ãæ,ôûaFS°¤Ì›0*{« a±Î…œŸÈß”ĞQìt6‹‡üçÑÀ¦7
ó »0WoBù lo‘aZ{kÉ„M…]šqù4¶ôé¯+˜P;†±ëìÇ€	G‘·sagfš» -
©¼æFL@ÄÔÂsÉÎ˜˜2=é@›¢!e¬á»}…7mí×s Œ	Ïy;ÚÀ@ÛµÚÕ[
ãÕ™ÎãŞáş¦´ìğ8o_?+*+Û‘„
Ü¬<pWÏØ§[jëqÎ3ı©·]ïdù=aš‡±ŞÔlé1“úišÉd—öàcõáÊìzQP«©Nó=°ï3M‰5b¯s³…9=âv£¯l5];«ãáÔúÆã<šš2¸œ¡°¾É60_ü½ Â\×n¿²ë¹¼™ö}·ˆ§üL!ÓMå)UóA8Í»™QuçúX"Â~ÃnÊàt¬M·\/I\2÷Ô™Ô…açÖMT_	ª|Y®LgÆ©_ŸÎâËÑËévš }°µ[öq°*é‚9QË/Øá#ƒ‡
o1‘¯¶4w’S¯3‹VÏ(_ğ,ÎÎCşY´º|Œu£.ÖÏf']”Š†—÷¾UYozøÁ¨ÉYuãÓ¦nşÛrÁšÈifƒ—2ÔùÉú™Û¼{k“N¾Ÿ//œë¯k7MWëQô¥%iÃù²7\7İÙÑ·Æ,¯PÔÄ@Ëƒü‹‡õ;æÃc:
®M)—ÒÄ_'ÓápEµ0Ôæ§Ósá,Wï¶$ ¬&>#òéÄ%«²#ù{œu¾ T˜nÃÍÆøŒïiÎÙz|{i™s-*]N®^?'_ÎôûÛjÓ™ij„ë‰¨·=6öâmŸÑIİé:×§ıåí’õ@a>Y/ß9“.ofşv¦Ø³Cù•ıÚ%»ñÑ›K‘æo0(—»WNÔfú¸òˆ†Ö²DCi˜ø9ïrjş|¾ş~çl/‘Âj´u!­Mßâ|OèÎHoùAšû6ÃîÛ-zîıÙfLâîüîë¦8;Ù¢¾¶^û7Ö¦Ï“Üxú6ŸfO.’NXp·N?~}Ò>æ¯MZƒUë6¸Oæ‹¶XmóÚá@D¦§ü‚÷:m¥•ˆbE•X-o³» 8aË-¦…–B$>‹t7üj±¤¢pÖÛv±+m"Í`ÅP|äPŸ0¤ïv@×®dH(Ò‹WJÌ‹VmMÿÂÅvsJã&cúÁnìÔò[-jÄ*Ñv¿z˜€'şu
ËÛ1²±À–qŞ´‚yĞšà¢€ÂQÈDf6a¤Ô¢.üjv—˜HJ0\GéK¼?a½]T¿K!›¦m?9§Ô>Q"·hZÅø”¦åMâçÔ)“‚„»\ì›¤%±uİÊU±, W z²İ?É¬;™MJ:&½—{¹…P'Ü–
9Üæ
ÙÜ:‰AnÇEÜŞ‹ÈøÈ áòTÔÀGZQW(ZÄ’–“Ç,04r¾œD®Æë[5Ì#X5ä(ÿœ´ş#ØÑ`·Ö rà?‚ı`ƒÿ ìÀ`ÁÄŞ7úÀü–ŸÃå7µX’µ›ò©¿’!×F˜Å³îØØ¨„±1T`£±ÊÆe
¿Uxl¤313ŸÕa¸¶Ò—âI‚=	`ƒ'øÔ'	zô$Xµ¯÷$€x,^œi<	`W]\5rİz `Õx’X‘;ıÛz’ø³€r/·ê„[U!‡[_!›Û©>ò$UÜòõèI˜pùX2£'©ê
E‹Ï{³ïg9Ó]åûö‚ï[„œí*gge„o>Ø;+ÄZg…ˆ³F´Î
æ—hÜY!†Á ±ÑY!Ú;+Äzg…˜¯s`1UD{g±â¬ jıZÇ
5BƒŠwGÃ£aJĞ€æ¬ÒĞ'¡‹ á‘3áb&·SÔa¸¶Ò—ì¬ŒpÈ¦~4w9d³mŞD=FØÁW!Öû*ÄF_…hõ ÖG=ˆQ‚}ÔcDŠXñßÆW¥˜Ø!êáp£²CÔCds3µ¾ŠDÁß¾Š—¥¬>âŠ²BÑá‰«’e?è_¼ËB}šk¾ ÑrşI­öòòÎrÇWYHÛ–p6éò\¸TîXmaÇ·aQ‰_ å¦%Ö”¡jÀ ŠMî6
*,ğÕ¥Á[)Xç¦²°TŒ˜¼3ƒy%gS5dÖNn£ËŒ	V¹™ØmÀ"^Î¹Šñkj|Ò±jÎ€á©¡æÕœ¥cEn¢ÓBÅ«9–eÕœ3f›bÎäµœénR	õBÚãô¢‰r²âğÀ¢ÆRÎVPÙØhô^Ã
]ƒ¯:©µœÁac™¤øö”ZÌÙ(ĞS°®)æl”Ä–ÚjÎF‰\ãš•s&°©çLpSĞ™5AYgTÒ™“E%TÓ™ñJEI.¼ªs•!/ê,¾@hÇŠ:ª“Zsš(]$/ê`œÁxQgÀÀv4N’HÂDSÓ¹‚¼¤3»»êƒ:!Å1jHÅD6³›ÊŞhKß­¢³	ºì*ì©‚óO{ªîRÅæò×üÜ~˜ÄµÂŞTyÆªÏ7ãõ¼l?Şó	ç™Ô†v‰x¿­³b92YPVÅj‘ÄF÷¼í„ëàëå×ÿ"§•b—>c•i.±(‘9Ò'¤À'´†äãûV.Wö j÷
çåoªŞ½ø÷ÙºÜ3½¢/Ñ±ÆQYc–.w%¿_]–“X“Ó‹d“ÿÂ4_^nşŒLâû6â£×D51ùVÎ‡'ØñÜÖ)Zp½ÀM‰ºµëÕpÎÕ?Ô>/o3}Ú}±¡ŒC´p¹4ã@iÀ…Í)s«OìÏH
ÏÌ„WJ–°äİ‡½¼[‚	7Ín‰Ãó‹n·±v·‘qk×ÁÜİoí"Öoí"6î– 
w	¾[‚˜ÓÆò%0bãn	¢ınIÄÊn‰K»³´§_ëj¡e=ï6 ˆ0Ú( hK³J›$Ú¤ áÑv3í{u®­ô%ï–8<\ê¶vë·v·K€Ÿa»±~»±q»Ñ~»±~»±a»Á~»ÄEãHÿ6Û%éfjØ.áp«RÃv	‘ÍíTl—(¸å«a»„—%=lí’ºBÑâóû%…souH4î@ü‹ìYÜ‘ {_ùÔWx“×:¼~1è;“Ç×ó™–Ÿ÷_Ot:©¼Zfìàº;¸qÆ®Ÿ±ñ,rœ±ƒgìàÇ;ø£;øqÆÆ·äõ3vğG3vğãŒ<›±Cèfìú+Mµ6³°îØT	csUe€ÍjŒU6ÿU¡°y²
Í¨LÌlîÍê0\[éK™±ƒgì`Ç;ØƒÃX¸hœ±ñ¼°Ÿ±ãûá†;˜á0±ş0±qÆfœ±«M7cÇ˜˜qÆfp«2Ãa,‘ÍíÔÍØUÜòÍ8c3áò±dÇ»ª+->?c{êûŒıÎØ¯_8ûÿÙdº\t¬–V}II–er—Ú¯;DëÎŠ3Ó‡7Î¸ÀRJÕòp_Pı‘×Ê|~ª;}Èfùğ;ËUNGyãr­ø–¢/µŞ‹MÌy#ó7l•zÚŞ;ş”Ö¥—·¸+ï×:«EµRptÖÇ
¾Ïê£Îê¬ŞøZ3ùıpBóû.‡íÑõJ;'¯Gºô´ü¼K±K5#t“$ï!ælÖUSšºubß©Å¢FÄÆÌ1/÷!s±>s±qe…hŸ9†XŸ9†Ø˜æŠh¿²ŠXYYá›¾›•ıZ{j„V ¼;Z+a´¦ hõÁY¥u
	…Ö3$<Zùp1Ó‰b¸ÆÒ—¼¶ò˜sÖå!Öå!4n†z¥]cÚ‘ŒùM˜¡Îxø&_Ó.¬‡Å×UÁB¦Ù	ElHrE°Or,©O¸v]•~ ı×{™¥°N˜MUr˜íª™‘wÌš‹˜ÑWañáá¶A«üùxó”5–´w²¦’åUwÆ oQÔà;Æ ëê/W`¸¯(Ù›Tg]Oi.ÈoSÓ´×j¹)ÛóàlY».lƒÂ½¢¦ä^”'ÁÆ7%SSàÆñ]ÍìX™*#ooÖƒ×Ú4–îÆœ˜¬¯?<Èö¦ ÈO)³#æ©ä|–˜ğ)ÙÇ\†œ/ ~:À ¢Ÿşâ[Òrlğºš9Âóağ-êøıç„	‘3P*Ã/O˜T<"&<ñ„Ii,øY#štI qXÁ²%ƒùsŸ(ÛÎX½ÁÜfšTI@Õ&àË”,uÍòü
Ä³$+Ès$+È2k,‘QÃ²Ù,¹±r×`I<5²
ìkjœ=KdÑ=#0XVÈ½MÔo‹sø^DÆD“YAIw“
¨R§‡´J”“ö‰ÃÛS#•Êyt<5Ü­Ê¤6 €‚çEbµ}Ì½,»0ˆNdÌ‡¯ix â …bY‘€é˜+JY}â‘äùtsÍ'd}ÔÄÃ†˜š¢ÈÈ®©ŒŒ½šóXåÀ!«Äx"$¸>ˆr!.d‰€¡§0Ti<!Ê±á1¥f™€‘8ãX&dÆl“	YA	Éî.*`T]5äT­2Â™TGÛùn©Xêÿ8M.¥vÕyF£@`8¿c_ü{]†.@80ñ¬:z>7î
[“Î„ÖàºÎ®äÃáœ{×	$–ƒE¨;$u Ÿ¡6>MâkÚˆ€8y†;„¡l½ZÊ¦fJ–™’${K)9\ûÂtÇéŠBúx…WÖD1ÙĞß W«û^]C­¿µP´> â6Á‡c0ß¶ÎÈ7Æ kÇD€m÷Øs­‡ò2Öºİ)·:d!fái›>£sÂß#–ó­uc1ê‡Sú”O|ÌrY¥Úâ\³ÃPèÂ ÷,Â¹ª±ÚåÖ~ÏŞDeµ-_áÙ`"A^T¼2Ï¬+áÈJè)ÁB¨¬‹zlŞxä@íeG…%ÁG‡èî­å]Ä¬èİ4üéDÎää›–î”¯.zÌ\é©<Àså9µiöNXÿê±¾ÈêD|&(‰›ƒÑ•5½İ)'ï^]NŞ5rºo~İe™_Y'÷Í¯¸KŸ´¶ş¼:ïœ1yhWB5|»ù÷ÛMKÔšÂ¯fZÔE‚úŠÿ!Íòîä]šWç]š÷8768ã_úö~¾k÷ßt{-
endstream
endobj
23 0 obj
<</Filter /FlateDecode
/Length 3758>> stream
xœí\Ù®·}Ÿ¯èç ns_€ €V?'PbÁ•;ÿä·ªîYš#¯eåŞ«‘zÎ°Éb-‡EvVcsùY~¿[ÅÛäôšuÎiùøéôË‰>7.©Åz•—_ÿuúÇŸ–Ÿ»U4µ‡í;Ü¨úıÛK½øõ§Ó÷?Øå§ÿ–şb¶‹ÖÆPw?DQÓz¦¯?œ¾ï–¼|ø	õbã“6~1vùğéôg¥¬ÿËòá?§€Ï?üs`Òp{  Àª¤ë}h] ; _oÉpµÓw.½­F§($×a?ˆÙrŞb?•ó[öêĞv\iqMr“Ü’ ñ&t¾İ8+ÑXÙ½t{qÕÁØpF1vÜK>tşWüşrÒ:¬~Ü¢£_Ñ=Ø¿5Ú¯=±ïÚ•üˆªWâæï´ÏŠPwìÅ~ïrTÕ×Ñ•ü÷ƒèÃ¨Õ/^{³|ª×.%³<Ñµ£ LhH„àã`Õ².kÂBV¦7SÎ.éŞ¤£¥3µF,5Ì1S!<úÓuclÃp‘éfOC¹7fº'PÃh#ŒT±¤C†:i0“rÅBÊåfCbùØZB\O-!½‹©aäùíêã)äØß<Ñ›ÕZíFK‚W6‹îË>„¸8ä´š`²"æ-~ÄT‹!âJÎ9ä/1Ú	í¦“IB‡Y•C–Ê&ĞÙ ²U
ã96AÍ¸õfõ§7&€Ğ:(,8|Ê£,{ZWEL€*ĞqáÙÌÃÆbŞÃ¥nZ«êV"……5Y0ô­…Î)êİİ:…¼[°B9ƒÕwdocûõÓ‰ƒ³>ÙÓäàì“,æp]û¸œ÷VÇ+’ƒKjœÃmÃÑÊ6äÈşxú7qBZê¢‚~]X–¼0Á¼0Á·Ï¿#;hFíÀçAŞ¨´¡ qG².)=aÊ™5 P¡OL‚ó[©6Âpá$5 ôtÔP0Ä“#ìŒ
º£†Š5´«Jí¤†	çİ	7‡"
ÇS!"æ,‚ih‡cnèP'+[Dñ°Šˆön¼ÆdÜAdõ5 8£Âà~YNt 7Ôà3yt¡1ÂàùQÎ›0\†-5øLÁd$3„®ƒT9açÌ@(‰+©°Æõ²òB½ŞğB…„ëŒî„“‰…;ÙkûD„w‹sÕˆh*a%t-pXEÄé°Çô=éÁ¼pÀ|›ğ¹‰A0°K'òÈ)_è%+¶Û4ê·´¼Şí
´Û5l¿k ¨Îh°=-†èô[Z ÔÓÀlÿV¨Wê›+TH8^ïMx¨VøòP¸ü˜ˆ1cFC7mCƒ",…®E «ˆ@ÖkL@æí´Pì.i Ò€´P°-lO İ
¶Û5ìl× ”Ú´ …ièR(½`g´PĞí¦¡B}ÓPŞ5bh×’¸1ûÏè“MÎ.ÉbÏ“a—³¡ÀêáˆijÜìš¾w{¶G+[#ûôà…	^˜à…	¾i&@’éèkÜ²:Ÿ*%œœ$”G*˜Ì¸y¨¢¯S¨bŞ(åßâ•ñ2xy¼´Rî=Á¿ï*î *ıö¦è±^‰£>líÇ¹Ö6Öş\h}»zßhG2à½Cÿ.íÚäzİÛ•6Ô/½_1­[_o>ëyĞòó	ş¿š¬”å£^SôhùIÀv Ou@Õª!H^ËP°V¤’p¼[µÁ°ãO[	¨
ÿ Jû‹ ZxX‘+†Èreì="{ÎÅ(B«×Q¶†˜ËÊ‹q€ÑcHÈ+%2PEKÙÑñ&3æ(±®rwC…ê¶0¼ºÑD“]Ut%b»P !iö¦î»ü€#fW—‚>Q€‰Û¥ÒAÓI‹`¬@“õº®El1Ûo#›ZL‚}BL÷¢WQ0“ËEÏËCùĞ…árÛX›¹¤¨éÄƒ'cYì+TŒX(¬S‚ËeµR} ê&Â±P	4R¶C 0oÀ6a¾52´í70²CÈÍãJA´I9y¿‰ C¨Fc 9pBŞ
d yãµ‘¢›˜i^N±aQ(£ÜİP¡¹§w ‹_p±ôÚFÒËp€Œ
 æ¬jâÑ¥o°ŞÇ…§	.àUñ·®‘V±†ú±†¦eİ"r¬a;)Õ0²”_ºÎ˜é%êÎvÇãn¬XPÊ_´rÑ³EöŒß/0N5`ÑºÀĞ0\.©a¦. ´°àR”¬4æZ²yß+DÎ‡/‡÷ÊÒ$…´ÀØĞÖ8İ†{ÕÖ1)Q›1ô„®ol,ÃÛÍèÛ:‡+:ıÜ¡3ÿ[élˆA:3ïÄÚÛÖÛ¢¿‡èŠòv£Né*©®«WœŒtáHOÓÎàól£—Ã’nJŞóêAºØ˜€‡™R2È;š[dµù&ÓÕÇÔë/ÔÍU›ò@%úšQŠ¡\ó¦$²É–]v¡J¤†Ú®_÷L²´{ÛÏí_ÓúËPÆjï)ûìÁ4Æé÷ô´eŸ>]fı(Ï‡n°G ,CjéÍõ¼…+ú½n§lnã3Ù|TØcÏ°{ût½;¶EßM”Ï/·{ ¬¢“ä¸üÈÒf¢xq×”°|3ŒJèµÍİ ğ¡Bæé!Q6„MÕc&CO·vY˜òhÍjíb6‡´h7Í#£9M{mU"ïš2ZôÏd´1òb~!F6†k†*˜†î¼÷Š¹°ğjÃœ»ƒ¯eîQn=SÂ¡I‘œ;_R-q¯÷@íBÇAX³—ì±"‘é‘x_3ıf‚¢DÇ—z“V{“
¥q×şÁ§éPSô}d&mÃ
ªÖ³=íó„ôGMU†)÷´Dh„z7Éò}7wäA•=êvœ°æ¦GÜ·á¬ÓúB/BÖ¾V'²foG¹ÎcvQ9¬mã $F»±EzˆÊéLM£.èà·Îá0•£.äêÖÙ´ÕÚŒzıL¤äõÿC'¦yG'îš2ZTÏd´¨¾Ò$î±FãiŞ»<ø™®ÁËçñü0dõ> ƒóÁÅj›’Úí°Û©â¿wªğ¶B	
Åºí«şpñ«|[àé¦€ 6ªŠ}ÈnoªŠÍ_“Úg=sHœ)HŸ Yd6¢,jÊA®JøAÏV^±®Ëà®ø`êF<Z¿­YÛ¡˜ĞäL$zµ?~
—ÏÿdÊ$•hxb]1İÛäsÌòÅ8e5ò¬Ø±Ù‡u¡&ğ$çtbnÏ\v ™h“dPî(òÎ×l‚¥zhäyDäŸßöƒÖGl]œ[S›»ëÀ‡Ûg WtmnS†èi%Í¢ş–_x”OwĞ›7š"9ô®Š ˜îä¶î†‘Q9X!ğWk]¥[µMYóW7½m7KÅ5âÓ>pÆĞ7:^¿xšV£MQĞ¿|ºÆJˆwŒÈdIŒ¯ÜÑH’*`¨¸…{j_T]}Îxƒ{wwŸeïMAƒ-©•Ş”3èÌêÊj€
Úò¢˜£PÉP)QÃ£OôLr[Ì {€ µ(f(˜ñZÔ2H–2PV2PŒ1DÍ€F”¹EBŸŞªjeCaO[0¬Ñ„$j,ÕYTá#ù­2›ò‹u½$­¢z˜î“ëõ’•”u¥$cQt"¤å)UhQÃ2fvÁgÎ‹,¸¯¹“xâK€ŞT* tô@[‹J`fÊ8ù´;Òş-B¢RA#jIóVT* £z 
$ë(Ëøf~ÎÏcpA€†kXl.2àéq=B×ƒ,R“%
 áy)Q¡ Œ|!Ky,ÕÓ¾;1ê+<œi¦
Ààò±-ŒŠŠ…MuÂ em‚¸{‹ğ \U"Åáú\úIŸà¹ïüne	!E¹k¹ãeEò<vÍ=Q	ùØe;ÎÏîëÚË¿¿€Ù–vĞ˜¯Õ¦¾Á‡mšRòÃpY&ÿş(á7HGÊ‰İ=JœH­¢ÏÄLİüöÜ}l´öû‚4qâÜ¶ãÜûœ0ã›(ÉóìEòü}Ï¨Õ¹ßE­G)vg€,áœŸ„ñĞ´W®²Hj<7Å´eŸĞÛˆ=Dß¡k%‚ZììÇó„~”×O†ú·áûs	qô76Ë}#ıæ2‘lÈàšŒâÔâ:IM	+qNçÉ¢èû¬±ù•§.ûSµx[/C]ÿWÈ¾ÌTÔS –xj‚IéÏ\¾†×‘S}YßÓNuglb6çÆWWù£IëQİÅ]ÎI`óË’ôø%)ùô•/I,áœŸÄ–/Î;{î$òÕ=Uö'JªEğXz®,a›œ²?ˆhTÜûpm™*2´h¹µtÌ²ÇşØíh9ê}ŸßwÄ(ôMŠÊ(ñ<ß±Gî™ç¥e½,¯ò»-})ïOâ®Ùˆ>ÛÙ÷Pq¦ËRMM"kÿ²$}é’tglbGªúº9us,İ6~¥¼á};7·í:Ô×q¹NĞ£ŞY5%™·ß¸·\¤µ:¡ƒ×ÜaBK3Ê#~K°æªMÒÎsĞ­u`ËAG)qùeYÔXê¹Iæ—”øZßóü3©Äc{øÑ÷Ğuç‚…†Ñgq‡÷ÏÂöuÇƒJ)ÕÔ$ÌKF}oß3ju_yF-$œó“02êÎ¬¯Ôø&sÙ÷õà¾l'–¥£gÓšÙö¬­ÔK~FÙOcİ~’keÙ}íLÌ?X¾“|öcÏò\»ïˆ”¢ke#B»óì“ÎRjóy'Aî†Aë)Ğì“îI©ƒV/)õ—.iw)qÆ&fÔùß<úkrÚ['ACêìÛÿ.FÔ}ëös8ÏJœ±I0"'ÚS5uÓ—‰Ë”=¿“CmJşkê7
endstream
endobj
25 0 obj
<</Filter /FlateDecode
/Length 4521>> stream
xœí]İ·¾?O1×2Ñ¿D (`¯í\·1Ğp›… éû%õËöÌœ³›5v;çpF"ù‘¢(ÎH;+ñgøç‡™}FÎ ÂôåÛå÷]W&ˆI[Óÿ¾üó/ÓoH7³tx«O=,¿aC9ÑŸü4¥üzùñ'=ıú¿ØŸ=I©u÷K¤º5}À[ß¾üøÉL0}ş;ŠÊIûÙ©ì¤ôôùÛå¯Bhû·éó/¯ş×„Ö³&øHğ• E$„qRF‚®›š@%˜ÔéÇÏÛ‚#n³’Á3É¥[3Q+&ıkUú&k8¤^wŒ$WÁLÏB¿{üfìf¡×Ò­ÅWx£32Ş~-yÅüïøç÷‹”nvôc&IH+‹«¤öÑ¼VÏäAÄ"}bÍ~ e˜±ñU÷Uèğ¼Hş;ƒÇø¿Ø®'bJÌvrJëé[úlÕÓWúlhô"(( xİi£e¢i’h„*÷	ƒİ~¡ÖAzébwröÚiº ‡K"gÃ¤$r¥t¦á ÆtÕ¥¶±¤½öhŸDÁQÄM« ‰æDÎQ.ëó–Gñ™D>Ÿ?}¹8ğåËWú2k-M½“øICëH`ó¶Â¬œÃ$šÕøÃ!šwŞ»…Æ`Æa.Ã†h2¨À$’à`5QF³J¤¡õ³Ñ²yS£l÷¯—v7twê5Ò^gü#Q¹«(( ¦¦O¤YiEóHÃ2ã–0BªÅF	¢e$IÄ’i(Dj\¬©(îÔ,˜H Ñˆé[ô]>½4Çh77ÿ©}6GãÌ›K61«çVeš‡s­ëPhğ´“a”­Œ·u©q…Í2m´6¶‘ıåòŠ	aJÿQ((ŸcA;ay‹o‘à-|ÿ‘àçÙAÎ0R`L	õ]„§¬CC¤­BC¤u¡©èšâ@ÅƒH†\”G4ü`xh@¢_‡†H[…†HÃ1
‹Ğ©(¯e±!Ñ(6äO)6ä/<6dó¾ÜwÓÌwš€Ìí«"l€0ÙPªØ´WdC“aÍqµ
ìÕz9ykh »/B ÉCÑÖ¡h]h c»Ğ@´uh ZÀ¸uh Ò:4M‹à–¡¨F[ËcC¤ÕØ@ßJlHŸ±¡ŞÌ¨vÊ\±gNYm¾[Ôa>Îônƒ¡ÄÆL’.†8‡Õ6l¼V¶±}$Mx‹o±à-|ß±àÖDÁ›àKpğä×<8 A†,6D’6Q“>ÒºØ€ÿ¨Ulˆ¤Õ"ÒÖK$Êulˆ´Ulˆ´.6Dê*6$Å†ü)Å†ü…Ç†Ljî×ºkÊ7—n"6Ïoª´1Âun£©¡S]Ã°NvÇÍ.m¼Wó¥xÍ[‚C´;DX‡H[‡H[$†upˆ´Upˆ´.8 VÁ!’VÁ!Òº5D¤®‚C¢•à¿åà?óàĞnfT;e¾ÆØ3¯¬‚6ç-ê0'gz·ÑPbƒ&¹XEdÄW«ˆbÃ‚C³aÛ…·XğŞbÁw~ŞûÀcúí‚öœHç&mQ_¼í£ı MOA¾Vª‰T3+D¢‚!Q1µRF"Ñ`#ü‰DÌº1TìÁ"ä¨o¤DÆ{¼Û!Y5	!	+SDH4ó`fW£’m³Aéù½H£„]Ø'¤Òs6+¹”*¥òL	$Jt†Ì¬è»¤&lb™ª›X†!A
Ê9##İzCnS…Ò8~=í“ªYš³Yü¬(Ñœ2i’D³æ^¡‘õ
È­m3GãÑLÇ¥iVnr7húõŞDşH~¦=ÿutE›ìg†XªılAÕbö2T „AB4‘Fi”64)¹°Yt4ªâY#¢Ašœ†‘3ù8ì$E«Bº9.#¥n^¦ÓrR)\oÓ>G±"ÓZ*of‹,9(•ü‹‹£<s+ÕRxå4µKE3Õ3Pb™Zàûzií5J Nr¦ÂIk¼è1À1©´AF¤ù³h€.0(Ş™õÄ˜ƒ Bt°‚G¤Ea*l™„²TlYËbÆ Úk!Jµ-šùKU®ó¡â]ûŸÚbHWSú‡‚-åJKJ[<ÅgÎ»2‹§Î¸s#mzêŒ¸¾º¿öÓKô½x”¿+ºÇ‹ÀzE4g8buà¶wîòv÷A×	$PÌ.ò;.ée‰Ùz„ì­“‡xÅà4d‘?l“Ók-r¼‡ö¨o³È|Aáı^ú«¥÷P<~	^Ãí$*¯Ì8Í@°LÔüN¨Èá:VgÆ"-Û•/à,ù¨j +‡ÀÊp]ë±°Cæé%œXl¼ÔK…Ó7xÁ.TØÄxó|Æ~ÈÚ…j[¿æíV=Á¨â}æAc*İŞ23py·Ãó;S³”•¯ıÆÎ€Ìm€³üÀwïX¬>^ax UAÅË¬”àØ¨^†I
`‚Ü›'y ¥¶¼Ì¢M­\«Ğ7ÉJxtTZÛˆ;»£§¡TÅµÓ[B¼dïi
àBÌ~€®æiíXÉ²?iäí•¹®÷¼‡š?ê#ëˆq¤¹µ×¥k~¸«9×CiÈ£†ŠNÑ(¸fqŒ6Â|Çz¨Å¨«¡G…-qM¼ 6¢‘@5ÌVü"(Ù¶Å1mßöZ?sÃÂVáºaš¿P4² ª€TæïŠ¸ !\ïh¬÷x`šˆOY?ƒæp°éŸ+Å¹i™Ş\I±áºâÇy·ÓĞäC©†ÌÇâımh)> Àìˆ ÇGÁ’qoÕâã€ÇXÁÛ½D8ôD ùsŒÿšêÙ5¢¹•xl¸ãXÑtÂïğ’¡æÛ1F<T-œŒCŞ(€™& AM³˜3`şR)¢#–rs¨M)C¨ò~²*™œ¢IM*Øäj‰n<
ñaƒ&hû şô^ÊûÔŞêÜ'¤ïto¡Q[cò½&õIÿ—2ßSSÕ[JÒÊ‰dQ’ö!ÕäZùÑ\(a²-Y1Úƒ!À±‚&®fPÔE%Ú#‹€VâuhŸØ¶:j&ğ
t&ñòs&µÒmë»y¹­Üämeã¦§å*e¥Œ¾.i„§o•ÒNGË‚4DŞZœ‘Š@’¥ª†4O+8GÚ²ŞœI¼ÜÜZ6Ì‡f.K³c“ºÙ»i×{J_nVÖºäC¨V²(53H)5+4k8Š•-Ñpsğ"X^d‚–nBVb"ÕwZ­´Px‰¹Ğx‰¹¶¬ZÖ-å.©E_&r-3Õj9ÀËÊ&^VFZ˜ƒ•••uädA3Y¦P˜°,+#EÄrÑii¨7*‰×•+‘W–[ã<cQ-´¦Ú’‰Í=£¨×yËK–‚”+ 9’R$/‘5FÙi*Gg‘hÑ‘Äê’”|Ê	¥…ÉÃ¿×‰¥Cz1_”kÒõ.Ç|’„8ÚÊi‡î£Ú*=ÎTAÜ–û¾PÕ­r» zÇ&¬‡<9nÃN„‰K£Åqæ/Y­‰ 6oæc2¦ÉõÀh’ÍS{ß†…ı€•ÙŞ:˜¹;`UÆÊ ß§lâğ´ï9íÏÉ#à©\ô8»Ğd/¬×r_w VYœ84E-&?½ÈÓÃPô'‚Jo&,yìƒ4ˆ3!ıÔî¹”ÌsªÜ
2ÿOyœœ§‡Ó>@ÜNEët{ÌÔ¦„½xÛ$>0±Y¡I)ò ©s4:gj¨3UŸ'N2×Ì¡11zÍ}µF¬RV#ºÆ®Å˜[Ú|_]l²©ˆ;CY°æÆxJ¹øgyDòS#”Szv~w>ài08MW@\siLçfc5.;ğíqië^ƒKW)«K`.Í²§’3Ÿæ–:¾ißG`RôÌÇò»S°2ñÍä6¬hèdR„‡Õ°ÁéšƒZpEèV¶Üå Ş¾­Rs‹Æ,ŞŞÕáé[åâš‡iÅ~/æ;ıµˆFå‡”!xÛùË“ãwô,(KàS–;´érä®=‹‡ı-ØJâÒ80;u Kí6ºb8iL>ˆ·Ú3ÒÔ¯`¤7)·¦¢ÑZóšäçLU!ÌÉ=˜Ggª[ÓWÓáæ`A/áÛåZ½Ÿ¨RnúÄj±ü<¾àåŒY!Eq&İÙÎÀ5»šx]æ.Ñ'°‡JÎ)uÜ»¬Û¤y².ã¶ª G z‘²n“ñeİÖû.À¼ {™²n“±–uı}ÊºÓ>ğ”?ŞŸ®¬Ûä¿_Y·ñØ©qgBúleİ&÷½ËºÓ>@]¿Úxìö`^A~Ò¤|®².ãÈrè{yèìÆfXæİ‘sà¥ÔË%ÚaØ ^Ãb¤Iù*K½Lü{yÉ®Zƒ	sôZ.Ï©¥† Ú“ÖsK­ç]ÂÑ†j¿l·k8ù†C•ò%ËÄLŠ'zõ0<³ªÄ
ºø^>‘o0fW—Êãî¿uâ5ø­÷
ã/X=fZİe\uwˆs?—dÓøº&<ù©¡˜i?L©ò8eQÖâz“ıÌ !…*U]Æán¥g:ë¡SçZá™N’éeÜepx/g4)O­<Ÿ6‚+¹6“ô©#ÿ¦rôDÈb
šU1è=Ú?¿³4)O)IŸæ$¸ ËÏ™„÷v’E™zs´·;¸”wWÜ~½ÉŞí?º€Í¿gCêY‰ :t[±é-n'Áò;iÄ•:<½ÌºÚ”ÎÜ	ªÛDØÂuuËñ¾òş Ìïhó¸è¶†Y
:\€íCÈ;Š´TàÙ¯‘EÃnçà»rEjÚ~Õíg¤6¨‡á½AÑ‘ö'9Ùm\êùç‹vœlìu|l¹ªd(Úå-V¸H7ÚIÅ7îŞ°µ|´1™ï°r=Nic›ág$·ƒß˜¼k7êB¿ÑÆkãG]vîwEó-½Nšš—í¨tFìÙµ?Úõ=Ş÷¶í7ÆvdğÃ»¥ïùojÚuÈp_yİ‘‰™ŸcQd¼7ÿ0ó¡æ‹m”Atû]1-Ò&;€~;rá™Åa4£šù×şX:Ñ	õŞ<ÔdïÆë¡¸f Õ›¥,I›.nÙc|xû¸)SÓ	ûæïæ+8Œ¸Ç÷Ç¶vß%=ÔÑCğ|:;¾WúøïÃ{ŒÄ;¹ÃC›ç³0b>D·‚¸²`Û¨-V~õ´SLÛÇO<^aÉù™
îcJ`¿Ã‡=ñµ¨Ã6/¿•¯kqüÂpC–êñDší»c89¶€Xc>ó>iœoOˆÍgƒŒn˜‡İ Ó°«ã'7Õ&{R…EƒQ
?éWsûıÉááƒ›@uƒı§Ë#o0ìq9Œú8»?¼j§1T£qytátÃaKÃÜp8†SŸ-=ì9Îm_ÖÏ“øqÜ©ŞÎÌ”°lò¤ƒŞYØµ³äœÜ4<´jW–²÷Å°Yœ²xØè7¤a£ô	f­÷ƒxÖ¹?Ï±€§êÇ}dhØãKÀóòÒ ºÂñ#÷,û—)ùs`r¼«¯OLY&¦ßo¥¬¼UàÀHNÏÆèuá,²¾r¥>dØ%Õ½ûq ³4&8×ıo˜¦_-Úş
ô–”²¡‹ôÂ‹BiºÃÏ
—
Î¸5^ÚQuÓ§8İÇu(¼ •¾3/ı^
ú¥×¥­ê=[õHo[æMi6Qd–:€ì‹~fÁj:m•ºCcy´È.ÚÃ1Tbè#í†=µÄAGCËv³ã&å:^¿ËŒµ.„Î“O:'ÏËú†ÖiçäA:+Ï(öØçïNÔç¼üÙq}œ_˜ª¯‰tÿö™yÿ0«<
endstream
endobj
27 0 obj
<</Filter /FlateDecode
/Length 3409>> stream
xœí\ÛnÇ}ß¯˜ç ÷ı$’òsbù %vĞìü?S}«êY.wÖÊ’MJgÏLwWºLwuS«±¹|-
¾YÅÇäôšuÎiùôÓé—İ7.©Åz•—_ÿ}úç_–Ÿ»U<kó'4ÔıùÇwK½øõÇÓ·ßÙåÇÿ•şb¶‹ÖÆPw?DÑ£õ¾ÿxúöƒ[òòñtT$Ô‹kLÚøÅØåãO§¿*eıß–ÿ=Üÿø¯€I[ÀmX€8 «
.÷¡uì |m’àj§Ÿ¼­F§($×a;ˆÙrşÄV•ó&[:´İ¸$¹InI`¼	ışù‡³+»•n+®º26œQŒ·’Îÿ?¿œ´k /·hbÚxx¬Ñ~èƒ½Ö®äA4D½Í¾1ÆZ·Z´¾ê¿ïrTÕ×Ñ•üíÎAôaÔê—èR\~j×#?Òµ£ğKXH”º¬³ºBÖ¥@XÈÊôÇ”C¯Ÿ¨qÒ JofÖ—Ö9#\*äAQ†‹L5î†ÚVSMFaŸŠ%ÑŒfMÊ)—ÆreÛ“—˜'ñ]L#§oWŸN!Çşá‘>¬Öj7$ xe³è°ìCˆÓÀ!§Õ“‘0oñ%T!,†Ã¤sÈyE k'Ø!L'“‡Y•CØ&ÔÙà°KÁ`>Çæ#¨™·¶iv<‰‡zp_OHĞ­«*§K…³uó¶`CqÂp©m"—¨Qe¨1I•’sÂ Dm<¬C¨³¾Z§™°`9¬~*¾iûõãIxÆxXxĞèTøš^xå”·«#œ\èÍÑ0AS‰ÔQ†WeÜ‡Ú¸b³[D¼rl:ı‡²BZê_JıºäX
‰ä-¼å‚·\ğgÈßß0Ch³ŒÒAJÊäàÓ&9øt–Ú&ÂÎ“ƒOgÉ ¸¿•¼†7%ŸÎ“aÛä@bÔÏÉPÈ+sCJn¨W-7ÔSn¨ğ¾Ş›pÓ6ìœ†|Âí‡"@„Â"”5qƒ@š‚jÄÃ("Ø»íZ2 ÛöÌPŒ.3ÛÌP0PàÄğÛf€¾:4«S°Mf(.Ã”€†Mf(Ğ&3ÌªÖ¸Û¦ ›ÌP±’ĞZ³–ÚµLãYvî’İLÎÉb¿Ê°K­G 0=/L#G–ä›c-Ã¡Êä°¾ağ–ŞÒÀ[øã¦ï÷–0–ŸOš3ë­07õÈùZÓx[¼^mÎZå…°¬4\Ìå5Ÿáwø„øZ<@y¾?¡µÓPsqquÉkÌ¹t
 ÁC,‡üĞ4yr4j(º³[c;"3fØSÇñ ¸KV^ôŒ
dQJa¬sƒ,/0ƒcÖK`UıÒ´A¤Çr+¸Mvá! ‚æœà,À@•P««rMpÀiÕ6‡¢MS¯€Ñå”¦¡‚¾PÚÙê©S*3÷b6Ó$[TˆÏ¦Šy¹¹“QT¸å†Å”j5ìqÂ[)hèPPIgrV$¬a$AfÒ1B#ŸjH‘v^ÛŞĞúa†S=]ÛÎNs¤ƒÍ‹"bŸÂ¥ÆEt«‡â²?‘Ml"ò•×FŠhp©Cau¨Ò°8T.m;V™y<‰¦Ê)(_zŒœ–“RåÈv¹¨ôÙ%W¢{Lú¡œA2ôW]L’âøbGãÁ¶ƒí2ÉÃ&²—`-·~Òè†Š*²³Yê?”7iÆ3#¼ú)a‘)KÂ¯L¤ìVöˆ^ï•rwø©ñŒ¯F‰zuÄËuoaúÜ·Î‡@è:EùV¤<æ|×våV † îß‰6ğ³áÊ¶kà>ÔşÜ‡Ö&¶vwõ9£|şÀÊQ»ÒÇ>§&KhıåÖÖåwP}‰cLâ·ÜM¥ú'Z!ÕÀ‘Àd+{­ÙÓë³ÇW,¶3l\¬#¶Ø3*P·QõnCc®1ïBcİÎ¬¬Y«°[_Ÿ±`×(»VnY¾],a†óy¼~t”×Ûõş×	ó=ŸmšØ¸	³†™À=†µ*İô¸‰İšíÅU;eDç}£-WÊpKF×oóéÜ—R¼ã/9Âjo(g4e !İ.NñÒ{†ÓPİ°+×9Wªd«L/I!Šò_QÄXÌnİV]ÔÿÉßbJ¼Iş÷¢ö¹ÓS§PfVÅ®Ú±Ae3É“®İ’^1Wœ35y9NF½/³i'?+ş<dslêş\ñÒÄ/8’gÜsW¬0CLY;±·Ç†NõCİ§ºM¾x×Œ˜t¯©¦)–øµÖßÈıçà—¼=f*5‹±äû5æKÈ½,†¢tô¾9LlÑô=¶¨ß/ÎÍïÈQ×Y}ãN)™™E©ñX¿_7;_aˆ³®n­çÇ}ûmúË¬#söº‡väò…•ª€Š¦XÓ|‰~œÄ2¹ÿ¢.¢Ò|¨Ë×s`yµYŸø€˜×n¸‡Ö•Ö^ãøF=ËáMQ¥`øFµ1ÖÖ6eÍ‡›Üı¼Ë¤K!°°ı´Õ#h;duMVo©x»=Ê–×`}ğ*\¡ëfr0ÁqßNl•º‹o´Ch«Õ.äh¯²qY‰wí­X{Š!L¿aL2šñnl£MQ_ºõÓxg$€3[)»DÂ×ŒCf!ù(Åœ#Ï„óE!2ô6w5–(~JŞğs.éoKk¦?ÃÄw®ßÎp–w2u:¾~jªRÆîoô6å 7Cy£ÜİÇSåÚë˜JËÚµ¶¡>.«× -¦%¥êÊÅNKç4U‰EaÔ"Yå›
ØÚú¼æäµ¬`ĞN5ìÉ*ö e{€¢ Ìƒˆâ±HšYxQ’f5'°"ëÙƒºÇÌX±"XyOÕMk¬¬g{âĞ;›§r6PupFT³}­ƒ–rigÃsm”yó\#f~¹5‚Ga›IyØ¼,¹ÜÅè>áEçµl¯ÛVÀTÍFöh&A¨¢l í .†ZˆhŸKN-ÈeûIV´-äÑaSÒ¶ĞÀLeí†L¥í†MåíŞ’Åb .*O²pZÈÍ¥j¡!—´;²Î=X“•n€~Ú:Qèß1u˜&0èå­›ÊÜ¾İJN¹}9eUût*
6×¸$+Ü¢e§Ÿûvš&"K/éª{ÎïVß:}Jôg­on¨o‹V{&ÛÁ£(q@…/º¾-äÛÅRôŸÉëÇ@oõí‰½õmÑäPÎÛ’]¯ É¹m·Á(k¥yş;§ÍiåœyÌ÷?JyÂîS©­Û±WµÜÜï¸ßËn­ÊÕËs[»>ƒmm÷|œàu%hz:Vªk“[}(ša.ÚHH°'°ãçÚ®Óv-i_8B{:è÷o†[˜`mÅÚE×»¡Ï=>v×’$‹ñ%nÅÛ¶Z#oµşŞEÇ8mÆ~5/.LÆÛ6C“z~î{ƒ›_Ñ²Z%çM·íÀ&Ş½EÆKnsUÎìÛïŠ‘÷	ÊÛš/%“*¸r3é åJGI·í¦ğütq¿n¥¢•Z?}íÛkôî·ë~µß«ó-›ú,-=±Kú9cÿîrÆ4è%Ê˜ˆ)§I˜:év)“ywñ‚2%Åµ]ÃÛRÄÁMê‚çÛv³y~âscøİO¯–´VO±Wmt¨¿M´w,ÓXÊöûæ/\şi³*MñEÏ;HV}—oÛ ÌOl|°ÉáìğX‡ö	û{± x¢x>í]ÜrÎ3Î!lí¶Ÿ-ñïë¿äıìİšjŞšîâ;>m¿SÛ‡Ãœ™_å,ÿï /™÷Ó»S\+{&c]÷hmd›}Üæ£&?¯Ãí¯l0ÁoÉBª¼â¸÷}üŠŒ‘o™¾%Hş³,ÄÓîP–=ßúñe­"û?Ä7´^3’T’=ïôÔşŸÑòÈ×CRö¬özáõàr›8éºìÚÖˆz[yüÌ‹Yåx6)®5ÿÛ.¡{²Æ4NTE‰QC´@_ËŞ2uOáèÙé–ø—•ŒmÍ%¤-‡­Ş©cD™²	LÕ	9Â¾™t~B¶]ÄÇÃ—¯Iü–ˆß–1ı¿™ÇÚc.-É–‡&˜¼§Êûrs©q„~î[–B<­Í6ÿåyˆ?vî+¿tJ{’‰=!¨­>2·¤¿8üÆbWHzlŞ‡oå·UdË]¤{õµ>$}½œG¯[¦Ub´]Èa˜ÎŸ/Èz:äMZ¡|/RÂÃœ>ÊQ95§	ŸIKwêò”íCWn1>qª~ô/·E…}¬äÅi~¹Šƒ®[O“w›T&¶Û!È+¾Ò™©¨m–S†}G2jûÆM?UĞ6:E®«õp™êK}×ŠGm4ÔY¨Ğ|OR0êUVÆlWƒC±YãäÎõö-9ŞG,ÿÆºR6ô¥£›ÿV[¸h
endstream
endobj
29 0 obj
<</Filter /FlateDecode
/Length 4525>> stream
xœí]YãÆ~×¯às Ó}@À;‡Ÿ/àÄ‚±;ÿHUõQER”¨QkŒ³ëñHŸØ]wu±ÕÅÍôgRğ÷›Y¼MNÏYçœ¦9ıvÂÏKj²^åé÷şş§éWÀİ¬\ËËw0POø÷oßOåÅï?Ÿ¾ıŞN?ÿ‡æ‹ÙNZƒÓıDˆÂKË¸ôË×Ó·¯nÊÓ×Ÿ`"âPO6Î1iã'c§¯¿œş¬”õ™¾şûàó¯ÿ˜ 0i¸5	ˆ°Š€´?‡ÖØø2$wÀ•I_¾gô6¢à\‡5³"²½b-ÊvÈZÚ®+ö87ÉM	4^™~º|qVâbe×Ü­ÙUWhƒ3
ÚqÍy×ù_áïo'­Ãğ›tô3\AßÆƒßíç 3±ïÚı	•Wbğ7Æ{—çêş—½Ø€ß»Uqã9G˜JşÆmA˜Ã¨ÙO))7ıR^GŠ~Ã×ƒ0!`£4áÇÁ:«d]
ˆ…¬L»L9˜õGœtÔf3s´FçAS ¼Œ†X7ÆV^8¬áÓPÆj£ñÂh#X©`IƒrŒjÖ¤\°2Q6ÀWö±^	üâ…À½‹©BèùõÕ§c{ó†ofLô+^ÙÌ³!”}±“¥YÒl‚ÉNğ‡˜·ğGÈX1†…À!gğ£Pb:™$ˆU9ä…ªu6x#ŒBØÎ±íª¶-cªÑßN|1(¿xRÂ@N't ëTÄ'€t ãÄâæÁÂBpÂàe¨j+*4`œL¬I‚4¨R¨œ0«êàfBõÅ^Å€ƒ°EÓòÛ^¿Ø-úµì<<%»™$ÎÉlv¿íÂ°K©{ °z8^XYRßƒlU¶ ‡õ§aBHSùó@{M)ì9ä3|¦Ï4ğ~¸¡.¨µM¸@Í	Ş,ò n•ZåÂÀYi@‹^í8-äØN¨±uZ Ğ¬Óa«´@Ø&-
ìz‘
†y¡¾*y¡¾‘y¡BÂ÷útÂKaáÏEáö] BfJ];q]‡"4YÙ"†»UD¬7ãÕ\{2©V—‰ub l•[' í:1¶J„m n•Z%Â¬JËÄ@è*1¬&zSC}-C¿–İ‡§dG“ÄÙ%™Íî¹]öp)uVG«‘CKê›ƒ-Ã±Êä¸¾¡>øÌŸyà3üçnÛÀ˜~=i¬_³aÒ9€ë+L~£SİÀxë¨CÔƒbŒM‚YÁUÚY£ãÀÛYøC (XGä^ƒŞAh‚zÒ)€N|ô†Ù¸ˆ€Ã¸Ê ‰¢>»9fĞ£hß• AN  øRV^’7ÏT^²e¬Åb„
 Ôà•Vv¶£]…oKĞÍÆÄ81!À T*	 s6ZI+û€¦Y;ækr½¦ÑU#+jnÊë ¯©™G³=˜
›NòÃVfÎÙXÂ3Ş„n‰fnëúÈÆêh‚B!ƒG[¢pm¢U	ü8éLV2¤†(2P¡gŞ …Û8Kğ€„;ˆBõh|áèM*—B€GVÖ–ıŒ@KÚ¹ûYEÑÏ"Ä–âr!Ë€j¤L„»SüLpe"ä<¯ÍB3
ë²V0
µĞøŠv¾x<¨FÍ*«81!À€g…¹£ó¨×V*÷ ú9r³&&`à3‘øi
©X¤Ôh»›UØéZ£›5‘n7ÉM·°`[xMoëIÍÉnØ…ùÍTş‡¹Ë¦%Â÷P´¥Œ±á›Ê÷³]ÛTöÀ¯÷ÀóüÖğA¢¾Àï ˜ƒŸç‚
ö
¿áµû®|c´®s¤2^CcCÁÔ—¶O=;T(è?—o;ïÛ—[–aÅ'€!9WHñ~¥BİWjà$òêíP¶6ÍÊ¢E$å×;å±.œ—5MòÄ¢åfÒæë@¹Èe‘¶ª-«É–U»èø¹Z~²Ùc}¹™Ù^EN	Î~ËåÉ^ôá;m+”Sß	‘‰^ğ{(¥ÀÛÀ×ŠÙŠ0†L¸¡¦q™­B!x)du½æ¹ª'®oñC¦wX± Ûv¡³#¶D•|ˆ-™j’mµg%rÁãËqeu…„ÑPÁkÜÛ®*Í`Q½i(_ïè[É×œ
EDP
S9ó5ç²«ë¹•Ñ›Ëgï¡N†»‹ã ëkìBâÄijÓ†J¤í>ZºdN\Ÿ(gÛ•g«2¦e×v…wªã_ê
úT¯ubn´pä0¦õBD†.ñ“=7bİ€ê)øâw¬…C¶ğ¹¹éÑ<Âµ°İûÂ_ã=k‹âÎ%ój“–îH‡®êëI¼×l/JÃPÖj@pwH§1]Ğist”în¤^ƒ¦@¦ÑYAåi_Äö{ˆd¦dj‡ô”ã%=½CGÚ‹ëá(R"¯Æï\~Hi‹÷å-(˜òuÂİÓM—ÛwİlœÉzOâú×Z¤~©}´H5Qµ"•¹;&Œwïf/ÕÏÈÍx¾ƒåÙX‡k$sxL x¹Œ3Ã¬G7e.`Ì0÷CWx—\áÛÏµ:ÕkBjqßdE%Ğîìâêó—ª¬Pç_ÍëÛØ¶Ú§²µkéQ)´ûï†µ•ÎWúMÀS•Ë7ü€ßx­×EĞ‘âeOôÈ>¶Pc}ßıÉ‹û¹úi%³ÿöq±^c¸PZ¨ºú0ùsT\9¡ò¶µ¡Äú	¿-Ìgğç©üĞõM¯êû€LÜ¬gº¯Z?d$«®÷Â ÷ø}ÓTßE©ïFÜ‹"N8’/tT‹1‡4çòÇk®ÓT5m×“8®9wSQêCúxÍuš¤9ÿÍ1‰ãš7•©>Å×\§‰šÃ•b¼æ˜ÄqÍ¥›*Ò ¶é€2 ğQîÖ¸İåÿ¥P×J¾U÷uÓ÷£Ö¾>¦¤r³@®‰Ï•¯ÀåÅµuS¨ÿõ.º¹ŞV
òw­:_§3›ƒJàøÅş¬ÜßĞù´5x%–˜ºÎòtş=qäğ‹Ò@Ûp<ı±8‚»s_µènº%áÚ-ÁCµ¸C¤÷€ÔbŸşf-†›ö´Cº¼§ı`-vê¿Õ’Ó¥“y¯ÓM[¸Qé?P‹L¿ò¡­	N®Lâøê(ÆÒ¡Ù–¾VÇhózul+œªw@b«ã¦•r÷FyÄ¾ïı	éÑ|eË4VÙ
Uïêeá*w‡R
”8âŒIìÙÏå;*)Äµ½2eg‹ø›
ô¯èkëb¿YëtŞÊ,	<Æ+ÄW˜LkˆW“º¿Å›î=Œóm#»Ìl³”‡v`:½rÙ)%·êùÕÂ)ÛÄ¡õ;><Í€«Ì-½µ?W›Ù†”Ùô º9y•“á¶`_l‘a„ÏxH÷:•İ¹œß#ïË'iÖpå¦I9{+¤|¦Oüù+GáJÛ²ÆÃ¯){Ã#|n{§3_ícÎÏUœušURYp:“]ÀT©-¸®I•£˜¦Ší!là+±ñ$\Î¯BÓáµœYKaQÖ¯…³2Ù­eŞNU6YÌG9ùµYñ@¸ÍY’Ø“¢j)bÇD¢^ûáV!û4j8Œ fã†[»SıoY£¹ ™a¹ÉŞë’ßj@—÷OUpÈ6xà³ãú<î^ª•2PöN|ĞÌ!Çl®Ë}»n÷}gÛqîùÑ>å“=ïS0j˜O%Ëlµg?Oa»Â•@=Ÿ80­iÙ6eÈ¶‘?YÄ2ê>k('ˆte© Ô]º.ûîT5¦´Yµ¶‚ìêdaÛ¼]NÎ(>ÖØÅãÀ,²Çïî\û!µ„2lmŞñ¹CÊZ¸µKBB»!ûîªwÏ Ê22Úöİ¤+JÁ(½zO%ÇˆSû®ÿTêq…ä¤[Ï•_k’R&0È5"[÷ŞÜ=«ïfÛ£m¿ôÙe7]¯÷r?–h›¯­$"U?5ñ|Äg5z!Ü—f¾¼¬{öÖ½ÅN«Z”ëVÍ××øÛK1VÒû¹¬=ÓÈ…Ö@Í,ú¸ XÓ¢°8;“D'@À©Š~ÑÃ¨›sŠZ´pf©¨õ uHöouP¶ou»Ÿ˜÷IIn¸£ª³ÍW,ÄªdÛVWØÛ¤¦¦$Ú¶ £æ§(ØìLÛ ÔPDÛaÑë(Ú¶*¶lÛê lÛâÑl¦ÂÆ’ü°U™s¶>KxÆw¶m[ÖiÛ28oq«h!¢lÚ¬ìŠŞc}ÂÉ [¶ Œ0O4¢c009è=G’íZ”İZ<¸w;	½-jÁLo l÷F+!^ïÈêzmZ]c²MËÚÒÇ”D›`Ôïä?€QcÔ²OPj¡Š¢OËÚÚ~ÅŠèlÓê lÓâÁÍ ‚D·Ô‚™nSÁ¶ğ’.ŞÖsş°6­|æ8ğ;÷±ñ6—İ6ÕµhòÙîÓwªwl)R“ø8I4äÑ­(şu«øWÙş”ËŸ{™‡Ø¡íEa„ÍA×’àæêŠÎ€£ÊØ$Oç¯…Ş¯¹P ßH3È"ØR¿ìM˜>ê×¥{Ş4‚ÈĞ*v·×d€\Ø;¸ñƒ­\ds	VŸH‡ãÛÆAÅãÃ^ ßkÍVA¶"m§j^U?-êGñéŒ#leÚ;seùFÕ÷±Ş«AÇşø×Û®ÿ£æ¾}®¦Îiv‰NûçÛ:a²èô¬),¦ 'Ünô•şqŒ/

î]P\`„ı›p&d[£E[	6İl#*¨Ú—­×DµZ—/h›ŠVëS+9îåÙŸq‚½zT—f«iÎ´v½7™İ˜±qî,T«>¯ußg¾÷¨U,¶…šß»²Á­xéu,8Ÿ„]ôŞ^Ì#Êªd;*ªJƒæUÎï5)hhÖjå2Úß_¯dÕ»?ë•áõŠĞî‘z%+Ñ9¾^Ók5´^y$ã¢^d×+Y¯B¸åÚpÚnˆzHÍ’7Ä\®Œ¶—+†•+’ç½reÄf—+Y†•+£ÃœË•óü*W$ÛiX¹"Y[®ìÓ retq¹róqåŠ´êıE(L×Ûı?Ë•”+7=L!+ñ8‚G”+<ıóàråqŒ/Ê~ØÄèrå‚ ƒá¾A'îM–m—}øşÊ‡ÉÈß†Œ¶²‘cDÁJ¿ú0“!]™T°lâfD½ë„çT¯8»VıØzÅ–|Wÿ¼×%ËJÇÃ
½r—ñK]ìÇ•,øQ®¨¼òj²ÃÒŸ®óY²< dÉ·4Øf-(ó€’…§×#ä%Ë—%“]²\`è2ícâÑî1UKŞôË`K‰–µãvXÏ/XJY§Ï<Aêş–Áa.vXÎò;j‡E°}ÿÂÖwXËƒwXö‚iÔËà;,W9¸Ã2Ôª0]rØg¹2¾\Ñ7=—-k÷°“tT®ğô#–AY®<ñE¹ât"ö¢ cË·8Ÿä99UŸ:5¢Dñ¶¯ïgpwÇ?Ua—RğÊ>‚ëûJş8Û@ƒJl­ù·tN÷«ªjDtó6Ğ@Û@ƒ“‘Ø:ËïÀm L]µÒñàm ½@·48ˆê6ĞU¾n	‹8¡æmîÀ_¼T ˆgjı°¾ºº¼òÃM‡-¯-ìîn%çuîşı»¿2ÔˆE5—{+õK9ÒcI§FÌ ì€ÿú‰Ş˜eàª:Öäªúøx`ìP\1æ_×“ïe	íÎØıP–èÏı¼g“÷lîÇnzòn6âÉ»g~ëÏ
gØşPï’QüXYÌLµ£ìÜ¿ÇriîİòÏoùÃ§öG]àS¹¦LXÛµÒ,´sD™ıi·Ÿ^{›×²æ–Okû/ü‚ƒ†
endstream
endobj
31 0 obj
<</Filter /FlateDecode
/Length 4321>> stream
xœí\Yo¹~×¯èç ÛËû ‚ Öá}Nb ?ÀÉnÈìæÿ©âUÅ¡†-Q
Ø¶ä™ê&ëúªx4»v¥cú³	øûÃÎ¾#÷(cÛ×ow¿İáue‚Ø´qûıwûÃö+ĞÍ.Üêsı7h(7üû—Ÿ¶üá÷_î~üIo¿ü;õç£Ş¤T
»û9QŞš?À­÷_î~ül¶¸}ù:JÊMûİ©ì¦ôöåÛİ…ĞöOÛ—İ9¸şåïT8Ì‘àÁ7‚‰Æ}H™ºlnÁäNŸ¾\ì¶+<“\º#u`ryÇQ•Ë&GsH}$îI®‚ÜX¼}!ÁÖàej-ôQÜ£üâåî´P\¦9áÏğ÷·;)İîğÙ¤·;ÜÁÊ•´»ƒÌzG`!£ü‰5şAïğ~}Ö
ÁD/2®÷è¡+şÚ]¡%v»Å²}+ŸµÛ3~6•a‹*F(lxÙi£e&iÒ\ªŞ&ŒÚ¾bÛ ½t‰a÷Úi¼1F¢L2ÎBb_)]hğÁ`c	W]në±Ä½öà¤Ll£0Ó*ÄLsLˆ­/w‚¸hx”ŞøPh
åÓ×;}ıòŒ_vR´;‘à¬Ğ‘u‡´hóc‡
8iVÃ¦
Ò¼óŞu:;4PÒ0ë M˜‘¤Et‘‰F;«˜WœgÈyH*ÎÍmŠ×ŸïØÍ@@ÈuŠ4°áÜ‘6¥«,f´àO'ıÆ´Ašs½‘]±Z±P´
mÌH‚®79Ò´¹qsR¶Ù9Åƒ‰£Jò0~IøĞõóóÃE½—Á§uÉ€Æ˜3H61	¹U†p¦5…B3‹˜fFZÌŞ,›gX¬6R\½û'f„°å˜êç”CÀOD¾çïyà{øÏ=13(³‹ÔÖûš$ÌŸb—vt‰•iÚx®A&
#»ì€T˜akc(=dšqàV²^&*-,OHuĞÌñ‘‰AZ"2Ñ…ĞçˆL¶8/#0"f‰ú1§‰úç‰J#,²>	¶B8“•"iEAÓ€â‹«Å!3*E,·?Å6s%òiÎÙë5gd@ğ¤‘(Ç¬‘‰ÎÄ^$Fk»¼ÔpL™xÈ™èÁ÷]ê@rÜ¸Uá;ô-|ç$^dL>¤B,¹#+É£~áÙƒnçÈjır28b›¼Ú¨ ¦:‹•f%TÍ<ş˜éy¬67ñ ne9àÄlâ{Òø4¾'ïIÃ×©‡Am€de¶İØ³Ç‘¦i/F‚ïL¿¹#`:½æİõ „}„Ÿ?
~,üH!ÌnëÀÿO™nÀ^òñ
MàöüÜÃO ZéÃºn]şŸ-<°=ôgBæü¬(÷ÁøØ‡Wmm¿Şºw%¸œvˆJH¤Œ!ô½‹¦J7D»KĞ`´ê Mï ˆ ` …ş0§µŞâ²A¸S˜#"ÆKpZH‰w# @! ,&ó®4L‡Ñì>"\áâYéù½*/}„e|.J”±“À	D$;Ğ$f Ïtä´jÔºR«á{bÜƒ…ÔÁØ \w­¬çi«“§Ú$:¤ŒHLE­Í®}j\mQIhŞf¶JD5ûV"sCãÁÆ¤a®mr34ı® ÃÁ¥î™'5´Ğ\D,6p1ªÓ„ 1] tƒ„¸×ÒïÂ£(F©Àp¬0³aª€¬ƒ™BK½ƒñ!ÂÁ¶HTÀû@£Œ¸šMD44º‹ÙšDEdyH“AŞ^y³Cv|”w;DrìäQ˜Û¬TLn…Ù“&S¯Ğ<3Dj\¨ÍfÏwÔG×0È¨\€¸QV3q€jYs—EpÈÒ° i;£*¨Š†¬jŠBKQÒ¬Öˆ O3/k]½À˜4ouâ4·2Á9Rª‚—è©À:±›½ãzş…c=å8Øã0 s”áS†”nmIÃ˜~!u‹ûš~÷èÌQ-ñ Œ)iÕ{$Öç?—Ì ´ÀüÌX–ç$Øı„2ƒ¥Pà[‡hX×â¡{q¥øRé’Å¬şp‹5–i¬õ+¬ê+¡eßı„Õ`şµï[M™Í«7[c)]R¤ÿİ*àiwÉé¶!¸R³)Fùá&l,å§Õ±ÚºOË$gQM’/q6??Âæ’ßô6,/õq¶‘â£M,—;›º~g3Éß%Ò­¾`tÛõN6Ä°fS¾‡%ÿGû¾±”÷«}O]«÷ğ=u¿f`¤@§®Ï:k5ål>ÜÙe9T²ĞÙ­kñøÎ&É—;›$?ãljÕœ½[íõ†›QÛîê.Í‘6*Âù!(èg:qÖÁ¡1Yƒ4Iÿ¸Vzôm0ú ı´Á„ñĞïÊÑ'–Îæ 'ÁÃªñïØ³x˜#¬§µÔ=Ş(R¬ƒ€°Îxø±‘"å@»)€åÒ­ËPÆ=Äº7iq?òsş`ş¹Ü£ò$¦XÜo¬ÿã¾&^——}%ú
(§v£$$.ıÌXa…ıè±‚XÊ‡Åcu-Â;ŒLòÕc“üÄXÁZM9[Ú—°¦íKTĞ>æÍøã†;ãÅá›­Nka’#=X5ÿ®›ÔıœUÜËÛÖºéa/vŞœæÜæ„“zƒÛ)¦³Öİ÷© nŒP]-z,¤d(2sL–í¡t´ÊŠá\Y³W·’„(^IÃ5E#ç9_MøKãÃ<Às®şiŞcs2^ÂÚ°t_<óp–¼ö1®x¬x«m7ï«v­Ÿc¦›Ê›C±~E¦:»ï„6³Ç‚x=Ï\.64'ıË°'¹á!gÂ¢À8dò«nK0Y¯H[0÷©Y‹8Ì	dë\é#r7’‰qÚi^3go[ÆÔûœ¼»‘»–lÆKúşš| }¨Ó1â8'`|y:Æ ıiñ"%pîëV'1Ôµø¼v’çOLô%Ãõ‰Ï³>&úôÅ[Î8ßË—Ÿœ±,~¿ŞùÄ}Í
9Ÿº~ç3Ñé-â³½V&şlô§äÄÚM¹_¿ü¦Ti \í~}xm¡û[×ïä~=.}&úÉØg-§œoo®*Ê(Ôfbk×çhÏbN;~È¹
Ñ–w ·)+©êÒˆµœ²°yiô‘öòhá%À¥e#q˜Ãm:ıÔ‹6gÔøò3Å4j¼xb·dcFâ•F§Öq¹ÖX°(ÄÃ¹ı¢°lsJ[ü6X0^ÛÍ[ıçûšZTÖ3œhéŞºà3l+!Z 9‹OSiÑÙ’·xZ-û‘YpÊ¦=r¹b8~8•°´àIOpuÉ‘l\ãO,ïëÂ‹˜\wğ"}ÒÔ„)tdK¢<Ô­^3zæøÒP&ÒóŞráÖZıWŸ5TuW?Zc¡$Ğâa‰lÎ-¥˜mÃ©¥T·–R¦ä”ºE¹Ò¦´uMr¬5)¬NœÈ‘H,æ÷&ÂÍÙTİ\Ÿà& a¹ÿ}lJu3–<?bÇç¨ëÉé¾¬ùµl¶|ÏÊü.×¾x#†:‰Ğy$ÍnŒi·V¨$¯Æìîµ‚Åª¢ycO.;6R9›ÓaÄmQğõUâ„]8a-
w˜¶[^XiWt½¢]ˆFQéóPƒ¼)já
wílÄ7§µB`*hŒÒ~‚G÷ñJˆÑj*Rê·\“kl_Ô7FF/ÂDó4¼2l#ªÇ$ 0[¾Æ ¶ˆ,aå'¬or4KH=ŞF™'cØ‚úø¦Ò2‹y9‚’yd"‡ÀdUfn¶Êµ¿0‰|‰dB®?Lä'šôˆé®ÛŒÕœÔ†5öE‚iHæÚ†	.ü¬¿>îÊağ¿ ‹Q_o´¤R«	.Ãü:jqÇXù0¥eÔÜ¿Ã˜úd’FBÃ¸TwygzxÍ5âó>‚åğÌïÚĞ‰“4Ú*:>_¬OõŠÔŒåowöBşÌë9	#nQÎ6-‹îÇ½µ¤{;~¨³}š68Ô2®õ”Œ|P¥AôÀø8gp8UŠøæà	é¥)˜@©#v …ˆĞ—:B×g°“¶G°ÛİŸf•7[Ôd:FŞUe®ˆ«ŞÒ•i!h Åå°èa~ŠSÏ@_éêqd«ó
êT…`DšÃ”óàX|‡.FF/€Fö/ñ|ÙÓPñ
ça¿ÔüLd•WCVxã]>²án#-Æ,êu¬y8‰Èxã»ñWÔƒå\4³ùSQ#ÂúÆûsˆÎÛ<:5“ªóF—¹ğ
xFò›œxŒĞ‘&]ºòNN¨ÈÁG©äºGÎg×a>ÅGYÜeƒx²Î{½(xEó&y¡… ƒ8É`ë…#öÕD}ĞcÔblİQ<w:Ø^€{atè¡"çÂ¡Èå=Å!LÆâ™÷Ê¢íRÜW€w˜†Ì‡ÉdjöæE?sı_å‡Ãã°E-Ä›RL˜šÕSa H]¼Øîº2Òò8s—süiÇÓ;ğÆĞİãéÛiKw,Ï	|t~ä,Î«=7Èº·,	Îã¹c­y“¥Î±‘Ø¦²È•åçåÔ¡í-›WLİÆMÎOTt5‰³‡Á÷¡‚ÁÂ¤o[W$:…Hd>¿/*Ò;G4+‡¦±±Ö1wu#¸Á;Äè(]qŞVÅ[ Ë:4ÔÂyÍpÕ1šê÷)&ÒôajGyáü<óöÏAÆ‰…Ø\rŠ§W,ö†0š„'ŒÈ²•ªp!=j%–G•f·Ú	ÉŸËÉ:kœ/õ–Ÿv^«ñ&¡ïzÆaY‘·<²+òÛ7ìr:ÈSßî82WŠÀ=‘õĞP•§]kÁ|ªóÔ‚…ØÕÁî0ZD^.ƒO¨=/+‚ŞEÀ‡¼¼\rNI^iX0ŠÕ3«¤®
\%vEà*‘Rk<XÉ5&+ÎÖäfEÜš~Í×ÒXØLöÜ£JÕ×*ƒ…ê ¼œÁBu‹vñp‹ÒI#%+—hŞæŠvÅ…¦ºpÈkÀQkòq!oqyÈ¯$9ùŸ4¼‚Ë"pßèÍÀbµ½"UcD÷(±˜ƒœè®¬Xj^9^ˆk•+Vh¹‚+g[Q1Vø,òškµBZkL…Ôˆ•\ãÂPq6›Š¸‘zTí­Ú—€kã%à€6‰B³p@ÃqYğpµ‚$Ô—€3Ê§ç.¼ĞR:ËJÀšïJÀ5"/ÇZW0&ÍW8Í«Lp“ªà%vş[%à`”pg¿ÃıAñ~5CÑ¥ó8·úb%ÈxŸ+OÑJ¡„<£½Ï£U{ûÕ—Q°¾?Yš•£«8
%:;ÂÚÂÑ»Úúş¤¤öõËj'ÃGßr
“”öğdåÙ•'øÌøuÓÈ.E;J{k„m}´c¼7üå¬P¹z³NAF©¶ÓUÕıTÌXÅ/¯“òªõ{;Mì™É‹Êôˆø-/"cıİô
 uR5}æ]S¸ß†£§©óÆ—¾9§ôÖ÷³4skÇ·ÍÁàõÔs Yáš7¿[	ŒNÌ›ï“x‘éw­Ö&ŒV¹%S’FE¤¢itCh9ã~í…êîèxE¸  LÇË— RX éĞ«ÑpüS?ß
endstream
endobj
33 0 obj
<</Filter /FlateDecode
/Length 4050>> stream
xœí]Û·}Ÿ¯èç jó~‚ Ö®äçÄä”ØA°2`çÿT±IÖa÷ÌvÏf4’‚•lÍô™&YU§ªx©éİÙØ\şLŠş¾›á29=gsš>}>ı~âÏKj²^åéşş§é7Âİ¬İ—Æ+j¨'şû·Ÿ¦åÍ¿~øÉN¿ş§ô³´6†»û¥ Šo]ŞĞ­ïŸN?|tS~¡Š„z²qI?;=}>ıY)ëÿ2=ıûèó§L˜´Üˆˆ°ª érZÀvÀ/MrÜÒé‡§ó‚“İf£SÉuXbVƒlïX«²m²6‡¶kàÂ—$7IO‰,^…ŞHà^nM,Kke×â®åW/c•AaâZ˜NÂ_éïï'­Ãø›tô3İ‰ ãÉ‘ös Ä™íÌÅ-ï ñ;«sÒ3…À¾[
—£ZüzÎ‘ºÂ©İ¤>ŒšiLåcœ>·mòôÌã2$‘Pqâ‚uVWÌºXÀ•é7*§§OÜ<é¨ÃÒ!uoÍ™B©b.Ø<ÒĞch¬òÜ^ÓÇ¡6Ô,h¾5ÚHlU0iO}Ñš”+R*íI—}l÷z6;’ELä¸ho?Bıê™¯fkµ“›	^ÙŒ}2˜=[g?ä4›`²CYô–ş VÆcr&×1Ú¡±ÔÉ$4*cVåû3êlğ©* qê€SÆëK³æÏ'¼Ÿ6‡°gƒË£fï›U^Ù z°)Æ 'ö#0‰ûjÅf0ó„V¥kê[Å­JK[a‹agıÂV#µ€™;m-‹ãØ~ñ|B‡i·£gõ~ÑAôØ./¸6ë„ ªC¬t+aPu{büé1V;MÔPÈŸNÿâô‘¦å?Îí}I8Deœ·¤ñ–4Ş’Æ[Ò€¤ñókºn©=d±g‘@¤Y$ØbÍ!‹0fÙ
µ`P9³Ê"Á²1ƒÅ,Â˜>FdŞ¹1‹[šY„Á¤Ã˜E)¯³Ã$÷˜E
¸d‘åmË"ËÕ˜Eı²÷‰>ã£¿wY1(ºV@` ¶n,ˆÊnT`±?Æz§
³Bã´åf]²;Ä˜E2[tE$‹ŒY„A²È*‹dc·Y„ÁMaŞ¯³H6—ñC&aL“i<“IŞd’öLÂW=“,c&i·£wõ~ÑAôÚ./¸wÓL 1Ó­…ÁÕíŠq`Ìvº0¸;±®Z‚¼%·äñ–<Ş’&W/E´¡ÕlÏ&$û*›d^Q˜é„A2é˜N$“®ÒIa“NÛ¤éb•Nrô32ğBõ?fÏd†7Ù¤€K6YŞ¶l²\ÙdÁßl}~,ã>ßd‚£*5Ä‘¨?Ä\3g3éÇİúCÈ7¢†äĞ(íùƒ¬Ò³Iqˆ!›0²É&\oh
¸ÙĞhÚ§‘AÔM
è­¶h…n74ëu6)Ø:›Ğª¸Ê&^g“lÙ¤\µlR/†lÒoï’~ÁQğZ‘W¼»ëq€&kAl‰]!‘Y¡‚[ˆ…\pÍRä-y¼%·äñ–<†äñóu¡é·1=›¬»rÔsŠîüğ;²Î¬Ëqßs‡¹VD"$—2ÉH`V:1È&4†î¥KjE4³wÆ1K:yb–aóÒÍ$òÉTN£g–ƒ‘ë_:‘¹E‚
.9"»9fZÆÌ„ç0{vA yXV#k”*‚‘‚d_ŞQ€j>©Œ¨î 6Ó”*†|a;eÈ)e0‰è³Á¤œ’ƒ	‹ÂU	‚#éHm	cB*í«e˜‹7;ÌL6›CÂŒ%Db	é ‚¸({ÖÃØYÙıŒârz(ºĞİOàwVÙî~ìç¨I9
>éÌÌ)298V˜³6İOå9z³l–¥,«w<³O†²™œâ]ƒ@C1–Øu´íŞWÁÅûBnŞ×aö¾HÉ%)7ta"í‹ÈFÃ`†çS¼å2|Nêµt0|Ë	µ­`DË”*v|>IgJ·u,­¼C¤ ¹$Õ•ç/EœD‚É7l©¯tm	ÜUI.Í2 r"µİû:Lru›c«ó8ÊÕ9GĞ—š²çü«9ßÅğ™óÉògk^™ˆìíJE_S_n¨é;–•(¿#ğáé4{OS0%|é_—Kçk¬}SäR¿µßÀ}SÂÿ¨È2J9G¯ôú@¯yùŒ_îÜ=.×¯©K<×C?±¶·µ=ÿoøË µ~ı°¼7ºëuÀdt²e^u6ª_š¸d
§ëı,‹ÙÔô¡šä¡Šk*®•Y5‚ÊkÁuU5-*ª÷]5ÇnZˆ)ßæ®/«ex
7Å(&oS--b–á£ˆÕ‚¡èúqÁ”¿…õiÆp¶Ì åÃñ-MI´jÔvlv[7jåæİÅ}}Í•7&òãè®…ÿX?Ã¶óG0îK¾ªÿ<Ô~’ŒéÃŠ°Z¾†S!¬µ«ã•«dvÙBÉPûoıEißåÌ×t;tQrä¹|ñE1ë±‹¹ŞVõæMÕ”k?¾y|:4>¹ïè-û4Ú
æÁ,a4o» èo÷º…‹nÑ²cy½EüyGKÍ€¢ê!jx¡Y©± ¦¾Q£¦S¼{À‘J{\¦ƒ!!o’˜4-\ÎÏİ8¶RşÒö4oÎÙ¥Us;$Ö¦Î4ÍÁ´¾‘œ‹}úqö2¸ó~«Ã1¯³áºû½ÿæhó[£AÊkæhhvŒ³è®áìGX">ˆá¾<®;qøÕì]Pâ¦LR˜öl"ï+Æ¸4;Fe¶÷š$úH_g’á¿±Ib°‹®‹C›W‹;‹¾tkŸkyàõ6z!Æob¯ ı¼1×ŞºÖØ9ÿkÕÄŸ‰ÔwN5wÃ)ZkÚá*[Î`Üİ°×:Ï>/ÙšSÏ~™]ùÈzW–e9]v95à‡]¼_ïlzZJu	şVMz{_[ª÷Ä¢^ğâL.@°eÙÊï²%h[—¥/	Ì{<ˆ1Ç”È¡B2"Ç§ÅÓ6àú*l¦FEdİÈ29ã6ã±ÑÛŒ7`Š‹¡ÿ–×6µ¹RÚµXÊJìÅÖ÷¶öæe¢u[B<¼ŠŒ¡B(.tmàD¸y©¡=Ö?¢ìcÍ3ÄPôf¨Ì‡\Q'¨¨H2
ÎíÄúÀXÿ J2”P0(IˆP¼hÊ¨
ÜMø<‚zcéƒ0K9«`]$Â/¿õPø ”ør„•sãuŠ™¡êÑA¬yHk!DFîP¡Y$oÏxÓ¶Úa(â«£ÁµÁÂÀÌ“b)Û÷soâ¬"?%gä&ĞŒébHXë ÔÎÄ‚qPë ĞÌ~‰	9£k c­»:&5…A.©?€R¨ m¥¨a r$p·"V:?s@²¨t–çÄõ\ŠÔÖs°*uBIş ”9ã’b)}4›T,5b…Z7F`Îİ N§Gßi
nıéëÕ6˜ûì*d¤¶³kÇ,eş¨Œ>W=níØ…‡cÙ:O•×vfˆÇÃQ®]y›×ûÿb‰¶nëËz6z³u¥çïÅ_–¿`¦½e¥·´3ñëZV†îÅ{‰º¶á†#ÜAU>Êzå¥İı-×øV¹vF’ïÑhÓ÷fĞìQù;Q!#•¬KÈ^É82e}İ*1bîs•^RÈj¨È¼¸L¼éYÕ'è¹{"£eç	ÍgÜ½ˆë#)¨œ‹•¼J–«›¹NvË?ÂQ·_È.7wENü šwGâXt·"5¸yk…]Z#/’m‰GhvŒVwİDı âÀ¦è«‹‹˜GNV×bîªæn~Âª„Ápø¨f¡Ù1"“¾†È¯X.¢ôïOoRsò¹œ„ƒ»ô¦<¯U?Ä-éq·˜Ï[µ»A}”Õé—å9ª¾¦ñ_¼G'‚#jßÜ|´}ñjî.~i+Ô¿Ğì˜3è|İı6İi¢—‘øäòûÜ(	áÆ·öÃõÓgP{eÅg]£]o¶Q(5‹¸Ì­Òı®ß–g×dtC¯½ºŒ´¸án}ê" å—àÔšà×#íï"÷öoÊõ…Ò+¸0³î*ƒõà•6_zŸëé%zÿÌAŸ•øÿÆ{9ÈH=şßmvyãê×êî/ Ê³3Ë7¡Ù1şò½*d¤Æß·³çİ³T;„ kL#G–_»)eXNun¶'Ÿ7$ígœúfšu[~7…ØÜ¿uÓBls€¶^ƒär®èZœ¡ –÷ÕQš·,®ZRºTG°¸jl/á@1Íò³ú1`mÕğCI™ˆå9ËÏ¿%c‡Êª!ÒfŒ†Â*a‰Ÿ¶²j‡°¨ÚA,©vJ’}(^‚4PæìrC9´ë7`­‚#`7Ùó Ò"I+ƒÅTÂÌLŠb1•0KZ…±˜J(3>EV°`S+‡bj±˜*­…EØBy„W‘\øÏxÏ¶˜jUrÕ± "f¥ -“h¾ÓPI%Ìóšs(ÆÑº„z4C•@ÍÏ(£¦ŠA Ø ,¡v¨ÒXÊ2†*Q)iŠØRúõ¤Fj{ZÀn1,œòá˜sy¼»B}Ë“²M«2?ıZıªIN(-íğ|a¶N3D‡°nÚA¬›JãF Ñ™„éœ‚Øè%M½­ç|µ²)ÿH»¶@Áï‡?.yZ»;éH¢ËDâúÖl;*Ào.®Ô¸í÷]¨55”t·¦ÆOT,ç_ØìÈRU«ş­¹³üø{óc¯:¨]¯MïÂ‘<¿‚âî’lÛb³c$õ¯ ¶İ‘”EM{(ªd­­Pƒ­	vıùŞéE?O*®:G¤µïËçˆ±ûUSôºtÕù5¸j?OK€ğ-%Aç[O‚ é5IšãÇùo)	Š8ßEq¯I‚ĞìIÁ½&	fÕOøûçï_Ä‡U’¼¦½?b‚¤Ú¹¨tĞéª‚»6ÊÜ3Êp÷9°Àå'1rs
Á?ö£ı†‰å‰aÚŒ)K›@+¿7Â-¿û€æÄÊò$êoƒ 66¤ìŒ=Òfùm´.{+¿Õ >;K;HM›ÕÍïJ pò*'#rùÇÚSÊ*óOÓÙür_M*|æŸö¸ßWıİ:ÑCñÖ¦`ºURT¼8J} Q.Ô9ª#Ã»Õ\‘èŠ´¨í}éN¤·å
½ŞÂ¾ŠEë™Ñ{Ñ%”C—ÿ/YB
endstream
endobj
35 0 obj
<</Filter /FlateDecode
/Length 6630>> stream
xœí][¯$·q~?¿b¸ÍûHÚ]?' Ä‚#vş?*^ŠÅæp»9Ó«³‚Ç¶äéït“Åªb5ù±šÜ”é?7ÿıÃÆ.ƒ‘[”1†Û/¿¾ııÿ®L7mE¼ıã¿ßşó_nÜlÒÁ­>—Ğ_Áƒò†ÿı?İòüõíÒ·¿ş_*ÏG}“R),î/	xkş·şøóÛ¿˜[¼ıü((I(oÚo>HeoJß~şõí_…Ğößn?ÿï›ƒ¿ÿü_7 TØføx´H@˜—!e46?	0¹ĞÏ?ßô¶)<“\º}%jWÉxÇ¾)ã#{uH½&wÌ$WAŞh¼=H`¿ş4X¹=-ô^Ü½üâëÂh¡¸0~/áßá¿“ÒmÿcnU¯,¸°’vsPFsc½¡Kaù{ìÚÊè64Ü¡C+è&z‘=z‹Šâÿ†çFÊPbÃ:·_ë…†Îö{d@ÄG*Üğ§–Ó&8]ŠnFİ~ÁÇƒôÒ¥}Ø¼¶o:QÁŒ3P¦„Î¯”® ü2ø¼„?»ò¸ÇÇ$Şêµ;0HĞ’RP£V!Ğ…`ñyÒEëë½Õ 4ÃøPAìõç/o.zºzÇ«Mƒ0ífDœ:ò2ŒÖ9ß×ï"4Å©h¸¬Zÿá­BĞ;ï]¯ A•BIÃ•… *p¥"¦Et±Ó?¢F;«¸©65Ì¦ˆU«çÇªC¼¿ñûAuÈ/Agb/‚ÑZYŠ+ò†vÒßxÃ´`ıN	z°}ÑbU˜qù¶ªU¸†²…ï,€ >?Û¬…°Ñ6[«5ğÊÉfÇ«ä8š.Şß¸ÃÔÛ¹gQ¹Ü™ÜcI^æÚØ&ŞXÓY_!-ñNEúäı©÷U2ïÔdP~yûá–ÿ‡Q£şNŒç4^Aã4^Aƒ?/Œ9Ê¸¥”à´oQÄê°‹"†İû(‚ØE£ˆÕnˆ"ˆQÁ1ŠXmÇ(‚àEt!î£Â wE˜£HşY£H¾ê£HÆ¸_R™Ü‡YıÜßIVŞ)¨U¼1ğÎFÊb½’”Ê;pÓ?ïëd*ªMkÜ@«·(‚ÑG§ıE¢‚cq:ŒQÁ!Š x'Š8»(×cAP‹°"Q$EğŠ¢H¾è£H½{•Ë½ÉÀ=–äe®mâ€5õÒïT¤OŞÿ˜êy_%3ñNMe1`ièñ
¯ ñ
¯ ñÜĞ#€(ŠxiwQÄK3DÄ†(‚àE¼ÔCAlˆ"QÄK5F‡(‚à(‚ğE˜£HşY£H¾ê£HÆ¸_R™Ü‡YıÜßIVŞ)¨U¼1ğÎFÊb½’”Ê;pÓ?ïëd*ªMkÜ@«·(‚ÑG@Æ(‚àE£HĞ"ú(‚ ÕRwJ@ğN	IÙM«p=FïL`6Ú¸.Š$¢H(¯¥é¢"õvîYT.÷Â,ƒÛG’—¹6¶‰w ÖtÖWHK¼S‘>yÿcªç}•ÌÄ;5”Å€¥¡Ç+h¼‚Æ+h¼‚ÆsC4?E‘ ºè£Haˆ"ˆQÁ1Š„à‡(‚ØETZØ>Š„àà1×Gƒ´}AğwŠğÀ&0G‘ü³F‘|ÕG‘Œu~™ÊÜE‘\ÿEHÖ®SÔVu¨) ëlUY¼WV¥v8é_î¢™ª‹
Å¦7@ƒ-Š`q}dŒ"QÁ1ŠD/Æ(‚àE¼EjÄ­Z…ë1Š xgƒğEHQ¯(Šä‹>ŠÔÛ¹gQ¹Ü³wJò2×.ïFê ¬é¬¯–x§"}òşÇTÏû*™‰wj2(‹KCWĞxWĞx§†
Š (¢¤t}Ä¢6##	uva$ ÎØÇ€a`¦fq$aÆÙ.$.ú) z˜Â$p?…Ià8…Iğ~
“ÁGÊÏGÊUG
Æ<³•É¼˜×Ï<¾ÉÊºEkëB\¬»5eµ~Ù”Êºp5@Gš­X\hV-¡#Iò‰. ú] I 8ÓK`´¦$€ú!$pH8€Ã­S+üŞ’s˜ïIk IW5”‹.ĞíkÕr;7l2t.[åå¾w= 5w–ª¥®WU}v=0©~Hš™º~]ÊÂÀÊèã7^qã7^q£ÆÇ Æ³HTØ-Ş2,Ş&l?Ià0tX¼MØ~“ÀAt\¼MàF§1	ŞOc2˜ÃHşYÃH¾êÃHÆ¸_R™Ü‡YıÜßIVŞ)¨U¼1ğÎFÊb½’”Ê;pÓ?ïëd*ªMkÜ@«·(‚ÑG@†iL÷Ó˜Ó@ã°x›Àıâmá÷>Šx·ÑMe&Aµ§2	"I)’àE’|ÑG’z;÷.*—{b–aˆ$$/sïÚ.Ş˜
XŸ!mñÎEzåı™€÷Y2ïÜdX–F!¯àñ
¯àñ
<xüùÎ'\eÈ‘¾ä{M÷)I¹Ëz÷aQığg¸=çC·ÛËY›IL°³ï‡†bœèŠÑ¹	zTĞ>%2Yv‰.ÈöåW®¼ÊXèí+2óS	ÆÓ1‚Şé‰ò<¡a4NÔ‘¿cÂï”|ôÖ×Q¿¬§Ğ1j{,®µ¥ï!ÜĞT}ÂÆÈpóCÁ¨Ê™%ÍÛ—¿“Ğ¬NwØó¹(1
¨]écq?MTõ€gæx åŸJ3l„'B|BªòÅáGœU>o`¨¦Õ6ºÎó€¯‡"T ;ù{Ê5¤'˜7#–'ØÉÅ3æ8%ná^åFö‡¹J¦Î>¯ä‹nø²9®·0hsüD×o@÷í’9ƒyªòÎ¯xQÍèZFcÏH5×â´vŞm£ğ÷­nıdÆ¢ÎôÎ³î0«üÉÎÖ5Óû<(.û{×ÙB:¶ÇTíÛÙ¦-œdVÔÔãÖë8î:û:æ!`9šÌ-u0JËÃ+ëËğêÂ÷ãÉşÏËZ2<2,™:â™½ğæoúYw½ĞhÇº¸İÄÎ3ªæÏ¶ûÛÌ7¥ƒ	ZùÃ¯ƒ	gÂŞ	3€é-ÄSÄÀ'bj3 >L$ƒÙ`Z-×ø}¸.f¶Ë€|<L˜nĞ”&0É)
 Bş_†€jÃj‚„B4›`«ŠáÔ0‚;Hßî¿%¶î!b'‡Ò§’K˜ÄÏZÆ±¬ôlÁª¦Ş;ìa®QN0*¸-“ÆÁ|,˜òı›Ø§¡0Hw–Æ!rãŠ
*‚ú¬ªªZ¨*´bMë­üf.I³d“¹Y¼µmôœ³¢)Û– o£(~Ô0]°waæ¹,»‰ À,Ôî`N«Ä©À’:à²‘Íü’›ÇYµA`&®ÉÂ/>UÀ¡‘˜X©«e 3ûäEB'òjÓAzLyAFteÃ´¼ˆ¡ğ#e+^"Ø.Ë›U0OÍOÏÌ6•Ğ³ãÀK@ [«ÃFû*3U‹!Öˆ˜K,r[¤x‚qéÎÒ8Äbâ’šœ‰ ©jÂk‚ôÈ©êfE“]:!È‚L\æÔ¬ÁKªÿ,ì²áî%ù_È» ÇÚ#;ÊDœIú|ÁÌ^¶‰ñ•A‡ùZh¢aĞ-+XºGäkù©{›õå®™ÚÔjm(ä¬o7l¿®[øÜ)T­.’ñbÕøbÆ·6½¾æ‚eEhıÕgÏè{R>îSlgµ<İpäpƒÙ{¹ğRÆÍúj·ëÄ—
¢¾ß\|ühŞ].|Ê÷*N÷í„¿Q\×J¯¤Ü¼^xcqñzªúÙcŞ1JNÛümöb:&—M¤­¶úMªî“ËìögÈåVÌ‹\~‘Ë'tøOK.Ï¦‰ÓyåGrËS…ÌIç™Ò¯$á¸Ä3ñb½rSÕnEŒ>ñõF8¸â[ºN_s_§èÇ)q¶Î}¬“æÇ"xUG©}Ÿò®8#,¯là…Ëô©i™Æ†e1¯+=dÚi™õ©_ºWªç6¼ÒT³²¦™5],:±_ZYS¦o¯y¯ÛÓˆ¼şZû<«c:ÈX–LëX=¯WşOÌÜ—íxë‡»Ãæ{®?ÁŞ˜ß`Óæ5×¬Û ŠëÖ`æÓë6íU =#ûKóQb°+ÂÉşŠq²¿b5oå7~KÒ˜ø&scì[Û8F„U]½w¦Ÿy4£ûq3…ÂgÇ÷b»¨eGøl6Ğ¢­…	Äü°ÀH)wŒ8İÏkºg43uÂ4‹2Á›éYG¿Y¤,²G5,@ÅeÉ†aróÁÉÈXˆZ›õ)-•ØåàıæÍõŞÂŸ{Ö?-‘—|Ï÷ß“ıyA¥2æ¬<âÖ»Š‰…g"[ÏšB¬~m2gú«j8Ó»MnZqJ% ¢‘CÇõÃ»O@‘QÚìŒ"àÈØ~ÜI¬ô‘ª ‚8ãO §ıÛÃUİ¼2L/ÙËÎ‚Z9xÊÇ1ÿt’ùÇl^°³ù>ó)ßgÜ‰ ä33Û*¿€Í„W´NwÅ*_èL[V-ˆ´{‚ÒÌz‹ò¤ŞŒ/zCıüğ¬îx3I„çµ‡é¸¢…ŠEí%­É©’FœßRëÁuu ó?O6]J™Vr_ëÚĞ·ı£(gç«Låì†¯SÎìög(çVÌ‹r~QÎ't¸>…›Í8—ÉİõyÚúDtê¸Sªı$§e—ÏÚ§óãëè£I­¹zg‰Ã´c™İ½ØYHö'kÎT2O!]fdçu,ëÊØ3Á•ëjÎÀMÃÕLªîx*MUÓ»@úhİSã¼!³n+?‘¼'W9ÊIT0Ã†©GPæ	Wœ{õzôúÂH§“NYÓúõ~û]†²ëª†v±NæoNŞÍ†ÓÎ<}`æéóÄòŠì•4æw0ŠPŒ“¬#/ôÀ@w2@œ«6.ŒçCéyøœhĞT_
Ì*Í=m…È¨¸µ(ôn1y¡œR­¨Q*DÖPá´/]XÇ´ûı4iy9=Ï"svbçàÑäó!’İçÌbN²KS¶fD«i¦÷YáFÉŸvüş¹Ñ·F€c°TG³Sk'¤d<{;½"œg¯çÙ+ÆÈêV#¶¹0Œo‚3º¼5±ëCyJÏæ(ÅÛÀ™v:1&rq<îà¢îiv
	Èû·öyÜÛ0¦ïÉIˆíhöuD;=É”O50;1Y˜I«ĞÌôÔ¶ÑkîPìŞºm—X/ÎRvÙ¢”ió¢gV›ÒtT®Ñb^ô$;Üƒgh‰e0dr¸‘Èâ|;œto7úšUÒ¨îNF‹3ÙÎZÙ˜ö¬|/JëÈwĞøtğœ{÷.h.w
äé³ì§‘gÙ†1 9$iÂ·/GšÎ<}PÃtÛ&´Jšµ˜4Í®Mlî'µyƒï|éî¡}ë¤;ş-Ê¶`*“ÇÇ)÷˜/CY‹#iœÊ7‹;Z@û¥Ë>íÁ¯g(;uè*hÛ/<K¶ã†‘íë¬-R´Ê¯Ôãñ[ò²å	ˆÎg=¬h¬.A\¡1ªü[iŒ*h£’g5„«Ô¿i‹3I;åÓ–¤µŸŠ–>çå¤AÇ4XîI/¯<Ç„ˆ]ûiçJKı´U -%üĞæZêdê¾¾¿ÔÁnf©£óZêx-uœĞá4%şw•Ç>«b=¯ÿûÏ÷grX“Úå—Ï5]RX¦?¿Ïóİ£ä7ùnbš>]'›.[,ûÕ6ŸñÔÇËª]Q‰1ĞÏ™¸Ê•:Ö±ÊU•
¦”`¸°×NÉ½¹i9«é„Ù?ñ ñ¦”pñ+ÀèğeDÎ»E«á,:Ú-Z	ói±cİ¢›“¢#İ ãŒ^vt×† £«¨LFl±ÚFr2¦¬6§ƒ*çGXÕÎ{ù=ÉXÏ<›U!káp1…³l
?«İ±l
ç.÷:lÍOXÏ²ˆ³líÉ¦ìVC3—¥°IİìÜZ7úÈH³ÁlD4[$b’aÏ3‘œe‹HÙÄ¼m½7¾ãØ`¼:šSlx\GŸÍJPG±U°£ØèáFTµ:£Å…iÜW»qdÔºF¥Å¶ŸFÅª²8½˜FşÉ1zM¡}wôNûĞR¿hDêË3~¢CŞ-¢i N¯ÈéµöpÕ>«‚ÌÔ	Cebsÿ¨Í|æãèµ¨ôYòãS›ªã”¾Nçij_³ ûí3½T§üÇÓú´½Nş–½‰ö|Î¦u#VªÂdJúë DTŸ•‚ÌOnø‹ÌÇ™Ë~¥vHŸ§VîŞ¢æ
RB×ÅºôÅMÀ”«	[±? ñÿ/<mòŒ¾Xù˜/œ·`š¿d»…»0Û«5Ìš´{_A¢O;Bâ †O¶ CÿPÕó-À¸²	Óy‰I¦Ò_h4ş\+t:À;omra+4~aö“ÏR;xÁ˜¯ôÓg	T'“é}…*3‰º:R‚@ÅlxãŞTqGÃC¬ÌşR§`àéF6¢Œ&mâğŒAsu²£á ‡]"ÍS<©Í0C`“ ã†	•ÂOƒ”,™@”Ê£ÉÑ81ŸĞŸ‹T2Æ°¹rÿÆ»³,ú E©¢<<óÉ†îÛ7^fe×¿ª<nÇÀ.¯g$Í2sN%nv|ßeß².óœSzw^ÅŒs’ §ˆÿÇzhÖ³Isâw¶°şiï}fêÏËùrrá=pì#s*lš?ëS²v}ËìÕ¼¸N…÷è.ŒlŞH÷½tSåÓzcùCĞxb'«}9ÅüNó}§½cÊÎR §- ñ=«DÂ¤{³?³+÷÷Ø=È´0Œø‘ò7hÆ•[Ü,g…Ï“¿§¸¼­ú¹×ï¹¨t‚ğVFÅÇO<òÂÔM.Ü¹é(ë>A}ı¬ö¹8½6t›l‹}ş?]wYnÅ<S~u±û1Áò¨qYå|:8k÷4³‚‡6Ã&GëûÅ=°õıòğpªÃõ}ŸÛNíÛmCøÆ İxÓ½»;Y¸}—åà&'ÇÚ}à#ÄåHü»è~ˆ«n1ŞÉ"Òèëj2µ?7ÈÎ3—?õ{`,tİ–p×½R~z·¿.Ÿq„õÅ©ÍÚû¬UU§Úoù{…	
»†<±%äóaa9Ué¢æYN0ºP'óWÄÁ&‡y¸L[^¯İfßNéª3“ÏSG¼]É	/g™^˜‘{¢¸ÓjT?.×ZxÓåÅNf\¢õ‡ß­/4§,Å°òÖ¿¾pG“öJ—=õp´Ñs&¨ødb9‹ùÛ§ù®;äúêÅTƒ¯5uH•´eóå *á‹iå’=ôÜÎ“ğïñ˜)åîœ3 ÇTN*Ù].ÛÄÓó K<é.=—ºğ$(—°ş¤)‚xš<U@–÷Fu°9&Ë¥#¹YÎµ¯ÃÆã¦Heï=˜eâ{1ŞÔeìÅ|ÌÓ.c/æ¡ºŒ½˜2]Æ^¼sä]Ö=Íl@µ0k1y˜]Irfjáï¹“¶îœ;¥Üƒ§”+G4±Ì=ÀòQN<%Ì•CŸxæ€ét(¹Øîä©Šğ¼½Šñ´=z²¥¿µò[¢¤¥Ô5‘[ê]kZKÑswNŸ"mu‰{!ÔÔ%î…| “äò„tôS9ÃŒ$ù(Ë÷B>K*ğÌ½¸;*]Æ^{ŠÔŞ
oöáb4K6¹oÔ†şòa9{#Ñ£"çé±œ»¶Û`_Úo]rö0C\zö;–OÛ\ş‡pÌØĞí¿ñë¾ÉXú|ï(¥N[³•#˜X3¸ÉÍv51¾,é‰Iw¿ÙõÉ›ñï	·»kwç_5UÅÍå&ú‡Ë“f¥ë€²r!WSËcİ¶¨Yß‰î×~xuÏ¾İå]mhø9¶î[%û¬ÕWwá™Ï§¹,¯æÜŞJgôñÔG'—õØènJ-.§K­õs:é”"tÏÑÉ;å†®[x~€ê½p§¹S1éÔñ">tp€ÊBÛwó†£›Ã=7Pgê åÎºû/jWÏ.Á„ë”¬ó°+í5!EÛâsyüÄâ&JÒmÊ™RFJ‡.¯Ÿràï{ÃÊ´³ƒÉCÄ´Ó
1“Lç¡Ö<éNV¢n/ÏV0u…Î¥ø±Ñúª;5ZFòƒÄı©Ñ†ú¦ŸÍë:ZbçFÓ Š]Áîäè
²££©vv4“†]ÅfÇDSë:Œ¶Ş'öŞƒ0œ¶ù(ŠR	`øæ5ü(kÀ0#>o¹E‚Št“yÀˆ­(z ˆÏå	äsy›ZÍT\šfÓ&w³}kßÏ§òÆùPœŠ­ÚÎRÄ£6»©<`è¦ò€ÉÍÄlG:CŞ@àêİT°tÀ;Dº İ)Òë‘®O¶s¤[ùíi.H;Gº‰ÜÎ‘nMkçH+¶åVI[|*o\›—Ú°©¼Aj!Â°‰É¸¼?»©< àGıT°´ùÿ/aı'xâÓyödU=«€lÔ‰BÖdB3ÿ Æ>óqÓy°N]¾Ñ-.wg©ùT_‰6½?œ~·¥Y­çfßÚÈ½”eÒˆş§ƒzi—$Vy?şP×¢
endstream
endobj
37 0 obj
<</Filter /FlateDecode
/Length 3478>> stream
xœí\ÙnåÆ}¿_Áç Óî}‚ ÍŒŸÈLbÆ€ÿrª×jRW—´(¤Yîåa/µww±(¡MÊ?‹ÄŸ‚]F«DR)Ååë·Ëïº¯m”‹q2-üûòÏ¿,¿·By4e„ù
ÕBşñÓR¾üñëå‡ŸÌòëÿòx!™E)­i¸_2"©iù‚¦ï/?|±KZîÁ@™Bµ˜ BTÚ-Ú,÷ß.•Ò¸¿-÷ÿ½xÜ¿ÿ×@Ç5`×@È@è€‘ˆ×ÇP*¦®tI°eĞÏ÷¹	­b`”+¿D¯&Ù¶X³²í²‡2kàJ‹k”ë¨–‰W¢7ø§{CË£·4kr×ôË§‰1RsbÂš˜®„¿ãÏï¥¼ğôcE¢×&¬•c36‚LŠ¦(ßX·­…»mÎ`SÅE
ˆÿ~[ch‰Ñ•>.ßÚ…qy Kş3@R\¨7Ö¨Š=>IİJ«—¯Ô=ª |Ğ‹`œ¥¦)Á…*f½Å˜
®¯µi ¾Yê¯pÛ×îº)jL€–*d¤5f4:¦
úõ× .¹ĞÚ::@°aCl ùCûúõâSèWt%ˆ	ñNšÄÇ$09ïÃ<¿OQh¯“å´è~8W‚ŸàSˆÊra¨¢\¨„™|šäO¨5Şi®ªB§–é”°¦õÒ­ÄÃ…·BâP™@oÓLÉ9U‡«ôäUX8c:høî«›ÀBèWäÕ$K˜‚h'-hd,ı‡Æ¶Æ–¶M±Ä¢STOWÙxL¿x¸p£iÍ¹uõq¹%2Üj;½Ì¼_Ü˜˜Ïtiqçêrå~ÈTÀ}¶«‹;wW,‹_/ÿ¡0—ò—¢Gû”‡Èó<ŞƒÇ{ğxŸìAê>¦Œ`±AÑ$ÂÄçhÁğ:š¶‰&n£I$Ù¬¢	a›hB 6ÒÍÑ$’h’Ÿ£	Q¹9šøH4!xM2X¢IùÚ¢I¹š£IÁ¸m–1ÍMÊüiM:­Ü9:WÜ‘˜ ¸Óua1ïìBå\ä¯VÑ¤«ŠG‡¦Ó?Hë=šdƒ˜¢	!‡œ¢IA×DD“³s4Š@éRäÑ$ƒÎ@¡LŞ­¢I†Svü.Y`Aàô¸2X=™i,ÃëhRÀMòU‹&õbŠ&½9³®1.³DN³ÚAï0ïÎs.‚á3CZÌ¹†\™r0ŸêbÎ=ËbÁ‘­È{ğxïÁã=xLÁãç½é˜å·t,tRÔIlßô!§b:bXqbŒ
Ğ$U$c&° KÄµÀöÛ®$•¬"a(ìßÅÎpÊ¤_QØ”Ã½@Á¾",Ç–é–¬	»¶
‘nDª‚ç]Â˜’t|€””i&ÎJQ5ST‘†‰Sêjg©b{˜¡”ûæue©9’	uŠ æÄ¯Q…ËJ=`CäûL}å3ƒ`4f>«<
è²€›ØFzkòe‡&Ø4CkICÅŒüaŒÑ‘!’iIyjŸox-ÊjÕ¡b_H˜fëhÓî„ŒĞÖDÊ:†$jÜÅ	1ÈÈOÈ @¯…øáF
bWğ=§£®F­LN¹&aS&„,* 6Di[¬pà‹í¾°š›ĞÍ)ÍIÕ!O³T±°4+@‘ÍÃeôDˆ‘¦M 0@ÎÑEF@ôuÌJ¶²¤€CÇ2x¨DÎ‹wtˆ"éFTAÔ…9:7‘ó9ºrfzº9íÜ(:—kKi&´;c,(_]ş£hJ;§g¯œîV$å)ámi5ğ’ñFÌ–ÎIiïğ‰•À))åÇúı®Ü·±b­­Åç§Ò–¾CEÒ~©cøÒ—pyGÿ¦ôû–í`|&³ÌÈZeí¯±å±öXÊJ{û¹²QÙ¡ëLvâ`œåOó¹/,Yl(•ÇKÓu{Ê´_9#tç³Ó!1—şºÒ@¢v}®Ú¾&Vi„—ÉÄyº/\T’M+´ôqòyH¯„:‹#ÊO½G~y…#WtBÜàk1ë3¸1¾Øƒynà>à–öcÑ)„_ŸÂuî¥´cÙ×¹«^Lši¥!gÒKqäœ¿Æ‘©ŞãkLøR>OáÈëÇb‚•7B§7z¦sW¬µ*>¶Ä¨gi9Ùƒo-
ûh×Ç¦ÜI¢	›öºIĞ ·¡è‘¼Æ°Õ<.Gu\ÿÈ?S–ÔJ«hf·²ïùjĞí^[QïÆgofÑÚº”`wÔÇ+‹kWÚf³jc·v¼¦G÷²ŠT³¹Yíã.ywK.®Î™˜ÄÊ›¯sºASã#÷5ÕU“G3§•öÆg3·Ú¾é¡ó%Ù=n¾Mæ±îŒV:écÄªÃ8L¾ÉÎ5¬é½ºÀÓr}Ûc»¯§3WÁ>Á®öù^ÌvOÉË'¢	ö¹8§æ'kğ‰}÷÷NÜ¨8y†œÊY2å12­&·÷°l³5ºî“°SæíJx7
aÎ‘ğù°„G×Æúu¨½{ôpôF4Ò‰£\‹§©•äj%~ŸZp.•Êy3uİ)æ ß°˜;qYÌgì¾&1÷á‹9;óºxlßFòz³jÄcù#±‘?ı	­Œî;¥¬Ã–r'îÃgR#:tr¬z”fœ±`Ñ²ãêÖi½Ï:´&I?SµÓ:¬ÃÖÑ‰;İ:ÆÈ/dc‚³¢º¦”5x§mD’_‰s§møíşŒC«}ßzåp–mğÓêpZSÀO~²†Ñîê!òî}äT^uØÁÑ.ÉÙ·¤¯ì]¥N»×6>ÇŸìYŒ5ÉÛÏMjû$R´f&?ç±j®tdÇ!×´$ÃÙ9HÊ·hÍÈÙ§|­ßnÈÄ}#>†®;%lÏ8VJ)‰/ñâæÑHxUŞ{šeG.[ô¶)SdEL‰R—K¨¾*$¢	<n¨+7ìçzÃHcrãFy•Æ‰ˆ¯n¼T#­ba¼,c?]»Ñˆ
ïõ²z½F‹½6iµõ…a!$§í²zá)`S­%Æº=‡ıRÉõ>:*"ºÉ kñ1È‘¸PÕ‘´VÆÚÛäÖ¶ëmtXw!'1Â}D?a],~º»«ú­Ã‘ÑØv¸Ğm	N5„ººÄ¶ücÍiRŞ“Î1,o{èôTşYÍ¼­ŞÏaù‰§ºí1˜RÕ“ïºÖT“ƒ“ Í«rT¬ /Ì¨X™Uå ò“$^İ[§Rg;•ä 5T’¦XENÆ²WÂ’ñŠœòšœ²š–>+aÔ°J™N7+©iìMP¯Æé{˜@èÃ³r`OÁğj` 1ÕšF8P§Ëeb¿Œ•ºÄ&‡ñRœòZœŒ9†ª85C©ƒî¡ûÁß#–³­ÃqˆQÕ¨XÉE4¶	ƒŠÂ
+ÆÁ	ó{Ãë=¢"X„PVŒĞá¾ãÅ8„±Zœ|ÉKq2À+qJ‡QÑ2ÆÅ/|òQ'3È5›QvÓ¸æµ8]>¼ ØõÆ²b`¸tâuAX¯òŒJq€j„zË
q åŠ,^‰S°¹§a¼‡õmâ3Œ)NJW #š[Dcnk%ß«
'ÍÀw-Gt¼J9
›îìr”'¯Ur2G¼eÅÑk”£œÍM.GYññšå('óÃËQf®^­ådx9ÊŠ£×*Ga¡p_9
£s×é3é3d:})w’h{’¦Š9—èº¿V¾q}i831ˆ;;1F^ósÉŸÖœAş§e}_r–f”û3(7AÔ‡/G>6--ÈÈ·'Õiè ëïlyI(—ˆYÌJ'=6 %Ş¬´p3òa»–ß¼™iÚ\üÍüæÑ ³+YX´ä¥
S<TJ@ÉæiJ\ô¢°v¯‹Q¢ãE„1K0jwr§Ò+/]lÊ$šC¿¨;ª0[Ù7³ÂäÇç„úJÄ¨â0²ªÛÉÁŒ=øyg£Ğ~“ÓDÂM÷ŞmŸüÃ¡‡F&÷ê&˜mğŒR‡v[8êyÚ§cÙ{n6Ágï¸†1úÎ«>*<6ô9pÚñAÉyj/$÷ç³BÙa¶¼ìq˜úxwÛg-îŒÇƒ‡`L¹“ÄplÑTéè¢Ù«±¥œ«ÌOŒÁƒªïƒ	Gb0ë¶Kş”K}e“Sî$Qo—uáL0½b¾ßh­±§kMŒ¶}ù¯ìÔ'yÏL(¤ÓdS|g÷^e³3%§àT³ósûYCÏªâ+“b+J²¿Á¥ZßÊÈÚ
ÎT*zâF§ûÌ×ŸQFwÌÃü±•Çv98F4½×GÁíTÒÓöWcômöxŞh÷"P_³¡Ïw>F'ám.—dL’k2&¶7ŒÙĞ§úŒqVD³|
ö¶WÛµ'ñ½‹³¾Ôßòõ «ŸÕ•°Ğ±q(×œÇn›ÓºFv·Òª.]’œ…}VÙm/ğ5L$ÙSâÓËYOYîÍ—©ÎXğ½îN;ÈßÉ®}õÍà˜r'‰¼IOåÿ”?Îå
endstream
endobj
39 0 obj
<</Filter /FlateDecode
/Length 3754>> stream
xœíÙn$·ñ]_ÑÏ¶Ãû ‚ +í®Ÿ“,ØÄ‚u ;ÿ¤ŠgõQ3¤Ô##€µ–5]M²î‹ìUé˜~ÿ>¬ä2¹FcX¾ıüôËŞW&ˆE[—_ÿùô÷?,ÿ¸Y¥ƒ¡>¯°½‚‰rÁıaÉ~ıéé?èå§ÿ¦õ|Ô‹”Jár?&ˆÀ¡ù}şúôÇ/f‰Ë×a¡D¡\´_}Ê.J/_~ú“Úşyùúï'÷¿şc€
{€Ù|øĞ"¿†”	 Àæ)±L^ôó×sÂAn«’ÁÊ¥Û#Q;$Ç{VSöâz`Fp”« — /D(¸Í·-÷ÙBïÉİÓ/n£…¢Äx–˜¿À¿_¤t«Ã³H½²`ÂJÚÕÁİŒõŠ&…(ò'2íƒ‘N…½kĞ
\ÀD/²E¯ÑÃ$ú˜wÂJ¬€Ó ]ËÏåB/—ïxaĞ#C‚ *,8Ài£ei]ªF-ßpz^º´ ‹«×ÖàĞÁ‰
Ì8kJp~¥t*-,Î—pÛ•é¦9‰C½ö §×T€Q«Ğ…æ+ .Z_ÇZ; ãC¢GÔß\ôíê;^­ZKÓ#ÄY¡c[Sg`´Îù†?æµÂªœŠ†ÒŠ@«á‡r…@ï¼w[¸WˆÒPa!P¨P¦Et±É_–éF;«¨ªtjˆNVµ§UƒøşDÆ#Ä!äBVN@ kCDFÛ¨ÈôÔ­ÊÆŒ°0–€VƒB‰Ğ;ëŠ‹À3‘,Àü
AßS-$ >ÏoK`£[ˆb30-Zg&ãÑíâû1š6œXW_—X"¥Xm§·›wã‹8A÷™.-â\]®Ä©
ˆÏvuçîŠ%±àÛÓ¿0Œ„%ÿ‡Ñ£~N”‘ç÷àñ{ğø=xü<N‚ÇßF« (‚@Ç«ŠÒ 0_=F“û @"A˜htæm Á 4
2ÌËÔG€–@ÁB%ZkÔÈ‘@°Qà:—k%: F¨Bş°À€L! 94D³ú(}ƒ¡’#ÈVz·™P 1
»ÁP¬Æ¡•ÙÒbÃÚpP‰>é7o¡I8i¬Rü¾…ÙÕÀì¥#	0¨8]T™ÕÂ @ÁCş¥³š`É
ºHT"É¸Ê-PqU¼}VWD_½+ÒÑÜ)î¦Ğ9;ÚZ"Z˜Øºt"§ÏùªÂ>Hd¶°-P¯A§¶IØUM‚:h@ÉG(ÎU‚ú5øŞ…>ĞeaVD‹ş	hUHƒ#¨ZZL_ºX†fÃèœM¬BÑÈ<Ä ÌvåÍjA:[lÀæjT2²iÊCø³Rmq!×vËtú.Ÿ´@VA~êÓ•÷¢AHKD CÑjQ İûbd•€ún£9VV– .“ÂàXÅ×€@N“tŸ\5BP4åmˆiŠ&dÛiìì©ZÚDC·bC™ÿ‡qk¬-¤·x©•_7© ªÁ¶ní_™ñ\Êxó~Öæ¿xm!×˜P`/¸ù ü~Éğ:^<W\©@² «˜7Q6×u/åH‹İ@¶À(KH¸´mKHˆ[‚BŞóØ,ÿrGBJèÕ‰¨wT	*•<Òl •Y¨âyLàwIÜ®¡$ÑøÃøÕZ(¼ ÍÃ½¤5óÆ:¯PÖu'¿º‹Ä*øÀê§Û·±²XÒç/^Æ¦uT—æ…2§®%ÉœĞmmªŞOªÀuÂuE/Ÿ±Pß¤a#š1;5ŞB”wgd$˜şêÏoua«!˜êä(oõ±¨êsõ>M“ û²±æ×±¢°¦îŒ“Ï]zÍXäUAn~GRÃ‘Í:An’k˜‹¸Ñ.Ûƒ~ 7AùÀ´ô\Ò”Ø^_ÂOrãÇhÇ@s®ıR¼X”Äû|¡†¬â2Ç‘.ŞãJLø’ÿ^Â‘Sç1áNètZm'¼Y¡)·ó•‡ú™
Ja—‹›Óˆ{•4¡r?k0ËõŞµMG9H"t’Sãƒ¸ÇR­ä‹å÷ªúJAÃTÈAµ‘\Ë*³¥Òçs‰/¥$¢¥TsEŒ7àæ:ÛP˜k<lœ«§¼¢–²Ï3õŞóUL'õ¡ŸÊ…a	Â«ê¹3¾j_kißkñfh1_‘„µ¨G¨3 }ìvn·î*ƒ+©ÎÒ®ãRƒk¤¾—Áu„58ëfîLÌ_¶gjmo>kdLM¨)KÌ¤RÕkızÖÄèî•¶$gÂÎ˜úÚüYß­Ì¾¦¿Õ'ì~É×ÉThOıÈ^X+(9¡0ÔöÅõÙ­ñ^¶ZhĞQmµ ÛüRãÎ;ßÉ…:u#¶½¥ì
_nÒ&ERÆ«ß½üë(I´såŸ÷bÖVJ4I®Tîåˆğ »Q›¶ü¾ì»i8,™×–„ª1‡øî6æ*Î æ
Œ ü„UØ­[ »ı¸éâÅøò Û£!»³8•i—TPóƒ#¤ŒiÇÌ%ßàìzªå»Ç¸ıXŒ¶“1Hv˜K’xø6£åç›ŒA²Õ)èÍÚéd’miiµİ|dYÙ#ö°;[MÑñ»ø]pgÕ!Š¼~¦øÍÇ,æ{ê¸/v/Z_@I¹òà*ú¸o7wT	õ@÷H^{¯´¿PûHDàÊßO½èNx*¬Î¯=ÉK_Ÿˆmæ”4_éi…ş½Æ¹––†HlÌbÛÅ©…‰ËF›¨¬FñR$•|óŠ=Rİ·£;	C$!gÒúÃÔïq¤FÑ]|¤¶çäÔ®æˆ©í9z‡#µË¹Á#µ=ïx¤v5?äHmÇÕ{©]Í9RÛsôNGjFÔè„+ÔŒĞï²ÑIÔÎ‰#5JéX–±W´3ı0Ayi1j„7.F	C6s4wİ±œèbí¤MËu.UEÔWEÔ{UÔ¢÷7WEÜï±«"±pEÊÖam\œjr”Çîò‚6ÇH-÷b)ÇÉ2èNá§ñp]^½ÏœØ+vñáb¥MÊF„1qÚÖ$¿¥Qmş[‹ûşL*!íqµ½ÉoYlÉÍµ­Z”ÙKï×ßôgîd’î=0ğ`ÒÛù,!¥“ş˜×‚éâ°œÜµw@‹²5=éœ°f±šbƒ¼¸*:@Ak­ìwt½£]ˆFõ×¥M®íêµŠ"W»*¯C´ª¿#móKåÖ²ßÛ½zmÖ „áFo{«:W`nU>DÜßQòÈ@Egl¿¡'!F«	Y¶NXè)‹¹Ÿ—`“ÒFkÜ ,aå ·¡£úH±1nt©”X»B:‰^è„—
;…KùZ3Õ›*—è ªÅp"±ı½à»+†òëb%ãˆ½JÎ^_¡Ö*7Š	NŒ%+±n´•‹§F‘@^ñIıŞ«¯J`1¥x¡4Ù+Ğ—µz ËËn,¡4
"
ÅX’¢ŒS¨YOfÔ¥ ²lMŸ%‹·¼ÁVÉIºBĞ“IåÁÑë3'6ÖGC£ñ‰TC,nÂ4¾¥u2C
©;ï%'AGãÈk=Ù²Äœå6§á[´:œKq‹¯]îâ` «†PO-JÒÂ%p°·vp˜ í^GÀ²p®¹LCÙ
)Và.şlWƒ™$9¹ñÜRUÅr°Îğ`vo¢/ÄeÙ‘— 7ğµËhî‹êSc´Æƒ²
-p“å`O'¢’çê+sDa?¾-Ô5xîÿz¬Â§ÕWâ!¾	#…6M°"d©âØ`WbEÈê››aËŒ]ÀTó„øñË»6Å™Î†oıQèÂA@0áœ?|½ıGĞñúÍKØßEQùƒN!/or¹ó q5ÉÅ}%œşX66Ñsƒœ¥ŠAãN~€sêN'¹ä„\OÕ›Ò€%©ºd>³Ê +XÏ6_oH>V£ŒúcqË	„¬b§ÍÇA³~}Àë‘ob]j*b#Jà^¼ÁÑ8[ç½ƒ&ºhUf¶\'FÂwÆ¸‹GôñbŸÇÁ'æËSÁíªT·Çj³ª”Ï¼\ÅÈ-%?¾”&¸‡ÔË¤¦¡âŒ+Jùªf,÷ƒ&ê<®²`C!_¦³KMWÄóåÜ¼yQ1²å“Ã4UeäDT¬Dî6.ã]ÇÛMÅb¸AK,qòDw\IueLe“ÆtÆóQqh¹¶œ¬nXh{Ã…7ßXP­Šç–8TŸ½¢°áÄ[;ü^£è=c¢TX<i‹›/ûùlâš/!¦;!–óW”¿ÓBäóé4ïB«éğ3æƒ› ÈÌ×ÉêÍÓ+Šï{HîÔ‡º>Ã«ƒßšOÜ%HnG>]ñ;u4è‡’–«¦ù	ìæèl]>¿åÇ)‰+øæ÷çÙ~EA÷ğé“{œßW˜®Şx­N—³CA’ë!Æöxş¯¶ªÆº^ßÎbª`TÎ+Â†‚Ë[sk™CÕÃ›ÂÊ¼Mw(¼§Î
ğşÉäÎèÄ›Ø»»S3ÜÕ7¢ 3sòşşÀÄ:ÏÆ}QRu]ªÚ="åOƒ™útÄc[`cv…Â*= 1æ¨Bcá†>©¼ƒF+
€Ğ˜yq|( TSŒ'æş©D*ˆÕä)%(–f¡âŞ~¿â×>ÛCÁ}ÄÜˆ_o,¹ñ\Ä!í¶Ã+¸÷$ñÂ¸q'0l7;“‚pRÇy| F“–Qk‰#f5
ª21`!¬HZş	›}Ş
Y7„Å™a«i´DÖOR2tØ«×âSş)3&Ôl·ùĞêÀ&ıh—á,§ØD*‰ÏœÊü¾g*¾zj)PZ¹ÏJşßù;
endstream
endobj
41 0 obj
<</Filter /FlateDecode
/Length 3702>> stream
xœí]Û·}Ÿ¯èç fx¿ A íJòsù %v¬Øù U¼{†Ûlg¥I–ÔSİ,Ö½Øœ5“*Ä_‡ß?1òÑkÁ‚ÁoŸ¿\~¿à}©=ß”áaûãß—şiûèš	ºÄ¡ÿÅ†¿ÿşó–.şøõòçŸÕöëÿ"?Ô&„”Èî—Háøhº€GŸ>]şüQoaûô0ŠÅ¦s^H³Iµ}úrùçÊüuûôß‹…ûŸşµAú=Aï	.\%(	~ÌCˆHP•`ÒP	:1ığé6p“Â;‚\Øı$r7Éõû¥\Ù‹C¨=ağÄ¹ôbó ñú
}4h¹æjwŸ¿FqIÁ¸=˜ª„¿Áïß/BXfñ—ŞŠ^0a)³À£™±bhR8Eº"Ã~ÒÚkÅ`ğ¡=Kğ OÍ‚NôowM’3˜ÒXé¶/ùƒ6*l/øA£CúHñ€Éoø€UZ‰LSÚ[$ÚÀe}k¹}Æá^8aCğe4>øP¦i«§ ß—R"\i/à¶ÍÃ-³uÊš2Ñä)aF%}ÈDëƒÁñĞãÊ³€u€ËĞÎ":D¹ü|±ÁÕO/ø‰) ÓFŠ5\Ê‰ÁXëúùmğLZ4ÅŠD£à]uÎö°!0BSa!Qxé©P‘¦x°¡“?Rµ²FRUE"èT"­h=+ñr!Ï#Å!6Â9­ˆHÆˆÌ.á*
„»,,hŸ
!áÚf)fÇ%yeÉFšğÂR-D¢â>¯‹d­LÒXVl"BÖ‰ªŸ¢ñ¨úáåBŒ¦>N¬«ñ%–H1«mx›y×uG "h>Ó¤Eœ«É•ø!UñÙ¦.âÜM±$|¾üÃˆßÒ=Êu< <ˆ<?‚Çàñ#xü7‚Ç?nÕ¹^‰µM_«q h€—+ë\&ƒpTh5–IØ©2ÁšFW™.µ	N´êZL5ó:
Ñè>ó‡‚.€'ìk@â„„ÜÈE· =µ£xê™yğ>ˆLIå–>ûp
XŸ·×hG1©7Lƒa;;ƒ*äux% Ô!&“˜f­±1.OmQ „“~Î«0”6p¸<ı!ƒUÜë‰^õàÆy	´`ıi9%û!$€@Œ6FX¬VÃ?aœÃeGŒd^ÍÖX†ëÊ|ÄŠ Òœûf"¹‘½a¶TèÚO88ed¸*hqÊ
wh§dHç²»~·¯ôõàNvÛü¢IĞgwÇkï¬3ã!¬±P†J™É˜Õ0çx?Rîy)î6Ü>ùic·ªËFdvN€û4n"ĞLp<‘pU–r°Hk÷‹NP?9EÄR|ZbçÔ„u·”«<n <(ß-e†øS^‹„î¹¼m-]:·K ı®ĞÄkİ—í³}0¦£7(2«>Jx Ğ¹•ê¶ıÒ <2ßóÉva-1ïç‹†âlÊ.+HÈ
åŒ°A«i(ª[O5«ÖÙÈOëhhÊ£„ª‹”?ò˜ÓyeŸå4“ä'}ş(H+ì«Rå¬`‡VöM+ĞQZçvcÓ?~ÏW #wZÚ×ÆğH­‹&;ı§ğ0ÎRÑz;QãvÔa¦xÖ(æ.½Ò"¬³gZ»|Ei8,ƒh[cï[ùé
°‹ÎÎ4;Ukß§§  w3ŒìPVÔXVÔ=èä]B4z¢^ÃéiŒjXMMt”ıF¨Ä»t#n‘Á:HA<òÁ¹Û%­¡ùĞ‚tF§[­±GŠÍµğAEãy®h¤ÍX@d©uÎtİ]ò¤*=h~@ö¶ÑvUÜù’æ[îäA“Ù ë§q£z>íæ^Ü…°ÜO°ZW«Õ(‰óè0ÒŸ®ÄÏ[È¨º·£øüÖİ¸b¤ë0~xxâjC†À$Ìá»“{ÃŒÙÕ
Ï¯G*…gZâiœİéíÎ±ø¿~»S	(oôÌ®æÉ­õ…åúyyœ6Ç¯xÕ0’à0RCÜá–›Ö0½ª·Ÿ¯[<Ê¤5¶5ÚaÊòG^}\^=ım5Ï¦—óidá+±a†ÛÎ¸>8/öoh­¨eÎ{¹1ë¥Ş˜6>\¹"–ÂŞ¬ĞsıûŒ1	‚ ÑãP;(
ÄšèÚŠ÷7h<æ?x/óĞºİ76}×®Íƒ|—é¾À‚şÔÄ8yÌpûí"¼„Ü+¬İ@k<ŞùBˆ&Ó^*Mo 'æ!‰iĞ3{¤9¦Aø 6¯™ğh`q _ûo˜ÒÒ
 j‘\@øx|!MÁ¿8ƒUã¼™‚n‚f.Àó…†G'$áÚs@ÁÖšÂ_ÆºBğĞ!‘ (4EŠh‚qç(k#´,ƒ86Óª°^z¢dÊ@¥Û&A_ ³TĞŒHç™*p J«íÖ–iŞáq¦*†L3QªE^•ˆŠ*bm£›øÛ,MQOSiCŞTßVxÃnğpš”äxâÚÆ[Öd“jD›ğ¥£)¥ğ7¸@ñşÓ[ÇRÀå¡“t ,ã£2àÚáùË°1Ï|qà„U‚Y•”	(p’ 3	ÍÉÁª<×u˜tŠŞñ–Î‚¹€ú:Òaü’Â…€ë2tY™æêòãØL«rz¹´Á@ÖB¡=”I ‚]A„%p0¤ÃİxÌªÇ×‚ H“WiñtNĞ"–*¨H U”dT‘8a^UÓÁ¨J$€©U”…][J1¢ùÓÏ_§¿ğ†õ²;_$n”nÚª/krx-áøC
¿PÕ%Zñã¿¹QÁ$Û\fğ`†dWï‰5É\!ò'W©wiˆD}Û4³Øo+°@w=ëVÖŞl*€^|İ¬ÀğHä2]®İ	r»9„V<ûö0ì`.à¹©y&ØİìRöšÁhŒ096|È—~~…«äLåöŠ°ÍÎÆW˜ÙÌ\yÑıÈÁ;ƒ;QGänrŒşËqC¡cÄŞ¼7V–Kpƒ°™‹ß#ê¦èwjn“¢	!ÃÔÁ°°C=£Z`Æƒ5šäG1ôè¢ô OAÄn'CÄòı9AÅéÂãŒgİ¶é&á)~îy°³ï+E6DËSdcÍ?NšI9§E†ÎÉÕú·¶ä6å$DïŞÔ’ëtsğ·ç¯ßÕû^,¹!ZnÉõ±H	G†ÍÉ´vz3+nSNB´ê-­¸M7	Ï_§fŒ`P¸û=ZÁ6¶ƒÈ×óš,ùƒKÿ˜µd³–TŞ¡
ùÅä³˜>fQ¬*‹e®¼)1yÉ‰óÆM±²1æšÑEMfíQVÖ:1Ñw¶¤ü–ÎSëĞX¯n{ò{7‚İ/ÒoQoƒşœ“éÚ8*ñKMù}YFXQ+Ç„;	­ìŞ°SÙ«xIã›h‚Ô›¨ ;}eIïÒŞôoˆÆµ=i~Øb„Ğ&#
)m”G¦¢ÒL>A¬R«+½9¬+KL€~YŞ£6(“Ğİu¸$»O…ƒ4é6ÑãµÈ¢Ê¢Œ"Â0ï›ãõsz)ÔñpyŒoU…)UÅŠp«â÷s³‘‡sµpætº2•BÍjy.ZªE¹”wLS|H&%ÈgRÿĞ÷pWĞ%ß#ÃæBò÷G½…~)4eĞ¼Ö·!;šÈåısvÒüfµ:ÿn1M¾Ì(§6üVöÆlym¼§HÃC.°o»9’WŞÛ£ r¤ K”¤I“BB”sGÄô¼FL*»)q3;3²‚ĞK«ù´¶4#D¾$4EÅæİÛÆz½ı8ü±²_@Mİ<K-ŸĞ¹‹½–ê*£ÉÍ2g4A,2õaiŞ*¢­øÚŞº·Áç©ıh¬Ñ£{Ûxå%Qé}Ûğ)I.ø÷,i‚oÍV_“4a$}$e!»A“ò•§Ú¢<Y`®”»²Å5‚×:}®ç­9­n4ÕİBú«Ø/e]oå(e_Š€»³«Æ"À§ØôøÌ»Ò.¥–*šÒ’ÖIÛr´lû.Õàø¹½aÛE´ÒY–ÎU“.4·iøo­ŸJªÌ‘0òà»B˜1|nlÙ(FÕÄñE-t®²^î=÷ô’š×@Õ¾Û nÇ¨ŞjH2émù”êÿÎŞ D«ß Ö9.D±/=.ô äí¸E¾ø¸Ğc°“ãBûÚãB·¡ß}\ˆ²}Ğq¡¥ÈÛq¡=òåÇ…–ânÇ…v¸q\ˆN±²kŒûş×«x«<ºÛMõşŠ¼Å-Û‹n.iÉ¯èWVçíe>·&µ†«qëŠ Dæm2tRÂz¼Õ÷í%¬×Ê%nœß¯ƒN[2Á’T…Y°äªÊzÎ:0å~¡´»âÈâ£¬£‚KßMZ{Êƒ²Ç¸zôÚVâwÏJø¶§¶ÚŒğ3[mÇbNPW[t‘G¹DÔ]Ğòãı¶{y|§›}Ş‹;“j|&äWªuO ¼2}·»÷J2^²' Å Û¯qÊò äC6¤;YWy	^_7GyåWĞİ”,ãı§V¬èüö+ò¤ñ|PĞ¬(¡>ƒ<:8YŞœ˜İQ|Õ‘%©ÏºW×wÉäÜƒóÈl­i‡jU¡ûá9P“éæ¤eî:»»—àá	HäÚÔ“P=£Ø"iº|[É+#ww_—¼I#Ù®±Ÿ”Y0÷ªw$Ç™Z¨Ze8×‹à—cO=¯¦¿Ÿ7ôùÛ½ÙC¼€†·}r©F~+‡mSOBuw—ZgáÆJ'fç6ù$ØÀ—F—;ÍièuëQ
÷tº“,kNšOçN1Ğ³oKÄrd:ş¿Òîf[æ¤X¤ÿâhƒÑ`ãsø?—‘
endstream
endobj
43 0 obj
<</Filter /FlateDecode
/Length 5192>> stream
xœí]Ûä¶}Ÿ¯èç –y¿ A ïìŒŸ/pbÁ®;ÿ¤Š×¢Ô5»5ã3k¯İ}Z$ëÎ")•¥cúsğÏ7ùŒ\¢Œ1\~üòğëş®LmE¼üöÏ‡¿ÿéòàf‘.õ¹‡ñ4”üçoß_ò‡ß~~øö{}ùù?©?õEJ¥°»Ÿ"ğÒü.ığéáÛgs‰—O?AG‰ByÑ~ñA*{QúòéËÃŸ…Ğö/—Oÿ~pğû§\ Pa˜5àà Eß‡”	Ğ°¹Il€É>}ºN8ÈmQ2xB¹tëAÔjíkV¶MÖâz0Wp”« /$^ˆŞP_nZî­…^“»¦_¼LŒŠã×Ä4%üşùõAJ·8üc.E¯,˜°’vqĞG7c½ IáùiöX½‹†Ö»­ÀLô"[ô=tEÿí¶ ô¡ÄcZ§üåKùb¬—ÏøÅ G†„ *\ğ§–Ó&8]ª](ŒºüˆÍƒôÒåÁu´5xiŒàD3Î@Ÿœ_)]Aød°½„Ÿ]iî ™“x©×ôTÀ ±O#jb]ˆÛ+ .Z_¯ºQ	È†ñ¡‚èõã.úöí3~[4Ó/FÄY¡#íÁhóãø.†E9¥A«áå
Aï¼w£ \ŒDi¨°”A*TÄ´ˆ.òGÔhgUUA§†è±ªõÜ¬Äçr="(y!='Ğ™8‘Àh­,İezE!Œ%Ğ‚ö©Ÿ]‘bÀØ.Ë«H6a2HGµ@-Bnß4–`£mÖXQlaÚIªOß’ñèöåó1šv9±®Ş/±DJ±ÚNo7ïÆq*‚î3]ZÄ¹º\‰RŸíê"ÎİKbÁÿÂ0.ù_Œõs
< <ˆ<ïÁã=x¼÷àq%xü0‘ƒ”<&÷à„u-šØ¨ÃM *œ§Ñ$aÚø‘…‘c4Ô­£IÂÖÑ$›h¨İD“®£I]«h’`‹ 5Œ¦hR>–hR¾Ñ¤`Ô6[ŸÔÉøÔæ­Ô9WÔ‘ˆ ¨Ó5aïlB¥ÜåO}¾©ŠF‡ªÓ?Pë-š$ƒ¢	" 1D“]	ŒÖŒÑP”6MhµÔT	ô û1š ÖÑ$aëh’@-ü*š$Øhãh4É`&é[&åËMÚåÄºz¿Ä)Äj;½İ¼_Ä¨ºÏtiçêr%~HU@|¶«‹8wW,‰3©È{ğxïÁã=xÁãæTÄ+Õ£‰“RÑ¹&	[G“n¢	 jh4IØ:š$pMœqM¸&	ÜF“¯£IS4)K4)ß†hR0j›­OjÇd|jóVê+êHD Ôéš°ˆw6¡RGîò§>ßTE£CÕi¨õM’AÑ%	ªT
)õI ô(H®AÙO˜_‡@!ø;¦’O0„±4~d,µÚ®ÆòeˆírbO­[bz„ b¥ÔnÍ‰bó„çîM8Ä‹š‰¿i×lz!.\ÕGü}&İxïâ=@üˆñ\~y >%êá’/äû7
/ûÜ“È†•…¡ŒB†‚8b Á³H%#ZŸ¤¬À) ÖÀ§`!íÂ˜‚äP2€ªLÁìóÑ,>JßATft‹•ŞÑæ ‚íDaé@ âù"(q JirD§$ ˜<ÍSVG0›UEPfŸ‡ï¹Q¼ôş½ÇŞ£0„ï!Fgş
Õ>$šƒ¾töÀr–ãª
€b­Â*ªª
µ@]ô½ï®%JEWh§·k¾ó5ÚZZ‘xÂ™´ûB¾ƒÌ„HEÔbCÚ^·‹@A‘Á€ŞÖ/•MVŸº"ºDôDÁSm©@´ŒV…|)E¦©Gw#å€¤ìb³¢‚¢yˆ A˜¡åÍbAÃP
D`T6#B•i)+ÕÀÁJ”×ú"’Ô¶ (´Ï½™·©QîªôïmêÄÒIñ¸ĞPQJ
ÕŞ&š]³°çÓImÚm‚ğ¶	§‰¬b@M“-i[u@†hÚˆiŠ%diìvS­iâØyÁcïüŒ˜H_5¥Ss‰ÇÃ¹¹ÁUºµçƒs~k­æş/á/Ä|ñ¾?Á_S~3ù;şÔdLÁßïà3şß÷öø»xNî·4à„sªÔ)«t°Ÿ©ëÁóõ{,	p“şˆ}dY–¡xšh{Ut;üè€V¨³Ø[ÇÄ`E½UI±Yó‰ôÚŞÕ(d^´R:ÖAÚ”¹Ó÷éóbr‹a¸ƒä½¹~±EHVŒ‡ÿš˜<qÕ[—¸~!*ıºb9–°ï
Ëh»•%õ…¢¾çŒK´BÓiÓàa¢w2ä(±Æöhƒ`U¼¦ˆÙ<·şÄ ¦oÅJèáÈG4¬ŸÚğ&)`Óh–Òåí£5È!­¾FE¹Åê>Ñluƒ.CŒ*'Ú&>>Â"m”ã„e•ù– –®1EîfÏÜÊï23˜¨(Áí»ÜÖ8ÜÎ0OL(^Ù<ûç jt¤oıº·©Ñ\Àm¦a´8;Ş?	m5Ø–#74fæäü6øãu8k’jH¤¨«ıPîa\p5ç¢íwPÊÒBAG^úİ¹˜ëë½†‹4ØN‘åz 4zX'í¶(7ŒB®¨%I¹›iµåEX ÓjWÚV! Ôw@zyF€…9,z¼&]eE[X AWFíòÀiÔVæ|À5ÿkÜ>Ze„ÕœİoàÄà‰ÛÜŞ‹•ÑC>
^ãâFi¡£Rk³¿òC(ò
¡íÖ¬¹nª2¢ÛØñ•!¸ØMNJë	QMwÊh°¿®<®Å÷ä‹Š,è¼=À†ÕŒÉ6#°v7‘y,²5™{ßÔf¾¾ŸûÓ'cy@"\óÄıÀµÏ…?c®;Æ†o†=V¬=³ìÍ›©\ê“wxÀ´/±ÄNÓÄ»ÛëZš(#G/©ĞKºëk·É`¸|…AÈXBØïjšóA†>‡">V5AØæµm¶2ºâÜo";ø´µQ·´d’‚¤9"ôÁıL lpá…×ß]Øç…¯hbÇ–Œ¤ø°JãN c<q
§üávğ>UóFÅòq( |ğ6Âò1ßkn–{å\@\u’pNç^{İ”€4ö€H¦½ŸÕùüà¬ÏsÊ +Nì¼HXƒ›ìåI³LÖÔÕ¿şXÙƒ¨àÕ4e~œN_ø‰ŸK.ø‚º¬§ù›†ÕyÀH”Èn†û‚Î[ğ™,Ë—ÙLÍ+œåïCé
.ôÇ«‰b	IĞL6v«%Ù¤2D¸7Ä&Çå©åLav‘À['»*dç?6†œ7]ó3Í«Dh>ŠIÕô4~l5Ä…2oT7d¦÷…‹!ç9Ã¢(‡çŞÑ{feHç¿[drbâÏú +÷ùÚ-AëDXóYù¼
ß$s|SSÄ€x ÷“ğ3Ï§ZVQ¼•|W[D¨éãaıéĞšuˆÇóÈZn;l|)5uºÒñd:króò p<(Û·ÁÙ}2~ˆûBÂ}‰ØÁõÃ7˜&Úá¢[óše—ì\î6;ô[°=ŸİO¯Úø±ßà(ƒ§ê4<oÛë{–n[Îç	Üós›ŞŸ¹YuŞÆßbzco~Ÿœµvó‡K—YÍ¹µ6½ÆÉyÉä//]oßÍç¥;	ÏL^:ïÓ:ÿÃG¥ZlëøÙV)ñ #§»I;«ß\6´Û'÷æ3fû<Ï)ô,x~cˆİchšNxÎËR¸ Í²O'öÇöù¥y‡6eTo³…<{Ô}æJà÷L2ßà~™ƒë¬!a?€Ÿ^¢ß¥Lo»+ÉZ…¶×=»ap~S•û|fzâöËôMºŠÄÙÕ$÷Xg?V¯¯3èè62=ù±‡v‹¹é½İõ'ˆ˜	Ïà´KÍS5o_g–ûûçüŞtÚx×ms@ˆ_óm/'šA´Ç›>¯±ë–É¢ÌÍŒ’õ~ñÈŒ1¿kÊZ—ğqû}óCÌß¨8¶ÛWpL”<”XqrºoSáĞÍçİa0İÓ™Iùô‚j~÷Xônë˜µ¨#¿«@ÏEÎ7™—Î;M›ŸLX‘°ÁsU0îºØl5q~ˆÏì.mİéÚcˆª°¾)‡µµù;iæ÷¦Ÿø£¬1çoİƒg2ØxÏûİğ	ŞÌ¼}Ş˜7iQM?Z2oêü>Äü\=-ÛoÒgîw˜ß
ß_=«½y˜x[té	ï*O|LÛòÄ%d~;u>ëá…=í~ƒg©øğú;ÎD'>–õ‘úöÛšµ·ãøTŒ9‚`×¯¿%ÍËƒ%âÀSËI½»w°N½½Õ‹KNéÅ™uXÏC«íƒè
¼Óç)½UO‚º,¸S¢ß€ü“î9£ô‘ÔI²ÈŸ->îñ‰ÿ¢=Å/ñs­º@}êŸÂOõ:”H°,FÊ¢| ıá½Ÿô(ısé?”6íQzæM@×™‰²Ğ©ú;¾’Æ…{&ôÓV÷'Ş"6ö¦ïeÿ*Wóáò]±)ûôöw7Ûô}Rÿ[Û}ó'Šóó¯>º%fËø ãy;$óÏLŞp—wGÛümA7Ê°g/ó7½ÎcEafˆ‰Ó×3@Ï4ŞñÊáËüQÊ¡§çÎŠ¾Æsœ+÷›í?ÉyK¡R%Ë/´Z©ô|ÚK„•®‰¤\)@€úTÂ´ÖÁLA‚hÍP¬P,èj%©U
˜HC÷â›¢•JH+•6°WüìcôÚ ”š^E´Óİ«6ö(‹V)mû<‚ +)U
"Ô£¤Ğ"¿øª(îR9şÊ_ÂB® YQ°±^iiÅÒŞº« Ò•Eééjí”wíw¯ØÎ¶r©Q³ê ô¾’JA,Œ5Ô/W(N“‚˜€Y,V/&i5)^
˜ÂªÕ­
ghÕÒÑ’¥µY+üIún%B"Z1QBn+:Ú¹juI÷´Xi“­X
 ™Ê'×A ƒìFiJüÅ÷(kª„
«“`<©X
â¤XiúJ+•&€–)ÍªœI—M!ÃàMu„Lj•­}ü~eJñ¡íº‡5å®/J±¦4s‹ÓÚ&Õª{.Õ—ú·7ôo'úŸ\\SúëB[[—WÊÛ9|LªMØ%{¬&.†Ê³\¥¨`+Õi
ÕR¬o¥½ROÊ^¯÷yˆ~-ÖpKÿ_¯5ÉÔ„jGWÊ?¾l!Æ ÅdÉX¯]+ñø¦Úº®–Ut"T²Š£*Se‘T±ÕrÁµ0*}ƒ‰~Ğ(tVv+CY~¯U>ÓçµÁ8¢&'zÙbsORjëTI“RÈƒêTIÒ‰Pˆf¥€y˜ƒ†¬0X€ÕY) f‰aÈJ–¬£§X¢YiiVÚ@’Üµ1HH¨!	c£›$–?Šµ¹³ƒ–äV„<Ü–¤¥€Ádí‡´ÔbIzuÒR@=°eIKm*h)IK6¦¥¤iioİuĞGéÚ¢ôt½vÊ»ş;‡W¬g›–ÚšÑÓ´TéÑSPÃâ¤'7ò£ Ğìz¤!IŠÑš—è¡Ÿ!/Ì¥—ô¤« 43­MM[Ëâõş{2H	éic'¹§—µ‡ê–ÊwĞöe`o`\ŒÓ†$§ [ªXg´Ó0*´’S@Añ¹qaÏb­{eÒkª26VÓ¯MSIÛ*û>BÓÑ@JÓ&!šÚGenk3¿[ªê¤9Zfã/Î‚˜ÄäÉºêÜYš”&ôÔªĞÃtüQ´ªĞBïÌ½òöí••1:•úë”´CÙ†lŠo~YÁ£8R">€[È†!’¦JÊ;PÓ„µ¤¿¦{˜àuÙšš–úX²•tx6|éDPçBæ	ª¾©à)ç¨ÂaÖ,ÕRûpòã½<8ÕT8r¡c1ìïŠhk‰ó3¸Ñ*nE÷<xömühã8~tOè’vKn}?FnMánİ|ÏT‰ +^jÙyQtôt_<õŠ1øz.ï6İ¸ËñÛçî§§0³À–¡»5c}7®h¦LI3ezš×8é®XÛ™Û]¶šP_}@©=v•:a&Iá¸¾Áô0\¯Ûı±Õ¿ÔÔ6ŒS­Ú#ÇÀ-ow9ÆÔÆp–¯aİÌíî(7·¡ÚÍ+g°§ï>e´°PËÛ)´lÙÜy®ëî3'ÑQ»4&÷N¤¾GÎ™WZ‡+4‡x÷­Nví8õ^+§¥ÿZí¹“öz	a“‘Ã)–LRÂ‘WK;4âmEwÖ2/e›%÷ İ¯Wyõ=ä@ù=<å:O®“Y“Ö÷ÏéšƒÛÏiÇ²êŞ@º!Ò®u}ĞG´£NNHH‰$> @)TJ1²õÜjUÛíÒñ„W9íëóµ^yD†8+^Ş†È›)y¯†|Ä[J²ouqîë»´0‹ÉÇ„©ŞŞ•—µg,`¥QrsBá1ˆsI¹‘»IùsçğÜ|öDÒÜ·³´	Ëõğ…„Të;ÏÇŠ×W¬‘°]£Å»Ğû¯"Iq1Ó’Ó¯˜:¦W=·  ÖŞ ƒ“Rw¢£p±ïÓíLa	ÅÉ;kÍD'«½ÔôÃ¿«äÕ×í•ƒ¿İÛá°¯Ÿ<ÓóÙö9Ô>ö¦oëÁbòò›°5Íş÷¯
endstream
endobj
45 0 obj
<</Filter /FlateDecode
/Length 4262>> stream
xœíÙÇí}¾¢Ÿ¨]÷V»Z?'cÁÊ€ÿBÖEVõ=šš±ìhå•¦9İÅ›E²ªË«Ò1ı,ş¼[Ùe0r2Æ°|ú|øõ€ß+Ä¢­ˆËoÿ:üó/Ë/ 7«tp«Ï#ôWğ \ğÏ?¾_ò‡ß~>|÷½^~şoÏG½H©÷S‚¼5€[ß<|÷j–¸|ü	JÊEûÕ©ì¢ôòñóá¯Bhû·åã¾ÿøã F€>|h‘ áôR&€n ›‰`ò >'ä¶*<£\º‰lïYÙ>2ŠCêpâS”« — /Do(x:ÿ4h™z$w¤_œ'FÅ‰ñ#1M	‡?¿¤t«Ã³HoW=IÊ‚!+iW#‘1ëåOìáwV*oÖİe³Và&z‘íz†âÃs[ Œ¡Ä
8½Rnù\.øÇò†ı2$ˆ¢ü‚78m´,0m|º(T»Q¹|ÂÇƒôÒåÅêµ1xkŒàJfœ	‹’”ÒŸ>/ák—+!H¼Õkò,À -Œ© £V! Áâó
¨‹Ö×{-Š€‚…ˆ~Q?~:¸èÛÕ^­ˆ¡›â,¨“‰ÀhQ:~ÃªœŠ†ÓŠ@«á‡s…@ï¼w½ \Œ`:J.,Ê *Â´ˆ.vòG¨ÑÎ*®ª¦S„U­çÇªA¼Øıq,lÜªT
,Z[†Ê´Ğ£0ÆS‚Yİ±Ÿ`Ş¹"¾")€†…‰¯q`.ù²«’ˆ]˜*3,âˆõ¹d.º]¼˜™´Û™=µa™é1˜•6RÉš7ÌæÏäM8Ì‹š™¿1i3×lza.\ÕÇüıÓáß*Â’ÿÃQ?§àZ‚èò-@|ßÄÿm€øáŠ\¢ä#e„ }‹^…!b ­Ë-YÍĞõ uÕ€¢m«…K$ è^t½¥^yt+³tZğè¦×—GW}¤HP‹X¸ø(ÊÇ(ÊU(
¬³Á2dg­	yèÃD#³³ıÂNç%•íÎŠ|¸×%)šŞ=Ã‘ Q4–Îß‹[D<> úûø 1> hŒÛÄ‡ Ã&> lŒó.ñ!€œ¹áz¶ãC‚µø€W->ä‹>>ÔÛ¹Õa¹½Ü2+©Ì€‘näÄ3ó†*î4UˆÜ½HÚÜ«^¸Ãõ1ï¾*ø¾…ƒoáàÏ~¸®²ür nV%º¾µnUØùÌ ï¢J-Å[»Õ+‰´ 0
²©hh"˜U*øA H’k¤PbWT¿‹øÖ6€‡Ù··ID&HÌd
?šÕGé95İj¥ïî H3
Ë‘{rğuG˜Ò„‹‰=c€Éû<g·VÑ¤
˜äøÖCÓ¨À€«8UÊ: Õk™™- T®!&­œL­à~!¡TXL²®$(ª°
›'­R §ˆtM´“QÇ¬
í-N	l§ÉÆ¢®²Åô]ˆ±Yƒ¬6‘ ‹2¢®2n,NRhKeÑàà#X¸Ì>Şˆ^P¨	lb
³h1>¼ÜKó”nöV€ÙŞ\¬öÖÀhoâG¦»…ÄÓ!SŞ­F%{ãt)Şo¥êxÀÙCbXaÌ˜çrIÏ0	ñí@ @¯Á`)Ó0Ì­Â*NÀüB1·J?·z™Ì­2ª¬3ÀàH2!†IİÌ­B¢&kö|Õ	CÓ´×ÔÍHçÖSY<bQÕÚ®èğ®`ªq°X‰)£aTg¥Vµ„ñL×¬6X»c-Ÿ»Õà<d*LÀ67üû~_á÷à ƒH•¾ã÷ˆ÷å>„?ç1ü+^ó÷V–ïàÒ˜2.ük`ò¸é»ïµ?×&ùŠíôüN:Èd©Ë0[Ş4LY@q‹C÷ş”H@ÈE$ºúLä5–+&_gÒé~0Úô|¡a¢(÷IYDiò=IÄ¡ˆğ}ã3§y¯ÖO‰&g„Ó‹ÂM	"Ï*\/"]$S¹Ârı²õTkÁqšx
ñ$Ñªòâ}¾ &H1 öoXÙ¥]+ëòLBÿÊ”¡ù
ŒX™œ q¢w2	ÉùcL8ëI@w4_L]{{Ì÷,‰;M÷X0”/Tö¾
H«uOò>Úº»×k™_»Ió¸L,î‰W›ûo4ª<.T;¬©ZÂ}W­'=ã^ï7%pÚ¢ëgDkV¡eDú.:)jğ›àÿ
éCcÉ`¦”vJt×gØº9"N€ŒÕS‘ı‡,?ñ4Yv„ùKy€úÄ(™¬ºçB—d‰[Mr¸Ü¤}İkç_Æ6î?ê3WšV¦ğcäÖnÖÁ^‰´)WtóÂ‚`‰íÓtcBİP3];Jã)Ëb˜ÈÄÒ5Lwëõ
î/·ŒÌ!:Šn`'.Î×aÕ%­dôì‹¬*>*ãâĞû[#”á5«"îyÂĞ½Ş¯0«¨a½çâ‚Ğy2”>ë>©Jxa³|ÍÊx¶~7Å`Ñœ¥“2é=©¦°ÏrMøÃ[nc!Åõ’•%2U‰†j–ãÔ¨sX'¬70ä%AåJ¡gæeÀÌ
‰‹Ù• “–Ü„Ğ¸KMÙ…İP·ÏG\ë’+4;û¦3éÇä{ó±VÍ¹r3ZÄÃ{&©¼xf:¶ŒjO¤ßjéóáO:÷=cÅmçµ·™DÃ+İ“Æ|a6•Æ¿¤ëÁŠrHbİ©†àxù2|µ+D&:ÇÔx²zƒ0&Jh¼²¥ÕDyM1ÿÑ\iKÏ\špµ¤áºî˜v˜*U5ÛçT×ÏÕÀ›12>SÔÖ*ˆ1lÜ±2|J¾AM#bm§(ÔuoôƒæÑ}­†	s,ïÖ{wŸc€ o{œ·Î°©¶,™gÏÊ53l×/ã’¦niÎ^rÕ4)y9JxŸÁ9Åî˜ÁLËÛq‡§ª6á>µKÙUÉ wzJpGAßT¿ójLmZ„ò%Q]?¿]9Ñ¼Rwõê	Àíö`6«ˆ9#e"ÛgA¡¶‰­²U½…9ˆák§Øf„„ã©OmÎÍ:	'›yÆçOÍ*6#ÍÕ‘œ6\×ZşÌ³±w×~”n¥c(o$pâ)éBÏÉ}{…^­[ffÇVƒÛÓÊÈĞÔÄYå PëÁæ„bû¶qxÏz­£\÷9ŒìkÂlu„nJ¨÷²ªÂ61Gˆ!«±ê ÖZ'Obg'ûz[©ÎXô
Öp¬²g8-úE¯Pâ«,ç,}ãÂ²ÁHİ'2ßU‰_×"÷E.B7u‘«çâA‹\éìE®A+Yäš¨¾È5èæQ‹\“µÃ¹í<`‘k¢jø"×U3}«¤íÅ%0œ©}éÎ1j÷ÅİØzG5™¨é-+‰º—1æNM…ùôusº¥»å»Es£A‘¶Ø¡›ZÛºãMÍ:
êlËŒèÒ*E©»½'cô1»¬0ÊÚ¶;i¼ŸÊ6¯Êqt«cË-YİZº®Ï\[Ş£ â{&j¯|ıcå„l8#ìB¢õé¶äóÄ·"nSğ{qÑ3%:eà$LŸU÷ŸUƒøn —E×¶–rä»üËo3
’7%iİ“iÈgyïgÏRZóKQüÍ¹m…â9ÃëÆvÚ†Ü9éùÚG
EA|©î\u´PªÁtFòb!›-‹>L”{T
¤Ä+&iU8QÈÈ¼_éäE]‡gèn/|Ë“.î[:Q…ÃÑN)œ>ÁÑ}‹'}Ìn/Ÿt(™ÿ¨{¦è¬Ä™­õàQ†îW<áš³H-¾™šI{ø©”´=!—kíåºÉÙÕæUNí¾ğ«Âµá×şáWuû’0#yŸIBïæ×sB15Mê›Js‚£»š•ö2ç[é”@Â)~î9µ¤rq¶nŒ3ÇKz³Îej»§ïÜ*`xêH—ş…B‚ñÚR¨ÔíÉ¬7œ7+·ÈqÔ¤Ç²\\Seps8qqÁde4”Ã¶ôaÕ#û‚¶»v‘aOÎ,åùRaæ1·}d|İ“ÉDÓ*¹³ÕÏéê©ß<yi
Æm¡5éqWµ.½­uy® ,ˆ|ĞfÃB];C¡Zï‹¬°¼P¼^÷ÎlOW-jÏn¸¸óşN&Ö}j¢õî;]­îE×okïk]İË'·1‘quuûKvöê~¾İú…¢cÜÏr–@ı†LïşíAL¼;ÕÑÎ>»eç¢HfÄwOi‘µ“£îª§ç×DæCÚ„nj{£çâaí†vv{cĞË£ÚõÃÚƒzÕŞ˜¬ÖŞ´óˆöÆDÍäöÆ•ÂÛ„öªö£v_øuòÚğû{´7ˆÌ‡·7õÔöFÏÑƒÚéìöÆÀÏcÚuÃÛä…·7¸v®ho°Ç¦´7dxÈ.á®½A8g¶7zNÒŞ ”W´7û‚v¼zIpGĞÖŞØ‘Ÿ_\OY‘-·-û{ş/:V(İeÀèêÖ„p<ÂÍm÷•âù©¶¯ØJvjX*Åº7
}Şí²‰¬GéHÆmËN=¯¬è¢n¯óˆwO;*Ó,Z÷a=‘€»@q6ŸĞÇ UÎdG=zW«<?ş`ax&;<Ò+·mTwø'@HF‰ ‘y¥s+ŒüIP~î'AÙ©™;^“ÑÃâl”³;‡FÇ”äöÖCıª­±ìÀO€w(Ïü4`"ğ„İŸ L.Hvàg‚;ğ³Âú?	Êü¤çI„‡tÆ)"íídÄã1+ÚøiL=’ø©<;0•Cõš²¤S ½•x¬¦æçEzƒ;™MwØ' =©©ØYŸ sY&ì¤Êã'}”ôÉ§s2	¨É	¢³7‰t:£³qH‡yz:-• $6~Ä'@±œöšñ	0dxNI]dëCwÄ'@#ˆ5SeèC†ñYaıŸåG|²ç«&š¦² ¦\F:·—Êâú]ø„H°éÇÛ>6ÖÖÜ®-½×#÷šêáõU³c/bVxÙ}Éûüí$vÌèÉy¥ÒÉØíıqÉr+èÍÁK/Tf™éq¬b;Ğğ:U…rû]Êd»÷×Ïâ±fÀ£Ñ<âáßMÙ~(­nïõrZvåˆ¸‘òªû#ïÃîÉ)ô™|"É½tÂ©°£Ğ'2ö‘m$?ü÷Æ"ÂûÖQaì`h3A2A•ó¿[+!íÒ‰Yê<ä“XÂ÷©HïRM« p«eWë.3ĞâŞf@P~µ'0Kfhq?38ÉF[Ašj
RõH/Ä‚rÊ[§Ô]F`â½€0Øa2˜n&ŞÏN²‘Ş~˜Â
”åU%î’úe´µyÃµ¹Kû.Ü[û„}Çˆ¶=_û.ÜOû'Ù¨ËfsØaªt»÷m¥¹#ŸÊÜit—o Ìq0	šoÁßÏîÌ†Ã	ÕEßÇQ¹*yGêaôWØ
endstream
endobj
47 0 obj
<</Filter /FlateDecode
/Length 5015>> stream
xœí]Ûnä¸Ñ¾÷Sôõ¬"I °csd€ÿ6'Ş IŞHÕMK´Õ“™]Ï¬g»?I¬s‘‹ô"Uˆ.+ııa¯^‹%ˆüå§ŸşõÀ×¥öëE™5\şı—‡ÿÿ¿Ë?	×‹°t«K-ôßèAqá¿üı%}ø÷ß~ó{uùÛb{.¨‹RrsÈÊ·¦të§/¿yÖ—pùòWj(r(.Ê-Îi.R]¾üüğÛuUæw—/ÿx°tıËŸ/H¿ôppPkü¸!" *`Ò#¡:5úùËmÆIo‹ŞçÂn‰È‘ë;¶¢\?²U‡P[`pÇˆséÅÅ“Æ3ÓW|zıi²r{zU[v·ü¯¯3£V‰Ì¸-3Õ ¿ÿzÂ.–ÿè‹pf¡Ö±$9²f±ÔRsfµ°c1¡ô	şÁhVº_ì»µ¤@ĞÁ­É¯—à¨)ü—»©¹.DÓyå.?—/ÒËËÑ—>"‚™ºğVi%2¦tÄlXe½¤½üÄO{á„Mí­‹S’ï)CÚª‹ÿRª‚‘›Ò³‚®Ùô¨ôŒæûœr¤ÉŒyA˜\V­¤³>–ÄU0®Üi˜Š$î½v¾`åãO6¸úí…¿-J	İnfÄ–«5ÉX0ÖºJÜÇ–ü"­ØdÌ(úâ0æ¬sÅ¶!¯H¡A?Œ	/}Õ¢ZƒEßZä‡µ²FVËøx'›Pƒ+6NOó¿<àı„.Ø,C67[`,“›ÊœzµpA3df”œ1g‹ŞŠ<éõHß¹áNãŒÉvÕ6Œ³´`Ä3]cf¥ª_^Ğ;ÊíèE¥Yô·Æ zfa˜¥A'o2C4å`Ğ%bx5mc »`ÀfóAtÿôğwNş’şã|P>ÇTBV¢\ò‘>ÒÁG:ø•¤ƒ?MŒòX#µà…mùÁÓ@¶ÏøÛæ‡ˆmòCÄ®ò¡~“"´ÉÛäÂH#Áb~ˆØ&?D,…(X6¢›ü°˜òÇœò·.?d|°6	Ş
ÄÁ¯+›àûUˆ’&6„SÕO‹ºªEOĞ7rµÄ{µ`ÎÑÆ5?Dówù‘M~ˆĞ&?Dl›¼ÊÛä‡ˆ]åB»üÀß·ù!bWù!¢›ü°’â·’ò—.?ÔÛÑ‹J³èoôÌÂ*80KƒNŞd†h(ÊÁ )JÄğjÚÆ@,vÁ€Íæƒè.|¤ƒtğ‘~ñéàÍÃ…°ÂtÂó›>?ğPv›S‰­* cix‹¢ò šÂ †¶ù±m~Î_åÆHäÎ^Œ]M'"ºÍKù!},ù!}ëóCÂĞK“è­8úua}¿ˆƒQRÅÆp*ú¨+ZÄğlúÆ@.–Áx/,m\óC4—Ùä‡mòCÄ¶ùÀ«ü±M~ˆ˜#ºüÑ#ºê’0n•!µº>EDTG%U#&¬¤ˆø­¤ˆü¥Kõvp¤Ú,¸0 ÎY8m.\åWÉ[LTAèTUBÎ!«u l‹!ÆgIá#)|$…_IRøÓÜÊÈåŸd×EAºœïüà´×‹r‚†Q/ÖÛ…=%zÜVá#Hãn·rÈëEHúÃ)$¬,”ğ†/­ 41±zKJ1Î$ĞJ±2H
Ó‰~Sša¶q°‹Îbò0~5HŒ@^©£§/©VR-ùH@X|ÉçPÔ,j‰Ïg”øÒÃäHÄ¾4ZªEÒ„Á[êE³7%q³“Ù´"ßhÂhjÄÅ²b
DTxQ#ÀlÆ¢rh¢ˆ5;vŒ5“ƒÍ9@Ü›şÅ®ÊÎ'W^T¶ñ¢4Õùüƒ6¡:ÂVPœ´¯ô˜-gù2¡Ú%9v>K¦ãUÑRdp(BiÒGNÊ¤†ßÊÈ—-{PÕù2˜œ&Ùù*ÌÎç(øUwMH§C*êˆIgI…Ñù/î:Hc²“ûÁi„Í˜C½Äç3Z|yh-LN¤,dZ†…&œ”9_‚rØb/ëÆv³+î³âóYXÂ8 |t¾¢˜F75L|U•cÅ6@ªZ±çªZ%@Gª²Şò®âzÂ/K§8Kóh«GÚ<,®j“Q)ºq][Ç4LnQÖÉñ§¬i/šå'…T*Ñ}/×m;Wq(#CóıÏÓàï•Êa”„7H‰§„Ê.*¬Ü/½&†~<KJ€.ğÛ ÜsWpã±`–XåÑ[sç©d}¨’¸“õP›~¾‡õ[ÆùÖŠqë7r3ÖßÖ¼ìYŸş½³õV›¦ÿRÙ÷°~%uëÅˆ9ÀÒ;I$¹ª[ÚÛó)¨7öZùY¹U÷vƒFô§H_šõ¦îá•ÔÜ`(›?~6ñÒªé­Ó÷sÜ‚&VäBõlìº…6·ŒpÌ-h,tg·hXŸ’töùÄPêÜ¢’ºƒ[Å0ò®ÀÃd$ºë4gfÕÆ¨GœÀÒ8û¾N X{"ióëéNĞHïc1b^¸KN »ù}wğ¹¹7ï!wë½İ¡Qà®6çUš½ŞÁ*©;¸ÃPŒ¯ã`§CvU!ßo×û)ëcÉ?w¿sùşØÉš4Úæ9Wì$>åL+3 ~J÷ê§¤eöÒø9×ª5èõù–ç^6+¤2\¦	ÑÄgÍu¥wW„¨ıu}ÜÑ¦Zù-™ˆsàñ˜‚ıÎŒº™zfHŸgÍ•Ğ¼ÂÜDİ	ó}¡1ûÃõìdWĞMx<f57±rF}£	‘¦¢ñZl÷½FŒëƒi.ÙD¸KBSqêŠÔcşÙÓ²ÒvÑ©3‡§ÙÆÉïŞ6NŞs¨ÔÙ¦‘z<dÊ/4Nñéæf.ˆïŞ0AÜ0Laá$ã„Åê4ØrÏï”¢3\ØÎhªr}÷GåëöT;H**^+¯KÏrM³Ú…Zóe_¥ÅHj«]’‰l±WÈ(Š€*lM7?,¢FŸ,şšß	ÆÏ,µÜñ}kÜ"­ÙôPÈxQFûK«d‰íÄ£²Œ/(Û3ñµ¦Ÿıœ¬W-^,© ÍüÌÔÌpÏ½¸¬Å‹¥›¨¬W†W2DÄº8#hâ×6Ïš´ßVÈ…ØÆˆvEŒ®èÏ¥5-L0ºíÕiÛlXœÕÁ(¸Tb
«àÚ¦Sı4À}gò/ˆI¾ êVäD×Q€»`Ù²ê¸d$X/¶rs ›`ÛFeœqÁ‰¶S¹l ¥ü¦BPf«§«–´‘6YfM@ŠÚ
í/‰6È;œ¯™Òftá1sk´AÊ}1²¦,×+a¿µ,4LÈíÓ€ÄPŒ±
GJÑ~sKn	.¸ÿ)KmÙÂ‡}š¢.-Ø w=j¬ñ!‰ScÚ#—2y;éƒ.Hí+)Ä
½OcèÏCG˜ÖÈĞÕĞÿ½·åèÿèƒŞûÛMusÈ±©.ğu8@§›B‹-n+İ«J:9FO—ueÉ°a…'jä“Ø#r”3x<Õ=1P¯6­îŞôTâX»Cv‹¯›5SƒGvÌæÆ_’pÃ‚h{ çü„—DcĞùõFô+²““ƒîáSC“İ
{ç¡©½;àˆÓubx›ö˜c›åJãµÉ¼§„Çø8ÁıXhn¤õ«è†Ó¡^èXNÂ ìT8€ó*<ÓsGæ¼·3*Õ¡uï$={`(‰)Ïhs[ã'¦¼c£¶áØbº©±)M‰óLcåáª8º=2Ú‰1?|™Ææ£ŒnM¾F#¡‘ÁçGŸ£™Ñ¨Ãšæy™hŞ‡S©óü¿ã‰Íë
{ıÖ^.yå¹åŠÚN”Øòåáè‚úáõd¤V®Oï…µX—‡nş]~2œŒ‚yL;3~%55!86K?/YM‡ùØçæ'aóóúÙÔZë:¨Î{r¢n‡=àH¼nPìÌ;Şu>J¡Ã>h¶ÓzC7>øÕäq?V½ğXF#†ˆP³¦4úSfŠt“£ñ¸w4\Ÿ#ŒG¾ó“‡ãÎÀĞ•ÚÓïÚæû¹ñ¨fÚÕFa1öœC3X÷€™ï®ŞğÖu¨ÛaSÃW¾Ãœ3/à(;‹“ŠóŞ‰Îwìó:ÇÇÔ§ç!³ë•ÈÔ°»š~C}LU~0:ôBæíMz>Ô±êÆï8†ïàŞ3¡÷ëêv—™f;ö±sGÕÃÄ¶ûŠÿpâş®rË0bÄS1êÛ7\K>·ävû­…7¼(ëûíÖ„
Öl¶¦Ÿ°8¨›t½ö‹[ƒì6[JîS¨û~½¦.bu‹pÅp£uCqŸuCar!»™Øø\9‡ÒEÀÊšÀÖMk/=*yÙÍÁşjÂ4Mu%îú&Œ¬á”èvWJÒ„xzP‘Prá›YãöØ¢‹‚…nkuCqgu{¾¢Ñi&CšqïÍšŒ·|èzOµ,[¾»-Õ‚¬Vü«C‰û©	Q‹Rl‘¶×;ÁGxÜMM"ó¡UAÂfjÂèª‰‡0ÖMÀÃ­ÔÅÔğ|Û„Üè´ıÊÈPÛÚÜXo{ ‹€m³tUn¡nJÃÔ„úÅk‰¨Ir>#‘Âäâù¨Ü>M(9ˆ‡L		ã´àì.Xè6O7÷NÃóÅ@¦Z¬c¨ÚXGo)"Şğ ÿÙ¶i¿Z]__­©$&@ÉAåj´X2#Óõºc˜£r%Z-¨ú”ÊhJ™lüÿºÖrRYÄNi¿B«F:ôœJå<µ”Gæç2¥¢.ŞûUNÏíùmÕ“)íäj§XNô´nkXnT;)i¦m ÊCÕN~õµª6W3±KYdªš*û`ªRTXŠµJİZ,Ìª‰E…Y¼Zã–ÍÛ*Å…¢öâGjUA‚c‹u»/J÷œşyãx8ãcéZ¼§l_]›¨­âQOĞ~©{jÚ©Õ~œÃm4öÜ®íÃ6)ú©{ŠeÜz©SN•×y¡×âpïˆíCjß˜
Õ_èí«oÏi,á³'6Ñš*¾^åŞ­)I[ÖË¸ØYš‰EBoxşMÎ^æßËï­¦‹¿¿§š_°ÛIv5¯ŸÖáıWìÆrâ‹­CËñÇæ±'.rOWwWQ¨eyWäÍ¢A#8OÇª_J5Õ˜Æ¡Õ¬CUzãâ¨ñ¾æÀ¨Adv1»Åx49Ú¼§èÌŠ˜¡ßõÊtîMà«%ºöº¦|' Ì‘Ê¥ƒyu5Vû×Î{UZá‚á¡"Ïapn8óŞ3¶í°„nŞÆYf”LÆÔç_¡*1µëàµmçq8ò!ú[_!Î¯Æ6U+'ôÙçmeø¥¦Gˆ£àü°gz§Á™WÃ<2šŒ–ÍÏ[ü6÷Í|ÅÉÓµÃ¢­Qeû†£ì9&ÍÖáŸ8œ'‹CÓ§#cĞİÑŞÌtzhókî|çW£OÜ›4ìß Åéª§ùqëø‰é)óÓù˜šß©2Ş2_Sö}Möö„ñ~sç½¼,ÖK}Yhn›Ö—®Àºãüº@:2ë)Iò1¿zk]è¨k4°ëœ_õ—5¡[ù0gúñéGãbI¾^?øó«ï•Ëº’N§'ÄwÓoÛîİÕp›ñÎ®Ş@Z«×u­Ù*³8—~­BY“¶|\3‰ƒ«×V©eõº/8 T,>–-Ôåp«òB5,œWŠ…eûBÖ÷¨¨œCÅ@•°Ãêú~C›Ş^z4qn â€OoàÃĞ±â€`Ñô½«8`÷â#ÖTW[5T¬¯8h(V´ç›%f3ä¨Y·ñŞ¼ ÉxË‹®+(Q˜âa°Šl­,†¨	Kñ×Ôui>›ÁQPà
¶5fñNw'¸¨ÉkËå"°vn¡„¤­³ÛVb+òíù¶rßè´5~d¨U4Ö[Õ@±ÕTe`ÕASVÏ2WPu@X<ô9ÒÁÇóÑûªBãIêXu@X:ˆª†UÅªx¾˜ÈT›uUëëè1EÄ^ô–ª£œºğ¯÷  ô[ìXåjç]ÕåìÚÿ¼ıHÒ»Ì'¿ 	8JE2‹ù™Ø—qëWà‘3¡ı¸°éZ§T::]Š
ÂÚ-¤¦sv+OÁ®DŞğ¯l!ıSw!Ù|åÈÆ`Ê©º(ô'\€~ïI­Ğp+ÏÛ?Âñ¶Şwœü‰Í—õûÎ¿Öød·½Â“†Ÿ J­ürÍù¡å{§¶Á²úÕÁR•Ë7ÿ)DP£É=ØÀË™5ôò4Ì:ç´<î/„I~ÕXÛ+²à*-úì´xHë7Îc{§û¦vÛqb¥HbS„guõ+ù´ª®"èŸ¯•DÛ¢'¨giÇ;A…Q‰8)Kã@ŞäA÷ÕÑPï‰êKµõ)½Î¸æU;qíMéx›1GBƒ…|ò"<Æ¢®'\¡7ëS_mW†{w¦Ä}:ÓÖş7Ô™‚Ğçv¦­á©Îô–^õí¿zŸ4¿µ>X›é3P‹‡´n§N&öÚ¿~2ñ;­C³İ*‰Ç#…Pë²ü^à9Ç|ÓHHúf­]»ğ/H¿';¤g³¾o¼ş†¢‘ìÿL€vQ
endstream
endobj
49 0 obj
<</Filter /FlateDecode
/Length 4144>> stream
xœí]Û·}ß¯èç ¢y'XÒÊÏ‰ä”ØA°2`çÿT±y)v7§»w{ÖJ¼RÖÚ93dİ‹E»"´ôg’ø÷`/£U@œ¾|}øõŞ×6ÊÉ8	Óoÿ|øûŸ¦_·Byüh˜gè_á@5Ñß¿ı0Í¿üöóÃw?˜éçÿ¤ù˜I)­iºŸ"é£ó/øÑ÷Ÿ¾ûd'˜>ÿ„%Õd‚Qi7i3}şúğg)ûËôùßßÿü	—€]!¡F& çP*¦n°ó¤Ÿ·G½	­b`œ+¿$¢DÖŸXŠ²²T‡2K`ğ‰ç:ª)¢Æ3Ó+>ÜVn£¥Y²»ä_ŞfÆHÍ™	KfªşŠ}PÊOì¤‚8; KÚ¡#kå„Ç™š3AE„æßØàw.é…¶~ß­5‚… g¿p*ş_·q-ÒiÂô5¿ˆ¤û'za).cB$15Ñ¼±FeÌØH˜©ëç¤UÓUP>Í@cé“ H²ŞLZaükm
†nŠc¾çóĞˆc<}.˜€šÌXTˆi¤et„Œyükä
\(ŸtDE#÷Ñ†X0
‡òë—¡¾z¢WÂeÛ‡	ñ­È¦$œ÷¡#î!
í5XÆ&aÎà&aÁ‡à¹Ø }E+ËôC©•i‘ #ÁC§oB­ñN3Ë$-h™	+6Gó?=°Ï‚Z˜Ø´	òyÚÌ@ÂÀ¹<ÕÌ)‚I(aÍÌ$OX@f½e%”¼é1šœ+=AF†Ù|Å<	µIIÕˆ3–&,ãˆ_mê‹§æ õãÌ‘ê´ÌåÌ9§Í…«<ÌÕ™ä-&ªŠXèTU² c:gáX­ÃÂ¶‘Åø—‡QzˆÓü?Ê
å÷”PĞV˜QŞ’Â[RxK
¨¤ğã‰š!×y†hbÍ ñE—%	¤F%¶È	[e	Dı"K$Èâ›\u„á‹.M è–i"a‹4‘°UšHè"MÌXJù×œ&ò«.MdŒûa™’{l#Î]»°ÉC ˆÃƒ¥ÉÍÃªhˆE_Ñ#Ó¦qĞÅ6<î‹Kf +·<“ÍùçYæ	‚¼õ„3}ˆ+Úwi‚ §¡“œ°uš t™&¢•Ë4AĞ:MºL	«i‚^Õ41¿èÓDù8w¤2-w¹Æ wÎÌ)sá"÷õ&9Š¢";Y“<ÈšÆy8Ûğ°Í&d1~ªtxK
oIá-)ü1’Âç=¦_ĞªBƒB~UˆV˜€òeè;‡%±ÒJª²Àé<D´~ŞU*•0ZJ*º-Â?já¬´¤M*^{E°A5ÉH%¶G¥¸à$TÚF ×Ø™ƒÎ ¬ ‡ÉÆà…SÁó)D—é81éGuŒi#ÉT'‚Š"0pq;°¨&Má¦Ç§õB±F
± \À¸Bƒ¢…Í¨ ¸‘P3ÿYÒ„yÉ›‹R
I×Eƒ%e·ñÍ*N3 ç¨ÙºñŞœ¢É¸åUäŸäqZÒ1±Oï9(×ĞwÎ™êqìD@1„­\ SjG±áñ7íÈápÖàËFÈ;EÑ;ç•pQÒù«Â¸t:ÒG½Æòä,ÊTËàìoŠ¿U˜ü-`‰ÒvSè`…CõtÄtÀd¯“¿q¾h§©Ò´…T”Y˜°\/i|†›ŸÚè J æâ©QB•‚fL!æ1=„ÌSæÑ 0§$ö³ ˆ¡*!w+:)Xâ¨*°¡ÈQÕ5_lÂÈTëuUC3Ö™÷T7<ªxÛ‰S]AgËó(SUÕ#m¿•¦Îe»ÃiK;ygÊé´ÃHwNJûÿUøƒëˆ|_¨…% Î`şŞ£{]¾şXÓÀP·’8§$‘ŠA
ÖâÏ#¾Ô3E‰XÀßãüšŞ³~æÈ~ÄŸHc+G0àJë(èÌÂôlõ_lÃÂeşR¤fv†ÍzvvõyáV.¸rbJš$–ØXŠyŞP¾Ÿ‘~Ö`±cÒ*iïÓ¬9²É¾0k?i¹h6M¸ËÿÊù=òïZêÃV2ÃŞÌÚnRÓ6èmœ…*©	‹´8ó²Äv´í•Êó&m’VáI1CiŒˆ&c]o9ä|Ô6Í¾Ç®~0«²Íï>ÎbTcÃì46;NrzÉ	bå	W$ï¨,¦DïçSŸ%8æ	‘$µé…~Ÿ=4{¼Â“Rà®H©{ñnİ†Úy 7²~¾ËKó«RŠ¹N£Iv`ŞÄÏYt.Î–”iöÇœ!6íxCÙX®˜¸˜î²QK÷H®´K]$W™+KE©ÉÀz«š`Ã¬†½„éræKbš3Ç^Jâzz6°dÌ’xú\æ!-½Àğ«,ëçu©è˜©bxQú¹"fíèè„³CêÑßg³E®)6p…eCìÉíÆÕ(9ºÚ¨C:Æ*ñ[Òqc'éø±¥ÁêÕê*]³
‘=“{Ø°cÊ^Ş¹¨ÔÖŞ»Ôh$îSj´ù¿¡Rƒ	½,5ÈKÍ3¯+CÀ· ¨lì–!F¶MÔ–Énz‘7¯^†0š¯\†,¤İ*C*şB‰5¤ä¬Şœ”lÙ/ä-Ë¯W	o¼ÚX‡Ò§ğÊúO?ôğ‰ÒFLKMòÃ¸µ!{y…¥z«ĞnWhLE‡Lµü–ª‡ÆÎ«ThŒÜ§+Ò+HzI*T]&A%2*»eO€º,²aÇ¼ÄÀ7å%•W­1ÙK¼ÅÙDÉ[à*	b¨å.#³ë.àûÇÅ­7ˆ—dş–™ŸW6’9œ;x´œWËš±ËÑt™Óç±òØÇF+Ís—ƒ×ô¯¼b‘O÷òüœŸÂ¹½`„²¹)Îã¯ËRIK¶`©¬âxQÑØ¥]à{DS¬ÙÚÈJ§%›êã•%aÌçÎŒ­½èà•véTÙkŞmOØHÜgOØæçÅX¿~\·ï3^È['&Ù=Î˜Uˆ‰–éHínîh÷âX÷7İÁX^ğ×Ÿ‹\[­RZo¯Ğ‚RI˜	´¹_cgªékì¥@Ï:ÇJ'À¼ ğé9‰;·Sƒ w4‡ĞÙeÿÈ³-ƒlÃ©]Hµ®wïùÿ*.uô‚Kâ(”EÃÌOï!1¬Ô€î¢Õ§öæÇÙèš‚Wà =èf‡B¡}‚fCæc4E7ÃĞt{ú,?¨´0>‚åcÜğ!Y¸v:	Q‡—p–“JÄW$“2ÆĞ;Á9µOÅ©Ñ!Ç9éxÑöAšÿaQnØxF'pá‡pZFØ³¤Ü)…Kş6uÜS´Pær8Ä«°ázÖÀr¸Iß'–u^¡ğRªäAı˜™ŠHÍƒ^Rt™³­Zj1b0£NÖ<­G”'G±$4 Æ5ù>fß2¸ûX5-ÔDÔHƒ°ŸòTQ+Êr¦{L º‰‘÷[¥‹ÀÛ}n‡‚f²n¤©!·!{‚'…8·?b¬[³Ç-–g`Á/½-‰Ä=Øe8a)pGÊ‘£‰t7†Çm|lŒ¡
òæ`-ÄÈzC©Ç.5™ü0¸ÀŒGÙHûq$ßuš*Ñ‡Õ&xã·¦Â
'Æm÷)Î”…°mşFN“^€EâüëTÕeWªoX¹’˜»ƒÛvWúZ%cµ5Jî84X]–Ü8¿CÑÇ–âNÍ @:Ñ¹Ş#WïpéeÊ¡c-
[¿ªk=®ò.ë±Õ®²pÉv,÷ÙB‡®¡zk—FAk)ª `ÍÙŠåBMÁ®2ÓpevÒŠ¼9c,—î´Åƒx ŞÏÚ·“ó¯g¬Ï;K…†J™ı\:tÔ·¿’ï¶w
»vƒy/7ŒÂKŠ±k«¡Q‡Ï¢A³<6,¡ÊTåöÊ.y]÷¼J™vŞ×†º²;,µÄ°Êş&ë›Ç‘†ñ½ TÑƒÏßŒ5ÒìPgİ1XÑ3fvè7§‹ˆóõÓ1ò²£[ıº$XsU¤P°ØyÿµÍø¸F;ÍÕ°¦Wì#ÃqÌî¨Ò²;ê>«Ù1Ú»;é•Sw$‡Ö ur:´[x††áqåÆãôŞq<b¨“Óq>f÷´ŞíO»\ÒV	-qã±”c§tå[ñqI<Xd‡«ß­;ËŞ¸Ón—™çw@¹G  ù¸:°ßX–ùºåù)óèho˜íO‹w¾°y;š}y!6êÿ"f¿n¬fß±z:·ŸAûUÕ¡ıC·8Ïİ†‚O¥†+Ó+TÌ7,xşvèq§}´[I½|‘Ô­½ç+˜’b—şãŠyÈß«Änxïé~láTC½+Çõ>ôŞC‡t€Ã¯NŸ°<:á¢wnİ…úsSïN) ^8<YaŒ¿t;ôÅÂ±#±WXšÇr‡_VàáAÏ`i¾ğò´t/üÄ¯êbº–bÔùâ¡°årÛ
¬—³Vß–$gÕõÆædäKMå2¿L¡ÊuÓ“Ôªz¾¤­è=ö‚uóûôoéÌ.Ó¥îr«¶Şax~O$K»Sû)ŞI[ôé„ò–HˆJrûÔÜ%G[Ií´,°~:ˆ¡¢u]?$D½ˆŞ²nH	Ò.µ5-­|Æ{!5”·Bjhk$TÉ´CœŸÖ›¨qŞz5	;,ë‚÷@jz{êQ¤©Á±HVÎ)5ïÌ„˜€aÕõ@BÔeï”°EÌÊhïÔPŞ©¡ÍN³ç¨Y·ñŞ¼ É¸åEëH–{ËÖPL¾MµTjÌW:ã ¦‘§XÄ¤ˆa¶hi¶£‘[4ƒÕ¬ÿbÔÁ*kÔ0Şı¨¡¼ù_{1:µËPÇPíGÄX¯}‹˜ˆµÃQSï{ÔÇû!ŠšYß#Ä(çjÎ‘%É”Ñ}ß#K×BÁ§fpEFÄòd,Úhï{ÔPŞ÷ˆ/¦`dªÍ:†ªuëÜcŠˆ^ôœ¾G/5ï÷>]ï˜Şë:=#q—ëô\„ºØT:/¾>/uºv¼ ”îş.–²k®Ğ;³¥¹ı;ôÔ¿l¥c÷€5»7œWõ¥h„<ûŞmMuæü¤WÇÂ–ÍÆÕå›Ÿ×µ"÷­ a7ë_ê'Ì­üò2Àeò³8lêİ‹ä@Müc©ÊêfÆ‡ásì’üõ*W©»i#‰¶ù³lîCO†SìÎEò‘Ç”·–zñ‚`e}œÆ/~®|*¬¾w§Fâ>ËáÎË“äU–‘FïÔ2²¥ğ›>`û>ù——Ls¶]é“õIjË^õ
Í±6‘®Y/ñôğºZª¦<œº4¼—õYŞ­.¥QG}®©tÄà!J‡~, óü[İ!XgŞic»ÄgyÅJÀcîè·âª-/
ƒ7Û]\áOí	}ÆÒAâ¹ª­ò{.ÅüõKq›ûìRÌFS¢ºK#= Fº{K1{ı©;«ï
endstream
endobj
51 0 obj
<</Filter /FlateDecode
/Length 3687>> stream
xœí\ÛäÆ}ï¯èç +×ı²3»~N<@>À‰³ìü?Ãºˆ,µÔRït¯xv=vët‰Å[±Xd'csùsVøûaÉé)ëœÓùÇ/§_Oô½qI­WùüÛ¿NÿøÓùànÒCc¥0>áE}¦¿ÿş\?üöóé»ïíùçÿz1Û³ÖÆ¹Ÿ
¢hhı€¡_Nß}vç|~ù	„
‡úlã“6şlìùåËéÏJYÿ—óËNß¿üóÀ¤%à–@,@œ«
¶ih] ;¾¾’gÀU¢Ÿ^Ö‡Ş&£Sœë°œÄ,&¹±åò•¥:´]#¶87IŸ4Ş˜¾õmX™ßVvÉî’uœUF2—ÌÌFøşşzÒ:Lş¸³~õ–Œ‡#í§ JìÌv"Ç¢‰ê'ñò‡ ²ÑSŠzß­‚ËQU¿r)ùo¼w	‚†QæÌÉ¦ó—ş`ğğJÖe*HSéL‚uV7Ìº‚…¬Ì<N9°Ko'u¨ôÂ­£‘9c!5ÈáKˆg¬1¶cx —5¾í]—Œ6B•K˜ÁdÖ¤Ü°€OxÙ€­ìc	†i$Øw1uŒÖCÿøã)ä8?½ÒÓd­v<˜àaFA’°ìCˆÃä!§É“`“0oñGˆCX1†Aî3¼Åh'4D˜N&	=dUyĞ8¡Îo„m
:aCÂº•ë[İ^Or<¨á,É\ ,{ÛH5N“EÜ©ãº<y“É	‹!4½uJn'u™œíAéY«ùfóêŠØˆ+û{dôâõáõ$¤—ÔÉJ—c¤s6N…wy¤¯³äbQtÉµÓ4)k\.Çn¹l›	Åÿñôo
é\ÿ¡¨Ğ?—€S!¢¼…÷ ğşPAá‡r†–w
Fp<G‰lı"Jdë(Ÿ¢aË(AØe”ÈÖ.£AË(A˜±cÈÖ\	Â’-FXHi$]‰‚Õ Q?ö QŸÆ Q1é…¤ôW\:vgS.€.\*³ØrMuıˆ•×µ(—(ë[.æn¹æ»{T ÷QÍ/cDAÆQ¡ĞÈV*–½—1‚ÀHZA¢bffÉ+C‚¡‰ŞA¢b .´^1°1D‰Š‚a%Ö¢D}jQ¢?È(ÁÃÙ“˜,ûœd€½“Y˜%bg—²Ï«‚•Ä‹‡•ÉËLj$Û‡îlF±ÊoHŞÃÂ{Xxœ°ğÃm¥ó/'H4™¬ñ¾V‘Š	#¿øCRTÑĞÇë;‚İ”\ÈğK€YéT@pe/<â-ü!Â;å(ÓÉC÷&h‚ÉaTÂÌ)@->zá‚QS8H0 kT° ²›bÖQÂdæ&¯c$ Â«²òr2€TŒÃ[cÆ*Ê"õ @MË0Jq°«¦h°PäëÛ)`6wæÉ Â<1¦$ˆSGNÆT›€Á/”UÆ6qÂ-M*öíª ©¼+RÀdÊ®t³yÄdlÊ16»‚Dˆ»êcä®ä€FQå8”/]˜á±°×ì,à¤¦¨2¥ä˜=iÄ`†*×64¬$mß B-^é¢MòZU@¡A˜š<ª7©Xb¡¬wÛİ¯ƒÕıBnîÇ0¹_DL$Lt“‡Š†ÉTè¹ßÀ—Æk3È`b&i½¶aQê¥¼ß`¡Å×S Œ€"…y.­¼³m|„èŠ*ô…n“0|Ã¦ò~üÁ[Š®³b:XlÌj0øšU.ItÛˆ©f+\Í—HGše]ó®îz7T}½±]Ğ¶qÆ”jÖµÄøLVÊ×ôÜPÀv´a{¯l‡Å%üä^¸¨Ä]ÿEM2"½5rIê7Ê!Ä\Q‡’ÁâäHÁHjŒ+Ô/Àí	(dGúî“RDğó<ğ}ô´¿“{†z~]‚ÛóheàH!-fRiÌF?ˆÎîØÓ§áX+šÓÏC/bå½ W²halù@²óøÁHİlË”ĞÜ<iŒÜÌÇj«¢A}Íi-47ˆta)óùk¾ÛQ'¸ÚZY8b… ooôR¥ÏÍı?Wõ:WÿK¢@‚*Ò¼DÈ‰ï·L¢š”¦‹d¬5ßhWìN…bV&­FOõØÍ£"{B„ÏÕSØ•)²/®3r¯BU™U•.4Íí¹y	=<U¬Qòn]=‡Şïf(êoŞD´fúOíûØ¾oôèscêweLn|èJÏ…qnõ¹½£Û³eú]²¾O;n°Û"[ªå˜w:Õƒòv™…{-|÷ Ÿ>÷UdÙŒÅt±†ùİÕõ´šåÚ˜§;È2‘‹½ómÎ^éâŒ*¼\şÜ+ü—ypº|tzÁS<&½"<8½’|“ô‚ç»)½XSøU°~H/¶–Ú,^µyq¹†3<bNÏx|vÁ?sµj#WáH]øocŠst,7ş&ÃÙGv*übíE›¨”Ê8f0ïòß&EºO>¸›ª)™º{ÊéY Úo¿dxÎ#KF·ç–Ğôeñÿ·dX¬[–L¼-yù¶ä=i½“vôlóŞ‰zíºëû¦è6L6·i—}7;ÂÔNLâÍY‰¼<'Ë#H÷På°Œqûú55}IKi¾tÙRÙLŠ(‰Æü…ŞøÂ}j¤´¶ØZQm§ ¢JÁğU™nÒ6eÍw[,ºÄ]›Á[jg,o6Ú)ÆL•å}V»pÚ¹BŞ§Tï¤j ’Çºzƒ[So3{/mt3œ~èÂÄ¡vï6OÁúàáÛMÕÉj‡Ì[\İ}nSDÑ#3lˆ¶)‚½™#Óß ¨ô‹>Şr>ãsS_NV'wá¯Õ"±ZÓıÉõ¤åœc[¸ØÆiıgİÃ»yj'ÁÜö½¶¿Íø~À”U¯`Š..ã'Ój`FÙKÛ÷ıNŸ¯öÛŞ\Æê¶•Ìñöë{oŞSg7¦<´Ş´ß—­7À8RÀï¼h½D”…´ì× ¼N>¹Eë›<!8ê?qÈ†4ÅRŸ#eëMÀ²õ&`ÑµâÉD‡K2&ºa,„è›±¸ØU#[o¬Ç×“Æ¾.oÀpà,íê™+`à™ÅĞvóŞQ5!iÑu+X0É‰¦[ÇòĞscT¶Üø}¶
ÏÃ”±­™wv
–qÍ«.›mŞ—6iñ8Ñ$_Ï'`e8,"'šm ©†ç­‘mì« ëbÍ6 8Ì:§e³`ÕŒÍ6Êf›€e³M’àF•˜Œ›Z_Ü 2p«LHËm5ÖŒì¶±e³Í{¤ù9D+zmÀ ÎXš·+`DãØi§dc6`ei9ÑhëXúlŒÊ6›x¿EL3›o`h¶´`]øÏ,âŠOı¾6ºÁòàOñ˜˜aq:®uñ;ŸN„8«ƒ‰¦O·_CÌ¤FÚPúU?Hiq¦_+5Ì}šµ2Ä§ÁÀoïÙ@FWafæÚïu½Q½eo©ÚM—ìm5‘øñ±Å'9Å·(>-Eº©ˆ$êµ#Cª4·jK×ic™u7¯£KOb¦»Ôô´òƒ$}Ph¾=°Û¶‚Ğ=Ûƒ‘¹yßûoí/Zæ½r¤xå7'Æ›vÜpŠ_‹şbÑÏg>ú¼¹ßè3R_£7İa £ª]ÔöÄõ²UÚT8´[Eß¯|ª/ŸE£ÀEVßŞ‰m©ª¢Óæ˜4÷Ì»ãŠé-¦­²îµ{é7W’³iPç1õëùòÂ`q3z¥·,Öì½ûâ€-Ô9ôl¤J{è…ùºšî±ß¹ra—ò©Šƒª3»¥à‡çêV-9Y4‚ß°=!±¶qAÿ˜fVzùoo~ƒ.7áÃ5Û«}ï[¾PœÜ‹0—8fÈuíşÊÎ^,«.×q¹S Bny1¢xAxŒzRC¸¥¹æqş
­q»Õú`ìÔ"´¾é*ÆÏWoH{F¥;^eèÓ'~¶´ënĞÜoÙL¯xÍ!¯aPn®Ë°Øyô‚‡¾»ÙRş±ÑÒ{V¦‹?}ÑæÛ’NÃ×%$Ë}ğ—ìY»¹C›İáØÂ:îŠ"Q›~ªfì!»ËVL±œÇ¬¼çÔp©¨”ÓºKhwÓg±Ã	‹|©¹·[ºÙınû@ÿs›ûA¥9Å#Jƒ/uâ|¼WiÃ9>ê2ııÚFoÄ®+ùªİWºåoô'i’™úz€¾‡Îª1âö¥áı;~z¸ª·å­K¿¤âè•ıŞ5"ªHw¯˜¹½KKº¤†iM;Š³+7îçpLıqõ¡âpRŒ¯r¸5=\Õ›½åv,Æ»­Â/ûá#îBÊ™ïsCEëÜ˜òA„tuGX†î#A¦y‡¹óşqú¿†´š“?ÆŞ{ÈÁÌ™eşÖóœ?•ZTÏwdŞ¸â=Õî°’ß%VŸü¯òä.êqòŞşç–[õC™¨lÈ¢Ìee¤ßıŸyÜºNğ,0y<ˆì†ı¨ğ5ú˜õ™Væísõ
J«¨T9öÖÌG	¡ÊcnVkz[EåQâÚéjouÔù“Yš^ªÑ	Š4ûèÉnşUyË²™o¾pú$ÌüÄóÉ#Åp”êÇébúŠKtsn¹ƒÛvÃeİò˜;ˆ“¥Pï!wğjY(»¿;¼%Ÿ¡_ˆ/í4ÉêAÑÌZ¥ëí2j¼?ø@ÆS<æ@Æô‹£÷«Ãã¤3+[sÿ=­§û¦Âå—Ä¡?ÖÕºÍÀuåW/¦ß=Õ™´¦Êƒ^éÓŞñä1×ÒKr,fÇ¦ûd—æªÎû†Õ7`£¸"+¶Qq·¥wú½½;İEo—ÊG}ö“ÇïR\ÉäFO:Ùyc¦äëÁêÂ„íbàÿ ×+i`
endstream
endobj
53 0 obj
<</Filter /FlateDecode
/Length 4673>> stream
xœí]YÉ‘~ï_Áç¦œ÷,Zİ~¶-`ÀøX,4ìıÿÀFäQU²ª™ÔŒw%MkÈ`efœ_Df±¢csùsQğ÷§…½MN/Yçœ.?ÿòòüÜ¸¤.Ö«|ùç_^şóß.º[t€Kcaıêşıãï/õÅ?ÿöò»ßÛËßş§Ì³½hmN÷×BQxi}—~şúò»wwÉ—¯…‰
‡úbã“6şbìåë//ÿ®”õÿqùúß/>ÿúçLÚÜ–!‚U…ä9´.;¾Éƒàê¤o_¯3z[ŒN‘q®Ãv³YdÅV”ı­:´İ„+$ÎMÒ—oLïF»Û£ÁÊ4ZÙ-»[şÕmf¬2œ™¸efáğ÷/Z‡%àwÑÑ/0{–ŒG6Ú/f"g¶:.T_±Á?§Áõ\÷İÚ@ ¸Uõë%G˜ŠÿãöD˜Ã¨œC›.¿Ô7Ö_¾á‡q™
Å!S¼ Xgu£Y—²2ã:åôågtÔ¡Îg—h^™3R#¹€+Cüc;ÜÆjø,´¡Æ¼.Úšl´¤a:kY“r£…”p°®²ıJà¯€1u†CùóKÈq¼û†ïkµ£‹‘<X‘M‰´ìCˆ«ÅCN‹	&;Æ&Ò¼…?L¤Åcàb‡œÁWŒvL?HÓÉ$¦E$Y•C^é©Îo˜e
,è˜‘Öm\Guó{¡ë´p¡i+)´i+•–}ŸªpŠÄˆZ¸@•æÁÌ$y¥ÅĞõVu„Ô„£.¤ËJƒÉ™Ö+Ø¨ökö©T`øBVl´ŒŒ÷qÈ°±ãÍ·òºœ<‰¦%Ÿãw«Ã‰I"rv.ûˆ
R)“ÂŒk’ìC;ÌÈ¢üç—ÿB€H—úâB] ¬˜ò~ÀÂXø:Q7´Ú£Í@É¿ô7\€ãRÒ'*m•¶Å	¤Æ5NTÒ'*Şp @"¨¤ÌM¦@ZÒk£!-¤¼ŠJ]E£]Ìø¸EÇ¢Ó¸#ö)¹ËÒâÜ¹;›<º8<\HnX]C,şºy ’ÆyHwÛğÈï6ìØ€V&¤@X#P¶H¤-R m‡É©R m‹HÛ#lW(»Ê-J mHİ¢D¡”Àw%ê›5JôË¹õi¹ÃÜ5;«ÌƒQîæ$3‹‡®6]‰<ÀHÛ<»]xÈ6ó±ø>U8ü „€ğşïÂŸÎy\şşÒ,&k~«Ár¾ Q*|£5(²“]!£±¾bVğ¾í’Œ‚}Br‹6ğ§§p¨“‡A&èB ¿‚Ò<a ùè1Eşâ:…V`<f‰YGNFgˆZÙÕ -ºSV/D<»®Ø2VjÁ¡¸@Ô{‘»&6Å”	™´ømEEÛEtÑ±Ğ4ÛÆĞì¢£m²6€
[…\<´
´b×"SÓI§å¢é®@¢¢»ªi<Ù„Ö!óqÈÒÄ;¹ÉxÍ§Ğ;ÑßŒÂâ’lL¶İßˆ
j-Zíº"b(ô}Œ'‹±pI|i ¯6¾øÄ1¸zMS°<Ra–Ğ´BÖ“iÄºqµän•VMòp·NFw‹àI9>ƒ‰nñ ÕR&†Å™ênŒ+A¯ÍJ3
ëW²6bäz)42)ñÛÍPÜlŠ¯úR@ğhÒÁUqF‹˜^æl XÕÅİº @ÃóP„Æ¡¢!HÚán
U³ñİ$l™a¼CÃÎŒuî=]Ä+Õ½íÄyî‚§ÊõÄb¬§ÖÚe•Cis¹Õ±´C7ôÙ®¹û!¶p} ÓÔë}€¯”Kğƒ¯5üÿ~üøú™Ç×_ê5`«ò¹úÜ×YrPP zL« ,Ô&e»¸%öÛ*{tT‹Ò¥¢bŒiZà€Ä©ak®B±M­ŞçñĞ3ğ¬xwãÊcüğ_°m|ÿÙK†ä³áß»-òoR¿iö$ş!” ´¹¦ÿ)ü{Ü¤'ê? Ô…7ü'~?éş›ıÎÿ_ï`„IpuëÕ¡@v{=À(T1PZºÿº\dØÒd)ê¼PF¶yÎPd+4ù/’šîàÿ>5({«°V ­AX¹æµ+¯cƒ9„ÀOìš›ólÊy,ë/°cHÕ>[Ú=Ù@U6ä¥@q`}H™  -úÆÌ,y[æEØjWfßåb$t"Şš*ı<”…œG’$Ÿ÷9Š|û‘´aEsúË ĞA_QÈÁ¸­÷ë×±óÅ47–èßÇæâ¨A=CsOHs+‘v–B1¿œıìrA-…œ¶›åX Bí¼G®Ç£;Â†åÉÑMK<'º™¯­f´ôºÔŠ#ê+`k}êH7/B‘v:x.`:mß¤aËİ…L§AÕ$ÍR7Çù,ì5-Uëx-¼Ü¹­IWÏoÖ ö<kJŞöÍ}t!¶¨¾‰AùRÖêıAàakÂ:†lœk¼M©µ›™èoMüĞpW´¿şAµX›–ëZ)š`ÑémÂ[¡Ñş¨3¿pRï@Ø°•õ˜—¦sè¤ÌT@œº¡Æ]cU±9g;Äœ›¦¾xÚ¤¶T´yÎv"¹ív¢lL;anÚa
‡×iµ¹¾=Ú%‚44*ß2Çxk§'öÆïW 2µõÍ]NbŞ×vš§D¼”9ßÚH…‡÷ªIiñ˜5ıØ%Ù¤½íA9›¾DRÏÑù±ü?ÛÜ•kÕ!ybÚzÑçf­÷º>‚«=&”“)Çg—“´ÄsÊI&Â“7‹L’ï²Y¤õNm¯)ü–dVEÕƒUß$²©?Ñ9q¦R «ÍÓË±Ğf5Ù¸.Qó¬)ÖmïëP¡mÚµª­óNÀ;g#:¾˜(£[T³0·Ø!ÛmİöÇò2[‘©¼g&0ìš[º)x^¹c~ıåVi¯vû<`>VÒi·¸î™öÜÎ#ûíÎã_á§'3Y9]­^R}‹nºR|>R%ÇzDÂUtH¥ÑnU:@b”¦°YãOÙ\ÇÂyg´Ä÷98[‹ôİÎøò, 	Ï]o{Õx/æ•å{D´ü”M‘¶a±¹noØÜ‡àk‡zÄGS¢¥ô•’s¥À»\è\Î§*îÔ¹µVaÊ:aƒ¦¡¶ŞŞïiõAI@MEB¾¡*µ†&$-ÖĞ² ègV7´{>£f‰,Q^¹şf"äµ»e¾Ú˜½78º[’ök“ãsCw]7ëmÉ#¥¾ö‹©§¦\Í‡Ìö¾»®AOxBìÒò¨z ğ‘øun =›ÿXüRÏ‡Óäx–PÔä;9âã¤Uô<$Œ~ZL9dß¹àËRgö%	ÚõĞcêtî:KŒ±÷ù9–ŸŸThî™ß\A·o À˜Ÿñ­•’ÕbËkŒùc•—Œ4ô˜{Ä^w5ÉÆòOp1÷³\ Øç¹ 1ÚÂ©Í€Æ¯IßqÕˆÙ.¦·¯] ™––lä!%â÷ï(1¶2Å¶2fWrá…)ßİbKdÑÜÛBìYœ´1D£ôüv‹É©”–:JÙĞcÊµùößÑ±Y¾^´ûÇ3[)ğ¯Õ†ı-4üv¶êùÇÖ-¾V‹O6ãw}GïZ‚Æ%:#ûÀW ğøXJö™E´û+	ğÈ ğM0¹‡¬¦¼ô4Uovß-ÌÉÓ¾ÀıœƒI÷å§romDPàlÙĞ¦³›cŠ$o%i1Îç¨©	J–°€9s4”(®ájzt€,6ã·áÇˆ$,.ë*¶Å3|âS>°xWI0"†´ÛàÊ/ÚÃˆèiª×& ¸Ef~˜Ûõ
4-İê‹ÛXá€]Eÿ”TûdÉæç1İŸiƒTWî©# Œ‚´5öÉ¸Î!š­|d„¶{§1 \¸ªÆÚòäı.T­/3;mÄ%ÁT‘p]¯ÉèœõÖ>åY‰œ‹Ôzš€wõÓ¼×çv€×6¼†ë[…»lıÀTSW8Nğ÷¯ïÎaÀÿ¢ÙyÇ^³Ò
íXu¯Yq&ÙÜ³²bk Ûò:<¤öÎ?Â«•,ÔñÚAá€ÏÊS	bˆÆp ^‚2ÓÜß¥+ÉÂX§TJ×=òÂuÿOVğB{$¾†È¯ÌÖ!Ke)È¸èîS—0ëœîO$.«=	J\eŒŸby*I#¢ÅÅÇT*€­‘W
œüô€JDv¥²ÃIHÂ¹µÎŞçö¼rWù’×9²Š˜+Å¹¬ªÓ!(OuKÎG(úy/‘AQtêCH½r81ÅÅ9†ç}‰yÅ¶§‘Á­»
•^·9ÄbA*ldWø@&’s0WUô»Â”EÆ†f'£˜è%­ÈljbÙ*vâÚ’;L,–ÄRg`¼ú—ã# –ƒ’W‹†’Üê|š¸¡¼O{$³ˆ˜˜›ÿ$ùN	;†t(Iõ¼‚=n¦òi×9ö¹ïùç‰ûW¬qÎ§Ôq²MôâTíôÇ-äKÌKVZçÈÕ¶XeH'ï8½ğÁÄòcè
æÉØAbLõ*¨ä|pÎ¬9Ïï&æÕœr9xzÇ"³;N¡ô&šï„ù	„;ï%3·áß!>•œãqÕÓgˆâ˜˜MO—ÒÑâù³£Î“÷ú~í&Ö bİÑ;¦‹çË[l•"/xòP1ÄéØyÇÅ3"Ï½J®ß¾áÉ5ä#âÚ¯®ÎOŸ,N;ä•f¥ù>àí
M÷Plû}î‡+åVÎïÙ-3¹*”Fˆ˜)¢¬V]@ğ#µÑÃBZy‚x)Õr™X!ˆŞÖÓ¡ÏÀ.?§ğDÅB Jı‚v÷×øU«ßtÊ=s)bôYP_…yäA+r{@1¬‚ùí´Å›f:_á‰°.ïWò§!?rkæ‘=¬QF_Ù·®ÅåÂ½CÛE¬ÓªŸ›
YV®:ÄD.åëik§OÄ‰>pÄz(ÕDşõ©x’å¾{†}3Õğ5ÎßÎ?·ıß%—n†KG©Ç@}ÅÔC ~d£3ñôúôıù•Ê=1Ò¿Cæıuëñ–š˜gÎ—€’ª\ñíÀ÷¸e8ñàù¢X6à¡w’Í#àBNtı^¢íúğwûW¾ç¸‹ËóÇ¶«Òê“–Œaç!I¼Å(îÉ,.&‡ûßÕÛŠ}ÏmkeæTâíŞq¶øñ&ìPµåÅ"ß¼	»É~ôTf·³×`+üµCÔ˜ÂhÉ¦4á-¼¡¬\¢ÊfÕ€¨qqøk™¨'x.½Ómt4Ş}¨¼ù:QYïò¾krÎøaíĞç¬múpE£®ÓƒJzû¶¢j½hH¬í:ĞÌâËï'Í‚`1¯Ú®¬¦“fm×-˜äXÛõN[·]'*o»NãÉ´ÙŒsDÖ%ŞÉHÆk^´o»î,Ò<ŒµÎ†X]»9Õƒ8¬å:Pìb­²¼i7$üÅ7\eğşlX¿u µnğ¬]ø ñvëDåİÖÙxjVNëP[sÎ5@'Ö©QzªEğ6ë¤4Şf¨ ƒy›u Á§1r~ „\·YªÌ)®Ô%Zé`Y›õN[·Y'*o³ÎÆwC°e†ÅVÛ2Ö¹·t¯xĞGÚ¬ßyfö~‹uíÕøµ¯í¡ß;¹µnå!ÓÑxR/¶îÃm~ğ9ÿş´2MK½¿f°Î¦É:=Í¶á<ÍàŸ8¬]Ğ§2á¹Õ¶›Òr
»Î‡Ò‡o*¿Ù÷ná\ËØv ?æ&¹xéÛ¾[êa	°Mik\Î%hîœçşr3ØÍhïˆİŞ&IÍz¬±%–š:«±Yç†5ë©6“óRElg-]2[ŸŒÑÃcJÖ­áš7=ÂÑªgİ…ØÔ£dwÖiö[ew¥¥æ„Œ2¦íÍNFSı ¨ÛXkWœLéÉŒEÖU™nš3¨Y:¨óÅşğª}–¡ğïÏÓj[pÙcŞÒÓ&ÌJWåÙø™Lóçâi^?¥`Mf²Ì"0–{8h®ë›–ÓÓSS¾ÒÒéñÔDŒ™T·eÇÜ`Ó%&ÒV½Ü©©ı¶¤9%?¦¦ıšë'áÿ÷Mšé
endstream
endobj
55 0 obj
<</Filter /FlateDecode
/Length 5720>> stream
xœí][¯ä¸~?¿¢Œ£ûX,é“çİ40¹,=’ıÿÀ’ºR²]åsLWwfN÷TOË–HŠ¤(ê“kQ:¦?7XÈÇ`äeŒáöó//ÿ|Áï•	â¦­ˆ·ıõåÏ¿»ıèf‘.õ¹…ñÜ(oø÷¿ÿxËoşõ÷—ßÿQßşş©=õMJ¥°¹¿%ŠÀKó¸ôÇ//¿5·xûò7h(q(oÚ/>HeoJß¾üòòBhûŸ·/ÿûâàû/¹A…™`f‚OßZ$BØoCÊDĞ`ó-±Lnô§/ÛŒƒŞ%ƒ'œK7w¢¦NÖWÌ¢¬o™Õ!õLØ¹bsä-€ÆÓ«»íı»a”ûİBÏìÎü‹ûÌh¡(3~f¦ÂÁß¾Hé‡ÌM¢ê•VÒ.Úèf¬4)ì"¿#·ıà¼¶™úĞ ¸€‰^d‹^¢‡›è¿pßšm(± o2èxû¥~0.Ş¾âƒ% S7¼Ài£e¡iæ¢Pí:aäíg¼;H/]n<G¼2Fp¡B2éKğ|¥t¥Á¼YÂ—®Üë–Ì4áaˆ
-HàFAgZ…XhŞÁÍ
ØŠÖ×+a¼ÒAxğ¡ÒĞêÛŸ_\ôíÓWü´h-M¿)Î
I“H‹Ö9?tîbX”SÑ6‘f5ü!â Í;ïİ ·‹q  ÑÒdPèIZD#Õhg›Dƒ14d‘VG9ßUàë½( †mI®4[@Z´¶4U8F nT ¤Yh*:Ò¼EqUIÇoT‘8!@ÃƒÊ‘,äÁkƒƒT`öF‡0Ñ’Êë}È¬ÒíÃ×jõrjFµYjpjš•UbÁ(5ó.3ñ‡ªê6U‰ÔÁº¶©+Öq¡.[†ø÷Ï/ÿƒ¡!ÜòêûL`” š|„€ğ~3áOoÈJ¾‘[@ö{„ˆBL"ÀHÏiÚ¸Q ´ˆÄÌ *Ú„V4B É ëRÕ¡Qè1@4Šè† ´€FGÇÍ$„)@ u‰–D~[Dş4ˆLl°49Xkë|°ëÂæ`ûEœÁKªØƒ;ıP¯+ZÜ³é{pä22ƒ¿—¬Ç¸Å‡4üC|@ÊiŠ‰6Ç ê9>$ÚÍOC| ª¡ñ?CÃTá‰¤…ÃC¢š@Û fZéSåÃÚåÄˆZ³ÄÜÄ0+§İ|“,ÄÄ‰ÄİšjˆË4ç"º&nØF…¸k<âÛoI>‚ÁG0ø¿ò`ğşTÁÇ”zŒ@QstH´):$Ú*: UNÑ!‘¦èhSt š˜£C¢MÑ!ÑVÑ!Q§èi7Õ¾®Ñ¡|¢C¡&XšŒµu>Xuas°ü"Îà#UìÁ™Š~¨Ï-ÎÙô=¸q™ÁÛË¶x4‰8üct ÊäJ³•¤E«Çèà#šödUGÚ:8 µ.·ª*}\$­Rç ‘h-@à§ ò‡1@ÔË©Õf©Åu¨mN‰Wy¨¥wÉ‰KTQÏ)š¤.Ö5N±uÚ2„ÄÃß”0|„„ğ~!áOG÷Cnÿxñ\T”Ài@-„ˆNúF'i¯’’Ì-wCb2$"4áA;
ş Ñá®¢d° jå$RÃ"uô.Åâœ…>ÑƒTH;1¥ó€¡¿ƒÊ}”¾Ñp<£[¬ôŞDÌÖ…¥İ 7ãD8RZ€Á~(ó@”XÊóTÌ¨ŠeURQÚ×dã-ZPë# ³Ñ„H¹ÁÕtQû,aa<­Bá»Hˆ´Xœ¶j"¯º¶ò
°«´ßÓußÛî£D¹èÚùí#ßåZÙ“¸)Œ1(äqú…~P:/×(ÉˆE„€Õ:aá±ù€Iàx)‹Ædã˜ëÚ8ŞmÉXp”¼°/³*¤+A>ù·ÔÍ–1“‹Õ˜
­Éƒ#a†Û•‡ØvA;RŞ-F%k",)¡ÌJ5p‰‚ÚAÎBôUéæB
İºë­ÁKğğÃGé#x”«tQ¸9b•ãÁû¾õéÊ"a€fÒzSD¥`œ««4à¥©¶İY€4ßFj`¤*a¹ÛHm¶›jPoØ¬]p³8ÿƒQs¡‘Ò×Hi¯Ç¤»ÍW~|¢î^ÓıéÅ À CÌÀ…ásÅ/¬ÛtTì€4m¡i«à%…0Ÿàõ^^h¡uy@¢neª?PYNÊ!µ[t8qĞvÍOY ë²@ÆÂÿáe
7ìíïéÛÈªÁ­"l¶¦Y†1Q(Ãi´ÊhÚ2¢>jz/8FrPü†D{÷ApZ³üğ¶<&N\æ­égù ‘…Õº Õdf>Û>
Ã!LºrVİiI”€hÖ¡GAda^A,“ ˜:é]9îZ£\rçö€Ï&c8­iÖˆÓZÍ£QLÎÿ±İäxüf0ó‰D>E¤1ó¥”ÇäYÇ*Q!WÈ,÷.N³Y‘ÙØ{«¶Æ·×2e²Ì2ntu>Ò)X³AóãĞ¿t2Å¡İ¸kÚ]5Kõ¦[L´9È§¸ø‰}–¢²pÎRD2’	¢)ştHÇÖ^îwÖ^áw­ÕëıO€Ñïººaû,†ƒ€}…îš…7—¹^kúY®Gdau½.ˆëChşPB¨§yÕ]]ÇŠ g_ õ¦9ÓÂğÓH[İS.°|•!÷¦ŸdÈTNC&‚”EA
¥fE×`ğiÉ.¾ S!Â´¹åÓÃ!)@oB(İOz—‹$«Á9rã5}a°¦/¢íô|÷.p[¢ÓóY¿8áEpªñ©4$uˆ’Üğy›nkC*:…åıvÃO;=ïtP[,ŞƒĞı´K™°ãâĞå‚ì_èú…¶Î
÷XI¶œY4"W½~¨%ëëÆ+KÔºÏÔn{b×ÊèÂo^{bïI÷®©>¬ì}”CQÜ1ş}ÍÊòD!eÉ¨î¶D5nÅ¦„	³âÇô…]pf–}(TíZ)Ü0Ü¶4#MW”|}ë»Lív®[»ì2ö±ÛcÂ”;¬´2úp OCNpw:QÚÖ†z-¶¥¢w!²ç:æåc­L'{³Ãîtò1œ‰zƒ“kq€×İÀ³Û' =©÷Zz³ì	·ÏR:ëÁ£0“+­ûV^w¯7Êfìï4´+Ú±Œ‹çoàu]O÷FÊ-¿;OşÀ‰Æà0AN€£‚¨èÈ )p/	ähbI3}Ç2€Mã¡Ä	Zú"eÂ¦TtĞpï½Ã'
bM
‰BM
©£5zÛ×A¹èÎoGŠt¹ZTtZSÔ×‘¨aºÈ–N4n¾¯)Ìhg.5ÀL4nİ[‰p¢&Îûû	QU• ;6 +Kwp@Wi¿»«¾÷Ò‰òÓ‡³sŞ‡½K¸a3kÈ‰ÎAA'ÀE…TPšƒ·8TŸ 4½DWt$Ğ0-Åœ 1-+5œ(h«lnUøD#QÀI#RÀI¿¹¡6Hß10Ó „í†!â5`IU›4}Q¸	#¢›hHòX”KÂĞ@TQÀK•q ÂĞÃØ¸	Ğ`¼3¦*"ÓFÀI¥QÀ	¹·êŸtÑj`¦)a›ÚHom7ßt¢ßÖ©ï‘fµ*%ÈĞ7[ês›,ÊPœ²Ğ2i×¾r0Ûw+–éë,ûà@Ù±É@ÔZàç²dQJ¬::PãÍĞj¢ûG†ÄQÏÔà›ky˜FE«X±Ü6¥5Ì®¹ü»kSœ’ÀÄ½!]Šíy¯«ãj¬eÖ³‹ıq_@–x¦¶Ìc¸¬–‹¼#ÍYÎaîÒÍAQWÇç²ğZ6ƒLËÌOî­âÙ´m¡†êÇÆFl0|h#E™i3şÈ‹av0urèûÜl“CóäwˆöD5`<»D	Z‡EÈâytğÀL0ZÕù¶µÖQ¹•ºcˆïåçG†çÌ»<‰VtMß	2ˆu˜™<äTd[şøË¾^e©¹m3.Xb$b~Óg[>*ÿ/ 5Sjå:¬¸¶­Ğ@Û>¢Ê:¼± LÛ7êø+‰û†ëÿıÛæ˜€LXdízPûÁa"û÷Ìî‹'yHû¥Ë1çJ) iSÎ©®Ã+ø§º;êg\³¬EêÅSË¡D
o”ˆ{R%•"VJºø‘iÕ­½Üèê¼A*ÉÁkiA¯÷xN„‘4·E*éòÓfâƒ%Q˜ıPrø¸v‘^®¬ê¤ìéú5ÁÉh²gdÜø¾zêœ³­2ÍÚÏrìôõè$G5XìT¥¦p…]C´x9éòÀØ	q‘ëØñ‰&ßgØà2qãùÊ5­ìÃDÃê| ~k îå&vÂ
~Ùx{¯IÙGæšÎ1XÒŸK6^3ñXV\6övÛoÈÆíôğ®*µüUYQâ	æĞx‡IÕ;±¤Tçä\ˆ¿SŞ)ÙÕâ!­[ñjıˆÓÜhĞ#ßŒÙB‚]ÕJÔtH­.~,-Ÿ¿´ìj?8L!\º´ìíçSyk3¡úÚlÎ=6"÷Û=õ3Š£`%^Nµ.SÌxåZ^j_äŠQÀ´}U²X:\­,×]—ÀÇ!â[_îóË²º¬)Oë€ouig/äY]–•ÔÊh±hÃn!iÅªWNÌÂ1®ZÙµŒëU¹²–•%®YWÑ™seéZ5[ÃÊR,ë‰‹kai¢_Ì*„°ÅX\\®˜?¼¶ÜbìH‚âÄ±õï/=¿|}IUsH•ê=[¶ÿîëËúÚGëJáZjMÕwà«ŒÈH9
ğ•"˜‚ìPO âÃí™Ú1¡@”t	zT
Ÿ¾oı€ñ2NViòMÄßkÈÕF¢@ßF¤PßFì˜YÒI‡×u$nç½#v‰ÑT hWÅ}‰f	v üÒwe(üØÒ3à}ŠU`	ŞhyÚ0Ï¦ÁV	6Ú4Ø*APW"Z·>$›pCÀÛ•m‚ñnÒmØÏìIx(¦Õ‰Rv|-%â€C\mÃ†Ñ ğ?=‹±ÂHeZo|$üUÀ6±­ÀT$´oúH‘¾‰@Q¾ù†”¥6LíØƒßR^N—JÕ½M~
ómš¢0ßô”R/˜oz~hTz@kIoóã^;>YƒØ`,ùÍãs))Ì7ÑF”o!Q/¹³¬{MYé¸íÎ4±&ÜÚ^öA¾ƒÉt/şBÛÓ‹ğ	æ%¬m>×‹¦Ë&¼•<ÕÙöşâ%•[P¶MùW`yeTc/ûuÕéğÙ°<ñË»Y®ˆÂËjAÂg)·m[ïVÎ}\‹Ø•«Ñ¿¤.eœ¬Ûã¬cb`2±nÛ©Ï²ŒYÏ¨šËÑ¹Ö­†”eï>ÖÃøà˜|ÌÓë“Ş3®ÇğÖ’1ºgÍ½C¨'* ƒ¿ø0×¬ëé!p­šÛ8‡¿•õGnğt"¬L}<¬`ÈÈˆ(s¸ƒ¿ø=—_ƒnİx]oëˆÒRüv‡k-Ÿ×ü+Şûäç“cTû\œ‡ÁäËûPò³ÕÒ@ZgÙÆqmKòB¶É:¤÷Â¼¹Ç>·8QheïTGÑ©Ì“Ò+[¶î(YÊöÓ6$ó8¥tÿ®4g97õ1Ë„sšì“::ËJİˆ¼x¤òœŞA¬ëf'Çì!ïxrr«|Ùïìš´Á²whÊnçl/k'3ú.ßâIß‹Dgc)Ğ’˜ã{9!?ç‘cÕdì2Kqút¦.{¶¤ÑÅútÒ§“«ú5.ú¾³ ®ûCi¹ì|¦A†UNÒ ëØ¦iá=YÔÓ ;ì_—µN±İv¢‚­º©Íª£g¥A¼ãDÒ IøÒ ÎùSÒ ÃxL§¥A¼NNÒ Fn{dô…ia=ÓAÒ ^'i£½_¢’ƒõğ[6‰”5KáãÜ‚ÉÍÿš´‹İ«	ì,÷^Ài">ê¹>œº"l%oN}$oß*ys‡ÏáH…ıSCÉ[k]ÉöÙsrúv´zuÆä­õÀ¼]ÄzÙMïÍ³W«dĞËZı	fzHNo”÷xôyÃ“‘éT·³xZ’0]¥ü ë¼¨„ÕYÙG
œÓ^kO)°ŞñÓ³Lk[³šÎô•Ù¯z-ÌÙdGÔÎ„É”ó|J€sŞÔ5Ş
ù¯C_ş{U Ç ˜ìí²"àÜK0öI£wË€gòPUÆXoIpB(Ş~p—ÆÑ;çÆq¼G¬'ª 9˜Ğ‘[ò3L6.A¸¾v²1Ò0Ì6³ñ±Î6ålŒ«öÓs­Q~|óM>š1YÇ„3Û|“ñ™;.Î±í”Á†­ƒë6¦x¶Fë¾tÊYGÛGgd]ã0Jó˜ü5?)áû.µtİÊ8ôeˆ>Hëò•½Ô²Ç:ã±ÍlÍç6X?Ë¶‘íE[ë—lˆ¥jK>úªÙNV·Ó­IşZK¨øxNÅ–É¯/¶dlød@õ–,>•[R9ê‹Oõ–™ëËë-+i8
.“Û²ËTpI%)N1Öcã-¹¨ÙQ¹R`~O°œ]’cÇqš®ÙqääwËÁòÎõU»sG<»óäüp·ñLÂ¦â"v§¤;›}ûñ¾‘åımR#z‡Xß¢FÄ« R#ÚŸ¯FÔ¹~RÈ²ı<©µFY'ÈR#bä¸×ˆZ£WÔˆìö~œ®ñš8©í¸8_¨upuˆÏXz¨·ù„Ñhû¨fdìFjGşã¤Ù7«ù·5SñÊ£f½u“½v´Ã:cí(^tÔìÖY<°>ô²ëÿÒšF;iöH0æl®ÌĞ¼ÃÔ!Ö[Òp<Æ¡¹¾Ş±†£Ş1š—{§jGy2ïA³Ñ¡y‹yû%òŸ3³„¡”ÌåÇŒ2ªË£M\SíĞsüäÀW«Ñà®ÃW+fËÆŠÇ¬‘«å7(6„ØO3ğñwß¬àÑ;ç.x¼G¬oPğ`V@/xlÉÏVğ \?§àA¥a+xôFYçÈ\ğàä¸<z£<f‹á*x0›x/xì¹8[Á£wpqÁƒÑXZÁƒ´ùÎãØZ·3o¥‚'—
ºîÍávÿ'•Î—
Hë†½T°Ç:_© ÷À\*¸PëÒ†U'ìI{…P9Îb6Ú32{£×b6ly¬á…ƒÑàÌ–Ôá[Ì³Á7×Ïo0ÚS‡o\„:|ƒ“ãß Àß˜-†	¾Álá¾qQ˜O¹ZZô’8yY®6uÄ“«Ñ/İ™s˜<Wø·ÿ¾ _mÀóŸÄ-9Ç±jüåW¬{OºşˆÄgQp—¢=*Úz®ÙĞ¨%Œı^[ÁÈÁ;PçlòÏQ½ÈKsÿ¤ó£fƒc*ÌõŞ(ëT8»ÇL˜ê­QŞ²Å†+sÌƒyIÎkÔíñÛœ
ÆÂ¾-úšÊ~Ú’`ä<UöÇá»®°?›	G]_f}}a#¦’(9Ûá­Ğû¨½¡:„? õÿ¡V~
endstream
endobj
57 0 obj
<</Filter /FlateDecode
/Length 3848>> stream
xœí\ÛÜÆ}ß¯às Ñ}¿ A€h%ù9‰€|€;dvşHUßê4gv‡#qF^hW^ïğ»»êTu±ºÈæjl.?‹¢oV8LN¯Yçœ–O¿<üöÀß—Ôb½ÊËïÿ~øçŸ–_	w«tj¬=ÌGÔP/üïï?.õÃï??üğ£]~ş_é/f»hmw÷SAŸZ?Ğ©o?>üğÁ-yùøuT$Ô‹kLÚøÅØåã/VÊú¿,ÿûèûÿZ0i¸-`UÒÓ}h] ; _›ä¸Úéûç'ŞV£SÉuØb6ƒœ±Uå´É–m·Àg<%¹IzIÄxú¤ux¾5YYZ+»w+¿z^«
·Â#üşıö uXÿ¸E3õÆ“í×@}ˆÛ•]Š‡¨Ÿ Ù›¨|H+5¾èÏ†f€ËQU‡^s¤ğÿÔî¤>ŒZY´˜ÍòK?°É.ŸùÀñ„L1,ÓÂ'ë¬n˜uY™q²yùÄ­“:Ôşô­á3s¦Ô ìb4M|:ìù'µåïBkÊmŸm$5,iGŸVå¬I¹a!%nÌReû™Gaé“‹©c<úÇO!Çqô™Vkµ““	õ’.Ë>„8rZM0Ù˜ŒyK? c1ÄPíóJ³_;à‡1L²*‡<ñÍ¨³Á°LÁÈ‚,ÈX·qmÕÍÿùÏ'„XX°[†Bë¶ÀXö½«&)WbaA}ò&OŠ3I¤J[§ˆQv:¤2fŠîiâœ!«bµŞ°£ÎºmX°ÒaoÇ67v|~@ÿè§£õnÑãD ôÍ&)xp×=]4‡)Ñ)Â™Ó˜Ä)&Œãdì¶ÁIÛL3üÓÃ88¤¥şÇ1¡.á„LEñä5$¼†„×ğ…„\‘/´œ£ö`½Î#(5ŞÄˆ¤õIŒ`l#;I«mŒ`h#ÛÆˆD	oqZ°cÛÁØiŒ`t#
VcDıØcD=šcDÅĞ{—è¯28:v'@W§ÊPçTçf^g§¨ğ“¹[ç|·`
lã#Šù§ÁÈ&F(¸„,{?ÅëÉĞÄ‰‚y23h^°“ QĞM Lo‚DN‚DA7A¢b=H”£$ÚÁ$ÆéàH£[p9 œ³K*.<ôWÍeNŠ`ê*a’ç0‡u`Úv#Â¿&qx
¯Aá5(|'AáËS‡¤dya}ôs” Äm£DÁ6Q¢`Êé9JJÙsŒäøK¤°M” Ìl—ÛD‰‚D‰‚n¢DÅ3¾îQ¢MQ¢a“¶.'‡ƒOİÄœf@Sgš+]íiR5~pî5§I:ø¦s³Ì4ë›G\ˆ¢›„l£C›åEÁ¶ËI#Ÿ¦(Á˜7qÒœ±Ü&J0Ú9ê\&EY{œÃc§a‚Ñm˜(Ø|4ÂD=˜ÃD?=©w‹>' wvQÁ‰»Fèì¢;ÌŠNNN&N3a'd·NÜfF˜åW%¯aá5,¼†…ï%,ücï­’å×²éj²f×ñ$¡0!Ğ›@:¥.:è´kP*Ù…Á¬t* _U´YHúaºÌ,ş'êÀß&h†ãêµ‹|n *ØY	LÔÌ‘?èDŞâÚø©Ü½áyŸİ³²Ys bÀæ’eåq ùfÊ³PÆ*b“ü Pó´‹¨êVRJó6ò>O‰}ñ¥>Jğ4ß\*«™.Pdúm¬Z6ÙC AèÄrfS23VÆ|¡·“V¶XçVÚ‰¤±J"¦™ÅD·ÿadÇ2<QB‰IVWÇè'R»˜yIÅsE‘1’Îlâ3Äz%
k&Ã³cñLRNÕu,…6'¡¤ÉS‘f7©œJb¹ºBµÃ¯T“Õ˜»[©nBCaœ'úÔØP„õÄÈ4Œ‰au¦xJd"Å6¯Í$½‰™õ“ŒÂHiŞÀÆÜçi¬]“Mµm%Ø@.—
l¤îr—§É,iK±½œÙ”¬ŞfN'£bE˜AZÇHšÁ.´íV€!†½&a†iAlğ•¡ŞÖºcí¿·KnK‘ø¹>‡0ËÒ©Ü•ÖÔ›îK»Bˆ×ã>÷ş_ÿáºó¿´oÏ¿^)÷H5ıÒEJ½Uü(ƒ2ô™Ö¦Šì^¾wtìŞÑoªç–Ï®«ÏÉ=İµ?åÇÓ|w¡<ş0Ñt¡Y¥5ªv>9ëî_ïšó_~ßË•’¨ÿã}yFúÃ5§|—Ö”UI“…öf¢ ÿ”÷Ñ.L²'úOaê¿x/SPYk
Ê–gŠÎêğ•²k
\N…M÷şÃ¢;¾®÷YõıG¨‘}¡ÉX‚c„:BÃÉê	S_-¹¡dYJ§’?ö(w„ô”7Ù>u.Øâ ›XC+6ÊÀ¶®Õ4Ë5¾Ël©Ç®ÅzçkL÷=¦Ó¯~w .ĞBTûİL|%ŞğÚúd~í¹(QöT¶é	‡{.ÚE•^èµŞN_Ï7àÜ?Ï×ú‹TRÕæHÍ.*i•ûÇ£’©qô×‡úY¿;ŞLgi·Û ôÔµšÖæ¦9>R¸‹rÊ£ÿx”ïñŞç)›½ö¼ÜWdªHÓ.ZƒÍT¯ÈT¿¤òdr«è`í)ê²ŒÃÊSÔqUÆi…§H’Óä uŒ¨-ĞÉÇ¦²S¤•¬ÖJG¨:EÍµ©Ôc¬6UKM‘Jô+5”@ª?"«T‰D'Äê
ŠIƒ¢Ï3˜×äU‚
“É¶­±(a$²sfª0Zj”*L„‘à±ÜYï4l.2ëLÒZX—QÄ>(XR$‹‹†g¼å´Òd²²Í‘ŒÎ®›JStš>iÎ|G5"Ú´f¯ºE´‘ºSq*3EKA:+.…:HllHµ$Ò¤ªgR}-GúÕœIQ÷‘G}Te¤Æ V–SX["Ğ¯äÎjK„‘¿´§éš4„‘FŞÎµ%²^}rjK„•Òc‚ÚRÁæÒRƒ°²-;ñ0À°Ğ$Ê°%¾Ñ•;õ—/¨-íH¦wÔ—Ò¸Íá9¡Px©Zs ÉÀ/º…äÓ¡>°w®et¾½Q®½é µÓ´MW^tSğ§KEo£]ø–Í²Ÿª4[ì™Lé—ÂLc»¬¦(¯(Pst_Ò—3•ÅØ“æ‘õv·‡5ræMx>ëúÚ²zŒÉ™Ü_›Êï«'MYÜ”ü½óßÒ>Övå€¥Hâ5Qvmg±/Pkù¶^İå51¼Ë"t±;õcÈ]}p±r]üxƒ]ğãìF¹5l~íL•ÚŒ±O× ¾a$“ÑoÉdœ¬ÄQ¾hõöÁJnõmØ)ùƒoÚp²ş=‚š¨¦Avr’O‹	DwË)øí¢;tÿt(;H¸
À°¥âwD$äú5×5Í©Zì¬	V“Š»4O½xãŠo«™N]ïp«ì¶„qóù‚.`(öãW.?‡-/At,º÷bô{(ÕtŞâæÜXù(¶TÍ…»[Eáu¸¸\ùşQş–óLœñ Æ2´"çä~»ÜÕûû»«ŒékP/ã%¹¾9ÎÔƒñó³×¢C\•Ÿ§¢¬)Í"_Ìµt¯ûOäz‘ˆc	0UƒP:F	Úc”‹3ù5'·m¶Óóİ3~óœ<ïC›¸áÁ=0ïÏöÁóUÉ¾Õú&É¾Õöl²D¢£ìÓÖÃtF¿iºãìd%|Ët†?– ÅWÂU	¿åYx‹XnÔM~éş®	?hÕüÅòPúõ¬ÚIÿxcêzssÿ¤Æ|II?ˆ}›¤ø^’~t¿]îêîŸôÃ˜ì®ïe¼n–~U¹k’o¢×t»“|¾İÔ_›…lze÷Èòe”«²|i¶ÓåÒı³|ó¥dù òY>’»Ç,Ô-²|kn^ÒÇ1öéê¾e/£ß6Ç—qv²â¿i/Ãß®¤ƒìä$Ş&Ã·ù¦¾t×_†½MIVëĞ’>v½Ç1œ¾vc¾¤ìÄ¾Mv|/Ù=ºß.wµşlŞØãÏ=…·àÊ"Ï¡µ€˜ú¶â8Rå éşĞ->†MCÙß^¸?î	tåÉÌs„<ë3Şİ?ÄÉ˜/å6ˆ|Ezä™X¸hÏNôcˆ2ÊUDi¶Ó³¹¿Ê˜/e"_ãùtÁw“7QãÓ¢§¡‰³rï»(íUå$%™:{Ïçµw–××‰G"‡C0|ñş‰/|{#ùjewFŞ˜î*Kå!İÌ²m^”~ÕèZ_ÉP_;øúvö´*Z‹/L“6¥˜åuïÎ·Óó9jù¢e×®w¤q>¾0½…Ïp÷î	­ûûây¶ä$yÛ%u¹¼Nd|ñx¥¿L›"l*ÏDã–«ÇCÛòˆ<šÒóö*†ú(½U9¯™_+"İF¦ÊkEäñ|Bãê’ÇWqğË_Ê«äqÿáÖˆâîˆÊFC¶$ 4²yAä–M¢ß„õç¶Lı!r„ÜJ<Ø A1Îi’æÊS6HšVmëë6ºzŒÅúú˜ÁCêû5€°$ÛW¯£-ğ?Æ K4`Ó!7Ø~èwâ7§›#h×yk…¹±«AO—SŸasavµõ5wıÑ{Âø5|>àæËëÜ¼…Í„.äyÿàæˆáæˆÑrl2€şÇv„I±qD@µ±bp€Û#W¸9ÂÆ¬ˆ„›#,¿ù—.@¸9Â–7›4o ”.ğ>ãæÂxª8ÜÑ°y{Ä qƒ´äË b%Gì)‚ƒ·>óÛ#væh—·HØ z-Êµìà˜:P–dF†€,Ó°ˆ-5
É¸Òû	¸+”şËŠ¸';¡%hû Ë¼Í~H'»¸¿¶ŒHZ÷-Ò¨øÛí€UÍ™\Ûlyö{áû€éÖWØË‘óòâlûb^íh…'ü¬ß™y;øAË¬?Ê‡•7Ñë&4n[2Pdiëg}	ÆÆqH8²ÆÁ/oè™ÿ~&.²öúœ«Sz—×¹ó;ç"İcŒ4Vn±–H‹Òúˆ:S¹c1«tıÔ`E	»Ãûÿ^G(k
endstream
endobj
59 0 obj
<</Filter /FlateDecode
/Length 5056>> stream
xœí]Ùİ¸}ï¯¸Ï¬p_€ À¸mç9‰|ÀdCà	0“ÿRÅµ(İj‘İrÛÉ´í6®êŠdí$KêMé˜şÜü}·‘Ë`äeŒáöãO??à÷ÊqÓVÄÛ/{øËonÿºÙ¤ƒ[}îa¼‚†ò†ÿô‡[şğË?~û}ûÇR>ê›”JawO·æpëûÏ¿ıdnñöùïĞQâPŞ´ß|ÊŞ”¾}şéáwBhûûÛç=8øşó_o@PaO0{‚OßZ$Bàû2t#ØÜ$6‚É~ü|ŸqĞÛ¦dğ„séöƒ¨İ Ç;ö¢›ìÕ!õÀÜÁq®‚¼ĞxaúĞúi¹X¹·zÏîñ43Z(ÊŒg™ù#üıùAJ·9ücnU¯,¸°’vsĞGwc½¡KáùiöÎkÌ¦¡õ©C+½È½E]Ñÿ¡İ‘}(±¡[í§zaaÀ/xa0"C¢dê†78m´,4mÍE¡Ú}ÂÈÛØ:H/]îOo^¼3F¡B2ø¥„ÈWJW8(´•ğ+M´qx(,ThABw
ÆÒ*ÄBs!`c\Eè«P_¼ÓAvğ¡Ò0êÇ\ôíê^mZKÓoFŠ³BGÒ%Ò¢uÎƒ»6åT4„M¤Yˆ8HóÎ{GÅv1nşÒı Mˆ‘¤EtqĞ7RvVË$XĞ"­Ú8·ªæÿò@ï
háF»E’+İVmå¾pHdÃ
„4«ü 9Ò<øyÖ[ÕR«ª.ƒ€üîÃ u¤iá³ıš}j’–º-¦Öå
eWº]|y Ro§T»¥>× ŞYY%N\%¢ÎŞe'QQ•Dƒ§*“†Y×:Èj¸ÅŒ$Ê|ø'&ˆpËÿ0/ÔÏ)¥€µ §¼¥…·´ğ–~eiáÏë†²öÈ=ilÏl3æ‰5êqÈHÓväH Æ]šQMHÚ§	¤ÁÅ˜'B”‡<´}@Ú1O uŸ'-ç‰ü±æ‰|5æ‰Lü°t9xl|ğíÂæEœ!ZšÜC\Ñğ+zâ´i|ˆèlš!î‹[fˆ¦ç‰dş!O e—'i—'mŸ'€è@4M$’U‘
hR×&€êiŠÀkì—*<Ñ€ƒ1E$ªIúiÌ´š"ÒUMåbHívâD­[ân„â˜Õî¿IâäDæM9$hªIt]“0lV!áZGb{eÑğ–Ş’Á[2ø?OÏ_* ˆW³ƒQBÙ(b¿¥H4m†µN¢¶F‚›Œ[ŠD2·Ts@Ûm)€öÙ!Ñ‚Ü™h.Ä1;$ê.;dÚMµ¯kv(WCv(´ÁK—ƒ³¶Á·.l®_Ä‚¤Š=DSÑ¹¢Eœ]ß4Œ«eh´WÖ|€6îÙÍ?fD'wÙI®t[@Z´vÌVŠ}v@’+SÁ‘æ]Øe+åàúvÌHİg‡DkÙ¯ZvÈcv¨·S'Êİ“Qa`·›(¬Òä€ÂPï"“X¨º¡!STHc««šFa5
Öb;ÚK+…·\ğ–ŞrÁÿu.øóìiÈíß ğME	şb£Ûğ¼ê'B{'eFâ*É ÉlĞUú†Ô(dHTè6‚@4›Tğ‰OD”5F9‰ô°Ix¦0ªD,Q=Š†}€›˜ÂP“.ÀK6¥o4´(0m¥wCk ‚Ea‡‘€ŠGr £‘/¥!`@Åƒ@”o~w ªâ`•Tõ÷e A¾"mqê(#ÙktÓÆ‘ƒ öYÎÂ½0¬@ÓEN'ğÈÊ`À4}dšM:®z«44]ÕpoÛmÑÇèv£Ütw¾»3tù~„ˆ¦…C/¼Y/‹‡uÚ»PVñaœBZP[ø†"v¬FÿGã)HTï"rŸs˜¡ı!RŞE\fGjİÂGğÖÌ”’º:VcS)‹cu*‰!Ó[*o6ªPŞmaãå!­Y©¾•(¢$,D_‘ÚJU×—‡Ş±c˜-0›´1,ğà|Âÿ;¾´Âä-NãÜ˜.àÆtg‘Ï0¶ISAÓC¢%fšº
	xi:%-«îÉ ÍJ+Í „iâM¸ƒÏToZ8¼İğğ8ÿ‡y—E#¥ï“ÒÙ³„¾Ìpúlpçí‚h§Ùô¼29Ì8{Ü`b
y€=­Ö5ûv0?D—ú&ÀÏ'øy„ŸØ†š„ÜRGá”=HÓ…°øó~öçïÀÈ.ùûÌ…šP¸C„j†€¹‘ÔY¼@ÊãŒûL%Ü½²ü0”.Üqˆ£æÏ%Ÿ‹qğ¹‹}ÏCª‰:»^	ED÷³°Æ±¡ˆ,/P¾Lè×(Ò}½Ÿ¨g2Œ™}w3õ°\ûÊQÜ‡¨Ql~¾8Šû0§(ar¯åSTS
ƒéÿu\°ô•]pé~X/¸ ínJ£Ö­İïkİ“ÕE79'¢~Ä{,JËyÒ|,¾öHhŸHUGqÅû¦×èD¸!‚in0£ÂF6¡Š{âÙUÁşW©¦åW$ní[]ïZ|<ñÅü[³Aöq;şß_Á¿S›©ûÕø‡Õ¡z¯ÿÇ+ø$N;ÿøsâÃZä¤5rÕÅş:{tAw”FàÉ‰®¼˜¹.7øÓ²×vî‹O¹|Ü]ÆHè\O6gÿ°	û"{Ş7²ÍË ‹{Èè$ùB•”ÔÑè¶6°g#_˜Ü v5ÁÇ^[òì‘SV¾l`3$ı)Gæ‡:ì½ñ¬.m>½ZDÑ`/Û¾¥« \ym_ 7£¿XÉ` k'æ¤¶JOxÑRrüÈ	ÇJÍ	Që›7c4lOûØºj6vˆŠµ/ÆpgBËËZ¥•{Å Æ¶Êê‰óšZB¼)­c$ú[75ß•åÜ‰Óø2·l˜–’oŒ­Â©_¶ ³Fİ^±~0¸hÎ=œu§ûşkH—fsíĞ•ñ‚Hy
?	Û¤(l(Ó…aCÀ
³(%aC>Ñ±<° bÉÖlğ0ˆ¶Òüiijmb¥PìµÒ(öZi¹ìıwŒ“rÒÑĞÎsGM»l”V¦x‚®V]}h°Õ7Şf´¶D¹EÌˆ°–pQËt2ŒĞûº„‰ˆ˜{ °+GÌ5(àJšuİ“º™fºE	ãİôDÄ£ßQWh¢·êñÜÀ¸+,Õ`³èpÙPºˆ5™07)‚çEÜT,]#¨:J‹Û¬†à­xE±V¼¦8kº»!•¤¿†i7ô“°ØPR"JCS«Èa­ª¡+ĞÜ¦u|Ë @D#‡c•Î
èØ@V ƒQ$‚²Q—©
h$
³6"Z{ãªn:F3ÌÈO³!å:E“òà)ßkªA(,êHÉºÖ.ğÃ¶Ö ¦@r\@!Côú	¨ ‚«n;;¸­Ö¡ì¦Ùmû|ìÔ]:xAúîÈ ?¥a]/Øœi°¡É{3Âéé¾v»u·NšMAÑø§ìc_Û>û_XFtî‡×²j»©³{j$‡KH“0qÒlÎHÎíñ´EêOE#¦Có06ñ‘ùş­M°~>:C“„#ZğÄıvegŠ8³ñ:2Ü${í	ĞÉûa.û~’ aç;O‚”Ó…$H›ÍÙÇÉï(	vş’ ew!	ÒfsFj'nKI0–ïùşıø¸K’+ííŒ
–}¥ó"Ò¤
ÖÈŒl'D¯’Få©o„	|Jì~Ã„ß0á×CºT€«‘.ê†œÀÁ¨M(C€.ø$£@” ±R˜èjØ¤
†¥V·É
sE¹
‰ E­o*.şÔø%@Uk •ıw§U-}iÀ‚·@\@‹`¸@.Xß`)pTÀT	~Šˆ[“h
«J)¼•h#ÀUHâê-»Òûİ<”—nÈÎu·w—îè+GtKù\˜FÑ-à®â‚”æà£$àôm¼†œsÁoC[‚ÀVşvL&ØŒ'ì¦’(ÌÕˆëê;jÔÇè e¦cQíZ5é:¶\+œ­´ª,Šwf»àƒWËU†… A¾‚ÿ°¨ ¨ˆ–`]Ğ5˜Za©rSC¡`W#R°‹´®ú'ƒ4Cì4“Æ©‡T^óÍ.£ú)ôÌ&[W~Í…Â
s%Óš³³ù}nş°8·l,«3å	©8Ï¤òÚtj¥¬¬YÙ~3ã56¿Û¡ĞUväuÊzé·sÎz¾â1(jß”Z³jD•}|šG³WS‘vÂy5’şX6§Ÿòµä³êŸú®¸Ò°ÎtuÑNí
“Hg¿›©x„q^X¤˜úÕ²Á=We“ªQÒıŒ]«Gf¯|9Š42`‹³\á °á©EidˆÓ’U…ï]Égƒjf< Öİ»’UÈxjÎå ïiÌ¦ßC—º¤©ÈÎåÏôº\2Êë{f/³¥lØ’À®ğO…ë\Òù¹gÂÌZêÕLy¦x¦djã™î¾]â™Á¿†gÿ]xf Çi:½Ğ3[çk–AWî
ÏT—y&eèJÏ4í-¢_Ó3û(ßÔ3	6/î.ôÌŞù’gRÕLy¦1WÌæ®óLÂĞ¥éôÎ3/{nˆzf%ïNÄ&O‘¦“–jÊr/ux)Ó
3óè)µ­Û§Çbmò‰w¸PyßÛ¹œhĞLó%€†—• "M5ñªçjJÏÕ¬©ËzdÜ¬‘œU™ì_¬%¢•‡úd»`‘;”s2»yty8Ï‘ø¢†­êµÑEfVÄ È	MşBªVDÑ(=Ñ™­MÆÈèE˜`ì#I>ŠAìÓÁ~)†s†¥(AŠúcåù±E‰3·<S}tUõë°ÀT3»q`'çYøƒ'‡ãº°I¸É5–úöúµ_`v”İ­7£ğúâ4Ìj¥”üß3<gÅr†‰MBŒVw…•£ŞÂäË‰ñ[mUÔ6Ìã)Ïxúr_1ŞÊ	ÏçÓÕ¯ŒÖÎ„/æÀ²:Ÿ*sJ–ÁúÖ‡qüÈôÅ+Lsf)'ığÜª$'ô’ûf_:2‘ØÎxëœ)â±|ÀÇäïhèñÉš´³êpmñ +E^ğ…˜xd)•“3”Şq|—ÎnŠÂóÓñşğ+åX~4©¾ªØ‚Zâ”‡ğ™¨/Y®Xç–/çàÄàKIØ'¦XÁ«"‚ò0Ó™zU-‹Á‡pEl;ÓÓòĞ¼Ø«tu)ga1 Õ'nƒ”=Í:¬Ğ8‡7'a1Âİ: «0³áI¾7LmmAäƒ}¼ÉaEDôtòà¸šsÂ ï>•8Î
ÈvU~?×Ü„U/Û/;­çj75Ê ŸCğßÑÕ“9!‰q]»|EÚº¡¦kä*îÎ”âëlwÛ\{‰³óOÇ®ö,>îxâ‰äXDñ-oç‚ğƒ³Òì=,ùhò‰â°®<vÅÎ>•Ü-¨„’3)ƒSâ•iéBo§1h§<³G‡ÑXâ·V>sqÆÍŒ§‹ÃŠ ZoWf¹şèøÙâûZ[.ğÙU,õaê]~úıÔÊ>Ü¿*Å·Ô»(œË¨Sc¬Vó=±EÉë5ÚËÕõétçlî q„¿—åÜàìªâeÕØtÖå_çö9K6n=ÅçY]úº
mØ@®÷‚yµÆÜrqH©nfÕ½>‹±Ke_v°Ü/;§ŞaÃÂr^XÆ^¸Üx=‡;.*±úc=ñÂµ»¾}F’álş*ŞÎ­ˆY•èòûZ7làÂá¼ä¨İñ°.Nlp‹'ëBÕÊ|2t`ğíï ¨xäUà•œ®¬£5,6øXÆ¶»Œ¿>Õ]8›.?éÅQüòbõ),võ´¬Õ¥õº×ÁÏ€VÙg§–H3b\¹^å¶¬µgf†©7gÍ™u7c³ùrnfqç¬œ®œxA¸Õ –×A	½Ê$åyw| AmÊå'’{ºo*6|Nß™”½ƒÙšø©^š^feî<¯ê±Z@Ç½ZØÈ˜ü[È$ÄMR>İUÌ\=é*¿=n><á½Cb`3Æu]ìÖ—=¤9áv~?>³»É¶½>½Ãõ<W®?ê|İşóJ•°ÇMìRˆ"µ¸Â3^àx6¼x•²/-c ëˆa9Ê[ğè„ÄèØ°zÑQ¶‡’›…)…9x0ıEç³fá7lŒ-~átÆ§îlc}Éo¹—0^8ßx"ĞiVWÀ,Ï`wyéø
vë¸ßbù ì°ÕˆÌŞzİ¯””(Wë¯â˜4µ¬)_â—íÄ¹5¿’Ÿ:rÉ:¢¹Ù²áø³úmÏÅLN¿¢:¯õ"³İ=»¢ÓÈ«šÀ(..Ü<ãEá—½Æûü5PG¸îŒìÛ£3y© ãD†~ÆšîHÿuË@şeÙİÖkÃ®¬ÕY_Û¬¿ğËÖõ2%–İõZoY.óŒeİòò»…Î>ƒ1Å¹"/3¸ü!ˆ¿dÖ6šÁ¥†53ëî×Ê^XÖ<|Rë¿D‡«
endstream
endobj
61 0 obj
<</Filter /FlateDecode
/Length 3871>> stream
xœí\[oå¶~?¿BÏ¢px'Pğz×ync ?`Û¤(œ Iÿ?Ğ^‡”è£ãÕÙ‰½ÙôI$çÎ’ò*Uˆ?‹À?ß¬ìÖkX„à—Ï?]~¹Ğs©½X”aùõß—şeùq½‚ÅW]ê¡¿Ã†°ĞŸ|·¤‹_¼|ûZ~ü_ìÏµ HIİıA¯¦|õÃóåÛ'½„åùì(R‹r«ó Í"ÕòüÓå¯B(ó·åù¿‹ÏŸÿµ  ıèppP"~Ş@TLj* S§Ÿ÷	G¹­¼c”ƒ‘Ã Û7FV¶MFq€É3Ê¥‡Å£Ä3Ñ›ÖşõÖ¨åÖZ¨‘Ü‘~ñ:1JHNŒ‰©Jø;şùå`WK?z½4hÂÌj±fÆj%“¢!ÒkösHÔuc–hş:8‘¬y»áÿb»-ˆ}H±"]:X¿üTnÈ3^èF“7úˆH"h¡¬Ò
2¦´'Ì!ë{BÃò™Z{p`S°:%éÍĞ}2¤­Z$ ×K©
†Æ‰mé™ÍM©¦÷œBI¨Œy@ŒÆRÒ‡ŒYï©1QŒ+o…¨÷Úù‚‘”ËÏ\½{¡»U)ĞíeB¬*°.	ÆZW±'¿J+‰àJ&aFác‡0g³œmÂŠ®šÉ‡0ğÒ3)¤D°¡È[…ÜX+kdÕŒo’
5Ó aEÇ©UQÿË…¿JaáİdQ,œ Â‚1¹«L)>"),œ!Âª™sN˜³>Ë­ÈˆŒ˜Ëï±ãNà)á’êªjÕJ/\±u¾#Z¥ª7/nåunD¥[nn n˜™Rf¾Ä7ñÆ1ó…"î2E„Ü¹š¬¹­pwÍÊc¾ıùò
~IÿQ4(×1 0’¼ƒ÷`ğşÁàûr„œg¤Œ	-:Lnûè€ˆ£CÄ†è±Mt@T¢5‹¢CÄ†è€ŒÑ!bCtˆXrP¦ØˆÑ!a1:äËò]2ÆL°vÉŒ•Î¬º’É,¿²Ã|¤±Íœ©Ê§ù\•"sN&oæÆU3ÌÛ«s<ˆ:®Ñ!ª¿‹„Ñ!BCtˆØÜD‡ˆ™Øaãœ°Mt0VtÑî©ãNâ„!	}xˆ(ËÃCÄL
ù:‡|Ó‡Œq*]r[kƒs«,d2ã%N¸7~™'Áp‡)ä®Õ$Í°è„;kVóì[…÷Pğ
ŞCÁ:¼9M°Â›l0Cl°Aoba”ªrÛÆÔÒô‰°16XÌ}C°]l lŒ„mŠˆˆ±!b)6¤ËÒ]ÖÙ_î²³Ô:xgÓ™ÌÎî3;ÜC*ÛÜ•Š|˜Ç)r×lòæN\4Ã}½h°DÒqQı]l dˆ²¹ÛL@Ä‚Q]l@Ğ¢xhˆ‘31‡$u¡!¢!¦ıU”ˆ¹¡ˆĞ¦ˆèPG$¬Ôñ®Ä‡|ÓÅ‡ú:³£Ú-³8F ³ÍBi³àÊ³tÆys‰*"æ9E’ÌÅ˜Ä™3Vİ0§-*d~KºğŞCÂ{HøS„„ïwöÓrz·UÌ‚
ë¶ihÏ,›ji[Ê ÁÄÍ‘¼ï•6Âü*”	–á2ãÓ «Çı²~‚bòŞÖ*µÂ¦í½™´‡cP,ÀÛ‡Ğó£!)Ûƒ´gåV]9ÖbŞ•)cklmëP?NÆ¨lXé‚3÷à¤#­3wh¹Áz&@5ab6tŞäô£0…ëœr7ÇT€s]|Ê–ˆTWÙÈ[³[¾ç¢}¨öïP†‚™Î‡Ì8¾ß™í”ı”x‰ˆpNÕLsmp©á®uÈeŒg¶¥'~Láw‡-„÷ûjÒŞíÛf]uíÕ®ocğèbœÙçÃ³Ó®:ssnâ°¦D0œ°Â¡`1#w®Àn3ˆÄÏ¤ûP`¬÷×M¤(Ct`Ñ"”H«×öº^çœkjÚÚÈÔx¦aáæ6“íí&=Ò7[Õ1gæNp$RœOœñÊ¤2•É´ÉÔ‚æv2Õú„`xHò¥<s!x¿ÙÏç¬ÏÆ˜38KU¦4b6 rg’5"µ)k¼aç8›ú}™w§ÕÙ‰7óäFÑÉv_â³1ò)0”Çê¼—„R/«6>•Ş°c»/:'²èä#òü‘b(©ƒø'Õñ¤iŠn	×X‚ÀÇLĞi1: Fç¹£>(]I}è'vÂµÉıÓõGb—¤GÜQôÁ¿7¢Z~¾`Q¸Ê Xî€´ÊĞ ¬¸â¡ª—ŠiÄìŠ6ˆ–@N¬0½4…˜Æøƒ–ÃH,U`@•–•hIX®VNÈ°vYépxOêŒÃ&„°,vdğ£b0 ¥€kï!BI0­{„èĞRÅÕeà#T£;ÆÇ’bÛŒE1½ô Ö‹’R«6‚Ø4xªj+1b½AAb.“h«U”t7îÄ’K]ªu‹h¢L‹¸
FZ*Be›ğÙ0MOIM¥Œü¦{Æè`5T¹’1IA'Im„…ˆKV0Becâ¿ÊÆfª†VÓ¥Õ(™6AcB¡`±ïÓj¼_UÕ:.™ZÒÀlK]O/¢¶iÙJ[J I›ÎDSJYš‹òB×fÍı¸ë[¢Y ï…é(æ‚ääbîD|ÎVÆ\e?¶ÍX”ÑË¥5D@®}hÁ¡@±dMiY#Atm„J=fºö¿‚	KãÁ°*§i­¦J!ƒ‘ *­
"QU¦¼y‘=§j©§©*”ÓÏÍ£rÚÛL1¥ƒg;W:Wšş¡Šå=2¬ŸÀf*Ôt:ÆKW§Â£1Ä²#­kœüh'¨Ú¸—3‚uÖØŒâjˆDËÇÊ‡‚©£œZhIg¡2)Ø¼÷ÄJ8õ»?ê8Ä5ÃÛnŒ8eYÁÓéò…–.hâƒ¦IòfÀ`ú…Arì¿O›vÚYhzd²¸Ò,éÇ&;úçl“äH9ƒ!«şPÙÓäjèštT˜ã÷¯°ÀXkcâ8*´ñbşàSÇ¦¼Ãf˜nË{QÏ9æPÔËçêGÑ|b$<^­¢•ÛniÄëN#ÍE§3V»$ïè6çÌŠ•²ÏDRÂÁ¥İY@øÛÖzwüC"¡èİ)§ñl'ÇI RÚF>G
è0ö|PRŞö¾†xïáĞ˜‹”HØF"w–Ÿòh:¹iÔÖ¤D ÿŸã¶TËCÜ¶ãä\sSI[[.ÔË_}/ôºü`·ŞCÂ=ê=ë:ŠÇL™2›’LxÄ\Sh/_ŸSûa‰S`^şŒé)Ëÿ6ıœ¦’¥U
€y1ÎÎóª‚Áô	ìÊ?„õª,ÒÌ
@ãĞ¬¢–µ×ÊZÚ^K$(y{­¤Ú ¬êâÄ°
­Îj¹Æ"eÌKP¤õÒcfÕÎxV"†É1­Ë4jğ++dW"ŠI¶§­ôÊ^ÄÒfaƒJ)r“•YIEœ­U“{ë½©ˆÓÑ´Ù(njoœmíe[øI:5íLWûáˆ}áG$`Õ	 Xå#$:…äEÎíX}§xíGó

@tÅëfMxXA^¶Æ­˜bƒ´Â«£§iŒöVÎ1.[Ñ'‡*°Œ‚h°*å-«#¶¼bÔ †:vÙ˜
áˆ:$&.=şKKMâ%`y	Ø°!ªª:bªVÙÌF*{»¹µş;˜ª]¯@o©Ú&?-.ñ0ŠÑ1Æ»vml‹ÙñrÜöy2ö%ç>%«—TÏÂ‘ÌÅWJQÊTJQÈÕr§\°»åñK¬¦¬Hå£…äš¦´L×‡<ÕÂY9Œôkú™zLbá¦¢Ï Êœxf$Ï”h<‹ÔM&zrQÁû?&µ-BNXñ0XÅß{Åƒ½ü!{qV Éî t+ênq¥«Ü»9)‡ÄîäŞ‚ÃUdõ‹Êï²0iD®Ô9i´.ñ
YQš~ ÿ¡åÓº‰Ç}é›ÒvWú'®g`§«7Aù½k…‘öa•ƒHi7l«¨×ŞÇéüëT©l¤X¥Zæ.\ašM O¯+8ºtQ°eFq†âæ :ÍAŒò«ëNXÇdÍ©B†xøEkN©_=f0Ep1{armÙ`£Ã”˜³Š·×‚Š>c)3E¬±èoÇâ1QÛßO†Óhùšõ˜Ä¼ıúKô>ëÿ”8’¶ííÉßaï0ÈKnŒ°söA°°+a»u}PFR•ÑNº‹œÌ0|G\ûÍ2_"§¸¾’Ä$·Éì«bÒ%kÓÃzíféÏ“HÎGô¬6¼yè§¬¡3rd OóÙ eb·¹Îòp÷‚ q$£~kapš\¤wköïJx]C>Ã5x"Äesıl«·ìXÂ¶-n4>óXñx ŒÓÚÑq?åï#¤hüH#;Ã Ã	’a;™¬û«IßdZ„1Ë¿aº¸*an†œÔ#áHC`¬ñ¿¿iÁÌ¶Ú8‰˜‚9~–bcïZáe„­Õ WÜ!E+ÿEÏìù;âÊ+±§2ÚÔ³Nşäl rb£\u]údÎë±ÙA:;Ñè¡Ø}ß$´G Fóñ'Iº3w[q£Ã6Ñ?Ã°è{N@­û£ê½~œ‹ëú?"Fú-¯“ÓÏu¥ßõÑ5ù0‚õ€A”­µM×ÎÊ}Ø™/ö¢ O‡¢Ïì<}ë”9‚NtguÆúõEU±–ˆÂÕtªµùÂhå¦0Úš´e¿-»î4Óï~˜–!K¬p‡O>ñê‚‹ù~'Ÿ†ïÅ-WÀ¿=ÖdëÆœJÈ ¬A¶ßÔÑ¯  ¯û—áCì´®}Wš] ¬ µ·vó‹–Ãj•±˜Æ-Ã‡O;&c×O¨œÃèÅ¾‡R“Ş@ì§ı¡óGIzåØÌİÈCs®¨@;S ¹ÈùsSd•¥÷€“âæÃ,»:‚›o
ÃŠ¡Òköp¦<Pºí„“£lØ×eƒ‹Ó«ê(lsÊ·XÆÖ³SÏæ™œSäRBPŒ9´Ô)Ğ²RI§~ê™<Æ~J^"ZAŸéDÇşY¾ÿ­Ç¤
endstream
endobj
63 0 obj
<</Filter /FlateDecode
/Length 4058>> stream
xœí][o·~×¯ØçÙpx (`KvÛèp›… éÿ:ÃËr¸{¨İ•VVJ­sæ,9W~^ædÖÓÏ¤èÏw³x-ÌˆqúüËİowü¹¶QMÆ)œ~ÿçİßÿ4ıJt;ƒ§GCî¡Gaâ?ûaÊ/~ÿùîûÌôóRÍ 5w÷S¢(~4¿ Gßºûş£púôu”$„É„9DĞnÒfúôËİŸ•2î/Ó§ßyúüÓ?&"è¸&Ø5!$BXF%B÷f!¸Ü‚Í~øt[p²Û¬!!9ø5½b²}b­Ê¶ÉÚ`Ö„Á#Éu„)’Å‹Ğ›Öøxkòrk­ÌZÜµüêqaŒÒR˜°fqÂ_éÏow ~öüc'`ÓkG!¬ÁÍúhalf)f‘_‰fßEUŸßhMCÀbP9¢gÔHşKí¶DêC«™dó*ºé—òÆytÓ~cyDÆD±,ÔÄxcš±‰æQéå9eaúÌ­#ğ¹?3cùIDB…dùC ‘¯µ©4
Pjô™/M5µñü\0<Th¨;M¼ŒXh>Fn¬I*t¡>Iòò“Ğ!ÄJãP_~¾ó–w_øİlØö0S¼SE—LCç}è˜{Œ³ö­“iÎĞP‡iÁ‡à¥Úq¦áVØ‡iuVd’Qè±³7S­ñNÏ$yĞ
2­ú8·ªîÿr'g
Yaİ&’/İ]•>KJDOV˜„>‰ä4JÅ-HÙlÅD‰ÊA'LI´@}K›'’Q!{¯z'Qm²ÑâÃLKÖv¬¹6Ë›/w">–ÇE-İŠˆˆØ¬’¶^ô‘.4oCb1‘9Õ’bˆ	‹‹Á¸øFÚêB1Â?ßı‹Á!Nù?Æ„ú:Á	¹ŠğäŞ áş áÇùBÉ9J>†#¼¶Ç¢˜5F$Ú
#½ÕaQ5YQŒH$Ë£WXi+Œ ¬1"ÑV‘hŒHÔFdZÂˆò²`Dy×aD¡É(¬]ÊxmÌe`W1å ¨êÈ¡²¨-ÇTµyÕŠrˆ6{ËÁ\=#Ç|õ`EöqÃv‡@Lò6v0ë1‚lÁVè@‚iÜ,5gZğq>bô~LÚS× ‘h@ğ» ò› êã2ˆj·2Üš 20‹¤"|YâMc1ªiä©&”ƒ«ÙZÃê9\‹óÄØ>•0¼Á¼Á~<º¹1ız”0`”"hh
aÍv«;2¤¶ `b* Ø
qV‚„xD;ƒ¦Ÿ)ø9åGp6cµ‡)cj‹Üš G2ÑÀV±Ì0$•)æ€ø-;)½‚>¥7dTNôE4Ş8SØqÕ¤9¤|DÎºƒĞ£Ñ²¶©e¡$ƒ|é	ÚE3µş‰hfÀÈq·ˆBD;[@Y£"5‘Inƒ>©Rô""%‹ŒU÷LtÉ~Õ<•Æ©ö›¡›æ“N¤æ>!~ó³Pt^6Zñ^.ãè— Xšì;A£ş¢Ò›DSC’¼¼e¥Ú 	{ „9XsŠMCˆCŸb—>vŒ8@ƒ‰^èÏ`ªeJäx,Ö+¡htGU£?ØÙ¡êúÓ3V³Ã$cM1£h)¢¦—à“EU
-,*§¶•¦«µ¡&.Æ,KåÀŒ<½6aÒ<£Q™Üc•›¡İ:t8	ÕtâmSô,úë&P3’nivÍ{>Í3LÍ‰B~‹¦}œÔğ9±£:ónş‡Ñ‘³›ÒÖ;iC˜C£Rn	[^GgË°ı@­RÎåßüŞ°ÛXhš~ó_Šw{O¿=o:Óô¦òoGÏ{ÕmBoyºº›/X¯ö®G¢sîyÔU5—U`ñíCQÏ³èµŸiA9ñzÕNdwğy¹&ÖÓ•Š)JNĞÍÎíˆàˆ¿F}Ì°îù˜"@µÁÇâ6U~‡Kõ'€¶ŠCSò{¡´2°êÿ ŒÚ<OùEç8¥O1K³¦åÉıÒƒ¹_÷lú>Û5Ù9^ sôb£8æÏàcŠ·|;¶Ò:Î±XXp=daÊèús*Êµ•³^œò@—EäØ#K¢CFs;õ~1±ep&0Ç|Ú½›W;;/Õä'ş&fvI4ŸÙ/bñvUâèÈÏ*wADXæµ¼÷{şq¼‘¦x¸uÓ[)o¾Â­ïJÄ†æÊ¯ãbšƒ5­b¯Ëc.~DÔ#îNñá*w§¥]ÁÔ&şÇå&„
1ŞòàÇQùsÏ¯¨Ÿ­œ"¡I“]ë=+^`S>IÀ2OIáE¦È{fdß¯1ù²y6­V(ƒŠ—L²†u=ïMFç©ÙÂáÑğ±v`†$¤pk¿=1ÀS2¯jø5éˆ~º×ª<÷.#Y·ë<\¡&Í$¶´}í?)ö*814¿Ûj»O:D7şÚó¯7ıû|ÜèRÄÆ¸¦LlŞ<Œ¯HG¹Åë Qâ6…¿3—Ş“ÆËüvEB*–!Ë.> ğ^AÅ•º?b+’OYÏš'À_¦ƒ÷yœÊ”æù“ÈŞD¯	¯ƒ»e¦=³jõt³Ö ®]O‡Xç9!n¹Æ÷Ì8N»„Úİ2ÄÎÎEçÎ4Ëö6§ÖSdñš¨ßåÜ»¥)PÎ‹„Mä—¹(7©è1?ói‚¢@éDS$…Ì‚mùéÖF/£ócúÀò„B×²…|!”¦2ôš/,F=Õ0‡€J+ùÊë¬¼FôätéÉ³á#´¡~`œ§ì|—…y—èd"à+Ô{_º2 @»ıiï‹Ş`"‚ßµÇiµ(1ìÉ•;¦i§˜ïşìÊô0Ğ!vq»Û®1]ÍÍ¨[?¶Ä€Q¼SkÏñÖ3òÈÆÚD³‰&>a0t\ëìø=¼‹Œ±<TAçÃ‹A­”=Úu4¥rD­×¡L,¬Ã aí»-báIª`6Q`èjû¼Ï›jèğqW±nãĞa1Ğbñ…ò-úµÍùHø,sÏycw¯¦¿Es;ûgĞ6:  ‰°ô—ÑolÚ„×²+Uu§µFwÀºutxŠ· ”:ª€­çC9n³k®t¬ÆŞ3”“ÏCÑÂ°ŞÚîó¾pŸ6¡sÃ(m	ş *ìÃáÆáÃ®N·+ş®A$Åm8 àp‚€,àb,ÓY4Ïù°5ƒ¡qŞáBZJu¼>ĞBFaÜ³1BCÊ|c|éX‹á¶İ]`ªQš7x4q‰‡—TæN!<bŞCèÆ÷vèJò©hmI£@‰¾ŞWtCƒÒìÂ¤ŸâÏ5Šİ®«Ğ#ı4ê¼	åü'ı7P	0´x8ší¤¾±.‹†è9âC@r#‹AòÂ9k8=yŒÅºnFMæ™cj†™Ğyi¯›„^sGUÍÏ[ˆb	;Z ÇÓşZD¢{°û<ù)@NZCÜ98få”9·C *1z¢ãiù	ÙÂ…(}:¿ó8 >«)ğuû5lr:€Æ]ÉÜµ~lpF¹Ù7ŠĞ'8v”=.ÕğÊnmÎ»|'ú¦$ÙÙ4PKeØ‰u(”òwìK%‚T×Åá8LÎ‹;ËjH<0f‹Tg•Z-ÇšÙávv¤D½ìeñ,¨ÌmÎİ~Îu³üı@¨ú…‡w¥ÔHä-9¿¯ÆşÂáY~¸µpz3w ßB;»1{šÃù´øäşËùÆ¡GÇ²['wÁü¬…òó6yÆ[C[]·P>\ç½T¶3†í!÷ÑîÏùäw¸ò&
{'†+ÓòEBëëøË±<%¸9ˆ‹3"Û°ÈÁÈ;Ï4Ö„tÏôÎe{ÙãX=½¾ğ áu¢C 8½»qöüçUw¿Ïj÷„-³Ó#ú	Q8Ü>…C©z8³“P.—CŸp1Úa„œ†ŠÓ–=R°äİsˆQO³ÚN„¿åÂß†¸ÜaÚî&‹úºñ«ùŠÏã„Ê×~ø‚ß#«÷Ú?¨åY-IèhŠ¿3­ìğ}Áz¯•­éú‘WéšÑrí¨Ü¯Á¸ŸtŸ­|^ï²A¹'×î#²5T¾Ş´ÏSªsäUY ¨!İŒ“5ºD¤ß¢(Ñ¥|?Î>¸(ËAiòæÑt%ºD¥3N–è-Ë$*Q+I–ë.DY´»EìÂCÔË
iDií"·¨Á­êu¤lY¼[íõ¥§‘IJ…‡a“XÎ–š4†âùJ,Ş5É$‘¿£`Qhü­3(Kw­¯Ü-$Y¸ÛZ6ë7ÍOR–æÑ&us|Ón5Û²]C‰R'Q¢‰Ö—xêˆvÖÑƒ,İEKé'—(E«èbWº‹†ò.pF–î¢acˆÂÔLè
x3©«á-ÍZ9lë»UÎJ!Z‘m·Uã6µZÉnÕ_ÖñVCÉR^¢Å9šèE%¯á;õ4àAˆC4¾ºšÊò›àD¥PQäÒ¦ÑxœXYÅ[h}ïB”U¼¢uµ¼`²¸¨gq¦\FGUp1¯VÃK¹{½«ùµkxëc7[9UÄ—_§†Wp¾¸†Wô|Ğa)ƒúZ5¼‚'\Q{Ò[6œªât/Q¿ë-Ôç‹Õï
_±~·ãzÄÂÖè½z€ÿåú])ÿ·P¿+å=Q¿»uÓ[İnõÌ·R¿+uùëw¥ø'êw·ÜóxPçÛÂ”ËjÑDï/Q¿Û	/"ğ›©ß
\\¿+{>Q¿{3§v¿÷áõêw¥t°ú]©Ú‰úİ­¿öü«w¿ âEêwã¯ßİ*¹g»Mß¯ÃÌÖûÖï
.§êwoêş¨­üú`ğV¿{£~wc¦=³Æ§oÂ+Ôï6q¯®ßİâXıî­fW¬(};\½zğ
ˆh\v/·v3üú|u'È¼¾õ=Biv\N“&ãd¤í˜­÷² N¦²y¥ ­ÁY–`5Y¨“-m=ã¨ã4MÖ^äü7&îŠ7êD.å¨‰@jSÇ¾ÏÄÎ2Ï˜Ø£š#Ù%Œş¨“ìvp¡“Zï¾?4JÆ©;e½×Ñ”‘Br½X¬ÜjW¦{W¯‹ƒïÈÊ¬‹×èZµC©ûÌ¯t’·m–¬¯‚{,}»>x.O=¼á-÷˜`è–óu¶W{°í÷LnÃläûJßÀ_°>ºf*å–"
Dš¹Ôæ69ğY¢3âzo=Š 7W™,XEİmêã¹/ÑŠ&ş¿'9¢Ó‚K½0`ùÚŒÚÜSvüu×`Sçåf²8†Í…Ëbïÿ´P@
endstream
endobj
65 0 obj
<</Filter /FlateDecode
/Length 3719>> stream
xœí\Û·}Ÿ¯èç nó~‚ Òj×ÏIääØA°2`çÿTñZìn³wØ£ ÑÊ’gª›¬{Õ!›½«>ü,şü°’¯NñÕsïİòåëå÷^Ê±Ejæ—?şyùÇŸ–ß€®VnàVgh¿Á@¾àŸ¿ı´Äüzùñ'¹üúŸ0Ÿõrá\œî—@axkü ·~ü|ùñE-~ùüL$ä‹´«u\èEÈåó×ËŸ“ú/Ëç_\ÿüóá¶µ%Ø@°… Y ¸şœ‚,‡øBPqÒçÏ·»­‚;K$çfËDl˜\ß±UåzÈÖ\n	;z’ÇOB_şğöhğrÍäVÜ­üìma$T»¦8á¯ğç÷çf5ø£¦BXp½˜£†±\1¤EüD†ıà¤’|ân<È å-‹½zƒè¿0îšs¶j´²°Ë×ôÅxH³Wü¢0!] 8”iÁÊ”hR)¤ÁgQîcÒ._p´ã–›8$x§÷A‰¤Œ\h'…™&„ÇÁ.š4ÖÀ …7ZiÁC‰æ8ĞÄÊ”Î'šqËk›ïÔÈF€øNY—i˜ùã—‹ñ¶|{Åo«”\Õ›‘b4“L‰4¯±sãİ*Œ@‹˜HÓ~ˆ:H³ÆZÓèm¼_!ÿ¹"BwÂ;"I2o|cq¤*i´ ¾	4ï“8Ñ‡HË^£r ¼^ÈıH3,dÚ@2ÊPÍk™¦Š’Í°}IƒŸ‰æfM¶[²PıBìˆßa^jğ@’,j]\¨Jª…80Ò|¾¡Ã…,_^/$8Êí$ˆÊ´$Üˆ $0³¤5|ƒ.$Æ‰Æ5ŠiHÎ$
š]ÉÔ:Îy˜œâ’¯Ùw$¹¿\ş…uÁ-ñ?,ùs¨$à#(%ß«Á÷jğ½üTƒ¿ß€½	QôHDµh
`8¸Š%ü#|²+`o˜ªè4Â*X{o=¢7½*p%20ÃÀ"@ê:Bæ™”ö–WÌ¬\âpÌ[:Â&FXou½ ^Òz^éŸ]+ Ã‚ Ìäo ùŞèa#(çZ‚cøÖ à.ë=Y0 È*Ô€v{,®lŞ—–ßVO©ìUf½qüZZíÁ{®®=tXÚ@PSuôÔqF_´H©„»#tT
VKà(±/U7vºš÷¢°ëã9lÛ®¥îLKçÜm© q½?-Ú]­İPZÅåM–Hû#dÖÏhî­%Š?¥^ ämı#â~Ì©Y£éT4a•³·CŠËcò+è)`uÅÌÆUfDó&pañ9`]Z<‘êSÑşàiXõ¦ê3ï…U7•Ÿ	-üÑÓõlÚ¤y3Ñ6SÅíHÀ¾WÔ]{9O'e?…céOy¼#Ö}'Üú©ÙĞÛJ ˆÖû¶:º) ¾±Má;l’~»¡»©ˆ]Í»SíÁ¡¼‘×²Ğã#”m²¿é×İFŞËåîˆ~7=W·‰¸q¦â=àØ](tÑŞC4ïòÈ‰UÌí;°«`?ŞæÓÃ›nvôı´³àÙ.!&¢Ù±Î1’MM€P“?¼3ƒ‹»¨êx8½»(·õzÆ=Ş‚£‹w@·4}‡æc5lÈ!Ç}û^(Y¨Xu<ŸúaÕÍ§Ã«‘w@Ğ®¥AH°ˆX*¼Ã$]„Ö3I?oºY {Ì{1İ•*=Ò~ áîqzÎîÓ<ÖH¯ÌH'Ø zÉßÛµén€v7«°!ÖU¯?U(¨™îaÕ¦JEN>}Ôpb.<jÙn‰Ü‡İ[02ó? ƒõ7Yï5Ø&ÇgLoÿqO?öÛåáf¿Ávy.õ}Pu´6~²îêğÏìç,ı¦ˆãÛî)Ñ×¼Ë£‹}ºà (X²İ÷[G)Ç¡Å<|Ö7bwÛkb0tÁááMÅãÌßíİrEó”É <á³á›íWíİ¿ŒÀ6Íl{:ëíŒ~¦v¼ÇV»ZçÄ²dUË
?°¹"æ“¥ÜÜ¶œ3ùáú–	tú-‰
¡ğ|(k¤+R|ºAcx€OLâK ¥9”ª×µ‰ßñ³"|Â5ã0l1Ñ/é:ÎËãõô4lü¼ãòÛ…;±
ÏYÀøpå+!íWiñF¦) á‰Ïù‚4è"ifHjå~€¤ğ8ôª/0X¯R	Ã*WˆH+îğü¦$ÒÂAKç0ÛHÁãB^­Ó0ÓğDˆ‡èâ¶Ş|òÂ4™hxÈ–ùFvÂeH|e*°ÈšQZ´@šhÅT¯-R3³T@s ’J£ÀİxRÅGí’Ü@å«0J,U»@sVı’M£fs"º)[µ®Ö¯\ªŸ¨<Õ¡Uòêøªá¨Á,P‚áÁo.)–ªğEi2ÓppÓ+sO`Y¿jÎ T'CDY»‚>.±µ'°1VÃeçš87‡7‚É¸ÌÁ½'ŒOÙ+Vé˜Šw« û³f>aÍ
yê[ÆÂbãå‚ŠåuÑT•D³Eå06ÑŠm^/u0¡ñp–)3Tk§…Š8@³p5EP¨€Ö]ˆ–¬Z yÄU}˜…ƒQ²D@b>2*[™L^ÜÑˆQG¦‘»8ã¯W­_VK]ĞÁ‡Ò¾¥mOñ«Ö¨Â©;•Ïß3‹v(ª¹Ø¦E7ãPØŸbñg/iÌ§x_¹fÛñÊDz(Ú.áµø‡q/i¬IãU,îaŞÌ‡ÈÍåæ=ºòBwnTY2FÆÏaÎtüŞ ŠkÛh""¾yAM(w†E“›ú”¨CUO&Ì=´ô;¢N1ãu«‹
ĞÒÊÏB÷Ï``K+X #7àŒ$wéÍe~|!şƒgqö–ÒŸÒR0™LYXÕLT=°J,«‰ïT‰Ç#«U§Ö^ï×‡+ìT&¼ÛÒ(TæVXPB†³Í÷7æÅV5«NÈG'¤õ$-KZåï¼F	"&•èl†%Ô5ÅÌÆ‹üÓNB€ßƒ±\ÇVoÄ#æ	–0$Bà=;ô´Ãƒ¾æ±qµ¼†dƒxå÷ûsĞ2éNÎAÂ¢”E*ùs[İçå#„÷æ¥¥e‡•Cæ»!,ŒÈ‘ßL?&Ú†ğ®vÃ9àâ(%á:$¥5Çî÷š4¸=£Ö˜øù<¡HÖ(*r`-R‰|NÍsFâ ¯P$\ËîeB½x`>ÇU«É3)ì/5VæhäìY‘±ÑH>‘–…ÅúãÌÖdùÛkMµrN-ä‰çòÊ‚Bv•Ò/¤™YÀ¥)Ş%ÚM«ß4³[Õ€ó!ªjæKª4|¬††j”şî#…‹QÈ¥g¤@r)›²?É†àIX\w”Ş`â¯ Î ¥ås?(1õw;$gîhT‚!hqì~[–	F¦•(nc". <¯"ı›İ-œÊ[5¾@+}nâÛĞ[â[hÆÕè+Â¥÷áïtm
uæºÍ~¿è^‡D–­è¦¼ßgÿââ,É±#KÏÌFr5KriÓï$ñ•^µu[ÃÛYâ–'JÙnŞ×²~ìÑfõ»A@,ãá€V¨ÉHÁ³Ó‘‚§+ém9›‡¸¯+j¢Ö4ˆ@H«ÒÁª½¿èÓje<E£?¶7€;Ø'wÿÊâüî¿Qçã ÙjÑ).ètCÖ×Kîi'”=;í*‹Ç¥QëŒ´kUºÌOA•q|À<I†
¾@74c…²1Maxc7èp†ÑÕå3$—;g,ÙékàÊâq)FÔ:#ÅZ•˜b•q€¼3IL1¢Q»Ít?`¯ÉH¤ŸV P_9}¬L XNK	êĞ‘t”âôİƒÊâ|ü°Qç^ü@§²¦ºŞ
˜RÜÌÙOK	‹‡oğíNÙàkUûæ|Tœ¡ rìô-,¢­:–¾sŸªeë»c,éÏyøªøé_+‹Çá¢Öx¥Uéx¥2ænÒ£>}e²ÁEAİ8¤æ	f%·ˆ§–k«R’.ÕŒ]5¯‚ŞB_)rÚqŸ<î•OÜ'gë)¸7ß‹;ëÔ{Q€ëé·õ6ÆŠ½]öşŞ^2ŞûX…!²ĞÓGä‡–í£ö|®;8zÊCj[~}0g·©gÛÔ¢C°úQyX8…®ù’ì7£†qÎó#†Êe?p¹„ŞØaÈn^ıïDn•%•zØ4¥˜¡°ôÌ«\wTÚÚ¾ˆáF­ùõÂgêÑRœz*‹¼™¦‚¯GNˆ"ÓpäSG‹³Nhl•eØ’™ÒÜ°K¥=¢ÑÌ!‰c(z5Py­œÎY8a±¼bUÖMOƒ›µ©JÓ†Ìh·gbóßÀùÖ¼¤kÄÊyÎ)„Ú©¨NC6p·–coL¼5/&Í›ÏØ'útZÓWÊ5Ëêik™0Q:Ã_^uÈ¯V÷ŞrWÜ¾÷6Èğ{U CDµ!Q–
ßô„g•ã!'<	»Ù'<7š<ê„çdè	ÏV£‡ğœ­‘s=m6NVDi}ËF¨ˆ
„•›èÍoEÃî¡-Ê;!TÒ© KüÉ ¶²8ÔENµ­ßf#‹JÚ
¦â5*Ó®ÚOØˆ¯,¦m›´Ú*pä\­bİ]µ	íÊ<ìø~Ó®Ìğ¦…ğfc¾¡xq½İŠsv'„k™¢13£ôÈ¤<Fyª•¤ü"7‡Xózß8œÕ[KÉ¨êì­tBwÍ©ML?â*ËäMWÍ_1VN×€òŠ‘*5d!Î®o•Åù7ê|“`ìÁbİ˜£Ü†Œ­nğ½a	Ë¯íÂ’.ÑVUíÑ:ì‰äz®Ï¬yß>/:9ÛŸ»—uÄ_¦ò_ôê$
endstream
endobj
67 0 obj
<</Filter /FlateDecode
/Length 5520>> stream
xœí=Ù¹‘ïıõl`Ò¼`±ÀHêöó®øÆÇb!°÷ÿ`òfVt’YÙ=ò¸5SReT’Œ›A2H.JÇôç&à¿ŸòŒ\¢Œ1Ü~ùşô'ü]™ nÚŠxûç_şô»ÛßnéàU¿ÖĞ?AAyÃÿşû·õË?ÿöôû?èÛßş/Õç£¾I©V÷×øêú^ıôõé÷/æo_ÿ
%åMûÅ©ìMéÛ×ïOÿ!„¶ÿyûú¿O~ÿúç TØÌàÀW€	ø:¤L ]v-+À¬•>½8ğmQ2x‚¹tÛFÔ¦‘ı[RöE¶ìz`Şà0WAŞp<#½+ıéõÒ åVZè-º[üÅëÈh¡(2~‹LÂÁÿx’Ò-ÿ˜›DÖ+*¬¤]ÔÑÔX/¨RØÄúû)ÀßnAÁ*´0Ñ‹U£—è¡*ú7”Û¡%‹lVşö=?¸vöZdH€Hİğ§–¦A|Wõ=¡ıí,¤—n­,G+|3F0¡2Nß”ËWJ˜RKøÑå²
|Ñk"Ê° ¦a´
1Ã\XXZÑúò¦Åf Œ†–P¾şòä¢¯OßğiÑZšö2Bœ:’*­s¾kÜÅ°(§áŠ&Â¬†?„„yç½ëèv1.à ¤!B˜*>"H‹èbÇq„í¬"²I°3:«V¤¼–*
ğí‰¼`ÃT›@ ‘‹VçªVLˆl¸zÈ‚œ	å	æ]á[æ@ãğŸ¡^ÊğÒb¥ºŠ&A67"ÀSéü„Wº>|{"ÊQ_'JT«%êF ŠY0mê›h!:N(nÆPYCl&sPQëÊ¬¶káb‡Y(áFìµÈ÷/Oÿƒ~!ÜÖÿÑ”ïÉ“€ŒÀ•|xƒoğáş=¼Á'¢„iäthî!hlç b·î!Á´qCQuî fãhãLéÎ; LCG½C‚m¼C‚í¼C‚n¼Ã
KŞ!ÍŞ!?uŞ!Ã¨
–*©²¶Æ©V4©ær¨T²©1ş“+\¤¶ÙøM­¸H†{‘`q(ãæPü½s ÈÖ9 hë¶s:ìœ‚l6ûJxÀïnã“=V†ƒ@ĞŞA të ¬:|ªb}èDy½Ó£°wN7ÃÖAz:M¯”S“È,ê,gådgb•ã1fÙtF¨@OE.áÃ%|¸„—p:lˆ«>ÂnG Ù*lë#lŠq·>ÂîF	´õÛú›¢ğŞGØı "Áö>Âî+lõ–*òSï#ìvPQ«¤újï**šÔ 
9ÔT*ÙÔ¦ìnLQ¹HM´ñ›s‘µyÛ)’Œ«Hâï|B6>"0|%$Øè6LSDLJ°Í "ÁvƒŠ(• Ÿ±bÊñÓ™‚*›d©‡XaÅC¤§â!òCç!êëD‹jµDßD3+ªM5DÉ	ÍÍ*sˆÑT&ó"Ü&†XåB¶ˆX÷LÈğá>ÜÁ‡;øÍ»ƒ?®†Üşşt,PTFâÏß	à'e­[ò® M‚€¼7F!Ã
2®Àã"üA ¢\T€”Ş*'X.!€yÈ€¦c5*$k1¹} &6€Š,>J_a(Î&*½£…ÈEai3 Äµ8c‡’Ò.;ô(AükK…Ğ˜X’Šg`bÜ· Ú¢¬—·Ö õ"c– @3È(ãJeFÀ $]z7“	@h´6‘™ù±mâpá[¡Ø
ƒIá&
ÒL[‡R1A¿)!t£G¨†¨^Jà"±K`@é; /µ\ñì0Ó;'“|´ÖÔtğ¬ĞBR/í—àÃÚ»A3A(XˆÀ9	–gUH¯»Bã‘ºiW®úåbÕ¯Eóà‚0]Ê›ÅOº¦”w‹Q«†¬”ÿf¥ê(P>"±¶£5}ãJ*‰wßZQ øÅ†´¼\ RŒ#IğG€yz­1#`½ƒ†[#€fÑ©ÎÂ
B¨«‚e  T™Ü
YĞ6ªØz|ªˆ)îTe*•½õšXÊ]ÀrãÜ©ñğ·‰)RÚÂÚø)­FK¨ÏtëÑ¸Úâ=8•¼¾íp[„0Ïğ¯‚_àó¹=§ß¿Àsh¿YÑ~3Ğ«CŞƒï¦¼¿YIêqäİ›Ûºó>¾k}k¯”KÏ_ò÷‚Oyê/­-„•6°^ós_ÏZ¾[ÁßóÌB/o‚Ñ¡g>(–XŞ+¿¿#Õe”2«;òğ7ú=´rë?gReşëú”Ù3;4!?³(‰E†hĞf£.E5*k‰¨Œ»ƒg\iH8<çw2/lÁ1ÿÊ…\wXùRE´‰*®“+Ö¿0î@{è!%)gO—kuF`ÌMÉ©-	1El	U“Ù’Q-¬AÒø¯~®¨t0ÉdSQ÷Ì£-¡SB§|"‚òLıœ­÷9³Ô^À&hkq"&Í'Í½PV$Ea(Ü=J³RYbßò*ŠpÎêm(ÒàâïS¤?g=Yõ?es¿‚"íå›Q!#£·Ğ6ğ°KØéö„Œ÷<BBlö®/¤“¹‚+ïiƒG}ŒŞ 	L <Ó7ôİ`<Vœ¶°W‘4XüøCÈÕ|Sm¢vS$rX»¥‹H’*ô4%wq=Ò˜$
‡ ÒW…FPéh_5ÔAÀG~9P‹Ô_í8;Ô[EIOÁ‚îc"D‘¥ñRB>#—Ê=_`…ëhn¥¢aes—xw©!íÚ­÷„?“H¨¨àQà§¼¸ƒğÛ£wlw,‚µ^i,V>ºë’ˆU·JÜEb®¤‹/¹[=ˆÏJ\*E‹ıRyöËkbhÍ&¼3¼(R‰mGè°~ˆÿ0Ôm|âT^"‚_ÖtÅ–è7²Ö,Æ´ÆÊoáñc(£–:ˆ{üÖA]!nÙ;¸ Lª}äğ0|iLNI8TøŠfW¡'¥KŠ\ñŠN 
'naĞ-İº¹ÅÅ„ğOk£Ió‹å¼ŒjõU#ƒ'2ô¨w0¶)íI¾¢\HÀ¶‡ÉC7û…W¾umLt™DèÈˆ`$ÍídQÃØ!æ(Ó1ç"«v¢†&¤‰KÃ9œÕÛ ¿ºë«â6)‰Ä—…oi5ª' Æhe*¨ÄiCÖ9`F8Á™wÍtM©ŠÑ;š·§±wE™=ëœÕiÑ-U\f?2y•4§ŞÜ
j•¾M$]£QÆv$½Îõµ¸¸«uˆ±a*, Ë…KLHt¾wÅò×õ°*,ğÕÒò’A‚öÕF[Õâå:ÜMm ¸»+p·½Óøld“çhÑª0o³õŒ®CÀknÁÕgLì)ÄÉÕ½‘+Nq‰DJİêîÅ¼‹oÑÒ¸èÛö»<yo©aˆÖ6ÖåíÒ,"XB«Ê|¹_"Ï…Çâw $·]6.ŞCÇÛvgfWŠ©˜Ğà/¹eã®ºUøÏ¹eƒA\ ¬-«üƒC+òvä‡‹õÎgGøÄPÁQmWıÛŠNaZày*XlYòX~0Däş .:Š49­,;®S@ó© k¤ô’ğ)0Ttü M3ü3EvNxÜqAµ	ò®µ„ˆK³õ‡•<»`D"‰°mÑmî˜l¶ÿg’CâVÔCıšêÏj3çY6}Æ.øe%dï—A¨Ry;ßh#tl·¨¦÷ÕNûïü2ƒ²À»g¹Ò:FòC&SËlt;áíkÊì€È0~+#ÌCˆ‘P1ß´ÉMk=.vá Â„¢ı,£²BaÖ°V…còŠQªE ñYy>óœ®kÊ§	ìéãYÈq„k"›$>zk”UËµÍÈu×©y–Åbé¦Zh©¹RF²Py{Ï	fwĞ…ÈŸö=\	–é<¯(¸L×6¬gìÒÄ‘6¨<¥ãºªX^±æ~ICUĞFyçÁLS§$qÈñpJÂû–r	N÷FÔ'~Dœş¡YÂk(Ë+ŞpX¥&„Ç—¥å	Ká;ØÇ+7İH¢1CuÃŞÀ2¯'¦ˆĞŠïcù>oS¢Â°M]Ú:+«/…vào4»ªbÍzÊPÇCwc‘;\ç<§#|WËE1l\w]„x"‚¢ÇŒİómğq+tĞ©y^±mÊµ0Lğá&İñ£!>°wæÎÜËër0Ô8¦YØ¹CŠm>áÊb.tôtÎ„0öÇÑÍ[8q–ÌwBCtÓn€÷ì`í~Ùx>
ùög÷^uÂA[ÓÖs³ó”s1ÛøG84±z5ĞwlªbÑ·Áù âBfuáÿÈë™£o>â¹‡1+{Ğ0ş#tW'Š‰Y‘™
CÁôü(M¯š(Åp*Í?â°X‰ğUÍ^šºób>†9œ›NƒÈİ}\]˜ıAÃ:¶nêDhÌrw~"£œÆ)“8É¨a'ÚÙqÏ\Ö/0!Ï[. fùq4ã9¬éÓÓñ×Í>ó˜5)R6èå,Š/(§¼_ÕX?>]Õ…sYÓ—o:Õ2E­Úà&îïô=˜b¼äXÏ??½áÀêDü4=¿vaã†”'VUf×î4>Üçî6¤¼œ»¡[Mƒç­œë¶¨kÅ”­Ã^¨z‡ı>g²ışloıèüëXT5*Ğ1‡è¯Y¯Îº6f¼nòPş¼Ö…G¸@°Ì^°Ûhò×/ÔôÂ7[€›Xäb\'UEpÅ8£Ä¥p<«;\&W›E zhâkº³f×ÏLiMIw¡ç#ß…ôjübÀùPšŸ8eYÂNpÕ}#ƒğ
÷¬¹·à•®Ú c_äÄ<=uJNªLÏƒæ½]¯Ìƒâ™%t–é„ÆqÌbç’~x=$ĞBŸÏE›Ÿ=˜vÑï1İ0ßiÎ§-]· zeĞs!…ç×·Óq<åCF~¤;Î"ãµ‡ãmÛÓtæĞ5%ÒqfôØ5¼L› è±k ‹4‘º;,n=ˆ­ŞœÇdUÓ¹P°,m%9q¾­(‘sÃ
ˆ¸VôÄµ
$G–Õ6ÈéfrZÅ›œ˜VÈë@+èQk™]ßzY€Ëœµ0àyn€áTëÑom€†#rĞZ‚ùõxÀÂ†ÖŸ³V`ôœµV¶±¿µÑE±i"mx7É7úvZ³?dM	í—ş˜5¢ËêÔ¡Ò«Gp…şÁ¯M–ÓºBh†±‹‘V“#Ö †“3ÂV =[-ƒèÁj¥X;—¬Õİ0£H´ÓÎºíX´FV;;­ĞOTË|¢Gªsp"éLi`Èò@±
±ğ–ñ¨V$=*Ä[F­®<È°ş<µ
¤ç©‘Ò…ñ¤‘*¡*K‚8ÑJàV_Î§6°	ëø(µ (qÉ3^çµîøNç
à¿y¸ÌÇ’á‡GÀHíÊÉ1¤úwŞ®u'í¹~;À£~~ k¿0)ˆ_Á™ñÙrp‚…l^ü•“l€;KÇ‰ÕØ¡<÷.^ä‚¼é•9!*.›‹ÅNğÌo»ÈªTBø‡æ@æ‡ÖüàölÁÄ†39ÚÜœM·\ÚMÿp™W¢uìÆW§3ŸN$ì²è”'İ´	Ï“@çîü0½bÂ'úÌÎœ¾b¸Ó{]ØÅÔ+?Óé‡'Vâ¦“¢æµdsf*+™zçÂ§§˜®›Şâ{(VFÓÓ
óİü|ì1dcaKL;·AWE7ã^·¤÷¾)Úo“Âtåä…›“ÖÆ×©êø{›Ë³Ãi®£ö×IĞ&yìÁìi¶s˜•Ç˜GãÛ“"=9M÷Ô'¶¸œØÒ1Ÿ4>ÍÃ3[¯Ã—Y§7¦:·?òD„ÍnµJ	ÚcÃçÿİ® ušÀJr7®›7µ3ŒÄüÌÛt"Ê,°G*@ráü“¥uåNÇ+ç`§åÄÅ‡]¾ÀH´ÜïI±ê‘EÑù­Ãó›øxd>is¸§‡·3#åéLÚº³W³%:÷ùĞæzhÊé‰¤‰0—üÙ•ƒT©™ôua~ní·>Sv‚Àù™ìë2éç£¤áB½ú!7M†ŒÅÒ£Öƒø°å=Åƒû}[›>Âmşø¬÷8Óch¿ïPîıPL0ÆOGVjUµ¸øğŠ{Û-:;™Ÿ4},s#[ó	¥Ó¹Êù/í"ßåxµ§y.Œ‘æÈ›~çO2»î€_uôÁEİ„1«Ô,ZÓÑú;0ñÄôÖc9ÁFç´2š¬À—dÓšj´­4Í
˜X¬4+y³h®\%i©x_œ”‚fóI«Ñ~ssÑ|à"iµµn’€K° ©º_’Ò[éê`zÙdWF}ëaqB8’l´‹ğšæLuó2@ĞdÉ&ÿKò3¬O®@šÜJ7Ö·Vš(>Mœó&öFáÙçĞ´¬N$ñÓ”ÜåæàkÊq­‰¤Æé%®¹°5åÔ8HCû$)€bI×ú’V°¤õJà–êZ@41¸ijp+Ü’l[-—"ÓwÚ-Á·‘×ò€MIën°Ê/š@<äZ’00k¯):xqü’î©§ÙÁÔT?iP¡`oä¦·-¯°>9¸Àhn0)[øOš¨‚ê©"%hS)äíõæ×Ë¶õ”tm^·áw^»öŠÔ0vÁ‡­ˆ¤|äœ‡œîoóä;¹™ªä&§ïCùÉ^”KöHsƒèÕûJvèÕ‡Ğ›¼ÅÕÛ1†Ñs=ªSè¹;—q¼ŠŒ=Š'è‡Ğ«Í¢§Ãzôzzêr½à¬Wôìş.¿WÑós×®¹hk:¾X¯á)7oß¹t½^FTn
Ï·-}ìKÿ<¾Ëá |…P¹:Èº†[Ãñ€zŠ¼Q¢qcŒ{^Ö…Sõv¤úGªç±Ï_µ¾„¯‡†Ê-‡¤ÉAÑÛÚEækJëuöù:Ôr7Ä>íZÒÏ¢¿º×ˆşšÔpl8õÊÑ—lDŸÈR_TïàËõàï¢Ç¡ÉÆÈ{åâèõ«ÖöÏk»<u¸åo½M«qvP¾tÏ…ÓÅ…‰âÒ|¡öH!dLwn­xø¹nßÇÖ¿İç®+-=Ï'¢T3f4¢\Æû#iDÜG88¥ğÿ©…ù$
endstream
endobj
69 0 obj
<</Filter /FlateDecode
/Length 4230>> stream
xœí]Û·}Ÿ¯èç jó~‚ Ò®ÖÏ‰ä”ØA°6`çÿœâµÈ™Şé±z¤M¼+¯4}¦I«N‹ÕœñªtL?‹ÀŸw+»F®QÆ–Ï?Ÿ~=ÑûÊ±h+âòÛ?OÿÓòp³J‡[}îa¼BC¹ĞŸ¿}¿ä¿ıtúî{½üôŸÔŸz‘R)êîÇ„º5¿À­>¾{2K\>ıˆ’„rÑ~õA*»(½|úùôg!´ıËòéß'‡÷?ıc Â˜ğ	ğĞ"a») `s“Ø “;ıøé²àĞÛªdğLréæAÔ4ÈùóTÎ›Ìêz6îØ’\¹h¼}ÖúáåÖ°ro-ô,î,¿xY-ÆÏÂ4#ü~=IéVG?f‘¤zeAa%íêĞG§±^‰R4D~Åš½18µÚëtVp ½È|^£GGüo´;Ñ‡è]E)Ãòs¹äeÏtaÈCB‰´ĞN-¦MÂ\ªİ't\>Së ½t¹?øVtgŒp §%á÷JéŠh+ñ+MÚ8ºÏkû,H}®ÂhbÁ\ÔXAªh}½ÓÒ(
ÒãCÅÈêËÏ'}»z¦«UkiúÍ„8Kóê]­s~ÜÅ°*§¢abf5~ØtóÎ{Ç§íb\áüÒ0ı&ƒ
L‹i]ôM¨ÑÎ*f™„Á‚†Y°jãÜªšÿùÄî'ZXX·	rP aÑÚÒU–`$-,lB	³03›yÂ¼«z+:ŠTfz¤kê˜k<aºÌ Ù&¡vaÌX$¡k;Vévñ|bìh·3µnß˜ Œ™MÔNà4Fr6çîM9Ìiš™{1m3Glva[ÍÇ¼ûóé_Â’ÿ£xP_§P+!–¼…ƒ·pğş áà‡ò„’k”œÕ->DéÍ€è9>$Lg±ú€	#Çø TA‡fádèM®:`¸@ì¨on`ANæBDB§ ‘±Eµ·k€(WC€(Ø@ÂÒå@×6ø@ì"æ@ş2ÁMÚ¼‡*â~Wô88hÓøàÊÅ6ƒÇ¶˜ +÷A#9B4GÂÎ"„³æ,B6GÂ<d#¡UIU™ÎZt>h -ü$5IIİŠ	kA‚®ZÈc¨·s&Õn9çº œERÆá:Nö>sæUEÜyª*¹›us‡¬Öá[ŒÈ¼ü¦´á-,¼……·°ğG	¿7}ĞÂ9Ñã$œâ„§É'›ãaçqÂK3Ç	‚¦íEÂ¦í0h„ˆÂAØ´½HØy˜ t	Ëa"¿¬a"_a"cœ†µKNØ>8gv“{@÷•6mîTU?Ì÷ª¹“v}sw®–á^_-XãÙ¸F‰l~%2F‰¹²kÉd,ZÍ£°ªcA"CcÈØ¼» T± ‘®Ç ‘¡9@dt+"_• Q/x€è·wõn;Û¸ —MÒÆŞ<—Îp>ãæ
]5İcªyp¨ªƒC5
ÍvÌµoÈŞbÁ[,x‹ÿç±à‡½ÏC–_N0äŠ¬|‘RC‹àĞ±w²aOÚ« !^ D`2$õF`¬`V©ğC C#cˆ62W•“ûÕÂn÷R•Îb€!?	 ˆ)£gˆ|=Â'ıvúñìN@`O–Ç‰8
¤´ Ê’„(ÉÑ<Ÿæ f…¤æ¬š{1¨Æ[¾ÎnE¡&@rØ¨eg‘0Tƒ[Ó½e ıšfY´Q ÒnÕZÈbU·ê`wk‚tË2¡;ØôÎD$n)AÏˆ]zG¸Ì­½óÆn`¤pHK‡€M‚Œd‹š×ò¨‚C·$[arP Ø› Åµ¡L’©nÅè&¯.º‘ËºµpËÅÊ­Œµ°kÓA˜¡±òÈô¡•aJ•ÈÅ%R`¤²RÒ+i¢v˜g}×Hj^ÀªºçSo,¬A§çËm‰p/.0….£Ğ¹Ó"?`HD—>S€L °XURÀ$SÓ]!TÓ2o^ÍÁÇi–ejVæòsâ´™±©òl÷#İ•(ç¿(ÒR¢4"}ç”GKôd†'Ò†Šùı‘4”	‰ñëò¿®nÈ¯Ëüú|û¼?*3;5Í/œ=9ßn—åÀßõşûıÚ§ñZ¤sxıDóËÿŠô4¾`¤‡‡òšô"Æ~dÑy(×Lo÷[¼oĞÈ<âu}Of,½vYïéşÚ·È÷“jµmÃíÂ³ÜeK0Íî²„«Ç<êh|¦I:Sfñ¸Á”p)^¬Ğ;å¸l¸âÁ=_Q*IaÜH˜3¢TV¢8¦ÎfØªÖ™4HQIÔI1^ï2'
ÓìKPğİ:Ü-¡£÷»S%*aÕı~É’¯©Ÿ/ûİ¥WlPÑë±ŞyEvd2ÈP3“Úv2É†z6¯ió±gY|Ëg?#¿4ï;ÛÉ‡“O?LmİèÛ/Å–Cj\±lÑ©‹/g±ÅvòBı•bË‹P×ìNK ›¿GZÒûİ)GtßjµáéH]y¼Ò‘İŒ¨‹÷+JK¸fwX‹‚½”–X&İµ´ÄïOKØp;ÅÓß,åacNG8a.eÎ_¿VZrÍ(ƒfwYÂê{¤%¬ßrøo–¨NŒ¨l¸´³ùÜÑšİe‰(¿â†×Å»Ç¡îÕSÆ¥(³¬Æ†\8ç:€›e§ceQÚ*´¢Tæ‘YÑİFÔ”ˆt#/`"3ØGL4•9µ/_Ò%{®wjËÙb>d¦¤{zJUm&ÑÀ’­nTôP-VAdEór±ÔµVÅ*…Z˜Õ*C%Í^SÔh‰|àõG*Ün†j1`±:	¹Yµ˜@V)N—¼Jœ ^!N «®öNY%–Àª¶]XVßíÓÀZSlXSÔóš•…²â00·je˜@€<f˜åi²¥G+&²Â0°¸¦˜ÛTĞ ^n /7°+½ÑíÃ¥é¦lbw“÷Ù]àËyqXÕâ=¯KİjêStŠVJÍŠÃ ±w±Òğâ0@ŞŠ`yq¨‚n=dëeKp<]Yy³B¼6Ü@^î{i•ÒË°ƒ<½dËdïÅ]6Ë^Öµ´Ş1ÅŸ„ÔÖè[¬^¦ó²u¼€µ”ÖL"`à‰Õq¨¡‚±¬,ÌÓ'^NØX.¯³–Õl€f¬A”fW&4cJ›Ü9{¾Q58bn7­¬ĞlÍµÊ
A+GÚöÛí[ãcÏ”¨ùJg£#Aa˜*Ö©t hëçë^^ƒ»`=ÕÜ££Í®Ãj-¼kñtœì ’tòİ!{¤Ó`şn¢+CëƒœÔn]I	Iî);½·QOjGÈÈwGÁµ_‘\Í\wGn,=ÙŸ¸÷	Wb‚¢j¦ÂÎPbÎë«µ.B#Îxüœæ1cÛ3Éıº¶‘w}kSÃÕP££dõ)¿gÛÎøB	g-9­}ØÜOºïiJÙV©l›ê6‰ê‰)If‰wKºùÆú‰áLSåxªòïÒ{0“~ìc—k( °q^
í)!g²¤kU0ì¨—¦ve,ûÈô––šØnÒ	™xÃm•äÒuõÛRYÙÿ¾§²™Vü¾"–ó‚ÕÅÔ¼z}HC*ŸgÃ\1TW	·5ËJW·mşµ‘“‘R¿úòC1Pè>›ŒXŒ“8ª¦ôfJa¨¬ÒÚÊ|}S:TK-Ç@c?òƒ¦„CÖeìW¥M¶_ëZ<\³‡l”47=â‹Ú‰‹ƒöz¡#oËêjõcÆ®,Ú×Dö}®6´ u„{7Œñbpİ)äã5ßâ.éozşuLÔÃÖa'Rn›EêC¸i¹Å5/T“«”ºO]šÍ…Zó¸<°%|³öt€•ûÇA{Nõ“±FüW:¥	J…A`YÆäZOèØêÙP;u©o{ d¬½7ÙÙ<÷œòœ”÷˜‘ÜÜ	êÚ2¯[©¿Ö­ÙL}¢xááŒ­ís:Ûe1šœM³ü,ı6Çms»Vâ—XVòwäÖÙeM_s·–VÛImâÍGOê¶À³÷ŠÙÄÇ²D²«5¶,ƒ]è“Œzƒ²_´”mC˜¶9j%ÅßÔ÷ÓyºtØT©‚Ì8íPÙTZ
U(çyr×“{”¹ßš2X5K¹œœß¿YéKÒDÊ÷JšÏº~<6O•‰‡™‘£oÑ(Õ	n¢=G¥çKs¢%ï/™ûHI!ñ ;D³êXª—ãDnãÜ¶ÏÖ§ÈJÛ¯8çÆ·=KWÂ1Û![:3ØÁHã{ºÃ³‹‘Z^däÁé¸SßlÄÇD†l†'³ó1‘woáÑ\ ÔVÓô‘ùRBåÊÜ¥|+v)ÿÅ>\äËQ^øô*½oPv›ø!Ş§ƒXE©W÷®IÄ¾W¨8ßjlÎAÖ<ºÕ|F]ÜÆ‹]üí°ì‹œ¼zÆJ¦Œ,Û/Ü¶vbŞ?Ÿz…ûikaû6j³¹œªãkÛ¯³¼¥ruÙv•¥½Ù}Kñ‡ßt>âü”‹míÎŒ¥ZµÑ(öİ©9“bUÆc`ï¨Ö&D¬'ı›=·{3¹`jW!ú³oh•aAĞ…Ö ÛLÒÇwC´ªRv/û[&û;ÙqQ$º]}s&Ûƒ”ˆA§%¶X±­y*£xMßV{:Ûœe¡H:ƒò×GÙœ¤+ZÑÎFçº¼6[+ W”Ñ™/“jcğÍ6lêä}}GjñŞ=òáC`¼{Üzc›_•EˆïÑ°¹Œì¦X_BÖß¡d«¹ j—³T²Z·ƒF·klS`ñ!½½¨Ğ1Ø/SË‘<MÉ%ş¢Ó•6Z1œ¬¤•y8V©"}s‚×ü3øÀHC‚ªfW¬ã'ğbë?R	L¯ş¾"ü`eÅøÙÊŠ±#Š­v˜‘IÂN=6™ÙéÈ6·%ğs•IEÏ# û¤ÙµŞa…‹Q19€aFGÌø¡J °…¦ï:mó–söÙW„©¬?QY±®ñŞ·—¤[±ËÜ­İç6qäü4¥ÓIJ¤$ã1J ØBKÉ?bë³ ƒ´syĞlX‘b~† ´cèëYÚ9?`e3ßN6ˆ¡l ?BÙ·SˆlŒv^q¦ldb·lzí¨dÒ?;™´ÄÏM@^‚aç&‘ä>29ºaWF§ø¹I ûşiz@pŸRVl<8Ù@~t’µ®šïc4Â4[2±9+êôF¦|«S“¾Uês…¶‹ğy'´}êqkW¤]«»xVlØ³)ò.nlŠ,§‚¾?v÷Êë”lO‡î¾h¿YÊİLüCZÒWï–ÿÇÃå3ô,şçş¤¡ï´³úsñà]éÛ€Î·­!|-¶¶‘9<°µOâ~líâ±uÙz7ù;[»øG<ÓÙÚú¾™­7œÂfÁéh¶ö‘äûƒÙ:MâÀSì­LüG³õ~ò7¶2ñfkïûV¶ò‰ïb«ÚúôúálíÕ¿#líåË«µd¡ÖF’ÂâÀ4
endstream
endobj
71 0 obj
<</Filter /FlateDecode
/Length 4262>> stream
xœí\Û·}ß¯èç ¢y+’´«•ŸÈ(±ƒ`eÀÎÿ©âµØ=­é‘z¼’V;}¦ÉºW‘ì&•u˜ÿ,šş¾Sâ2y£Ğ ¦åó—‡ßø{ë“^h\~ÿ÷Ã?ÿ²üJ¸W&Ğ­±ô0_QC³ğßü¸”¿ÿòğÃnùå¹¿ˆn1ÆZîîçŒh¾µ| [?=üğÑ/¸|ú™:ÊšÅE“±°X·|úòğW­ümùôß‡@ßú×B€MkÀ¯˜Ø§3öû0&®Pš`|éôùÓeÆIoÊšç&¬‰Ø‘íkQ¶MÖê0nìÜ±Ç¹MfI¤ñ=¦¯´&+ÖÚ­Ù]ó¯¿ŞÓV2×Ìt#üşşö`LPÿøÅ°ê-[*PÃb—bå“hö)£WÚRxŒºx´ÂHäÿÔnRV+ ÉBĞË—ra1š°¼ğ…çˆLfjá‚óÎTÌùÄX@mû}Ú›å3·N†:*ıyç;)„*äƒ[¬¡È·Ö5Œ”Úú.Ô¦Úx¾/ºHªX2„Y¢ålÂŠúD-q…ÛÀT,qŸ|Lã@h??Œıê…¯”sÆ›	 Š.C!NÄ&eƒe†;›Œ£?BÆbˆ1H±¢¢ğ7^è‡1“lZdÈi8é›QïXa™Œ!VnŠk6.­šù_Æı!-,£ÛChÜgN$«–ûŠ<²ò¼`1¤ª¶¢"Fí2Ô˜¯©_¡ïQdËUËÔgı4ûUsëzÅö¶®_¼<ß·İo“¿ìœvï-²—÷PªÓ4hEl5UCi\£°%GaÖn;ÚŸşÃY!-å'ƒö9ç²%’·\ğ–ŞrÁŸ!ütÃ¡2JÆ%hÉ'fJŒèUr(˜óa€16•L„F$ÚEh„¡99lNŒ%jiÆæäP°Ò”
:'‡Š-¶]“C»’É¡aÒ[—ÒYqéÕMéùM#]lLM?"äšel}Ë(n–‘ÁŞ,ØÒ›¡'‡lş)90²JZ%‡Œ­“a•2¥à‹!ÌÉ!£˜ã¹«’°¨Lœ2DÆœ†9CdÔg%u#¬eˆ|Õ2D½˜2D¿]8RïV¸œ`@8gguøp—Høº}EW’ˆ¦KdBç"»uDØ6#Š¿eÄğ–Ş’Â[Rø“$…Ÿ.o,¿>E•EÃ¡O£Uå"§‰¾k·¿tĞ3HšMÁ j“2Há`½¶ze,ı!XÓŞ{âË0¯ŞÃ(—|Dº5*€¨f0E6ŒIä-¾Ï`¶yŠŠhâ Ù¬H51Èæ’¡Iˆ@^aÓ8ñd&m’Iö	4<LRĞ	,*ÉÍ+Ø•÷2ƒA­sëJ‡0òHúOpDz[Ä¬ÌÛè‰OÃïRf,XŸ…¬ê¨d7ÅuíÖT<Z[*Ãj’ŸaàÁùğ„!á?bWd³šW~su‰«‹ğÁÆê:RK\ThÒ”å	Ayë€ç¦rÆRÚ"0*KRgíibœÃ…PÊMğ”<·É¬N‘yZX=Lë¬ö€Í»´Î)=$í§f¤-¤Ù¿˜bÇš8±T	,;qm)ÅNR¾
Æ¡‰Ü¼‚]g/£¹Æ(}£Ñ±<ã4‘§&%Â¥èR°;ó„F•œç”Ğ¤$ŒU—…lª(XI€®;VÁˆ›®XÑ¶é_è–š˜éFl?éâm}§¹Õë²Š×…Ëœay¤4#c•—•õå§…eÏ“òD&,+Ë^OËĞÛûÔŠšm)›­V¯÷ÈDwÛıhëı@i€Ø{¢ß–@5K?V,ÑïPîŸéÇ‰çFƒ4NÌÊ/¤9Ê|s¶g/[nMƒƒF6’äj<8b‡½¾£:õú\Ö¹\#ñ&ÎáÎ)üË“ûúéŠu-GAònfê˜S 1@§\£Úì£Ó;:…àÜŸë3û79ÅhzĞ)œş#:Eçª>=<Å)z§÷tŠÁù)9N8ÅÄşmNÑ›t
›û ÍşhîA*ü˜ÅXcû‚”~Cjıî»8Zs®ìX‰Ÿ‹—ï<f‹æëõšNQnç‚,8;¦¡ï !ÇŠYkè+áÇß[]~şjÿãÁzíıã9ŸÑçåÚ€øªó}<DËû#´¢è?‰Ïx­àĞz_¯‰†yŸŸn¢•ìZîÀ˜0÷g´Yõ7Ú}‡wÓİjÇî=‘8àŞt¿İ&F¡¼>²¨ ©0³Æ®¸·q-±Œà>[T7rW‰Læı‰¢J­è•ÂyF^Êk[AöÒ€ùp­h—këºÛC® I°qšƒÎ%3ÂDâT¯HaÃ¾¥ÿñLw(æBœæŞ_RÒÚ¯¯šŒOæn™?ÆÉüãgo¼8éøÚ(EŒúfZ‡xÃp—,eÜ;K÷sK™¥„Hçf©YÓ²”ìöˆ+Xç/ºéIºŒQAuÒAéTç0ÚXŸ¥¹O“¹EÈtšwğ;•­ıO\êæO€ÛI]GSÙ¤ù«©Œ¦jå}İ™ô!V£ıªûpË¸]:cBbq38m±ı¡ÄuWIIÿ§" ğ$şTóÃcmoÎÌáÎôÙr›VâÉ9|*·Ì›ò¼à­B²>÷¾e!Bª3ågá§Í¬ælŠS—b¶Lä€hº|Sö6aË6e;êbo¾gÍwèœq°ÒİÄÎõÔ‘.©òX<:‹«xì•íCñâ¼kD9ï{sŒåm
ÓõW”N¸ØàƒÕzÖé,à!…øÛ†.ÌÃÆ;Ì‰óg3ûF–ãP;¯» |~$4‰sZ\i©%åœUŞ×Îƒ÷#ÛìüSù¹DY%›Jà†ÛÆö.…âkK[
¬–—a—Xæ™µ¯.ÎX{A—ìaßkøÎ‚.{8DÑú{GÜ Qjû	.*<^¶²158BÉÁP«NvX(í;§µ©,şÎª;¤j¿7°<R%ôóğÕ\À÷m,u|GYÊÚ×níåEÔ¹"}ïÀÀaPÉWsu%ğJ­I'8ƒç·ğ=/åN:n²¦Señ¢Ûù<Û² Ës†,Á«–zWşò|®	/Éq–M@‡Kr\›ï~ ä™Vâ
¯`ïÉ:	ß¢4ÏjNPúöš‡$c>WlÌšÁƒ:Kæ-%%ğóşì”4tü
)iÈr—”4ûËSÒã.)IØä–””n{F&¸wJ$zÄÆ:Ì³ærExéëYâÀó…´íõbÍmóPpmzqf"¦}-¯.;•5½ïœËÇƒÛµ5š¶üı4xÜ›–”ªpÒÄ¼ºû·`íZXäIZ5»m’Ğæt{ÉŞ›ìgîÔÏyqÌ`ŸŠŒ®*"Ş6;©¸ÍÊówz)AÚªÂ 4ùh[3¬‘îŸÆÔºùé©¾Éï×wßDØ”½…†ks8•@v{ÄÁøW²Á ”mp!TNÕµ‰üö>ä!‹ -u]õÛ†x—Wnè?Eµ‘ñ˜ö{-íwJYû«òÁE^ózLm=¨sÂ>Ç–ûõ7®È°+u¨”'±’ÅÖì>G¥È×í©;³zÈ¼ öêŸyIä£çğÔ5`Şô7	ô/ŠĞ†7İ=Îò©ryYc²ã‹zÔLR¤ä-ÚW[Ô¤áÍa	Á
ò¼Mˆ>ÂhSŞpEƒGpáHg…>Unz+ÚÓË.Ë5Öh§µpøòMÓ–º!¶‚úzl2úw«u¾vøÚ7—®-lLH„˜«SĞ£’`“H‘ÁÄ[¤_ëş+ML3$Ù¾¬_‚¢ò†)¹^±/æûFÅ¸ˆq+†«ç!/nvt(º„ˆÏRÄ(éÉÆçİ«Î._|ÊÛ§0„7ä-Œy´í.&1–|Œ ‹7RyŞQøtFâ—f	Ú\1KAA˜74ì0+Û°µ6„²YØñë™¹K±bÑÛ…&ã1€ƒT±”·J)•Ÿ”B™ï´xsUÅ¸ÇÒUnøÔ˜œü:(OS¿ {	<iÎtz¼U”Jr,É¨HŸJ	@A‚˜`–•ü‡\ŒÔ
(ËSTÚeÀZof=¹¥U”j&«ùŞüÑäíÊsCŠmJw3	S¶?Ï¼ó¤Ì‹à™fÈq%Ådò¥±Pƒ¦V™ŠP%[XéU+Ş œ2À›?q™í¤›	u±º°0%½€š·³¿(Î&«ğ3ù_e{òÔ.àäÓE“ëW…MAÒ4;ES5ÁuÕTØMÈGÔâ»Y§È7µINvŞ
ÍËfè.|ÑR#}0n³é¶E;÷¤qˆÖ)“ôê(Á:iEE®ƒQ4ØïéC­ÎRV´şzWşcí*Yƒ¸ÉqyC$¢µƒ„ŞËïĞÆD·µjËík¨p¯§šö)<Õb»U\ áv¸­5h|î¦"½§Z¼ˆY¤Bìô´/Æ®5¾A´£Ã¦*ªÁÑ®¹êuüº‚ßÖAÂ6u°u`[	³ÖÌÙ…°|ÜÔ”†$)æ2HXôsV#(å-àSş#)ıO9’±^!¬«`ûZ$áÖ‹ÌÖƒLë•1™ıÿ²NtAe=i‘u§iN¨¡cYÊš5@š«^ôn[	ÛÔ@~9cSÁò¦­¹‚ÍGNÍÂQ5Nv]óãU$l]	*ÅIªß–"6YÉ6ÚuÌ_I°ÛØÉL^e75°q=yi—oòçª‰Éï«Æ¦qŠ`³ÁrNÁlÃkEP¼å¿—ó÷RÆ~uÜ«§o¥ë~¥«ÎÖxµ‚TºÒ”¿y]k5'¤/¨E@ÿº:Ü£ñZ¿½«×|×ğÆ!Æ4’@Yäw¥˜ONøÂnıß£Îô/È'‡I_4¹×|Í*‘>£Xcš$÷ig%Eß×º(ˆ;¡éñ@WSŞ“J„ş˜ø[N-âåÎéÄ"gL9)rœRCÏ§ŠãŠœáãDÊÉ5íÜÂH ¤İtZ¡A%.°ã$Œñòf?p§!ò ¢†ÉsŠ6Îùı$'ãì Áó8chÈ6aíäÌe5½Ì Í	-ÖFÿ¼d®ïvœğŠ4•êzVkã™ÓUphÅÙD„±Ÿ ˆ³‰
6MÔ0y2Ñh;ô>hIn†-ßÃæC¾•¯lO%"÷O$rÆÕSÃ$äcÄqD„ÑEyaZ¥¨ƒ<ŒˆWõHë|n?3‡°²>Öé<¨ƒòH¢Ñ¸Ÿé#hôÓ&fú9A‚í~¯<Tµ Ï"Êš’ç@÷¤äÅ9D„1ïIrâ1Šß4ŸCD(Ó å9D„ñéQùl¢¦ƒŠÍuPD$Z7å"İJ;İ‚qéMÀÙ_¾å¢ƒï\=‰È¿ ŞŒÈÏ¶ÎØ|!7¼Wß®ïõVÇ¦ÍV¾íû÷^óh»OïñÚGŞ™XTàüï|¬?÷}GõÀ—]½‚­#Ï÷Í]ÛKséÆ]ui³«nw#ğÚlWwĞÉı
éÂ:üÇ,X
endstream
endobj
73 0 obj
<</Filter /FlateDecode
/Length 4342>> stream
xœí\Û·}ß¯èç jó~‚ º¬üœX@>@‰kvşÈ)^‹ì¡¦G;»­liæt“¬;‹İU»+ÓÏ&ğçÍÎ¾#÷(cÛç_~ ëÊ±i+âöÇ?şş§í7àf—·ú<ÃøåFşöã–?üñËÃ?êí—ÿ¤ù|Ô›”JÑt?'DĞ­ùn}÷éá‡f‹Û§Ÿ1Q¢PnÚï>He7¥·O¿>üYmÿ²}ú÷ƒÃõOÿØ ¨0f||´H@XÏ!etl`ò¤Ÿ.¹íJÏ(—n^DM‹ï˜Y9™Å!õ,îXQ®‚Ü$¾"Ú|y4´ÜG=“;Ó/¾LŒŠãgbšşŠ?¿?HévG?f“$zeaÂJÚİanÆz'“¢%ò'6ìMt`aÇà«ö¬à&z‘z3ñ¿1îb%v»i©ƒİ~-_Œ|{¢/†2$DMİà´Ñ²`Ú$ÌE¡Ú}BÇí3ÒK—æóq÷ZÑ1Òä2NoJÂñ•Òƒ}b¬Ä5W†ŒqtŸ×
*Xİ…Ñ*Ä‚¹h°UÑúz§¥U¨Æ‡Š‘ÔŸ\ôíÛ}Ûµ–¦ßLˆ³ÄWŸ’°hóÃâ.†]Ag†‘I˜Õøaìæ÷³íbÜáıÒ0ù&ƒ
LŠi]äM¨ÑÎ*¦™„Aƒ†i°ªã<ªªÿéİO¤°±iäÊ´…€„E[©Ï”tÂÆøIU‘30’²ØŠˆJFÇD	ÌïÒ.ô„iQÔWÕ“P“„Ô”˜±4cG£”n_˜´Û™!µi™É1˜q6R»7˜­3Ş»S4!1ß©²dNÆdÎÜ±i‡¹mU"óñÏÿ¢ğ¶üE…ú9(å{Pø¾…ÿ« ğÓ9CÉ;òJBò5JH‹¬eˆ@ô%¦¡Î aÂÈ1J U£aQ"A¹ä›¢09G‰„MQ"a‡(‘Ğ)Jd,E‰ò±D‰òmˆãfX§äÛç¦]Éä.PÙáÎÒØæ^UåÃ|¯J‘;i—7wçªîõUƒ5.[”Hê¢!S”HĞ%6G	€aŠ	²Ğ2c<aŞ…1J <BĞwš—<a `Œ	5I@M«"}«¢|"D»Q›–™[!À¢ÊDb†™8c¹ûB“s™*Bæ[LÔÌ›R˜·Vİ1×¾%cø¾Ç‚ï±à;ütöéÆöÛ¾«(a/È~Ì®=':øFŠüÈã©†@³+B”¡QÈP·ke,ß1
?„"U3ÆH’…¤ÄÆ('	'™ åJäJAZ,4&d€¤L¡ CäğÑì>JßARjDö%=»…VJØği¤Ii‰ÂŠ€Jr8?p; Y0i‚6> Û¥iÎ²0Pà#
HFgFÒGœ$©½ñ™0§Lb©¤`6É¸Š®¤¼*â>º+£¯ÒÇééJn„wkèü]°%2G23%èá¯K—l,fÖÁ78_e+cN>ÉoJ¬í.‚D”xC”(m5íFHÏ16†Å<XVÉc@59ÌJÊáìÙ¿„ZèNŸ‡@]-¬,¼:›W;^x„‡ Ì0Py³[ˆcXBy·EÆÅ‰QàKY©º„’¢ç°€¾‰".X“ÙÓCSÀã´ßú2À >O!¡Ì!:›<c! ßCzĞxF²‹DM•DÆòaI7³Êˆi‚ec«ØMSœ–¦SF4³’ÆÜÑrªQ0‹¨‹O‘~Ã&r4cıØ”-KLg†‡Ë†ä!Ôçóˆ*Â¾Ã¿®|†{Ûö€y§GÑù/Šê´àˆÔWÇuàÔFßòÕä‡áÁ÷q”È¢£W|ÜôÀ|Á¶vş?qcÁÙ{ü+‰3àïw†Tƒˆù­Ìğ}Í™”Ø"…–‰7¶&ÖÑ´ÂzoËº$Q’¬Éë'šB¡EåkÂŞAÚJûòæe éı±)ƒ}TD&é’¶’‡ûwk‘B`»7>Ë1™è„­¹ÈóQçuì})yDÄ¨³ú*ç¸µñ¶û‘ ¥sÎ¿8/2Ã</Ù2Ù˜}É Tv“nK\uW.Ğ6ê”€¤nvÖØÕ|ÈÎcüè,Éq/¾rÁF‡›_™!3§GJ3ø—ö”:ĞA‰&oøéæÄ…„;±-Õ]ÙPR]bã,(ÊØs<x8¥jm'U[lWeUw•Î±š}¯±ó1Æ¾f:qÀKpnû}^¾_"\âïÄµÈ¶éh>õşD ×é½I8ˆû”z¬9µm^PÛ5²¤Õ-®ëÜ1$âôŠÉ[$¥KœªRQ¾H-–«©,IUïµ»e”Û„èoÊ‰p({õœˆ¯i»HZHÿØ?'WûĞİ«æJé³ÌşN÷'Q‰{åJ8¹™Ğ«™®-´Æc¦tCÆÏ+r_-rÌ’OÒyÕƒ±Ú3|´5–8c¬R‹W7V¶æ7’Às’nHàé’¶9¦´wHàq|m©ïË%ğ|•sÜ†ÛòSœ÷_ÄÉU+ìz©-qCÏF9¤ßFß	{‰~dûxÆÆ½xÎÃ)U;=©úJàqßRÏÈº5çâ>¥p.Ç{nÏ×¹gHÔâ5ó¾Ú½ø»Iƒ'úL(”{¸{„ É ‚Ô)ÆÕÕ=^œæŒ©ju.ÃIºn¦ÆÔøÌW¸«‘êøšFª#7Ò—HÎù§TgÃ)Õİ39gk~+É9#é–äœKïEË÷ùÛ*X™vMbTİıM*‘Ş.G«{‹É¬Ùzˆ5„d3Ğ¥Œ^ô^“$èUšƒ‘Å~Åæ¦Jl¬ÖÊ>æÃåELîK‘Tª¢U¬"ºô&;å¯Óû¡0¢@æOÌ´\Ü<.Y¬bÔÎFçÂQ\JËèŒ<±ŠµeˆÄä•>!G«êÌ5ªñm½"µÖœá?.Ö_kx©Ç÷¸TóTğ CUAÆR1—¡âäHÕF	Ù›0U½k·2Œ÷ÖÌ;zImè}­SN%YNoÀœ€¦À0²`ù·¡‹Î¥",B‰;`B"ôóFm†–³äÊ†^E´³!,½¹.Í˜§¢: ã¨6ÊÍ/»İx˜ŸÅÁrŒÓ²­GE»ˆ*1Àš%§RöVÆ9°»Ö;ò
=AãVr©`W íĞréÙ]Z¥Œåla~ÂVŠF,WYù’îM]*«vZÂå²²‘b5ÑÂh&V'æè‹Éƒ™hTZ…‰‹fŸä
*LÈJé
 ¹0»QO¶ªĞf­3Ó%nÄ­œì…¸ÍÆÆ+Ó3Ø_!{°ÔÆà`ÓYƒéNR%;xSQÁàuEU±©J2ËN2?oH;‰k9j‹t0p/ıœ¨´«˜9f‚4£g1“¶?‰ƒ)jPİ;UÈ9–á ‚”&ê>ÂêQ¡\Û¾ÄÚeGJå&1ªüJOå¥ıpµÈzÈJº_!’•V")•EÊ
²eoó8#`	.{£:Ö\|(Æc#Öñ9zªvhévT'x³‘”­ûÀ_Ù8K,E¸¶„µ¬V¶$wíË\åmèƒ>¢Y˜tĞæë«ŒA¤û!œPÔŠªõT§8+Ó5‘åQoë…(ã	bÍ»Â7”©Äñ:±qAÓWıc¹.\/Âé¨KFcYB(Ê+
o©sjGgsjÌªqÓòéP2gvÔq&Â˜ÙSjÚ/]Èì€2;ª^œ3;`2; ÑØ1³#¬ev©©mÈêe–XÔYxÒ×ã©J¥Œ§4•üt^y–T¥Â³©*=vu9ó­(Är…•/-±óá˜Ø399c+ĞñGÍ™÷ÇÌØœÙÑû‰cfôÙ›3;@9ãbò–23®&ZÔ—Sb—.1#¨Ã¹¹´e¸]r¸ùUª¹¡vş¸IApË¯ò|$\Hìª
Ÿ,±K*¼–ØµÊËeÂ°ŞíV‰Áz'ZFğeñò[ízC­û¿	>½Ú¹ø<®¨}…$¸şRzüÃi¼Fpï#8êv"8aVæI˜wS·BÎæ„ÍgsÂœP7ÄoB<b'wHÂÊI™¹.¡óÉ<a5~[¡§øİ.÷øÑfaq†­ÇR£Œ®B?pŒO	›DXÄl’c±µ‹˜á¦Ë•U¾Ôèm…8DoÂæèMØ…è#5cô6Goj×:FoêÇŠnŒŞÔ@B;ßÔ¡5‡oêÑšÃwŒ%|Ç8‡ït‰…ï:œ‡ï¶ß•¿+İ<~wyü.¢àñ»Jlp&ÛÁ•Ä!€7mÅ¦Å+Ü
ÛŞ­‚Ïò(¸ŒJ‹3â2}¼õ˜½ŒŞ«B|¼ÄÖÁûöSë‚¹µ\—±{¹ÍñlÚEs]·s¯eø³JW[ÖúÔxóAúÚ°¾X¹ğîŸ,Ü´gO7Óz{^±ŞÂoÎÖ‹/¥ŠhÖ`~zó³œÛW¾9mZ+ãF\å'Màa~ÙROĞÒNyç­¿/kè(5Jå^6ŞQŠMJçî±ŞB;´Ò‘µ“Ò™}·VğfRrÍ]k¡‡VREµ#R
ÉIQ_ï…, o"-o!-Pï¿ìs÷NMNEoéìôöÖÏÎ×€éÒQ×°&¨§ŒôÉ±¾Q£´ÜµJ=•`
LæßŞÓªéxªXã(0êÊ4–5llm oí£»èû*]Iœ®ÎNyW{çğ‚Í;G*-·¼sTéÖŒÈ1‡R²ÆQ`z–Õº)L(ïˆÜ"
ÍÚF•.‡½	²A¼o´¼u´nİ—lÖ¦9Ó:Ù­ñ“±×:D«x×h“ï5$/ud]£À<u§rrè/LX¬ªN¹em–µª¼³¬g´ ¼e´@¼c´«rgS7D4U2r¹mT¶öòı¢'
®÷ŠJzà”7Zõ¶Ô_<æ:‹T )X‰JÈµ¦ùMûø•ê²¾Î¹z'kA¯zìu(©»à}¯iôÕ:/!zÂUúXUi_î$yºÖëR™ê…\aijH”¥”EQ>ŞB¾­'ËÙz@P¼j—$ôA´ŒFZ­ª¬•qµø¨”@İ³’—•(u"åÛ¶À3Êx¨f´Ôãô©OÊË_j^z~±¼‹­ÖÓ•
&;Ê¾V:¥0x•|,øÛé¾·]µâµŞ;ë3™Y©àj}8¥2;•¥+VÈ¯‘éÆr-2ck%ú¿ÌC£Ï} ÿŒ^¨®d’Ÿ*<Ä^Wùht›>ŞÁ¬$ı>Qªè=§ìÊë~Œ)2±…¾Ç®ÇæŸj¦,½Nü2½=¿Ì‰L­õì¤Rˆ:K®ÕL¼1à±GAYŠ©ª2Ş£hÏ é6{;#ıãàÁ_'*³p6WjRIÆêé¥Ğ‘úk%‡&Ğƒ«qÌ9;Ä!è%â›wqöÏ’QÄnÕ@’ú³ê>³^ÁK~`xÅİåß·',Ï¬î§ºçR¢ÏØ:'ŞÚæx½óWºò)¼¦mÍ4ÿ¹.Îb¸-â˜ İÃ‚‚r“Z®»·Œ"ZÃv€”T™>Ö°,'İÿá²Uõñ9‰5–4—±sN¬Æ¾¢åœ¶•~q¬Iñ©“x’%÷2¹û}1g-…øæT+É/Y„÷°cKûÒ¥_rCÏ©ş:S½
endstream
endobj
75 0 obj
<</Filter /FlateDecode
/Length 5158>> stream
xœí]Û®¹u}?_ÑÏ¦\¼“@`ÀI~N, 0‰’;ÿdm^«šênÖŒ„‘ä#ŸZUEî;77ÉšM›”ÿ\vüıi£ËhÕ–TJñòË§—¾È}mã~1nO—ıÏËıÛåÀí¦<¥…ù
/ª‹üıÏ?_Ê/ÿúÛËşl.û¿Ü^Hæ¢”ÖÒÜ_3²Ë£å<úæÃËŞÛKº|ø+Êª‹	[ˆJ»‹6—Ÿ^ş}ßûãåÃß_<îøï €=!¡fÏ@\·¡TL\y%uÀ–Fß}¸N8ä¶iQ®ü±}èäüÄ‘•ó+Gq(sO¬(×Q]"$¾"Ú}şmhy¼½›#¹Gú÷ÏcvÍÄ„#1]	ÿ¿ÿ|QÊo^şØ‹ÑkÖÊmm36›˜”tQ~£×~JITgğöMƒÖp›Â^,zKMñ¿xï¢½oNÈòáò©^(‡¾?Ê…Œ1BÔEğÆU1c£`>íº?·[uùEŞ*(_ÚÓ[0VL	.T!‹›ZÁóµ6ƒâ]…{¾¾ŠX¼<L€†*šÓèËè˜*æc”—5¨J.´'A’<éBl˜8Bûõ—ŸB¿ú(W›1Ê‡ñn7‰š,9ïÃÔ¹OqÓ^'Kd
æş;‚‚g¶}JÜ_Y’`*êHRÈìÉ§IŞ‚Zã&Íd´¤AÁšË[Mı_èyA …5›!o=±äõ…R€"…ñ“!-ã¾‰­ŠhºåZÚegÕ5ÕdÔfu,‰(Ú{¢pmúÅÇ2ş8Qo–Ì­Š­6Ã¬¤^†ùffÈÄ‰åá]6ä2M„ä[$jòÂ®òÖ¦;rí_^şW¢B¼”ÿI0h¿ç8!üˆ?bÁXğ{ˆy C¨YFmÁ¹ÀÈ>­u:‡Œ;3 ˜hj
@!£)8dÈz5IN040E€IÒ2•™Ô%˜~=D‡‚åèP­Ñ¡^MÑ¡bl‚­I6ÖÑ9›u#“M¿±ÃN2øfwj"§krdïg?nºawo:lA´<ÂƒÀ€Ãƒ@Çğ Ø)<8w
9&ÎŞÂƒ );ô¥sÙïXèeõzŒëB®z„(s„h³!µfÙälœ•R2áÆÛúàœœ¢‰ˆ}§J’lHœİ±é†İ¶ª|ü¡ŒáGPø~…ßGPøâÔÁšWèàâ!J!á%;F	ÁÎQ"8ŒYq_’œ`‡y0·‰Ñ²;	ÁÎABĞcÈX	å×$ÊÕ$
ÆVØšd{³a72Ù;ì*mö©&ò¼&EvÑ!ovæ¦öù¦ÁDÇ=FdõO1B²å ‘1oS±c 1¸ÈQ"cNf=c§(‘Ñ6ùªÂ†Æƒg±gÌìn=„‰‚åÛ{-LÔ‹)LôÇÉ”z³dtD ™g'uXqçˆ¬xnÑ…DŞÓ…I~FR'ìú!Ïíz$?$}ø~†áwşrï
Éå/Pê¦“­jWÍ|"è§Ô&ëZ;h4›ßwHIÀ´«˜A·íÁîè*ÚM!ŸÕÂú“µÂ‹Š×È™#I‡òõ…C cYŸ‰’­½Hü>Ù-$(ZMízdğ»ãN ÊúÜf‚aC”0"& ’*_`6'°$¿^Á*¸3d1kpÒ{ï DŸbRD@/«±F6+ù€Á‘I!?[ÙÌ`°9dvĞe	7É5LÔÖL/UP7CmICÅDş0bôdIbŠbbz—Åc‰O)†laù)Z_-l“È(u:h&ª$JrjóÁ8j„>íÄÂœÙÜn÷2*	ƒF‘Ø HŠSÂÿœùQè¾O™nbƒgW+˜X@ˆ»^ÖÁn"™ºÑ0,«³‰1E:ˆ{+=Q¯CFİÄgÃH~½‚Ep_Æ»°&¯9÷N0u…¢%r@1´švSš«”§„‘Êáïe°ˆ†nmæ°‰¢`%6‘5ÄtÙÒ»MÔE×ÖDLWì zØÉ`î`;Í¦X×İd]¹ü#ñUR¥©¼,­Ğ–¦­õÁB]™vğhçöİşŒÿWøÁØ°¿Áõ;üØzÏ–k¹gãxJÙmª÷ßâç½ì?¨÷cÅCÁ[û‚KûûÏò3-¡Ÿi5p½h…u&ù°ò¾bzûŞXì$ßÉ"†ÀïÅNò,"uûŞXì$ßÉbŒ§ç7çĞ
ò%ğ¯MÙÑXÛzt½]°Z»^ÚK¾²ªÈTG¬÷™ıŸç{Yüzıœ“çŞ_ïGîç6€»¦†wõÏµgÊ5÷oßU·çóıFgÅÜÛ.Ë;BæBu&aŞ£T½kÿÚ­ú~ÛÍ¹¾5q"ûN6­û:¶‹ï`»ïŠş»(=‰‹ì·Ëói<ßì'ßoâÊÏšæN2‡º`z‹•±[4Ç¶_nôıDú¢w#IwÑDò9b•¼Š=…,ğ
ÅâÀ¢
ûÃÌ=Ë=ÔÛ[vÜ®»‘x{¨]K=Œ}A4¸éÅen”5Ä½ŞE¥~(íĞÊ¶1ü5JÊƒÄûê(ÇÛ4ÈÒTÔR¯bRé_gC%'Õ²ûh&IÚFĞj!¿ÄäĞwrNÍ¸¦İ1>&«ÇvR[ØÆ“Š@ÛwË6VĞá]ò>Ş~!•.v™â$¯ÆæakÛÀ˜ÌŒ¶ª_!Ø¾½ŞKJªIó¦±³µ*'¤õè~-•å+ë^ì»%/+¹²åÓKÉÑ¬º£—Àã¦ Ö@ÚúŒÀjYó˜}¬ÕµTÊû}`*™IµOJ\3Sºz ×Ì Jõ.WvFAEfÆè%D.¾ÈŒâ±vª™6µSŠjfœkfâšY¹fÖA*:N¨@ÅQ1kOe¯ÁæÖ@²&¹3ÑHíztÌnÖÆ@ƒ>|ÒSÅ(äse·ñ,Hµ4R½,cs¹¬B\-oŒ†º˜–¡ÙAõ0ÁİÙ~Î•2	Å²¦¤Us¨•)i"D/K&½¤¢d7Şr­LÉî†`]t\+êğ€“*r¯çHU²|É%²p}¬¼ĞëKÜh/EÍı÷¢ÓÚ«[ÌU/‚uş¹2ÖÅµ1-ÜEÕÆ´Vbf‘kuÀ0Õñ@a*{
TÓ-tˆ‹cäêØx¹	ºèê™ˆéš$²Ù6{'{ùÍêcŒ}eŠ#É®s‘œâ´ù‡’4§'ÍV$˜gDùLÑt½N˜9¤ÊÜç^rÛtºcuú”ß¯Y™ªù©{SóÔgLgHcL9&ÒßOÓ•/“Š•ÅMçs|Š}õq¿Fı­”ÕÆ´Éº+ÕÖN8LOı_5úMRBKÍ_m³5Æ©‰LÑÒ’\¾Év·WmÁ>UuCSû>u–F³­rÇdİ,šxÓg…æÁù–éó­o[IcZˆnÌû»$®ÉtíMéZ ¾şõ'Ë4MqƒÔ›®HÓyóàÄ×\™m~öy—¾•‰ò åNÒÃ×)J›4¥ÛO-àºZğu­€\Åq,T÷âp±¦b ›Ã³HŸ`x’·b±s—X‘W=ö¼qßK2H}v’ŸSõ¹TÃÎWÉMht'v’›ä}?%7™%%qü)Ô;­¯Q+J¸2k›Ş¹Ï6İc¹Œæ{ö™ßTnBd=’›Ğk÷))}	ä ó›ÏMˆÔGrzí.ÅIë¡çÍ7SÄ¤üöE|—z¿|7CÅm{¢2ºÓ½†Ñº¡¢tXU÷×µïš’8Ù0›‚Ò¯($?úÂ,F,ßXSµ®b/9_¯Sô¯fXÙSìuº|z±²c5É¦ÕŒl2ÇÔÚœŠ‚E‚sù ³•*– ¨Ù·}ÏOú]®˜£À¬BøQ³J—·1§÷y· B,0DCÅ‚ÕĞ3.V,æ4P8¸¯h²NÔŞIA¯bÒbiJv0ZÙYmC4|Ûo6$ï¹Ù¨m½QsnK15¦òÆ¨Ä¸ÍE¢›y…9@µN±T°dÙuéyÁr«ºœëÛp©PXiq¬²z‘ŸÍ¿–hó‹ĞB‡.dE§v1ˆ‘Ão1³2ˆ–’mP3{rÄ.VáA …›^&ÓÉR®h¥k £Ë¤(øC¥?µç[díu6˜Ş[V%‡°QÍ¦:øc£n’`ão›Ü¤Ëvr¨ª…Éñª¶R×¢œé¨‘ö¸¥aÏæÒ2“UÀœMy{w÷†ü4¾jè ÑIHí¡£$²Š‚©™Ç -õsl/‡…<ô²wÇx&‰”A[ÔCª]Û=PK5j9§—|<-¡æªzJZ Á@ˆ§åĞ+}¿kòØUò<¼,¸[wıóâÆ²ï6^YÓÖMæêğÛJ¬i"*Öçá–)pM«6B‚{¼ıÆZR+ş>ÃF³BLl0Æû³é¸…%>d¡Y$có&É±Ãš=\²òé£Z{Àãš×]`åËç—$-™`	zu•V$œ1^”ã5|î#RFıÔ
}wİ¨"õaÿÔøKŠr5M¯_i§d‰Ã;Ù ,Å^U’Má6¹S	÷ôaÃÂ3ªĞ{:o:¤cNÓ1`§tXMxDrº$<r;¥cÀ®¤c@Oé°S:æôµtè)¬§cùLÓ4Ê·Û”´V8iıqvÑ(ã,¤qÀùÊà•3›&Î€šô8Wræ¬ªiÄ±ÊêEOÇÜ~NÇ€Ùà]ìõ16mr*b"XÉåw€®dc@OÙ˜M§l¢›Ó1€ğË9“ëP9¤cù™A{fôÃ¦U	blt³­Ùª«(Øø›Ä&7é²ªjar¼Ò±¬Å[é˜•æU"³ÌpÍKne87†Š)íZåë`ÙÔ¯1Øòp4%¨©ŞˆrHb•ïIí¾<ƒ;÷±
ü«`¬¯Ãƒ„`Î0§üléÀ‚?Á"¢Ùy<rbOÍ>,ÚlrÆ¼#ÆÏÃ°`gçöÚh ô4ÖGƒà£A»M±¨µÂAkôÇÑ­ÆA°ÑÏá²3ÊaµI„Ão“ê.bèM•U/úPôy( v
‚¾6u
‚Ê_7›™Ã¨õq, j’™Ç`ÚÆƒ\Õ•Á ¨ó` ÓàP9ù[:£ŸÉ°*E“VÊ'Kí<N6]¥1Ù¾:C¾“;éópĞ4–º&o!|ÃÁ2†¯æ&Ëğúğäd5;ÿFÇ•_-¸Ÿòğì¼.! ¡‡¸ß®ˆ¬eş°¾×\ÉiUğY·ô=Õ³î4œ»æƒ“åğdô.Ó‘c÷7gíëYøgÈ× ë–‚ºŞĞÃÒ¨«ig™´âi¡æÊ”}éI«7n×=es-fĞªO§sçZÌ²R²¦jiÏëÑÊBÖŒ,»d£/*—8¹c^œÜ9/æô<âº²l%’ËVÀNu`Wê$r¾àX'vª“ä5íSfœü93¬gÆ)3ãv›³Ö
gp£?Îõeœ68{¼rÙ¤Âùh–Ş¡N’å|ª“ˆBz¤i¬^ôäXf“c`§e+`W–­’¯~Në$€®ÔI€ê$Àu@§U+`§U+IVCıåç[læ¼jÕ»™Ëœª$êÉRÍµ*IÄdúU^““Øò•ªÙ™ìyÍª©*uŞÊŠSßĞéÁo™=­ïr4X²j¯£Š°z^,x4[ş&³É‡Sße6¹ìš£·l\ıò~]_®¼-W¿JZä®¬à®éÔúeumY¨»™‘ß½º·^`{XT¿¶¡ß•üÎ{¤Î[¤$âs(ËŞ?«^[óã³©Gnum)BÙ‹„ê®Éöó¦Îí?Œ$»S¼¶ö…§i-ò‡ÃèttçÃ´ å”éôı9-èRåte?›]>¹:}NËºä+¤ÍØ|¶C|¶ƒ|¶ƒtµ÷A§V‰:ßÚé¦s°¿	;¢­û8CRË>{ÀäÃmò™îN°ü7;¡š?Çgh3–•×¤Ğ>BÛ0>CÛ°!ûÑşĞS2ô9hz¼læ|€ÖsüÖœñ|~`9iJÇg5<0Iåã™ò=A9½Ê‡gµ|80)gèì¬ÎŸ-'BÛ§Üú¹Ñúñ´q¶´~Ä­?mƒªÜù8Ò:ÈG_;ãˆlã›ÏÍVùğ±Ylşìš¥c³Àò×Ù˜`¢¼˜¦c³@ËßèØ,°üa8>7[±ùÜlùÜ,½İNtÍLätádÁ£|É¹Ù;ÏöÜqv6ŒË¾EĞg|_'öÎy[¹lÕ¦Ã#ckè+ömË$a/‡4"í§{£óÁ¢P{İ§ñûÆgsâƒû³ã•MÑO‘¢íS˜ºÇ»8Ÿ÷•¢Ñ‘®…¶ºÓßGmsë'pİ| 5•õ£ı|î«}ìÇ“Šd»º«†¡{6.täÔS>}o/ğåËçèà­o‹o]ñî÷×3“ãÍ{w7?W”ÿÃÉçS×ñYÛğ‘l~ü<ÉşX…½§¦¾|˜«ß{‚üTşõÌÒu7¦FÑ½ùMO³-ÿ}®zŠe§ì3,&ìíPÄvû&ßÒF—Ÿ…K›ßËq2–â]†ÏÇ"Ÿ¼RÿÄÒW^£‹¯¼Fû}ôz[±`z^°2~3©â¬š<Ÿ}JÜRÉm*x½¶vdO¡œº¦™‚ı? ×
endstream
endobj
77 0 obj
<</Filter /FlateDecode
/Length 4765>> stream
xœí][İ¸‘~ï_¡çFáı,Øn;ÏIì˜\'@²ÿØ*Š—¢ªE£nÏ8mO[%‘¬ëÇ")‘«Ò1ıYüıi%—ÁÈ5ÊÃòó/OÿzÂûÊ±h+âòï¿>ıÏ-ÿºY¥ƒGıVCå‚ÿô‡eûåßúİôò÷ÿKõù¨)•Âêş–(İ~G?~}úİ³Äåëß ¢Ä¡\´_}Ê.J/_yúo!´ııòõOîıËö³'øDğ• E"¾)AW‚İŠÄJ0[¥Ÿ¿3z[•p.İ¾µkäö‰½(·EöêzO`à8WA.4Î1í^.Vn¥…Ş³»ç_¼ÌŒŠ2ã÷ÌT#üşşëIJ·:ücéí*8Ï¢”GVÒ®jjÎ¬Wt,lhûşI‚Ó(³Æ¨ÎıZA$˜èÅæØkôPı?”»%BJ¬vÑZ;¿ü’/”·aù†3$ŠG®|Ài£e¦i“h.
UŸ:.?cé ½t[}nõZá“1¢26’qzQ @)]hà§PVÂ=—‹Z(cğ9¯=*Ó‚„²jF«3Í‡…p­/OZ—t >ÆCùõç'}½ú†W«ÖÒ´‡‘â,ÊÕªDZ´Îù®qÃªœ†›H³ aMÄAšwŞ;*¶‹œEICôƒ4T ZD’ÑÅNßH5ÚYE,“h1fn6"­Øx+UÌÿí‰<”t»zÍK9H´hû«@5Ø­p–(Ñ¬òTôDó®(.+)QctQ&Ğ rï¨ÚM‹lÀb D5Ú,ÄŒ-ÕXÊa)¥ëÅ·'â"õqâJµZât„â•ÕæÅU"âíDöUI$zª2Iœ­“ˆ¬ö!‘[íHâüç§ÿEˆËö"Cù=
˜PåŞáşã€áÏ¹CÎ?r ˆªz¤ ŠDER¤H4mz	vƒ@ H‰bœìT‡´P€’bQqµÒ‚tÍæBè"Qw@±ÑPä_3Pä«(2úa©’zlkœúva“Æ@‡FK›†UÑ‰¾¬D¥MÛ4‹]hÜûd@7œ78p"àD8Â‰p€á 'Â!N„œ8q"àDèp"Pœ8p"àD8Ä‰p‹á 'ÂN„œ8q"àDèq"Ì&ï°ğï°ğŸw§FÓp"‚{œˆI‘¦Ã‰˜i:	v‹1)’âDLjìq"¦‹'b*ÓãDLU÷8´[œˆ»N$Ú†Û¯'¶«'6õÃR%õØÖ8õíÂ&"–*6«¢}Y‰4J›¶i<»Ğ¸/ö+Èk‹ÅøN ” (N$šËø“9H´=N Ñ¢(N$šÕ’Jh78Ô#ğ*¦
O$à ‡ˆD5:PˆH4»Dş}ˆ|ÑD¦ªUW#§,\6×Mr÷&Ò¶8¨j!ÑRÕGâŠè™D`µ‰Ôj9×3	Ã;¼Á;üÀ@ğç¹e’åŸO`ÌUE	KkÜ®ıBÈ?iœ*3JFĞc!$ƒ¥\€T
‰Q @G2E¥‚?@t ¢“•‰Rk£Àç,¡9	q‚ZÒz‹DB*‰Dp³q‰Éà.«ÒS28‚U1…#U xŒÂÒÆ€ˆw`Ú1¥¨ü‰
DÈÕMj¬ŠÛ‹jR™Lù­'‡Õ‰€øZ“ÖŠU\bmŒRj8d™¦2Iˆ,.õ*µr©‚¬šBPåE‘„Œ¦,J'U4óÆš);ÆšÙ‰ÍAˆ¸‡>†îŠ¨®2»tSÉê€üDyuÀ¬× ¥À °Ø|DÛiÚcÍ­Q*‹¨ı¼Ô2 ÆPãêÈÜ%„ªU5à¢@ÔÕÿ2qó?*dÿ«dô?€„éªPŞ¬tÔ5¦< JşGùR‡Ru2(Q\ÛI›‰j&UÉDßZ@6«ñÒ&Ærc@¤RZÂÁeä*Miµ@ï0‰±,.ë“ÿÕb2sS$!cUé´ŠbÚV5dÏW5:•:S•öÈÃŠûÍ¬£ë/Ûÿ¯1Õê)mà•Öº!qºÚmpU ‚Peõœş”•nè* [Âîi^/líiå}ŠÛ6¼sio»– B…	ğ/td6l×VÖcZ“i™d'ÒÇZ±Ac‚ùãö.HwıB¥Ì…˜ÖP¿UğóŒohdÁüsÛö¡ø¶ Úçí_Ô#êÓÀµuÛµøÔ½ép[­G4;ß¾Ú“b›Ó8qóüj-Ä$
Æo:M²£ñRnõhçzş\ä„[İ ä­nó)OØb=t?¥"Ñhm”“[J­£‘äö;€\òó%ûóÌxĞé­Bâ  ojÀxø¹çµ+q«‰2ûÙÇ{ÄÃWòsŒË÷e.c³ağ÷ç.ŒÁû`Di1UŒ„®-Í;í‰¼™4(/˜JD¸ö¦Ñ Söé;­Z|‰G``…˜ß3‘µ¯e¢—îQdÅl j«Š€±©>dËŞzˆK€B†.ƒ†67dƒƒ²Íc¬³7¯•0Ô¯…•ZB2–±2¶0Ì/%>f„–VîÃÈÓ%4bòD"ükuÊšß;-ˆç3ä÷8lW{ıx"æöSÏ[q‚*ß	Àe´ùmWÊä% Ş9B­z#N‰lİ?-:¦jÏTıš@,LRo­¼¼“ô…67¦åPı¿•Sr¸M”®@b%ü«!1cß.k%­}DÆhRh²N	ØÔ%q®}…[©9óBœÖ»ánÌ•™K ”3Éjæ;æÔ¹*Ã×@r‹øVóV[ÁœÓzĞ3ZUtN“£›*W¯‡Í42ZsCú&i):¤oäì5ÀFd8ç ÿ˜íõ¡Í àuºWìœgR*Ì}ÉÏ~ÈÏø­D+åÆd5ânÀ?ß+¯ÓŒšÛ ]‹ì%y¶-É(¾ê×,tÒ.h.İZP@ÕçÄ’Ô«â¶}zc¾¤;ßßzcƒjœ¿uÆö•U–/®ÚÙˆo.Õ"ÛçW—ÒB´ªµ’]Ï¬ÁŠTû„+OÈØèÑß|Ot[Àn_Iœ˜Ñj"‰­w\ˆFµÊÌóq#<¿æ3+ü–\;Š^„½$ÅC`´ˆ©ß¿=çz„‚z¨€²ÜĞ ]»·‡¨ÁIKÙ
ˆ"7xq´Vîu…‹ 1‚í”Î uŒÚ0Eh ~p?P“fJ°MäÔV°wôQíä× %<mÂg«:å£·vo¼[M±*dÅ`¿£ªç|Ã‚ãD5  [•.ÊuVFGİ~ÊJŒTB<×ÕÇÜ84 nNíÄ¹ç¼OYNµÓŠbÎŠÍI11Ğ)FM&?·¹i#@òñÄ’;ĞÆ©&úc¹£hÜ–ğS0Ä3°4ã´q¶^‰,XpJdÕn>®¢¤¨ÍZƒGUVUŸ™ºæ5r‡/<ü„@Æe§sãØ_r	è­¢‹‡h¿3 §’êˆGcâ†oƒwDÎ¶|_3`(€É@Rˆ¡¢Óî¼#àUÅÌd’ÑxÉAËÆæ´®:CuU%[®-ŞŒ Œ§½Û×pBt:ïzR¶ï-bpB'Í±•\$\•È4Fb½é.“Í2‡" t¾|ÂzYZú=SVSeÏ‰Ÿa&³Ó¹8à,¦—t0
†frÀ¥X+ºíM	Î§æ½“í|Ç|¤ÃôÇœ„ö±lÉæ[|†6ßÿ½gšÃJd²@^·oBtmq3Ñ2“)ü¦òe^#ó°vb=šUî|’;í$¼«ÿàC$^¾i­óHs!'mİIõ—òÏP–/sÇáğMê~ÂfzÂ*p$¹˜ˆ{ ½É ¹¨ìF4#“HwämÓbÌ^˜#¸~é0»÷œùœ‘×ÔôaÚ9§… Ø…+U÷'¥¬:Ê<ƒ– Qæ NGüù0·îÕ×ÍñÜüÜÒ<>­0t—ñiĞu¢w#°¡^&¯…5€5]È®œøù1úöKçXç‡GÓ³g|	Vv`X½]‹Dñü€ê-Dg[¿0â«šwv
»¥zJ(9 â¼AXïÈä€¸ïjƒœH:Oİ^ì‰ºY!â|z…s~Íwzuõt~1x:‹¹—©Æ®*óy “­óægÕçWÿ/|ë“ãÄÏ~Ùà>‡g·î…Ï—çxg—oæ_ÙŠË
î˜ãeŒ+³®³ÊëÖçx«³i3»F~İDİØ”ÑH°Ë¾óx‡¯[öe(>Ø•WV¹C“=CrÌ;ÉÈj£³¹a$­«_üœöC~Dåu~³õØ4ÓtW÷£,„õCCY6¯+næh~.rvºs>“>]ÿVíüÜìéLæ#>ÄWqÏ¡ÙZb>Å¦ö¶áæå×Íc®*h|İxd‘šËİøÎl:S¸ğ}¯;Váç“Ó±×	:Ìç³C£õnByúe¬+óC>ùÿYÒ{¾şË×qÓ@ECNéQ¥ê5ƒf½$®@ÃhäÔPLow£×O4Ÿ$¶~ıvİw|ÊõÀwLîQdwòôW¹¤9=[ÆÏ+rğÉÚuhú‰25ÿ†!a¿©/Läæÿf•‚G2Ö_Ï˜ÉÏ‡ÃóÖ•‹wÓÒãı‘X²ôÙë–Âò×Åfµû…êÙ‚üğ)‡8qÄ©ƒCWzàÊµ¾ù×¸ÆyË^6ó|åçF×åö¿Òlî&Yï4^øşäu×ÌÇÍ¼v³JN2Co÷+Å ½´SÄ#½g¦ù4eš«ëŞU¼)~^höÃÖù•åéÌ÷º¹ÉóIÙ‡óú_¬ä¿Ùø®_pŸNtªĞ[ƒ¾eH>É7Õx&¸”‡ÔÂÉÉOLú2ÿrœÎ[.ˆ5à[—>Øéºokæ»¿¿ªı•öïÓ³5W.2òs^¾ìvåGM×}ŒpıŒÔoåKÜ·ğÅ;Æ¹,š¼Á7Gó3ë¶ßƒ’Éãî«‘ï9Åô2«N×İlªJğæŞ"¹l®ï¾¡•î¡÷şGßïc7fbmldäss¶é;^¶|dğşæ/²¾Ák©üëóù8Õ-àp?œ½éIsß+_•ƒ™ÆùŒJ»Ü†1`(n™ÔÑU+v5t(2g¾ì>éêN±cB|'tñx&?ß¢¡¾01UoÔıFî?yIKW§jÑƒ—”u
bÁ‡îÜ% 
àZ‘S—”µxT˜®Ô4à5¤“RÚ¡>@ukpéœrúO¢á¡,äÄ¥F£.5*=o©QÛIE­v¨å¨Ôxo%U;RÖ=h©éí[G•r•ÏåªÍàÆİ«é”›ÂĞ ¨EÆÁh`/rÄR¢9­9a©ĞBwÀR£Òó•Zùf‰ÖN³a¨·qŞ| IxäC·+~Mñ¯FU6øâ_Õ¬1TTØšZ=Ú°Å$ôû|O>´¼ ‚Ğáëá>èéÌ)r R£Ñó”•§DÊ×ƒˆH;õÌ¢¡z¼Qã¼ƒD¬'&5UĞs”šÚè1J@Ms*†œ¢4<O*ÂxÎ¯”¾;C	¨x†Òä%<W`õc©*£ĞBw€R£Òó“Hùb	ÒL5YÇPµ-aúKñÀ‡î:9ipgêóÓ“´o;Sã«e3lW;ŞÇöâ®kƒìŒ«Ç¼°Ê¤joˆ/nú­cŞõ»5 ó–·i›Ø|¨Ğ¶åñÂH<ØmÛW¸µ(ÏÎ;À­éñ®§c›
{²Õv§¾Ç6Æ!E›(ûøæıƒÓ6é.ÿû,Ú>Âx¿\ïî×È‰'•}|ÓÓ'u§{¥¸2Ñ>´õéF-÷×X|“*ûÓäçlÍİ[é¡ä;+Õ&Š[›xY|ì,~m|6æUş!n¶¡NôÚøÃçk`ÌåÓ ˆt›?&ÿÄ½Í¿ŸÙWË>Ù.Ó3XrOe,÷Šß–úÊNõyû´çµdòG|ÕøzìPï‰’‹ï2èàd/ôşg¯O)wº„gpğ^ÇgIGñ“Û°¡&X=41aùöş	i¯¤Ş±2Äº:>Éaó@Êşá3g"˜â&”¡!Ú¶ğ#nÂ…u™ÃgÆ İ5°|l¯ø£‘<úE?›5´é™»™^¾w şÿº’–9
endstream
endobj
79 0 obj
<</Filter /FlateDecode
/Length 5233>> stream
xœí]ÛäÈq}ï¯¨g¢ò~;—Õ³­ü+K‚1#@òÿÈ[œL»ªºÙ½öªg5»U§ÈÌ¸3ƒÔfl..Šşùİ_“Ó[Ö9§Ë/?şşÄ¿—ÔÅz•/ÿø¯§ÿü—Ëßw›th¬#ÌßèD}áşã—úáyúıìå/ÿSÆ‹Ù^´6†‡ûsAZ?Ğ¡Ÿ¾=ışgwÉ—o¦Š„úbã“6şbìåÛ§UÊú»|ûï§@¿ûÓ… “VÀ­@,@€UHÇch] ; _OÉpuĞ¯ß®NvÛŒN$×aÄ,“ìXUÙŸ²šCÛ88âHr“ô%‘Å„~^oC^–³•]Å]åWÏc•Aaâ¡0ÿNÿüıIë°şã.:úM)
‹1Ùh¿I‚ÙnX<Qı'ÿN+ŸÚ‚·ãÚP&¸Uì-GÿMçíAÃ¨Í_¬ÓÉ]~´/6S´|ç/3Äl,¬³ºaÖ,deÆqÊæË/|vÒQ‡:Ş¢åsf[TÄ²Š¦ü7ÆvŒ&¦Sù·ĞÎäsÂ¥ÉOKš0šÊY“rÃBJ|2•}ìG’¸—"|r1uŒÓ¡üå)ä8¾}ço›µÚÉÁŒÏjÉŒeBœ&9m&˜ì@LÆ¼¥? c1ÄPí3ÅŠÑìÃ˜N&‰±*‡<Y›Qgƒ7à—‚‘ÿø±îázVwş÷'82‚¹À¸d `Ù÷±ª¤z¶Â*˜·5/X¡Ù­ÙˆĞjŸfGşN£ÁDT×u×ÔÙzds`ÁŠÇgŠ;¾|‚ĞhĞB&‡ ìRJè= ¼A[ÉƒaÈ–a>È+°3dàğdêğäõ/OeJH—ú?f‚ş¹9ˆXäƒ>ˆàƒ~óDğÇjƒV_´¼öƒœq~fB[™¡`¶Ê54`lÇ„Ú™
²0CÁf ÌĞ9™¡`IÛÉ]Œí˜¡ 3T¬0CûØ˜¡}›˜¡a~}HT™#º‹‰QßÕÁüjc"uû@¾5#b^Vkû™š_&fşë\Àf`çÏÌ@ÈF¦˜±•#cÏÌà©Ê5>MÌÀ˜7qÒœ±=3x'f ï+30´gFWf`¬3CıÜ˜¡~™™¡b@}H5™ƒ²I	¡Ëz`x‹¶İ,˜-İ|˜WbgÌÀîÌÔî9Èë‡J„"ø ‚"øíÁËK„”€B43„¨wÌÀØÊŒí™!Dµ0#+30¶2CyÇŒ­ÌÀXÈzaFWf(Xe†ú±3Cı63CÅ0üú¨29Ft£¾«ƒù1ÔÆDêö|kFÄ¼kcw¿`¦wÿu.`3°ógf dÇŒç'	Ûİ<¤´gÆVf`lÏŒö¬nË”(ïb˜¬Î˜U~¡Fu=¬ŒØÏQ¿ÌÑÇHêÃbÌ‰ ]Tâ®»èYÑ„¹Ó‰Y&VÇ|ìşÁ¼í~„,¨`ø …Zø …Zxqù@UğDvzá‰²2¯=lY{,Ø'²ÍO0²òc+Od›v<ÁØÊŒío,]y¢`•'êÇÎõÛÌÃ8ìCbÄ–Éw<ÑÅÄèê`¶µ1­º} ûš1KÅÚ˜Ïİ/˜÷İØÃƒ'Šó'`d]{,ØrcQ°•'ëÚcÁ–µÇ‚íx‚ĞéÆ‚¿/7ÚİXt¡ˆŠuŠ(ß:E´/EŒÃ!ˆÆ°n  f—TÂ·è!K.Ó@ÆBn­!‡W [‡÷ ·)>Èàƒ>Èà7N|¬câò·'rèf²&‰ïo$îùh gúÈQş} ä€HQ©3ù±¬x3$øÍûÉ¼S¢ı¹Ş2I6ñâ	ï¾Xg8äí¦uRŠÏdOÒ³yUæÑ‰"Å•¹ÆIŸİ3¯O”=›É²¥Ø(aG™j=™‡0nÜ!¢DÆ*2)ÅÈN•éç:6¬QÎn¨Xîû„†M«ÊùmRÁRX(‘¾‰rÈT-›ì)Sâ“ÇÌEtd,XÃİGÃKºX¸[NPöZ·±œ/¾yÄk(‘øWd—8¯ÅG$Ç˜QÜSø7ŸGŒ	ªÑ~€Râ%R®*
á¤33ÑY"Á	£2]¹)'£·¡\9ˆ³¦dg$™˜RÊ$ƒ‰ m³“`l{ºß+6”#,S$5'Rt›'«À4†ÒÙrç$‰Är^ÜĞGÍä
6,‚)ÊÙ³}’óSĞT÷k_Îoó+ˆ ´A‰R›Òu¿RDOß$+G6Sï`İ©Ç|¡Ân8AI¢ab8¿;¦›¾Ñ%^DÅ+1Ôãë‘¦/âaŠ`æş]VR-šVLn¤Jûš¦İÔÀæÊÖ
­ƒÍe¥¼§¿f´~ıö´q›[ıÓ;O4#½=r?>_¸²~šEØ@3ĞÅÈ3­Ñı×ëŠIÓİ½JÌ®½İqŸ™çwŸY;úk›¦¬q<A[škŠ*§Ôú¯ùRkVŞ8‹İêhôİñtu bˆ.É.Ò¿É„Å v¬`×¸>n¨Ú¹¯Õˆ¬U1.vUC÷¥âå¸ÏMëfqLc9÷ÚïÎ4§²CsO5';/²”c¿òü'8İyªC<W"“iîs‘ëİ·/Q‹àÛ&û4TtLcÅÁ¥³yúşLLÛØ:…Q\ÎóS³ì×:µòg¤]œ›-e²Ÿ§~™–x×‘"i§‡í¦e]~‚èUÏDóº:ËÕÔjÙYÙİ{¾¿ ‚uÁlŸËXrŸåíGœD:+ğŸwÕ«¥§úŞi&W‡¸ŸkŞ¸t‚6^_Ï7ÒØÓøÏº/ùé¦©%‹ÀÁ%q_@
·¤-¨*ì˜üNa©L9WX­åJ\Rê¦ğÈDCœûÄ§¹Ş@üÂ®+ºæmU‚Äµˆv§*:?v<åş}×ÆŠŠ©áû^g\g¸\e¾Š¿8á»ßNa`*7®Àí<í)×“¯ë“ÚÓ4ã¹Ò”8rg]]Jë¯^E8™ yåpg@ı©æG{:ç•z÷z$uE‹	qöEtù|G.{«ûÁ©÷Q€¯d¿kÔPÜZ4‡;Uâ€^›ˆˆrÚ›>4…÷Åt\ØØÙŠf¾^’hÆt‚v¹>àµYíBğø]ºŸÏÊğ=éøAüà¾Ögü6­-İ ;ù¡æUÁ*ªDWéñC½¨¸¼Ÿµ<dæ¾à]&í\
AìO½m1Òµ,¾B‰ã3Ú“p›Á¹àE(×Ôö–WÈå`Ù#a‡ı–ÜÏÍ.Ğøws›Lp¯0_»úot­~ãQcÚ	s?iÉ÷¬^½bêÉ×ÌÑ÷‡™ææ±Ÿf/ß^ĞY×%Ãi{A+Xk•ue‚íF×•`ƒ@½%•|†µjÕF¾6aÚbĞ*P„˜ì1ØW-e©@Üe · –µz˜L–õ'Ád ”­PwaqZàaÇïÊ»CÉØlĞü`emB©²!†QO›„:Jšº±Ğ5Í¦La³¡ciÚl7ä|ğÊ˜¯‡ìCÇkQµßlĞ)Ûq€ÒåWV÷VdG§xÜn *ÜŒâgº`¿AÑ°6¦¶É×7TÖd4í8¨±[
vl`ÏAÁ–l:À²ë sÉ¶Ã$•ì;€²ñ ºÊÎƒØ·Äˆ¸õ@(ñ2‘l=–xMÔ¢TÄy[Ûlñ‰)K´=3İbëÒü$&î<Š;pşğˆL#¾yÄË"8ÆNWğJ<ıºÜĞ+«Ğîî\«EÏ¸sHašnÊEµİÈ…d\vœ9ûU½½“	n/ò¿BŞËhå¿Ì¨¿Ü(±u ‹mêš)uO–ÛŒwe‚¢´M•1E7X«–Îğ|Şß%ëyŞ´¿í¶ªü·ß:™ÓîR‹7ëvj÷©/ƒ¶ÊıöxY`ûvP¬ZyøíhE«wx¿wÆ>¬U‹z7c\Ö¡¯yü¹ ·:N.W{î+aYLğ[ÉÈ—°–Ã8õ]¢Úğ€¨W]"ï¿u«ndE¹Ktïı(Qü«ÇÜRa,0¢@w)İ#ar”"2W¹_è.òc;N›·&~™â|âGñß„øgáÇî²ÃDz=ÙÛpmÆ«lûò»'MÓİ®0ˆÔôêÓ;ÃÌê«yuR¸Iï	ÌT–ÙÏˆ´)&Ef5İ‰á´Ø)t­ÙôOgìÏó&œ²åB CßŠæ®½3î¯è÷Ôp!‡ºîÏ1cïjée}!m}F¶97<úÇĞú3œ¾£1±ÆEulÈï•ÿc¦˜§õh­ÿ…ûïËt–û2´Ã]vKé½bÌø.	‘®Ü¸›c†ã^’wÜ}2z¿ëä}¯ñšyµÙ/€{Xb¯5//ºÃBw+&y5×g~sÙñ[´&G½Û(ğ™7)Újı¯†ÒüPAÊŞÀ:~ìòÚ²3wŒu0·Ï]?ïtfÓİ¡ù±µ×„\îÊ«R¼üxrüôKæç'Rp`ÌeÓÚ<aÉÅè}ÃbàfsÇKwÏa4m¼¯HXPšà†sÚ­F_êÙÆ„P_Á«Ó¹œ­´â¿ŠEGòğtŞúÔ°äxEPª6È»ÍÎó‘†÷gFz¹:?âˆÃ­‹ÉâÏasDìG	|{¬çó[N”ˆ%£øŠÖêŒPˆóü¬+¹#'ã5Z…n“™¦<ZªLo¸ız²3e¤W±©Ò<âÑeíK9¶|dU/óy¬i\fõA§YÖ´ˆ"MåøK¨gƒø4™ÍÅÃ/v-bT§ˆX^n…@?ùîB_½.‡(h§Oñ2æ™"«
4`“{
Õ¡áÔÍSğ7›MiÒ;åSóÂ”wÕYyøŸì;öë½%”G“Zj€ÊÿÉÆàØÅ4ÖælıJ˜$İ-G³#L»%£s69šÁõ¼Ê™wÒÊâ§±¸`ÚñRÙÈÙ˜›S*Ñ˜—¼G¦ˆ{ºÜÏ}<Ôç#¡Ô«Ñ~’ãSÚæ1o¼Ëİb}=2â›…:rø¡Õût“Ó=Ş8”õ0NôßÑäm…ÂSmGzƒÍÛe0’iò»Báp¨7‰ªÒö=ÕM.ïè‡`3?n¸TqS&fÒåºÇq¨ÃÉ'ë&ëCªW¯‡!o7¿\¨›ÆôÄø/mnK‰æ Ò#STÿ¹t¸Gœl…Æ=´Õ¡Õ"÷r'Í}‚"ñ05³#¶ìdİ¬î8ãØT‡Ar8Ç¡1g³ŞuıŸL‚^š*oæÒ<ğ{ì—Òœ±µ4gl_šÍn*Í#±§z‡±ò:F®•9ckeÎXyBK2×Â¼`½0Z/…ùøYêÂ1
2šC.(H‡üPºŠ¢Pã‹@-<,E3ØÊëáîj_zY¸×a.ËZËrÆveyPÄkÉMe9cüğú¤›âÇ~ÍR–3º–åŒ-e9CºŞî€ù	\ËrÂšU\ÊòúÄ@?ƒEæÁ°jaôu¹1LECènün³)EÒ¾,^˜r.²¼úğFY´—2vµÕtÍæ·\½f‡|G‰ñk–/êğná¨{ŸŠ¯+\»î¼±ò½-6Q&âk~T;O}pBkY}ä"Ğ/PâPØC_zïáÿWMš£bóñrè°êy»ˆäß±XGÕ´·GzH$×À‡eÚ-"éûW;äË€ëÛ¦7tCÆ…£{ïÇ/-Ü,‡›h×ÿ¯“ÖÛøaYåryÎøá„qÛ[ §qãT}ÄÔ2N(¿(¨´¬ö.bÂøÿ<Àè7&Ìm™Ëì'Ôr©—¡]¼`¥§TzÃfqA±W\Pé´–y¤'%’îm‘]º¼EÇ	kÖÀ.q±Ü÷åškê'ŒÒBqTlÎÄ©IÜª¤¶à¦&qÂ4%+;ŒÑ±¹I\Pl—óÅ28ïŠä¢áµ(Ú÷ˆ[ÊÎa‚AºaZ^Ø¡CÜ+ùÅ.ĞcLPyŒÃöpw/¤)X™[º›ÃæpA±7Î½Õ0ÏhÂíÚ"ùèêGÿ·˜»ÂÅlØN¨!1B„®pÂÜ–Tp aÄvî
'jæ0u…Öb[l!v…Š]áp~wL3<†òÏ‚à-]Á+ô+w…G5^Ôòf]á2ÇµˆÉ¦½Ãç]‹Ø+vË±9LæºİwàÜÖÛ®ÙàY¿˜ë}œCÓÚ5d¦S›µ2Ò€ˆÚœĞ"ãOÏÜöÏ©5àrëA<µy+ÍëûÀT	;+üV-„ü²¢Ş$ÓİncŞ=öÊ³1éZsß$FÙ¿£‰DæŞ?U}F´bÃÊ¢çk_¶ £š…×à…iimlíî%jZï²k„—ß§0®­ç¼¨ß$¾ZâÖ[6èÒ»)íkôƒï
¬ğXËtLæ½È1½IçôLé:¨‘ÓÕWß‘c­rSïŞ«IZZAñ7#I~ÃU}ILw›$ËÚë5Ç<–I]o±¾ò(ÃÕ7C¼–g‚.º§ƒ,núÛµèÆ4ûû/½t‚ë5 ÎzoŠår¹=ê"ß$›`ÇÃ=hõ»¼4Ş0qçñö½ge¦·#Ôæ-ÈFÆ¿—lÊe®_Şà½<¥I´wóÿTïı5O#%käu/` ·"%¹¾Êd7)	¯¯×œølûç{˜ß•˜|z´ê/»ı´`q-Q>ŸEFã-R äM*²Iüâ÷½Ôïù^+ëÀYæë¾œhˆpÏ¢õÃû-ÇÛ‡;Gsÿ?^µş_À*Ü°
endstream
endobj
81 0 obj
<</Filter /FlateDecode
/Length 4126>> stream
xœí\Ûä¶}ï¯Ğs Ë¼“vfvüœx€|À&vÌ°óÿ@ªx«¢ÔiVÓâÙu¯[§y©»È#vÏÆBş3)üûİ,.“Ó3h€4}ùzúõDŸ—Ôd½‚é·şş§éÄİ¬6e„ñ
;ê‰şşí‡©¼ùíçÓ÷?Øéçÿäñ"ØIkch¸Ÿ2¢¨iyƒM^Nß?»	¦—Ÿp ,¡lœcÒÆOÆN/_OVÊú¿L/ÿ>üüå&-·bb¬Ê@º<†Ö°ğ¥tÀ•A?¿œí6¢\‡å$f1ÉºÅR•u—¥9´]Z\’Ü$=%´ø%¡ÓõŞèeî­ìRÜ¥üêº0V)L\
ÓğWüûëIë0úã&ı¬ÏdŒÇ@6ÚÏGâ`¶3MTŞ‰ÎßiÚ‡Ù8s;®f‚ƒ¨J`Ïq,ù/ö[ƒ8†Q³ÇCA§¯õÂÓÓ+]8JÌ”5“HÔ XguÅ¬ËX ez;eaúB½“:äñ,ÌÑRC ²EA\@«hÌclÃ0L±«ÆÏBí™°¡vÑFôSÅ’ÆáÌ¬œ5	*R¢Î…[K—Z¬15ŒÒ¡½ır
ûÕ+]ÍÖjÇ		Ôâ!	Bë@ç‘Òl‚'Ä$Ì[ü#Ô!,†ƒT; `¬í„}ÓÉ$6"!VA€ÁÚ„:¼~ÉúÏ	ÿÖ<\z5ç¿D{BĞfãf, Y„ß¤/’"È
“P(cŞj©yÆbÕnÕFˆÆIØ‘®q`iğ¡ÅuÍ5uÖMÂƒ0eç+r¸±ıâõ$‚£7AÔ‡á&Ù$åğÍºˆs.tÓˆŒé&¹%l-²°{Edk÷Èí/§QYHSùªA{Ÿ	:	+ÉG1ø(ÅàQ~Ü±F¨ëŒ:‚Ç¥F«Tª"]IV‡ŒÙ"W×€°UuğÆP`;Q2äğCi;Âå1Ê§ ËCÆ’ƒ¿[•‡Œ.ÊCÁry¨oky¨WCy¨˜ŒÁ6¤ŒV\†uS†~SG&IW[fS³HºfE™lo™ÇÍ32ß›[E “s} ÷õ‘m;ÔÂ–õ0´öX<¹Õ§¡>æMT'l]PÓ¡>àõ²>d•_ÔB—õ0_«Cy_«C¹«CÁdµ!e¬ñä2*«”"vIß¬­H„f™/Í|2³ØÎ2›Gd®6Ï‰ÌŞµPø(¥à£ü?—‚7/‚ŠkƒGÇµÁÓReQ[ÖÂÖµÁG7n"2²ØDdlYĞAËMDÆ›ˆŒ­K¡ËÒ±RÊÛVÊÕX
6„_rÔ>ùÑUÌ!ê«:C~4µ‡Dªö‘ùVŒ8äe·öÁÕ/C¦WÿõZW†ìü¡2²¬ÎK	2¶ÜD è—•!c‹Ê±UeÈh+ŸÕ–ˆ…×ÕÒê[•‡Œ.ÊCÁÚN"_µQ/†Ñ›‹HêÃŠ˜ˆèì¢rwD°İ9+º‘DîtcŠ,VùØı#ò¶ûQdù%ÃGYø(eáS~Ü÷Hdúå„®h”8üÀÒƒ ¯µ8zãıµ£è94«`ôD(Ó'6&‹˜›µ1´°‚‚µ@ÒéDák¨8`¨8«TÀ–-âéYšµÍóè„1ãhnÆ(ıÓt(¹ĞÏÙ-Eƒ	”ó FOæájMjµ”1¡€ó°ëÖÈ½+Ê–{PŒTŸâÄÓÄ€›KÏNY qs€kI(JVÑcÄ˜Š9>ºŠ„¥dÈXİK:¸QrZ31÷gWğ<ì4)»—eç0è*‹"ŠGŠ0£è‘q Ïˆ­Æ(Ml«°ÅÜKÙ¥0€“
e,k	åF,Ì –/âı¢·!ß"Tv¸Î1”haL(“ŒLm«™#Ó(&e”â+b±HjL#Ì=FÓ*#½9ˆc"V:¯Üà[MåC(X±(L‘{W”Íözâş¨èlŒ&²Ï§@£JÓ%Š.b¹%æ1«èÑa	ãrËªbôŠTÌñÕŒQ±"Q7£(Q7±èß!¦éê¾¢‹xé*‰¡_{éâÍË>•ÿ	“;•ÅÓã­U~:­q@7<ŸvtçUº= v ”÷ø2ıÄÀç—ÓLO±Ë?TÜi¢i§Öã96úa…UÄ|Æ¾pFçÊ¬ü,}«rfÕo{ èŞ0h÷HZáËVIÓx€–T˜"Ğúê¶šÃqõPÆbH)«íb¨İŠñî¿lÿ–,ãúvÄ|=WU½°^
ÃBvCÂÍÒW¯ÆåaWàå‘ñÖÂaĞ' ŸäPĞøÿTq»ì/¼×*œ×ÓjSS‡Bf,Á+A=ËÚ>\È…Ç,küè>ıt+ú‚É³<r5J¢Ï¯ƒ"QV’>“‹Å…Èber/æ80µ¦ÅÙbü\|Éö>•JEÑàŒøü‰>;,$1wÍİ¬ğCÍ‰T“
G\õ2Ù§»”´N¸ì•«1	úlL®_ƒ4İÈ]éâ^ï ú®¯ø;è9¨µ,Îcox]Ù¥×+¦ùsw¥É¶¹j×vÊàHÜ‰ÌÎ×RÆj=Şr	ep+klò¤Öj_{wªF<ÓûU#©Í{T#S5
å³¬k-÷T?®ùƒíÜ§ÒŞ=‰bâ«^–ÈŠ•ïV½,î/ËR‚'»Y»p72ã2.WØsN¼Â.m*^G-š1h}RTìs¯ãÁíí¹¹²>ß\t£­Õ6„¨˜½Z:¾äÕWøÕÒâÏa ¦Q¬[Õ­3§µ…îr`Xn×÷c²/î‹[€”}"J‹&ï51/¹Ngœ¨’‰Šîy`ŸR/ÇÖÓ¬¬‡àWÇÙ) 1îmkï Ó ıƒÇ7Ùi`q_oçècXDÓGùD
`‹ˆ÷‡ÙY%!¸35ÚÚ4°ˆ`qî‹ ,"c’EdT²ˆŒ2Çó0i'%bzegu˜à0eË½¨Ÿ]²AĞˆˆ¢Ë¥Dˆ¥YÇ¨QÀÅj¡«hÁÂÓ±ai •4"÷g_ğ<ì5)û—eç8`ÏÅÑšGÔI§cŒ‚daj‰Ù/xD¼]Î	·‚•OÏ4leî+}…Ù<"P¾û‘GdLòˆŒJQôïdOÓY»AœÎï	Á;(ìŒ!V²‹Íl’GD“kôb‚GDuó…[lÌf2èíÔ˜ÍF&1 £<"=-"2>
±aià•<¢èß	]†™_)sÄ,ºˆ—®â™úyDîÁ#ò,÷å…v÷ào©¹ƒG”CÉšäîáï>K3ÄvòîÈXôPü½BÁà}„¨ƒô¸µÈô®-2å,[¶'Víã­éŒWİf)ëñ¬ïP#u%Ï6,£-LëŒEØ(²ÛGRØ vª¨õÆ-·Îv[U¦o<X´ªDx/U¾‰=Ø¨ºÅ¥DjÖc£Ş°Şj]kOÛëvº”«[£~WµÛdKû¥r—añ7ª‹+Û]í½?Ø<›ÃlIn29¸Bˆ³èUî÷Rõ-ÅaP5î+ıìï¥ê=Š‡¤·YÕÿêÅóãØXé\-@ÔüõQœqcÑ
Â¤PÓÎ¿€÷:”)HŸˆ›bÑÃ´‘~0-~V`HöBºxÁı´Âı8ZêöPõËş8ö0üû—	'¨C)T/€˜ã"wÕæğ
 ‚¹İã­ä‘hÚ¸ú±¼µY ×eÍ;Âä!	5.ö¨4+î}-öP¬Fı}Š4'4NØ¢ßĞ_r­ix€°AÜú›0Ü‡h¶L~ÑƒûC4§%‡x#BéŒXtR:ï¨èôíõÇ?`Ò\ô¤õÉ.cºäx®z$1Çä âm©¶Ùp˜cSšÃ¦¡.™}[š{w!H’ù#Í19#VP'’ó ÊÙúÚr œb¶‹©FDQt± œó³÷)Èƒ«J»×|v<¸ª4Ş‰ÊÈ~pUay•	ë~pµcÃÁÕW;*®öyÄÁU!SÁ,;SÆ¬ã€uºKgí–{Ñ0G;PÎˆaªà…Dˆn•âÀ8[\¤ài`œ£¯JÅ ç†Œ3£’qæşì
‡&Ç’»äâør×ğ\­	g\>¨aŒâ;&ì%ªé'’’ œ¢§ ´ /‹(wò’pFĞÇ!gÄÊC	Á83&gF%ã,úwÚVÌÓ	ŞA NÑ;e,Tìä2CRÎl8I9Ó×İPàåŒ˜Ã»ç@9#†ÕÀ†8PÎˆ¦Ù…håŒAPÎ)gF%å,ú7WˆiºÏºw…è2bšŠg¢èM”óZlİú‘w9¼ƒéí*õË3ÑfD×ã5í¸Ç°WiGmêŞÆµ-™­{W÷$uOÒê„²'Êí‘Š&ytÔÑNŒnnéäCİ*†çpÂù“%ïá$>^ÑÎWÕ'şdÌlXyr5V'|®0Å¡ÍÍè„ùæ°ºÑTÏÜG:)o@Û\Ôş¡¼×G»ÂÜ~¥îÍılşJP!|ÂÎC(áÌÑƒ«íC¼—¿ûL9)Ş”Ï|N}bßõDŒ"fôÚ¯9¡Ÿ+ÁĞUåkåç¥7MñÑ5ìcöB
÷r\Ÿ‰¬ÕıYÌ
‚AjÕö‘“RægáĞÍ‰ùé¨ªJÇ¼Z†±z7+®ëyHÑk“»¢ÚÇNFãîä^)çå§·çevc%û|«ÍÏìŞ~r«‘O<nnˆkÅÍO¨vÛµôCzi‘m¾rö^¾ê3å{f#l“ê´y&_Ÿ…m[¬‹”Œ×˜Ÿ@ìMA8za#tÚ³°İ¶9)ì{–H»ÿ;95ÉƒæÙÀoMÀXƒÁW‡'ál½XZñÙaÉ×š6Ÿ2œšö=ÀEÙïä$‰œdÚ­>i1ä)™AÃ²İ?«·İÓ;Ü…z;n‚¢×6wé}‹Ùd/Ÿj>Ø½V?Öé9Ø6"µg—ªÚOäÕ—B8›†Ç»×n?Æ,Ük÷í%’¿×^‚gÊ÷AUïmr!ö‡ÃÈ4fáîì;¬TºĞíì7ïòùŸü+ C·mî‰û–¬	ü½ÜÙgÊÙ7fßòî¢M»óákò{82Óè€F];
Unú’" ÷İ6ùô½¶<S¿ñµ¥ä§uËã¸ì©¶LËvS”çŞš–á¨m<}çÍ—s|Bõ›;yúe…¹¶9Òî[Æ‚?û=Ô÷p|Ÿ)'excR¶dsjü®£„V…C=°v=¸&W%?'ÔİÃÏ‰nÛüïµ­à™zâ‚Ø>ª~ 'û5Ti$ÿ*—8‰÷¾
º”¤½¿XòèÃ¾Eë“zØG¨x³ØBèßeİ¶ùÖË\zfü_|
endstream
endobj
83 0 obj
<</Filter /FlateDecode
/Length 3793>> stream
xœí[ÛnÇ}ß¯˜ç j÷ıDRòsbù 9vPìü?ª¾UuÏw–ÊDÉ”wÎÎtİOWw…6)ÿY$üı Øe´J$•R\¾|½ü~Áïµr1N¦å]şù—å7À­Pne„ñ
TşıÇKùğÇ¯—~4Ë¯ÿÍã…d¥´Æá~ÉˆÄ[Ë¸õîñòÃg»¤åñ(k¨DˆJ»E›åñëå¯R÷·åñ?ß?ş¼  ãØ02q¥2`:àÊ#©¶úéq[qğ›Ğ*¦¹ò³=	Yß1›²~dv‡23°sÇæ:ª%‚Ç÷”NÏ?Q¦§¥™Õõ—Ï+c¤æÊ„Y™„¿Ãßß/Jyáñ]TpBJHEk‰¬•F¢d6•Oìá¨&(}¸×*Á¦ Kb‹`,ş/<·a-…[Œ—Á._ë…sÁ/Oxa±0cF@o¼ÁkTÅŒÍ˜OR÷û¤IË|:ª |ÏŠ`ğÆ”Ğ±¼¢ şµ6ƒ4…G|çë“Ñx_0âT±¨`8-¤5:¦ŠùñaJ%¸®(¨‹w‚ò6Ä†a9´_.>…~õ„WÂeéfD¼C³hHÄ’ó>Â}ŠB{,S1gà3±à¸™™íS‚\ÑÊ2ÿ ¦¢äDDŒL>ŞFÔï4‹KÆ ~–Å±áòTşÓ…İˆ ×.lÜŒyë¸K®i_4Ğ	íÊÃÕ Œ9¸åŞW¿Ue4%¿0_æ…
{=cFÖøµødÔ»°(,ØÃ§´éO–!ıv–I}X–sL–]UJânKvf;UEw«îLVeÌë¬{|Xİö8²*ÿrù7D\ÊÈís¦pÊ;-¼ÓÂ;-|g´ğÓ}Cí=êÊ¹Î^&;ò P
ĞÑzf¬- lÅ€ê‘'22ñDÆ& L5S$ ‹Ê1lÅx¢`‹î_7¨WOTlÈÃ:ä±]øÛUÍ¡ª9Cµ4³‡²ªşáÕWœ8Ti÷öPÏ5.Cİ×øufH–ñä	@V<ØÌˆ­xB9¿â	Äf@lÍˆÎ<¡\Xñbk@tæ‰ŒuÀ«Îåbä‰v;Ï¤6,Ï9R€ggS•%q³ˆ';ÙÎª¢9‰×Ns&¯2ò:¯Ç^·-¬ÊojŞiáŞiá{¡…—¶ÖZ©ˆ'TpO(laÆeFÆ¦eFÆÖ<¡ »y‘™'›yB½â	Äf@lÍˆÎ<‘±Âåcã‰r5òDÁ†<¬CÛ…¹]Õj š3TK3{(«ê^}Å‰C•voõ\ã2Ô}_g†à:O”àsÈä—e<Q°‘'
6ñ‚À|Î2(ØÈ›y¢ #O f&(ØÌy¢b•'ÊUå‰vÁy‚n§L¢a)ç¸”¤jOb²ˆ’ÛŞ«‚œDµCÎ¤*ã^§z¤øPİRY•ßĞ>¼ÓÂ;-¼ÓÂ÷C?İv|²üvĞ
”Çı2ÄC£¯ı Tòx|¢¸³áù`c›ğ\Ñ$UDTK)¤÷Pp-”†?Eï5h©"n¢i(ÄÁ1Ò'¼¤@‹æ2
®V(QEa‹„"$+BRaÀ1Ü ¬Ã0qPH¯$İ P<Ù“iÒO0<?Z¨‚ÉÉòm~ÊcTœ¼úÄQ¯„’x(EÒŒÍ"ø’if¼Q¢³ÍÕ
¨[ öİ^Ä¼Ñ!cÕ7‹*{½y’PŒgó:=Oñ!9K®Åt§!·r³óOK<|öø±=ÿı€!ìù7âVXq€" =£J9+f¾óX.ĞÜ+ítF#–~ñ£¦ÂÊ8J¨" <p6ùŞ¹`5æ2=ûÅHøÔ²pÌ>˜L”vEƒ¢ü4Ô¸í©sòÊA€”MÑ!¡İn4»¢apR£âäÒ§a8&³I3Y^e&lšÙ
imÊ˜ÕH­ÎWk§Dp!ç^óLÅr¤É„‚Bİçìù’Ò£8¨Ó#Îg™ÔÜÈ®–y·œ,öò25¶\#BË±|ú­`0;œÛ¼Ø‡i´€;({ç¤´÷ğ?0ËÈ»v.,ú |–Ê«Ãu{Ãb-êŞJäv.I:|û ÏçñUø‰L:~öU‹ÿ‡û,\ËÏå~§§{Ê=¨qï¡àùs³F£ÌnÉÇíXc,„Éšûá-ƒ§œf3>f®<VÂcÃ·
O—„á1ºHÉá©¡Êa‰,ÕÕù¾3İ¬u$‡‘Z×üÕQ_‹3/zcèC¼Â:L}P©ˆ±ÍZmÊù˜XbU„®‡f-˜s¡k3&ıPp4LÊ¬û°ªÍ4cÆ;ByßA(Í×$‡fv®õ ¤;õ
d#Çš7x¯A{P<5¼Õğ d>$¦49"éŞ^UÕ=(¤lZÄ®k5*6µ„òVƒ§P
×ˆÂKºSt·²hİi¸z†joZ†q†N&EÖeX˜œ$ÌNÍNP·0“šÚù×YÌ˜Ùq]@s0Z•M³"a¼· ”wìù>%“˜>wêôY)Ş»f`ïÈ¼› ·ñn4°hôšu.¶Òİ„ƒTQÆ§¡™pÉ‰äğYèRÓ«ù¢bS7A(ï&Øó-LL×§G–)NÙBndĞ‹º	ç@.,ğ@¡<k _ÏØ±BÑçë´¥Ët•çiCóõ<Wãô†÷â¤“ŸÉóÿëé[{ƒ­/T2§oßçôíq‹Ï—ı$c˜ À27Æ‰¾=d‡"ˆŒ¾a±_‡±'nbŒå‰›·u”q`—ÃØ’iÄxµëÎè·ÛÈ±æNßä¹§	ßDÍø±¼
`!!	~àoDÁ7e¹[mDÓ×3şnXø›PÎßô<Å‚äPÔ¸F_Òò€lÜÊ£5Ãwõğ…xÀÅzã§â†L«‘¸> NRœ<Î…8ğ·Ç3E9{`ƒ:¿w"Œó7¡œ¿ÙóILgK®M§U¦v§_f^'jr§or§oD¡´Ñ7`°va
!K²şF2HqşF{ Ãø›0Îß„rşfÏ·801=^ƒB=²Lõ![ª‰ô'8ú–ÉÙ$"ë¼
ÀEÙgNÎ¯èöaı,ğÌ9÷íLö¡õ‘ŞXO	g‚YpCu±¸bÂöõ)ãöõC^ÙH6‘á$N°›­½4[­ÔU¥õW–*¯xC9àtiÔj¼C^„ô»éşØŞš·m‰şP2õÇe ‹ÆËV¦
7­“/«9’'­‚[Fâö@[ƒÚOøû¥İpwu•|ÎšTR¸¢»É](è-’Ôô_ÿh»(6`*0dÏ$ÁT×¨[£ÚæÑWà¾€p¯:Œã»É\oe•Ş¸íÛĞGC; ß K*_^O˜ÁgrúÌµ8|Ç÷^“:xğ³²W=\ÛÎP
úXHí„áÙÌ°š
ı¼²(yàH‚k?×(Š—4×ğEĞÑmYT&§F™ÖÓvU îË„•é m]5ÊªßgŠmôqÇ(x•p…Z²ÌïÛ6Y—ªfÜFËú°Í<û‘íp*¶Rº§	7ãm\9Úpuz€må®<äú([ú"²/Îî›*7…¾wP~º­'€Şs/UšûÚ¦qb)¢ª]ÂÖv:1EÚfµk›Î÷cHætë¡ÚK¾¡XÚ¦*C•Ù¬İoX
Éq6cl¡İË¡ÙZú^K¿Ü£Ä½xÈë&ìx}M¯éy&q™‡tt~GÇ7Ù]Wùe
&Ô•œ§¹şyOd7u3<PÊğ&¬¥‰üø‚fécÁÚÏ)As
—×&oè3w\ÛĞwOÜ
iñĞ
upÏÏ€×K×gB&É³’%®·/z+µÃ3ºvÂqÈyÉîÕÉ¦ÑZ@öc»v^„ÍÕêşÏ'´(:QºtfD­ùñŒ3@¥ûáqõßÈiá`î=§Ì7Êe&ÉOÓš’Ã4Ôòv·›1%ÈXó4ºÑŞïÉèTÜªÂUM°-Nİzn>#~®ÛÊ÷~ª×úÚÔénªêÉÇlZ3Üi:jÏ…á”Ê°w@ºÔİí5æ»:Ï¼p”*•ìÇş“Œ8/ÚöjÑD	“×{\ıCæù­j‘$ÍµèYí.ÙÜ²ñÜµş"×îÆ÷¼ÕÜã”¤´ù7¤7“Ó)¦k9yĞ…<Ww©PÕñø=áh.æ75Ë*Ÿ«}ÄLÜáøæí,êxyÕ³Ÿ‰ùÌÜÏÛ‡[CÙ]¯ôC¦årfŞx.‹¶ö·Úšó´F„öæ„©v-	mL½9áIu(	õöºï¤NFˆ$©¿üÕÖãè{uF–Lº-Ï¼£$ËJˆ‹9äi»^½rº)ãúy³eò^nÛöB¦}‰6QôYşæ½İR¹`/äï2vÈ_ÑÎ³MZ<ÉŞ«E†:97ØgètP¶Ö¯l(^ÓC3bÑÕªWøéùià¬Ó `Ì8ªz¨Œƒ_73gœ…Ğº‡7;"osÄL¨Û[Ö±uÁ78	Â÷Şë)3öOK³ä{§Aê\=92ÒnYq,;ÓvOyŞÉ“ğ¢“#®á‹¢ÚÛ˜ŞÚØ‹µ<c=µ·Wru‘T_qs™onÛ8n{ã˜ÿÈÉÄÎa\?9Š„çmE[9{ËÍa«{ç”åÔ&ÍI(»R>Ü‡¼övNßî„Ë<¤cº¶xVÇN’Ş¸cMÚ~¦¶”˜ wµm»¯×ñµ¿W·ŞôÅ=WñH”’ZïÃÑí'3wV}®µ²¿†Ûİ÷Œ†½‘›æë7rw±ÏÍÛf»ãKí>ejgÇ3Låc©á7Ú°3R#Æ95>1:`îœ?m#£íüççêÂíêË(î“lÜùÿø9ãÔ¬erS„;H½Áñeøÿn¶
endstream
endobj
85 0 obj
<</Filter /FlateDecode
/Length 3049>> stream
xœí\mÜ¸ş>¿ÂŸÄ§÷ 8 ›İ½ÏmèH{W6îúÿ’’hQk¬ÉÚ{8$›Ìf†c‰/zH‘”Yé˜~&>Ììc0r2Æ0}şrùí‚ß+Ä¤­ˆÓïÿ¾üó/ÓnféàRŸgh?Á@9áŸ¿ÿ4å7¿ÿrùá'=ıò¿4Ÿz’R)œîçDxi~—>¼\~x6Sœ^~†‰’„rÒ~öA*;)=½|¹üUmœ^~½8øşå_TXÌšàÁ/-!ôç2ôB°yH\&Oúô²-8ØmV2x&¹tk&jÅäúŠµ*×CÖæzMè\Ñ“\9°xOè·GÃ*×ÑB¯Å]Ë/n£…âÂøµ0Ë"üşüv‘ÒÍÌ$½… ğLJY ²’vv0S³XÈ(¿cƒ?Himğ³‰j×
<ÁD/2°çèa.şÆ]a%f#Ó—üA;zzÅ3$Š©Â„8m´,4mÍE¡–ë„Óg¤—.Ï§g¯ñÂÑ™bXE‚ÿ+¥‰0…¡¾se¤‚1¯óÚÃ:Z@S³0Z…Xh.¬@¨h=]	ââ• ¼ñhèôöóÅE¿|zÅO³ÖÒÔ‹‘â,ªU§DZ´Îù†¹‹aVNEÃÄDšÕğÃÔAšwŞ;®¶‹°¢¤aöAš*T#"E‹èbcm¤í¬bë’h°~†­Òh…ó(Zü×K½>Qf­ÌTçÍ4g,“ Ó¢%é“¤HT³²ypV(Ó¬òLóLóÎ»ee*Ù(ÛiàŞ1«gšeıÊúdªÑfª«XhiF‡£”^>¼^*BêåIuÚŠ9.@EguqÕ¨‚ë¾xE5RõjÌêeÜêÕëúT¿­ëÈ¼üóå? Â”ÿb\ ÷)¤ÀrALù¾‡…ïaáÿ¸/ü–vVQ‚Ä ¿ƒ¯`­¾0ê$€ƒ5‰lÍ¹8Ğ¢!Ó4º†"$õ
~ĞÉ$2X£ ÿHv ¿‡D(8d¸™œÇ	 8†(DÑÌ>JÏÉ¸ÊÑÍW‡‘ ŠÂrf@Ä„ª‘F0¥`Å• ¢TfYÛ–V“ÆrµâëŠ
¸µø8!-ÌA3™€äÅ,¬Ìªñ‘
ËÒ=3-¤U%“M'K“ı*×L]Ç×5©|êòq‰êJ/¢W@T·…ØD´)ÅËß¡ùÚ*ŒŠğÌhkÉ4„ÅM	-È˜V
=2l :(;ás"{±èD“Ğ‡
âø*¸¥UAb„rˆº¢-UF›‹ÚˆŒhƒh¯ƒ0Í
"±ó4Ì”w³QmL.åA+U£ƒòÕµ¶…è¹eÒ…\Íøz©3 6…è VH³3Bx
Ibq±ˆDïI£¢&,€@`è$‹-mÍ‹ù*ÄY,ÍÆÓŠT.ËÒqi–E®R7È)Êm ‰vO]6[›\ãá·‰)¥ZÓjµ–*L	š¦Æ4°{PjV‡U)üPäÃ{ó	ªØK Vó˜¿3Ï…îòw6dºµ™×6>}G×Ä<Ws-Îmó¼tİšGºFõx4UtOGˆ?­æ©Ìÿ 3Í2™‘·¨ßÑ{ó±Ê—èLwn¤/öûÔÑëSË7Ù€dA>¾ê*h¾Ç–/É”d0YNcÈ&3vò/Ü®$-…ºO×v³«Ãü²1Ÿ2w¤¾Å}K™UCl¶`xsü¼ö [’Ğè`\Ô1Õ$W×C¾™fh$!ÛyMë[:Ï«©Y–VUŠ¬"Ä>EªVLt…²ÍáìWÄ>ï!ko¯U(+MHïiµz+¨
°	Ôªu+pGQ²Tº.¡¾Iı¦5±/;n>¹SÙç¡…[fÚZ<3¼)x™ÃUO§ˆX!ûVmu‘;˜¶:B¢.’—oáã&da¤ëùkQ%w¢Ôïn>!ªrøH¯É$3Ñ…õø1 ‘ÜÒè>@H
Ñ´Ğö 38ÀlI×-)ñb¡Ÿ‡yº–ƒ.Ñ	tfO_©™u/Lí!3EÑ3Ó|@v2ŒäÏ×¦Itİñ'2•kOoH,¡Š©?b.Ì[·Í¥bIdIHœh#Jšøª7¦*	€¥8J «É´¯c‘N	†9]Ğ™vZ4%$«Ä¨1¥kÍÜ]º–ı¹ÈÆvìç”‹Õ¹‡¬®B¹ş®`¾—ÊúÖ:mŠ¶—w@]TºoPã{>7ŒñûÏój.W³XÊ2S(+ ²%EÓ²Ìd*V ,ÀØÍÚÔ£9:qÍ‡,å\ÇR×›ÈvÛf£á<‡d¶#criÊë«U•8,í‘Ši2î"H=}‹QŒaF	÷¥ÖZ˜ÛùÄÛÒl–WTN&@Û£!Ñj³vºì i&ÜR-¥G¨åÃ¬cÎWZİ•íEÇ°µ@ƒĞQºçóg@IJYËªÊ;©|DÕ&ñ”e¥Ô¹
.!7\és‚mĞÒ¶Z½)aÜ†65Ğq¶Cˆ2ÛÅÍş«ÁÅÓ¡Q\I5™û3UXyDëGaƒ—ìfî+¡´Û.¡Nâ§Ãü.šè”½R¤¿-çeß)ó¾·ğiËp¯$Z’Ğ+×Ş!8.¼“æ%UL©¥=j{‚İÏ	E¸®ÍŞ0yÑLİ–MGÇÇn®nÜ®.Op¸…SBî’Î±†€™Òˆ«\v}BÊ8[O^ï«˜WTŞïã\×ƒ½¢N}]çáRuä¿¹¶úºd<¢Io,•y§5é+‹sšô­
i;{¨)J4âm·‘`ƒ^Ğ¦Çìò§íÏ+ØÂÍzZôx¯Ñ¡ƒ›€õÛ}†ãZôŒÃWµè¹„CÅí&Á½Å(ësıZô\í3YÙ+ˆ¿‰=WÈ\ºWí½µE¿‡02W:·ç×˜–ïÌn™r¹— Dõ4ÇcÿP¾s%Á (ïØx¾l{İYÃlBIÜtC¦¶T½,·N„"6CSRí¹š¹1Á ‚o›j¯Öf.qºJ;¨ß«µºRmøMÒºøâr–B~w5x8e¼.–ª€H@.í{)ïO\í!3…Ş‘Øy=zÎsDFLS:=úğ—ºqÄŞîgå4œÃDª{´±O±^Ó×íò¹É˜¦{ >%àJÁlï_ïVNç´Ú¤ıóÓ‘•gcíªÓaÇìô¡UçØã¨¨EÍÙaÆõÛÎ¯õ+ïƒZ¥ÎN*ñ[Á;ohõ8÷@@ÅÔY³ÂPè{¯Í"â©ô—eÛƒ¿
Ë½\”Ñ½øãNÇ*ïã›†<°U>ûmC«©ÙÈ-3dIõµ§B}¼q—ÆŞqNÂ˜p6;Ib~Ä¥´_î”ä6²™y¯¡Êé¼¶j
½­JıØu:_ãSYÓmp>ps^¿dÇTlÜ±{§[¶étª*í>1¬ù¾a ,œdIÿîeäI ×OAôn£ª9…ïÓz¨â«úœÇô8oÚI¯Ÿ¤h€Yæ$ûıé©æÇÃ’'1É†<)ØëàˆC‚à—;pÎ:$¨,Î9$hU¸	pæôøXµ«ĞŞq‡Á—™çá(ŸxÃÊ-¨T%ÛÍRŒ®	ßÖzß„`ÜNøkû3_Õöçhe/ñú&úÙ\ı!séŞƒ§÷³{Ï´=Ù³w¼ÿ½ô²M;Ô¿ÙRİ»õÜˆ¥ÇÍÍ9d~»ÜõB¦ÂmÀ^‹¾´üÙã€#ˆŞíÎòŒ½Š3(¾{ÿî,ç9$cèugOì…2¦§ôB¹RF åzá÷½œ	rømä’CFQ½ûÿ·+†#Á™Ò1¯-lI³Gc&µÀó©$D}´-I7cPÆˆ€)=|„j§éş‚ÆvC¶6;÷UÛ3N§5ãWÚ¼×-û\µnÙßÑj¨oŠ›‰¼¶ÑBÜXÛô„Ş#ã}lë}¥Ô{İ™¿Òçè;ó×ZÚˆ7lï`liş—@ÿôT¤Š
endstream
endobj
87 0 obj
<</Filter /FlateDecode
/Length 3206>> stream
xœí\YÜÆ~Ÿ_Áç ¢û> #€öò³íòäØF°
`çÿ®ê«Šrº©áF¢•F;¬é£ê«»ÉÑ¬tL?“€?fvŒœ£Œ1LŸ>_ş¸àçÊ1i+âôç?/ÿøÛôo ›Y:êó
Ë+˜('üóÓS~óço—ï~ĞÓoÿIëù¨')•Âå~MCóúğzùîÅLqzıJÊIûÙ©ì¤ôôúùò½Úş}zı×ÅÁç¯¿L@PaM0k‚OßZ$BØ_CÊDĞ`ó”Ø&/úüºÍ8à6+<ã\ºõ&jµÉõˆµ(×SÖpH½&ìŒØã\9@|é‡Û³AË4[è5»kşÅmf´Pœ¿f¦)áGøóÇEJ7;ü1“ôvŒgRÊ‚!+ig+‘1ë7ÊïØäR† €,}ß®x‚‰^dÃ£‡µø¿0ïšk(1[˜i„œ>çí€ëé/:fH\…	8m´,4mÍE¡Ú8¡ãô	gé¥ËëéÙk#b‘)Æ*ü_)]i`¦0UÂg®ÌT0Çá8¯=è©Ğ‚šš…Ñ*ÄBs!àdLEëëH`GóÆ‡JCw¨o?]\ôíê¯f­¥¡ÁHqÅ¢%‘­s~±¹‹aVNEÃØDšÕğÃÄAšwŞ;.¶‹lEIÃğAš*ˆHÑ"º¸@©F;«˜^ôg˜şV5œgUå¿]h|¢ÌZ™‰ÖÍ4g,ã Ó¢­Ü'N‘¨feóä,P¦Yå™ä™æ+¸eŒ2µb”±DxwõLÓ¢è¯è'S6i±ĞÒŠuÎRº]¼]ÈBh8Y-K6Ç ë$V›“Ddì\öæùI^ÆQ'$ıß’™—ºü"Lù/Æ…ú>…PÄ”oaá[XøşÏÂÂÏÇ
¨_@µ³Š8†²İ
 ^õƒõÖÍÊ@ÁıÖÈ&‘Ae€Eb2d"˜•Z.¡‚$:ÑIäPØ+p $Ë9	Õ|p ÌMDBB¹…ÓlMá a-ŒÑÌ02ª9ºÙ¢zØ@£°|3 bE,.SZ º`W\ J0‹¼YwI,Ğ¤
™p|[QÑšÔD[!b„à\!ÍÌT›„- Õf#h’"¶·hĞ”J	ëŠ QQ…lšOZ¡}Hœ#Ò5ñNFA2nYÚ'ZœØğ¹ü™²Åâˆ
°jY-nIÖsĞä0+È˜”¥ ,Ğ;´Ê&‹ƒ~/ø¬Xq	ı©qöC‚kZÒP6 5\"úlp.6ƒ«d48ˆø:³XBA4¶€Ïb3å —ñ¥<„A+ÕBå#ŠkÒ¢çÈ¤
™`|»Ğ
HõÀMZ l…´8Á¹,ê´ÏkŠ™*,’"2P@s­ £¥&ƒ+Tà¨ÍæW¥°mšú5M3ÖöSDÜ°©joG:´ÅüFd,­–êÙRŸ)a1³è4då ‚kë±—±BX|)xÿ//Ÿ=CÂµK…HBJ`@"(FRs¸&ÖÓk.•„|'±ŞáÌ–cÜ` ‡½¥1M	Ì0KıùnRØ!Ü›VCÇl>A¡2£kÚ>«RJŒ`2ñJ{› ¯ĞÃ÷'@"†g‡§8|ùÔÁDB„•ëYƒHB¸ş2Dë3Åú·¾‚ÈK¶Nğ»Ã‹2¹ØX24$€Ñ›œ¤zqCghÛNItÙBÉgCqDy†`¡¿éç5@¯Å—BÓ©«ñ³µPêC™i<ü˜%W´}™òºPV–u]K—àõ±üö$¢•% ©kSB:š˜~F;Ë×é·‘f®ùØ0ãtíh/ä-ñø@< îÓ8UÖ0™×&Wåù)«óöd÷a"‡ä—qKÜåJ¼tp¡ıî±÷Td&KeœYªÒá¦ß÷ı™¯0´£õ¾qWtÉëúšü’¾ëx¶PyµœE[0Öò”W³vqõ+âPh¤õ“9V“-¦‚¦jÌi5‰„*XÇà˜dÅ)Mæ`á0[¹êÆ¼uB7a+HØ1vtsÓ\âvíÓ¤ÉÊÃ œnx-®Ç´I;|¬¯^ÎÁÓŒZ¹pG$Âw»9¢OùTæ¸’˜YPÃ€*^nÔ-XQ?S5I=ÑK0¶¬Â^%¯D¯ÚôäÅ®ÙfÓåbÁ¤·+ûòF…-9é#Á—büË54‰®wrP…?ŒòÕ“ZJS¬Š‹?—U;p©XÊ6™Ek©‹—ZçPõ,¬Âe±tàcÌr¯Ó”8.ı.åGZ£”XŠ¤Ï\)?k9âØ|®¶^y`#T%$qè† öµºkÕD(l3kJ¢½Ì,ø6T>54ş&‡7âvPº(:-Ò.W~“¤.¾˜æJæwGĞàá,Pí™&ƒH†,ó:R	OLì˜ğ ô¾‚Œ¯0´£Ú.á/7»ân±zW-xM`Ş¾ŞV>(ŞÖ”¶[ù ¯xŸÕR¯Ä‚Á\×¥7Ç»İC§à4÷¸j‹N´7A´I`A¥î5ä&°%HîÆ­ôÛ>«¾UòV½îc€7‹¼aÅt¡wît+–WQ·*›&nµ¤]+Â#ÿZòsVGD³âX5bÕ^5Ò¬¨ŠÍDİÓjƒÉ‹¥åYŠ–MÓÏR$£U8·ÔÑèúú}µêæ¼Å»°[¥æ\£pP†@4Ç­u²ºÚ©XkRm¯%ézt¡–µF«[8Èİ·¦®6æ¥¼iK]ÓSD·T´ÖµR‘Ã4kèeøTè³,Ül«¾¯¿w\w!vI
õdè¦®KÄºæª~â~³àq«’x¬¬	3ŞÖ+ˆ† Çr¹“{¹|”®¬ÆQ¤mIáãˆE±du§×¤ı—&²ğFo–TC¤ÕS>'RNË8\CğjßK\šó–…7‰Ç˜#õqò’ÉKä_$ËAë[·­àğÁiÕÎïÖW',÷§òS¾çqûæ¤Û ¬Îg;Õ&¨fˆGòks³K?ãìNèÙ‰˜:^.üX^îU?¦Şz"qÚùËú8+ˆİã,¼N÷^È¿üˆs·í3ŒL>ÀE‚@ï¯lßR¸ó|2ßc›Z|ĞŠ•v3œÅ‹º-\‰aúF'Ò½¦L/µ{Ù˜D]mAyTÎÇı!mÙ½Êñ=µE›Âº&Í'J~MK% ½–½zjÓÓŠ–ÏÑ’—å¦ô
½gVy”ª ]óL×|¯;µá”nÇ:\'ÃqZQt°ÇJjïk½˜b·×ç+ìÌEÊ“T†÷†ê½ob¡ëY‹/Ø¼1QÃöÁ‹EOTÕ7k¯©m¿ŠatJ×3òñqV:ı’0ò}¨à«JOïœÕŒ-º†cmH{mHÎÇ§aM³SÚ“¾)uVÈå’_íõ	g<¯Ñ}FC©Ğ2geˆu³}¬yşƒ@´“Åc‡b¢É¤ÏP Œ[%aj’y§˜’ö(úbÀİkëÚéòİD.Ğ)ÆRt©áV÷àSV]Ğëç |jî}ª+—¥Îˆ/°ÆÓ#¯S²nJ UÁÄN/N§äP•çu« ²¯ö(íüşŒ‡ur½¼êPN\x®è?±6pÚ³»×Ñ|ıÒ;‰qf¶Øƒ`Ä¢heŞ‘ †{XväRíõÊ_'~DÛü•±fóíƒzS‹ôz¦ÌïZŸ6ØíªB·:¬÷J~gv\6Èv¸Èî>„!æ’’8 C&fäÚv=¯ÙJA‹6î·YüÉ=6oL@×»Ióõ|ˆXãçOï÷«1³49™!$}¼2È;ÌÀ*¦TZúe ıO<7=ÒQ*:	a"¡wïlØí#§£ájÏåxó»Vø­HU"±nKØgO\Ørİc•ç‘­ûœõ±ºSŒ6"¿ ö»
tÂ6 àˆ_Ş;_Á¦>@ÈÎŸwmXSåwkMŒümîGÑàĞ‡¾?àgåÒWÁ"A¤¿ì{nÇv¹"[ì0Ä‘íàŞ§Ÿ`œ7NÎë&X¸’ôL“;­C-Wpœò­ª”+ó©Ò_ôàôÈƒfF¸õ¶CæéÇÚÛ¯Tü°s:Î*&‰P¶ÄF¡ØIº¥ÆÕvKıÊÚ&ùí;Ï’Ífìoî6¢~§‚‰/=R0ıWÛöû}d¨¸²ÒÔg_9M3ø?Uü$’—
endstream
endobj
89 0 obj
<</Filter /FlateDecode
/Length 3285>> stream
xœí\ÛÉ}×Wôs ÷Öı<š™}N2@>ÀÉnŒìæÿu#«ÕRwJÆnâ±åQS]U¼²HVË³Ò1ıLş|šÙe0r2Æ0}ùzúå„Ÿ+Ä¤­ˆÓ¯ÿ8ıíÓ¿nféàVŸgè¯` œğÏ_~œò›_>ığ£~şOšÏG=I©N÷S¢¼5¿[ŸŞN?¼š)No?ÁD‰C9i?û •”Ş¾ş(„¶šŞşurğùÛß' ¨°$˜%Á'‚o-!\ŸCÊDĞ`óØ&Oúò¶Î8èmV2xÆ¹tËEÔb‘Ë;–¢\YªCê%áÊ×8WAN4~éóíÑ`e-ô’İ%ÿâ63Z(ÎŒ_2ÓŒğgøóËIJ7;ü1“ôvÀ3)eÈJÚÙÁLf=#°p¡üş82ÌŞ¨m\+ğ½ÈÀ£‡¹ø¿0î’s(1[i„œ¾æí€ëé/:fH\…	opÚhYhÚ$š‹Bµû„Ó¤—.Ï§g¯ñÆQ™bhE‚ÿ+¥+`
C%|æÊHcŞçµ;Z@S³0Z…Xh.¬€©h}½ØÅ;yãC¥¡;Ô·_N.úvõW³ÖÒĞÍHqÅ¢)‘­s¾[ÜÅ0+§¢al"Íjøaâ Í;ïÛÅXQÒ0ı MH‰HÑ"ºØi©F;«˜]ìg˜ıV-œGUã¿ŸèşD™µ2Í›iÎXÆA¦E[¹Oœ"QÍÊæÁY L³Ê3É3Í;Wô–u”©UGY—Hçği=Ó´(ö+öÉT£ÍDV,´4c‡£”nï'BİNH¢i	sœB'±Ú@LØ¹ìÍ+HIä;¤Lò2®uòG²ù-Ù‘yù—Ó?1@„)ÿÅ¸Pß§æ‚˜ò=,|ßÃÂÿYXøë±ò0í¬¢¥ó †¦şÊÈŸBôrÎ+Pg%›DG¸‰ÒœL„Õˆ—ÁO"ºY‡,Ê`Aù
Ş#ÙÏVØ÷:Ğ‹è"1ÌÀ½"@ÇT`ˆföQzNF;G7[´›ˆ «(,_ˆ˜RC=Ò1¦´ õ°¸@”€‹²X·'Õ¤	
™)ò}Av³>Í[C"0„dŒ!1ÌAˆ÷ª@6b¿³‰›‰üv"ÕT¢
IåU‘ŒŒ¦¬JgSyØbdÊ12;‚ ÂÄ]ÅÂ¨Ö.ÕN ‘AËÆU ödˆa7ö
2&ÛYp‡Îâ U6áÏ&ÇOf˜ë?²*„‰Oµ*ä[F"QüQeø¹ØàWÉ?Ø t¦›BAp¶ ¢n1˜3*Ãñ¥ ´ÊJÅEP>¢°¶“µ=×K_ÈL‹ï'šÈ‚‹~¢µúÌ›nå‰n†ÒÕçy‹Hö3Ôéa"i‘
µ‰U3Œˆ!Tú*k:çSTãğµš{¾šÉ¹JMÚ5|Uğ©Şf,"ó?­1íê)TÏ¥=ÇtU¨;JIUí‘WWß^Î-™S‡£_acTæö¿{8‚öRÜS'Ø®CVÍ’V;3·9oœ2æ^gxÅ¶Ò\[0o„[,ƒ‚X|)Xæ~Ã²ÖÁ{¯gx)lÙ”ë×ò[•{^ó8ğD¦mĞ!lw¬ZY–ó´¡aßºÔÅ(şl“éÎ¢g”aïÑ]â%Ò“áP[ÍX¶àè¹à
Œ'Ÿwx‡…ÀriˆNeõ‡œêò•ği«³˜â©)Ò`À„s´»¾®D¥`WAêUXF‡²¤CÜgôîø[”{P£é½\¼g.cŸ3ûé³zÏŠUê=ÉU±d`k™ÖA½aµ ØöÅjÌ
»¬›iq·çº\Ñ¼£€„¬% ÙI…na‹ø"ÿ…—„îsAtYŸËoOzL	×‘/y
òÓ…É+kŞh×ó–İ"„”HûÌå g«šGóW¤'³sI‘f³¶*J;«¬m$ğ†
ÕĞ;Gi4”…Ã@æéKjğ.‰·Â,ìhVgn
(­ş!ÖhoºİcÈì~#ÙqR³‰¯g´Œ|ŞJÒ æòÑ¥ĞÄõ´K¯*ÜP>èÉ²|nË<mŒ/‘eT2µ-´œ•ËIWÍ.Ušğ{Ù›«¸7¯YîLSİ'S|5Ë´Qi§çxâé7·Wm˜ßac5æÀÆQ°5P\—ÜàÑ[aîÍde·UwrÜlS8¶¢®uÆgä¦p¼ mÊ’B3Ö\É÷
^d¹.C¼àN9h3S^;1íìÑ&¶?¦Íÿ‰ k°_Ri®Š]ªSûº
£ö}	ûĞÙihíñ}cÒîí…ŒG"•ùõ»Šàğs°Q‡…è»à`ô è¹+Ë*Ñ“VİÉ¥S÷øûèL@F[şéXƒe‹–/ÕÖèş©B7ƒv~<lh®EllE-¨}Â»Ëácİø*‚8©5_òéËˆxÂÀUZÀÂªé ÌJªD+¯¤ n„Ó*Û..ãl}Ñ×Ã.½É½•ÔcœÚÉÙÕ$”ñbs‡`ÏkŒW;ÕÜ“±±åÕ)*Š—Çê.£÷Ö]ß@ñº+¬jÆõL™“U^[¬49k†U­ôYÔ)L[-!™ïÓ+Û´`:è¶iM×é}½ç•Æˆ“°ûTS“º^¶j,¥[ÒÈ-¾!¶ÕXGÍÙú(:¬¦’øHn)i”·Ø{ÊÁÚ6bÃöiÔ«xL<–æ[y,´ú2#»³ÆÌóÚ–`D¨—‚Ïü©võcF’u,uªş‹¯Êì·õ`¢;Œˆ,g­>]ı¯ÆŠ’†Ùz~%}³}úßÖ1¥(Ö‚F|¹.ó˜{$‹Aµ°®ëoœd=z¹Ğã…'î8À9Z
¡²ÖÆŒi\©8;p;İ‹·®ñ2·WØ‡˜š«K3?—¬´Ş{eL2Ë“ ,¾æ­1çÒŒ¨Ûáç%›çÛn $YU¸GÖGBCIÕª›» ¦>¾W¥ºì›˜n«:«í\’c§ÜîØâBİQnFÍ£ÍŠÍ<•›6ÛÔ¼hı#½şJ‰]İ8ŠåÖ>NU%­0¬^Ëœ·¯	™ºÅ)úïğVÒ*m#¨›M=?ƒ«ñÖscË&«É†<“Ú."Ÿ¬Ş•ê“-4b±U2?>å.4šöP‚ DMeÒ£˜¦lmï]‡”æÜÉƒ»Ü7‡à5×dÅ¥Kd¢Ş&ÉÊ ¢!£’ £têÖIÑá°lÊ¬>¾÷ÑéE·$}ÕïÎâGÇœ†1i^ÇqeRXªK~d©iï{ºÑ
D­±+ëTùx­Sµ	¶ôİ%2kG3Öl©†$dø%‡Ò”¢%LÉyE÷ÔŞİ€QÖ´˜.ŞÇCÍµZésã¹AÖ<—ªÇÁ!—–`¬+ä­ ÍeÒìÄ]ùÍÏÓáš,B¹ŸØ!=kÖYõîH†á&,DMU@}äÌ±<Õ=xµzÁè^¤íà0_šd_hÚ¯†¶ñ‡´ÒĞCâ½j`ï¥i‡DşQI0“iX¶áäŠÊ®î5›È€@^w{>İ.lØ}Ï°<âÑZûòb„–y—y!çİç)kc“Ú‡¼&¢%dé/¦˜Tô”*yî{º*øt6jÙYİÙ(£y$‚ëÖ.(ÑÜP"¨s.jéjåì)s\¶ëS{Ú¹Vø‘æY¶º[kº~^Ák!ãg#R-£ñ»”K‰7;“š²äFØ¸(õ‡Óâ+!õPG‹XØÉ²¾¬÷Gô±£åÇí{" ÖùUôÍ¼sí
ÒçÕ¯Z¯ªÜÄr÷‘©íèsS°œpXs±à±­Å0¿Ä²1#cşÿ-N®i‰Ç$×4íÁÚ¢Şú]˜æÆõ!µíÇÖò%ÅfoºÎ=)°±+:ØNtXæ¼fš›h	ëõıø$˜VjºóÅ¨vT™¾ÈÔ‹t½_:´_¾Ñ²b`H×
‚n/U9İMçe<·ay÷—}¤ªGL@1êû>xBz¡¿í#¤å€ Gµ¬TÌw‡^ì„ûÇ†^¾Ä#B/Ÿ3ô–£±ö@@=¡•İv·cµ”£ş¡a¸>_ÆWÜÂ>–òdİJ7cÖËÍÑQ˜¯ôĞ(¼é›GaÎÀ°(ÜIu 
³¶÷°(<\@­$á·MúŞ7‘¥i†íÖ”l­3ÒGR›³ì.Ÿuk5ÿ½õÌZ)è.k„Ü…±:½[s—ìRèEIN_J/5N}FèxOyŠ!X›„1bq§Hª–§|CûH77Æ;ÄKßfÈaœ¸%éğÿİú/Ø”P{
endstream
endobj
91 0 obj
<</Filter /FlateDecode
/Length 3097>> stream
xœí\Ûnä6}ï¯ĞóQx¿ Áã[³k`?À»I°ğ,ìÿ©âµ¨V·(7ÕñŒÇİÕëvŠ<EÉ3éÃ×ÄàÏw3yëŸ=÷ŞMo_O¿ğs¡›¤f~úı?§ımúÈÕÌµq†ö\È'üó§øâ÷_Nßÿ(§_şæ³^NœÓı$‡Æ0ôáõôı‹šüôú3L,ä“´³u\èIÈéõëéÆ¤şûôúß“Ï_ÿ=@¸¥@-6lHîòœ,/ñE â¤Ï¯ë†CÜfÁ%–s³T"JÎG,]9¿d.—‚#.Y.ŸD<mw^Y®W3¹4wi?»>dâª1%	?ÁŸßNœ›Ùà—š¸Õ3c I@\Ïfª`–3ÅWäâïà½j–ÆnãZ@%(oYöì-ÌEÿ…ëÎ…0‡`³†+ãÓ×øF°zzÇ7
Ó‰«Ü„ŒT’'™TAf<e“~zÃ«·ÜÄùäl%ôc%Ê@T8Ô¿2Ë ¦p)‡ÏLºRÀ5ÇYi!OIæ8ÈÄÌ”Î'™q/`”×6sq$¯¬Ë2,‡üòíd¼-ïŞñİ,%Wu0JŒF·ê”(óÚÛ(7ŞÍÂ¯ˆ™(Ó¾ˆ;(³ÆZCİ6ŞVW$>(ãN¸D”Hæo¢R%$/AùS$(ËWåä¿Ÿêø ™¥PS7ÊŒÒÄ‚(ó:[,E¡˜…G‡¢LK<2kLŠ[ŒQ”æÅX¢ŠÃõ(“,å/å'J•TSÍb’…óux•åÍû©"¤¯HªÓVÌQ*:«©ÄÕ£
vê{©Š¤Z;5˜µÊhÔk=ÖüÔº­y$Uşvú7Å¿¸.ä×aItÁšòmYø¶,|[şbËÂ?÷à/ÚYxs©9äPC¬¾1pàŸ (÷{‘«(Gr
ãQêwQêƒG Ù³ğ¥Ø {ƒ94$@@9„P£G~“Ô*.@
 RÙ "¬^ÍÖsÛÈ1ßŞÌóDg)àË3İh)Ú¯Zû„diÀXãH9`$iÌ/¤)Na$'a}oÅ˜O'ÃÌI
¸€ãP WÁì	Ša=ğ ¦ê4
1İ¸¢—e¡u!ø9 DŒyÍÑ'SÔDe5«aÄ‰Šâî*â¼GÁ°4áC…é‹p¬b³9Øí ÃÜÇ;C]£Ô@†G)¬j"T``VŠ-­FÄp|!\lùìŒA©$hRÑÓ4f9¢öé˜jg°hkV«QX3+‘ĞHÌÖKÑ8#¬GÏuëx’Ú&La$'Q}?ÕIPl ×ÚNU
,ZYbäĞ*Œó&OPiåxÙib­qæe¡p.%b0¬DŸN‘óDu•œ¶v Pheo×ğ–Á¸§·°qÂ¢šÀ%hÙRV;¾Ğ¥r˜P5}ª‚Mºu•û^Ã˜¿4~<,ÀN·ôâĞ¯ÎØÙÆpA¥­$Ÿˆœëâ¸SyƒgÎ¶“¾d£ÉÇh›rÑ6@Øm„—á§æ Wğ|ÑO@àı#|›ôÙc¼ÎÃâ¸,ÓOqö¸a’"]cb§K ·8^=§p¿|Ğ%¯£óàÏüÙ‡İ“€V%cÂŠµÕ»^^‹.:|Â&Ëdô­Å×KPï|ŒB‰[ä’$ú9EXEyˆÚKûBÆãÜ–\§ãü(ó?]ÔŞdCÈŠãt—#¯>$0>¾$ÛTkC°-\×ƒ&!‰£´Õ^Ç0/EAzı$£­o>¡'ûLBİSŠQF§N1}ªñÌc1!¾m@Ñ#)€o»¸Œ,e[¸–ªÇ¦˜ú‹ì‚I\z©
y¶Í
÷èÕ€ãìgÂË
¬…,–T;„E¿7TilgfÜsã1İRxeÖrÕÃ‡hj&ÉºaÅ÷:è’*ş´µ¨b/u£¾E2QÆÓïAĞ£Ù+šôˆÙCÊÆÏˆ÷+ªr½åİAĞ¤›¢è´@&ÍŒhM	xåô†ÂŞ
M"óam½`\x{¶_ªTI…ŒÚ‘…Š.TY»Šªóoı™lªzvi¿¦&w¹èM§‹4#ŸËN¤ƒŞÖÄŒó{Ü•\ïÈèU¾©7ôÅV7TÕÚe¥T½IÙ Êì°RîãæRËî}¬î4g1}¹àÅ&nvÂ…]¦š2–¥J+(KMl²¿àbfyÉù§%¬jÁ K[²>·`¥y.‘*Í›m°‰g&ÉÒœ_*Íì¸¤CÆÍKçE(ù‘+”ê)ö>ä.ê+Ì8o€[)3–ûØ’ÈöÍóïÓ†Xö¸´$EÂ×ŒdÏ3ç>óì‰†[Ÿ/÷ 9
› ¶+Şpô„}«W^›²·.$é+Lµ!¤}åç>ãH®Äá<¼ª8†‡×ù»wëeX]aoæèöqXûŒlo{¨È.˜ËĞn³ri™_ËÈU¨uV£Úî¦”YVàëÀ‹ÆuAÖ2Xãjq¯)qûeœé¤©"¦aá¤ñ"¶onÀœÏŞÅC0šé.d˜uf=¾_«šBX¤<Ş¢HQë…u„ö¸ü+UQ«Ö1ØÕræg3o­ÜğYÛŒy³¯ïP®¯ïX­KÑM™šÎ<ˆ(Ä[«¾–¹ãn…4<WØ¼¿¶€±vB½B\FœÚÓæÍşk¹Õl½É_ÜUS` /‹“j¢õçÈÇŠ:smÌ]`Vy±&SoÖ8l˜K{:A úzØ#
¼ê¾OS_‡8™P_èxÆ¹{Š»àÃÕü*y¯"/š-òÆŸ{¹Z<m=°ÈëÔ;Š\í»—©ø¼"/ºïTäfåNèME^'Ô+G£wñ5û¯æÖñ{xÑth7şÜ«À‹Ò!ZSàuêN‚ĞØq>­À«îû8õuH“	õÊÉi-ğ'Õ†—£<c¼p õHÏ<çåzHé<QÅÃ±|Rİ<¡ê|”±hOÎ/99ÿB®¹t®yé¤{yz®1ÆTz«º*ªcà
D(ª™’ør¯ZØ°ÙVÏör$Í¼¼¨s9Ò—nÈæGÖvß€½„ìpêÚa—°¬Ü†¢æu¹c×AÆo±UÓ!§`­#4‹½õƒË)=û"º:ü g­Uİ®XhDº àûnL²Ñİãxş"ÇÂ©õ‡Uğ<†S0ÁE£~È
’iD¼l§ŞD6Ùné>TXŞû À:J®ÔS²ˆjè²H®·ıÛßké_°b&|0D¼™sT§†§‡ÇgÓ]&¯®øê¾ze\y:jõ‘³q;v8j^—;v½‰¼.ËÇ>.Å©!ëJ»¯?³¾¯?Û—E|oƒ‹?o©®¹ã˜¿i½»uW¬ëbµ$?ƒ@†Az{·˜úÜ#q¯G]«¦CHcëÈ±¤‘è:ô@0Àªr›";é4*]pP}Ï¨A«îÁÄ±ujm©
KüY¦òé
®û,•Ïc·ƒô¨N5¶şg#·n¹Dj€ÑÏq¿ /±Ÿº!e›Å®§´3·¦Éïª ÓûóGI2ÕĞe‘ë}ÊxIŞ±+SózÜÁ_K¾7'Ms<FâªSÃ9?WW|Åğj“$ï€5¯Ë5¼…Ùä¤ÇÃ¥85œóÓxuÅ×|¬§O’«%G“dêsWŒÜz_4$WM‡äÖ‘cI2ÑuÔiz²ZÕí:Y¥é‚‚ïë) ÈU÷`‚Ü:uñd'AH0)A®Æ#˜ø+oËo³LÂzi;`Ä¿ô,û –Ùhè²Höşvâ8–yô>KœMËšxuÅW¬¯¸ÏQlc^—;vxSÒy{$\ìĞ[<\ì®.‰ûÅ6æõ¸ÃùÇš’á,“Xr0Ël|îŠ‘\ït†³L¢é–¹päP–Iu]*jË$êö°Ì&"]PĞ}MÙ,“èË2N]êººOÔ¾O§Şqÿ¾	H¾ÿ'Ä? ¬\t
endstream
endobj
93 0 obj
<</Filter /FlateDecode
/Length 3000>> stream
xœí\ÛÜ¸}ï¯Ğs kÉâXÇûœd€|€7»Áb`7ÿ¤Š”TEµÔÍ¡ºÄcÏ¸»šªOÉ#G0)
ÿ|ÅÛhõ˜tJqøòõôÇ‰>Õ`œJÃŸÿ:ıó/ÃPnGíqh(êwx¡èÏßÊ‹?;ığ³~ûoÖ’´ u¿f‰¢¡åıørúá³Òğò+*ÊêÁ„1Dn 3¼|=ıU)ã~^~?yüüå—×»„,‹À¨,ˆû:´Î³\¹$-[”>¿l;yAÇ <×~mVFÎG¬C9¿dmÖ‚{CÔCÄŒON‡m—v¯ÆYæ«•Y»»ö_]vÆ(¸èÌ2	Ã?œ´ö£§/;èàF¥<€C ƒv£GMf3°ÈPy%.ş !Z›Æ”à:®+Á¦ 
°ÇP—ü‰×Q¨Ñá•Véákyc<z=¼ÒK…³Ä¢Wq ŞX£'™±Yæ“‚eœ2iøBWG´/úÌL‰rQ$ÖcV4Ö?€™eS¼Tãg~ºğOã‚	8O“,j”Á¨¬˜&™‘.t*¹0Dwi$:oCœeTóË/'ŸÂòî•ŞÆhËƒIâ…Å*I–œ÷¡2îSÁC²ÂM’9ƒ_"’‚—aû”+ ­ÈÉt„ÈI$‰QÉ§*Û$µÆ;ó’e8VÌÉæ.WÍ“ÿzâñY2°ë-2oğ È’›½Ï’FpåâP‘9"ò"ŞOy+9*Ò9G%—$Ãâ^d½ÈŒšæošŸ"µÆ<‹“,kœ¯£«À,o^OŒÎHbµŒ9é £“]]@Ì1ØeìKUp’¸v8™\e2ë\<?\·<¢Ê¿œşM"å/õ…ùun)8]ØS¾·…ïmá{[ø?kÿ¸mƒûœÚ’F5îg1DL6Ğ.‡Ç|Îr[ävÄ{Hš”“Ô8A¸Š¸³ü*Ò€H@¼}A' °
²qãlÂÑ“ã¿YŠPôPŠ ²‹$»A²cH:TršïäGGó$µ ñ•”«,¢”6×x2©ı£0ÓBJ5bd¶8E¾’NyÊ:&¹HëëJŒ:æŒí‘Ğ¼µp„è›Ó¥Î‘	Ú4	1æH-š…sòç„
1Íëœ}¡‚'JãY­cˆ -"ÜMÄx	 è4èó‡âGcšÉkyTcPs§òQ'[¤è˜¶$õø)&Ç:K#£JËbLd Äh¬^q°ò4I£±H¡ Ñ§‹œĞˆëºek-€MÛa²j‹üh¡ QºGi §¡B¢È]ø$Uš²I.²úzb%(&€°=¢9œdá	Ñ7\hŠŞ)c 	xsĞ$D€`ó8CBHÖ,h\ÄèØ’}©b'ik™ÓÚ¯ 2	­%Ú-¼Í`¼ål7Ò³ü ^N›²ZÂ§½|B¥J²ÕÕâ‚ˆóe–3ï-ßÕé÷\·¶X|@máÊUÅ#Œï-)åœR6Åß@Gşé_W>Ç—;ã®ø×QˆÚ¬Ük	°-½-ûŒ®¢{öóåp¶Æ‘\+éã˜¼Â-»£}B÷“ù|¿Î„ÖF°ç+Sæ”ƒâÜµ rG5µj¸R¬òÕ”_£zÃÅw„‹t¯)Ü't†Ë*œGÀe	j"õ:ÂEä«)¿xvyO¿Ã=ö3ÚÏxTˆÅñµlßuÑÙëÈhÖ;$©l°V–sÃÊ³Œ—PãeÆ“A<©Ûå”s÷ysê©|¾w½lw{zª1-ú|ƒ>Ïú¬º’3‡çK­‰UêÚR;×ÛÆ¯)êkãñçz<î ñÈÇ=ğ'‚6Cx%ÛVÑë—Eİ—g˜PºÂï§©Õ¬à£?u*£âCœWbG6?»y*c‡Š¾²Ñ±5â9É$åsm²#“Ø# xrC\†ÚOÂŞuOS«‹ú¢‡ØFÑ¥í9_‚§Z¦™|Â™tº '¯Ã¾t~Œº¥È'Ô¹yÍ&ij©~jFŒ›ìÎú²ıÉ]ç¢÷i²ó“¸ÆÏh›ìã¿O‰?Ïş‰÷ÎˆfCú®í#J®@É\E¶;û™m}âÜd_ìFÎ´x-÷5Ï“O¶Ès¾>‰øı…¦ù²µŞœ?(ùÚê¶Ç¶Ç~ÊW¤©©1Z³·Ï"÷ªíß<í—ü.Àîã´.]óKn¥{Má¸ímM§~ğHœJO`K9ğÔae?¬‘sõşÔÒÉ<7›|;¾zyÿ’«PhR	ª¹¤¦²P=¶ª:¹°Ã™ÊÜÕÄ&Ÿ%¼
!4íp{íhµÎ–Ù[lw‡†xÔÙÖn>ë3˜¼û£¡2ßå  2âM­ú** NO•Ô	iBEòßÈ¹‡=é‡¯G¯æz©#İ:	¸cN¼Öe/båD‚„îÛT‘m]ÜzyçœĞÜ»ÓË)tˆËX?Ú¹ó§ó£Ğ{#p¥ÛÇ3Ø9İÃû ¹KW¨Û?7÷: ™¸™¶$=æÆú¾q¿jrvUG=/S¸ñŞ·š<˜°t­&o·@Ñ/FÃyïRL>˜|ZİsşÒâæôÌŠìŞõC/İFŸ7†¬¯Ñ¾±oZ\÷Û=C\xOi²ÉE÷¶û<çß[õßt—å˜>a Ş–’æ ûÜ–À&;ïleşšòŞzëì<ºÑ™šn¹+~f½4$émSté­7µšÑtí&ÌĞ´Ùç®…DSºí&—×o½ÉÕŒ¦kw‰n@“ô¶):xë=¯cÎ*¢Í²k‡Ü¤¡ƒà¹©Æ¬Ù{Q>léÊ§äXÊGØrÌÚJæ·í#ù6yı€¯õ²’Yi‚ƒíÃ¶;Ó>uP›{tZ>‹¾5ò4ù´¢¸lİ§Rºæ¹Ûz‘ïrk—×v–Så½w¹çáSœO×;>ãÿÕò;=ï^ójÅ×*€ù€&'¿©âÛ(®UáŒ¨ŠØŸè
ê<Ğgòİ“-}öÜwç¤aføØ¿>Ûp‰Q½+ÕUp!¹¼Ùò¿›ï‚…ª!×‡äŠ‘+2Ş—ärn+²®$=—9Q&eu¿’òÚM¿‹YÕT
±Q3W}PMá1Š×¯c*Ë{·E7üÑª”ë]R^ñ†”Õ_*©ëôUŞ.Ie-+f€»óVÒd“‹öñ¼UûÉWzÛ<KtÌn@ğ(dwVNæ¯)ßññ¼ÕhŠ·±Dhæá,Ñáhâ »³r2MùÖß,oÅ®Î[É,4eÍÜ‹·bK‡ğVu ÇòVÂÖÄ[-ewÄ£Jlî¦G•dFš àÇY±íÎœUÔî}‹9«œä¬ØÙ~œBûUâGòe›`¾•g›Ø“cmZEz‰ùé»Ëg›Ø‰Ï6­"»ÏóMi#¦¾ÔÛ€F¿ ±T#¯ó£Î&æxÎÇ†­˜ºr>bâaEO";Ñç!'ÏO½‰øîò“ãŠ‰?:‡F_¶'¦CÙV©˜Ù©¬e™Lúîl4Ùä¢y<Ûsø	–ƒìÎ‡Èü5åÛ=jçC¤·MÑ…Ç³=Ç£)ö”’Ì_S¾Óãù§Ğ”nb{Pû·Êö×f{ª,4eîÄöKG°=«@e{¤-'èÔñ	%Áös·°=UFš `ÆöÛ}ÙUP{|øQ¿˜&Ì÷şÅ4©ú†_L«Ò„
ÿ7Â“CÈ›u¤o|l§÷Ïü©ûlL"P†~ƒ#LÄàTó×ŸÁYÁ¯ƒ³Âİ=ÓANkUİ¯¢¼òó¯ñËŠêòÔ?tTIyóÍ£J*ó8çQôäq@Å#y¡şRIµñ8•²–S«{ó8•É&áñ<NóI°ò¶):ûxÖä˜Í ó
"ÈŞ,U•¿¦|ûÇó87 ÉßÄš`…=59Mñ¨§vªüÍªé?¥şµ:²
endstream
endobj
95 0 obj
<</Filter /FlateDecode
/Length 3420>> stream
xœí\Yo¹~Ÿ_ÑÏ¶—÷,YÚç$ò¼Ù;Ànş?*^Uìƒc±½Ç’eÍÔğ¨›_‘l­JÇôµøşaeoƒ‘k”1†åãçÓo'ü\™ mE\~ÿçéZşt³JM}¡å‚ßûiÉ/~ÿõôãOzùõ¿i<õ"¥R8Ü/‰"°i~MŸ>œ~|5K\>ü%å¢ıêƒTvQzùğùôg!´ıËòáß'Ÿøy‚
[‚Ù|"øFĞ"Âå1¤Lİ6w‰`ò /Î3z[•q.İvµ™dßb+Ê¾ËVRo	Z\â\¹ĞxaÚŸîbo°2õzËî–q-ÔUfšş
ß¿¤t«Ã/³HT½²àÂJÚÕÁäÆzE—Â)ò+Öí©¥s¹ÃMV&z‘]z:ñÿ¡ßc(±Zèi„\>ç7Ú!¿ŸğÁ‰b€«°`§–…¦M¢¹(Tk't\>bï ½ty<½zc„*ãÀD"_)]ià ĞUÂg®ôTĞÇa;¯=X¨Ğ‚šZ…Ñ*ÄBs!`gLEëkK`[óÆ‡JÃ@¨/?\ôíİ'|·j-5FŠ³(‰´hóİä.†U9ciVÃiŞyï¸Ø.ÆÂ_¦¤É ))ZD;m#Õhg³K¢ı³Òª…s¯jüO'jŸ(«Vf¡q3ÍË8È´h+÷‰S$ªUÙÜ9”iVy&y¦yçŠŞ²2µê(ëiŞ1­gšÅ~Å>™j´YÈŠ…–F¬ı°—ÒíÍ§y5'O¢aÉç8äÄjsb’ˆœËŞ¢‚”D±CÊ¤(ãZ§x$ûPÜ’Y”<ıDXò?ÌõuJ)`.È)ßÓÂ÷´ğ=-üŸ¥…¿B@.`ÔUEÀ'‹ÁÃ0Ÿéœ‹¢+Õ$*rd$F!C!ßÆP¼‚¯LÔé/,h\Û'2x1è^2,Uˆ(˜à/¦2 ’ÀSV¥¯$4jt«Ec°®@ŠÂòI€ˆÈÊ!¥H^Ä™¢'¨e1{bÖHê_¨EuŸzÌ©¬[h/"š9xÆĞ°L
1Y˜*p©“›V)-™±ª¢RP·Uc•†«ª­4² OÆâœ]‰gr ’mç=è~èVJ`%çÒN%·"(ÑV.7Tak]EÑd"Ê†aã€=e³[Nµ÷)FÀ"‰
ìh*!ê¬
¥)"rX&¤f^%2LG¥»HUÈè]Ìu¦BA¢µ ˜n2åİjTñ.âKyÈpVªNå#Šk;iÑ3Å¤ş…Z4øéD½„
˜²ê4@ó`G@ƒ
Ú¥ó^xÔOjX„’\ƒÇüÒôQh9êæ_…ì4-³ŞÕ4G3[ÇL³0c›ûLoëGÕÁî©¸V,ùò˜a*õªÁRÅ(a0ÓÕŒ–)¥ y­AßòSëKXaõÁUh.dÆ¶´º‹±çI‚á‚ÈïX3V?&ÀŸ—6İ€.L¥0î¦ÚÔÙ—´¦ä}í¸¯=øØ]íäöÖ¹üÛÊl!%:+E' U[„*àg ùR	¾%^±“` 4º(Ÿ¶LŞ`)âEíû¡¹‹Y r " ÷@ ÇìbÚ•á¬GÁìÆ…AÖHÊ² -H*é·y_h:û`úLd_Dåš×ÜÆ<ŸéãZ[‰+f5NıÌÔùĞ¯_òoœ‡®úş|ÿ.ÿ~¯?À‡yÚ´«<’Ç5æ†s9VÌŞá‚)®ú$@×>|Ó´Oû/	®›cŒ'È 5Nª9cQ™ÚóyDÜ³†5ÄËœ¨±š"’Æ6N¶¨dÃÿQsHd0·ÈãÜŒXE\ØªeÌµ=<BhA n+<ùÂSÈêüšQÒùrãhNœp?nCO“˜V—Ğÿ…ÉÖ7ÆBÅ&¾¤ö«>éõÍ8¹Ú?*n¹	wëùµÈïi!NŸËBeQ¹}ûì¹è%HöùïÚ¼Ò8â•>ãöL+U¸Ï_ºöªŒSü$}Îìše±at	43µ™ÑÈ
š-3ë«Å„Ò‡ÓÎÌ1k™pÒ®ª`¦æ1³˜øÖ4ûôºƒ†¾©ˆ®8×ï+JV´{„:åë ®}İâÁEõuw_=c‚˜Úx™_;ĞØ·]Ÿa©sİfx¾ßj­qDéıA®¥TaZr~Ûî–<JY@M/hè ¸G·¬S3½úÈã:Í"Fùï™÷3¸Éáhƒ ˆËÀKå>ì“"%-öo>‹™j´V>4ûlß¼m[9ë%´ıä¢kgà§Èœ2ğİôÚ²ZLM ³vÌiU`bª““ÂÂ‰½t–^JhÔ§iÁ¶ç…Û&gäA¥ÂêKÃdzÇ»ö«~Ë:üÄìCl9‡Ø“Ë÷7ò$ƒrO´·æHºrB2ëO?ùñ¾å_š©.éÙŸ1‰LÆù¡D+‘qÚôşjg½§ß/2¦lnïvï¯˜Ö‹ÌŒ³wxÏövJ‘ÈÑ»	
Ò^®nËÄód¶
‰kO¯Õ!×R÷•NÇ³®(ÚÎBJH¦¬"ïY¢ª›5JĞ‰"[¹µp§ËĞŞ—€L£Åuºa“ƒ™‰ìë¼Ll>ˆZP&Â4óSöé?Ï`œY¡şQÆ,jÃ‹¦¨(ø&­ï’Tõõ-«©ƒÄ´ì9QµyVÆë.®Ä+±7bh(Ö²2s»ÍÄ°Î{aŸK^Ö¤¨T0¼ÚUk,¢Ö}ŞãÛªà¶¼8V¹½œ¯ğš¡øp ±.né~Ñ>ÇUıD^+ÓóĞ°½cNõzàÎ9¼_¶ŸŸ£ íæÚ×lû<Çôlç÷•º^Ú¯„sh¦¤äØ0šUÇ›A
yÓ
9"[Óà1Š(gÄ' µ·'FI]
:UFéë&Ùœc#fôªñ Ö[£:gø9‹è4ã§mØz0>¤šµVä—¬ëœKéuECéC·t¦ÈæZÏ“]«;¡¹§ínHº1•_mÕØœæKZ˜vK°×Â­,’~Û²‰Áı;‹ÏÍ&XÔ İÙşÁ²I:À<ÈüN«âÏ™ôÊï;”E¬¾’EškMÏ&9ÚÛäóÒˆ1iË-¯OmüGË$ÑÑ:İ˜œ—K¤j „T0šJÜ©DÓhærSS‰µ5;w2?b"ÁEßˆ£ÌŸ®
êm§¼ú¿cn0›xu+›¸ã²	M>Ó¯ºÃ@š#… 0ª¥¦~y˜,££ kŒÏË2NS%Ğé%‰q§¾F5 #yö|}XëZØ‘+–l‹/6§Ô_¶Û‡CífI›}O“6ìºìÔÙõæ±Ï<ş¾S÷§>·fc¢¼ûÈtAŞwÔ¥“€İ>òÕj>™-TXˆ§;¦çìuhßëcHæÒ¾ûNlÿòöñö›s³7'WÄXÅ×I¸9‰•Õp½éÙİ÷ JnÈ.Gì"ĞÜÓ¶%3Øõt9(Ï¤å™÷	ˆ‘9òì>“q&”RÆ¶mcfŸ™€*İØKQ-5Îó-§£«e3œ›µi
n¯Ïn`YMÕÓÎ¥ÆˆK¼çşöm >ÃGÊÜÍÑ-n´k
âÃ±cô›4ïZqrÌu”àö3å°{ëm¡Óå­Ğ TÕªHòçNv‡å€1áæ)WLXÄX»yÉÄ±Ê ?¹/}ĞıÑËIEå	9¯œ4­|êUø¨Õ¤Rí‘åÔ‘ŠU[RšÛ–“sJI<Ûè{_HN¸dC+Î®\"¸uAàæÅOîÿ|æ™´/¿(A9kè2¿¤À.—‹
İõ~YaèR.©u$3a–©ntFåİ½iv÷ÄqÚûN=3ğ (G ŒÁAäXQ~@ñÂæN9çufÃÎ0¶2~åZ+şŒ[#sj*4¸ŒSk§Ò%•û¹µLğç¤¸³–¡c™i–3²A2n¹)ÅŒR;›”0­tí5æztïèK˜n†!¬ÿæ1ò Œ·Qáãc¼#ÔÁ0şŒÇõ=ó° GØ²BØ»öµğwmehß¶•1­Rgœ\©oeX©ó¡+õ-DäW»+À7a£(!ÿ”èÿZDEùõ:¯ØW	øºş•	ş]íóvÒy¸—a£²[;ÿş¬ÛÙpbY¥¥4£eU-‹ªAs›ü|%»¿]Ÿh)ÅvíJyeùğÃË¥Ë%ä¾¹øA7ÓìPf’š_d:ü/iàƒeõaI6÷ ¯vlêˆ¢‰æ{â³êJ•t Öf'>Œ‘Ù'>\Æ¡G0YÅÕ3ä#şü#˜ß¾%!À·4ú£b[ir;@0r½"æ[gêù;w×¹ØVÔ;¹]DEP‚U‰“£±êFæ™X•v0RÚb[s}3oÁ¯·ò‰³‹Eõæó‘JQÄûöNñ\w
Û_»áßÕÿnÉ8ô
endstream
endobj
97 0 obj
<</Filter /FlateDecode
/Length 3924>> stream
xœíÙnÉí]_ÑÏÜ[÷,YÚç$òNvƒÀ°›ÿBÖEö1Ó5Rµ=N,{äNWï"Yìö¬tL?“€?ïfö19Gc˜>}yøí¿W&ˆI[§ßÿñğ·?Lÿ¸™¥ƒK}aù	Ê	ÿüåç)¿ùı×‡Ÿ~ÖÓ¯ÿIóù¨')•Âé~I—æ7péãÇ‡Ÿ^Ì§¿ÀD	C9i?û •”>~yø£Úşiúø¯ßüû Ö ³øğ E„ËsH™ ºlÀäIŸ?î#|›•a.İzµZd{Åš”í5;¤^.\q	sä€ãi¿í®)Óh¡×è®ñ×‘ÑB]E¦	áÏğç·)İìğÇLY¯,¨°’vv0©±Q¥p‰ü{'µ	AÎ =Th&`¢Y£çèaÿã¶@˜C‰ÙÂH#äô%ĞÑıŒZdHH…	/pÚhY`€Â\ª]'tœ>áè ½ty>={ÆT Æ„€8­”®0ĞO*á;WF*ãğ:¯=¨À‚˜š…Ñ*Äs!à`HEëë•€.^	È*í ¾ıôà¢oŸ>ã§Ykièb„8‹dÑ”‹Ö9¿XÜÅ0+§¢ah"Ìjøaä Ì;ï'ÛÅ8ƒõKÃøƒ0T &"D‹èâ‚Û5ÚYÅä’` ?Ãä‡°*á<ª
ÿó]Ÿ ³Vf¢y3ÌË0È°h+ö	S*PÙ<8”aVyFy†yç
ß22´ò(óa`Ş1®g˜E~E>j´™HŠ–f¬ãp”ÒíÃçÒºœ4‰¦%ãvªM‰‰"RvN{³
bÙ1“¬Œsì‘äCvKrdVşéáŸè Â”ÿ¢_¨ï“KqOùá~¸…náÿÌ-üµ7rÀ„:«(W¼œ1¸üÂ€ï ŞÔ pÉeT°É`7Cü (d( ?[¯ Q¼‚Ÿ•ˆHX®@ïlÄ¡(\ë€æ/@’“ÆÔõ0	Ôæ’ƒQºÑÍ¥Â¦  (S–/@Œ !ıX ¦´ ¦‚:q" (AÊb‰Ø(³%/àÆÂÏK a¢u fgZÅP˜ö•)-Øğ‘¶’	° FçÜ8R`6ñ¹r¯Qv•Ï4šB«ì8>$fÂœ´(ÜÑ&THT4%0µsé+ãŠ¢9
é.{K0tó2f)I¸Â£æ;È1•ÍªúIT2-ÚM‚ú9 qK0E«B¹. “š)Z†!÷]$=ËPT3pï:ÃÇ+ğ¼8³XHãŒ*ZF8)à»²R-ğW>"©vAizÎ•4A7~~ 	 ŞÜiÔ”º’¼†FR ¢H0MYğ((hÃDt4ÀDÔ³Ê‘ËnQ75Ë0À¦ñ˜­²`K4©-ifhs­©äm5©*ÙiØŒi`ş…nã§%„³”EJ˜Ë,òH{—F_óÒ[^5Ç„¶ ÜŠ&ØåBFd«•Œ-Ò˜9Õ28&Æ
aáe¼¼i5;l*ÆÃo˜?­¶‚]^-S»H¡l^=ÁZğ¯ª¾‡ÒâºòúH-~_ßŸqJï_ò˜ô]oaŒ*4Ôùe~ß¥9u¾Æ¼/ÿúr­*ßËBÿ3ƒÕ1/«õ|^+áıæMß^¶5Ì¦¾p‰OÀUÆ'³Ä¥®Ÿhó——5?ìÓûA—ñ•/h4[ÔkÀğì)æëld×³±×J¿•MŸ:Œèì{ƒí«úX6qËõZø]#d„¸wFôÑ|¥Ä°¢à&`˜„İ!ÿ.Òó˜_I%LV•ô¯'UHßUqVc¢e<‰6tXÁƒ'…T'•ÖÀËøª q»ˆ:,†õkòmìĞ°áÔ>?ĞÊğ•T™Ó¨°xY®{¨FêjËı‹€µøúÁ7
½ú!TÏädõÃ„ï`‡‡tQês„ş|]ônÁY_JéË)º¼‰rU¼Œ‘M³kÚ½º¾­7È~E…ÅÄ÷êJVôu$ ;\èp$ç9¹¢_=ÖŸ@8îÀ…ê]ñß›CA‹·§)ğa6VË^t»,×·Ñ£.—bì—rkÉ¦ßçS–%\ñ¯ÆŞ¯kYXCtœsÁª ÜåC¯sqg8ÛŸ6zIõXïâUó_¸7çÂ­¼¤`cOº\ƒ3e×–‹nÂq7ÑÖ:k¹·;‡äou"©²˜ék¸U%%Õæª-‘ŒFáÔŒU?ßs1Â’™5Ä‡é•Áó
½f}Rq;¾‚ÙÈÎÆóÃI;¯õ°Ø¾9ŞÁ$XÕg1~6Ô–1S,µ->TÍt¨-;d¡Ñ<ß 9²Ü€–(û‹üp@qd94İã— ×Wø´Å°Œ#Å«»ßÅïŸÇ%*´T”¢pJSÉùÑÅ?Õ[8^—'SE	uUšä<½eŒxQ©ØÒ
"rL4¥Csxœ]ü6¢‹ßgdí´ö¸j`
İWD=^6¶ì Çfåx]¼!"GP‡6‹ùÃŠÆ‘!°2¶Um™|†Æ-^ìQQ$u“‰—^ŠMªï"é¹q	«….¥w¸!¥ªÇF§:-ÜÆNºoñÇGl|….Œ|xFã	[sÍ§¬év„¦³`Eóãƒ'ğ¡¤K45Ø‹ª§œåä*¬•´İÓÁr—bÂ±—6®•jOš¡íT:õ)îŸcuÄ`÷(-b†8ş¬%U\ı‚…÷š'AblQúñì°:¶Z*M_S¥Õ>ó:³µØö¸â÷È¼‡g’\¤=Vdåº¾ûõ"AZ{üù0¯¹®hüÊ!¦E"‡²¨Ñ840tjÖ1û"&®¡ağ{T¼"0\L¼=(d‘“Ü P©Ì:ÂAÊ8£ºÌ\¯ËíoµkÑ)Ÿ¾kş÷÷n"òŒ½{ÉÂï`ï>|ï¦éÏÙ»¿·{÷€NBl¾?îÛ‹çy÷ÛÕî¾šx2§¸3ïËÎz–òŠ«İ€µk¯§k‘wá—Ş:ï‚Š•Cy7^^ë¨|íì\·[1×ÆZ¼ÜãzâÔãY%T¨iŸÜ±OŠÚæCöäämÕA§ûªƒçgê„ÉÙ™úŠæ‘™:›º3S_ëï^ôÈê([üUl¬a¢ö»Š­§Á÷¶ŒãßQïk™ÈéZ¬ÏÆ²£
Bê4qtÍÎô4/‹ª¡èV«@ó5É•ñçÄTÑçÎ7×÷ly“ôéîöò6´uˆı®™q¶Ï3¹V¹cìoFCºŒc²âŒ«»­>$Şt½ß.§µŸÉ¬ˆº’zSCÇ)g2„Èğ3FcOÇ³vÎ.Q·§qß]ŞDD‘7Ñì÷š3IÓªy'°fÎ	Í’ã&gZßS×±õNÑšK¹EtYy]åa|lK˜œÛ®hÛ²©QÂB´”¶9W__ÂŸ·Ä»ÇÿÀ˜ta‹DêQLšÊÕó»Ô­—¾™‚6L®ÜC9FAİmºûíVãoa£•êE£ÇŞÂF«F’Z_ùn+@”ÿÍBLZ{pˆ¹"êÍİô „—±aht­c—~ßçÃ ‚èZ”KÓ»1ƒ¾jhK)¾U‚J•`º=·Ø*“àˆÆDº1”ñ`ä^ÚÄ6J2LŠ) ,œ{:xÕ!©V±v#ÄxûÅ4²´¶ÂczfU»‹•±bØá-;z¦é‡	Õ³Ä{œG°ŞáÖ{"ì:ÏÅ[«éïHÿªáè·µ÷‹	“³Ó˜Í#Ó65¦1¡ã(UID}`årIéH½ÖRüMê2*%á·Ñ0´R’ÔÌ°ac—ªÙ¾¾ÍS‚Æ¶ö¹B+ï¿^ÆÚ-	ùqõ2§)àYğæ^‹fšê‡'ğÃÚV?d*)6-G¯,™¹ƒ|òDƒ¼FzÅ†‚®m*İl¾Å®Ïwø×õè°M5LNß¦–4İ¦ü¢´ônw¡R¦©2VÍ5mS¼º¦XÅ®<]É”9.(­°¥ÔjÅ¶Ã½s¦ª‘ş¶S¶¿İ)­}òn7‡nßÑnÇ?Ô„ïfŞ|»Ùx~ğİŒTò”İŒ¸K±›Å›N_»Y¼íô5Ê×¾ßÍ“³w³Í#w36uïn¦öMtñìÄ'±h³YŒåÃv0Gºa$nbôHÎã.=Ô}g˜gìa´öø¾‡Ñ:ÇG"V×ƒÎ™.NÚ{9l#LN·è%ÍC-Ú.ëÀãOÁâÏk'¼ÃîGdwÇ3´ïGd‘gT—2ùŞ‡@¬_÷±æ"òŒæœ%ï5:c75œÀ~SMÎMŒß#ã3~C"i—Å›0ş¶ëÕ¥Êù¢;Z”n”’µµÒÔ€{!¹:t4Ø˜d¼@¨‹ ³_ŞüÀV–§F“n'TvKÈ#‹Ó3w­[V&ÎèÅÿcC¯„Eåˆ˜ÏËı“œŞ®>QíKX³àT—Š¸;)»1LNkÖ4køÔïóCŞS¯>oBã}ñugŠ%ü©7hÈÁ¥³TÖÈ'AÅÃÇËêyÜMµ3#Â6_~ó³á¯v´Ÿq¢¥lúÃrØú±“U¼%Ù<h}ŸæŞŞ>şJí«ÏøåÈré<`HëTõ9`şŒj¢'}²éÇ5apŸ;ªVÒ½E²üiÅ×$¼¾n¨¤Y/óY²®O<CĞ¬œv† Ó³HõÆŠ{œ•T­½úVp:áÎ·şFÄyÖOKŒl:K9ãŠ†qöOY:ÇÿVï~dû§Ù|I¿Öâ}$^–~-Ø3Êæ©ú~†p.eû«Foô­Foû•áT¥`Fßˆª£7ÛÒÖÈ-ŸÄpÊ–¿ƒıU­pêµZq´ì\w–V4"ÎÓ
Z¢'Ae.ŞİTã12ìß‡0¾„A+“Ê¸³Ô¯ÓJ%lnöÚÑš8xA=Ğû–™Ö:êKÉP?ˆm1¾f©z9ïú.ô6¶ôkÖ+X–×ê:ãá˜Å­ş;´å³s1<¬Y^¸­n4pÍ¹ö7,9n±ÆaVÎclX)òbIó¤DwŒoó±Õ/	C]¼?&›'gRSõ¥¶×¯•caròï•DÒP&ãÖ\RXÎµ:5şÿ»ÿ_Ü
endstream
endobj
99 0 obj
<</Filter /FlateDecode
/Length 4235>> stream
xœí\Ù\·}Ÿ¯èç ¾æ¾ A K²ıœX@>À‰’;ÿ¤Š[âMO[-éA£mæ¹$‹µñÉÖá|m¿.†~sÀc	ö¨¶ÖrùùıÃïüsŠ¹øhêå?üó/—ß‡Môjî=è'jh/üû?^ú7üúğíşòëÿZ¹ú‹µÎqw¿4Äğ«ızõÕÛ‡o—zyûuÔ$´Ÿ\¬‹ç/oß?üÕÿvyûß‡D?û¯®ì@ØÜ€¼ oP>Ü‡µğˆ½I]@è~ÿöqÁIo‡³%ƒä6íƒ¸móûTÎMvuX¿xãC’»b/…4>„Î{ë§çíÈÊÒÚø]Ü]~ó´0Ş¸ç	ówúıûƒµéHü+\,«ŞEragã‘¨qc°Kñı;höõÅÔt°å®z´£5›îÒGÍÔşKíÎ õáÌ©e0öò¾?øÄò¾ã‡À!YHªrá’ŞÌ‡†¥jÜzÏøzù™[›mêıù#{~±V
¡„D&²ùÎù‰‘ƒRSK?K£¥£6‰ßË>“…V,aî0Á»R–JáÆ„ª1Ï7I\~“„¹LŒa~ûóCªy=½ã§Ã{äeFRäiI—ŒÕ˜RVƒ§Z—\ &cÑÓ/˜c9åœpÚ©ÖƒÂßĞc¶¸"JdÄ“WT¥mFƒOÑ]Fö`?Æ¦…{«iüwò~CïÂEúíX
$èXSú&)ƒîp±7îêXtfŞ±œÒĞ[×QG§º.£àÈ	´Ş1o†ı†}:|¸ˆÖzœí¸•óëáİƒxˆ¼.$İŠÏ¡ â"êrb™‘8;Î}E…(IbG”)Q†Z—xûHÜŠ!Ê~ø'ˆré8/Ìï[J!sQNyI/iá%-|eiá§xÃà£‡HôãıJÎª<ÁˆÙòDÇtèØ'µ•.¨‚ıPé0(+[¢è˜NÛEGu¢ØÅ­D1Ÿ0QLL9âèR¹ì\9÷SÁ˜
—9mWC?~C‹*N—¾UDË¨È\¹ÁYÈl~)"÷áŠÊŒí™‚±ªÎ‘Íºe
Æ¢ójêŒåä¶LÁè)"™pÏŒ3£Á«DÑ •(øi%Šş Å|=iôŠ.'Ã£sNAÁ‡ç|Ğ×eæSE;S•e¢sŒÇiŒÛiEˆò›èÃKZxI/iákI>¤X$OÄ`¶<}=å	Æö<ÁØ9OD_T™Ñ‘³VaH–ÊÑ“_T§òcÅnF#Œì¼å	F÷<Ñ°'ú·3Oô'':¦Üpt©v®\{ˆ©B`LGËš·
«¡!Œ¾®F¥Kß*‡eTÜ®Ìä	6¿Î„œ
Æö<ÁØ©ĞH±òc{¡ÁØ¹Ğ`tÏ)™S`Ì»å	F·<Ñ •'øiå‰ş óÄ|=iôŠ.'Ã£sNAÁ‡ç|ĞÙeæSE;S•e¢sŒÇiŒÛiEˆò›èÃKZxI/iákI>%O¤\¶<Av=ø<EÉE˜Û3>ny"å´å	Fô.eÇNy"åxÊŒíy‚±s`tÏëy¢;óDÒy¢cÊG—Êa×àÊµ‡˜*ÆtT°¬y«°ÂèëjTQºô­âyXFÅı°àÊ¹@`óë<AÈ©Ì`lÏŒòUWäÜEå	Æö<ÁØ9O0ºç	ò¥S`ì\f0ºïS6l%
~Z‰¢?èD1_GWšİ¢Ó‰ èSTğâ9#tw™;ÄÅTFÏT&Æ™h#rÚ#wÚâü&ñ’^ÃKbøzÃŸ§<ìÊÅÇ-SÏe*Q0äu`èœ'Š÷Gî³_
!h¯4;%Šâ÷ƒÎí•Œ7*İEÃz¢èßÎDÑŸt¢è˜òC¿tâàÊ·ı~Ğ)ÓQÑ²æ­âjhÃoèQÅéÒ¸Šènøİ€+3¬6Óø:OrÊŒíy‚±Ó>eá”'Ûócç}JF÷<Qc<å	ÆÎ…£[¡Ñ •&øi¥‰ş ÓÄ|iôŠ'Ã£oNAÁ…ç|Ğ×eæSE;S•e¢sÇiŒÚiEˆñ›èÃKRxI
/IáëH
?=÷Úæå·2éáªe×‰Ìb(Iôµˆ¼U9¡Ğ!R_ï$°[èK ÇÃ:úÕÁpËci38¢Ë&Èš¶$ÒD$ÑØ†·…<%¬ÁÆA_I¡Õf@Ùª•È›CPÂxĞDˆ@¾6lªÊyÃ›NVM€@K^0‡êSİ@Ó(-y "!r$G’1x£‰“‡XâğfVJÕç>Ç!yJö(ôb{sÌ0%7‚WtÁXlÊ:ëÛkjVÚ‰	¤±J"†™Ådn'ßaçc§r†ï°'ş·İ©bvuiˆX~aW‡)¶v›¸J3åˆ!vn]ìNE]¦¾Ê5+\te¼Jy’ëZëÁ©Ø½*Uñª³[eJÅÕ…Ë½¤5˜ãĞ¿¹\¦Ô­Ssp¹òt£ší óÔJk< ¡»wÒ4ÑÀÅJ'2Fò‰œ®„â$ŞÏÕÔŞáœBáÈ”ØÛ›cŠ)İ]h~5µÑ±^5MÅMŒ¤Y†¶Ó0Ä²™f™ÄoYÓÛ=hºÖ-·Ì¾æŞÿáÌÊI#R:µ[òTyQœâ=ùÀ‹“Kfİ»×#}‰ôO(ôõ}/X Uƒìal_}5ıÀï~xüîß¼ÉO‘H&{Ôşõ<?éq§òMõTHDÿŠ¿®îŸ¡­áÛÚ|Ù´¥>ƒğ!íæú±ÚOh5ö¾î«ÑL+¸ã#%>kôõ4ªŒz–F©ç;htÓŞ‡´‹¸›†=…àl¬fsO{JË”¿’ßö{Ê‘wRğS	Ş¹»ƒ‚a6ŸJÁ¨°g)Ø§ÛŞñ¶÷sïGRnÌİPÍx¾ŞtåïôÕ¼zÜĞæõ•±¥úÂÆ®’%‚ˆügX»5®´ey{¶´GÅÛ³Í‡qÁZ í™:¥IPí"<0[â;t¢H{&`­±8{¶Ì5…{ögäêAŞaºÒ¯pb”@Ø³È*,[æ„X›:òó¥¢w¬G‰¦x è–9œw^qtIèVHÒ-“ÀœÚÍ5?ÛébhÔnªÁ
ãmYá›¢Rh.º‡ÄLJ(±(L@LS}ÄoÎœİã‡K	HìîÈšµç`é;Ëç<‹ÕeÏ'ç68àT<Sw&W¤ìÙG’Äpñºød*Ö™áêù¢¾Z.®ı/V¬YüD^<¦¶èøĞ 2ô¥)äèÆƒ[‘tÉoˆ#!K'æƒñŠ¦S<XªB¬ÀÓ	”pª¢š§i:6êÇ1–¡´<Ë¦(;:ÉšåÙs¾ [k-¯{æ-çÀmÏõœÏ9ÿ›W¹ ÚÒùšHĞÔÒGk+E£g‘ŠLŞWŸ$Jnßzq—E™<a2WóÚÂÕø}ûÔµjö¬µ6ÈZë‡	Bı³š}^mvûşcí’¨*7µS‘ÅÄ;jµ'p·ÀDêÍê½&SHZŞî¤8°©ŸåíàEÏ£¨Al¹G­a–üyv­ìÚ¸ĞŒ«<8Ò{_u;KuÖäK2ÜGò%Jym©x¯HT»¸lÒb]úZlÉ”¼cUk1ÙŸÒåÆ™G-|]WøÒW*dE9áEV9ae.sÂBÖ ÈX@ d7Sv¤Ak’Öµ$àTœbQÂ‹—ˆ,*ğ.$-¡(RH´zVŠYM¢ˆÕ‰ƒÚêl`ê{¹SRj‚ŠBM!ƒ€ÑP °ï’A&ùˆ=ÂŸÂ`#ÈŸ¬µSXz*ó“¢PòöBRŠ0ş\ŸV ‰"”MŠŠEØwÂ…YÔÄE­–BE` ¡-J¡8 ·!˜¡Ğ¦©Å¥òºÙ<xÒ@Ôn<ı8ûv×c	ˆ²Qn¨Vs)ªîâ7.˜Ê…ÚXúRHXüNëõBãeEL¦$ó‚ôè2kg?ú‚l*®Ua®ĞŸ†=us¿+ªUú*z3~úJÃÒXa<T÷Xéç!{ü+†Å±`*W9å£É±âkq\‹cˆİJ¼‘Ôf7Öâç­·Ê
,¸OÉ(2ozŸüâ)şğ‘E+G0©ÍDFjşTe´¶Ë3¶åÚÈNüä1ßš>e¾»×6/ŸÎ‘Õ‹“‡®¼†üş»~ÀãµVÚŒFD·Z‰7.Iÿ¾î1šÂÜĞü¡k²‰úF¢ò.Ú‰†ˆÒÚ™Æbƒ67ƒx_suZíú£¨eFÓJşhbÙ6â,âĞ†VFş€lÖ´2ò…Æx¢•‘oúVF;YÏbGÙÅ£¢°á[^&ƒ ‡C€î-ÙÊ$ØÕ¡hemĞÎÜ2ÊÚçñ ßÖvŒ_7>Yû‰B:Yùp:ôÖSuXƒÂê<Ç½®¶`€5Ø
¤«N±Áúkv›ß<B#ë¶gcHÃW6
‰˜¼QÈÍ%–¨(dû”İ(äø—¡ùI.àKóã\À«F3a_Ğ¹05%‡°:YøÌN˜âÔƒ¢uß†«ıŒ=#s¬í0¾x§¶sû¢Ê	å#şŠGå„µİÙŠ¬±Ê¥h«
•Jë¥{D¬„âˆAEpô9Aí3_.æE>]”1ŸEÙhÛnsáŠs}»+tTt§]Ğ«'E|ü;v>òÄ*¯ål’ÁÏ`M±®Ø Œ›e	ß}.;À‰:ˆ{•–óAé`hù¢ğ¤%â¼
Òg³D4·DC†³éô%,!âŞd‰xÛ%“œ*ä¥ÆñDşµĞ|µ	›™½€êÌóô³øÄÏÒd¤ëé¼ÇvpÛÈø2¹ñŞï2tıL=—ò™Š:‰ıœË•5Z–ãƒ8¬Û|
¸§< K™Ovøâ?UÎ\qÖg•:éê¸ˆÃ~L©ã|±ûea7O…ídœ}…RÇñ!#Í7c	+ÄtŒW•¡ÄO’±Pè4LÕ9Á2gbXåLLŠé_Ê
”Dê‘Yê™›Âæÿœ³ ¡©wsí
-”8„¾j‹7‹|)×©‡ĞÄ×w±Æ!Œ?WñÚAÃt‰3 ¬p¤%(~ &YÀ˜Kj0úšİÙ_ÎU™i¿!L‹Ù(-
ÄùªÇ"Åï@dÓì3é3a†8­)Xã8¾ aøX[è¸›÷„¶;¹!ßÁå‘U	HãU0À«´PÂ¬"Ä^Å
LoU4CXäLeaCXáK³	êç»šªs£ô“·:‡ĞÀv#Ô9„qØÜ˜®sˆu´^ú—AÄP(˜TG™<yÍ,uÊZUI1nñvÇ%¾O~ï˜‰ˆ·VFsğ±iÜwMd»â^]ÓÈc&G)7r”²ÖÀSrÅxŸÏpŠÜÜZN}6ã)+ˆÈWG	¤“¸òyÊtÕÜv´ºô$½1vï±ßîq´É‹psó}ııîUVˆçğ`áç¿Z›e»8&‡óÿMµ…ë
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
xœ]‘Íj…0…÷yŠYŞ..j®Ú.D¸h.úCm@“Ñj1wáÛ7N¬…ø˜sæ$“¨jêF+Ñ›E‹¥¥Åe¾YĞã¨4K8H%ÜNtŠ©3,òæv]NfV Ñ»¯.Î®pºÊ¹Ç;½Z‰VéNŸUë¹½ój1+K8øNÏyé&„ˆlçFúºrëÙ{ş«AàÄI¸˜%.¦h;="+b¿J(ü*jù¯W?ˆ¯Î’úâÕqÌãr#¥	Ñ%TÊˆ2N”Şå)Q”yM™{wş›u\-IH–T!ó1d†Nü!„¥{‹`Ú^°Mú¸Yë'CßA#Ù†¡4?ff³¹¶ı{A
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
xœì½y|Õ•?znUWWuUuWUwW¯êM½himîÖby‘Z²dK¶eK^e›¶åİllœÌˆ€„Yœp6’ 6IÃê ‰“g™™àÉdáÇl™D‰É„%‹ÕïÜÛİ¶à—ÉûgŞÏïÃãJõ­ª[Kß{ösïm	 è€¥Ë3[ÿş…/kGVõÿö'o?‡çWxÎnŞµq¨0À×ƒ×ë6ïÿP´>‘°âù Î½mÏö]ûŸí9ø€5¾}ã¾=à@ô!ú)Û¯<¸mÿç>q ± ï±[vh©ÿæƒ »ğrcß­·ˆWüÃxİ­;°BÌ-û\'vìúĞã+ô»ñÛcıú•WmŞØö›{ğıOğ—íÚx`¸Bz	à‹Q¼?º{ã®­/ıÀÖç9l_í«ö}¨0K¾|%½¾çê­{ºæç?ğü6¼şğÜZòqğøî0Şq[qO~ÏükÁÂ[9Ã½»ôttA®€…—
`&ÿ%x›pï*$,'qÓO¾[ ´V+xÓ$,_³Í´Ç¹¾-}$P
ç‘neP°#ªíà@t€†¨¨ƒh€ÑÉĞîÂŸÁ&¢	DC/ø
C?ø„ Ã +† 1!Ä„£-übC¬d‡JÄ$“DL1¬‚Tá¨†*Ä¨A¬…ÚÂÛfXiÄz¨Cl€zÄFh@l‚FÄĞ„˜…· Ë°2ˆ-El…æÂ›Ğ­ˆ3¡±f"Î‚vÄÙ0«ğ{˜³çÂÄ†Ğ˜ƒNDÊ¡ßC7tşæ1ìyˆ½Ğƒ8z¿ƒû`b?Ã…Ğ‡¸úoÀbXˆ8 ‹— C¹@d8K—Á âr†+`q%,+üVÁrÄÕ°qV!®a¸V#®ƒáÂoà2Xƒ˜‡µˆëaâ¸¬0	#°q#ÃM°q3Œ n…_ÃV†Û`âvØŒ¸¶!îdx9l/ü
®€ˆWÂNÄ]pyá?a7\xÃ=p%â^Ø…x5ì.üöÁUˆ‚=ˆ†½ˆûájÄk`âøâAø0âµpMáu¸ ‚ƒˆ×#şü\‹8
×!Ş ‡?×#ŞÈğ£ğ7ˆƒ
¯ÁMo†Çà£ˆãğ1Ä[†›o…›oƒ±Â¿Ãípâˆÿ
Gà0âÇáVÄO0¼nGü$Üø)8‚øiø8â]ğ	Ä»áNÄ{à“ˆGáSˆŸO#~îBüÜ]øø<Üƒø†÷ÂÑÂ?Ã}ğYÄ¿…Ï^…û~>ø%øâ—á^Äà>Äá~Ä‡à‹ˆÇ‡/!>_.ü/ø
<€øUxñkğâ#p¬ğ˜€ãˆ'àaÄ¯ÃW…¯">_C|A|&Ÿ„ˆOÁ×OÂcˆß`ø4<^ø9<O >Ëğ›ğ$â·à)ÄSp²ğ3ø6|ñ;ğ4âwá™ÂOá4<‹ø|ñÃïÁ)ÄïÃw‹–H*L}`‰>°DX¢,Ñ%¶DÄDX¢,Ñ–èÒ["ªí6¦Û2Óa…é­ÊôÓÎtÒÁ4Pcš¦3½2˜9™Î¸˜n¸™>˜Lâ=LÊ½Lš}LvıLRL:ƒL
+˜Ì…˜„…™<E˜ÜD™¬Ä˜LT2	ˆ3~'w“Œ—)Æ¹*Æ¡jÆFıZFë4£l£c=£T£N#£Eëùx®ğOh‰~Pø	Z¢çÿˆ–è%Äx¹p-Ñ?~Œ–èˆ3áŸÿ€–è5ÄYğŸ…—Ğıq¼Qx-Ñ›ˆğNáGh‰Î‡á»ˆ€ØMl…¿ƒyÄØCŒÂ¡—xç“@á{°€„ûH¬púIq!©A\D
§a1™8@Zß…%dVáÛ°”ÌE$]ˆCd~á,#ß„åd qYVxV’Uˆ«ÈšÂ3°šäOÃ0ÙXø¬![×’ËOÁ:²«ğ$\Fö"æÉ~Äõä`á1Ø@®G!7"n$7!n"·…ÍäÂ	ØBîDÜJ>]˜€mähák°|qùÛÂWa'y ñrr¼ğ0\A¾Šx%ùzá8ì"O î&'Çà*òÍÂƒ°‡|q/9ƒx5ùAáË°¼€ø!òRáKğaòˆûÉO÷Ã5äÄä_É¿#^K~Y¸®#¿)|‘ß!^OŞDüòÇÂga”L!ŞÀÄpÖÂgàFN.Üåˆãœ…»á&Îƒx3@ãÂ…OÃ8WYøÜÂU!æjwÂ­\Cáp—A¼kE¼ƒ›U8G¸Äs]ˆŸàî€;¹şÂíğInIá6ø·¬p+|š[…x·¶0wsëïá6!å¶Æà3Ü…›à³ÜnÄÏqû?Ïí/|¾À]‹x/÷7…á>î£ˆËİ\øÜÏ.ŒÂ¹;¿Äİ‰øeîîÂßÀÜg‡àAî^Ä‡¸û×Á1îÄãÜ±Âµğ0÷Há |…{ñ«Üˆ_ã¾QØpß,|&¸ï à¾‡øuî‡…«áQîÄÇ¸¿G|œ;[ØOp?E|’{¥p<ÅıKa7œä^Cü÷Ÿ…+áiî·ˆÏp¿C|–{«p|“ûSa'|‹+ â¹Âø6oEü/¶ÃwyGaœæ]…­ğïE<Ã
›á{|¸°	¾ÏW"~}}}]ú˜ˆ777å¦{ZZO¯@¡À66ÔzÔûŞñóÿ“…Æpÿ‚ñÂ¿€“èyá*î_x"ZÎ7S…)î½õW/,à56‚¿	Ş }äMn	Şÿ_¸m/j¤t×Ãíà^á%2›{$´fQFúQ×– Ï–­Ï
´%»QgO£5A1TxkQçæ¢F -[Œ¶áÃ¨ï¼Ö‡÷>v£å¾Ÿ¼9ş9"£%¼mÇi¬İÏÕ¢˜ƒç-(o¯á§ÂwÉÇğÙKIá¿R6a¯Fh¯‘êHiFqÈu¯\±|ÙĞàÒ%‹-ìï[0¿·g^wW®³cîœÙ³Úg¶µ¶46Ô×U§’‰xeÄç6tÍ®È6I´
#P×Ÿ?HLXRñ¾¾zzßˆ§UŒLD±jş»ï™ˆ°Û¢ï¾3‡wn{Ï¹â¹w=:æÔ×E{ãÑ‰ç{âÑ§ÈÚ¡a<¾½'¾&:1ÉØ±%ÅNìx‹áÑ^ßè‰öNÌß¿ãpïH¾ï„"Ï‹ÏÛ*×c$.+x¨àÑDu|Ï	RİAØWİ;ë’~ìŸìİ¸ebph¸·'‹­au0½kÂ:oBdïŠî¤m†[£'êN¾í)6¤Õ-ñ-/à7âC‡ùŞÃ‡Ç&ŒôDM¼g¢æÚóa—·NÔÅ{z'Òq|Ù¢e>€LI==ü&`ãã“¿~wÍÆR5©¿	ôvñ™ğzù°mØBì_,FÛrëS9Ø„'7Ï£°)øuÈ5¦×Lp#ôÊ©òs%½rCùÊ…ÇGâ1ÊªŞ‘Òïş¾‰6Eëëúì7‰¿x=:Á§F6mŞA÷·÷ôé¶bx"×ƒ¹¥¾öhjÄû7`'vR2O4Æ÷L¸ãİÅ°"Jy°sù0{¤ôØ„{ŞŒl.=5ÑØÛCÛí=<ÒSl }W|hø$Æ+¯hÍb³†¶cÂ3™’ê=<¼eÛDd$¸ås[t8›È­Aò­‰o]C¹×'j^Å‹±OdOaßŞswùfÚs1)E‡¹ ¿†r+¢óâİsğ‚ìb§”£İs¢Ã$åÛğSJwĞ£w½Oøä¼>z‰§ÎëÆÖÄŠå¯4)Xj“œ¦½KÇŠm*~ÎÛ´âİ´A5ÑŞ­=Óø®—
¥–Şö—ÛÉQZ”>Ÿ(;ûÊ—ø$j.ÖqøVE¹è‹NÀ`t8¾5¾&2”¦}£´fü]´<¾hhí0ãvIJV¼ë¬x}æ…k¥£	n
àüt°ÌSv¾€_8í{Ïåşòåèa)¾hùaúæxé…=Ü?(²9TÎ™Îæ’şÎGóŸ¿1Õ£óo|ªpÃ¦Ã'r¹Ã{zGvÌ¢ï‰÷o9_><'Èš·løúàµôãœ˜c/ZÑ]_‡Æ§ûDœŒÈ‘ñåk‡Oê ÑñÃ'8Ò½†J¿ov]ot%Î¡5;¬¡¢$$ş’	ïÀ¤*Şq‚pVuBoíPâİ´¾“Öwë­´^D¶©§¾ƒÇ|‡Ã¼…`$AcXég5æÛzé§‘\G¾‡?¿ç’\w÷q¾‘ßc‰[ş^¨NâÏkÖÅkÅãÏ?ˆç¥néÿ²=#¯”¥Ü£Êêlu³İŠ?IûGv-¬Öè_0®4~íü¶óœ«Ûõ}÷WÍ>ó«æÛZZğg‰g‰Wôúì¾{üóı·º÷ş1˜¾\¡T¼šúJ˜–¡HSä¦ÈKÑ¡Ê=•¿6ş³~>øùÿæObYbm1Nÿñu/}2Ş Íyüüë´æ‡Ÿ¦û—¾+dk
óì÷ğßÁS[1Æíg Èw¸ß ~ŠÈÉÎ&Iä­4>ßø<Ñ_yg4e˜Q…[†|<3õcî7çîğùıô0¶~ãm˜Ïé2oÕ-¢èõğ.ûfitvşâb8Û³§ÏgNÏhr¹­b¼Ì%Y<ŠW¦Zš[³Ï3ªm–Mİb$"‘İÈVÜÒÓsËŠgÎ$X]Äæ#Í“µÜ;[/"`½˜p9¶!øSîo„øÂ$ÌÙ­Şg·¹œ]v)¼*»$^µ¹E^µz-¼*øg|œ]å9Ş>ªòn•·wªDåCviA]vÉAİæ6†Ím‹u«×0Ÿ'`X½ÔŸ5"4
œêF ĞG€ÛèMĞbø¼nÍE\Q«÷ àtÙÜeÀs£[íæ»2¯äO?Õù
ÑÏæO:u6:ßÒ:ÅëõÓÄG/hXN±ß³?~÷u­Tf4‘|dÛ²bÖŒ³-ŞÆ¶–,Û²<îIÅıññáí•·Ü{v¼­rWÜ¿ŸL=ùäÂG>ùdq7µøQ”+¤8CŠÛÀ“³Á¨$)²Å¶:Ÿg,Dvše~Smm6•{'3ãŠ––+23ğé%…d.¯6æº-¹Væl29*ÿRşƒÌß*YäA!çò˜BîSÈ
	)»”ë^Sˆ²_p#ˆºÈ‰EŞÂ[6Ag¶3K	u>&ÏÊŞŒşâŞ•+Wl (Nm^yxa_÷’–t÷-$é~š¯ßğöw¼½¡>é/æ0…ğV¹]²iIZ8«…ÜeyÍò–…ÿ˜…XDEãI'OóäÜÀ'¿‰¿šç'ü0m—&F°]š"oâ-[şz»šSUmaBÉTÕAşÕvµ@)p1P`F. Lğâ#&l6»ŠaÏ#V«4Ê4§ÌONfÏO2&üúÔùeD¶%k"ßÍxK¼åÙÁgñ—,á…¥?ú}sª°ÅLÔ'ÁZx5gJJŸøí¢,;´NûR;g­Ğ˜mÌ³·¾ÌdÒ3šÚ<îRÓ[°#_'ÉhŸ_'äjI“:¯›éÍîl°ûú	Ä «Ñ’Ôç‚ è'	9î°<ß‚au.šèƒ»Ñ°L¦óhX¿¼0£i}Ş…m¼ı6Y½š¾e&Z“oÂA¤@å£Q<ªp*§ªfXÕ¨ØøÍ(z{©YJïÅ¶M3 ß,[Ö²½À¸ãu”¿{Ï<TåLw_#œ›pÄÂó[¸-d¦·¨„¤Q?;–»­“7N²6åù“ü÷™},¼ÁqÜsØüâñ®Á€ÿ©Â¹GqïÂ}Î†­•ŸB¢:ğ@Š"X(pXEo•ö~zK-}’^Õ(¨·Ys!2€ VİpÂb«®:cÛhßÅ‹Å=Ğı¹Çè-ôà	zDƒxø¸‚Gl´5.<´­6tÜGxºCiíLO¦é†TKc™ÔÏ²İŒ& {’.#£ÉHšlnàâ•Ît‡¹l¦ƒË\·k×ut#»í‘æTª9b/ïÉº¯=óÌ×èÖ¾mq}ıâmí¥=åfa/Úes-¼åV1‚•š5bå$«Õa¿]ü¼Èm¯GE^„;t5ª6©ƒêˆºGµª*/¬äW!Pó“Ù|Q,×ç_Èg'ÛQÜ;H[Öˆ^Ì·_YßWã5õ&—òô6Ÿ_Ä5+>[¤ò„-øOä_ü{®‘]^ŞëºUäÑ¸DõÀm*ät$nN²!AÉ+äëdN¾M¯OP>;a AÙg°ı÷s>¼7‘ğ4¢k:,£ÈõÅŞ§
¯3æĞƒ'³¢WMâƒéX‡ï<fƒdm™…xğú£øªZvEa(LÖËw¨+¡s²“2%›N;ÛÛ)»Òéå–şÊäŞ3ÊÂÓ“x¥±ñ]Î  :;ÑÁ›13–jniîàÚ:ø–7Q‰yd1ù‡PÓœ°Q_$S—‘H¦#ì¯›®hÚjJÄ["Ó‘Øµ‹³$æuu††Lƒ±Ôª
C}¹°¯±1S®­°ë¦×Ú-‡Î­Hå¶Âä—Hå™ğİ\øÁ¹+FÆbÄ!!B+Õf©¨çr›ğ`¾SçôÛÄï?çQíâéëR$ŸÚ•âä”œj¹œ'ıütÌ·¥I$Mi"¥gùü­-í©”|‡$…[áH}oK“D‰Ü´Úgñ‡%;*F˜J=0„ôd†:ªö¹èI_ÉPÚ­G=™Ï3òåóúéYQPğZ[¦•’,MZ¨ì©g-/ÌQcæM$s¼²£–ı_ÖD›{¾˜¿¥®ÂKûšæyj²¡%Ô6Øè¨f’ŞH×¦y¶¦„ä4–öÌŸMg±¨¯¬¨(ÚÉ¥+ÁóªZÜR¸aN²~`fTRUË@„¦Œ“Q‹a]‘ë¬æˆd‡™Hµ0SàlÑÁ~«(Û¼š›ÌŞà¾Ê=êæİ·8<à¾Ãnï°Ùe¥v‡Å" FeõIªTèA&3D!£O^½>¯ŸıEf2ƒú•§NÖçIEU¬èR›¼˜­vu/ßĞ´fÙ²µS?$­á¹³²îŸŸ«ûğ¡MS}‹Oœ wE—®Z›¦šß…ñ+ls<ÓıÔÔ
>
n*³ñÀAÙWy¹‡xnÓøÏI|Äã·Fƒîh0uØ«ã•wDá 3ŒA	õ%HmZÚÑ°©A)ºÊa±ÓWÛ%&Òj(²ö3]´z´¯¯dÎ¶¥KQÕzdûé|wQ}‘©84ˆ™qÿ½»ottZ(fÖÏMîİ+¬¢ÕÂ‘%ç‰Åb!Ç­¶7,¹À;we½?5»Úœ±jÙPıR-ÛÖŒ”™ƒäy“q3™s:I¢p«¤‹šc¥M¸CDö`«‘+úÙÉb€•¥-h‰™Hÿ/Zë»—¦¦!'cƒ²ÖÁ©Hİôå§ó4Û¦Zxµ0Yè%“è¼^§~'Ãl®ÒÛ^r_<5=Ô„õÒ
¼š£¾„êémHàwr1Ft˜×íšÑ¨5ÒGµ®hc´ëV­Ñ­5vi”mX=¨‘(%ş†(A§•ënÛDÃ®.è¸ÍèkŒÊÛdÙ'Ï×´hTh?â¡.ŒZ\ÏpUéc«ôcl‰ ÓKebÑw9Ûı˜PNOş˜z0TÙ¢ú¦óéoYÒ:AD¾BzÌqZÇïıqÉÇ=\²Ä\fS‹ÚŒfÑ#”Üex•ƒ¸¦y?o!çCí«fv­nö¸"5ŞMá¶%M3³^#”tïŸúŒ=šIUf£º¯¾³º~ÆíuÑh=šÇÊ¶Tmæ±Ú-¡äÌyáPKCÒ1sWª·9RÙ’‡²u•ö™£Îª˜Ç©6£M	¿Í¿4i‰ˆé$ºTØæŸ‡ºŸ-L¡´<¨‡rJâ‚•ƒ®Ä=Ü¿ó(úRb/¡ÆÁöïäjĞù„m1fc·å³üÃ<wO–b8Ë;(·"ÀIĞ˜.=¦Oøx9ˆŒ3Âb¨4óÉ¶¨|JÂ«©#aËò”[““iªqY¦lÔiégĞ¢èÁóy4;éÚ–rÀAhX‰Tos2c(KÄLk[ksËxÈ›ÏÿïÜº8«ºã³—5{-Ëf¶¯~5Ş"j¤¹:Ö¶w‘û^ø²Ä×²b®ªÅgÔ&»k«ïºÅnWL%½tv¼"õõ,À,’Å˜œÄ¥À@]=§0T‰äXšN7C1"_Œ¹VÉ¥,‚,`}D°¸‹U 3<G8ŞÍñ„Ã˜m’À<œŒGÜ Ü@3mcşùôói‚®sº¨âùôSŒh1Ù’ô~lL’‰ Iß9ğäà“ø8J
äY–¥7ä¼(r‚`“¸G:a)<‚Õ–Gš¬9+g¥™Á+ùb^Í6f1FÆHÀÀ­…üpª•n¯/%‰¥ïêÙ–\%]ã­Â#Şmá4h@_ö‹–`nd¡½¢ı³ŠdĞz½cZßõéİa{ßôŞµ	¦P•l	‰©Á ÙLe»{ç*ü9ÈìV=Üyl(Ø(¯p”5l£h¯r­ÔšTŞXÎì«®v‚H>?Ù9á#£¢R¥´)¼‚Í!ß`FQû“›)KhLÆÁ8ÏÑêñÖè	ÑE¤;±÷êÑ¢G`1&ºÆ‹ÆÃUI³Ÿ’µ°˜Ä§öÃ‚ùĞôŒ¯uw*W6µ÷×TC*@–X¼‰ê„·U)g&Ü5•}NO¤iv°²¥¡¶¾%&¨‚Ûm®¯ª®Ô¶œÿÖ…Ì…Cÿ¹ÿ0Ò¤VÂÛ¹¯>ĞCn™wt·½“¬ì$Ã-ä®rwüÁ8wØOvú‰#¡*÷Œºë"w¹pqã.²ÊE\G+Up*Èš
R1úñ®ûº¸±.¢uEº8©kõòÑ•W•s
P¹E9Š”ÛŸº9uWŠ¯Jµ¥V§øÔè«mäŞ6Ò¶j`pLŸ3sé#ıŞùcÖÆÌXCz'¿…çñëxn~~sJh™¥qÔ+P ÛÍtf_)¹ßüŞóXß;YÂğÃyq4¢qÈ´Ó(ãrIV¦ª¦Û×p{.†dåô„åûÓ-5êUXM%ğŠ÷õh­ÃÓiZ:+½²5»Òëqªüjİ²÷÷_;<£9?ºxö€"k²k¾°¿·gßİ+–İ¹;iî;g¦³Všæ÷¤šj„g¯joZÙ™Ğ¥©¢Ä¬şTçU+šf¬ûØŠá›ÖÔ;,­ìÎ/î¹òş+Z[¶YÛ³cAb“ø€ú+Î2<oÁ
Ê_	áFøàç'ACÙnF½Ò5‡]5TQ²ÉŠU±ø¼Õ&ª:ÉböY·U¬(ÛN—ÛÄxªå<•¨x¼ÏPİ†
†iZ æã¹ÀÀ}-@JI—Ÿ·ôm0¯2GMŞi:MÕèV»”.k7Ëƒ‹.•oj¶ó{õ3z^–]øh~LÒÔ·NŸFüKÕla‡éH:Ö@ªb"£²aŞËã™ƒˆ\ÒëSg:·VÏŸ×X“è7¿ú¹hge¼3R¿ºşÄî§:ºhÑÑ‡ŞMÈê/.ZôE:ª°ªğGn{éUƒyÆØã«MÒ´Ÿæà¡÷qéì =ÈÙÑ~è‰ıLêÈbOÑ—¡ÎÓ!¬OzIÏ¬YÔ—UØÈ€æ>á¡ö™-‡WíÁš°*½È!æC'Êog–eL|ßBcQÊ¡LÓ1´yÆ‹Æ´Ô€ôÓãBVMO#ˆaÎ˜Ñäv7Íh2çì¨k­ŸÛwtª hö¸7=0+˜ÑS{ı¶D®1X1£;™¬5¬ºî>ÃLgz~¶½ßé\²`ÇNÒÿ{ú]D¥ÃÆ
u‰¨†kü*‡öfŞà–£õ¨‚×rñšœêìÛÁ“°„ÉìXğî ÇÑ#¦cº¦UÆkÔë£©PJéH£À~Ş"°+Ÿ AÙ±j¤íë9·Ó]İ”hÖk¢œ"Òh,IM³FïğÓ;4™&É2äŞJ­ªŒĞÛèsô ç¢ÏFÅÙµ8Ğ0Ø¸ŸOC¿L1ëídi0;$úT1ÖÏd2Ô»¡…Î§I>-LS¯ØÀ¿Û:ğä†ş«[ÖèI÷f£Ö
[e:hîˆ…f­5oØã­}ZÓec«W]Ö¤êºeĞêpØR}ÛsÛú«+”AAsÈTo©A)Ô!7æBnvÇ­#ñÜ³¸u.÷~ÈÙØ¸Í;tü€éhŞTşàX$°Oz(ğJø”÷ªÕŞ AébÇjã$PÒ	óY"›Î‘Ê şVºHƒtº˜î£B	dŠĞÌ5EÅÌîÈÌmw¬¬İZS³µvåÛfN?\So³Õ“ukoZeî>YL¯¾iê3·ŞÎ‘ó¿¡ŞVaG=h›hÉ…D^“#2'Év‹´R…ƒ¢Hl•nş é¢Ã,MAÆ ­e}şÌl²À,ÿ¬"N}ƒTN½B6p/aèÜr(~y‡ÍTçÜ"¯°WËÅW_xñÅ÷şRc¹ê[$4õ¯øÂ—–M}›Éûï¸õLŞ_zœ%T su(½6:üàõTí#9‰ à5r„ ¿¬©É!kr
²¤†P‰¤ár„Å9ÈÈ~•>¡R Ê©”EôyõXµ—İ…Ş ½7pÈ DôPÙwPaö”wFoU¢ôV:”ô$Ş˜8Ä‰ÈÑ,fš biPŒr]fjeû-„É3™RüA²†ƒ¿[¾Étù&ç7ªõ³ç'Š"~°·±¿9f„F2-«çV†f¯];ÛNVN=c‘e±é²›/ˆøË_p›¥Äx¹ÂCâ$h$ Dxˆìã²pİ@ç,°­ç_Ë§é€³_µq#÷øùEôi	³Ï/âÓ.8xx¤…}»NŒ}.ªtä!Ód*2­”©Bh2‘d·³KqP2‡è¸À!™‚Ê5
M=I*iµT!˜¢FÒk’E’¼bßÚbdÉÍ–5ó*Û*å”9/Ó×½ñeVu%ÃeĞbıkÈó¥sWaÛğ³ÜH€²|ã ƒ³ën·“Ÿ¨ä'yĞJŸ”¨âì“ŸR­ğ’²Ïf“=ş€`›HxË© ùa€ö™·ij æW>´ 2“F|q“<(È¼\aî}Î‡‚®S:Ñ¯;…ÿ‘I4“˜¦áê2ºå"İ‹¡{Û÷Nîídjz‘OŸÉçÇtæƒó{ÓÓ½/1²>}’R½j'¼ˆ>8ŞÀWq#‹^«[Y²rE2=rÙPğêğ’Õkj7nŒ¯XÖïç¯\¾zE"<¼eGcã†ÕS(S/Ä–¯•5øm¤˜ ÁœDË>î!+ß%$İTu™:3£)‰êš5ÈÛS6®X‚r/>9€Oâ“5dáIH¢ã)­²}ŒJ€Óô÷m‹=ãŞ’Cd[ˆøé˜*^^í'>ªyíxl3É¸ã·ÓAŞ¶IòIÜ$dÓëwT:&qãÙ)‘Õ<ï20¸1QÇ´öÔã(wéc6†aUd_˜ÊdB¶÷…+Ipßä¦ŠOWpK1^®ÙOS¥[ô£ú1×é)¼QGñÄGå}šB$åX­'÷yÕÔTDº+º‚]FW%úÅx®RÄg4ıdñ„HD6™·~	é]2º&)gĞÉùKGéßÂü#ır:ÿãüù³‘ÊÌË(ğ¯¥õÉ|>Sd&†f%²]:lª¬Ü…0‹îœ®xŠ«r"¹]¥Ò©˜¬8„Ù®ÙV;:fù|³::‚++‚C)İ1â[¸jİPÎØ?5yÛÚ'O<´¨îÀG?ÚÚúÑ¨›:1õ™Ûˆk¿‘Z·j¡¯¬572¿+s(O®Q¯`’ºOWÜº¢ïs²ÌYRüyHz‹ù1““Ä}¶‡Ü®î[ÅÏŠÜµ"¹B$kEÒ/’éŸÒ¹MúÕ:ÇåôAsëÍ:'ê’AªÜ%uC1P¥‘j>¿¡”'0qCIG#zMã,“ÈÇ*TÒ‘"(†ÜO{÷‚ùİ¯Ø™nH^¶yÛ†ÑóèH27İ>Ş‚põñ4zz½‰ªˆø¸3ª3ğ*¯§Ii.„­5hdHlÜ˜¯K^ŸíKÃlôœ¥¯&V„©oS·Ş_4‚¥;è>§Ñ©$jåc5çjˆ»ä@ØiH.ÆÔ*ÓÏúy@]«ö—îd{¹8K•à‹ü‡´ùqú™qoÄix?$ô¢š¢Ü0˜æ}.•f‡.Ì¹¦åVÔÂ¶M2£ÎhVËºƒ=ó®YÛÒ²öšy=×µl‹Î^ÙÒ²bv4:{EKËÊÙQ²nÍøº††uãkÊûÎí}UU}Û;K{]!ùçbtå€
XF}Ğ¹Gílàuº§iüã¸÷ígÄôÓŠÛŒ}ÊC!çAtr·¡R1gf‘{1~x‹ÆÔ?ĞĞù-—&(Ä[)å.ÇŸO}¨`cÍÖLG¬?3Ø´Ìç¹j÷œ•-¾©÷°,®ä§ÎÙ#­µÕÍµ('˜œ„!C”“`/Né01Ê"‚y·ıÿQ,¨ÏÓöPCcŠ*5ûeÓüßÅC½(Í‘ÒÈ_¤,‘ÿF6²,ü ÑvâFcü'ñ©À|÷!³<eÒ©-Şl6èô¾†CÅè³—M6¢D°øó¢ è¯Ñƒ^ÒÅaê¢¸äÉ{d…:ŒÇ«øÿVbªlh%Us&½Íšm{–5ıáYríš6Ù÷é–Å¢75»Î’]wãÊ¿,I›Q’P7a×(Mî‘È-è8¢$öƒ¯Ä_ypÜGÇµ|ÔLÕÉ
,ö	Ö}Û-cÎbjGj‰Úg<T
2Ãp8t§Ù«wÌeÙhÛd9IÌcvÒ˜/Í³¢$2›&%×k­,É_q¶•Ÿ.…ÇôÍYçåîÆ¦F—=èXÒX{çÑşŸvÄz©D†³½¤ÒİµtUujÉ‚/™zƒŠåî]½›H=?õ'¹"[[ÕV©ma4FÇ›H$×.TÉA$;‘SäîJ"D0s’£N2î$Î$Ä(YbaIˆ	Ò¾pÌIá°äö'©|”&0O=¦8ØÁ¹ÜF”¿=I’Ì÷«:µ{>ôÇ*»Uj]Ô†úœäè«Ÿq@
d®0 pŠ@¤…Iw˜a!¬-h Û±•‡ê©˜×“úêù×¸îvqt¼ÊsÈI?ÅÀ+7;ïrr×8É*l§†Â˜¥„Dçñ(±<‡G+ò	9[šâ¦NqÒho× $ºâÓOç™ú›ícÃş|qoztí¥}Ör@ùö=Á†Ù±TO&thWçv_Ä\ŞVÑ”0=Õ-ÑúEmá›Öô¶V)!ïúŞÑú˜OµÇê;êÖmêKí~Õ—ôW¤B>Õ™ÈôÎX·IÑë =J9¥£¤ÒxH„Y¹„m”&'€‰=¿oÔrÄÂ…XJc7ßM¬i,xşº¼³ëógóùó¸a EÌ8ÊT¼…KştãO¹ÇWœ¿—Û¸‚¾}}f^à…5¹„"nRà)pô}š3âä$çCş{ıDÜ'<ä3º¬]Ê!–¾ª¥eJ9'Ÿd	ÀdE)%­gÉ7:ØÒà=rpd¸gK.²ñ²…É¹u¾‘®ÍZmÿ–YäÑ©áë½M‹šÉCS³¶ô×bib}3¶Ñ	ßËÕä€N¶;H›}}ÌÎ_£’§d2f#ld&é#ÜËÚ¿kÜ0!i¢q˜æÔTç>Ü ‚Ê"3MU¬šUİ§Xİ
n?¢È)ê
’Å ]>aŸ•šé
Z÷#+±jJDá$Ååì*‡	å˜»³Hé—óéóéôËù3l_X™•óéi‰¡0±X¥B#mªëYÓÛêlãnNõvwU®«ìš7?yEë¶¶-ÜãG¹¾0õóFIòØÌ
ŒoBZDÉú\bf”¼%j»fFÈis’ÿp’kldŒ#c„|HˆÍ6 ş}(Dc‘ò¹ÜJJ‚ßíß¹¡û*IeÀ¬„ƒa®Õ ·Äm°á6öAØá¨›¼è&n¸ÎB¶£"1"Z$»´O´¸EÑrOØ¸ÚˆAçòÉgtR£÷ëktŞ­^·ëû€§_$Úc'¯Ú‰ı>‘°åQ’w‡º]n;DñÉ£@ Ùän;±“û
;v‹nø»¤.±ËÒÍ—¢»³§ß±ØÖÈ–y÷¿œßë{¹áÑ8§`ãxæÓŸËï-_ÄğØ¯¿ì;“+]ß›¾0¶¼—>¹—8ˆHd.Œš	‹šiİ@ÈKµ«Ò[†âÛáhÔ¨^[µ¢ê²j=	;6'†š7Ö­ goş·+’ß_ò¹OŞÜ¾óO7ßü§3oşäç—|ê+G¯ü7ä¤—y ªyÿúè}~Êô,ªŞwØMx:4v3rÁ%{uÃ©xu‡SÍæ’—Z)»(©1Aw³*§âÜç’ñ1——€Æ–úèæòuöè^Tipc ™ózG¼7xïó
^ÿÇıDó7ú9­$ê>o·«ËÙ¥wi]
M1K¤/óJıL9µD/N©+ŸkXÁVÒ´ÓJ;z$%Ÿ’,ô$oiµ™V¿¿uFZ»¢şšy¯ìyøØU?í9Ğî_º4_º´?<üÄY05E¸©g7>µ©fEª"Õt¸õ$(Ø¿e´S’"	Ê>Us«š¦;¯RïUQyÅN`}–”Y"ì³·…«à^6'¦Y"N²„hšª³qn¡ËÒu¡§Ôi7–:››¦Ö>­ê#;VRn:øÔ@ª˜ˆ ¤ àê½¶õêÔúÌŒõUW¶^ÛC<W¼¸eÙ±%K-Ûò£Ë§^g{âÃ˜0«U‘ËN¢H9¢­½&E$N’¼.Åã×Aw—"JmØ¸ó™ç:Ï?—%ú+gèˆZ‘æ¥im:¤)Ïëè² ÎáÛÓ×Ûá'7OÙÌö®ù½]Á©Ï‘Ÿq;ık6oİR¿¼«zdË¶õË"Ë±M#…¤‹×ğÓC9;'ØøQQ²ŒY¹1€ÆI-¿‚®óÚA‚ÛÈ?>üÏ¼Öÿçö³ğËòÓø¨ú»>{
_@×ĞµdÑeIŸ>ÙÏ·öÓµxÆÏ>W¸ãËÉ„ô/q‹0!F¶g4Ñ~YÈï§ÔË—Òø:]x“œâLÌZà'9%Fó—:ª:4»¦sİNjÃ½f¦„5TjFİ,çt³Qš1Í¤‹	ÜÇÛ"m$“¥ZèUXœUoŒ°#4»p–Âè ]Ø5È¦iìi­IŒ[Äœ“°ä]ÆğZÌQ¥d§N¼E5ÆÍÀP¦q<«ÒÁ½İJOØdÊÙâ”ÓéL1Á:Ÿ>uaõ]2ÓÚÖR9<.6¿w¼ïâ
$‚b•5äú¨ÙXÈ5Îht«éÖÎHİÂÖp|Î`#t[ä@}¢¡×Pœ+æñ–Ï
¢ÕfªÈß‡Zúë¦æD«à¬ÊÕ§;RNõ&à­›vq 1¿ç¼„8ã£ÅˆøÕ\ü4#ğßH××HôXÒ;,–ãİ£úñJç—g\·—Í–½´4Ñ>ÃW<I«báq ¯SÙ*Æâ²ÁÒJ6ÌÏ–¾¼E‡¶Şby£’ëÂäkq¨»Í(î•¨òU£·~æê9‘dÏÈœ®-Ñ¼#›Z´VO´W§ryCñU÷m™Ó¹u~Êiã~©Ÿï·ˆ›×UÏÏ†”èlá÷äY”°<y¼Ål“š[ºK{şÂ|>Œ´‡(ãuÕÓŠwÆ—Æ¹xNóô1aSñ÷*>§)[W(<\é0h´eĞKÆ¸½8/2XÁ²u{1[/ùÇCæ@†2™ÒH1İ‘Q0K?›>SZG!L›K“§=2º¢ñ\¾=>?jšm‘%Ë]5¹†äÃ.…Siµºoóœ9[úkTûRYİ´¾v~&è–6Q`+O~OÎ£,8:_½@ôJ?)íßyLA=(C=Xã@!`}×Y—õãq‰›K7úÙ9ßdaŠÊ»×ÿp%”eøq*/9[Q`
£?
2n¸‡ô%h½Ù„š)İŸ?U$
¹ N”(/ïD&÷¹Tu{B_»(•uä£[ºæŒô$#sVÏ¬ï5ÈgPv~õºÍ¢…{P?/Úœ©ù[;çlé«ö)%ªü%& qøõIL³Î•Ù÷hIYèŞQ¢’X^ÕéÓ‹c §ØŠ+ky,È¹Áu•‹so”N.M^•äâx…*MüÆ‹s7#”x˜×w¨–¬>œpjìcğó´qO|L¡js¹a±¢.6ûI×{†J#Ox_x\d@(ZÔPMê“eùBZNÒq ÉÓùÌ…Åq’zYA0ª#Ófİ“­)¶¸4[İ½ª~ç2õ9ë²Õ3ævcekÏæ\„l%]íÑ•.ğ½Û{*?z³Õ%­0¤%6wMßæİCşêæ õ˜ƒ·¢Ä¹ '³¸ˆ$:‰Ê›²­‹[[hSP{%J@qœgj‚Ö–Õ$SvÎègÏĞ¨d}\P‰É²ü¨¹•kf«†Zíjşş÷ó›xI­Ê‚9õK¦æsm[v1÷ßq.C=üçI¨.r´ªÄáx‰³ÌJèlÿ:uEÊSôã\Î®>4ú¼ÉiMs«$c2&WÉ%v¯TÖ‰Î˜TwèhÔ‡!=Üà{ÙP`ŒM;.‹T¢Á¬Ò'êkÇ€Æ‰‡Æõù¢]-®ƒ,ó—Mföüé‹Ë±’ï]iAW¶”çQøwYr—ÚÛĞ¸¼#QÙµ~v×ÆØ¡¿™±:jTÕ-ï'ÆêECŞªl0Ùál–üáÎõ]íz«\ÒTÓ+ueH1ºûÈ=qÓP}®Ö,ñı÷Èw?ì¦«Î=]¤[y¢Ä&ó¨ñU•FQåxp4øÛ ·4ø­ ÇùFáxÀ¿P]èsSı¢ë}¬ƒ5thQ6ò{i·‹y+Æ­Y´%çB¥£´JÚÌf‡:–ÍpçíáLR‹†¼÷>õ–¬Ä;‡[¦~Nô¦Z—E°rSƒ4Né€op¯Ò²9İà$ã8‘ÈqİBÕQQ}–[äå\?,¤á'KËœÏ¼¶óÆ,ÆZUåeD¦ÛúÕ|¾Ñûqã¤õ±ŠŠİğ“
ÏzÙ'i„¥'ÁQxı1«Ps“sÓ±¾â¤Ğq¿:êâåãlÆ“ã>ıÏrª=¨7ËŠ££Å&œÎ–ÚN‹ÙM3x«kZ‹5eWå€ÒT“_WWjÚÓVa1o™İN
SÜ–|ìb;‹ı3r4 …œiJ&‡EşY%j
5…Ì¨ûTz¦ĞğÁ¦ûh`Q^ÒèÇÛé$ŠÛG³½¬&µ¯A2`²)u·I›Ô¦Aë êñÑô‡Ö²(#ˆ¯2Á£ºéÖMĞ=:¾Â#P¤N‹Æ|t8 Wi×û„
]uzúuz5]·šıÚ;Ê“u¡°ğbÆfóŸ§XHw¦˜3”S"6Ú7}äœV–GıĞş´Ñ	·,ze5<¯k–{—Ù6§£"Ÿ÷Íš™qîò¶ÎšMÂŞ¥Cñxÿ¼™®?R‰KùfÍi3ısæÎeß¥zş€4U`nÎE¢Ôè&?$ŠÔ[lgV_—Ô>åa”?®
K”qB0«x>ğ
€6ÉÛ@Z°-txë×«úò’3ì‘¹ù¹=úù#Ş°ÓÆùÇ£_‚zËqØl3ZtnEå(MŠàşÅGK+‹Ë¡
·ScY¼Àâu•e²:å5ßFƒvI§ã‹ÖÒ`,å{ƒPzƒPzµ¥tŞH](5ô ×†¦±ñ¸ílıÑ­ÑÑàÒ0ÑÂD
§Gë7Ô-Œ,4¦S© úÆày+m'6ÇªPoKH)F¡Y¶-i,9¼5ùóõù½™óí?Ï§'_{×œÈ´ÂÂS·´¨lGØJ éF%>İÙ›éñŠáºÖÈœÅi-oó§+ç*’”—ıé˜#òYòä’3œ†=n¦¦¦¡»ÎôËÊò	Ç[ÈTÿ»‰\òR»i¥QvÊAÃL;å“µä¢¦÷õ\„®Â-åÇıßòsÔ{ÜçYh[hêãP\^ËËvó]£}(C®¿`4±—÷¾Ûh²ŞL7™¥¦Sû_\£(Dà#'!Rô©AjÆ‚4œª¦ã”ÜtBÄ}#<‘@9¨Ü(3? 3? ?õÒÌÏKMw\•fLB¥…5¡qa¨íL–&»ŠN™¡dÚÒp¶™-¡)†\0ÑE'µºåıÆ¥==KéF,[ètÃ–¹[é~ëÜáíÛ‡q–I-àÈ=_›¶Ó¨K¥\á|tíUt¾ø¨ıB†¸¨ã%öBcFH{8nõúWZùñ@hĞ·Hdş]”Ç½ìÀë*/aíÌ–æ¦Mà±®]XD‡fÛJ)”/¯:¹vQm££o,ÅÀùØf~İ&«eê)÷VÏf!ğ‹Ü	É…qYş`úM«à¢Ô‰&Ój×¼Ú™ÉĞÕŸÅÅ i‹W°E´	DW#a¿UW²Õ¬”mâ\¼ pCEá¦‘ß©&~J5FÜw£¬Ô“Yt½ÀOèÚàdy¾Jm²•VåØ(]éòõœ†¤LùhŸ¤´¬,ICeék\ôœ}m/&¹ÙŠö%¯Xi	5],¯±³ïóÉÔVQ3EW½³°½ÛEı˜“MŠKä»$!–Â±QArRL~ô^q%nìl$Q¥¶!L]a˜Š%µma[no––Û»±9i¯­r{Ç]*²âVú&Ñ_9Kòtş›Şø‹ö©è™ØWšRåIl˜>ÉÁ¼ÿÚÛZ;ÂmÕ¾mÃºTH2´\}Õ,{°º"9«ÆsÅæŞ%CŸ?/«¬ö«şÊ¦xï Jü dDbFÀtÊ`"›ì[èµZÙ……7ÉÜ1ú—2sZÄßèïôó®(åggËîë³û—ú	ï5ûT›Ù¥Òm·ë‰Óé¤’>äåÆ Õøy6P.Oµa*œEYg_#}ïz`£íÁçS}	_mVv:æ×·ôÖyNZr®*R]–Ñ¶.m&/êå–ş†“À„Á\ÌêÃ&®P‰kT3#&'™Ç½ßòyT:îq÷Ûú]&hôë4šì›€üPy©Ş»m&]–TnOy¤ÍÈ’ß ?˜³,ãÉÏY E+ĞZjh,s«[HbêÜ†eÏsäÉÒüy£c2O?¡1™SŠh"I‡Ä¬”>ôklŠ÷ãvB	ûèœî>¶OÕ÷1Q^èòôÙvÉ9JÇê·K¢Ån‘F‹ün:dÊ~(µ–GèÌ“ná,¥|—³_êû-ù…”	Ó'Fòçq›>/R¡Âx5]ÌÄ¬—‡Ûù6òZÕÎ+fì¬Ú¢Æ’)ÃH%c*'İ9õûË/'ê3®Úµ­ºzÛ®«èwÈhNßÆş'øæl¹	Ñaóm,dÊMIò¨·¸XµØË¹Pq…júiÄ}¥ïîælt–±eG6Âö¹LXœ ÚO¹Jr2Ò5— Í	’`”¬íK0£Mö] ¹Ä`b$Á³*ÍåíKDƒÑÑXÂK¤bôv¡FåÍæcA`ßÆ!Åä}¡F«2‚N?è×y€Nú¯ÃîF«Ó}çü
È?yÈg0'r=ppiİßÁÏ€÷èNÂÈshxP/÷øì¥*_î‰z¼°Øƒ‘/­{çQw‘j9Ú5–¥‡ñ J‡|öRÕÍØ’V±xÈ[òor·çI·ßC¶xÈ2™ï!ğ'<<AÏ(n:ƒKƒKÅ‚¼(aCDºÂOd©é»±–Šd¶HÄÒRŒ"¯ÉR‘~˜£HCÓQYtË²h-QŒ]¾Ïê+§¦‡EŒçsºÙÁ«4¥¦÷?³ÂJØÔ³*İwÖJ>f%û­¤ÇºÅÊ±j~ŠIIgêørS²“‰Ge¶5÷ ~ˆéó D‘p¦N‡QLJ3ŠÍo5‰b’?˜ä1ó´Éİe’í&Ye’…¬îïÌŸ™¿2ù“&±šº9Ê[İ¼µ“_Êoà¿ÅÿˆÇ üÿ[çsú‹:7¢ŸÓ9='“ÒâÚdba¬?Úïéê	lÑ?¤si|'·óä
ş:ÓyLH”~¹_Ä„.&$íÅ	-6KVÔÈ½Åi²‹saù½¬\}õ4¯@+ÒåŠ³hX—.ßöîé´¿ğ
,åú‹ïòë/ã£gÆŞû¾é#IôãcÅïL³åÚ	ò‡ŠÎ@ £b¨a¸j‹\©ÔŒX8(Øá˜¡Å¢òHÕpCßÉ-[Nöm'ÒÑÆİ»·¥w^±½¾~û;SÛvïn<:õÎö²õœDëá…c¹Ä|7rÓ½†SÑ½ıâp*gİ4(Îº½{²m´<Ù¦\˜n¾8Ï6Zœgóú/Nª-tõ;ûõ~­_Y(_äSyRM?saFí=jl>ìÕ´½3š¦Í¥Ue½mY‘Î¥)ÑTµËUŒ*#ñM_ÙyèúÍ5m{ZÛgúıíí­fÏí¹·Ÿxâ®Oôb¿¹Bù_Øï(¼yüÅ€-£DQ¶øµ›¹qª•©AiVn‰@ÓˆÚ0ëwy]ºÓër
^	áÅóJ›ûpåğ—„¨‹N¹T»&k’hµY£)ÔÓhUmŸUÖäQ›Õm³
šf‹Ø8É{Q{U;§ñšUàÀGƒË(­dt§E*ÑIoû^F)ÿs™1ßEJ•–´ú_f’yæâd^š£´¤!&]?M—E¦½Å1Êi¼Vú½x¶–Ã¥`2ŞáïÜ•Ø¢DRu¾ÔLÿHb8ëN7wÕ ]–‚mFÛb?\¿c÷îìÎv}rêıõ]µn^°rTª'ºtå’‚Ãæ¥«„âŸ6°ºÀE$Íæt€6¦÷Ûë˜ˆ‚pşÛtZïÛtZo}^%_ş‹t­ ›Ïc_ó%ÇÌŞ¥˜Â†§öùæô§
äòïŠm{²K:ê.ß™.FŞ\”z!£¹>¹F“¸m±¸ˆİrOø 9óO$÷$ïKòZ2’lLòMM°uNÕÙç»%¼ÜÓï^X^İ!9qœÃN.…Î|f2OVË#V“™õù<¸:›Ïœ)Ï¨ÿÅÖ÷Œi‘`<£Ø•T°8ğJ>rqŒ‹—l–A‹íâ ìŸß™6ìU(”{ËYÉÃì¯U õ'ÙŠQ/ˆôY,`åŞbepã)²(Š’Õ*oEñ”l¢M´
¢hµ€†÷X­øÏ[y}Ô"V¥Vø?÷'6ÿPDT¥È/	Šü‘_‚È
^y
‚"JÈ$Æ/ÉªØ_’U”D¯Q~!géıøå­dŸHùe½Ô]|_I»*RF	6ø+üRQ§P™lÀS.ÙdI–ğÌv‘_X-I‚$ñ¼h¡Ìeübúw©»ø¾*HXÍ!QFYéFC#’íšÄ
^–,¬›,+6LÑæJvEµ©¨o²Í\ĞŠ Q†Zm6—,v›ÍÔnŠ˜+Š—º‹ï«‚„Õ5ä—Å"*Pä—òËÆ
^¶Y(X5EVĞ*È/™òKVe<³QÎP~Iïá—|‘_Ò¥îâûªÈ2º2ªÈ/dä—(³‚—eQWY¤€€\ÒT»lGî©Š&ÓhÅŠüBám²Ìó6‹FE)S~~À¯ÿÉ¢(àrÉ”_˜Î u: 7(¬àeE  9íªêPd;XQ³t‡¦jªŒ<s©4Z±‚dª€ø˜Å":}T¤QC-¼Ô]|_U7å—`}¿¤÷òËe·#¿Ê/»ìÔtU·+²Ãî²«ŠÈş(²QU$UµZe«SÅ×¢T?à×ÿt±ÛÁt+”Q6
4¾§üRYAvªÉmwØ5Uq€s?ä—ù¥2~©E~)*LÆ/EœÆ/E–/ußWÅá ¯W¥ü’5<Åì˜aÙì¬ ;íV
6¦9t»ªUu¨NÃép:TUwx5‡]¢ÿ¼Pûv|ÌjUEd®ƒ:4»l¨²r©»ø¾*š>Ê/«(ëxŠq<8(¿¬ ;V
²WÓ4Ãa×‘_šê6œšK³«†ürP~©`güÂÛ­vÑCµ¡½T]ªò¿ş'òËï³3~p‘_ò{ùå3tİé°`EKèqº4—Îø¥_à† ¹Ì/|­Ìø…öòRwñ}Ut‚Aå—âÄSÃM´‰rñOi#;5‘‚p†KÓœ`uŸÛÔMÃápéAC×0K£ÿ°]š&ëšÕê}:¾Ã]5ªıRwñ}U*¿$ÕE~éÈ/EgÙ©‹” Ëi¸uÍ¢Ã©ùİÃãÔ4—+è¤Ù›şk=ä—‰¢&ùuC§ˆn7øõ?YœNU`¤!şu~©.—Ó4tØ4ä—éuz‘_nÊ/cyÊ/ÃnèŠa0~(
ÚKÍaÊ¥îâûª¸\1~Ùİx*Òñä—j°‚êgˆÔÛåB~¹‘_h=È/—n˜® «È/Ğ»9•òKG~¡¨ğëÿ…‚üŠFtªXvO%ä—S’%ÕÉ
ªŸS¢`›¦Ûë4<`ÓİFÈëwùİ†ËcFÜ.'fÕôß‹bâT].›ÍCN|-fgNÃ¯ëÚ¥îâûª˜&Ä"J6‡O%:>EGt]¬ ;]{Äcº}.'òË0/à˜N—×Œ˜.×4~ÙKü¢Ú5»ËNıRwñ}U_ñ˜“*–æ…"¿ÜtÜİÍ
àf£àˆy½¿Ûå›ÓãŒøƒfĞã2}^ÊF£yœ2ºx»Í)GÜøZ‡îp»BÎøõ?Z¼^HÆ1Ò°ÉšOm˜.™È/‡É
²Ó´QĞâ~Ÿ7`ºı`sy]‘`ÈòºM¿7î5MÊ/'¸0d4ñ1›Í%ÇL†fºPÓŒKİÅ÷Uñù •`üÒ§óK{/¿~Ÿ/èq@vùÜ•aoØçö|qŸÇcÇìËnÓcj,»•¨ù¥šÇq¹—º‹ï«‚üªNadhSŒ Êv;xe#+¨~^™‚
ü!¯Õí7+C_Äoú*IT;Ê/7˜>—ÏƒÉ²©TzñµšS÷z"n·ëRwñ}U¨­ÆÈPVx*;à£3\>V>™‚Q]„}Ş
PÍ€'‰b/¨
ú|öïFĞ»ù½ø˜,{”„Ïïİeø<hİ—º‹ï«BCFŠİÁSEÓ @gL¬ ;
W]$ŠüP½!_u,Q‘À 1N‡³//ø0	8ƒUõÙ«øZ§éø>¯çRwñ}UÂaÈ4¡çRfOéß>«Pª«‚ÀM¥ànŠE#‰P°ìşH >Q®Â £2Ş…tŒæıÀ¤Â
ÙíG:a â«~ß¥îâûªD£ĞšEÏ¥jŞÚ1Gcæd²öFv†í<ÙD<V	%@VV4VÕÆjÑ‰%“ÙÊH³jBEÔ›‘ˆİ^áhŒàkMŸ'¬©ú/ußW%‡Ym!d”î«ÂS&º1‡Óá)şhÀÍAÁÛ–J&jb‘*ĞC‰p¦¶>^ŸˆTVW·&+c˜UCÂ•ÁÊ¨§2¦ia=«¬OÀÕ‡CÁKİÅ÷UI&a^®0š« ÿùYÇ@<¥›z Å
à¦SæêÒµM©D=¸*kã³g4×4×&ªê;j«Rğ@âU‘ªd *åtÆ]sRÕUS•Í•±è¥îâûª¤ÙÿhşK…yPa²°¦·ßSü/Âù
ù=ıÿÀ¥òXã†ä~èã>Kÿãî´òô‘X‚['Ê5C¼)’† îg’
¯c]·<n3qkÃ­·®ÒısJuYzùå|
\üĞÅİ÷QXÅ]	³¸à~6n~ÜîƒY¬ÅvX…m–¸c«øí0û	îe¼¤´§×ÜãZ@ç&`ˆû8ÈüßBwx¹U`åæBŒôÃ{_?°uyä×…?³6Éæ`¼YÜg¹FÈ’aëÆãÙ0ç¡ÎÁû‰Kø<^ë úWHèıƒì]x?ù&T“;a!^û¿Û»šß6Š(şŞ¬í¤P*«U‰½Q%RÔÄi$( ¡$.nÓ$›0%Î‚Çë&–";x×€)ù(`1NËGÃG‚Ô´Í6¹¤\’cáÂ‘c'óv³A©Ê? Oš™ß¼÷æ÷fÇ#?ÛòìÅ?!¨€ÃX şuN—ìË¾ìË¾ìËÿÎQ÷–³ŞB‡`	Á_³š à—¿Áïæ¸Cpûß\×-Fàq¨Â'<¬Á1ôyØ·ÇÇá/\½èsşgz.yÙgÀÃÎŒº<¬Á)Î,;Ø·ÇÇïæ›põ!hä|ØÂşq2†nÆqf6Î|A-×z!ÉÖûÇ!Ëı]ûõ{Ç„™wò¬M±Çë$gşgùfFaöO»‘Spç!½ØŒìè“l7¹6XãğŒèó%˜cÄå³îpıš™5t!™5S™´5l9µ2éîx|¸Ë2•j(—¶r²79œg]ïXÂ™±|65<bÉ¡æf§3éT">*yt£”]©D2m&™KÉ¬´F’»Œ‘LÚÚ1'’²¹1ä¾®T
Ğó_{î.j(Ö
¶=ÂNr	¡ó”ñ(×ƒ\De‹íO=ÙàF¡»ˆkË$t6)C<Bmb5”±
¸=À­Ÿ[¯W:O°Şd¼Í¥ÂE«l­WêŒ8§7ë*ÁÇ"Ûë¿¯WÖµÕµÍ5Ñj—íE[[½yíVõÁHğæâMÑº]\Ñoàâüa©š–¹|¿t”–D}'4úv!@ß,<L‹Ü~‚ĞO_¡¾œ¿G_Ì¥Ï¯Ó<û^§é3q‚>«£OæÆéãkËt‘®bÍa-•Kgè£’A=%Ì”&Kbµ„­¥“ÏEJBĞìL}83N3|É§÷‹ÇhºÈKW”ÅPQ‹‹Â™öÏE^®"¯Õ{<±ÕÂfá—‚VHïNÕÒ;W~¢·'—é
Ş£)ÔHNâ$ÓMä[hüòÓôVŞ Ëâ8½Éá.æ3y‘‡é«–^ÏMĞk¦A9'‹¯mĞ3EĞ”æ–©™LÈ¨W'ÆÔˆ®«aı¢º¤¿¢}@%ô—ÕSıáê¥°R}ånÕ[îTçËgU´Ü¡zÊçTÓ9ÜìØî¨th§õ°Šèíê½MeÚğÅ¾„õôã–;7´ßz;íê¨nã´ıxŸS·°Ó6¨½ÿb)V˜…öúN»¾¯ß^¬uÚg´:`ŠÔß©ör7LóÛ¼X9@ƒµ«ğú«kD·Û`:ï(>ì½IŒ×3-Ëä N7ŒÃ.…ó£Ô?…Ãcr
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
xœ]RËnƒ0¼ó>¦‡òª„ÒHúPi?€ØKj©Ë8ş¾ö.I¤Z²W3»3¬×¤U}¬ö,ıpƒlÀ³Nå`®N;ÃE›DdLiég„§ì[›¤AÜL£‡¾6İcégÈŞMl±WÃ’ôİ)pÚ\Øâ»jn®ÖşBÆ3”%SĞ§×Ö¾µ=°eËZ…¼öÓ2h_“–!ÔŒ¶•àZs¤àa•¬8…U&`Ô¿|Nªs'Z«W±šóõ±D”:E$öUt:pN³fwsx|0Gß`È8:ñ‘‘;"_‰‘$ÅÈ#†|Kä‰J(—WHfd–“Ëê™Z^QËÔÄF ¹^ßnÃ6›/@-Ç©Ä×»\^ÓÆ'Æ1Çk÷¿À6ªâşÛ9Ÿj
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
xœí||Õ•÷¹wôi¤Íhô¶,É’å‡lË–œÄNœXñ+Î‹ØqÛ	JìÄv /âçÕ„	8¥P ”B
-e)”mB¡„²İíBË¶Ív¤İİ¶ÛnÚ²”n»ç;w$Ûq`÷ûö÷û¾ß~ß÷cÆó×Ì½3÷î9ç{îØ2 p  Vt%SÃo¼@lXÚ¿ºeyïÏ¿ÿÎğú: ÷ù[v€Ú ¼-X_±qÏHØõGÛñz U‡wlÚºçÅ–³ ş›LÑM»v€€ğcŒeÓu{‡_}#° ò,@¨|óàÖÑÍ+¾ö@æ' ÖÛ<40hü^Gàı³7cãË¶“ K‘b›·Œıœ?ƒ×F™n¾nûÆ_IïÃöOaıÙ­£;L<`ùa¼oØ:´*ñÎ¼şÊ·fÇö]#Ú­0Š=ı3«ßqıĞÛ°† :
°½CÀÑ›è`Ä{_ cxÇ'rŸäm|æOX*ğÎD9Šºš¹µ,\¾Ân¯-‚:îx1ğĞjT,ésŒ8 Ø¶‘°Íh2#Çéç¬˜áIKı›Ê2x™ÿğ h—Po­`CÀhÓÑ"¢¢íÏà QÖQ'¢TíßA¢Üˆn=àÑş^ğ!úÀè‡ b 
 ˆDü#B!bBˆaìÛ¿A"ˆEEŒêƒb1#Æ!XeÚ Êµ÷¡LÇrH & Bû=TèX	•ˆUDLBbµ5BLAZ{Ò:ÖB-â,˜­ı+ÌÖqÔ!ÖA=b=ÌEœ«ã<h@l€Ú»0_ÇĞ¨ı!ƒ˜Ñq!,Dl‚fÄf[ ±Zµß¢W·!.‚EˆíĞ¸–h¿%°q),C\Ë—ëx\¥½+ğüè€ˆ:®„Ä.èD\…xºa¥ökX«{`5b¯}Ğƒ¸z×êx5¬AÌÂZíW°®F\Yí_ ñ—0 ë7@?âFX8ˆC°q6"n‚Aí°†·À0â5°	ñZÄ†ë`âV¸q\§ı¶ë¸¶"î„mˆ×ë¸v ÀNíg°®GÜ»´ŸÂ0‚8ªã^Øƒ¸n@Ü£ˆ`/âAØ§ı|LÇCp ñ0D¼QÇÃÇo‚CÚ?ÂÍpñ¸ñ|ñ(Ü„x+Ü¬ıÜ· éxnEü„·ÃmÚOà“0†xC¼ñÇğ)øâ]p;âİpâ=:‡;ï…»´ği¸ñ>Ä·á3pâıpñ¸ñÜ‡øYøâƒp?âCğ âçß‚ÏÃ	Ä‡á³Ú›ğxñxñ/àsˆÂçµÁu|¾€ø8<‚ø%Ÿ€G¿_Ôş¾!>	#>…øC‡/!„'Ÿ†/#>_A|B|ñïà«0ø58‰x
F<­ãóğ¬v¾_E|¾†ø¢ß@ü¼§ÏÀóˆ/ëøMxñxQû>œ…o ¾ªã98£}ş^Fü–¹HÄkE¢"ÑG‘è£Hôß‰ì8ÿŒD•E¢"ÑG‘èÿ¡HÄÆ¼EÛV}$ú¸µéãÓ®IQ’>Æú¸’õQ¤ècÆ©U.İïİº—{tŸöêìÓıÕ¯{g@÷¿İç‚º‡êÒ½'¬ûJD÷‰"İ¢º½cºu‹u[ÆuË•è*ÕíQ¦k¿\×uB×l…®ÇJ]SUº^’ºªõ×À9Äü•öF¢ïhßÅHô·ˆ³à¼ö:F¢¿Gœ´×0ı£ö7‰~®}#Ñ¿h‘èí¯0½«}#Ñïµ¿ÄHô'íF"M{2„hga!1"6A{š‰]û&´Y{Z‰[{	ÚH q)Ô¾í¤H{“¸ö,!eˆKI¥ö<,#)Äåd¶v
®"sWùÚW¡ƒ4!v’6í9XI–hÏB¹J{V‘•ÚÓĞMVk'a5Y£CY¯=½dƒö$ô‘MˆkÈ5ÚW`-Ùª}®&;µ' Köh_‚udŸö8¬'Óƒ~òqí‹0@hÂ2¦ıl$ŸÔAr—ö"÷"“ûµÏÃ&ò âfò°öl!_D¼†<¡=×’'µÏÂuäiíl%Ï!n#Ïk÷Ãvò’öØA¾©İ;É9íÓp=ù6â.òºv/Œ¿ÕÃnr^»ö7µ»árA»FÉ?iwÂ^òÏˆûÈ¿hwÀ~òí“p€¼«İÉ?Fş¤ƒCdñ0¥ÚÜHMÚmğqjÕ0ŞP	ñfêÔÀ-Ô­İG¨O»ÒvÜJ‹´Ãm4®İc´ñ­ÒÁ'h
ñv:Gû|’ÎÓÂtv î¤MÚ~ømÓöÁ]t©¶î¦+´àÚ…xœöh{à^ºVÛŸ¦ëï£´øİ¤í‚ûéµÚõğ İ¦í€tâgém;<H÷kÛà!zHÛ
Ÿ£7i×ÁçéQíZx˜!~~RÛĞ»´Íğô>ÄGéÚ0|‘>„øı‚6Ó/jƒğ%ú%m#<AŸÒ6À—é3Ú |…~Më‡'éóÚzxŠ¾¤­ƒqúŠ–…“ôœv5<M¿øı¶¥ßÓúà9zñ«ôM­¾F¢õÀ)úÚj8M®uÃóôWÚ*ø:}ñú®¶^¤@üı³Ö/Ñ	Ä3§­€—9³v|“´åğ
'iËà,çÔ–Â«œW[ç¸€¶ş’+ÔÚá[\ñ£÷DåDåDåDÿı9Û(ªş–›}0z°rVƒÓ¼~èoÃ½wà!r¼^÷[<Şe‡ÖŠõ/_ùnıûv÷ÃhC@Kú Ú}ºĞò ìwì÷ŸøÀó¹úƒùú=3jä?çæ?;0Rµa,Û‰÷¾‚£©cÄÿ±xÑSşïŞ²¥VAeëùßsÌ ™ÆŞîU]+;;V\µ|ÙÒ%‹Ûµµ¶47-Ì4.˜ß0on}İœÙ³’U•¥ñâX´(äUe‡d¬Şl28J ¢5ÚÖ÷âÑööJvÀ‚Ë
úÇÃXÔ6óñp¿~[xæ¼søŠ;3¹;3SwG¸*+Â­Ñğøk-Ñğ)²¦³Ïoo‰ö…Ç/êçËõsC\¿°ãE$‚O„[½›[Âã¤?Ü:Ş¶góXk¶wR°6G›‡¬•˜‰[<ğl¼4ºã$)]@ôZÚ:÷$ŞÎhÇ¹âÖÁñÎŞÖ–@$Ò§—A³ŞÖ¸©yÜ¬·ŞÂd†cá“gÆ>qÊú¶ÁèàÀÕ½ãÜ >4Æµ—ãeÑ–ñ²}?õb—‡Æ+¢-­ã‰(6¶tå7;¢á±ß
½øë™%ùS±ã÷ÀNY§Ô„õ“ç€²¡„Ø¿H„ÉrìT6àÅøáÎŞÜu6†L2Ñ7NûYÍ™ÉW7«9<Y3õx4ÂLÕÚŸÿÙ³Ù;~xC¸²µ¯ÿãÖ‡Ç¹xÿ†›ÙçÀĞX´¥%§·U½ã™<ÉäûÚz²:‰÷ôc'¶05tö'£;ÆÕhSî,3léêÕÉ?6®6CÿÆüSãÉÖ&W¸u¬¿%' k+ÚÙ{s—Ÿœ¬IcÓÇäw7£Qâ­c½ƒÃã¡şÀ úçp¸7Ïô¡úú¢½C}ÌJQÇxÙO.¢3êOaß®¸{òfÖss1î¥®YÂmÑ¦¬p ¹ôKfÑ¦†p/	ÀämÈ’¿ƒÍh/¸âævVÅ±G›Û‘¾HnûOD
äe2ó—µåÀ‚)™r<ÿ¡h¹»™@eáÖ¡–ËœÑ¨1/`¾µ—“2]ä‰ñ	™³}²Š+Æ‘‹e›Ñ‹˜½áqè÷F‡¢}Qô¡LG/ëÓµnß¥]Ñ¥kzukç½dÕŒ«\}İT]şlœ6£¶%“6Õ¯é×S—íWT/¬ñÑ¥]c¬åh¾A-tÙÎ:¥6?~Û0¼EÛ¢aG¸mlà”vxÃØÉLflGkÿæ¹¬èâÁ±hWoC@oeïÁÀ>F§à{éª¦Ê
>M'£äÖÎ“rk×šŞÓ€ğ­«zORÒÔÇ¼ß»;ˆÁ®5<È”s oóXsmp£"ñ‡Œ“è\TEœ$Ôd·F‡šÆ…h+odå¹r+7£Yˆ›T²™ƒÃõÅÁL‚å±İ»0Odû×à<\šÜÉõÿÓıël§Ü+q?I_çæq‡q?Ë5$ô}»áÆün²ãÂ½÷sæˆy‡ùÛü,~ÿKK•¥ßòk•µ×úë¿‹„qÃ¶Êvíû2ûÏì??%ş“Ô€ûq=S‚ïï¿ëí}ï­—~>î¬ä¯Æ¾ÚË>ßxÅ˜ÖVkQûİÜ7ñ^K.—–U¥p®ÿ&}õ`†pF2Ğ/´S‹™ğfÎD!ùZò5â¸ğšãBâµšê´‘KğH‘;Sß§ï\RRtì¦-×2‹ÈzNÂµbIÆ)I!‰ò«™ Ó,
VÎ Ét2Mç/K9^MÕT¯Ë:U·Ç\EfÕÎãÉß/iØÜ}õÕİ›–ÄóİÍß?vìıÍİçYëFl½Po½2ãµÌ‡í2IÍRkšb]Öq>1Éâ¬—Ì)$.Õd.Y@ı§2®ÍÏc>&Cü4.iÏd$lßÉ×)[lŠláYû¨‹×Ó—R©×5ÕzÃ"e-Ïª­¢³¾G‰ :w{BÈ}^Õ\ØÜÒ
6ÄMNUá‡ş™Ì#ÛPÛÑÓØ©‡‘‚!‰•Õ” Â³¯e‘ämFàŒ¸">R4ql;Ê.Äç1³ØÓv|ÚOÛ3pØdËXsô¿Füş·ıºxª)ZGõ¦SîÖÇbõìXQ™LVâ­ùµß‘?ÒWq»2SíÛøT©°mL1¥¦ê¤ºPİú:WŠŒsÎ8‰3sH!J+ÜTb´lB;4^l¼¨Ôû’ş·³~¯.òùs¨ú‰‹ßÏ^¬©öUQ¦ùtj6ÓM‚ÌJ§Pv-b¶àÒ©BÊÌ’ÓáOuUö ¿³¡5ã)šÛä.;¾ˆœX\8Ë‘¨™ß7· ªdö¼pËÉlM_mE ØcåŸ³@±ø[­nÅœµ¨¼l¹êî™_İ9/Â|¼Cû}Š¾6Bm¦ĞÔfg½´ïAˆ@‹{´ĞfYâöQà–¸4¦/¦ØA³‰ÄEİÒzGâLx#Ê‹Š-‘Ö‰_Au÷Îëv;Š$òJİ¦{®.ß1{öîò¾Om®;DÈÍ[wú£5Gz+Ìı‚Õ\ºúê>¥ı+=ˆºÂ‚L4¶µä$-®Í½7f·ËXp¿D”§…Rê“9¹ŞO\<‡NŠL.µ¢tsf¥e‘DQï³jP&]äá­Şêöj±x¢àÀÚ«­©™½îP{ÍŠúb¾2ÜEçïİ’îjˆPîw¾ê«¬î9’­¶ËŠñ ìc>×Qâ×¸Æâ œóX‘yì(mQåÑaQ Kï0wMËÑ'ès—–æŸ¤ã“*œÉ\'É¢l¬ö˜•€Õa¥gíD°ìÔj·/eU”EÕ©ÈªL9#.‰  g$a$’1„Äh\&«ªŒ‡[rşY™ÈF«Ñj1µğ£.•©Ê²ÉBM<ÆöÆÆFæšŞF&Ûû—Î@}ıAÎxö¬÷o²è¢ç	ãAÇYÈf³$›=*=ë`@¼óG¬ÁR˜®¨©Tq%rTN£Éç¤E‚Në!¿tÕ7·ÇNœ˜¿ÖéEw¬èz`QÑŠ‹&Ş¤ÏMü)slŞª+Z¿±+¯‡êÁŒÌÆnÔd Æ%„gƒ¼è8WS]ìŠ`û44QsâÈTáødNU­ød)¬ËXCPÔU­rKù)´B­P.<ä ¿ÏX-+¥QŞèó	E¼Ì;xZ©
¡ë7¦ätc£®ä«L^ó½•J½•õ¾özâb*åÀ½¨ó,àæ¤ñ#ZEJDÎÅcG£XJx%‰!ÄJ'•OZe»`¸³Z•ŠD©¸U,MT(V+wŸA°ËVú\d`çÚÚ=;"­Oœ~~åĞ;{Ë‡‡³‘Hvx¸|ï;C+Ÿ?ıDë¤o<‚=“ #Sö‘¹¿8*ƒìÃr‡ü]Ùh6´˜F’nÚıáÌÔD¼±³q*Ëº•ÎêF¸˜Ò‡jŠÙŠè¶Â¾0…FšOôŞ(ÒÑµ2öÀ¿Ø41…ìßº{6ùóRªK2 ÇÌÎ„\-…Û5Ùbõ+í&ğ¼}	ÓçE¦É‹ÌåÏ¬ËG’rc$KWıÃƒÂ•z$üÀ£¨9‘¾~–±Õt®t•ÔÑ·8¸ıô	+%ßªhÆ=–¼GQÁ`f¾Í$˜–É6ôx›nËÉ;#RŒØ0áå€³Å55ÉKƒ$'oã>à]âÒ­ÑB·yVc—Î¼¾EçsG‰£ÏNJmÖMÎ•D¯>N'mntUU–+O9KÊJÕå'Ò[kå€­¢wÙrúâöİ‹×úıÍ‹WÄ‹Úšæy/åûóBÅ¬tBÏŞÅøöö¦!S"·(L~eÔ×è[á{Ê÷’Ïö3š×«P™2Ã¢n-L·ycfóš5²h†VÌE8ıL¤dıâkZ#'œ‘dAı¢Em×‰e‹‡æ“§&Ö•Ï+v´­"OtÎ^\ÊüÌŠZıÊá†Ç3§Ë-»%ÑnÂl7Qİ177q;Ç2Ù­ÊnïCòwd*›y‹U0	zÀ¥B¨„­1›A5‚`d2zxğ‚›—1×Cç¤¹ĞÃ¼rNˆç¾Wz™²1œèÁ$f0Ğø~õ;:Y•/Í}ä‚M:? q$’Â²öùî/«Éš*Õ™¬IªzÚ;Êz^8õXSÃ±±UU}lìXCÓc§^èAUŒŸÃÇÈXF[!’r‘œI\\-‹‰ÅJDœËQÄø!A¨`\ï&	7ùºûÛnZæîsoqsªÅò/ó¹UŸÏ}ĞEÖºH›‹”¹ÈY×O]tØEZ\¤ÒE|."¸Èõ1²:6£Kcßı*Æ¥c¤(Fœ1BbÄÅÚ—ª¸ú$²T"šD~*‘oK¤OÚ"Q,JDÈj ïùş_‚=i‚ºw1 ‘0x¶+’ªHFIY¯lW8öñ”ò’¢)F%êÑñ	ù˜U|Å~ê£ÆPÈÍg\.>¦H€°b,Ñ##äãáºlúÚŠHİZ?Èîôâñê”arÛÎÉÏÓÖdW“¥¬Ü1Y±s§Ï1Ã¸X2_MÔ¬ÇW¬q:id±#E{Àë±>];ëhS8œ‰Ş1kmôq«×•¢p@ ×–mÚ¶-™=|hŞ“÷¾ÿ{×\ó½şÏ“á'ç:<š®Ù¶mX÷ø5˜)oÁLÙñŒJÉ²Pë4ò†níH^Ôã×E–(ŸÑ“LŒ–®È"İxãÄï8é†Kñô±ƒ-ù&[bäÛ2ŞØmné¼Ùh`
!¾‰ßİx#‘Nß@¤·ØÒ{Ú+˜CÄ¥F0 ›Á0\µÃájš¡”ŠĞ˜õ¿– 3”È…i/yoÂ6ÿ †²¨ö{òZ "ÔÀÕ™úb®SeVV÷¥¥t(ıPšã+Â•Õ•™J®ÒÖÜŸ2˜‹«‹HQ‘ÄU#s·Ë+T”uWJd2ƒÊ²*›~MOïÎfSz¿„¬Å,…ªÂJÄ¼ÔídééŒ|ÊíÉç˜¼É]j³Ä$Wq#lêå_ß‰yT¸xAG"X)VÕÇ—œö’ªôfJwRƒQô*Ñ y¶°®£fâ¯ÍN¥¬©º*—1^%XG³ûÚ†Ya’ã1¿ÃòLÕL]8ãí/ª.:\D¥¢På½¦NÏ¾ˆ‘öø
ˆÇk2YzÜ²ï`.s}ŸÍN˜$²T0É!µLrYOcçèù+¦çòœ|
K>}§RŠÔùî+n^˜W_«÷ÍÕ­[H„;m–‰ßQnÕÂÆáö#/˜è½l%íCÌº•Ú»ä<Z(M™ÒÍò¨LÑJ-¼ËÍ,å…CDê‚ı….¥Çí,¶ŞH®È²/$R,›Ífy]›™%0µu3=9;T·fÊÛ"!W*Ô´pş²À¿ËU²}ssˆ˜ë‡–VHâ¼meó¢«¬Â>Á‘X2„:­Dºó:]‘©¾M {	™:ÃL¶ğ¾ËÕ
]îı‘PØd¶öˆ‰ë±Mi•¹1Ã2oæ.L«Îœx2“•ˆÜ_™óê‚ùj‘ Vz®!jmı¼ÀÂá¶âpCO]¨Æwœ­«8J$‹mbIàñEC™Míq›ğt©ß¥Ôi”0¯_íöS®Éçq¶ïJò„ß_&•‘ÇJH‰u[ªH=Ş’¤ĞˆÑ\0:½B#¦æ‹ÙÆ4óø×9]§rn‘=«¯Á'õÍ2HÎ;<¹Wql(˜+mk«w|œ’‰'Ë2e+|ª­´¦®`Ñ–ÖYGOÔï‹yí˜Ÿµmi‹İv‹=d«š-	{M6‹©|ñà.g¬@‘Š,'@gù
ZÂó2^%<gÄà‘ˆv¹Ó¹Ï-[İ"Ìİ˜r9ÌÅ\ÿVö\:+§™ÄdÒ9D$i]Q¹v6)/osÕ¤(vYN:¾‹Ã4ø‹EòÇ\şÛhùğ¨®Õj£~ô…rÎd†È^øåÌÊ÷UTW® RE¨‚òNEE™»Âû8¼Ê‹	6ÿáàAºàt÷(­ô¥Ô…l6u™'ãl².;RpáTÓ“qÅDôy~U<Ÿ0§O­Õ^ò”ŠB¡:o.YtÓmÕıeşèòšÌ,oºpëH¬u°1P_—V‰÷ ‡rWM¼sãAY<(:ê*œ‚pãÈÜõ-ÅldBNÏÔ¦ë¹9Sf¶±S`ıöy$‘<!å©«“ìsÛ­ªÜÃ™¡&L”s±£1<v²&È´<Ç•‹.¦j=ÊmÇ¥¤;Óv/N©Q‘şÖûg£%šé=ñwÄÓŞ`6L°¯ñÀ\;ş’N`Ü— ò4Èõİ(‰¼ÏÀuZé>‡d&f»‰½‘½D˜H]J±¥d§¤Ëß_¼yü¸8+›Å*ŞW–L–áÚ)m‘Î!áŠ±é4‘#ŠÁ½[gÆ-q!g¿ÃÂŞÉIœ>“İ«‡ÃÙ$—"ëœş¿ÁLÀŸ#öLHÏ6MÎË„p‰s¼ªäsFLJsÚÄï5ÊKÉ&Œ›¹õ“¢åìPvğÂÓ™ˆEòIô¬JêU’P‰O%‚J$Uí³ˆªÅ"Š&œÿ-Óâ€å1¨ê\XŸ‘ØŒ„­}ûLÕd1ù%LÉ(¯b’ç,ÄâÂiÀ‡€Ëj±%«h5±¯5N/YÌºt6;µ ^—^â®××¸Ù®zg¬ˆÙš³=û$“ËgsŞt'+JÄ“³†
3)ù	GYUÚwü8éğÖ¦«äùÛç–vtDüsÕŸ£Gè«€÷I%jÀ¡Œ$ï4íMf“½‡ m]¼)\ı«¸Y8aï!Ş…Iù¸I¬ÄŸl.§ÍŞK¯¨a·HóŞÍq—@÷3f)c©D%¼lŸ¯S*x©€wJ%/•P¾ÄÜiÙW·ú­&+
õ še•˜uOÇaŠß\æ7qñ­uÙ‹oeõw8Sæ\—CäWú~!Ás²©¸R,;ÓõÁúEpW´±³Z9^\iKˆfÃq68:qù³Q°ƒªÇ?=8lO:8ñS#ûâ„ºL‘µ“gÃ”ßç’\Dr…\”W:aŸªX-VYì.?g6ææ¡¹’óc3Úmjî«u×:bâqògÁ9ÍÎ¤ÊÏ/)œ_œ˜×e¢j0nØ©)ŠPŞßeİş´‡xz0Eï1êöº˜œsëŞ|"1ÃÌº¹9›¦b-ëçaXŠ—´®¯«ÇÏûæ¤ÓuuéôÂ/Ø´¸´tñ¦†ÛKKÛ‡´®XÑÚÚÙ©g@‹hRĞaXœ©Ú#(tÙ˜p3S óıÎÑâqÆV'çê|(Î%@ºœS6eãzNşí+g`–üLMÔ÷Î]]ší;>5_®µUö¯ÛİóÛKmÂ9ú›¯Kçg´Ô2g'ÈÌáp=²Å6éhèf,¢¾Å¼œèÓ€î[ºÕ<ä&uvH,±/İÚl+**²‘1£`ä&¶‘wEgÄ¤YJ0¿zmUÇ2Qd9²…'AH<,$J!BÂúyc¡‘ïóªşBŞï7z¸ÎS\d…T±¢‚––”x:…ı	¿ÑU
%1Aaù-êìµ;äúzf\ºÖğÒñòQCÂAYdX—[îŒŠi6³ÍÑß”à¸ÕccnNf¯"=…œkj¢{»¬¨¢2Z_êŞÖ_İë÷ûçÇÛLJÈ[“)–v_Û–U|ñk% ÛJfÇ—¬–­#±Ä"Ú%‹-KE®êğò{%µ°P{<HÇYmn&luŞn³9<aõ¨	Ç‰Ûfé±; FÌĞY_OM9Â…sÙt.ypÎqaÊ03«œµğø3ÏDRŞ´ËhªßQí¤Ÿò>pàt²ÎÂÈ¼UiÈñS3.Tô±ŠÙ
Ó¬ó²±jEÛ«NœÉô±*|ØX-Î²‰%—8¦©yæ`UglášÙ¤xâb{Ä{óï0
Yg3uM&S(…Ş£<¢|_áŠ””BõE´ˆ}’¢âÏ!	3Ì[>ã
øxŞ®æ³—ú’Ø`1ôq r`aód’ã8§ÃBVZ6X¨Á¢ZbÎ¢X%œ,09Iëótv'®ú²So7Ö}Øº—-{Í%éé•.[ÿş ½%ù 5ŠöÂ`ÀzrKzØ,Y›íÅz³kKœxo0×kÎ„½.…S™ÑòPWF
“pxvœÄ¡8PL‹%?ñs‘z×buİ¨“Jf«m*U%¸cIæfÌ.ªê1=u .$ÂKak—…ÙÎR·[Ã¨N§~é|èw¤K$ƒ,`°rÖü\Z¿sgş-ªş¢à¢ß÷65•Mewú½oãÉNvè'©,VfıŞ‹l¸³uşe/s¦ßéD«9¢VúF”òÊ¤û³¼Óå±Ù}¯º½v›×åäp'+Êˆ£Æ²{—•Üö™«bİkÖ–W\İ×‹uõ]]Q¾vMwìªÏÜ6R¾ìŞÜïÈ¨5†ßdÿ±BÊ<e?{SRèÊ×•7•_)†‡²W!óÂŠ“
w››(î€»Ï¥¨.—ò]Œà<Ã98ú÷,÷}î§œáNìáH*Wæ¸#ab	ûÂeaçÂpp*àô
IXÛÁğüuß —M\LÕ®HbÚ }K9Eáİ¨s›Ô#ğ"°tE)J½œNgw¢‚Ï%RÉ4ó&ö>&ïPë¦ŞÁ\ş²%W€ŠF¿b«–ÉÔmN™z¹â«Ü0×Uj,Îsú=1µ4!¥‡+ÑC¢½ à³b:9ñşÁÊÆ2§¿7%âƒ|`ÚQ¯QşçQ¯2®TcŒı6‚Ä„H%‘A´qÀQ#vÇÄ:lrV;	æ›¼„a¤nXLİl>`+ŒI¯§’lrz;
/5&s¿vÈf™ßpæ´+2ÅgoSŞPæ·-
NL,wÍ[˜	ü„<L¾¤¶¬\S~ 7ÖµjEø ‹NÑü[Ÿ8´gÊK…€Ãİi(êïˆsq&R¼$ŞàtZ=A¡Ça©¶ôãè†döbò¢R??™öê¯rÙ˜ë)™“­QpfŸG\8i‰ş»:üpëUt>›U£•¥îtw£ê«”—„*}jcwÚ]ZI†kË?h®òŞPZ~Km»ßß^{KyéŞªæÄ§Ëkóo—:&%î/İQz¸”+…"®Ó#	&q zâq§ÓèqTôpB•½sÊÎ8¥K|õV¬‹)æ~ÙÈ„gÀÄÔ
)>M:ş#‘ûŸJÌ¶<Ì²õ¿`›Á€çıÊtåß§ñ fö§&«ØfŞÊÁİ&“Qÿá8“Áb2aânÄ++˜ŒFÌámÂ£şŸÌWrXx³`aß°Å‹0Åa6›Ìf£Ùl0˜V³ÙÈ`6[Àlbõv»yšYÁ`2äÅ¹Y,f»+‘Ñj±³GpÇnñf7ò¼ÁÀl<Ï¦÷(r3Iâõÿq‡1/öÌM`?°òvùQ$]§&Ö-o±˜,ÎW6‹Å¬ØO3Ïdp\ÎŠÄŞ‡sØr‚E²}Ãr‡h±"¯sXtY²Ìä0æ8¬WrØÚÏ*Ù‘{e³OrXÀŠ™¼ÕlµV\­Y­Øé‰±Ş)[™RsŒ¼)¯š™›ÈhÌ`d‘ı}>Øeİ7Ì( X£Q0É‚M`Êcı¬Ì=Tçÿ"‡ÄhÌ 
2û›ä$ç4‡Íj³ñ6›Ñh3É6›°¶)—SøPÛ‡p°—Ë¢Íé@2q’ƒµ! Şû4‡İã±¬Şã±M8t:0ZLyõÏÜP1äpØUÉÑ!{tß°0Õ‰6Ñ«B³Ñnv‰¢ÁÊt‰ÄÈá½œL9ñJ…Ñğà]
ûv^]Î!Ù$Ñ*J¼Iäİ.‚Ñ&’İ‰¬Şç³_Éaş8äE“}÷¯Øoçu;ˆ’]’éƒvææ€8ÍNf«9¯ş™›Šór(’OE…Íöî"HÑá°9¼ÉÁ{ y’°sX_À8Ìäp\Éáb4<8>ûŞ^]Î!‹²Ã&ç9d4¶xG0(ı—8TGÀÈárôáˆæQ$E¶É2o’y¯¬(`m2ãGáåú1/ğy7š¹¹\rÀÃ¾ù2“CFET‹E¶ä°K¢âğ`±¡G„Cé {‡r%‡—ÑàV‚^$Ã^y<!`ãÈ†}Vœ§SÄùÜ‚¤Ó‰ÆvHNô	T ÖGBò4Pàmú•óC8<Èáq}ì[;—s ¨²êUÆ!ª:Å!³úh‘r%‡%ïF37?€9¼jÈÏ¾„W¾" =¬ ¸—*º\‹*].ˆhô	§Âê‹£Îé@A ,vKŞÄ3· £±Ï)`ß5Â+?¦mzXAó¸n·ìvÛ¬.{‘ÛíF'PÜŒÃÉêã±Ë80Lr¸¯ä(`46ğ»"ÁG ›âpyœ·ìA7rx<:‡«ı›Õ—ÆÕéÉBçuÏ•AFcƒ€'ZÈ¾'…Wq =t©àöª^ìõÚ¬{Ìëõ‚ìT¼.\À¨Œ£¼Ô5ÍA 9¬yÏÜBŒÆAoI˜}ĞëK#êÕãsù|ŠÏg³zí1Ÿ­:}¸]L†ª„gz²À  ‚$äM<s+bÿ¦W™şò(2ÆH$lÉØg_§ àìB@*	€Ó­|1Œ¸
zD*é›,pğ€M¶çÕ?s+LÍPTPG²^'ô!ïƒ‚B_aĞ…ãÙt$‚……¨<OûYàcõ³ÓéÉØ1¯š™*&Å…ÕeH†æ—¦ù¸Šª+Œ"aO8ìCru8ß% 0À†ëÜ9Áé@¢S¹‘+9P1e(Si$]}*Á«{qîÆ=áh0Zä+*’¥"gº(Eåù‹"•²¡ÔÜX4 Ñ!ÀáÑ¯âWrÔ ®ÏT¨Š7¤‘¯¯jKšª¸´¨´¤ ´Du”¸ç–”•B0RXR<âE~fY‚iâ#Z3Ø¿¦­ÖºíwçşÚô²m€¼Çş4¿ıöJò™„6<ŒSïƒLV¡ ï£§\±ÑººÖu£ÿ ÿ[îü99IC®Œ~:h:¸¡¾—/»9ÿùÀeÏ½môoÁÊ=;3¼‘]°&ÿ©5ÔCî~ôz5öó=¨ÄÏJÚ•äQlc%/ÇòÌ!ímÆóhãÖa–Óõúımz[x?ù”`!Ö-¤qäwäxh— ïAy£SüÌ*„¢Ï}¯(úEú05
›şˆÚfµ"<9e»Ådcşœ€‰dóç¤/ÎAˆÌÍŸcÚL’ùsLoI4nÂr/û¦–Å³»àHşœàŞ—?gs}şœƒP›?7 ƒæÏx;nÒCo7l€İ°F+¡‰}o¡ª Ò3jÃSµ-0€Ÿ#xµ–ãù l‚ex=sñ®&<ÕædÉå÷5cÙØ‹òoÁ¶6cY=¨ÇS5#Ã6mlÔ¹Ãy¾*öV<gåCX¿‘q±vñüz<aßšü€\mz{#3Ş¨ßWƒ­VwoØ½mdweÓöëW]¿kËömáêªºt®8ÌŠ[®Ù¾mùÀÀ¦e#ƒsÃ—Õèw²“\Yóö{¯ß²ióH8U]SnØ¶}Û–×…ñ¹ªpxÙ–CÛv†woº><²yh²­¶íÛFrÕ‡Â5UÕ0µÔnaÿïƒÛó`!¡O†Âíè¢Õxdğà qT;ƒõ³ëÛN³ÿc÷ô£¡ê…^t1Bx¸“˜¡›˜ğÓ‚ŸFü4 Î±”€Äş:¾ƒøbÈÜNo<¤†öl+ìB™oÛ¶¦@hË@YhÓĞ`h¨¹,´q`0´}€`q_ç`¨§{0ÔÅ]x¾½“tbñ²–²Ğ’öÁP;·µ†:ZH7-”CÒÂĞÂäB·—óİÆrÚm å!©º…rk·¹ÜÔMğÜ‚uÖ­ê:Eà71’SäÎ¥§ÌÚÊ¥ã|ÇÚqrëxqÃLçšqÓ­ãĞ½fmïIB>ÙwËí·CSpéx°«wüsÁ¾¥ã‡ñ‚'İĞÔ—H@br[·‹$#zùÀ§ş±kd»`e#»Şuğ? dtDØ
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
xœ]’Ënƒ0E÷|…—é"â	!%¤‘Xô¡¦ı b)R1–!ş¾f.M¤Z2Ò™—ï0ã—Õ±Òí(üwÛË3¢iµ²4ô7+I\èÚj/Œ„jå¸eWÏwÉçi©«tÓ{y.„ÿá¼Ãh'±Ú«şBOÿfÙV_Åê«<;>ßŒù¡ô(¯(„¢ÆUz©Íkİ‘ğ9m])çoÇiírŸ“!1‡P#{Eƒ©%ÙZ_ÉËw
‘ŸÜ)<ÒêŸ?\Ò.ü®-‡Ç.<¢ ˜)Ü0Å1S”1%	hÊ@%hÇ£JŠ*q
Š@Ï S€ tbÚÀ—Yú¢1ûSüèğÀaD[ÎNLac	‘x:†1‚x#ÚISI@èc²1]ú@d†vR<›¢t¶[´BİüÇçÍ¸SŞ¬u“äõáÎÃk5İ7ÌôfÎšï/‰¶°í
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
xœ]’Ûnƒ0†ïó¹ì.*åĞI©¥«ÄÅÛ@b:¤¢^ğö6m¥Eé³ı;¿1AY*İ;|ØQÖàx×kea¯VoáÒkF\õÒ­„o94†^\Ï“ƒ¡ÒİÈòœóàÓg'gg¾9¨±…'¼[¶×¾ù.kÏõÕ˜_@;.XQpïôÚ˜·f  l[)Ÿïİ¼õšGÅ×l€GÈ!¹‘£‚É4l£/ÀráOÁó³?­şåÃUÖvò§±Xúr!¢]±Pø‚´;"ùàB±@ÚQ.¡\,ˆND{¤4AJ¤,"Êˆb¢’è™ˆzfÔ3¥Ù	­¯“›ãÇ„G,Ô)Ú£Vœ‘Â‚%ÙŠi ò“†<P®N32²C§7tçò—}ß—$¯ÖúıàO‹YVÒk¸ÿ7f4‹jyş cæ¨Ö
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
xœí|	xÅ¶p-½Ì¾oÉ$™†$@	4KbØ$,“@€€H	È•°CØá²ˆ¨€ 	Š€ÈõŠnx7PÔ»°*âFÒùOõLB‚Ş÷şÿıß{ß{ÿ»S]ÕÕUuNsê,Õ=A!dDUˆ¢òììagæ,©€š:H1ƒ†¦¤Í¸u4BØ÷Ec-.G:”÷3à>yÌôJïxáÑp¿!òâ¸òñ>Qü²!nBâ¡ñÅåÈ…ÔéTĞŞ4~ÒÌq‡6v)@È\‚P‡¥c‹K¸'½pŸÏ3J¡BõzÃ÷eÂx¨ué£•3Şx@÷o!¤i=©lLñÜ+Ÿ€ñ ŞöhñŒrq'ê{Ú{'?:öÁcV#ÔOø¬//«¨”PBv°çåSÇ–¿ukù*¸‡>ü,¨c³G½yËßê=ëyå~gE:¢Ü9¼ñĞn3€†±áœ£qÄ¢â‰È©	á	Ç¡{=‡öFRÜ_eÀUØCÆ!|ââ@—®|ÃàJ QH6¸b%çK©gOPCƒ’à	–?‹~=í¨H¹¶8¸®Ğó1h{Uéuµ¡0\–GÈ#îÅíÿæP…³Cè5´í@oAiaäÑôzlÑü:ƒ^@ËÑ1´­@şé°GaœÙJi=*üçĞñnT†f ] w>Œ÷*zWcŠŠP%š‹jv.WÃ½!@WğAôV£ÇqÙ 8l@óâ>úÅ€kÑnô\Àu« ß¢µ¤šL¥Yh)Ì°ˆ€ê7 öƒh.@Ã*™ X (•¶+öC‹ÑãPšÖü	?¯®i¾Œ—¢U€É4 !‘Ç	ãş
êÙ¼ˆ+uËû
{h99FTõ›Ğ8ÂY‚Jğ\´í–Kå­hÎÂYhµü}ÃßÑ,>‹Dº†ëüoën¡Éh «ôoÿœšüÎ"c]\Ã·ä2p¤‘?®EZ€Lõ­@šf4Ü”‹ä¡ĞÆÈ9øgùƒüh&*ær¥ÈÆ½£HÜ‡ò˜ãÇ ¯ İô@ÁÈ`~Ş°¡Cçzpà€şıúæ<Õ§w¯RfîİîïÚå¾ÎéSS:´On“˜ßÚßÊçqÙÌ&£A¯Õ¨U¢Às”`”ìá¢¬÷š³‹ıYşâœöÉŞ,WiŸöÉYşì¢·Ø‚ŒKğçä(Uşâ·ÈJ€¬¸YuQH‚–ãîi)…[JM-±ÉÛuc üŞĞ¹>~o-98Ê+úøƒŞĞ5¥<P)s	Ên|>è¡`Å°õf…²§—Vg¸F«éíï=VÓ>Õh´PÔB)ÔÆ_^ƒÛôÀJ´ÉêZCJÏÀÂL³ŠKB¹ƒó³ú¸}¾`ûä¾!ƒ¿òõV†	½C¢2¤wC-óÖ$Ÿ¬^^kB£‹’t%ş’â‡òC´úVÓ¬êêÅ!sR¨­¿O¨í¬/]0ó±¡dŸ¬Pµÿ&8ıï‚Ä!>Şä÷VßF0ÿµ«-kŠ#5B¼é6bÅéÂCò}ìpg­««³ıŞìê¢êâÚ†ªÑ~¯É_]£ÓU—g¹Qn>QÛğÊ2w({y0d**Å]ƒ‘©gé².È‘øloi1ÔÀ_¦ßwŸÛgnj“ûÏ# (ìó12,«•Ğh¸	UÎß{Ñh÷A$¥$C¤ˆ=9ÙøÄÇT5>iê^äŞöš_ââû–ø³€âËŠCU£Aº&2ÆøM!Ã÷nŸ¿ÚbövI	*m½€Uß’	ŞŸ D‚^Í;€Ü°.Õ&åÆğ}8»æ 	f‹·‹†aãdù³Š"ÓK]0€“„aù!©¤âÇ²jRS Gq0lB…™¡yÈæïÕÄ]†VÖ„¡ùJ—H·­w¬z¤W(%KYWŞ¬ê¢>aØXşÁùGQ áRM'¯û¥ (ò`ÖØÑ¤,!«:¿d\ÈSä.u7Î›ïö…¤ p8èÏdbj{É­GP‘•aùı‡úû™_‘ğ6ŸuÏ0ş|wxÀ*^åÍ'n„†&¨ğfCÁß«\Cb¼
’	®Ô2ÁíÕÍ›İ¨±5 jëÍÛ'Òİ·”gâÔ;§q4İÂ8½sÜ¾ /|´O&ğØ=TŒ¨9@MÁÈgï¥ŠÑÒÅ„Ş›ïëúK½!)7ŸÍ‘G¡r„
Í#¼Öâ®±€LÈo1CÙIîæÄ= Ü7İæÜó¸oãcoµÊßh5Üæ}Cˆ‰°tŸÙ­è¶ ı {½&XÒÊ‚®®‘$¶˜K»²Aü}KªıCó»)­AŸüÆ=‹Á² ş¸ÿ°^í“Aµõªñã%ƒk$¼dèÈü£&ğ~–Ë?H0é]Ô+XÓåPRj	«e•ìÆËnØHCàF¥´w•ªRrJ…r?¦#¥NÕX‡Ñ˜Z®3…%(€$ğ­ÆÔrá'RckêTáº*¥N9j#™¤á%•¤–tDOÜ5˜U„šWÀ/Scô’ë±»zQªkqUZr‡[TA)Œá’¼» óFæ¿¤CĞM¹ ^ì qq•³Á¬dyK˜ Ì–VÙbC`üáö÷ 6ù{ "‚.¤ñíÒú{±úLVŸ®X½"ŠºWïsC˜I@A¾–¤7úŒ»Útq*J¥ÚôU{fòÁÅ#ÈŒ0xÌ3ñGÎh*æà|ÎøM|›ä‰¤šìÿäÏ´3Lrn÷>?ÿZ$Lş ÚÅ,å\-^SõW-Pı^MÕA8Wª§á5~M¥æ æ–¶#œKµßèœº¾ºÇá|EwSïÓçèÇê—ÃùŒş„¡‹¡ÚpÅ˜iÜhü“©¯i¾é˜égs's¡ùUóO–Î–jË'V»u†õˆõG[’m‘í´]mïbßd?è°ıœ©ÿ#ÎìfçC‘óüóóËÿğùó¿Îÿ}N§G‰Ò!6?‘Wq®ĞØí6ñ„câÆ}ƒ?çÜÑÔÅ×oâ¿ÿŒšf¥ÏP¯sÉuĞ«"Š“t)¢*5„RÎ¥œ3[p—.æ€9Ğ15`ö™©Ïì›CÉ\™m\¯·Ge",^$gø>Ê(í$+EÂq*5ÆñOpĞ 3%ÉlA]\)lDs@ûi€¦ì¤f½ëô›§ğ
zäçcgÎÀ`ØNÒ—!d#ú$ƒ(*0¼  …‰f)iÍPc)ƒ-_Ùæ’l_ÑöHæÔÏ%sØ3â–ñYÈ<¨Fš¨Š±s6µY§S[Œ-§±ZmOœÈ	N£(ÎÅó‚MĞøh´“º4.¯OÅéôºÁX¬A&³é@0Ên£_¥ß®§ƒô…z2ÈŒÚ¿a¦fÉÓ*GoÖ›y§•jx”ÈXº€ëœ4jÊ¨)0ë$3bSäÊœ+ó°8»(I)¥¥…s˜õÙ}ÔoeÉŸ€ä³(K¨÷YéÎŞ˜“¿ÊŸ<\~rØäag>ïıƒ“óñ#ù“ó?¬—²ğÄŞ´§üÆ$¹ÿ–¥I¸û¤pI.$¿»#¶›Ôğwô6 h:¢)a£ì'”úÌébcí:] Íİöå ×}¤À›y”ÚõrS)à,‹D@.”™™™””„\ìæ6L&<³@D”ü8 ±³Mğ·JHï”;%ø[	v›#–Áÿzõ§kè®uu;°{íŠk—cOf¿½zx 7Qı¢Šï«’CÏ¿¸oÏó{äĞcNœUY^vë5ãïAHş È˜SRSB8^YE™ˆŒ†åŠì‹ˆô. C=j%5Z-GA>EƒQƒ87L»I´ÃBi²8ı	Äl²t„˜÷<~òù]o?¹—XäkrŸ«Wñ«à™ñ‘›WåŞ0z.Œ>­qt­FC9NDˆNmt"ú3,fI8,tÚ³'OŞ½ûôÉ7v›ü7ù«ßà×ÀÔá×¾¹) ñ#©£øw€¿c¤Tƒ^¯!b4k‘ª9Õ4İBQ	j'ÎÑ®Ò­VÏ—‹Uà&Q±¶áäËj](êú$±N<ÕÈTvQäÙ¦\¼“wŠZœØ9¾3DÜUíå¯>¶aëc¯Ékµº%Ü®ñúşœƒIÊù±ï¢Gp[À²âFpÛÙ$5Ñéyn	e*‚Ãšıf_º`ùìäÀ:9ï^‡w“"yŞ·ï“‡­:RùIr'_½’‰"ªŠã1ÚZÀá-(,“ŠÃêƒö{°Z>6ÔODĞÿAü}‚”Cÿ(I‡(ëûJ0cŒRF…;CÇtŸ?HRñ{;v°>7At>V`:%¨C%¥$5ÊCß¼‚“ä`S®rAEöb$ıH Eft?'à©4ı`İ»6şÒÏ^æÏ†ƒø‘@!'h´aR‡è(Å"è€bb.lty\Dï’ŒQ(b§QQT­6VÕ"µWi’­Ì°..|xTô¹‡A35BdªH‘-+&¸¾4m,Ò,ñ «¹A?İºõİuÔğÓµ#+v>·fİíëåü+äùEyƒ‡áQx¤üŒün…i’?–/Ë?aÃ¶Ÿ~‚Y¯ÂLMl@÷I±z€5XÏh…Š (R ÃW™a*ÒÅ}˜‚ÎFÕÜ8zZëÎLÂGâå+‹Öc±Ós¸x­°rı¼1w¬h«Z7 Tê&ÅF#¤7Äˆ6ƒ-6N¯7›5A³ˆ£QtshÊ5%BÆ•Hï;÷ÀéŠ6{à@šÃnD}öÕß=¸}yuÕÔúZÛõS]ÿíÆóÛ}äÃi~ºrÎ±e3~3Å¼÷÷'C_ÍØµ¥/H'ªşõ¬Ú¡éRÏÄÖÀºäØ¸8Qp¶nÍx˜”œh1[ÌA£;©ÅB}±±>`é©º"(Ár$ìrV¥ÈØH5%ÌÒ0î]WşŞGdy²Å	Üeúµubg‡/-#½Sœ„Ói¿2?{æú×}ñ‡ä|¥56.ÙR°µxÜèá«†,œÿØ:İaÛ§.\Ù¶tã<õ•³§™~bfÿñ·v)}`âc³ÊûO½úüc¡Î|D{<pb,ğ]º-[JÔñz¨Ô„bŒˆÓqAoÔyt)º2§Óa­ `fH56—MÖ2¢ÿM€¡lWcİs¨~*yü÷ÇäÕ²‡3å×qær:«nÉJÚ»¾?j¢{ŠEùRû(—Õj·ÙT¢ŞÁ-ª"h³¹İ¦Š ÛÍÙí®Š ]à@FT*N¡q³E&tR)aŒ²¦H`¤Uè	†ÌtĞ”ë?ıò–ß}ë}¹ËÕ»Ÿ[Ö÷‰ÌP
õÕ/ŒöâÙ;øØ²*ö=c÷šÙÛ:t&Z#y…Ù£€wÈ‹"Ş)Í'è´Z'ˆJëxÈE¡#›ÉF4Ôfƒ¥n ÉÑa3ïF¤¾»+>Ğ$Ê²•Ô\:‚2±€…^«¨»"	"›†‡­0—sëÂU«nâÌ¡ûÒ_Ú´·ãÁŠ“;²i~¿ıŸ~bÎF|ü‚Œƒ¸;~Ï–?÷ì“ÿq§ ğÚùÕ;z?Öÿ·gw¶$´.¨Q²dÏBÔ‚Ë‰4Z$ªD ¶@×ï²;ĞhNÙo²XAõsíåÄc·¿­÷ĞUÜ+õùõ×±HŠ1¬wŠ¥²Rn”€ÒĞD©‹ËŞ^“¨±·ÒëÛöD Y 2›ÌÄH=”˜x—Fß.¾]E0>šÍ¦hê/”dx-ÑZğüÅ<–Îé`1ºÅáÈ¢MNŒ×ÚÌŸá²úëÛ/_Rööü¥g'U—ÏÛòÙâ9/­9ÿÖK¶l\»n5Uû‡^™{ØÎ¹_,½#?¸mì”œ½ß.›2urÙ,¹jÆÜeS¯¨f’²æŸ‘”Bé>Qb-:§Y@RŒŞŠ Îhô·oŒ‚†Ôn	²+š…™zÒ¤RZ‰À]›Ùä~ FI·tfRO`úïİÙ‚Fá2åï¿{ö÷Iû2j7ï'mNU¾öÕ¿àOOï˜3oÃ†ª‹$'äçäÅË¶¸CØùıÈGQÃ¹?ÈÜÓg^\¶ê@Öã(V•ëªD‰’U <˜VµŠç¶ğÆFÆ´)¨`v–†míÅÚR£bs	.’Ÿ¤–Èh©R4ÁX9^àˆ+¸­*~KFŒ¨ÑsUf‘@6$ón^‘*CxÜ;‹·y.›ÁsÙBv¿äåxÂ‚¨ÂˆãŸ)”	s*H{@<Ğja/ª{J ĞÌà[Ó1è3{%½\÷Iî?‡wn–×Êk6+q>7‚^Uğ.İÏäcP£¿?häÊ¸UÜvî ÇGSN²8r ”ÙLÅ¹¸—c..U8„ßÃ¼1ìÈ(F#%)¬š·ƒK/Óüõëe´~=j1¿.’§q~ÁŸ‘mÂe¢2&)bsd\•S¼wvÓÕ8Ín$ÌîòæM¸OŞ,?|.üÎqgA3ˆ`#†Jí´„‚/ ğ €ÁÅWØh1Ñ’Â h¿‘*Ü_…:å@º3ÓÀM5ªKJà®ıÇL&À£Qœˆ•(„jl„ˆŠršêúsKOcùÏøvıV]ÖFüî~ü„<ÏúùUîpâ9ˆ¿cŞÖNÀª
°Ò#;ŠC¹R­ÛÀP²‚™p y¼Zk´5º0hµr<o)JîÂ gùrw	)Z-¬98?„Ô,æã0<I gLQ@æ™«’¯'·Á[ñÍÕ³Ÿ?"_ß¸ñâç8yğÁPÖxÏ>ôŸ%µ+Êr_~¤@.’çN!·š	üšÚ`º¢ÆJ™f“IEÒéœ.d0ˆQíQ=o°Íf‡„TA(r…BH¸$ÜµšÕÖˆÄTÁÅ6*Ã#áèµÎNâó‚õéÀÔîúBhì®.ÛŸ”Ê?É_:gwüSã_x–ì‘oÈ7–®é)/ÇñPR#×ôœ2_f[;#ş‚
™QÉfàÔ@j‹•×+ô5´ ï]_Ş„ÚÕ¼ˆš2¦Y¸±ò9ùy%îŒûâŞ'?¹1sç…ó$$–· ÙÈ‡°ê›;·°¨Å ˆZ4BÊàÕjD5Q@T…AŸÂ#\2ùB~€¿È‹Êƒ‹¹Â ¦H]D–{=ë)¹Æ¨WÙ>±û"i'İXß†l­/(k«<r³ØÊÖØ)À¢»bH)˜ç¨FË ñ \ˆAçdÂ¢¡:Š%{ÛŒyQD…A‘òÅn†¥€O½œé.ü%;KvÕ?t‚>Îí‘-Ûê/t‘SD„œn¯ÕØ5ˆGÑnUmÃM)JoÎq9ƒ.Q©€Z­Š# ëÄÚè[4BF-Ü
&áñ`A/ìU  %,ˆã~õ÷Ÿå«X…ÕxdÅ¹ïíyçõYÛAş_\¸	Wà~¸ "îÃ÷ıµNşkıgí¼8wàú6Ğ+œê"ÅÀdC­Öé9•¼-T‹´ÀÚÜ©o²5aÄ¾·igù4îVww“O=îÜÚº•Ó3ª„®Ò¿ $X—Á"*1–Ùbù3Rª)d‹µ™sØd/=‚ÄÎqà
Da€CÿòÁñÎú_µL¾/ŸÁ·ñ®÷ÿzğ¤gz†øLá“Àw”yåH	*µZr¥)å´œN½Zs5xº¸¬4VİÕ|]Â1xsú.l
±\»Z^‘£9q‚tû\V‘,òÄ9‰Ïª/$O×Ÿ®ûÁ¿ğ |y$˜Y^zW²# ˜$3Y¾v‚ìà³îŒØ
}çB_æ[» w‡!—J´šôzƒÁê¢ÑQœVk´Ö6œ”tsU¥r©¡y¦³Ã[Î»îEØŒwÊûLı4!ÑÊfau83±lûJ%Ï®¥ÏYäv\;jO‰N>ú9-YÜ«ä|Ü¿Üá¶üaİVXßÎôƒ#—ãüüj#uÛ)z¼” rkµ:^g0j—c<ã	`:_…§©ğ80-ˆ-(fUFe²K ¹òV(ë°3¤pB:s7úÔÿhÚû1Yöq÷©[tY¹z-b°	«kœ±Û™63)räpªAÔµ©õWµYxáÒ@¡…P"pnœüÃ?É?c®ş¬:#¿-¿µmÓ3ëA•×ãqxnÎ³ò^b¯¿"«Ë…"ú´P‘-+ê$EëID$Úm¼	4*¨•±0¨¢Bs%ÒlÆ‘ÈFQ!iœØÉ3ãTøØ§kä¿Àg¯czR®ı^~òZó›Ó“ëe>ë£Srıµµ°7E,h¡”ôz5Öé¨AmÙVsN‡XÀª²`£%ÓRf9a¹aáuù"7+ú>,+-+
´÷»lñ+8*ñ+¸Şm+J_“×^?¿øûw¯>…Wÿ(¿'ßÄ®U›Hfıë|Öë‡<]ÿ=wQnWÅ$ep«¸•ŒúIm¾•#6F‡PŒƒçÚwh¥‹¢QŞ¢`llGAéK`/‰ „µÀ¨fª°K3Óó{©¢XÌM;Pæ/§9œÌJzí¶8âŒã¸RùÖOrç~GcBë¶?ÛsâÂ>O/ÒîÖå—’¹VÿFş*½`fÖ²Y…}ñÔÚóx\üÜi³§fçßç7·ë•7¹ßşW×‡|åc?êÖ¿£×âOé6d2›Ï€ˆ#¢É"‚¾$à3"çm±¥Y¸Õ"²öÙÉïËY\'nÏÜ­ŠZ	´aöÉŒâ%³Z0‚[¬&PRº»Bh!ÄLFA”®=°V¸î_Ö}÷ñ‰i›ŸwÿC¾}ë
ÆôÑºıg·ïº@ÙœHøRö
Ò¤(
. @Ô¢ÑêÔ„æ	¸€„#‹³	˜â…¤ €‡‡ÎŒÎ8@Î¼)‹g°äIo“Œ{œá³êfıÉytÀh0ö(ëA’|T@jß @h!ª8•^‡ÔTà°Š³05œÉ¶ñ]šiø0kÙö¼š)W¿ò ãğÀsò@üÉ9¹Z^v"<Gû\?»>“t¯ƒ¼ND ïV¼›’T	à@¢QTB¹¨ÑLöJ‹\˜AÊ.È¨@#“,]ÒÌMœbàäô19æ+Ï‘œúZ’CêëŸ"c`¾ k¾âQ¤KÑœŠ¨)˜VŒğŸ€ªÆr¯­ìÒ¸¥Ñüu&ØÇÍ¿ó&M«wÒSuçiñ*.zë²;_€´YA_ãÏ‚|nƒ ’GH¥ÆÜí û@ôv¢ñÌ{C4qƒğfâ—×à2y„8mÙOO/|+@ÂF6î‹Œ(¦ÁATË}QØLwÕ½{¦‡7F16 ñà@óˆ"‹ën!üOğ`ö6 k —Ë„Âe?wZsï7, <ì’šòàr WaF°º±ÒUšğÜ>)*b»¿k¹Ú•?¶Ó%i9W"º¼ ­CàØ†xzÀi'Çå¿»ÌÕ|{Ãº‘íI-áD­P
*‘º¶7FE[T‰‰^o´‘¦v´´´Xt1Æ¨²¨‹Q7¢¢x-ŠŠ‰qäcL:.Lm0¨o•Î¡¼Kº»Z’íŞu#z(>­³]ñLüÊNUº)¾sã¾Ÿ…©MX§ñ¹wÇ¢@ÏŒöõy ¤@zÖÌÛ¶¿yubåôRÍ±xæ[gÚÕÿ¥hıãÓggËÄrÓ„ò™÷mÀ£xîşùÃòÍ¸õ«5r‡ÜÁÂC›‡9’:fÈf^‚9÷>Ù‘íÇğƒŞÁŞyømQ¹A³Í¤G;õÀä(››¬€‘êD?hy?Ó*f›h¹ûÁõzçµïF‘¼(â¸‚[xñ+ÏrÉ‚‹g’Vò—ò×µ©¥ºŒ=Ü59Øó¡·êÏ^:óñgï¿ı>Ó@ó Ãû€+Ñ¨TŠÓ#Q¬6dsÇ”[1²š¬EÖrk•õ¤UPSÅ«ñºãr¬V—Ë”t9¨&7èçˆ«D*Jğ \DSøÉ]æ0ÿ|Js?RfçÃÆ q˜#š‡Éw/_9iªš¾mİº§&­4×?vzæíDâ@n[Xo(˜púãÏÎM|TWôT{«¾æ¢€Æ¬®R¬SˆEƒQ0ú[[í¤òæµ*Î/¹‘ÆaB7Q9,-ÊÆóØÎ@"#³Óß‚íîş&}¸ãÎ™oÇKf>Ó‘CÂ>N¨ÿü±Ek—/~rñŒ'bv‘Œá£7âgîX÷d+“ğ¤ÏŞùğë?>x*;v@iĞz”¾Š^£¬VQOİ1.uiL&{nĞdÒĞÜàEá†@ªÀ ‡bqGµŒ±ï1¹*â¦÷f;I÷Üëéåã·DoK¾òÌUù§+W¾•ãmåINşáåóÁíg/À	Ø‚µØÑãEşàÀ&œÃ$£ZñsÏ‚Ÿ¢°Î	ÑGEkÌ¹Afµx.7èàØëÓ&67Öˆá·3^p,KÛç¸tÂëŸç<ß.îHJéÄø
İW7Œî[unŸ^µ†×u(¥Y	[%çsq\X;)h°”ÄQÚÆÜÊ©V{ÌÔn£->7è´™É€‘ÁÄÜ —KåØ@ı¥E\”¦Ksn‡1lŒYÌéş»tæwÊè@;{˜¬QLÆï>SkòĞ¤ã‹3Ş<rúì”çÛS÷‚pÁ·aşÒYIÅys³åüê¹QıãûOŸˆ)H„k'Ç­Òeì­{óòWôİ×?=qqãÜÂ#ŒÆG’Lvmu99bµÚ4Z›Öî°iì¢17È‰&„·ğ5­`mTQà†5ûVÓ	ÿÀP1{û!ş¬<ëşêsòüúrdÉ‚Ã[êW0ª*ûgÁJêQ7É£Õé0ã'áfhP‹T@H•q8LíMÆ²…9	¯˜HP™îKdß5üÏ®k‡Ÿ“_Ç·ŞzkåÊ•4nå'O²:¬U€h‚yfH1f›! ³;,æ¡A2rƒF#U¸F»Õ">Pl`8ÆL{V´Ï¥wíj¿áñªjyéÿÖ[1¯~m^ŞjÁcôwaØ]ÌV‹ºK±X£fA&œHËiuzdB|i“*üîÌÆ7ƒÍ_„wÔš‡—kåµÂ(÷Åçñ­Ñr¶®˜èå”úˆÇZ€ùû®fl‡¦ÏÛãìp:œ‰ÎÄtÚGÉ+§trPù"ş»ì]Æ›N¯ãWr¶ì¸E\·•w|íVuáµ••l&c`ÔĞ‰(KjåHLDHíñÄU*uœºM[?g~E;ŒV“ÎèQ+Óùš¿Oj¹çk’s§D0×åˆ3œ)µáÇÄÚ±§4hğ¤@Z•>˜?ÂJÚ”åM·»cÏ^É‹›?¹«şi:ôµvsRÇ**™8rßû nP¿{7ˆàı“qÀÛ…R$§ĞE.µ+*¤ ¶¶êíïAô^!jd(¨ÑE¼…½˜PB'|³o£x3<øä.ƒÎ½zª>$Y·¾ ›½?O)üæØ¥†µ¥6QĞµÌ$ü2½û¸…•í{çÚß~¨ÿÛw×_[ºiËêÕ«·¯$qòà]k0NNàå?ä¯ÿxáO~ğñ˜í—Gp½¸\€ìg¶?Mı«u¼İ¶ß3W¹‰V9ù·l¿L¿£‰a.µD«—<ãû<;,À –Ó¶üæÍS¯Ìš¿qÑ¢'Î"­êß®Um“ÁÁØ›ÁÆ¸&Æ—¿xıãÏ>zómf=Ëh®Ÿb=Ó%w¬İIu:­]ëomËi°8´n¶“‚(g¦)86C1L®f:ÓoîÜ¨K›ĞBÌs7w$"@8Ì‘ôm³ß>N>Z²~ÑÌYó×-ãúãæè2¾¼“ì~d,Âv’QéÂïÏ^üôì_˜}d.ÚQ[Éf€h^´;œ«•	ZMZ£`W¾Âi.=€U“ä$$˜T“@š“³——<ıæ!wÔmT|ZÑ‚ÂÒqtƒõÛWe¼6àü˜êòò	éfñy›Ö`yĞƒR;QğX££tà–[.±Gç Xp'¢Ë£‰–FG;LÌçÇÑ¸?v÷ıã/cã¦½2/8‰­Ù;´¦Ø¸Ëƒã×úïçÏÿÑ·İú›Ø0z¬üãÊÎ„>ˆŞ©ñØí¡=öÌª!8}ó¹Ë<Ã½ ŠêÙ¯lèºçÎ±åôÛØ-Çáióà46‹ã7éOü0 [†äæÕjb³N³¤Ï¡‚çàvbJÙ+ @Šù×Œ¸5=`oå26†½étóñ½]gàœ›W¼è™=ÏíÜ	–GË_¯¬¯4 ÕÒK×“íŠmz¸®@¶ÈºÇ.—:Úm¶ÛaİÛz»
ä¯®{ÜA+NitàÍøÑÑOÌİp8²ğ{<3óà³\×ú![g†vŠºıáµ_>ªæ,Q|Û,›Å€†íE‚kJ4D§UcSxm¿'¼Ø‘øÚƒ31Äœï|$zëÌü‰Øv€JéµÓ¦“S ÅPj•y”:`d1¨Àk-TKEW”JŒİÑÔ`ĞŠQQ.•h´h§ij‰–|È Û`¹ò9C3$œw_¸3\h"ÛX-öŒÎV¶AØ©ıùìª.‰»ß9rp”/Ñºøõy^§J§£cCøo/«ÿ`ú´ücx·<bÂ¤¸‘…Ã£H!`ı0`ı(`­e> Û1ÇQ¤xP
¶QÔp˜SñFÖÎg‹O, »°Šo(t—|B~íŞ.Wü'ãvgä
¼“ûdbğ³õßÕÀøÒtÎRå“]$·Em É¬ÕhÌv‡A­æM#âs›‚Ø@K²t	3·
;Œ;ØáìWÆ­û¥%t´,Õ"·;‰Ub[œq\¾/xB¡],LŸÛ‘K©âRÜdj¹óæ•ã€É: B2`¢ìˆ«ˆ„F+P<pÎˆEæU"û?İ14nØ×‘=õsè€úáäİ¥4aÙÒº¿°ÿ2Ì4<?.¥™ü8•6ÎÅSÚ:DC%ŞU)ªUªwU7T¼™ªT&¿É|;^_«Q|d3°éÕZÓB˜-Ğ#é=0äŸ]Q{á×ñ,Â½ÛiÌ¼]kçÎ[³sVT[5~ÜÜÜ‚ä{áÂGfğKùY¥¸hésËò‘Ÿıdq­/?;1ø«<‚Uv(’ZùÒ|Å»ßç…ßëslSãÇeŠæ_ïïÊŒGJéj—›z­àgz)Ï·W»cÜ10ewŠ{•û€û]÷·`¦n·Y-·ƒÖ{·.~}ÒÎ°^bê!ò‚™½ALDôN»Í[ğ?ÿQÁàªqãªrú«>Í°k<bYp".·ŞE¢6ã‘F.{n©¼cÂL ÂÌ‰òÓ‹wÿb‡f-ˆ<Y^À·ØáHï°óxíåßÉ¸ÛØ¯Â±4È’À~mĞôqY%-v›p™;ÙâqR:‚¿_¶%Kêî¶åcıwÛF"Ü@Ó8Ô•H‰¢#¬r{wR2rºœƒƒ1Ê—pV
‘y42µÉÃÈÂuƒZ—c2j[yÒ:8{c(‘¤\Ã_OµôÃôÅ‘à×ß"&Ngñ\À°7‰9+ƒùæ±|'š_÷âôÅë–-Ü¸h&·¯. DÃ!Á¹J‚ù©ùO=5¿¾ğoœÿøİSï =‹«Ğcx˜|˜‰ŒmSÔŒvÊªUÚ
·Åá¶h+ê,HÕD;ŒİÀËà¥µ’Ì*JÙv æ–`ae3ŞİfŸÀBXá kÉk»äÒ¿‘'p57lÕÕ6¤üJ]ØS¿	!>Xÿó,ş›ğïÖïd)w}c> ‰°_°Û¡œÑXÎñ÷†CÊ…º!UB™µ}ÒM¸Ÿ
i6¤õVCª‚4>’o„´ÒBH+ÂíqQxŒpj‰Ú	iJ$gé»<R(RÒÜHyË#mØı H ­„¤‰Ô·¤¾ 3äÂÏî@ymß— ÍƒTÁ™å« äÓ ]…öZÈÇ4kÿR¤í·‡t<Ò'£éÃzAZé2ĞÚÊÚı{¿·şl.ÿãşÿx0ŞşïÔ3Şÿ×`ôÿæñŸµş˜ëş«aşëø×ñ¯ã_Çÿ„ü7óÉRÜ
å $€woB)è!„èQjü"z±É·WGÊñÜH™ ÏŠ”)ŠÆE‘2×¬xH¤,@™ıbsj¸Û‡~)cˆ)fEÊàNŠ”)ê„î‹”¹fmxg¸,@	¡hÆ¢©¨üNöŸy&£Êµ<yV_©õ¢4Ô¥ÂÙ¥£P?OF%J+/jé×Fó67ŒGÓ Ëbhño·í5ã!±'³ U	<+QZCi´(G3¡/kU
µ^ÔjÛ*X¦¢¼èhUÏ'A/êå©Ğ«¬Äà÷şwGKƒÒ9Jïd(õ…şcP‡FZ\9¡lòÀ²ÉeÃÇN­€¢7­Cjj‡ôcÆN.;ÕÛŞ{·™—µ2vü´IÅSï©í3aü„Ê	³Æ–xKŠ+‹½cÊÊgN0¾´ÒÛfL[oZjÇTïeeã'õö.›Z^îØAÓûŞfiŞ!0DNqe²·ïä1”ÿD ‡ìGÃº7îA¨g
±Ö@”Ç$NÉ‡ãaÈ†<8räƒP ?õ gÏ»£î¸äİ }WÈï‡{–§ãN«<¨gÜ	™ %u€'”ƒÓPª‚+†®íıR¡ÖW)\›µ#/\‹ @ºƒrGw8ˆQ^-n°;Ë’_BòfX XI=`€Ş0@/È{Eî3á¾‡4>ÕãÛ¹m<ßf·ñ|“İÎs3;İ³êúöë®Ó²«n7ğØs£ğFÙŠ®JW‰æJvƒç¯_&x¾ş²»ç«/ã<Æ/qìå/²=Æ/°ôE¶Ãóù¥lÏ‰Kï^ºx‰J—Ù—²]cØ†z`ÀµJºî4ïb÷Oó>ëşIêiÁÀˆ%;Lï \1LËr!Ä^Çbl–†ÒÏ§ø“<ï'¹ŸT}ú„3~‚ß³<…o”½1çzâ~=7ÁS~{§?yœ–¯:NŒÇ<ÇHÊ±ÌceÇ»xŒ?º?Áã­M­Í­-¯­ªåÙvBL­µm¶éöÉ=Ru$t„«::LŒ/e¾tã%Z‹õRÒŞOUhuˆ„B'Cï…hÊÌdÇşĞ~rrÿ{ûIÊ¾Ì}dûøäŞ÷ö’zlDi0æsÀlÌÄ ¢fÄ&És·m-ßJ7mHğü6;Á“ºQÚH ‡—68b².êsöÓë»yvôTã,ÔdìH³¤6%'İãúëO¬§ÒúØÙÒz‡.:c¶q]ÊºÌusÖİXÇ_Á:T†u’—¬]‘àY3´Ásq5N]=«SV“²ÕsV´Ê´Ê»Š*Ÿ?¬rÅd{W¦®$ƒV®([AS—cãrÏò”åTZn²f›N`-ÌB‹R!Ñ†“X{ĞéÍ>Ê
R®É–½l^‚gi¿n%‹»{/èæYÔ¯Á³}!6-ğ.H]@Sçã9ó°4O­Ë® ş”pM†]yQW yp¶B:Úp	‹=	ÙJAòXc²™ãy(»£§ ò‘[Ó,y<¦y\IWvwó)>Š£°ë`ºGª…ÌÙ&»k¤xpH®ÛscpÃ`"N¿/[ß&ûİ\|q ëéŸãÉ­Åni4îüèˆå@z Òl|1ûF6©ÊÆNlÏs¤ÙóÌØ˜gJ3æXiÖWŒ»Äã1fsŒœÑ˜bd,3®2^46ÅL¨»a¤e”ŞáÀ<®Å«k†MJê_+6éRç„ğ’PüPv•	KB(odA~Æ+ƒW¬@½bû‡Ò†æ‡ŠbƒıC%PX¡

¦Øê¬¨¬¨œ–>p¤X’’*+!Wn”'ì§ÜIf78©¢²²"R=à®2išrMª¨hìÈÚB¾¢±N•I¸±z1 ĞW"¥[\AÂHW$¡‡+”Û‡¡ŒPÆ¥	·‡+Â˜V4BTBÿ½ús
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
xœ]’Ïnƒ0ÆïyŠ·CEB)m%„ÔÑUâ°?ÛĞÄt‘Fˆ=ğöKlÖJ‹è÷ÙŸmÅ$U}¬­™xòîÕÀÄ;cµ‡q¸züc™L¹6jZßªoK‚¹™Ç	úÚv+
Î“'?ó‡ƒÎğÈ’7¯Á{á_U¸¹:÷=Ø‰V–\C*½´îµí'h[Õ:ÄÍ4¯‚çñ9;à)²¤iÔ at­ßÚ°B„SòâNÉÀêñœ\çN}·³w![ˆtSFªö‘¤ØˆHÇ5’”‘dJ”eiûŒ=—êÛ¿^÷ÑĞ$DN=Ö"IjfDË$‰Òšªd{×qr±II|¢AâÅ,EÊñ´ÌJÓÅ«Š+½íA]½+À½ãİÇ[7n¿†\tÅçn¢ù
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
xœ¥z	|UÒx½î3™é¹g’	é†\$$!! ¤!ÉH"™ÈI !ÜKıÀ‚+²*(è¢+2•€P÷suW@t?]OXo×\Q×…ôüëõLbàï·ûû¾¯gªû½zïUÕ«ªWU=	 à¡XhñùfN_UyüÄ\AH˜Q‘•³î‘=. ‚ º¦`Ä‚û+±ŸQ×Ñ&ŞV°vö÷0OÍoYĞô«à³f n&€æéÁÖp€ V‹óM–¬šÿ«wÿøG ƒ	ÀailÖs·r7àø_p|t#"´uò0 /klj[ùÜK¶ö‹‘GÇ’æºàÉûçSyz›‚+[¸ï¹pêIì‹KƒMÃ'Y°åy³¥¹µMN†Ó )=t¼eyCŸ²÷6ì#?Õ?Gw™wßNú|¹ôÄ\¥ÿpİI`¹SÌ1Pá¼ûT¹8qHäÉa>cÑªFÇ0*†ãàškä¤ŠÃx©Ì2êAı8³  äÄ¹Q/ãTET0âA`lx'Ê“—‚§#+€#ªW!ÖáJ;Ü¨Ü¯º¸q¸rÎıJYõUx^¤-Ï
ÿx­lÿ—K«ÜII†oáÂÀ{„ƒ'á"ü‡ığœ<›¤¸ˆs>†Kğ¼üËT‘^,IRšgáø^‚í¿8O†½Èó¯°™ÜÏ’¤Z‰ŞÅÙO7<€ÜÎ=È½H<äcòì'×“‘ÌNf)1Â‡Ì†«iÉƒ”¾!Ûñş¹‡J®ÚÀÆAˆ™›˜G™JøÊ`¶2M†WÉ8ä_ëá7Q­°îñ’áVØWãÑV±Ìôğwğ,œ„?Â;p3lğà•¯t‡/!ÿ(0qÄNôÑ%½ıkÕ³-Ì1FÛw/Ü‰Ÿéø©‡zò¼ED¹	¥;	wÃk°ŠH×MR‰Î¡~šàaX¿†gà	ø™IÔpì …¤(œ»HD“,|ªzHu3Äªş¦+‰áï˜ËÀsĞÈoÀ	¹1ÂŸ­ƒ˜>>ü}xeø¢üCøC–eÖpqªGUU/*òmàV€{[ñ¸ÿ”×ÃF´ÅßQ‚ÿ¦ÔTû«*gV”—•Î¸qú´’¦OñL$åOœ0şúqc¯3:odvVæˆŒÔ”ä¤aŞ¡Áe3›x£!F¯ÓjÔ*edˆ!(
±I¢ÙôyƒÅ#2Ä"WcáˆŒ"¯/ƒb\²·¸XAyƒ!1 †’ñ„„$œ9ÿš™Rd¦40“˜Äñ0²ğŠ¡S…^±‡T—Ua{k¡×/†¾VÚÓ•6—¬tØñxp…"•V,
ù:»Š(#éÑxô#2 [ƒÍl…R½-h°‰Di0©EãºĞ([ÜiQ°>TZVUTèöxü#2¦†ŒŞBe
’!uAH£RÑáv±;ãd×–Ì¤ÇÖ{ëƒ³«Bl×v±E]]›BæôPš·0”¶úcî¼!”á-,
¥Sª%å|J~fIBª$“Wìúp;Ş¯¿ºŒbÔI¦ï6CLAˆ”Wyèåö¡®»º|^Ñ×è
ö„;çyE“·«;6¶«¥Õ¥UH¢'|ôvwÈ·Å2É8të¾ò’µ¬¦*Ä$ùÄÆ bğ›ïõ\çö˜æ”şwÃ€jAå †=ª†Û{$˜‡PgYU¤/Â<÷A²Òı!&@GNöØ+éHgÿÈÀò€m[RQÕâ’¦Ö{‹Pã·CóĞ»QÃxM!ãn·ËbÇfù•¹"J5µ~¡R%£’pÕàè7tI—Iéˆ<¾v#ƒd³EëE2”N‘·(ıv4º€ˆŠ.N8ÂÌªTˆ)µXQwv®Ğ`c†²¼-!›wò€u©XE+ª”%Ñe![A³ztU(«H9WbQW 0"¥å-«:¹áóİ£D÷¡\şB:ÙQ€^–\ÔUU??$Üõxîæ‹UnOHò£…ıŞª?u;ÔPÚy·â~ÅWfV•TxKÊª«®‹
 ä¸¤¢kÈx«Ü2è€!m’V¬bÜ¬'š!ú°á<ï!M’Á„
W°Ôq'«01ôÏF1BibQCatí_ETEİ© ¸Ÿššv‘NA±Ûã÷D®‹QÆ¸BK•ZÜ?„a
´èŸÅ
ŠêÒE^¬ò6xıŞF1$•VÑ½Qõ(Z*CÑyÔV3¯êRª	<8Üß¡ÊùÒİƒ•š¢ôºÅ×Oí»´Ş’Š.JÜ%ˆé/ij¨K×™İJ, Ú‹±W4á‘VtW·$ÑÃÜ8ñN­ïòVTWfc<Yç^MyY „”Ìœ<"CÛän/Ù\Ö-‘ÍÕUG°ğ7Ï¬:È¦ 0Ùß=Çªˆ˜4,C±I;"íPJåØÑ*óİG$€Ne”SJ¿®‡€‚ÓöãÔõ0œ)Â(Ya$amU×ÃEF¤şÙâ´\§‚S®n *“ô*I+é¤XÆÀ¸»	EDÌQL¦:‡b1»»qU¹‚î!İ:É™Ñ‰3¤ˆ„›+f]Y]u(p™rGF“é…îâjDccZ)ë©£¬õ7vüô°Mƒ_"Ş‰h&ïDDÒ{&‡b¼“)>Ÿâó#x5ÅkĞE‰ƒàòN´}iˆP¨©òà‘ã_qw™¾¦–òcPé2}2‚¦|,ñ| XuÒºÔûo>×ÃLü<_y<Ï$2™§Y/{{ğ_~>û|dVæVp¯ªÜªåª×ÔõZõsêKš\M‹æMX›¯ı•öí;:«n­î„îŠ>Kß‰Ÿ·ct©ì±Îk¯[SËÿ"õkÿvñeı•¤+}ª»4Ÿã\í@ÑÆ`ìæ"ê@‰R¬4,°Z
‹)È:•uÊl!cÇšsÍ¹#³sÍ3ë1{Ö³Ì™îûLL³l‚5×½ìff+RqHz|›P8ê'Ç ?]Y?2›äyì¤Áy—.áü7‘õd$ÎwI1¨~NdWX¢(7dd&ob…;R>ƒóÚÃ_q³TÕñø~0SÊ’k³©cA‚È»‰[â„„m	{N$œIPØ„V§3µùuÖÕæÇz7?\”<ŒueÕÎjÙÀŞÌEFx‡2f“Å“c!£2‰w¨‘Øm‰$7gtR^®›†KßÿôaÿùwùÓáUå7ÍNK¯.o«—¿Å<"ï—w“:,Bd–¼W~4tjîÜS¡§NÏ}góO?¡Î»p“X#a‚$bÕDObY†áM¬Z¯Q·ú5½:– iõãkŠ	¹®üÜ,E\E#ÎÜ¨ò<f#ñæåŒƒ²ßMnMù¢óö÷®CzgÙ5å-o®^|yËYä¸9V¢Æ†Pm¹	1ò	Z;oOx£`Ì2Ö›*k”bùb£Ñâ¶Ä´ù-L"îöA"Dõ•
‹j+WùRA&’1™¼QÉŞ¡jMÒDT“ÃnSkŒDã±¯É9ÒİU5·¦ºÖ(âúşwäÛn{á?™;^\úşöe7•/.M¿?ı‡ß6Y¼ó–ÂÏ¨Ï	Á5 Äi°R*LöšÍjp'$hÔv¯—Úyxº†M6¹³ÙÔîÏ7Ï0o3ï1Ÿ0Ÿ1«Yƒyˆ™1pf3+hmAÃêÚÁæµs”¶e¬yìÏ»‰Üg¡>`ã¼C‡¥$9Ğè¸µt’i({=,7'‘ĞMÚ	× {áSù;'IŒ{}aÇ›æÍ^½±©æ¦­ü™ƒ°oìx»u÷÷?MVı•Ş¸c³fÍşhNEI ¬Êvè…êG¯Ù›ÀYÇ]7¢g×¡g¿”áÔ@œËjµÛlZ‘IÁ¦µi9·ÛÜîw»9»İÕê·«9´wõî”>³œºÿÙúÌĞä”$Å›•ıh<VİÃF³quë¾~ğÏáDçh©\²ºcQûò7#Ù}!çü{_ù–¼´å­'qV—w¶7®«a.Ÿ•Vÿˆ`J^ƒörb|œ%eZÕ†ØXšjX’ÁÀÛínôf»É.ÚYkÇ›WÎ£ç—Îc´5Ø.ÔÍˆMí
f œNµƒ]q5•b»Š«‘ßû^ş–ğWI—L¾eyçˆœ—?mV·vÌ³„ô¾ıi&Ed©zà±¤Ûß>[RúÅé¦5Í5Ëvw¢6âY)Dè!C²³§Õh0JÆÄ‚V§m÷ëÔ,åDôk×¢Ä(<tfÉB<y®0üšüî}…ìóÜ|yoßa ã%c>£Ù¦	u@]ÅÁP7Ié½!Şšh° MíE•ef9ôzO²'¹+0ÖdJèğ›4lzÇµªŠ„„Ar-~ïÍ5zL^&ÁGôH¢·’QŞ¡Š²¬Q½Qµä.|-·§sÙÖŸŞûèÇ;–oÚ-;òl­ÿ°§¹©aé»‹‘_{óÏÇ:Ú¹¸Ç–î}áØ“‹ö99ÇSäÃƒkrSÃÂæºsKĞ–ãîÊöZh‰u¹0 KÒht<ïiõó¼Àgñè	<ogíî6¿Oé¿÷sÀQÂsrähQÜ9oH¸ÊÊåoÃGßÈ Ú”­Ë72Éûë@¸Ï/ßê˜]ÓÔ4»¦ƒ9"?*ß±çÉ¤»Î-©üáµÿº$?½gõİ–.ÙÔi)’›¸	JFL•l–å ı@ÅíªQñi*"1NÉVÑŒ%Ÿ‹d-6VÉ]îGï‰Şc¥Ğ•ŠÓr:]¬ıL[ë×XØˆ©õ#Ç¨ñ´Aç€VŒ÷èifÏıìù2æÊ2F~EUôñ•Ì®Ã¾Æß‚”ì’UGà9?t¢PÑ`Vqo¾ĞÜ¿­vw#$ÃHH¦aš‘#íF>ƒeÑ@¹9)=á“’h²§h$ŞHbX£Æ¨1ƒ9¦Ìo6¹2!³Ô/‚òse
€hn5¢ÊqFÍ‡Û™­¢öOúƒ)fY‡İL­6Ænd©e½FbÕÅ7óÈáûCg_;ç»qj‘V~w4¹óo¥e‹‰q©©#5èÕù½øÕeÃWo¶ın×¾,7fÁ¢©¥F2é¥“òÊš"õ=j½šklXVÏèÆ35ÿ{ÛqÇ[pÇKT¯¢Ÿƒë¤!.+Ç±‚5$%›JıV“C?´Ô¯Ö›°$±ã‰ÏÏ¥vÎMìŠ˜ùFç¡¥5¹4YÌ6F‘™ÕöstUoÑ’8†I{´ùèË>ÜxÿN§6äóÔÏ[¶¹;/w¬©—ß‘¿“åÓuAO{<ã]ù˜¿§çğñ“4.EI+Ñ6.ğIÉ<«·ÙtxjââÕ†R¿ 'z½Ú6“1°6€¹ÔOM¡X‚ K‡9éƒC)Õÿ@¥¥ÙD‘ÊÈ0-?È—ˆñ'ş)ÊŸÄªŞ~¿t‰Äó^·‘$¢&±$ıäãÆŠ:ùn¹«¡ŞĞüT-ê1ˆÒMŠêqœ4$Qïb­V›Ş–”lƒ»Ôo2˜4R?«q(zŒªoƒ³ŒR^z”iÕEEËMAÍÚœäç#=‘°#¹.o÷âC§Ï_üÀp†!qZù£–ºúçåñ«RûIa‰¤ç$[/‹õ›™¡û{Ÿ;ÜsØÿJ[Ò.D]Ú!*¥q±±¬ÅceÙ!‰¦ÜØ2?'Ä1&6.4G™_c>ªÔÿ&8ıìİå¢ş f»G‰DcTjE?Ç-2Ë¯Èßløæ‘¯‰ºoèÆå7,·İ˜0„¬æÈ«š56’FOÿ£Sş½ü¾ö®'ó';·ŞËvß¾fåÔ0$qóTCÙs¥x+!j†‰u8õ(›`ÙÌ¡×ªxQrÿ9ì7;ÆLT'†%8íT©CˆÇÎl•?§¿µ¿û§=ûvvÎ›Cc×^¹…]Û[ñÔ„kYÃØ^ÔÚZùF®š+Á|•	3¤TeÓ,^—^/ZÄ¬ìŞ\êwÙMÇŸQêåí )ó£†óûÏÕÓÿoõˆ\µÈ2Æ«ä ˜»<jŒjvPXgşÍMâø¹“fÎ—‡^:}rá*|MÑ«Ã–`ıÂ%µó›äï»Í3iÚÛ®oıq¢G¨‰œë]i]rÇ•¿~t‘ı`ïÑg<õø1ª×m¨×Rô`dKN›ÉdÆ”ovº,`ÖØ!–-÷³¦:<P @á#µ.ª6""Õ±Ù¦!{Ç>¹bß>ùó²Ùó×ÉŸ¡—²óÖ¶¼úç¾r¦é7+ÜÖw\õª¼¸©‘FŞä¾¹ëÀ€çG0 )ñµI¥2ò1úŠšĞjJıZ8íËÚÒÂ@ÒqF"QR4!äy’0°³ñ$xù2¹]ş€¹òïííez{_<s†rl—g±ähFO%¹-ÚN«¥¢Æ
&ô'ÏéËıœ;êñp+©¢%dRğ,;{ÛŒ½#6¯_:[~€YKù6™o~}èâ&v¹ÂÀ~Üï]È=$IÄà…o˜:ˆ¡©5†3Äê5„átZ^1KFNNú³sìÕ%@¤æò¢pâÑ6 Ÿ[EY’›I¦|¹—üm¦¼Hõê•§ÈI¹ºo	¨à\TÓfÌÚV°Ñ¿'%9íIÉ)ôCwav8Î+a~[~¤nvz¼“¡
dìîÙwèäN2½*óOiá|vgïå-7¹Ã}ò>ú'AEHûfŒ+)ô|8RR u¼V«u‰©iñŞ2|¼ÕÁóV+W†É%–t‘İEkIü(õÜÀ&•²’Öë®å5JÉuÚ•\ƒ§#êyŞşaò}RNîõŸ¨Ïª™¡7VÍ²2©Í•ó?¦Xæ×w·»·ï([q|øúìùsõ‹ªŸ<Û—Eñ=Ô÷[ºƒMôp30ËdIN3Š.+.ŞÌÙ¹r¿İdà#_]ûFç•œâÁ×"*œGØë¦ÏmDÿW±ø‚«çğLRfñÖ[º7õc‹g5gXÖ¶È¾2ôÊÙ™—¡õx±Ö2«c°vºtÆR¿ÎÄÚĞùp•+‚J2ÉàÚo™|1üƒ|‘eF'¿3ÕÚ¦æ¦µ-L"¦Øw1•0•ë{íäĞ‰ç»Ğ3±EÅ-Áİ;!	&J‚ wqJKIvòV·)Á€5ÁÁÕ`Q 1.Î\ù×d2U ¦HAà¤šI!ƒj#!»Õ:.û¡ÅOŸŠ¦2ù3-2ªVj˜¯ä2nœıWCjçË¯Ë²ü£ü&f3y.÷cıæ¾V<TÙûlO¦3´ÚKhµ±¨5¤I6£Z­ÑØì£ÅÂ”û-¦^­”.WYl­¨'9¹±-õ»ËŸ»ã?LÏå<±¹q>[jıêyùæø´Óu7ÏÛÜb¦W¡¨Ÿ¤B•”£Q{lîx@¼MÍ¥÷œ¬3±ÔpŞ-¸=ëv;M¬#ŠFÔ0µ!­GhZ )4’CÇ^“B•w—ä”1ıúJÉd"o0N­W¨‘‰åğGç¾NùÑ¾ ³cÉ¬Æo›uáİç¿òSìÜùõõÓkÖÿçŠ)düı‡¶Ş4]/š`Ï*Û0w×şwÄO”;>kŒ%~Ì´¸£‡Âßq1ª™èù£%·#’Ëe‹·¡ãÙ:Â,cx*ºùS«7/×šKKr³bc¬bQL,hHñoŸ©
‘òzÏk7ŞÑ!­ÿİ,L®$^ş´·ï›ª	^÷Q§®è®[éùC½çÆ¡÷ãùÓÅ[,xş,ƒ]ü/Ÿ?¢”ÎJ%jsz’óhMÎ3“ıÕí´Bº«ZüşŞ'¹q}uİÕ½‰)¼ÒÓÕ¸}Ê—gO3³€>ô8rÖCä$ V3:=Ë0úúÓ”ÅÓ¢"7?7—ÆİŸ_6•¼“FˆÇêpN$V«–CòB’v–¿N=á<IF~¿ÎyÙu†şš`¼îäâ„iR,VL2ZÁÀYYÃ‰;³0ÊğN‡#§†ôä:6klîÀk®Å9ğËSn/›œb$¬—Íµ:ìc¬xwmÍå¸KÛâbÛıİá+¬¶ûŸßÂm³?$o•:t%²“êân ßÈcsò'>ÌQÂdŒ¡„v¨‘lŒÎÊ–½Ù¢·8œë‘…‘¾¹yK1c´gÔëtV‡Å£çAUá‡hºÌíÿ­…–ˆµË+Ì©Ô;)yÁbvŒ¢¸1n|CÄpP´hZnîøù)²DÒzS'èÊ&É²TÚ+Ï2¼¬b“«rY}ß6ı5‰$1ÖË[O?Ñ_1R`í'Åk8¢cÔD­Q³‹é›'Ğ”ûÁ~í»dTô‡;ú{…ëÀ.f\ß¶¬ï¦ñÌ¾?½Ò7ûTä·dõã}÷¨]IúçjÕ]‘ÿtÍáNÑß#wê—şƒá__Ü)Rˆğft};BÂ„9Q\#Â:„MËûçÿo.\ÿÿví¿¦¾¥¿aÂR„ B}t_k¶!tDûûÎ!!lB˜M×Ei¼„°
á¡è˜€K¦vW,1—…bÔ“3˜	²`6 û6kş_°×Mäõh› O^Œ¶àÈ‰h›…xòh´ÍÜm«ÀH6FÛj°’J£ix~mH„Ç¢m´ğ@´ÍÂ(Xms˜1&GÛ*|7H¶ÕØ˜a4ÀrB¶›a)LWîÍ0×5Ã¨‡›”­Ñqrğ}$?™÷‹Äâ I¸¾ç-Å6-"}ñß¬î_û¯g"fY³êq¬^™ÄVÎhU¸–ÎjD¬ˆ©ƒ4eÙ0A„)8«Ç—àz
°½W5_Å1#uÁ¿¥–ƒ­ò¨ÅÊêlMÅõu9má¼†åÁ¶…ÍK§7/m1¹yIıMË[±/ædfggæı<A¤3D:cRk]ÃÒú†åâñša:zªpá‚…mW7Ô‹õÁ¶ X×Ü²jùÂmbj]š˜“=2[œÒÜ¼`IƒXĞ¼¼¥9²0S_pí´±IÛ2Ä©Kë2!òŸcxÉ^ˆF¨«¯Ié¤™•¤<ú¼‰ÌÄúH •øğ9rÉˆŸ†O‡½x¿„À	0ŒÇ‘ñ¸r>¯Ç>}æ‘Q;˜4‚Œ£@&äB1ÉAx'ìH\—Xï!‚ÍB,>AÄ{ Añ3•$PÙCFœ@‡ SèœG
éÔ&âò2Â(şäh.“ğ)EûùH~¢ä®4õ‘o}ã…‹¾°¡ù3ã«Ú¯˜¬/ó¿d’tœ3üÙÊ¿Mø¢òs2ÉLÒPÀ;Ê]Ä{)B EñÓ$	}FÖºíÓ=Ÿ²g>!Ò'â0ß…II•\™„ÀGäÃóñÂ_Ï§
ç&|Pùş¶ò2É@†+ûÄ†£n†CC‚Ã%ø€¼Ç†…=oxƒyååñÿ²ğ2óûãéE«Ë×C<_/ôQÒÄÁ$pÙ©¥!½©BV/9~,^à	ÇÖÛvŒ;z$^˜qxıa†ï%*Ô
ö  *)†{íá‘ƒlÒrz¢X&9Id!00ïµÍN œA¸€FĞ‚D$ó_hÿx¡t`ÿùı÷sRI<h²ú„O’!’=–÷ıî	~"ğÄù'.>Á=³¯ELm{i(ûLûÄ}ìƒ»S…Ò==Ì»\‚¸»t7Ó¹kû®‹»ØìIF2CuC½×/Úb½r?@¼R1İ×yßöûØí÷’{~“*~CšwÙyn'»}'9N¦"›÷‘¢ƒõè6n|+"¸C’0á^³•ş	åŞ‚÷í
ö5¥ÏGg &ÉÁòwçßÍğ;¿#kGşõ;öì¸°CİC,Ò-)Â]¿N¶ãóÂVÂo¶0ô–µeÏ?FÌÈŞÖGú.Şâ›±‰ÔŞŒF‹—¬+2„ÖT¡½5NhCh-µÇñ%İÑH .â8˜!¬?İm{XÔƒı`\úMÊöe-¾¡a)ús<qUÆåº*5¹l¥]h^í0!ˆ@¨-Z=º›şf®o˜0£‡X¥82Û'ÔTçÕ¾xÁšc©T¶’Ëañ˜i%[x–T Tåe¥‰Â¾Daš/SX_BJpe1ò¥
høX©9Æè»Á— \˜Ê”N%S}1B~ñŒb¦Øç¦ø¬ï[ï»àû¸„zw¥“Ø+9öJ3á+M9|%ƒ'œÆ
Ïçkùõ<ÇóYü¾™ßÆŸãÃ¼&qx¶0@‘NQ¡·wÏ¬HO/éÑ„ËKBºÒšÙJª w©¬:¤Ş‚ÊêšªnBîğßºu+LRÊ©¨
†øKBõØh£¦!İ˜ìomkmkO\¤-=½-½ïéŞ¦ Z<m@¤İßW† ÒmmÅa$D‘m­­­mmííí(ÚmÇQlaq”xkºÂ¥µ•àHº‚Åõ‹(ihÃ>Ğ…Vt,BW‘¹A+‰é—P!ÖÿMïÔğÿ ©š
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
xœ]QMoƒ0½çWøØ*”v•RU4‰Ã>4¶ ‰é"…ôÀ¿_°»NZ¤½g¿gc'ç¦n¬	¼ùIµ`0V{œ§«W=^Œ2mT¸!úª±s"‰âv™&Q– É{ŒÎÁ/°9é©Ç‘¼zŞØl>ÏmÄíÕ¹oÑHEUÆ!:=wî¥’mã&,Û¨ùËøXBFXr7jÒ8»N¡ïìE™ÆSAùO%ĞêñœUı ¾:OÙyÌNÓ,­V”	í„v¡‚nšı¯Ã½ L)MJvªI+ÙWîéÉÙ^>2Y3Yp•WaÁ^YLè9dLrwËÇ[[ÜÈú¯ëNîƒTWïãiq4¼ulÆâ}·nr«j½?ï&–¨
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