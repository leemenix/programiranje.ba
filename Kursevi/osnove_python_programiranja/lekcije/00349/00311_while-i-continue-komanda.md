### Naredba nastavljanja (**continue**)

U slucaju da nasilno zelimo prekinuti **dio petlje** ili blaze receno 
preskociti izvrsavanje tog bloka ali nastaviti sa izvrsavanjem sledeceg bloka
unutar iste petlje kositicemo naredbu nastavljanja **continue**. 

**`Izvorni kod: kod-312_demonstracija-naredbe-break.py`**

```python
karakter_opis = {}

brojac=0
limit=10

while brojac <= limit:
	karakter_ime = input("Unesi ime karaktera: ")
	karakter_godine = input("Unesi godine karaktera :")

	if int(karakter_godine) <= 0:
		print("Godine ne mogu biti manje od 1!")
		break
    elif int(karakter_godine) => 100:
    	print("Trebali biste dobiti Nobelovu nagradu za godine")
    	continue
	else:
		karakter_opis[(karakter_ime)] = (karakter_godine)
		brojac+=1 

print(karakter_opis)
```