def zbir(*brojevi_1,broj_2):
  broj = 0
  for broj_1 in brojevi_1:
    broj += broj_1
    print(broj_1)
  broj += broj_2

  return broj
  
print(zbir(1,2,3,30,3,broj_2=2222))