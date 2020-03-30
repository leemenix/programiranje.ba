
## Rad sa stringovima
Stringovi predstavljaju niz karaktera (velika/mala slova, brojevi, znakovi interpunkcije, specijalni 
znakovi, ...), koji sluzi za skladistenje i rad sa tekstualni podacima. 

### Jednostavan primjer kreiranja stringa
rad_sa_stringovima.py
```python
print("programiranje.ba besplatni online kursevi")

# escape karakter \
print("programiranje.ba \n besplatni online kursevi")

sajt_naziv = "programiranje.ba"
sajt_slogan = " besplatni online kursevi"

# jos neki primjeri kreiranja string-a (kao sto smo imali slucaj sa viselinijskim komentarom)
sajt_naziv = 'https://programiranje.ba'
sajt_slogan = """besplatni online kursevi
                   za sve """
```

### Funkcije nad stringovima
rad_sa_stringovima.py
```python
print("programiranje.ba besplatni online kursevi")

# escape karakter \
print("programiranje.ba \n besplatni online kursevi")

sajt_naziv = "programiranje.ba"
sajt_slogan = " besplatni online kursevi"
print(sajt_naziv)
print(sajt_slogan)
print(sajt_naziv + sajt_slogan)
print(sajt_naziv.upper() + sajt_slogan.upper())
print(sajt_naziv.isupper())
print(len(sajt_naziv))

# index stringa pocinje na poziciji 0
print(sajt_naziv[4])
print(sajt_naziv[-4])
print(sajt_naziv[1:4])
# index funkcija i proslijedjivanje parametara
print(sajt_naziv.index('g'))
print(sajt_naziv.index('mira'))
#print(sajt_naziv.index('h'))
# find funkcija i proslijedjivanje parametara
print(sajt_naziv.find('g'))
print(sajt_naziv.find('mira'))
# razlika izmedju find i index, u slucaju da ne postoji trazeni patern
# index() vraca gresku, dok find vraca -1

# replace funkija
print(sajt_slogan.replace("kursevi","tutoriali").upper())

print("{1}, {0}".format(sajt_naziv, sajt_slogan))
print(f"{sajt_naziv} {sajt_naziv}")

# jos neki primjeri funkcija nad stringovima
### char i ord kasnije potrebni za cezarovu sifru 
```
