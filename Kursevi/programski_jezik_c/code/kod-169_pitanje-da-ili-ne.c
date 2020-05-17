#include <stdio.h>
char pitanje;
int main(){
    printf("Da li zelite postaviti pitanje? [Yy/Nn] \n");
    scanf(" %c", &pitanje);

    if (pitanje == 'Y' || pitanje == 'y'){
        printf("Postavite pitanje.\n");
    }
    else if (pitanje == 'N' || pitanje == 'n'){
        printf("Hvala sto ste ucestvovali\n");
    }
    else{
        printf("Niste izabrali pravi karakter.\n");
    }

    return 0;
}
