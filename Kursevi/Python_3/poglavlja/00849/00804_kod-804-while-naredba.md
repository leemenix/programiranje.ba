
<a name="kod-804-while-naredba.py"/>

**`Primjer: kod-804-while-naredba.py`**
```python
broj = 32
petlja = True

while petlja:
	
	pokusaj = int(input('Unesite cijeli broj: '))

	if pokusaj == broj:
		# prvi blok izraza pocinje ovde
		print('Cestitamo, pogodili ste broj.')
		print('Pocastite se kafom ;)')
		# u slucaju da je broj pogodjen postavi vrijednost
 		# varijable petlja na False  
		petlja = False 
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
else:
	print('Kraj while petlje.')


print('Kraj!')
```

**`Rezultat:`**
```
$ python kod-804-while-naredba.py 
Unesite cijeli broj: 43
Nazalost niste pogodili.
Hint: Trazeni broj je manji od unesenog ;)
Pokusajte ponovo.

Unesite cijeli broj: 31
Nazalost niste pogodili.
Hint: Trazeni broj je veci od unesenog ;)
Pokusajte ponovo.

Unesite cijeli broj: 32
Cestitamo, pogodili ste broj.
Pocastite se kafom ;)

Kraj while petlje
Kraj
```