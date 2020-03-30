
#### klase i objekti
- ekstremno korisni , organizovan i mocniji
- kada radimo sa programiranjem susrecemo se sa razlicitim tipovima podataka
- takodje susrecemo se sa razlicitim strukturama podataka
- sta u slucaju kad ne mozemo predstaviti neku pojavu iz prirode sa vec postojecim tipovima 
  ili strukturama podataka
- u python-u mozemo krairati klase (definise vas licni tip podatka, ponasa se kao template, patern
  kako nesto treba da izgleda)
- objekat je podatak u memoriji, pravi podatak kreiran iz klase

student.py
# posto ne postoji student tip podaka, kreiracemo klasu student
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

# kreiranje student_prvi objetka
student_prvi = Student("Darko", "Programiranje", 8, False)
print(student_prvi)
print(student_prvi.ime)
print(student_prvi.ocjena)

student_drugi = Student("Dragan", "Ekonomija", 8.3, True) 
print(student_drugi.brucos) 
```

##### funkcije unutar klase (funkcije objekta)
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
