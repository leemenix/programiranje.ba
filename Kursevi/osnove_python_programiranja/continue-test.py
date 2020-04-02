karakter_opis = {}

brojac = 0
limit = 10

while brojac <= limit:
	karakter_ime = input("unesi ime ")
	karakter_godine = input("unesi godine ")

	if int(karakter_godine) <= 0:
		print("godine ne mogu biti manje od 0 ")
		break
	elif int(karakter_godine) >= 100:
		print("trebali biste dobiti nobelovu nagradu za godine")
	else:
		karakter_opis[karakter_ime] = (karakter_godine)
		brojac += 1
print(karakter_opis)
