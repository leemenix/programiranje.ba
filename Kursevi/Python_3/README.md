
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

Postoje dva nacina koristenja Python-a kako biste pokrenuli vas kod (TBD: program ili kod). 
1. koristenjem interaktivnog interpreter komandnog prompta
1. koristenjem izvornog koda (source code)

#### Koristenjem interpreter prompt-a

Otvorite terminal na vasem operativnom sistemu (TBD: ovo je vec objasnjeno u sekciji instalacija) 
i pokrenite Python tako sto cete ukucati komandu **python3** i pritisnuti **[Enter]**. 
Trebalo bi da dobijete Python interpreter prompt, koji izgleda ovako

```python
Python 3.7.2 (default, Feb 23 2020, 18:31:07) 
[GCC 5.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

Odlicno, sada vec mozete da napisete vas prvi program u Python-u. 
Nakon znaka **[>>>]** ukucajte:

```python
Python 3.7.2 (default, Feb 23 2020, 18:31:07) 
[GCC 5.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Zdravo Svijete!")
```

i pritisnite **[Enter]**. Trebalo bi dobijete ispisanu recenicu **_Zdravo Svijete!_** u Python
interpreter prompt-u, nakon cega mozete nastaviti da koristite Python interpreter prompt. 
```python
Python 3.7.2 (default, Feb 23 2020, 18:31:07) 
[GCC 5.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Zdravo Svijete!")
Zdravo Svijete!
>>> 
```
##### Izlazak, napustanje Python interpreter prompt-a

Nakon sto ste testirali vas prvi Python kod, mozemo napustiti intrepreter sa nekom od sledece tri
komande:

```python
exit()
```
```python
quit()
```
```python
Kombinacija tastera [Crtl] i tastera [D]
```
#### Koristenjem izvornog koda

Kreiramo novi fajl **kod-201-zdravo-svijete.py** i upisemo sledeci sadrzaj
```python
print("Zdravo Svijete!")
```

Sacuvamo fajl **kod-201-zdravo-svijete.py** na zeljenu lokaciju i isti zatvorimo. Sada je
potrebno otvoriti terminal na vasem operativnom sistemu, pozicionirati se u direktorij gdje
ste sacuvali kod i izvrsiti komandu
```shell script
python kod-201-zdravo-svijete.py
```
Trebalo bi da dobijete povratnu poruku na ekranu
```shell script
Zdravo Svijete!
```

Odlicno, sada kada poznajemo na koje nacine mozemo pokrenuti Python program, vrijeme je da
prijedjemo na zanimljivije stvari koje mozemo uraditi sa Python-om. Slozicete se da je 
ispisivanje rijeci "Zdravo Svijete!" malo dosadno.
<a name="osnove-zadaci-za-vjezbu"/>

### Osnove zadaci za vjezbanje

<a name="kod-201-zdravo-svijete.py"/>

Napisati program koji nakon izvrsavanja ispisuje

```
Ovo je moj prvi program.
```
Rjesenje: **`kod-201-zdravo-svijete.py`**

```python
print("Ovo je moj prvi program.") 
```

<a name="kod-202-zdravo-svijete.py"/>
Napisati program koji nakon izvrsavanja ispisuje
**`Rezultat`**
```
Zdravo
Svijete
!
```
Rjesenje:
**`kod-202-zdravo-svijete.py`**

```python
print("Zdravo")
print("Svijete")
print("!")
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


<a name="kod-501-osnovne-matematicke-operacije.py"/>

**`kod-501-osnovne-matematicke-operacije.py`**
```python
print( 3+2 )
print( 3-2 )
print( 3*2 )
print( 3/2 )
```

**`Rezultat`**
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

<a name="kod-503-modulo.py"/>

**`kod-503-modulo.py`**

```python
print( 10%3 )
```

**`Rezultat`**
```
1
```

<a name="napredne-matematicke-operacije-2"/>

Pored navedenih primjera, potrebno je napomenuti da Python raspolaze
sa ogromnom bazom naprednih matematickih operacija koje na jednostavan 
nacin rjesavaju kompleksne probleme.

<a name="kod-505-napredne-matematicke-operacije-primjeri.py"/>

**`kod-505-napredne-matematicke-operacije-primjeri.py`**
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

**`Rezultat`**
```
12
8
2
12
2.0
120
```

<a name="kod-506-math-modul.py"/>

**`kod-506-math-modul.py`**

```python
import math

print( pow(3,2) )
print( math.sqrt(9) )
print( round(4.335) )
```

**`Rezultat`**
```
9
3.0
4
```

<a name="unos-podataka-od-strane-korisnika"/>

Pored navedenih primjera, potrebno je napomenuti da Python raspolaze
sa ogromnom bazom naprednih matematickih operacija koje na jednostavan 
nacin rjesavaju kompleksne probleme.


<a name="kod-601-interakcija-sa-korisnikom.py"/>

**`kod-601-interakcija-sa-korisnikom.py`**
```python
trenutna_godina = 2020
ime = input("Unesite ime: ")
prezime = input("Unesite prezime: ")
godina_rodjenja = int(input("Unesite godinu rodjenja: "))

print("Dobrodosli, " + ime + " " + prezime)
print("Trenutno imate " + str(2020 - godina_rodjenja) + " godina")
print("Hvala sto ste koristili ovaj program")
```

**`Rezultat`**
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

### Funkcije (DRAFT)

Funkcije predstavljaju dio koda koji moze da se jednom napise a koristi vise puta. 
Nakon sto damo ime funkciji, ono ustvari predstavlja skup izjava, koje kasnije pozivamo
bilo gdje u kodu, sto je i poznato kao pozivanje funkcije (calling the function).

Bitno je napomenuti da je koncept funkcija veoma vazan kada se radi o iole kompleksnom
programu, sto vazi za bilo koji programski jezik, tako da je veoma bitno da ovo poglavlje
shvatite ozbiljno i ako je potrebno prodjete vise puta.

Funkcije u Python-u su definisane kljucnom rijeci `def`, nakon koje slijedi identifikator
ili ime funkcije `def ime_funkcije`, pracen otvorenom i zatvorenom zagradom `def ime_funkcije()` unutar kojih se opcionalno mogu naci parameteri/varijable i konacno se prva linija funkcije zavrsava dvotackom 'def ime_funkcije():'. Nakon ovoga slijedi
blok izraza koji pripadaju ovoj funkciji. 

Primjer funkcije `Zdravo Svijete!`

<a name="kod-901-funkcija-zdravo-svijete.py"/>

**`kod-901-funkcija-zdravo-svijete.py`**
```python
def zdravo_svijete():
  # ovaj blok pripada funkciji
  print("Zdravo Svijete!")
# kraj funkcije

zdravo_svijete() # pozivamo funkciju zdravo_sviete
zdravo_svijete() # pozivamo funkciju zdravo_svijete drugi put
```
**`Rezultat`**
```
Zdravo Svijete!
Zdravo Svijete!
```

#### Komentar na prethodnu funkciju
Definisali smo funkciju `zdravo_svijete` prema prethodno objasnjenoj sintaksi. Ovo je 
jednostavna funkcija, bez parametara, sto mozemo vidjeti prema praznim zagradama 
funkcije, ali je dovoljna da prikaze nacin kreiranja i upotrebe funkcija u Python-u.

Parametri funkcije ce biti objasnjeni i prakticno pokazani u sledecoj sekciji. Trenutno 
je vazno zapamtiti da parametri funkcije predstavljaju ulaz podataka za funkciju i mogu
biti proslijedjeni u razlicitim vrijednostima i tipovima cime dobijamo odredjen izlaz ili
rezultat koji nam daje funkcija.

Bitno je primjetiti da pozivajuci funkciju `zdravo_svijete` dobijamo ispis teksta `Zdravo Svijete!` bez da moramo citav kod pisati ponovo.

<a name="kod-906-funkcija-sa-parametrima.py"/>

**`kod-906-funkcija-sa-parametrima.py`**
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
**`Rezultat`**
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
Return statement

Prijedlozi koje tekst editore koristiti (Sublime, MS Code ...)