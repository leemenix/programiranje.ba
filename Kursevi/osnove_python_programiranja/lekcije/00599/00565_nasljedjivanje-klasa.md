
### Naslijedjivanje - podklase

U slucaju da planiramo kreirati novu klasu, a vec unaprijed znamo da imamo ili
da vec postoji klasa koja sadrzi vecinu metoda koje trebamo koristiti, medjutim
mi trebamo definisati jos par novih objekata ili novih metoda, u tom slucaju 
koristimo naslijedjivanje ili podklase, tako sto kreiramo novu klasu koja 
naslijedjuje staru klasu.

Nova klasa ce imati sve osobine stare klase sa novim opcijama. 

**`Izvorni kod: kod-565_kuvar.py`**

```python
class Kuvar:
    def priprema_mesa(self):
        print ("Priprema pileceg mesa.")

    def priprema_salate(self):
        print("Pirprema Cezar salata")

    def priprema_specijalnog_jela(self):
        print("Priprema rebarcadi")
```
**`Izvorni kod: kod-566_kineski_kuvar.py`**

```python
from kuvar import Kuvar

class KineskiKuvar(Kuvar):
    def priprema_rize(self):
        print("Priprema rize na kineski nacin")

    def priprema_specijalnog_jela(self):
        print ("Pekinska patka")
```

Dakle, sve metode koje su definisane u klasi **Kuvar** , koja se jos naziva nadklasa, mogu se koristiti u novoj klasi **KineskiKuvar** , koja se jos naziva podklasa.
Mozemo primijetiti redefinisanje metode **priprema_specijalnog_jela** u novoj
klasi **KineskiKuvar**. U slucaju redefinisanja metode, prilikom pozivanja 
metode **priprema_specijalnog_jela**, koristi se nova redefinisana metoda. 

**`Izvorni kod: kod-567_main.py`**

```python
from kuvar import Kuvar
from kineski_kuvar import KineskiKuvar

novi_kuvar = Kuvar()

novi_kuvar.priprema_mesa()
novi_kuvar.priprema_specijalnog_jela()

novi_kineski_kuvar = KineskiKuvar()

novi_kineski_kuvar.priprema_rize()
novi_kineski_kuvar.priprema_mesa()
novi_kineski_kuvar.priprema_specijalnog_jela()
```
