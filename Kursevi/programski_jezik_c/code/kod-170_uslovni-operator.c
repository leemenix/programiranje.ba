#include <stdio.h>

int main(){
    int a, b;

    printf("Unesite vrijednost a? \n");
    scanf(" %d", &a);
    printf("Unesite vrijednost b? \n");
    scanf(" %d", &b);
    (a < b) ? printf("a je manje od b\n") : printf("a je vece od b\n");


    return 0;
}
