Python Overview
Python is a general purpose, dynamically typed and interpreted, object oriented programming language that was created in the late 1980s by Guido van Rossum.

Python’s design philosophy revolves around readability. It’s meant to be easy to read and easy to write. This is accomplished by using white-space to deliniate code blocks instead of the more traditional curly brackets and semi-colons.

How Python Runs
Generally all python code is run using an interpreter. The most popular and original interpreter is called CPython, because it’s implemented in the c programming language. Several other interpreters exist however, many of which are implemented in languages other than C like Java and C#.

The most common Python interpreter CPython, uses an automatic garbage collector to manage memory. And Python is widely known for having a non-traditional, minimalist syntax which is largly based on white space, and designed to be clean and readable.

Python Versions
When first getting into python it can be a bit confusing becasue unlike many other programming languages Python has two major, non-compatible versions that are currently widely used.

Python version 2.7.3, released in 2012, is the last iteration of verison 2 that was released. This verison is for the most part, backwards compatiable with all previous versions.

In 2008, the Founder, Guido van Rossum decided to clean up the Python codebase and overhall a lot of the things in Python 2 that he didn’t like, thus creating Python 3.

Python 3 was adopted slowly at first, mainly because it is not backwards compatible with Python 2, and there was a huge eco-system of package libraries written for Python 2 which now would not work in python 3.

But now-a-day’s the Python 3 ecosystem has for the most part caught up, making Python 3 the obvious choice for new developers looking to learn the language. Python 3 is also the version that will be taught in this tutorial.

Choosing an IDE
Many developers choose to write Python using a specilized integrated development enviornment. Three of the most popular are Eclipse, PyCharm and Netbeans.


python 3 - uvod u python programski jezik

- jednostavan za ucenje

- kurs je dizajniran za sto jednostavnije ucenje

- citavo vrijeme cete biti vodjenji


- PyCharm installation (Win, Linux)

- Sublime installation, notpad ++
  - mi cemo koristiti PyCharm - IDE (Integrated Development Environment) 

- python 2 (legacy), python 3 (future)
  - razlika u sintaksi

### Zdravo Svijete
- podesavanje PyCharm-a i nas prvi program
  - promjena teme, odredisnog direktorija, velicine fonta i sl.
  - New -> Python File ...
     - pozdrav_svijete.py
      
       print("Zdravo Svijete!")

  - dva nacina za pokretanje Python programa i kada koji koristiti
    - cmd, terminal - (ako nesto zelimo da provjerimo brzo i trenutno)
    - direktno iz IDE-a (precice) - (kada pisemo vise linija koda)

- drugi program
  - programiranje je davanje instrukcija kompjuteru (kroz programski jezik) 
  - crtanje_oblika.py (priprema za igricu vjesala)
```python
    print("_______")
    print("|     ?")
    print("|      ")
    print("|      ")
    print("|      ")
```
  - u ovom slucaju python ide liniju po liniju i izvrsava kod
  - sta se desava u slucaju da zamijenimo prvu i zadnju liniju?

Zadaci za samostalni rad!
  - napisati program koji ispicuje vase Ime i prezime
  - napisati program koji crta pravougaonik oblika
```python
    __________
    |         |
    |         |
    |_________|
```
  - napisati program koji crta trougao oblika
```python
        /\
       /  \
      /    \
     /      \
    /________\
```

# komentarisanje koda
  - upisavanje podsjetnika
  - komentarisanje koda
  - preporuka da se koristi taraba
  # ovo je taraba (hash tag) simbol
  # komentari su po default-u ignorisani u python-u
  '''
  Viselinijski komentar
  '''
  """
  Viselinijski komentar
  """
  print("Komentari su korisni")
  # print("Ova linija koda nece biti ispisana")

### promjenjive i tipovi podataka

