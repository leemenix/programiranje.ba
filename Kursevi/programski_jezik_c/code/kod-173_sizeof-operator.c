#include <stdio.h>
#include <string.h>
char nazivKaraktera[] = "Goku";
char nazivPlanete[8] = "Zemlja";
int  godineKaraktera = 14;
float tezinaKaraktera = 44.34;

int main(){
    printf("Velicina promjenjive nazivKaraktera u memoriji %ld \n", 
        sizeof(nazivKaraktera));
    printf("Velicina promjenjive nazivPlanete u memoriji %ld \n", 
        sizeof(nazivPlanete));
    printf("Velicina promjenjive godineKaraktera u memoriji %ld \n",
        sizeof(godineKaraktera));
    printf("Velicina promjenjive tezinaKaraktera u memoriji %ld \n",
        sizeof(tezinaKaraktera));
    printf("Duzina promjenjive nazivKaraktera %ld \n", strlen(nazivPlanete));

    return 0;
}
