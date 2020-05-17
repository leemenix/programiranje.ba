#include <stdio.h>

int main(){
    
    int godine = 20;
    float tezina = 54.4;

    printf("Godine prije kastovanja %d \n", godine);
    printf("Tezina prije kastovanja %.1f \n", tezina);
    printf("Godine nakon kastovanja %.1f, tezina nakon kastovanja %d \n", 
        (float)godine, (int)tezina);
    printf("Godine + tezina = %d ", godine + (int)tezina);


    return 0;
}
