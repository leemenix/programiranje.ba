from random import randint
mreza=[]

for i in range(0,7):
    mreza.append(["#"] * 7)
def stampaj_mrezu (board):
    for red in mreza:
        print (" ".join(red))

print ('Igra Potapanje brodova moze da pocne!')
stampaj_mrezu(mreza)

#Slučajnim odabirom u mrežu ubacujemo oba broda
def nasumicni_red(mreza):
    return randint(0, len(mreza)-1)

def nasumicna_kolona(mreza):
    return randint(0, len(mreza[0])-1)

#brod 1
red_1 = nasumicni_red(mreza)
kol_1 = nasumicna_kolona(mreza)
#brod 2
red_2 = nasumicni_red(mreza)
kol_2 = nasumicna_kolona(mreza)
#Da se brodovi ne bi preklapali, potrebno je da nemaju zajednička polja
#To se obezbeđuje funkcijom razliciti()
def razliciti(r,c):
    while r == red_1 and c == kol_1:
        r = nasumicni_red(mreza)
        c = nasumicna_kolona(mreza)
        red_2 = r
        kol_2 = c
razliciti(red_2,kol_2)
#Kada izaberete jedno polje, preostala dva mogu biti horizontalno(levo ili desno) ili vertikalno(gore ili dole)
#Zato se definišu sledeći pravci
def nasumicni_pravac():
    n = randint(1,4)
    if n == 1:
        return "gore"
    elif n == 2:
        return "desno"
    elif n == 3:
        return "dole"
    elif n == 4:
        return "levo"
#Nasumično se odredi pravac, i na osnovu njega sledeća dva polja
while True:
    d = nasumicni_pravac() 
    if d == "gore":
        if red_1 >= 2:
            
            red_1_2 = red_1 - 1
            kol_1_2 = kol_1
            red_1_3 = red_1 - 2
            kol_1_3 = kol_1
            break
    if d == "desno":
        if kol_1 <= len(mreza[0])-3:
            
            red_1_2 = red_1
            kol_1_2 = kol_1 + 1
            red_1_3 = red_1
            kol_1_3 = kol_1 + 2
            break
    if d == "dole":
        if red_1 <= len(mreza)-3:
            
            red_1_2 = red_1 + 1
            kol_1_2 = kol_1
            red_1_3 = red_1 + 2
            kol_1_3 = kol_1
            break
    if d == "levo":
        if kol_1 >= 2:
            
            red_1_2 = red_1
            kol_1_2 = kol_1 - 1
            red_1_3 = red_1
            kol_1_3 = kol_1 - 2
            break
brod_1 = [(red_1 ,kol_1 ),(red_1_2 ,kol_1_2 ),(red_1_3 ,kol_1_3 )]



#drugi brod:
while True:
#Nasumično se odredi pravac, i na osnovu njega sledeća dva polja
#Uslov je da se ne preklapaju sa poljima prvog broda
    d = nasumicni_pravac() 
    if d == "gore":
        if red_2 >= 2:
            if (red_2 - 1,kol_2) not in brod_1 and (red_2 - 2,kol_2) not in brod_1:
                
                red_2_2 = red_2 - 1
                kol_2_2 = kol_2
                red_2_3 = red_2 - 2
                kol_2_3 = kol_2
                break
    if d == "desno":
        if kol_2 <= len(mreza[0])-3:
             if (red_2 ,kol_2 + 1) not in brod_1 and (red_2,kol_2 + 2) not in brod_1:
                
                red_2_2 = red_2
                kol_2_2 = kol_2 + 1
                red_2_3 = red_2
                kol_2_3 = kol_2 + 2
                break
    if d == "dole":
        if red_2 <= len(mreza)-3:
            if (red_2 + 1 ,kol_2) not in brod_1 and (red_2 + 2,kol_2) not in brod_1:
                
                red_2_2 = red_2 + 1
                kol_2_2 = kol_2
                red_2_3 = red_2 + 2
                kol_2_3 = kol_2
                break
    if d == "levo":
        if kol_2 >= 2:
            if (red_2 ,kol_2 - 1) not in brod_1 and (red_2,kol_2 - 2) not in brod_1:
                
                red_2_2 = red_2
                kol_2_2 = kol_2 - 1
                red_2_3 = red_2
                kol_2_3 = kol_2 - 2
                break



tacan = 0 #U ovoj promenljivoj smešta se ukupan broj pogođenih polja oba broda
prvi_brod = 0 #U ovoj promenljivoj smešta se broj pogođenih polja prvog broda
drugi_brod = 0 #U ovoj promenljivoj smešta se broj pogođenih polja drugog broda
#Na početku nemamo nijedno pogođeno polje, pa sve promenljive postavljamo na 0
#U ovoj promenljivoj smešta se ukupan broj pogođenih polja oba broda
tacan = 0 
#U ovoj promenljivoj smešta se broj pogođenih polja prvog broda
prvi_brod = 0 
#U ovoj promenljivoj smešta se broj pogođenih polja drugog broda
drugi_brod = 0 

