
niz_brojeva = [4,2,1,5,3,10,233,13222,100,222,3333,4444,555,666,777] 

# inicijalno stanje varijable, koja nam govori da li je bilo 
# zamjene brojeva prilikom iteracije kroz niz
zamjena_izvrsena = True 

zadnji_element_niza = (len(niz_brojeva) - 1)

while zamjena_izvrsena:
	# predpostavimo da je niz sortiran
	zamjena_izvrsena = False

	# isijecamo poslednji element niza, jer unutar petlje provjeravamo naredni preko indeks + 1
	for indeks,broj in enumerate(niz_brojeva[0:zadnji_element_niza]):
		if niz_brojeva[indeks] > niz_brojeva[indeks+1]:
			# mijenjamo mjesta elemenata niza
			niz_brojeva[indeks],niz_brojeva[indeks+1]=niz_brojeva[indeks+1],niz_brojeva[indeks]
			zamjena_izvrsena = True
else:
	print(niz_brojeva)


