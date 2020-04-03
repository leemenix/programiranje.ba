from random import randint 

mreza=[]
for i in range(0,5):
    mreza.append(["#"] * 5)
def stampaj_mrezu(mreza):
    for red in mreza:
        print (" ".join(red))
print ('Igra Potapanje brodova moze da pocne!')
stampaj_mrezu(mreza) 
#randint(a,b) funkcija vraća jedan nasumično izabran ceo broj iz intervala [a,b] 
#Red koji se bira može imati vrednost koja se nalazi u intervalu od 1 pa do dužine mreže
#U našem slučaju to je broj lista od kojih je mreža sastavljena (5)
def nasumicni_red(mreza):
    return randint(1, len(mreza))
#Kolona koja se bira može imati vrednost koja se nalazi u intervalu od 1 pa do broja članova liste
#Kako su sve liste iste dužine, može se uzeti proizvoljna.
#Ovde je izabrana prva lista(podsetimo se da indeksiranje počinje od 0)
def nasumicna_kolona(mreza):
    return randint(1, len(mreza[0]))


brod_red = nasumicni_red(mreza)
brod_kolona = nasumicna_kolona(mreza)

#Korisnik ima pet šansi da potopi brod
for i in range(5):
    red = i 
    nagadjanje_reda = int(input('Pogadjajte red:'))
    nagadjanje_kolona = int(input('Pogadjajte kolonu:'))
    
    if (nagadjanje_reda == brod_red) and (nagadjanje_kolona == brod_kolona):
        print ('Bravo! Potopili ste brod!')
        mreza[nagadjanje_reda-1][nagadjanje_kolona-1]='X'
        stampaj_mrezu(mreza)
        break
    else:
#U slučaju da igrač nije pogodio polje, može se desiti:
#Da je naveo red i kolonu izvan datog opsega
#Da je naveo koordinate polja koje je već otvarao       
        if (nagadjanje_reda < 1 or nagadjanje_reda > 5) or (nagadjanje_kolona < 1 or nagadjanje_kolona > 5):
            print ('Ups, izvan opsega ste!')
        elif(mreza[nagadjanje_reda-1][nagadjanje_kolona-1]=='O'):
            print ('Vec ste pogadjali!')
        else:
            print ('Promasili ste brod!')
            mreza[nagadjanje_reda-1][nagadjanje_kolona-1] = 'O'
            print (red + 1)
            stampaj_mrezu(mreza)
    if (red == 4):
            print ('Kraj igre!')
if(mreza[brod_red-1][brod_kolona-1]!='X'):
    #print ('Brod se nalazio na poziciji (%d,%d):') %(brod_red,brod_kolona)
    print ('Brod se nalazio na poziciji ' + str(brod_red) + " " + str(brod_kolona))
    mreza[brod_red-1][brod_kolona-1]='X'
    stampaj_mrezu(mreza)