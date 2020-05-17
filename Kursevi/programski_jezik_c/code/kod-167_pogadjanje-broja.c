#include <stdio.h>
#define TAJNIBROJ 4

int brojPokusaj;

int main(){
    printf("Pokusajte pogoditi tajni broj? [0 - 10] \n");
    scanf(" %d", &brojPokusaj);

    if (brojPokusaj == TAJNIBROJ){
        printf("Cestitamo pogodili ste. Tajni broj %d \n", TAJNIBROJ);
    }
    else if (brojPokusaj < TAJNIBROJ){
        printf("Tajni broj je veci od unesenog. Molimo pokusajte ponovo. \n");
    }
    else{
        printf("Tajni broj je manji od unesenog. Molimo pokusajte ponovo. \n");
    }

    return 0;
}
