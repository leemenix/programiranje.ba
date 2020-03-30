
#### Rijecnik - Dictionaries - {}
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
