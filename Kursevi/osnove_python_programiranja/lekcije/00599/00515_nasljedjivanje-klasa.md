#### naslijedjivanje
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
