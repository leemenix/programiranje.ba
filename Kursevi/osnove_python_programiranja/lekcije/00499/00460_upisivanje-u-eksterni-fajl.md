
## upisivanje u eksterni fajl
```python
karakteri_fajl = open("karakteri_porijeklo.txt", "a")

karakteri_fajl.write("Bulma - Zemlja")
karakteri_fajl.write("\n Chi-Chi - Zemlja")

karakteri_fajl.close()

### upisivanje u eksterni fajl

karakteri_fajl = open("karakteri_porijeklo_novi.txt", "w")

karakteri_fajl.write("Bulma - Zemlja")
karakteri_fajl.write("\n Chi-Chi - Zemlja")

karakteri_fajl.close()
```
