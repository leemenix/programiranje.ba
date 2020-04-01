
<div style="page-break-after: always;"></div>

#### Rijecnici - Dictionaries - { }

Rijecnici su tipovi podataka, opet slicni listama, ali za razliku od listi 
indeksiranje se obavlja kljucevima.

Za lakse razumijevanje ih mozemo uporediti sa klasicnim rijecnikom za 
prevodjenje rijeci sa jednog jezika na drugi, gdje imamo strukturu strana 
rijec na lijevoj strani i detaljno objasnjenje rijeci na desnoj strani.
Ako navedenu analogiju primijenimo rijecnicima, kao tipovima podataka u 
Python-u, onda rijec predstavlja kljuc (key), dok detaljno objasnjenje 
predstavlja vrijednost (value). 

Elementi rijecnika su smjesteni u viticaste zagrade **{ }** a parovi elemenata 
su razdvojeni zarezom **,**. 

```text
{kljuc:vrijednost} ({key:value})
```

Bitno je napomenti da kljuc (key), mora biti jedinstven, sto znaci da ne 
mozemo imati dva ista kljuca. 

```text
{"kljuc_1:vrijednost_1", "kljuc_2:vrijednost_2", "kljuc_3:vrijednost_1"} - ispravno
{"kljuc_1:vrijednost_1", "kljuc_1:vrijednost_2", "kljuc_3:vrijednost_1"} - nije ispravno 
```

**`Izvorni kod: kod-230_rad-sa-rijecnicima`**
```python
karakteri={} # prazan rijecnik
print(karakteri)

karakteri_osobine={"Goku":"Vegeta", "Picolo":"Namek", "Krilin":"Zemlja"}
print(karakteri_planete)
print(type(karakteri_planete))

karakteri_planete["Bulma"]="Zemlja"
print(karakteri_planete)
karakteri_planete["Goku"]="Namek" # prepisace trenutnu vrijednost ako postoji

del(karakteri_planete["Goku"]) # brisanje elementa

print(len(karakteri_planete)) # primijetimo da se broje parovi

print(karakteri_planete.keys()) # metoda keys() nad rijecnicima, ispisuje sve kljuceve (keys), nema argumente
print(karakteri_planete.values()) # metoda values() ispisuje vrijednosti elementa, nema argumente
print(karakteri_planete.items()) # metoda items() ispisuje kljuc: vrijednost elementa, nema argumente

# metode get i setdefault
karakteri_planete={'Goku':'Vegeta', 'Krilin':'Zemlja', 'Bulma':''}
print(karakteri_planete.get('Goku','Karakter ne postoji u bazi'))
print(karakteri_planete.get('Pikolo','Karakter ne postoji u bazi')) # metoda get() nad rijecnikom vrsi pretragu po zadatom kljucu, u slucaju da kljuc ne postoji vraca default-nu vrijednost, vrijednost koja je proslijedjena kao drugi parametar

print(karakteri_planete.setdefault('Pikolo','Karakter nema definisanu planetu')) # kljuc ce biti kreiran u slucaju da ne postoji, a vrijednost ce biti podesena na vrijdnost drugog proslijednjenog parametra
print(karakteri_planete.setdefault('Bulma','Zemlja')) # obzirom da kljuc postoji, nece doci do promjena

# metode pop i update
karakteri_planete={'Goku':'Vegeta', 'Krilin':'Zemlja', 'Bulma':'Zemlja'}
obrisan_karakter=(karakteri_planete.pop('Goku')) # pop() metoda prilikom brisanja key:value, zadrzava vrijednost (value)
print (karakteri_planete)
print (obrisan_karakter)

# spajanje rijecnika mozemo izvesti upotrebom metode update()
karakteri_1_planete={'Goku':'Vegeta', 'Krilin':'Zemlja', 'Bulma':'Zemlja'}
karakteri_2_planete={'Chi-Chi':'Zemlja', 'Vegeta':'Vegeta', 'Bulma':'Namek'}
karakteri_1_planete.update(karakteri_2_planete) # update() metod nad rijecnicima prosiruje prvi rijecnik vrijednostima iz drugog, u slucaju da imamo dva ista kljuca, kljuc iz prvog rijecnika bice zamijenjena kljucem iz drugog rijecnika
karakteri_1_planete={'Goku':'Vegeta', 'Krilin':'Zemlja', 'Bulma':'Zemlja'}
karakteri_2_planete={'Chi-Chi':'Zemlja', 'Vegeta':'Vegeta', 'Bulma':'Namek'}
karakteri_2_planete.update(karakteri_1_planete)
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
