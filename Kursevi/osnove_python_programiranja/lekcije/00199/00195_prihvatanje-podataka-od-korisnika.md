
## Ulaz/upis podataka, prihvatanje podataka od korisnika

```python
input() # hej ti, cekam da uneses neku informaciju podatak
input("Unesite vase ime: ")
korisnik_ime = input("Unesite vase ime: ")
print("Zdravo, " + korisnik_ime + " dobrodosli.")

korisnik_ime = input("Unesite vase ime: ")
korisnik_godine = input("Unesite vase godine: ")
print("Zdravo, " + korisnik_ime + ". Vi imate " + korisnik_godine + " godina.")

# vjezba ispisati preghodni program koristeci funkciju format
```

osnovni_kalkulator.py

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


interaktivni_karakter_program.py
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
