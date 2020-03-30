
##### Rad sa stringovima
      - tekst, rad sa tekstom, funkcije nad stringovima

      rad_sa_stringovima.py
      
```python
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
```
