
<div style="page-break-after: always;"></div>

<a name="istorija-pythona"/>

## Par rijeci o Python programskom jeziku

Python je jedan od rijetkih programskih jezika, koji je u isto vrijeme jednostavan i mocan. Nemojte se iznenaditi ako vam ucenje Python programskog jezika ide veoma lako i brzo savladavate lekcije, jer to i jeste cilj Python kao programskog jezika, da vam omoguci usmjeravanje paznje na rjesavanje konkretnog problema i pronalaznje rjesenja, umjesto da morate voditi racuna o sintaksi i strukturi programskog jezika kao sto je slucaj kod vecine ostalih programskih jezika.

Python je programski jezik opste namjene, sa elegantnom sintaksom i dinamikom, 
zajedno sa svojom prirodom interpretera, ali i mogucnoscu objektno orijentisanog nacina programiranja, pored sto je moze pisati skripte nudi 
mogucnost brzog razvoja aplikacija na razlicitim operativnim sistemima. 

Jezik Python je kreiran u kasnim 80-tim od strane holandskog programera koji 
se zove **Guido van Rossum**, a naziv Python je dobio po BBC emisiji "Leteci 
Cirkus Monti Pajtona" (Monty Python's Flying Circus), cime je kreator htio na 
saljiv nacin da predstavi i programiranje kao takvo, jednostavno i zabavno.

Dizajn filozofija Python-a se svodi na jednostavnu citljivost, dakle u prvom 
planu ima za cilj sto lakse citanje i pisanje koda. Ovo se postize koristenjem
white-space za odvajanje blokova koda umjesto vec dobro poznatog i ustaljenog 
nacina koristenja uglastih zagrada **{}** i tacke zareza **;**. 

### Kako pokrenuti Python
Generalno sav python kod se pokrece koristenjem interpretera. Najpopularniji i 
orginalni interpreter je CPython, zato sto je implementiran u C programskom 
jeziku. Takodje, postoji i par drugih interpretera, a mnogi od njih su 
implementirani u razlicitim jezicima od C-a, kao sto su Java ili C# (C sharp).

Najcesce koristen interpreter CPython, koristi automatski garabage koletor 
(sakupljac smeca :), kako bi obezbijedio nesmetano  i efikasno upravljenje 
memorijom kompjutera. Python je siroko poznat po usvajanju ne tradicionalne, 
minimalne sintakse, bazirane na  white space, i dizajnu koju tezi cistom i 
citljivom kodu.

### Verzije Python-a
Prije samo par mjeseci (pisano Mar. 2020), ako biste htjeli instalirati Python na vasem racunaru, dosli biste u konfuznu situaciju, jer Python, za razliku
od mnogih drugih programskih jezika, ima dvije glavne (major), ne kompatibilne verzije koje su podjednako u sirokoj upotrebi

Python verzije 2.7.3, released u 2012, je zadnja verzija popularnog Python-a 2 koji je released. Ova verzija je uglavnom u potpunosti kompatibilna unazad sa svim prethodnim verzijama.

Godine 2008, kreator, Guido van Rossum odlucio je da ocisti Python bazu 
(codebase) i rekonstruise dosta drugih stvari u Python 2 koje mu se nisu 
svidjale, s toga je kreirao Python 3.

Python 3 je prihvatan ali veoma oprezno i polako na pocetku, najvise iz 
razloga sto nije kompatibilan unazad sa prethodnom verzijom Python 2, i zato 
je postojao ogroman eko-sistem biblioteka napisanih za Python 2 koje nece 
raditi sa novom verzijom Python-a 3.

Ovih dana Python 3 eco-sistem je uveliko pohvatao i izjednacio se sa 
prethodnom verzijom, sto nas dovodi do zakljucka da je Python 3 logicni izbor 
za sve nove developere koji planiraju uciti ovaj programski jezik. Python 3 je 
verzija koju cemo ujedno obraditi u ovom kursu.

<div style="page-break-after: always;"></div>

### Karakteristike Python-a

#### Jednostavnost
Jednostavnost citanja i pisanja koda u Python-u, ponekad se granici sa citanjem
nekog teksta napisanog na standardnom jeziku koji koristimo u svakodnevnoj 
komunikaciji. Ovo donosi ogromnu prednost Python programskom jeziku u odnosu na
druge.

#### Lak za ucenje
Kroz samo para dana i vec mozete kreirati programe, a u nekoliko sati rada sa 
Python-om vec cete se osjecati kao da upravljate avionom. 

