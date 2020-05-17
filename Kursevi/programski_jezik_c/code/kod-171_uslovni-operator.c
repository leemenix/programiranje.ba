#include <stdio.h>

int main(){
    int godine;
    char slovo;
    printf("Unesite broj godina: \n");
    scanf(" %d", &godine);

    slovo = (godine > 2) ? 'e' : 'u';

    printf("Imate %d godin%c\n", godine, slovo);

    return 0;
}
