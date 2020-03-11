
# Uvod u Python programski jezik

**Autor:** _Milenko Letic_

https://programiranje.ba

<a name="intro"/>

### Uvod - par rijeci o programskom jeziku Python

Ovaj kurs ima za cilj da vas nauci osnove programiranja u programskom jeziku Python 3. 
Nakon sto prijedjete kompletan kurs, trebali biste biti u mogucnosti da samostalno 
kreirate programe i lako prijedjete na napredniji nivo programiranja. Takodje, bicete 
u mogucnosti da prilagodite, prepravite Python kod sa prethodne verzije Python 2 u 
Python 3 verziju.

Python je jedan od rijetkih programskih jezika, koji je u isto vrijeme jednostavan i 
mocan. Nemojte se iznenaditi ako vam ucenje Python programskog jezika ide veoma lako
i brzo savladavate lekcije, jer to i jeste cilj Python-a kao programskog jezika, da 
vam omoguci usmjeravanje paznje na rjesavanje konkretnog problema i pronalaznje 
rjesenja, umjesto da morate voditi racuna o sintaksi i strukturi programskog jezika
kao sto je slucaj kod vecine ostalih programskih jezika.

<a name="python-cinjenice"/>

#### Par cinjenica o Python-u:
* Jednostavan
* Lak za ucenje
* Besplatan i Otvorenog Koda
* Visi programski jezik
* Prilagodiv na razlicite platforme
* Interpretiran
* Objektno orjentisan
* Prosiriv
* TBD ...

<a name="python3-vs-python2"/>

#### Python 3 vs. Python 2

Portovanje Python 2 koda u Python 3

https://docs.python.org/3/howto/pyporting.html

<a name="osnove"/>

### Osnove (DRAFT)

<a name="kod-201-zdravo-svijete.py"/>

**`kod-201-zdravo-svijete.py`**

```python
print("Zdravo Svijete!")
```

**`Rezultat`**
```
Zdravo Svijete!
```

<a name="kod-202-zdravo-svijete.py"/>

**`kod-202-zdravo-svijete.py`**

```python
print("Zdravo")
print("Svijete")
print("!")
```

**`Rezultat`**
```
Zdravo
Svijete
!
```

<a name="varijable"/>

### Varijable (DRAFT)
Kada radimo sa podacima, potrebno ih je organizovati, kontejneri kutije u koje stavlljamo pohranjujemo nase podatke predstavljaju varijable. Sta predstavljaju , zasto su korisne, koje sve vrste (tipove) podataka mozemo smjestiti u varijable.

<a name="kod-301-varijable.py"/>

**`kod-301-varijable.py`**

```python
print("Bila mama Kukunka, Kukunka")
print("Bio tata Taranta, Taranta")
print("imali su maloga Ju-Ju")

print("Jednom su se setali, setali")
print("kraj duboke rijeke Nil, rijeke Nil")
print("gdje je bio velik krokodil")
```

**`Rezultat`**
```
Bila mama Kukunka, Kukunka
Bio tata Taranta, Taranta
imali su maloga Ju-Ju
Jednom su se setali, setali
kraj duboke rijeke Nil, rijeke Nil
gdje je bio velik krokodil
```

<a name="kod-302-varijable.py"/>

**`kod-302-varijable.py`**

```python
mama_ime="Kukunka"
tata_ime="Taranta"
beba_ime="Ju-Ju"
rijeka_naziv="Dunav"

print("Bila mama " + mama_ime + ", " + mama_ime)
print("Bio tata " + tata_ime + ", " + tata_ime)
print("imali su maloga " + beba_ime)

print("Jednom su se setali, setali")
print("kraj duboke rijeke " + rijeka_naziv + ", rijeke " + rijeka_naziv)
print("gdje je bio velik krokodil")
```

**`Rezultat`**
```
Bila mama Kukunka, Kukunka
Bio tata Taranta, Taranta
imali su maloga Ju-Ju
Jednom su se setali, setali
kraj duboke rijeke Dunav, rijeke Dunav
gdje je bio velik krokodil
```

<a name="stringovi"/>

### Stringovi (DRAFT)
Kada radimo sa podacima, potrebno ih je organizovati, kontejneri kutije u koje stavlljamo pohranjujemo nase podatke predstavljaju varijable. Sta predstavljaju , zasto su korisne, koje sve vrste (tipove) podataka mozemo smjestiti u varijable.



