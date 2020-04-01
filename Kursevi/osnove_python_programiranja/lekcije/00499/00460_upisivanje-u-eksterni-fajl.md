
### upisivanje u eksterni fajl

**`Izvorni kod: kod-457_rad-sa-fajlovima.py`**

```python
# dodavanje na vec postojeci fajl
karakteri_fajl = open("fajl-455_karakteri_porijeklo.txt", "a")

karakteri_fajl.write("Bulma - Zemlja")
karakteri_fajl.write("\n Chi-Chi - Zemlja")

karakteri_fajl.close()

# upisivanje u novi fajl
karakteri_fajl = open("fajl-458_karakteri_porijeklo.txt", "w")

karakteri_fajl.write("Bulma - Zemlja")
karakteri_fajl.write("\n Chi-Chi - Zemlja")

karakteri_fajl.close()
```
