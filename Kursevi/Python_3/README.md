
<a name="operatori-i-izrazi"/>

### Operatori i izrazi
<a name="kontrola-toka"/>

### Kontrola toka (DRAFT)

Do sad smo nase programe izvrsavali kao niz komandi od vrha ka dnu, uvijek tim redoslijedom. Sta u slucaju da zelimo promijeniti tok izvrsavanja programa? Sta
ako zelimo da se nas program ponasa drugacije u zavisnosti od situacije u kojoj
se nalazi? Recimo da ispise `Dobro jutro` ili `Dobro vece` u zavisnosti od doba 
dana? 

Ovo mozemo postici koristenjem izraza za kontrolu toka. U Python-u imamo tri izraza
za kontrolu toka i to:
1. if
1. for
1. while

<a name="if-komanda"/>

### `if` komanda (DRAFT)

Izraz `if` se koristi za provjeru uslova: `if` ako je izraz tacan `true`, onda izvrsi
blok naredbi (tzv. `if-block`, `else` u suprotnom izvrsi drugi blok naredbi (tzv. `else-block`). Bitno je napomenuti da je `else-block` opcionalan. 

<a name="kod-802-if-elif-else-iskaz.py"/>

**`Primjer: kod-802-if-elif-else-iskaz.py`**
```python
broj = 32
pokusaj = int(input('Unesite cijeli broj: '))

if pokusaj == broj:
	# prvi blok izraza pocinje ovde
	print('Cestitamo, pogodili ste broj.')
	print('Pocastite se kafom ;)')
	# prvi blok izraza zavrsava ovde

elif pokusaj < broj:
	# drugi blok izraza pocinje ovde
	print('Nazalost niste pogodili.')
	print('Hint: Trazeni broj je veci od unesenog ;)')
	print('Pokusajte ponovo.')
	# drugi blok izraza zavrsava ovde

else:
	# treci i finalni blok izraza pocinje ovde
	print('Nazalost niste pogodili.')
	print('Hint: Trazeni broj je manji od unesenog ;)')
	print('Pokusajte ponovo.')
	# treci i finalni blok izraza zavrsava ovde

print('Kraj!')
# Zadnji izraz ce uvijek biti izvrsen
# naravno nakon sto je ispunjen jedan od gore navedenih uslova
```

**`Rezultat:`**
```
$ python kod-802-if-elif-else-iskaz.py
Unesite cijeli broj: 3
Nazalost niste pogodili.
Hint: Trazeni broj je veci od unesenog ;)
Pokusajte ponovo.
Kraj!

$ python kod-802-if-elif-else-iskaz.py 
Unesite cijeli broj: 44
Nazalost niste pogodili.
Hint: Trazeni broj je manji od unesenog ;)
Pokusajte ponovo.
Kraj!

$ python kod-802-if-elif-else-iskaz.py
Unesite cijeli broj: 32
Cestitamo, pogodili ste broj.
Pocastite se kafom ;)
Kraj!
```

<a name="while-naredba"/>

### `while` naredba (DRAFT)

Naredba `while` nam sluzi kada zelimo da izvrsavamo blok koda sve dok je uslov ispunjen, odnosno tacan. Naredba `while` je primjer onoga sto nazivamo `petlja` u programiranju.
Naredba `while` moze imati opcionu `else` klauzulu.
 
<a name="kod-804-while-naredba.py"/>

**`Primjer: kod-804-while-naredba.py`**
```python
broj = 32
petlja = True

while petlja:
	
	pokusaj = int(input('Unesite cijeli broj: '))

	if pokusaj == broj:
		# prvi blok izraza pocinje ovde
		print('Cestitamo, pogodili ste broj.')
		print('Pocastite se kafom ;)')
		# u slucaju da je broj pogodjen postavi vrijednost
 		# varijable petlja na False  
		petlja = False 
		# prvi blok izraza zavrsava ovde
	elif pokusaj < broj:
		# drugi blok izraza pocinje ovde
		print('Nazalost niste pogodili.')
		print('Hint: Trazeni broj je veci od unesenog ;)')
		print('Pokusajte ponovo.')
		# drugi blok izraza zavrsava ovde
    else:
		# treci i finalni blok izraza pocinje ovde
		print('Nazalost niste pogodili.')
		print('Hint: Trazeni broj je manji od unesenog ;)')
		print('Pokusajte ponovo.')
		# treci i finalni blok izraza zavrsava ovde
else:
	print('Kraj while petlje.')


print('Kraj!')
```

**`Rezultat:`**
```
$ python kod-804-while-naredba.py 
Unesite cijeli broj: 43
Nazalost niste pogodili.
Hint: Trazeni broj je manji od unesenog ;)
Pokusajte ponovo.

Unesite cijeli broj: 31
Nazalost niste pogodili.
Hint: Trazeni broj je veci od unesenog ;)
Pokusajte ponovo.

Unesite cijeli broj: 32
Cestitamo, pogodili ste broj.
Pocastite se kafom ;)

Kraj while petlje
Kraj
```
<a name="moduli"/>

### Moduli

<a name="tipovi-podataka"/>

### Tipovi podataka
<a name="strukture-podataka"/>

### Strukture podataka (DRAFT)

Strukture podataka u Python-u predstavljaju upravo to, strukture kao nosioce podataka
zajedno. 

Postoje cetiri ugradjene (built-in) strukture u Python-u i to:
1. List (Liste)
1. Tuple (Tuple :)
1. Dictionary (Rijecnici)
1. Set (Setovi)

<a name="rjesavanje-problema"/>

### Rjesavanje problema


<a name="objektno-orjentisano-programiranje"/>

### Objektno orijentisano programiranje


<a name="izuzeci"/>

### Exceptions (Izuzeci?) (DRAFT)

Exception (Izuzeci) se pojavljuju kada se desi neka posebna situacija prilikom izvrsenja
programa. Recimo program pokusava da cita fajl na disku, ali fajl ne postoji ili je pod
drugim imenom? 
Slicno, sta ako u programu postoji neka sintaksna greska? Python ce nas upozoriti i 
dobicemo poruku o gresci (error).

### Greske

Uzmimo za primjer funkciju `print`. Sta ce se desiti ako umjesto `print` pozovemo `Print`?
Primijeticete da smo u ovom slucaju koristili prvo veliko slovo, sto nikako nije ispravno.
U ovom slucaju, Python ce nas upozoriti i dobicemo poruku o gresci.


<a name="greske"/>

### Greske

Uzmimo za primjer funkciju `print`. Sta ce se desiti ako umjesto `print` pozovemo `Print`?
Primijeticete da smo u ovom slucaju koristili prvo veliko slovo, sto nikako nije ispravno.
U ovom slucaju, Python ce nas upozoriti i dobicemo poruku o gresci.

<a name="kod-1502-greska-print.py"/>

**`kod-1502-greska-print.py`**
```python
Print("Da li je ovo bilo ispravno?")
```

**`Rezultat`**
```
$ python kod-1502-greska-print.py
Traceback (most recent call last):
  File "kod.py", line 1, in <module>
    Print("Da li je ovo bilo ispravno?")
NameError: name 'Print' is not defined
```

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

Naglasiti vaznost engleskog jezika, kao i to da neki nazivi jednostavno
ne mogu bit prevedeni

The Software Development Process

We have now gone through the various phases in the process of writing a software. These phases can be summarised as follows:

    What (Analysis)
    How (Design)
    Do It (Implementation)
    Test (Testing and Debugging)
    Use (Operation or Deployment)
    Maintain (Refinement)

Show Kanban and Scrum#### Pravila pisanja

* Prva i zadnja linija fajla mora biti prazna
* Za naslove koristimo tri tarabe "###"
