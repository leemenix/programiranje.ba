
<a name="stringovi"/>

#### Stringovi

_Stringovi_ predstavljaju niz karaktera. Jos jednostavnije vise rijeci predstavlja string.
Kako su stringovi sveprisutni kroz cijeli kurs Python programiranje, bitno je da dobro 
razumijete ovo poglavlje.

##### Stringovi izmedju apostrofa

Mozemo koristiti apostrofe _' '_ da bismo formirali string.

**`Primjer`**
```python
'Ovo je string.'
```

##### Stringovi izmedju navodnika 

Isto tako mozemo koristiti navodnike _" "_ da bismo formirali string.

**`Primjer`**
```python
"Ovo je string."
```

Sigurno se pitate, pa u cemu je razlika izmedju apostrofa i navodnika? Hajde da
jednostavno kazemo da nema razlike, mozete koristiti i jednu i drugu opciju, ali
prakticna primjena je u slucaju kada trebate ispisati jedan od ova dva znaka 
unutar stringa. 

**`Primjer`**
```python
"Ovo je string. Koji sadrzi rijec 'Nova Godina' unutar apostrofa"
```

Uvijek morate voditi racuna da imate otvorene i zatvorene znakove apostrofa ili navodnika
prilikom pisanja koda. 

##### Stringovi izmedju trostrukih apostrofa ili navodnika

U slucaju da zelite viselinijski string tada je potrebno koristiti trostruke apostrofe
_''' '''_ ili navodnike _""" """_. U ovom slucaju mozete koristiti proizvoljan broj 
apostrofa ili navodnika unutar stringa.

**`Primjer`**
```python
'''
Ovo je multilinijski string. 
Koji sadrzi rijec 'Nova Godina' unutar apostrofa
ali i rijec "Stara Godina" unutar navodnika
'''
```

_Stringovi_ su nepromjenjivi, sto znaci jednom kad ih kreirate, vise ih ne mozete promijeniti. Iako ovo zvuci kao losa ideja, zaista nije. Kasnije cemo vidjeti kako 
ovo ne predstavlja nikakvo ogranicenje prilikom programiranja. 

##### Metod 'format'

Ponekad zelimo kreirati string iz razlicitih izvora. Ovde nam u pomoc uskace metod 
_format_. 
