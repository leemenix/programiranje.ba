
<a name="kod-802-if-elif-else-iskaz.py"/>

**`Primjer: kod-802-if-elif-else-iskaz.py`**
```python
broj = 32
pokusaj = int(input('Unesite cijeli broj: '))

if pokusaj == broj:
	# prvi blok izraza pocinje ovde
	print('Cestitamo, pogodili ste broj.')
	print('Pocastite se kafom ;)')
	# prvi blok izraza zavrsava ovde

elif pokusaj < broj:
	# drugi blok izraza pocinje ovde
	print('Nazalost niste pogodili.')
	print('Hint: Trazeni broj je veci od unesenog ;)')
	print('Pokusajte ponovo.')
	# drugi blok izraza zavrsava ovde

else:
	# treci i finalni blok izraza pocinje ovde
	print('Nazalost niste pogodili.')
	print('Hint: Trazeni broj je manji od unesenog ;)')
	print('Pokusajte ponovo.')
	# treci i finalni blok izraza zavrsava ovde

print('Kraj!')
# Zadnji izraz ce uvijek biti izvrsen
# naravno nakon sto je ispunjen jedan od gore navedenih uslova
```

**`Rezultat:`**
```
$ python kod-802-if-elif-else-iskaz.py
Unesite cijeli broj: 3
Nazalost niste pogodili.
Hint: Trazeni broj je veci od unesenog ;)
Pokusajte ponovo.
Kraj!

$ python kod-802-if-elif-else-iskaz.py 
Unesite cijeli broj: 44
Nazalost niste pogodili.
Hint: Trazeni broj je manji od unesenog ;)
Pokusajte ponovo.
Kraj!

$ python kod-802-if-elif-else-iskaz.py
Unesite cijeli broj: 32
Cestitamo, pogodili ste broj.
Pocastite se kafom ;)
Kraj!
```
