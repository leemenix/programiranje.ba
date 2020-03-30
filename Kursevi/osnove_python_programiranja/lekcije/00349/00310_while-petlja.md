
## while petlja 
- struktura u python koja nam omogucava da prolazimo kroz isti kod vise puta, onoliko puta
koliko smo to zadali inicijalnim uslovom
- kroz svaku od iteracija kroz kod while ce da izvrsi sve sto je unutar while petlje

while_brojac.py
```python
i = 1
while i <= 10:
  print("Vrijednost i je : " + i)
  #i = i + 1
  i += 1

print("Kraj brojaca")
```

igra_pogadjanja.py - primjenimo sve do sad nauceno
```python
tajna_rijec = "python"

pokusaj = ""

while guess != tajna_rijec:
  pokusaj = input("Pokusajte pogoditi tajnu rijec: ")

print("Cestitamo, pogodili ste")

# limitiraj broj pogresnih pokusaja
tajna_rijec = "python"
pokusaj = ""
pokusaj_broj = 0
pokusaj_limit = 4
kraj_igre=False

while pokusaj != tajna_rijec and not(kraj_igre):
if pokusaj_broj < pokusaj_limit:
    pokusaj = input("Pokusajte pogoditi tajnu rijec: ")
    pokusaj_broj += 1
else:
    kraj_igre = True

if kraj_igre:
    print("Iskoristili ste sve pokusaje. Kraj igre")
else:
    print("Cestitamo, pogodili ste")
```