#### Besplatan i otvorenog koda (Free and Open Source)
Kada je u pitanju razvoj programskog jezika Python, od velikog je znacaja ova 
osobina, sto cini njegov kod u potpunosti otvorenim za daljnje distribuiranje, 
kao i specificne dijelove koda, ali omogucava programerima iz cijelog svijeta 
da rade na daljnjem razvoju ovog programskog jezika.

#### Jezik visokog nivoa (High-level)
Prilikom pisanje koda u Python-u mozete se u potpunosti posvetiti rjesavanju 
problema, bez da vam paznju odvlace stvari kao sto su upravljanje memorijom,
striktno definisanje tipova promjenjivih ...

#### Prenosivost / Portabilnost
Python kod je portovan (prilagodjen da bi radio na drugim platformama), sto mu
omogucava izvrsavanje na bilo kojoj drugoj platformi, bez dodatnih intervencija
nad izvornim kodom. Ovo znaci da ste u potpunosti ne zavisni od operativnog 
sistema ili tipa arhitekture na kojoj radite. Python kod ce se izvrsavati isto 
kako na Windows-u, tako i na Linux, FreeBSD, Macintosh-u, Solaris-u, OS/2, Amigi ali i PlayStation-u, PalmOS-u, cak i na PocketPC-u! Postoje platforme 
poput Kivy-ja, koje vam omogucavaju kreiranje igrica za iOS ili Android.

#### Interpreter
Mnogi drugi programski jezici, poput C, C++ ili Jave zahtijevaju kompajliranje
koda, sto znaci prevodjenje/konvertovanje koda sa **Izvornog koda** (Source 
Code) u binarni jezik (jezik nula i jedinica), razumljiv jedino kompjuteru. 
Prilikom pokretanja kompajlera, linker software-e kopira program sa vaseg diska
u radnu memoriju kompjutera i tada ga pokrace.
Python-u nije potreban kompajler/prevodilac iz izvornog koda u binarni, on se u
potpunosti oslanja na interpreter, sto znaci da se program pokrece direktno iz
**Izvornog koda**, naravno u pozadini Python pretvara izvorni kode u neki medju
kod, koji se jos nazive bajtkode (bytecode), a zatim prevodi bajtkode u jezik
koji kompjuter razumije. Iako ovo zvuci duze i komplikovanije od kompajliranja
sve se desava u realnom vremenu, tako da nema potrebe za vas kao programera
da brinete da li je program kompajliran i uredno povezan (linkovan) sa 
potrebnim bibliotekama, kao ni da li su sve biblioteke ucitane ili ne.

#### Objektno orijentisan
Pored proceduralno-orijentisanog (niz procedura ili funkcija koje se mogu 
upotrebljavati vise puta za rjesenje problema), Python u potpunosti podrzava 
objektno-orijentisani nacin programiranja. Prilikom objektno-orijentisanog 
nacina programiranja, koristeci objekte i funkcije, Python uveliko uproscava
i pojednostavljuje pristup objektno-orijentisanom nacinu programiranja, u 
poredjenju sa velikanima kao sto su C++ ili Java.

#### Prosiriv
U slucaju da trebate sakriti neki dio koda (kompajlirati da sprijecite 
mogucnost citanja Izvornog koda) ili jednostavno zelite da se brze 
izvrsava (pisanje u C ili C++), mozete jednostavno taj dio kodirati u drugom
programskom jeziku i pozvati ga direktno iz Python-a. 

Veoma vazno je naglasiti prosirive biblioteke Python-a. Standardne biblioteke
Python-a su ogromne. Mogucnosti su nevjerovatne, koriscenjem samo standardnih
biblioteka mozete upravljati bazama podataka, serverima, raznim vrstama 
datoteka, grafickim okruzenjem ... Pored standardnih postoje druge biblioteke
koje mozete koristiti unutar vaseg koda a mozete ih pronaci na oficijelnoj 
stranici https://pypi.org. 

Nakon nekog vremena programiranja u Python-u shvaticete da je vecinu stvari
neko vec napisao i sto je najbolje vi nemate potrebu da izmisljate toplu vodu
mozete ove vec napisane dijelove koda jednostavno integrisati u svoj program
i koristiti.

#### Ugradiv u druge programe
Python moze biti ugradjen u jezike poput C i C++ kako bi obezbijedili mogucnost
skriptovanja.