<a name="operacije-nad-stringovima"/>

#### Operacije nad stringovima
Kada radimo sa podacima, potrebno ih je organizovati, kontejneri kutije u koje stavlljamo pohranjujemo nase podatke predstavljaju varijable. Sta predstavljaju , zasto su korisne, koje sve vrste (tipove) podataka mozemo smjestiti u varijable.



<a name="osnovne-matematicke-operacije"/>

### Osnovne matematicke operacije

#### Cetiri osnovne matematicke operacije
Cetiri osnovne matematicke operacije predstavljaju
1. ( + ) sabiranje 
1. ( - ) oduzimanje
1. ( * ) mnozenje  
1. ( / ) dijeljenje


<a name="osnovne-matematicke-operacije"/>

### program-xx - osnovne-matematicke-operacije.py

```python
print( 3+2 )
print( 3-2 )
print( 3*2 )
print( 3/2 )
```

**Output:**
```
5
1
6
1.5
```

<a name="napredne-matematicke-operacije"/>

### Napredne matematicke operacije
Ako damo sebi za pravo da ostale matematicke operacije, osim osnovnih
nazovemo napredne matematicke operacije imamo sledece primjere u Python-u.

#### Modulo operator ( % )
Modulo operator uzima broj koji se nalazi na lijevoj strani i dijeli ga 
brojem koji se nalazi na desnoj strani, a zatim kao rezultat vraca cjelobrojni
ostatak prilikom ovog dijeljenja.




<a name="modulo"/>

### program-xx - modulo.py

```python
print( 10%3 )
```

**Output:**
```
1
```

<a name="napredne-matematicke-operacije-2"/>

Pored navedenih primjera, potrebno je napomenuti da Python raspolaze
sa ogromnom bazom naprednih matematickih operacija koje na jednostavan 
nacin rjesavaju kompleksne probleme.


<a name="napredne-matematicke-operacije-primjeri"/>

### program-xx - napredne-matematicke-operacije-primjeri.py

```python
print( 4 * 3 )
print( 2 * 4 )
print( 20 % 3 )
print( 3 + 3 * 3)
print( 10 / 5.0 )

broj = 20
broj += 100
print( broj )
```

**Output:**
```
12
8
2
12
2.0
120
```

<a name="math-modul"/>

### program-xx - math-modul.py

```python
import math

print( pow(3,2) )
print( math.sqrt(9) )
print( round(4.335) )
```

**Output:**
```
9
3.0
4
```

<a name="unos-podataka-od-strane-korisnika"/>

Pored navedenih primjera, potrebno je napomenuti da Python raspolaze
sa ogromnom bazom naprednih matematickih operacija koje na jednostavan 
nacin rjesavaju kompleksne probleme.


<a name="interakcija-sa-korisnikom"/>

### program-xx - interakcija-sa-korisnikom.py

```python
trenutna_godina = 2020
ime = input("Unesite ime: ")
prezime = input("Unesite prezime: ")
godina_rodjenja = int(input("Unesite godinu rodjenja: "))

print("Dobrodosli, " + ime + " " + prezime)
print("Trenutno imate " + str(2020 - godina_rodjenja) + " godina")
print("Hvala sto ste koristili ovaj program")
```

**Output:**
```
Unesite ime: Miladin
Unesite prezime: Sobic
Unesite godinu rodjenja: 1956
Dobrodosli, Miladin Sobic
Trenutno imate 64 godina
Hvala sto ste koristili ovaj program
```

<a name="operatori-i-izrazi"/>

### Operatori i izrazi
<a name="kontrola-toka"/>

### Kontrola toka

<a name="funkcije"/>

### Funkcije

Funkcije predstavljaju dio koda koji moze da se jednom napise a koristi vise puta.
TBD.


<a name="funkcija-pozdrav"/>

### program-xx - funkcija-pozdrav.py

```python
def pozdrav():
  # ovaj blok pripada funkciji
  print("Pozdrav")
# kraj funkcije

pozdrav() # pozivamo funkciju pozdrav
pozdrav() # pozivamo funkciju pozdrav drugi put
```
Output:
```
Pozdrav
Pozdrav
```
<a name="funkcija-sa-parametrima"/>

### program-xx - funkcija-sa-parametrima

