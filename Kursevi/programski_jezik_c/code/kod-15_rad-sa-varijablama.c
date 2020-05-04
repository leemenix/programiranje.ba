/* program koji izracunava potrepstine za 
   za polazak u prvi razred osnovne skole*/
#include <stdio.h>

int main(){
	// definisanje varijabli
	char prvoSlovoImena, prvoSlovoPrezimena; 
	int broj_olovki;
	int broj_sveski;
	// definisanje varijabli sa dodjelom vrijednosti
	float cijena_olovke = 0.50;
	float cijena_sveske = 1.68;
	float cijena_obroka = 2.50;

	// informacije o prvom uceniku
	prvoSlovoImena = 'G';
	prvoSlovoPrezimena = 'C';
	broj_olovki = 4;
	broj_sveski = 5;

	printf("%c.%c. treba %d olovki, %d sveski i jedan obrok dnevno.\n",
		    prvoSlovoImena, prvoSlovoPrezimena, broj_olovki, broj_sveski);
	printf("Ukupna cijena potrepstina za ucenika %c%c je %.2fKM\n\n",
		    prvoSlovoImena,prvoSlovoPrezimena,broj_olovki * cijena_olovke
		    + broj_sveski * cijena_sveske + cijena_obroka);

    // informacije o drugom uceniku
	prvoSlovoImena = 'B';
	prvoSlovoPrezimena = 'V';
	broj_olovki = 3;
	broj_sveski = 2;

	printf("%c.%c. treba %d olovki, %d sveski i jedan obrok dnevno.\n",
		    prvoSlovoImena, prvoSlovoPrezimena, broj_olovki, broj_sveski);
	printf("Ukupna cijena potrepstina za ucenika %c%c je %.2fKM\n\n",
		    prvoSlovoImena,prvoSlovoPrezimena,broj_olovki * cijena_olovke
		    + broj_sveski * cijena_sveske + cijena_obroka);

	// informacije o trecem uceniku
	prvoSlovoImena = 'P';
	prvoSlovoPrezimena = 'F';
	broj_olovki = 10;
	broj_sveski = 3;

	printf("%c.%c. treba %d olovki, %d sveski i jedan obrok dnevno.\n",
		    prvoSlovoImena, prvoSlovoPrezimena, broj_olovki, broj_sveski);
	printf("Ukupna cijena potrepstina za ucenika %c%c je %.2fKM\n\n",
		    prvoSlovoImena,prvoSlovoPrezimena,broj_olovki * cijena_olovke
		    + broj_sveski * cijena_sveske + cijena_obroka);

	return 0;

}