#Dozvoljeno je 15 pokušaja da se potope oba broda
for pokusaj in range(1,16):
    print (str(pokusaj ) + '. pokusaj:')

    nagadjanje_reda  = int(input('Pogodite red:'))
    nagadjanje_kolone  = int(input('Pogodite kolonu:'))
#Ispituje se da li je korisnik pogodio neko polje prvog broda
#Ako jeste, broj pogođenih polja se povećava za jedan
    if ((nagadjanje_reda -1  == red_1 ) and (nagadjanje_kolone -1  == kol_1)) or ((nagadjanje_reda -1 == red_1_2 ) and (nagadjanje_kolone -1 == kol_1_2)) or((nagadjanje_reda -1 == red_1_3 ) and (nagadjanje_kolone -1 == kol_1_3)) and mreza[nagadjanje_reda -1 ][nagadjanje_kolone -1] != 'X' :
   

        tacan = tacan+1
        prvi_brod = prvi_brod + 1

        if (tacan != 6) and (prvi_brod != 3) :
            
           
            print ('Bravo, pogodak!')
            mreza[nagadjanje_reda -1 ][nagadjanje_kolone -1] = 'X'
#Ako je pogođeno polje treće polje prvog broda, korisnik se obaveštava da je potopio ceo brod
        elif (tacan != 6) and (prvi_brod == 3):
            
            mreza[nagadjanje_reda -1 ][nagadjanje_kolone -1] = 'X'

            print ('Bravo, potopili ste ceo brod! Ostao vam je jos jedan!')
#Ako je reč o šestom pogođenom polju, korisnik se obaveštava da je potopio oba broda
        if (tacan == 6):
            mreza[nagadjanje_reda -1][nagadjanje_kolone -1] = 'X'
            print ('Svaka cast, potopili ste oba broda!')
           
            break
#Ispituje se da li je korisnik pogodio neko polje drugog broda 
#Ako jeste, broj pogođenih polja se povećava za jedan

    elif   ((nagadjanje_reda -1  == red_2 ) and (nagadjanje_kolone -1  == kol_2)) or ((nagadjanje_reda -1  == red_2_2 ) and (nagadjanje_kolone -1  == kol_2_2)) or ((nagadjanje_reda -1  == red_2_3 ) and (nagadjanje_kolone -1  == kol_2_3)) 	 and mreza[nagadjanje_reda -1 ][nagadjanje_kolone -1] != 'Y'  :
        tacan = tacan+1
        drugi_brod = drugi_brod + 1
        if (tacan != 6) and (drugi_brod != 3):
            
            print ('Bravo, pogodak!')
            mreza[nagadjanje_reda -1 ][nagadjanje_kolone -1] = 'Y'
        elif (tacan != 6) and (drugi_brod ==3):
           
            mreza[nagadjanje_reda -1 ][nagadjanje_kolone -1] = 'Y'
#Ako je pogođeno polje, treće polje prvog broda, korisnik se obaveštava da je potopio ceo brod

            print ('Bravo, potopili ste ceo brod! Ostao vam je jos jedan!')
#Ako je reč o šestom pogođenom polju, korisnik se obaveštava da je potopio oba broda

        if (tacan == 6):
            mreza[nagadjanje_reda -1][nagadjanje_kolone -1] = 'Y'
            print ('Svaka cast, potopili ste oba broda!')
            break
    else:
        if (nagadjanje_reda < 1 or nagadjanje_reda > 7) or (nagadjanje_kolone < 1 or nagadjanje_kolone > 7):
            print ('Ups, izvan opsega ste!')
        elif (mreza[nagadjanje_reda -1 ][nagadjanje_kolone -1]=='X'):
            print ('Vec ste pronasli ovaj deo broda!')
        elif (mreza[nagadjanje_reda -1 ][nagadjanje_kolone -1]=='O'):
            print ('Vec ste pogadjali isto polje!')
        else:
            print ('Promasili ste!')
            mreza[nagadjanje_reda -1 ][nagadjanje_kolone -1] = 'O'


    stampaj_mrezu(mreza)
    if (pokusaj == 15):
            print ('Igra je zavrsena!')

if (mreza[red_1 ][kol_1 ] != "X" or mreza[red_1_2 ][kol_1_2 ] != "X" or
mreza[red_1_3 ][kol_1_3 ] != "X") or (mreza[red_2 ][kol_2 ] != "Y" or mreza[red_2_2 ][kol_2_2 ] != "Y" or
mreza[red_2_3 ][kol_2_3 ] != "Y"):
    print ('Brodovi su se nalazili na ovim pozicijama! Vise srece drugi put!')
    mreza[red_1 ][kol_1 ] = "X"
    mreza[red_1_2 ][kol_1_2 ] = "X"
    mreza[red_1_3][kol_1_3] = "X"
    mreza[red_2][kol_2 ] = "Y"
    mreza[red_2_2 ][kol_2_2] = "Y"
    mreza[red_2_3][kol_2_3 ] = "Y"


stampaj_mrezu(mreza)