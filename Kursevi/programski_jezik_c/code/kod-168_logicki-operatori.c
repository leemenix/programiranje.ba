#include <stdio.h>
#include <stdbool.h>

int main() {
    int brojUtakmica;
    int brojFudbalera;
    int maxBrojUtakmica = 4;
    int brojLopti;
    bool prijateljskaUtakmica = true;

    printf("Unesite broj odigranih utakmica? \n");
    scanf(" %d", &brojUtakmica);
    printf("Unesite broj fudbalera? \n");
    scanf(" %d", &brojFudbalera);
    printf("Unesite broj lopti? \n");
    scanf(" %d", &brojLopti);
    if ((brojUtakmica < maxBrojUtakmica) && (brojFudbalera >= 11)) {
        if (maxBrojUtakmica - brojUtakmica == 1){
            printf("Imate pravo odigrati jos %d utakmicu\n", maxBrojUtakmica - brojUtakmica);
        }
        else{
            printf("Imate pravo odigrati jos %d utakmice. \n", maxBrojUtakmica - brojUtakmica);
        }
    }
    else{
        printf("Odigrali ste maksimalan broj utakmica \n");
        printf("ili nemate dovoljno igraca. Minimalan broj je 11. \n");
	return 0;
    }

    brojLopti--;
    printf("Broj lopti %d\n", brojLopti);
    printf("Prijateljska utakmica %d \n", prijateljskaUtakmica);
    if (!(prijateljskaUtakmica) || (brojLopti <= 2)){
        printf("Moracete igrati na boljem terenu. \n");
    }
    else{
        printf("Utakmica moze da pocne. \n");
    }

    return 0;
}
