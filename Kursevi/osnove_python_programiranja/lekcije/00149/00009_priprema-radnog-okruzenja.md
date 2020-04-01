
<div style="page-break-after: always;"></div>

## Priprema radnog okruzenja

### Izbor editora teksta i **Integrisanog razvojnog okruzenja** IDE (Integrated Development Environment)

#### Izbor tekst editora

Za pocetnike, se preporucuje koristenje nekog jednostavnog tekst editora kao Notpad++, Sublime, VisualStudio Code ...

#### Izbor Interisanog razvojnog okruzenja

Vecina programera odabere pisanje Python koda, koristenjem specijalnog 
integrisanog razvojnog okruzenja. Trenutno tri najistaknutija za Python su 
Eclipse, PyCharm i Netbeans. Za potrebe kursa, koristicemo **PyCharm**.

#### Instalacija Windows

##### Korak 1.

Nakon sto otvoritmo stranicu https://python.org potrebno je da skinemo 
instalacijski paket za trenutnu aktuelnu verziju Python-a.

Za vrijeme pisanje kursa verzija Python-a je bila 3.8.2, sto se moze 
razlikovati u vasem slucaju ali princip instalacije je isti ili slican.

Iz padajuceg menija "Downloads" potrebno je izabrati opciju "Windows"

![Python instalacija korak prvi](../../slike/python_instalacija_1.png)

##### Korak 2.

Na sledecoj stranici je potrebno kliknuti na 
**"Latest Python 3 Release - Python 3.8.2"**

![Python instalacija korak drugi](../../slike/python_instalacija_2.png)

##### Korak 3.

Sada je potrebno skrolati do dna stranice

![Python instalacija korak treci](../../slike/python_instalacija_3.png)

sve dok ne dodjemo do liste fajlova gdje mozemo skinuti instalacioni
fajl za nas sistem, koji je u nasem slucaju 
**"Windows x86-64 executable installer"**

![Python instalacija korak treci](../../slike/python_instalacija_4.png)

##### Korak 4.

Odaberemo lokaciju gdje zelimo sacuvati instalacioni fajl i sacuvamo ga
sa klikom na dugme **"Save"**

![Python instalacija korak prvi](../../slike/python_instalacija_5.png)

##### Korak 5.

Pokrenemo instalaciju Python-a, klikom na skinuti fajl. Veoma je vazno da u
ovom koraku **prvo** cekiramo opciju **"Add Python 3.8 to PATH"** a nakon 
toga kao tip instalacije izaberemo **"Customize installation"**. 

![Python instalacija korak prvi](../../slike/python_instalacija_6.png)

##### Korak 6.

Pod **"Optional Features"**, cekirajte sve opcije i kliknite na dugme 
**"Next"**

![Python instalacija korak prvi](../../slike/python_instalacija_7.png)

##### Korak 7.

Pod **"Advanced Options"**, veoma je vazno da cekriate opciju 
**"Install for all users** i kliknite na dugme **"Install"**. Primijeticete 
da se putanja do instalacije **"Customize install location"** automatski 
mijenja kada cekiramo navedenu opciju.

![Python instalacija korak prvi](../../slike/python_instalacija_8.png)

##### Korak 8.

Sada je vazno sacekati da se instalacija zavrsi i mozete kliknuti na 
**"Close"**

![Python instalacija korak prvi](../../slike/python_instalacija_9.png)

##### Korak 9.

Kako bi smo bili sigurni da je instalacija kompletna i uspjesna, pokrenucemo
**"cmd"** komandni prompt, tako sto cemo u Windows Search unijeti cmd i 
kliknuti na **""Command Prompt"**. 

![Python instalacija korak prvi](../../slike/python_instalacija_10.png)

##### Korak 10.

Ostaje jos da ukucamo komandu **"python"** i udarimo **"Enter"**, trebali
bi dobiti Python shell, kao na slici

![Python instalacija korak prvi](../../slike/python_instalacija_11.png)


#### PyCharm installation 

##### Korak 1.

Nakon sto otvoritmo stranicu https://www.jetbrains.com/pycharm/ potrebno je da 
skinemo instalacijski paket za trenutnu aktuelnu verziju PyCharm-a, 
jednostavnim klikom na dugme **"DOWNLOAD"**.

![PyCharm instalacija korak prvi](../../slike/pycharm_instalacija_1.png)

##### Korak 2.

Bitno je da izaberemo verziju **"Community"**, i nakon sto kliknemo 
na **"Download"** dobicemo opciju da sacuvamo instalacioni fajl.

![PyCharm instalacija korak prvi](../../slike/pycharm_instalacija_2.png)

##### Korak 3.

Odaberemo lokaciju gdje zelimo sacuvati instalacioni fajl i sacuvamo ga
sa klikom na dugme **"Save"**

![PyCharm instalacija korak prvi](../../slike/pycharm_instalacija_3.png)

##### Korak 4.

Pokrenemo instalaciju PyCharm-a, klikom na skinuti fajl. Sada je potrebno 
kliknuti na dugme **"Next"**. 

