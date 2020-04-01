import random
niz_brojeva=[]
for i in range (10000):
	#print (random.randint(1,100))
    niz_brojeva.append(random.randint(1,10000))

print (niz_brojeva)

# niz_brojeva = [4,2,1,5,3] 

zamjena_izvrsena = True

zadnji_element_niza = (len(niz_brojeva) - 1)

while zamjena_izvrsena:
	zamjena_izvrsena = False

	for indeks,broj in enumerate(niz_brojeva[0:zadnji_element_niza]):
		#print(str(indeks) + " -> " + str(broj))

		if niz_brojeva[indeks] > niz_brojeva[indeks+1]:
			niz_brojeva[indeks],niz_brojeva[indeks+1]=niz_brojeva[indeks+1],niz_brojeva[indeks]
			zamjena_izvrsena = True

else:
	print(niz_brojeva)
