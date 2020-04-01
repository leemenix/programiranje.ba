
<div style="page-break-after: always;"></div>

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
