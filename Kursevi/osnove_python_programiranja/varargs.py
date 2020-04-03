def zbir(*brojevi_1,**brojevi_2):
	broj = 0
	for broj_1 in brojevi_1:
		broj += broj_1
		print(broj_1)
	for broj_2 in brojevi_2:
		broj += broj_2
		print(broj_2)

	return broj
	
print(zbir(1,2,3,30,3))