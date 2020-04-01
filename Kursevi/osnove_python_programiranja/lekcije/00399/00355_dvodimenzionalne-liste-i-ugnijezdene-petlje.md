
<div style="page-break-after: always;"></div>

## Dvodimenzionalne liste i ugnijezdene petlje (nested)

**`Izvorni kod: kod-355_rad-sa-dvodimenzionalnim-listama.py`**

```python
mreza = [
    [1, 2, 3],
    [4, 5, 6],
    [7 ,8 ,9],
    [0]
]

print(mreza[0][2])
print(mreza[2][1])
print(mreza[3][0])

# nested for loop

# mreza = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7 ,8 ,9],
#     [0]
# ]

for row in mreza:
  for col in row:
    print(col)

for col in mreza:
    for row in col:
        print(row)
    
# cezarova sifra u python
def enkripcija(tekst, pomak):
  rezultat = ""

  for broj in range(len(tekst)):
    slovo = tekst[broj]
    
  if(slovo.isupper()):
    rezultat += chr((ord(slovo) + pomak - 65) % 26 + 65)
  else: 
    rezultat += chr((ord(slovo) + pomak - 97) % 26 + 65)
  return rezultat

tekst = input("Unesite tekst: ")
pomak = 2

print("Unijeli ste: " + tekst)
print("Pomak: " + str(pomak))
print("Sifrovan tekst: " + enkripcija(tekst, pomak))
```
