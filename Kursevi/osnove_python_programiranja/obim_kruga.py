def obim_kruga(poluprecnik, pi=3.14):
	obim = 2 * (poluprecnik * pi)
	return obim

def pozdrav_svijete(rijec="Pozdrav Svijete \n", broj=2):
	print((rijec) * broj)

print(obim_kruga(2))

print(pozdrav_svijete(rijec="Zdravo \n", broj=10))