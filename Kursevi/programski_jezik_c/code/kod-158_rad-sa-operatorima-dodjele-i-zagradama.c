#include<stdio.h>

int main(){

    int bodovi1, bodovi2, bodovi3, bodovi4, rekordanBrojBodova;
    float prosjekBodova, razlikaOdNajboljegProsjeka, procentualnaRazlika;
    
    rekordanBrojBodova = 95;
    bodovi1 = bodovi3 = 80;
    bodovi2 = 75;
    
    printf("Koliko bodova ste dobili na cetvrtom testu? [0 - 100] ");
    scanf(" %d", &bodovi4);
    
    prosjekBodova = (bodovi1 + bodovi2 + bodovi3 + bodovi4) / 4;
    
    printf ("Prosjek bodova %.1f. \n", prosjekBodova);

    razlikaOdNajboljegProsjeka = rekordanBrojBodova - prosjekBodova;
    procentualnaRazlika = 100 * (razlikaOdNajboljegProsjeka / rekordanBrojBodova);

    printf("Vas broj bodova je za %.1f bodova ", razlikaOdNajboljegProsjeka);
    printf("manji od rekordnog broja bodova (%d).\n", rekordanBrojBodova);
    printf("Razlika izrazena u proncentima iznosi %.1f %%", procentualnaRazlika);
    printf("od rekordnog broja bodova. \n");

    return 0; 

}
