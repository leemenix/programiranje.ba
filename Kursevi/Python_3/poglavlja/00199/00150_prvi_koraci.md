
<a name="prvi-koraci"/>

### Prvi koraci (DRAFT)

Postoje dva nacina koristenja Python-a kako biste pokrenuli vas kod (TBD:
program ili kod).
1. koristenjem interaktivnog interpreter komandnog prompta
1. koristenjem izvornog koda (source code)

#### Koristenjem interpreter prompt-a

Otvorite terminal na vasem operativnom sistemu (TBD: ovo je vec objasnjeno u
sekciji instalacija)
i pokrenite Python tako sto cete ukucati komandu **python3** i pritisnuti
**[Enter]**. Trebalo bi da dobijete Python interpreter prompt, koji izgleda
ovako

```python
Python 3.7.2 (default, Feb 23 2020, 18:31:07)
[GCC 5.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Odlicno, sada vec mozete da napisete vas prvi program u Python-u.
Nakon znaka **[>>>]** ukucajte:

```python
Python 3.7.2 (default, Feb 23 2020, 18:31:07)
[GCC 5.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Zdravo Svijete!")
```

i pritisnite **[Enter]**. Trebalo bi dobijete ispisanu recenicu
**_Zdravo Svijete!_** u Python-u
interpreter prompt-u, nakon cega mozete nastaviti da koristite Python interpreter prompt.
```python
Python 3.7.2 (default, Feb 23 2020, 18:31:07)
[GCC 5.5.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Zdravo Svijete!")
Zdravo Svijete!
>>>
```
##### Izlazak, napustanje Python interpreter prompt-a

Nakon sto ste testirali vas prvi Python kod, mozemo napustiti intrepreter sa nekom od sledece tri
komande:

```python
exit()
```
```python
quit()
```
```python
Kombinacija tastera [Crtl] i tastera [D]
```
#### Koristenjem izvornog koda

Kreiramo novi fajl **kod-201-zdravo-svijete.py** i upisemo sledeci sadrzaj
```python
print("Zdravo Svijete!")
```

Sacuvamo fajl **kod-201-zdravo-svijete.py** na zeljenu lokaciju i isti zatvorimo. Sada je
potrebno otvoriti terminal na vasem operativnom sistemu, pozicionirati se u direktorij gdje
ste sacuvali kod i izvrsiti komandu
```shell script
python kod-201-zdravo-svijete.py
```
Trebalo bi da dobijete povratnu poruku na ekranu
```shell script
Zdravo Svijete!
```

Odlicno, sada kada poznajemo na koje nacine mozemo pokrenuti Python program, vrijeme je da
prijedjemo na zanimljivije stvari koje mozemo uraditi sa Python-om. Slozicete se da je
ispisivanje rijeci "Zdravo Svijete!" malo dosadno.
