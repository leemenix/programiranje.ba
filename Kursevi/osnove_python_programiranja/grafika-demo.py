import PySimpleGUI as grafika

grafika.theme('DarkAmber')	
izgled = [  [grafika.Text('Program za unos teksta')],
            [grafika.Text('Unesite tekst'), grafika.InputText()],
            [grafika.Button('Dalje'), grafika.Button('Otkazi')] ]
#print(type(izgled))
# inicijalizacija
prozor = grafika.Window('Dragon Ball', izgled)
# 
while True:
	# event, values
    dogadjaj, vrijednost = prozor.read()
    if dogadjaj in (None, 'Otkazi'):	
        break
    print('Unijeli ste ', vrijednost[0])

prozor.close()