
# Uvod u Python programski jezik



**Autor:** _Milenko Letic_

https://programiranje.ba



### Sadrzaj
=======

  * [Uvod - par rijeci o programskom jeziku Python](#intro)
    * [Par cinjenica o Python-u](#python-cinjenice)
    * [Python 3 vs. Python 2](#python3-vs-python2)

  * [Instalacija](#instalacija)
    * [Python 3 instalacija](#python-instalacija)
    * [IDE - PyCharm instalacija](#pycharm-instalacija)
      * [PyCharm podesavanje parametara](#pycharm-podesavanje)
  
  * [Prvi koraci - prohodavanje](#prvi-koraci) 
  
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

<a name="instalacija"/>

### Instalacija i podesavanje Python-a i PyCharm-a

https://python.org/downloads

![GitHub stranica](slike/github_stranica.png)

Trenutna verzija Python-a, koju cemo ujedno obraditi prilikom ovog kursa je Python 3.

```TBD: par rijeci o Python 2```

<a name="python-instalacija"/>

#### Python 3 instalacija

##### Korak 1.

Prilikom pokretanja instalacije, na prvom koraku je potrebno cekirati obe opcije:
* Install launcher for all users (recommended)
* Add Python 3.x to PATH

![Python instalacija korak prvi](slike/python_instalacija_1.png)

##### Korak 2. 

Na drugom koraku je potrebno jos jednom cekirati opciju:
* for all users (requires elevation)

![Python instalacija korak drugi](slike/python_instalacija_2.png)

#### Korak 3.

![Python instalacija korak treci](slike/python_instalacija_3.png)

#### Korak 4. 
![Python instalacija korak cetvrti](slike/python_instalacija_4.png)

#### Korak 5. 
![Python instalacija korak peti](slike/python_instalacija_5.png)

#### Korak 6. 
![Python instalacija korak sesti](slike/python_instalacija_6.png)


<a name="pycharm-instalacija"/>

#### PyCharm instalacija

https://jetbrains.com/pycharm/download

##### Korak 1. 
![PyCharm instalacija korak prvi](slike/pycharm_instalacija_1.png)

##### Korak 2. 
![PyCharm instalacija korak drugi](slike/pycharm_instalacija_2.png)


##### Korak 3. 
![PyCharm instalacija korak treci](slike/pycharm_instalacija_3.png)

##### Korak 4. 
![PyCharm instalacija korak cetvrti](slike/pycharm_instalacija_4.png)

##### Korak 5. 
![PyCharm instalacija korak cetvrti](slike/pycharm_instalacija_5.png)

##### Korak 6. 
![PyCharm instalacija korak cetvrti](slike/pycharm_instalacija_6.png)


<a name="pycharm_podesavanje"/>

#### PyCharm podesavanje parametara

Nakon restarta pokrenemo PyCharm i konfigurisemo minimalna podesavanja

##### Korak 1.
![PyCharm podesavanje korak 1](slike/pycharm_podesavanje_1.png)

##### Korak 2.
![PyCharm podesavanje korak 2](slike/pycharm_podesavanje_2.png)

##### Korak 3.
![PyCharm podesavanje korak 3](slike/pycharm_podesavanje_3.png)

##### Korak 4.
![PyCharm podesavanje korak 4](slike/pycharm_podesavanje_4.png)

##### Korak 5.

Kliknite na Project interpreter i podesite Base interpreter 
[vrijednost moze varirati u zavisnosti od vaseg OS-a]

![PyCharm podesavanje korak 5](slike/pycharm_podesavanje_5.png)

##### Korak 6.
![PyCharm podesavanje korak 6](slike/pycharm_podesavanje_6.png)

##### Korak 7.
![PyCharm podesavanje korak 7](slike/pycharm_podesavanje_7.png)

##### Korak 8.
![PyCharm podesavanje korak 8](slike/pycharm_podesavanje_8.png)

##### Korak 9.
![PyCharm podesavanje korak 9](slike/pycharm_podesavanje_9.png)

##### Korak 10.
![PyCharm podesavanje korak 10](slike/pycharm_podesavanje_10.png)

##### Korak 11.
![PyCharm podesavanje korak 11](slike/pycharm_podesavanje_11.png)

##### Korak 12.
![PyCharm podesavanje korak 12](slike/pycharm_podesavanje_12.png)


* [Prvi koraci - prohodavanje](#prvi-koraci)   * [Osnove](#osnove)
    * [program-01 - zdravo_svijete.py](#zdravo-svijete)
<a name="zdravo_svijete.py"/>

### program-01 - zdravo_svijete.py

```python
print("Zdravo Svijete")
```

Output:
```
Zdravo Svijete
```
<a name="operatori-i-izrazi"/>

### Operatori i izrazi
<a name="kontrola-toka"/>

### Kontrola toka

<a name="funkcije"/>

### Funkcije


<a name="zdravo_svijete.py"/>

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
<a name="moduli"/>

### Moduli
  

<a name="tipovi-podataka"/>

### Tipovi podataka
<a name="varijable"/>

### Varijable
Kada radimo sa podacima, potrebno ih je organizovati, kontejneri kutije u koje stavlljamo pohranjujemo nase podatke predstavljaju varijable. Sta predstavljaju , zasto su korisne, koje sve vrste (tipove) podataka mozemo smjestiti u varijable.



<a name="varijable-01"/>

### program-02 - varijable-01.py

```python
print("Bila mama Kukunka, Kukunka")
print("Bio tata Taranta, Taranta")
print("imali su maloga Ju-Ju")

print("Jednom su se setali, setali")
print("kraj duboke rijeke Nil, rijeke Nil")
print("gdje je bio velik krokodil")
```

Output:
```
Bila mama Kukunka, Kukunka
Bio tata Taranta, Taranta
imali su maloga Ju-Ju
Jednom su se setali, setali
kraj duboke rijeke Nil, rijeke Nil
gdje je bio velik krokodil
```

<a varijable-02.py/>

### program-03 - varijable-02.py

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

Output:
```
Bila mama Kukunka, Kukunka
Bio tata Taranta, Taranta
imali su maloga Ju-Ju
Jednom su se setali, setali
kraj duboke rijeke Dunav, rijeke Dunav
gdje je bio velik krokodil
```

<a name="stringovi"/>

### Stringovi
  

<a name="matematicke-operacije"/>

### Matematicke operacije


<a name="strukture-podataka"/>

### Strukture podataka


<a name="rjesavanje-problema"/>

### Rjesavanje problema


<a name="objektno-orjentisano-programiranje"/>

### Objektno orijentisano programiranje


<a name="ulaz-izlaz"/>

### Ulaz/Izlaz


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




### Organizacija podataka

### List

List funkcije

Tuples

Dictionaries


Funkcije i uslovi
Return statement