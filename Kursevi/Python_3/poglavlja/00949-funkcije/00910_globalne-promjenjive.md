
<a name="lokalne-promjenjive"/>

### Lokalne promjenjive

Ako zelimo definisati promjenjive unutar funkcije, ali da i dalje budu globalno
dostupne, potrebno je da kazemo Python-u da promjenjiva nije lokalnog tipa vec
globalna.

Ovo se postize koristenjem _global_ statementa (TBD), ispred promjenjive ...
Iako je ovo moguce, generalno se ne preporucuje definisanje globalnih
promjenjivih unutar funkcije jer dovodi do zbunjivanja i tezeg citanja i
razumijevanja koda.
