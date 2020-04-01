
<div style="page-break-after: always;"></div>

## Ulaz/upis podataka, prihvatanje podataka od korisnika ili interakcija sa programom

Slozicete se da je programiranje dosadno, ako nemamo interakciju, nekakav vid 
komunikacije sa nasim programom. Kako bi omogucili interakciju sa programom, 
Python nam na raspolaganje nudi funkciju **input()**. 

**`Izvorni kod: kod-190_interakcija-sa-korisnikom.py`**
```python

input() 
# hej ti, cekam da uneses neku informaciju podatak, naravno korisnik nije siguran sta se desava

input("Unesite vase ime: ")
# aha ovo sad vec ima smisla

# <naziv varijable> <tip podatka>
korisnik_ime = input("Unesite vase ime: ")
# naravno, posto nam je korisnicki unos vazan mi zelimo sacuvati isti taj unos u neku varijablu
# kako bi smo kasnije mogli koristiti
print("Zdravo, " + korisnik_ime + " dobrodosli.")

korisnik_ime = input("Unesite vase ime: ")
korisnik_godine = input("Unesite vase godine: ")
print("Zdravo, " + korisnik_ime + ". Vi imate " + korisnik_godine + " godina.")

# vjezba ispisati preghodni program koristeci funkciju format
```

**`Izvorni kod: kod-191_interaktivni_karakter_program.py`**
```python
print("U dalekoj proslosti zivio je djecak po imenu Goku.")
print("Goku je imao 15 godina.")
print("Volio je upoznavati nove karaktere ")
print("i imao je najboljeg druga po imenu Krilin!")

karakter_ime = input("Unesite ime karaktera: ")
karakter_godine = input("Unesite godine karaktera: ")
karakter_prijatelj = input("Unesite ime najboljeg prijatelja: ")

print(f"U dalekoj proslosti zivio je djecak po imenu {karakter_ime}.")
print(f"{karakter_ime} je imao {karakter_godine} godina.")
print(f"Volio je upoznavati nove karaktere ")
print(f"i imao je najboljeg druga po imenu {karakter_prijatelj}!")
```

**`Izvorni kod: kod-192_osnovni_kalkulator.py`**

```python
broj_1 = input("Unesite prvi broj: ")
broj_2 = input("Unesite drugi broj: ")
rezultat = broj1 + broj2

print(rezultat)

broj_1 = input("Unesite prvi broj: ")
broj_2 = input("Unesite drugi broj: ")
rezultat = float(broj_1) + float(broj_2)

print(rezultat)
```
