
#### Rijecnici - Dictionaries - {}

Rijecnici su tipovi podataka, opet slicni listama, ali za razliku od listi indeksiranje se obavlja kljucevima.

Za lakse razumijevanje ih mozemo uporediti sa klasicnim rijecnikom za prevodjenje rijeci sa jednog jezika na 
drugi, gdje imamo strukturu strana rijec na lijevoj strani i detaljno objasnjenje rijeci na desnoj strani.
Ako navedenu analogiju primijenimo rijecnicima, kao tipovima podataka u Python-u, onda rijec predstavlja kljuc
(key), dok detaljno objasnjenj predstavlja vrijednost (value). 

Elementi rijecnika su smjesteni u viticaste zagrade _{}_ a parovi elemenata su razdvojeni zarezom _,_. 
```text{kljuc:vrijednost} ({key:value})```

Bitno je napomenti da kljuc (key), mora biti jedinstven, ne mozemo imati dva ista kljuca. 
```text
{"kljuc_1:vrijednost_1", "kljuc_2:vrijednost_2", "kljuc_3:vrijednost_1"} - ispravno
{"kljuc_1:vrijednost_1", "kljuc_1:vrijednost_2", "kljuc_3:vrijednost_1"} - nije ispravno 
```

**`Izvorni kod: kod-230_rad-sa-rijecnicima`**
```python
karakteri={} # prazan rijecnik
print(karakteri)

karakteri_osobine={"Goku":"Sayan", "Picolo":"Namek", "Krilin":"Zemlja"}
print(karakteri_planete)
print(type(karakteri_planete))

karakteri_planete["Bulma"]="Zemlja"
print(karakteri_planete)
karakteri_planete["Goku"]="Namek" # prepisace trenutnu vrijednost ako postoji

del(karakteri_planete["Goku"]) # brisanje elementa

print(len(karakteri_planete)) # primijetimo da se broje parovi

print(karakteri_planete.keys()) # metoda keys() nad rijecnicima, ispisuje sve kljuceve (keys), nema argumente
print(karakteri_planete.values()) # metoda values() ispisuje vrijdnosti elementa, nema argumente
print(karakteri_planete.items()) # metoda items() ispisuje kljuc: vrijdnost elementa, nema argumente
```

**`Izvorni kod: kod-231_konverzija_mjeseci.py`**
```python
# recimo da zelimo konvertovati kratke nazive mjeseca u standardne
# Jan -> Januar
# Mar -> Mart

konverzijaMjeseci = {
    "Jan": "Januar",
    "Feb": "Februar",
    "Mar": "Mart",
    "Apr": "April",
    "Maj": "Maj",
    "Jun": "Juni",
    "Jul": "Juli",
    "Avg": "Avgust",
    "Sep": "Septermbar",
    "Okt": "Oktobar",
    "Nov": "Novembar",
    "Dec": "Decembar"
}

print(konverzijaMjeseci["Jan"])
print(konverzijaMjeseci["Feb"])
print(konverzijaMjeseci["Mar"])

print(konverzijaMjeseci.get("Jan")) 
print(konverzijaMjeseci.get("Dec"))
print(konverzijaMjeseci.get("Dese","Nije validan kljuc")) # ako koristimo get necemo dobit gresku vec empty
```
