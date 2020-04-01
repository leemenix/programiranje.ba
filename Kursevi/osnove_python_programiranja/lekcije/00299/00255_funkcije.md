
<div style="page-break-after: always;"></div>

## Funkcije

Skup naredbi koje po pozivu izvrsavaju odredjene zadatke. Funkcije sluze takodje za bolju organizaciju koda.

Funkcije se definisu pomocu kljucne rijeci **def**, kad god se pojavi def na pocetku linije, python zna da korisnik zeli kreirati funkciju i stim u vezi se i ponasa.

Sintaksa funkcije:

```text
def naziv_funkcije(parametri): # parametri su opcioni, ali ako postoje moraju biti definisani/proslijedjeni
  blok naredbi # argumenti (poznat jos kao tijelo funkcije)

naziv_funkcije(argumenti) # poziv funkcije
```

Iz sintakse mozemo zakljuciti da je naziv_funkcije identifikator kojim pozivamo funkciju, dok parametri sluze
da bi se definisale vrijednosti koje se mogu proslijediti kao parametri naredbama unutar tijela funkcije.

**`Izvorni kod: kod-255_rad-sa-funkcijama.py`**

```python
def zdravo_svijete(): # funkcija bez parametara
  print("Zdravo Svijete.")

# moramo pozvati funkciju ako zelimo da je izvrsimo
zdravo_svijete()

def zdravo_svijete():
  print("Zdravo Svijete.")

print("Prije funkcije")
zdravo_svijete()
print("Nakon funkcije")

# prosledjivanje parametara funkciji

def zdravo_svijete(ime):
  print("Zdravo " + ime)

# moramo pozvati funkciju ako zelimo da je izvrsimo
zdravo_svijete("Goku")
zdravo_svijete("Krilin")

def zdravo_svijete(ime,godine):
  print("Zdravo " + ime + " vi imate " + str(godine))

# moramo pozvati funkciju ako zelimo da je izvrsimo
zdravo_svijete("Goku", "15")
zdravo_svijete("Krilin", "16")

# primjer funkcije sa korisnickim unosom
korisnik_ime = input("Unesite ime : ")
def pozdrav(ime):
    print ("Zdravo " + ime)

pozdrav(korisnik_ime)


```
