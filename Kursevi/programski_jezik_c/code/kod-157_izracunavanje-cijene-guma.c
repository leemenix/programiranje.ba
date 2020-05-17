#include<stdio.h>
#define POPUST .10

int main(){
    int brojGuma;
    float cijenaGume, cijenaSaPopustom, ukupnaCijena;

    printf("Koliko guma planirate kupiti? ");
    scanf(" %d", &brojGuma);
    printf("Kolika je cijena jedne gume (molim unesite cijenu u formatu xx.xx)? ");
    scanf(" %f", &cijenaGume);
    ukupnaCijena = brojGuma * cijenaGume;
    cijenaSaPopustom = ukupnaCijena - (ukupnaCijena * POPUST);

    printf("Ukupna cijena guma bez popusta %.2f \n", ukupnaCijena);
    printf("Cijena guma sa popustom %.2f ", cijenaSaPopustom);

    return 0;
}
