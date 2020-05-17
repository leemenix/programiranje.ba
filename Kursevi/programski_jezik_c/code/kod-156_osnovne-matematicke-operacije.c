#include<stdio.h>

int main(){
    
    float x = 14.0;
    float y = 4.0;
    float rezultatRealnih;

    int a = 14;
    int b = 4;
    int rezultatCjelobrojnih;
    
    rezultatRealnih = x / y;
    printf("%.1f podijeljeno sa %.1f jednako je %.1f\n", x,y,rezultatRealnih);
    rezultatCjelobrojnih = a / b;
    printf("%d podijeljeno sa %d jednako je %d \n",a,b,rezultatCjelobrojnih); 
    rezultatRealnih = a / b;
    printf("%d podijeljeno sa %d jednako je %.1f \n", a,b,rezultatRealnih);
    rezultatCjelobrojnih = x % y;
    printf("%f moduo %f je jednako %f \n", x,y,rezultatRealnih);

    return 0;
}
