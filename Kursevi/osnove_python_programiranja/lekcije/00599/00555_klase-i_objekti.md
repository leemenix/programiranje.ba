
## klase i objekti
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
class Student:
  # inicijalizacija klase (inicijalna funkcija)  
  def __init__(self, ime, smjer, ocjena, brucos):
    self.ime = ime
    self.smjer = smjer
    self.ocjena = ocjena
    self.brucos = brucos


from Student import Student

# kreiranje student_prvi objetka
student_prvi = Student("Darko", "Programiranje", 8, False)
print(student_prvi)
print(student_prvi.ime)
print(student_prvi.ocjena)

student_drugi = Student("Dragan", "Ekonomija", 8.3, True) 
print(student_drugi.brucos) 

## funkcije unutar klase (funkcije objekta)
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

## naslijedjivanje
- u slucaju da imamo klasu, kada kreiramo novu klasu mozemo naslijediti staru klasu
- nova klasa ce imati sve osobine stare klase sa novim opcijama

Kuvar.py
class Kuvar:
    def priprema_mesa(self):
        print ("Priprema pileceg mesa.")

    def priprema_salate(self):
        print("Pirprema Cezar salata")

    def priprema_specijalnog_jela(self):
        print("Priprema rebarcadi")

KineskiKuvar.py
from Kuvar import Kuvar

class KineskiKuvar(Kuvar):
    def priprema_rize(self):
        print("Priprema rize na kineski nacin")

    def priprema_specijalnog_jela(self):
        print ("Pekinska patka")

from Kuvar import Kuvar
from KineskiKuvar import KineskiKuvar

novi_kuvar = Kuvar()

novi_kuvar.priprema_mesa()
novi_kuvar.priprema_specijalnog_jela()

novi_kineski_kuvar = KineskiKuvar()

novi_kineski_kuvar.priprema_rize()
novi_kineski_kuvar.priprema_mesa()
novi_kineski_kuvar.priprema_specijalnog_jela()

## kviz sa vise opcija



- devet_depresivaca.py - (Rambo Amadeus - Devet depresivaca)
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

    