- promjenjive, varijable (variables) 
  - programiranje se uglavnom svodi na obradu podataka, stim u vezi je potrebno pohraniti podatke 
    i organizovati ih na najbolji moguci nacin. postoji nesto sto se zove CRUD (Create,Read, Update, Delete)

  - tri glavna faktora koji cine promjenjivu/varijablu jesu
    naziv, operator i vrijednost varijable
    
    naziv | operator | vrijednost
    
    ime        =        "Darko"

    godine     =           23

  - gradjenje varijable
    - naziv varijable ne smije poceti sa brojem
    - naziv varijable moze poceti, malim, velikim slovima ili donjom crticom (_)
      nakon cega moze ici broj
    - malo a i veliko A se razlikuju (a != A)

    - naziv_varijabli.py
        ime = "Darko"
        godine = 23
        _nove_godine = 24
        25_godine = 25 # ovde cemo dobiti gresku
        a = 3
        A = 4

        print (ime)
        print (godine)
        print (_nove_godine)
        print (25_godine) # ovde cemo dobiti gresku
        print (a)
        print (A) 
    
    - prakticna_primjena_varijabli.py - (Dragon Ball - Zmajeva Kugla)

        karakter_1 = "Son Goku"
        karakter_2 = "Krilin"
        godine = "17"

        print("U dalekoj proslosti zivio je djecak po imenu Goku.")
        print("Goku je imao 15 godina.")
        print("Volio je upoznavati nove karaktere ")
        print("i imao je najboljeg druga po imenu Krilin!")
        print (" ")
        print("U dalekoj proslosti zivio je djecak po imenu " + karakter_1)
        print(karakter_1 + " je imao " + godine + " godina.")
        print("Volio je upoznavati nove karaktere ")
        print("i imao je najboljeg druga po imenu " + karakter_2)

  - Tipovi podataka
    - Znakovni (string)
      - string()
    - Brojevi cijeli, realni (integer, float)
      - int()
      - float()
    - Logicki tacno, netacno (boolean True/False)
      - bool()

    - korisna funkcija type
      print(type(karakter_ime))

      tipovi_podataka.py

        karakter_ime = "Goku"
        karakter_godine = 15
        karakter_visina = 168.5
        karakter_osobina_dobar = True
        karakter_osobina_los = False

        print(karakter_ime + " ima " + karakter_godine)
        print(karakter_ime + " ce za godinu dana imati " + karakter_godine + 1)
        print(karakter_ime + " je visok " + karakter_visina + "cm.")
        print(karakter_ime + " ce za godinu dana biti visok " + (karakter_visina + 5) + " cm.")
        print(karakter_ime + " je dobar karakter" + karakter_osobina_dobar)
        print(karakter_ime + " je los karakter" + karakter_osobina_los)

        karakter_ime = "Goku"
        karakter_godine = 15
        karakter_visina = 164.5
        karakter_osobina_dobar = True
        karakter_osobina_los = False

        print(karakter_ime + " ima " + str(karakter_godine))
        print(karakter_ime + " ce za godinu dana imati " + str(karakter_godine + 1))
        print(karakter_ime + " je visok " + str(karakter_visina) + " cm.")
        print(karakter_ime + " ce za godinu dana biti visok " + str(karakter_visina + 5) + " cm.")
        print(karakter_ime + " je dobar karakter " + str(karakter_osobina_dobar))
        print(karakter_ime + " je los karakter " + str(karakter_osobina_los))

  - Rad sa stringovima
      - tekst, rad sa tekstom, funkcije nad stringovima

      rad_sa_stringovima.py
        print("programiranje.ba besplatni online kursevi")

        # escape karakter \
        print("programiranje.ba \n besplatni online kursevi")

        sajt_naziv = "programiranje.ba"
        sajt_slogan = " besplatni online kursevi"
        print(sajt_naziv)
        print(sajt_slogan)
        print(sajt_naziv + sajt_slogan)
        print(sajt_naziv.upper() + sajt_slogan.upper())
        print(sajt_naziv.isupper())
        print(len(sajt_naziv))
        # index stringa pocinje na poziciji 0
        print(sajt_naziv[4])
        # index funkcija i proslijedjivanje parametara
        print(sajt_naziv.index('g'))
        print(sajt_naziv.index('mira'))
        #print(sajt_naziv.index('h'))

        print(sajt_slogan.replace("kursevi","tutoriali").upper())

        print("{1}, {0}".format(sajt_naziv, sajt_slogan))
        print(f"{sajt_naziv} {sajt_naziv}")

        ### char i ord kasnije potrebni za cezarovu sifru 

  - Rad sa brojevima
    - brojevi, rad sa brojevima, funkcije nad brojevima

    print(3)
    print(-4)
    print(3.333)
    print(7+3)
    print(7+3.333)
    print(8/4)
    print(2*4)
    print (2*(4+5))
    # modulo , ostatak 9 mod 4
    print(9%4)

    moj_broj = 13
    print(moj_broj)
    print("Moj omiljeni broj" + str(moj_broj))
    
    # math funkcije, funkcije su vec pripremljen kod koji odradjuje posao za nas
    broj = -2
    print(abs(broj))
    print(pow(4,2))
    print(max(5,10))
    print(min(3,6))
    print(round(3.3333))
    print(round(3.6))
    print(round(3.5))

    # import math modul (import math funkcije vise kada budemo pricali o modulima)
    from math import *
    print(floor (3.6))
    print(ceil(3.6))
    print(sqrt(9))

  - Ulaz/upis podataka, prihvacanje podataka od korisnika

    input() # hej ti, cekam da uneses neku informaciju podatak
    input("Unesite vase ime: ")
    korisnik_ime = input("Unesite vase ime: ")
    print("Zdravo, " + korisnik_ime + " dobrodosli.")

    korisnik_ime = input("Unesite vase ime: ")
    korisnik_godine = input("Unesite vase godine: ")
    print("Zdravo, " + korisnik_ime + ". Vi imate " + korisnik_godine + " godina.")

    # vjezba ispisati preghodni program koristeci funkciju format

    osnovni_kalkulator.py
    broj_1 = input("Unesite prvi broj: ")
    broj_2 = input("Unesite drugi broj: ")
    rezultat = broj1 + broj2

    print(rezultat)

    broj_1 = input("Unesite prvi broj: ")
    broj_2 = input("Unesite drugi broj: ")
    rezultat = float(broj_1) + float(broj_2)

    print(rezultat)

    interaktivni_karakter_program.py
        print("U dalekoj proslosti zivio je djecak po imenu Goku.")
        print("Goku je imao 15 godina.")
        print("Volio je upoznavati nove karaktere ")
        print("i imao je najboljeg druga po imenu Krilin!")

        karakter_ime = input("Unesite ime karaktera: ")
        karakter_godine = input("Unesite godine karaktera: ")
        karakter_prijatelj = input("Unesite ime najboljeg prijatelja: ")

        print(f"U dalekoj proslosti zivio je djecak po imenu {karakter_ime}.")
        print(f"{karakter_ime} je imao {karakter_godine} godina.")
        print(f"Volio je upoznavati nove karaktere ")
        print(f"i imao je najboljeg druga po imenu {karakter_prijatelj}!")

  - Liste - []
    - rad sa listama, velik broj podataka (organizacija i pracenje podataka)

    karakteri = ["Goku", "Krilin", "Bulma", "Chi-Chi", "Yamcha", "Picolo"]
    print(karakteri)

    # mozete smjestiti stringove , brojeve, boolean u liste
    # referenciranje po indexu, ako zelimo pristupiti elementu unutar liste
    print(karakteri[0])
    print(karakteri[4])

    print(karakteri[-1])
    print(karakteri[-2])

    print(karakteri[1:])
    print(karakteri[2:4])
    print(karakteri[2:-2])
    
    # izmjena elemenata u listi
    karakteri[4] = "Master Roshi"
    print(karakteri[4])
    print(karakteri)

    - funkcije nad listama
    karakteri = ["Goku", "Krilin", "Bulma", "Chi-Chi", "Yamcha", "Picolo"]
    print(karakteri)
    loto_brojevi = [4, 7, 3, 10, 32]
    print(loto_brojevi)

    karakteri.extends(loto_brojevi)
    print(karakteri)

    karakteri.append("Majin Buu")

    print(karakteri)

    karakteri.insert(2, "Vegeta")
    print(karakteri)

    karakteri.remove("Majin Buu")
    print(karakteri)

    karakteri.pop()
    print(karakteri)

    karakteri.clear("")
    print(karakteri)

    # provjeri da li je odredjeni element u listi
    
        karakteri = ["Goku", "Krilin", "Bulma", "Chi-Chi", "Yamcha", "Picolo", "Bulma"]
        print(karakteri)

        print(len(karakteri))

        print(karakteri.index("Bulma"))

        print(karakteri.count("Bulma"))

        karakteri.sort()
        print(karakteri)

        karakteri.reverse()
        print(karakteri)

        karakteri_novi = karakteri.copy()

        print(karakteri_novi)

        karakteri_novi.sort()
        print(karakteri_novi)

  - Tuples (tip podaktovne strukture, veoma slican listama) - ()
    - razlike od liste
      - immutable (ne mogu se mijenjati) za razliku od listi

    koorinate.py
    
    koordinate = (4, 5)
    print(type(koordinate))
    print (len(koordinate))
    print(koordinate.index(5))
    print(koordinate[0])
    print(koordinate[1])

    koordinate[1] = 10 # dobicemo gresku

    # list of tuples
    koordinate = [(4,5), (6,3), (7.4)]
    print(type(koordinate))

    print(len(koordinate))



  - Rijecnik - Dictionaries - {}
    - standardni rijecnik koji imamo ima strukturu rijec i detaljno objasnjenje rijece
      gdje rijec predstavlja kljuc (key), vrijednost (value) predstavlja definiciju
      key mora biti jedinstven

    Jan -> Januar
    Mar -> Mart
    
    konverzijaMjeseci = {
        "Jan": "Januar",
        "Feb": "Februar",
        "Mar": "Mart"
    }

    print(konverzijaMjeseci["Jan"])
    print(konverzijaMjeseci["Feb"])
    print(konverzijaMjeseci["Mar"])

    print(konverzijaMjeseci.get("Jan"))
    print(konverzijaMjeseci.get("Dec"))
    print(konverzijaMjeseci.get("Dec","Nije validan kljuc"))

  - Funkcije
    skup kodova koje odradjuju odredjene zadatke
    dobri su za organizaciju koda

    kako kreirati funkcije

    zdravo_svijete_funkcija.py
    
    # kad god se pojavi def na pocetku, python zna da korisnik zeli kreirati funkciju
    def zdravo_svijete():
      print("Zdravo Svijete.")
    
    # moramo pozvati funkciju ako zelimo da je izvrsimo
    zdravo_svijete()

    def zdravo_svijete():
      print("Zdravo Svijete.")
    
    print("Prije funkcije")
    zdravo_svijete()
    print("Nakon funkcije")

    # prosledjivanje parametara funkciji
    
    def zdravo_svijete(ime):
      print("Zdravo " + ime)
    
    # moramo pozvati funkciju ako zelimo da je izvrsimo
    zdravo_svijete("Goku")
    zdravo_svijete("Krilin")

    def zdravo_svijete(ime,godine):
      print("Zdravo " + ime + " vi imate " + str(godine))
    
    # moramo pozvati funkciju ako zelimo da je izvrsimo
    zdravo_svijete("Goku", "15")
    zdravo_svijete("Krilin", "16")

    # primjer funkcije sa korisnickim unosom
    korisnik_ime = input("Unesite ime : ")
    def pozdrav(ime):
        print ("Zdravo " + ime)

    pozdrav(korisnik_ime)

  ### - Return izraz/direktiva statement  
    - kada zelimo dobiti povratnu informaciju iz funkcije koristimo return direktivu
    - kada zelimo da funkcije mogu medjusobno komunicirati

    2 na trecu

    def kub(broj):
      broj * broj * broj
    
    cub(3)

    print(kub(3))

    #### 
    def kub(broj):
      return broj * broj * broj # aha zelim vratiti informaciju ko god da je pozvao funkciju
    
    print(kub(3))

    #### 
    def kub(broj):
      return broj * broj * broj 
    
    rezultat - kub(3) # sacuvaj vrijednost koju si dobio od funkcije, ne i samu funkciju
    print(rezultat)

    #### 
    def kub(broj):
      print("stampaj prije return direktive")
      return broj * broj * broj
      print("stampaj nakon return direktive")
    
    print(cub(3))


  ### uslov if
    - donosenje odluke, na osnovu uslova koji se moraju ispuniti
    - krairamo program pametnijim, omogucujemo donosenje odluke

    Probudio sam se i oprao zube
    ako sam gladan
      trebam doruckovati

    Trebam ici u vani
    ako je oblacno
      ponijecu kisobran
    u suprotnom 
      ponijecu suncane naocare

    U restoranu 
    ako zelim meso
      narucicu stejk
    ako zelim pastu
      narucicu spagete
    u suprotnom
      narucicu salatu

    dobar = True
    
    if dobar:
      print("Goku je dobar karakter")
    
    #### 
    dobar = True
    zabavan = False
    
    if dobar or smijesan:
      print("Goku je dobar karakter") # koliko god koda mozete smjestiti ovde
      print("Freza nije je zabavan")
    else:
      print("Freza je los karakter")

    ### 
    dobar = True
    zabavan = True
    
    if dobar and smijesan:
      print("Goku je dobar karakter") # koliko god koda mozete smjestiti ovde
      print("Krilin je zabavan")
    else:
      print("Freza je los karakter")

    #### 
    dobar = True
    zabavan = False
    
    if dobar or smijesan:
      print("Goku je dobar karakter") # koliko god koda mozete smjestiti ovde
    elseif dobar and not(zabavan):
      print("Freza nije je zabavan")
    else:
      print("Freza je los karakter")

    ### - operatori poredjenja i uslov if (>,<, >=, <=, ==, !=)

    maksimalan_broj.py

    def maksimalan_broj(broj_1, broj_2, broj_3):
      if broj_1  >= broj_2 and broj_1 >= broj_3:
        return broj_1
      elif broj_2 >= broj_1 and broj_2 >=broj_3:
        return broj_2
      else:
        return broj_3

    print(maksimalan_broj(7, 8, 9))


    ### kalkulator_nadogradjena_verzija.py
   osnovni_kalkulator.py
    broj_1 = input("Unesite prvi broj: ")
    broj_2 = input("Unesite drugi broj: ")
    rezultat = broj1 + broj2

    print(rezultat)

    broj_1 = input("Unesite prvi broj: ")
    broj_2 = input("Unesite drugi broj: ")
    rezultat = float(broj_1) + float(broj_2)

    print(rezultat)
    ###########
    kalkulator_nadogradjena_verzija.py
    broj_1 = float(input("Unesite prvi broj: "))
    broj_2 = float(input("Unesite drugi broj: "))
    operator = input("Unesite operator: [+, -, /, *] ")
 
    if operator == "+":
      print(broj_1 + broj_2)
    elif operator == "-":
      print(broj_1 - broj_2)
    elif operator == "/":
      print(broj_1 / broj_2)
    elif operator == "*":
      print(broj_1 * broj_2)
    else: 
      print("unijeli ste pogresan operator")

  ### while petlja 
    - struktura u python koja nam omogucava da prolazimo kroz isti kod vise puta, onoliko puta
    koliko smo to zadali inicijalnim uslovom
    - kroz svaku od iteracija kroz kod while ce da izvrsi sve sto je unutar while petlje
    
    while_brojac.py
    i = 1
    while i <= 10:
      print("Vrijednost i je : " + i)
      #i = i + 1
      i += 1

    print("Kraj brojaca")
    

    igra_pogadjanja.py - primjenimo sve do sad nauceno

    tajna_rijec = "python"

    pokusaj = ""

    while guess != tajna_rijec:
      pokusaj = input("Pokusajte pogoditi tajnu rijec: ")

    print("Cestitamo, pogodili ste")

    # limitiraj broj pogresnih pokusaja
        tajna_rijec = "python"
        pokusaj = ""
        pokusaj_broj = 0
        pokusaj_limit = 4
        kraj_igre=False

        while pokusaj != tajna_rijec and not(kraj_igre):
        if pokusaj_broj < pokusaj_limit:
            pokusaj = input("Pokusajte pogoditi tajnu rijec: ")
            pokusaj_broj += 1
        else:
            kraj_igre = True

        if kraj_igre:
            print("Iskoristili ste sve pokusaje. Kraj igre")
        else:
            print("Cestitamo, pogodili ste")

  ### for petlja
    - specijalni tip petlje u python-u

    for slovo in "programiranje.ba":
      print(slovo)

    for karakter in karakteri:
      print(karakter)

    karakteri = ["Goku", "Kirlin", "Yamcha"]
    for indeks in range(len(karakteri)):
      print (karakteri[indeks])



    for broj in range(20):
      print(broj)

    for broj in range(14, 20):
      print (broj)

    for indeks in range(len(karakteri)):
      print (karakter[indeks])

    for broj in range(5):
        if broj == 0:
            print("prvi pokusaj")
        else:
            print("ostali")

    for i in range(10):
        print (i)
        i+=1

    ### eksponencijaln funkcija - kada ne znamo koliko je eksponent
    print(2**3)

    def eksponent_broja(baza, eksponent):
      rezultat = 1
      for index in range(exponent):
        rezultat = rezultat * baza
      return rezultat

    print(exponent_broja(2,4))

    ### dvodimenzionalne liste i ugnijezdene petlje (nested)


    resetka = [
        [1, 2, 3],
        [4, 5, 6],
        [7 ,8 ,9],
        [0]
    ]

    print(resetka[0][2])
    print(resetka[2][1])
    print(resetka[3][0])

    # nested for loop

    # resetka = [
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7 ,8 ,9],
    #     [0]
    # ]

    for row in resetka:
      for col in row:
        print(col)

    for col in resetka:
    for row in col:
        print(row)
        
    # cezarova sifra u python
    def enkripcija(tekst, pomak):
      rezultat = ""

      for broj in range(len(tekst)):
        slovo = tekst[broj]
        
      if(slovo.isupper()):
        rezultat += chr((ord(slovo) + pomak - 65) % 26 + 65)
      else: 
        rezultat += chr((ord(slovo) + pomak - 97) % 26 + 65)
      return rezultat

    tekst = input("Unesite tekst: ")
    pomak = 2

    print("Unijeli ste: " + tekst)
    print("Pomak: " + str(pomak))
    print("Sifrovan tekst: " + enkripcija(tekst, pomak))

