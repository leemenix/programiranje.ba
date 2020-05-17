#include <stdio.h>
#define TRENUTNA_GODINA 2020    

int main(){
    int godinaRodjenja, godineKaraktera;

    printf("Koje godine ste rodjeni? \n");
    scanf(" %d", &godinaRodjenja);

    godineKaraktera = TRENUTNA_GODINA - godinaRodjenja;

    printf("Trenutno imate %d godina \n", godineKaraktera);

    if ((godinaRodjenja % 4) == 0){
        printf("Rodjeni ste u prestupnoj godini. \n");
    }
    else {
        printf("Niste rodjeni u prestupnoj godini. \n");
    }
    
    return 0;
}
