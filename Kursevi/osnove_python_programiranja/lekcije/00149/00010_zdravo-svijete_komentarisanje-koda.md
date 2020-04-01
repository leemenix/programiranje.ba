
<div style="page-break-after: always;"></div>

## Zdravo Svijete

**`Izvorni kod: kod-10_zdravo-svijete.py`**

```python      
print("Zdravo Svijete!")
```

Imamo dva nacina za pokretanje Python programa, ovo je preporuka kada koji koristiti:
- cmd, terminal - (ako nesto zelimo da provjerimo brzo i trenutno)
- direktno iz IDE-a (precice) - (kada pisemo vise linija koda)

Programiranje predstavlja davanje instrukcija kompjuteru (kroz programski jezik) i na osnovu ovih instrukcija
kompjuter donosi odluke. 

**`Izvorni kod: kod-11_crtanje-oblika.py`**

```python
print("*")
print("**")
print("***")
print("****")
print("*****")
print("******")
```

- u ovom slucaju python ide liniju po liniju i izvrsava kod
- sta se desava u slucaju da zamijenimo prvu i zadnju liniju?

## Komentarisanje koda

Komentare koristimo kada zelimo da zapisemo neki podsjetinik unutar koda, komentarisemo kod, objasnimo drugima
i sebi sta odredjena linija koda radi. Praksa i preporuka je da se koristi simbol taraba (hash tag) _#_. 
Komentari su po default-u ignorisani u Python-u, preciznije ignorisani od strane Python interpretera.  

**`Izvorni kod: kod-12_demonstracija-komentara.py`**
```python
'''
Viselinijski komentar
'''
"""
Viselinijski komentar
"""
print("Komentari su korisni")
# print("Ova linija koda nece biti ispisana")
```
