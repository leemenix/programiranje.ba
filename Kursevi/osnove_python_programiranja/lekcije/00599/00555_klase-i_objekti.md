
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

### funkcije unutar klase (funkcije objekta)

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

**`Izvorni kod: kod-558-main.py`**

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

### metode

U prethodnom primjeru smo vidjeli jednu od metoda **dobar()**, ali ajde da 
pogledamo malo detaljnije o cemu se radi.

Recimo da zelimo funkciju u nasoj klasi **Student** koja nam ispisuje 
kompletan sadrzaj instanciranog objekta **Student**, ali i omiljenog pisca tog
studenta. Za ovo su nam potrebne dvije metode unutar klase **Studnet** koje 
cemo nazvati **student_opis** i **student_pisac**.

**` Izvorni kod: kod-559-metode.py`**

```python

```

