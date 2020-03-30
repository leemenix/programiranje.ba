
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