```python
def uporedi(a,b):
  if a > b:
    print(a, 'je vece od', b)
  elif a == b:
    print(a, 'je jednako', b)
  else:
    print(a, 'je manje od', b)

# direktno prosljedivnje parametara funkciji
uporedi(3,5)
uporedi(5,5)
uporedi(6,2)
```

Output:
```
(3, 'je manje od', 5)
(5, 'je jednako', 5)
(6, 'je vece od', 2)
```
<a name="moduli"/>

### Moduli
  

<a name="tipovi-podataka"/>

### Tipovi podataka
<a name="strukture-podataka"/>

### Strukture podataka


<a name="rjesavanje-problema"/>

### Rjesavanje problema


<a name="objektno-orjentisano-programiranje"/>

### Objektno orijentisano programiranje


<a name="izuzeci"/>

### Exceptions (Izuzeci?)



<a name="standardne-bibliotke"/>

### Standardne biblioteke



<a name="tips-and-tricks"/>

### Tips and tricks


<a name="dalji-koraci"/>

### Dalji koraci



<a name="korisni-linkovi"/>

### Korisni linkovi


<a name="feedback"/>

### Feedback

### Sadrzaj
=======

  * [Uvod - par rijeci o programskom jeziku Python](#intro)
    * [Par cinjenica o Python-u](#python-cinjenice)
    * [Python 3 vs. Python 2](#python3-vs-python2)

  * [Instalacija](#instalacija)
    * [Python 3 instalacija](#python-instalacija)
    * [IDE - PyCharm instalacija](#pycharm-instalacija)
      * [PyCharm podesavanje parametara](#pycharm-podesavanje)
    
  * [Osnove](#osnove)
    * [program-01 - zdravo_svijete.py](#zdravo-svijete)
  
  * [Operatori i izrazi](#operatori-i-izrazi)
  
  * [Kontrola toka](#kontrola-toka)
  
  * [Funkcije](#funkcije)
  
  * [Moduli](#moduli)
  
  * [Tipovi podataka](#tipovi-podataka)
  
  * [Varijable](#varijable)
    * [program-02 - varijable-01.py](#varijable-01)
    * [program-03 - varijable-02.py](#varijable-02)
  
  * [Stringovi](#stringovi)
  
  * [Matematicke operacije](#matematicke-operacije)

  * [Strukture podataka](#strukture-podataka)

  * [Rjesavanje problema](#rjesavanje-problema)

  * [Objektno orijentisano programiranje](#objektno-orjentisano-programiranje)

  * [Ulaz/Izlaz](#ulaz-izlaz)

  * [Exceptions (Izuzeci?)](#izuzeci)

  * [Standardne biblioteke](#standardne-bibliotke)

  * [Tips and tricks](#tips-tricks)

  * [Daljnji koraci](#daljnji-koraci)

  * [Korisni linkovi](#korisni-linkovi)

  * [Feedback](#feedback)





<a name="ulaz-izlaz"/>

### Ulaz/Izlaz

U situaciji kada je potrebno vrsiti interakciju sa korisnikom, ali i
u situaciji kada je potrebno vrsiti upis i ispis u i iz fajlova.


<a name="ulaz"/>

### program-xx - ulaz.py

```python
def reverzni_zapis(unos):
    return unos[::-1]

def je_li_palindrom(unos):
    return unos == reverzni_zapis(unos)

upis = input("Unesi tekst: ")

if je_li_palindrom(upis):
    print("Da, unijeti tekst je palindrom")
else:
    print("Ne, unijeti tekst nije palindrom")
```

Output 1:
```
Unesi tekst: _*neki tekst_
Ne, unijeti tekst nije palindrom
```

Output 2:
```
Unesi tekst: anavolimilovana
Da, unijeti tekst je palindrom
```



### Organizacija podataka

### List

List funkcije

Tuples

Dictionaries


Funkcije i uslovi
Return statementmama_ime="Kukunka"
tata_ime="Taranta"
beba_ime="Ju-Ju"
rijeka_naziv="Dunav"

print("Bila mama " + mama_ime + ", " + mama_ime)
print("Bio tata " + tata_ime + ", " + tata_ime)
print("imali su maloga " + beba_ime)

print("Jednom su se setali, setali")
print("kraj duboke rijeke " + rijeka_naziv + ", rijeke " + rijeka_naziv)
print("gdje je bio velik krokodil")