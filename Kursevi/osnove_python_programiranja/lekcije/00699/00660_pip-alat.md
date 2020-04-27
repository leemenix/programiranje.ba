
<div style="page-break-after: always;"></div>

### Instalacija dodatnih modula **alat pip** - (package installer for Python)
U slucaju kada zelimo instalirati dodatne pakete za rad sa Python-om, koristimo pip alat ili Package Installer for Python. Za razliku od modula, Python paketi su zapakovati programi, koji se odrzajava od strane Python zajednice, potpuno slobodni i spremni za upotrebu. 
Naravno prije same upotrebe je potrebno da se upoznate sa mogucnostima koje sam paket nudi. 
Kada se paket instalira sa pip alatom, on se u sustini raspakuje na vasu masinu u posebno definisan direktoriji, odakle mozemo da pozovemo sve njegove module.

Ja cu vam u sledecem primjeru demonstrirati kako mozemo jako jednostavno napraviti program sa grafikim interface-om u Python-u pomocu paketa **PySimpleGUI**.

```text
pip install pysimplegui (kao Administrator)
```

**`Izvorni kod: kod-660_grafika-demo.py`**
```python
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
```