### try / except (catch) - hvatanje greski
  - kada ne zelimo da nas program puca
  - ipak zelimo da nastavimo i da damo informaciju korisniku
  try:
    broj = int(input("Unesite broj: "))
    print(broj)
  except:
    print("Pogresan unos")

  ### 
  

  try:
    vrijednost = 10 / 0
    broj = int(input("Unesite broj: "))
    print(broj)
  except ZeroDivisionErron:
    print("Dijeljenje sa nulom")
  except ValueError:
    print("Pogresan unos")

  ### 
  

  try:
    vrijednost = 10 / 0
    broj = int(input("Unesite broj: "))
    print(broj)
  except ZeroDivisionErron as err:
    print(err)
  except ValueError:
    print("Pogresan unos")

  ### citanje iz eksternog fajla
  - dosta puta imamo potrebu za citanjem sadrzaja iz drugih fajlova
  - parsiranje teksta ...
  - apsolutni, relativna lokacija

  karakteri_porijeklo.txt
  Goku - Sayan
  Krilin - Zemlja
  Piccolo - Namek
  Frieza - Universe 7

  # r - read; w - write; a - append to end of file; r+ - read and write
  # otvoren fajl
  karakteri_fajl = open("karakteri_porijeklo.txt", "r")
  
  # provjeri da li je fajl citljiv
  print(karakteri_fajl.readable())

  # citanje informacija iz fajla
  print(karakteri_fajl.read())

  # citanje linije u fajlu
  print(karakteri_fajl.readline())
  print(karakteri_fajl.readline())
  print(karakteri_fajl.readline())
  print(karakteri_fajl.readline())

  # citanje linije po liniju, citaj svaku liniju i pohrani u niz
  print(karakteri_fajl.readlines())

  # koristenjem for petlje
  for karakter in karakteri_fajl.readlines():
    print(karakter)

  karakteri_fajl.close()

  ### upisivanje u eksterni fajl

   karakteri_fajl = open("karakteri_porijeklo.txt", "a")

   karakteri_fajl.write("Bulma - Zemlja")
   karakteri_fajl.write("\n Chi-Chi - Zemlja")

   karakteri_fajl.close()

   ### upisivanje u eksterni fajl

   karakteri_fajl = open("karakteri_porijeklo_novi.txt", "w")

   karakteri_fajl.write("Bulma - Zemlja")
   karakteri_fajl.write("\n Chi-Chi - Zemlja")

   karakteri_fajl.close()

   ### modules and pip 
   - python fajl koji mozete importovati unutar vaseg python koda
   - kako kreirati svoj modul
   - kako instalirati module (list of python modules on google) pip paket manager
   - build-in moduli (ugradjeni) i eksterni moduli
     
   korisni_alati.py
    #
    import random

    def srecan_broj(broj):
        return random.randint(1, broj)

    def pozdrav(tekst):
        return ("Pozdrav " + tekst)

    ##
    import korisni_alati

    print(korisni_alati.srecan_broj(3))
    print(korisni_alati.pozdrav("Goku"))
    
    ##
    from korisni_alati import *

    print(srecan_broj(3))
    print(pozdrav("Goku"))

    ##
    import korisni_alati as ka

    print(ka.srecan_broj(3))
    print(ka.pozdrav("Goku"))

    ## how to install with pip
    ## how to import and use modules

    ## klase i objekti
    - ekstremno korisni , organizovan i mocniji
    - kada radimo sa programiranjem susrecemo se sa razlicitim tipovima podataka
    - takodje susrecemo se sa razlicitim strukturama podataka
    - sta u slucaju kad ne mozemo predstaviti neku pojavu iz prirode sa vec postojecim tipovima 
      ili strukturama podataka
    - u python-u mozemo krairati klase (definise vas licni tip podatka, ponasa se kao template, patern
      kako nesto treba da izgleda)
    - objekat je podatak u memoriji, pravi podatak kreiran iz klase

    student.py
    # posto ne postoji student tip podaka, kreiracemo klasu student
    Student.py
    class Student:
      # inicijalizacija klase (inicijalna funkcija)  
      def __init__(self, ime, smjer, ocjena, brucos):
        self.ime = ime
        self.smjer = smjer
        self.ocjena = ocjena
        self.brucos = brucos
    

    from Student import Student

    # kreiranje student_prvi objetka
    student_prvi = Student("Darko", "Programiranje", 8, False)
    print(student_prvi)
    print(student_prvi.ime)
    print(student_prvi.ocjena)

    student_drugi = Student("Dragan", "Ekonomija", 8.3, True) 
    print(student_drugi.brucos) 

    ## funkcije unutar klase (funkcije objekta)
    class Student:
      def __init__(self, ime, smjer, ocjena, brucos):
        self.ime = ime
        self.smjer = smjer
        self.ocjena = ocjena
        self.brucos = brucos

      def dobar(self):
        if self.ocjena >= 7:
          return True
        else:
          return False

    ## naslijedjivanje
    - u slucaju da imamo klasu, kada kreiramo novu klasu mozemo naslijediti staru klasu
    - nova klasa ce imati sve osobine stare klase sa novim opcijama
    
    Kuvar.py
    class Kuvar:
        def priprema_mesa(self):
            print ("Priprema pileceg mesa.")

        def priprema_salate(self):
            print("Pirprema Cezar salata")

        def priprema_specijalnog_jela(self):
            print("Priprema rebarcadi")

    KineskiKuvar.py
    from Kuvar import Kuvar

    class KineskiKuvar(Kuvar):
        def priprema_rize(self):
            print("Priprema rize na kineski nacin")

        def priprema_specijalnog_jela(self):
            print ("Pekinska patka")

    from Kuvar import Kuvar
    from KineskiKuvar import KineskiKuvar

    novi_kuvar = Kuvar()

    novi_kuvar.priprema_mesa()
    novi_kuvar.priprema_specijalnog_jela()

    novi_kineski_kuvar = KineskiKuvar()

    novi_kineski_kuvar.priprema_rize()
    novi_kineski_kuvar.priprema_mesa()
    novi_kineski_kuvar.priprema_specijalnog_jela()

    ## kviz sa vise opcija

    

    - devet_depresivaca.py - (Rambo Amadeus - Devet depresivaca)
        print("9 depresivaca gajili su bostan")
        print("Puko lastik od bandzija, ostalo ih 8")

        print("8 depresivaca, k'o u dlan ih gledam")
        print("u krivini hladnjaca, ostalo ih 7")

        print("7 depresivaca, opet losa vijest")
        print("Neuzemljen bojler, ostalo ih 6")
        
        print("6 depresivaca, turbulentan let")
        print("Dnevno kilo vinjaka, ostalo ih 5")

        print("5 depresivaca bez mrlje na jetri")
        print("Moca od pecenja, ostalo ih 4")

        print("4 depresivca, veseli su svi")
        print("Droga jeftinija od viskija, ostalo ih 3")

        print("3 depresivca, svaki od njih vrijedan")
        print("Dvojici crko facebook, ostao je 1")

        print("1 depresivac, oprezan je bio")
        print("Onda se ozenio")

        

