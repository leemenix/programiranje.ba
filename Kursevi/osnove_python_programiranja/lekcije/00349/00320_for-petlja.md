
### for petlja
- specijalni tip petlje u python-u
```python
for slovo in "programiranje.ba":
  print(slovo)

for karakter in karakteri:
  print(karakter)

karakteri = ["Goku", "Kirlin", "Yamcha"]
for indeks in range(len(karakteri)):
  print (karakteri[indeks])

for broj in range(20):
  print(broj)

for broj in range(14, 20):
  print (broj)

for indeks in range(len(karakteri)):
  print (karakter[indeks])

for broj in range(5):
    if broj == 0:
        print("prvi pokusaj")
    else:
        print("ostali")

for i in range(10):
    print (i)
    i+=1

### eksponencijaln funkcija - kada ne znamo koliko je eksponent
print(2**3)

def eksponent_broja(baza, eksponent):
  rezultat = 1
  for index in range(exponent):
    rezultat = rezultat * baza
  return rezultat

print(exponent_broja(2,4))
```