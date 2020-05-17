#include <stdio.h>

int main(){
    int broj;

    printf("Unesite broj od 1 do 100\n");
    printf(", a ja cu provjeriti da li je djeljiv sa \n");
    printf("brojevima od 2 do 9 \n");
    scanf(" %d", &broj);
    
    printf("%d %s dijeljiv sa 2.\n", broj, (broj % 2 == 0) ? ("je") : ("nije"));
    printf("%d %s dijeljiv sa 3.\n", broj, (broj % 3 == 0) ? ("je") : ("nije"));
    printf("%d %s dijeljiv sa 4.\n", broj, (broj % 4 == 0) ? ("je") : ("nije"));
    printf("%d %s dijeljiv sa 5.\n", broj, (broj % 5 == 0) ? ("je") : ("nije"));
    printf("%d %s dijeljiv sa 6.\n", broj, (broj % 6 == 0) ? ("je") : ("nije"));
    printf("%d %s dijeljiv sa 7.\n", broj, (broj % 7 == 0) ? ("je") : ("nije"));
    printf("%d %s dijeljiv sa 8.\n", broj, (broj % 8 == 0) ? ("je") : ("nije"));
    printf("%d %s dijeljiv sa 9.\n", broj, (broj % 9 == 0) ? ("je") : ("nije"));

    return 0;
}