![PyCharm instalacija korak prvi](../../slike/pycharm_instalacija_4.png)

##### Korak 5.

Ponovo izaberite dugme **"Next"**. 

![PyCharm instalacija korak prvi](../../slike/pycharm_instalacija_5.png)

##### Korak 6.

U prozoru **"Installation Options"**, bitno je da cekirate sledece opcije
**"64-bit launcher"**, **"Add launchers dir to the PATH"**, **".py"**. 

![PyCharm instalacija korak prvi](../../slike/pycharm_instalacija_6.png)

##### Korak 7.

U ovom koraku je bitno kliknuti na dugme **"Install"**.

![PyCharm instalacija korak prvi](../../slike/pycharm_instalacija_7.png)

##### Korak 8.

Mozete kliknuti na dugme **"Finish"**. Nakon sto se sistem restartuje mozemo
krenuti sa osnovnim podesavanjem PyCharm radnog okruzenja.

![PyCharm instalacija korak prvi](../../slike/pycharm_instalacija_8.png)

#### Podesavanje PyCharm-a i nas prvi program "Zdravo Svijete"


##### Korak 1.

Prilikom prvog ili inicijalnog pokretanja PyCharm programa potrebno je da 
izvrsimo osnovna podesavanja, kako bi prilagodili program za potrebe kursa i 
lakse pracenje. 
Na ovom koraku mozete ostaviti cekiranu opciju **"Do not import settings"** i
nastaviti dalje sa klikom na dugme **"OK"**.

![PyCharm instalacija korak prvi](../../slike/pycharm_podesavanje_1.png)

##### Korak 2.

U ovom koraku je potrebno cekirati polje 
**"I confirm that I have read and accept the terms of this User Agreement"**, 
cime se slazemo sa polisom koristenja ovog PyChar programa i naravno za dalje
kliknuti dugme **"Continue"**.

![PyCharm instalacija korak prvi](../../slike/pycharm_podesavanje_2.png)

##### Korak 3.

Obzirom da ne zelimo slati nikakvu statistiku sa naseg kompjutera, ovde cemo
izabrati opciju **"Don't send".

![PyCharm instalacija korak prvi](../../slike/pycharm_podesavanje_3.png)

##### Korak 4.

Ovaj korak se odnosi na izbor teme, za potrebe kursa koristicemo **"Light"** 
temu, naravno vi mozete izabrati koja vam vise odgovara. Konacno mozemo 
kliknuti na dugme **"Skip Remaining and Set Defaults"**. 

![PyCharm instalacija korak prvi](../../slike/pycharm_podesavanje_4.png)

##### Korak 5.

U sledecem prozoru mozemo odabrati opciju **"Crate New Project"**, nakon 
cega moramo podesiti radno okruzenje za novi projekt. 

![PyCharm instalacija korak prvi](../../slike/pycharm_podesavanje_5.png)

##### Korak 6.

Nazovimo projekt **"moj_novi_projekt"** i kliknimo na dugme **"Create"**.

![PyCharm instalacija korak prvi](../../slike/pycharm_podesavanje_6.png)

##### Korak 7.

Sada je potrebno sacekati kako bi se kreiralo virtuelno okruzenje za nas novi
projekat. 

![PyCharm instalacija korak prvi](../../slike/pycharm_podesavanje_7.png)

##### Korak 8.

Nakon sto se okruzenej kreiralo, opciono mozemo onemoguciti opciju 
**"Show tips on startup"** i kliknuti na dugme **"Close"**

![PyCharm instalacija korak prvi](../../slike/pycharm_podesavanje_8.png)

##### Korak 9.

Iz menija izaberite opciju **"File"**

![PyCharm instalacija korak prvi](../../slike/pycharm_podesavanje_9.png)

##### Korak 10.

zatim odaberite **"Python file"**

![PyCharm instalacija korak prvi](../../slike/pycharm_podesavanje_10.png)

##### Korak 13.

a nakon toga dajte ime fajlu **"moj_prvi_program"** i kliknite **"Enter"**.
Ovime smo kreirali novi fajl moj_prvi_program.py (ekstenziju .py ce dodijeliti
sam PyCharm, na nama je samo da damo ime programu).
![PyCharm instalacija korak prvi](../../slike/pycharm_podesavanje_13.png)

##### Korak 14.
![PyCharm instalacija korak prvi](../../slike/pycharm_podesavanje_14.png)

##### Korak 15.
![PyCharm instalacija korak prvi](../../slike/pycharm_podesavanje_15.png)

##### Korak 16.
![PyCharm instalacija korak prvi](../../slike/pycharm_podesavanje_16.png)


  - promjena teme, odredisnog direktorija, velicine fonta i sl.
  - New -> Python File ...

  - Sublime installation, notpad ++
  - mi cemo koristiti PyCharm - IDE (Integrated Development Environment) 

- python 2 (legacy), python 3 (future)
  - razlika u sintaksi