
## dvodimenzionalne liste i ugnijezdene petlje (nested)

```python
resetka = [
    [1, 2, 3],
    [4, 5, 6],
    [7 ,8 ,9],
    [0]
]

print(resetka[0][2])
print(resetka[2][1])
print(resetka[3][0])

# nested for loop

# resetka = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7 ,8 ,9],
#     [0]
# ]

for row in resetka:
  for col in row:
    print(col)

for col in resetka:
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
