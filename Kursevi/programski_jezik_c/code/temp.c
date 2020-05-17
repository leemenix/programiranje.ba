#include <stdio.h>
#include <stdbool.h>

int main() {
	int a = 2;
	int b = 1;
        printf("%d %d %d %d \n", (a<b), (a>b), !(a<b), !(a>b));
	if (!(a < b)){
		printf("A nije manje od B");
	}
	else{
		printf("A je manje od B");
	}
	return 0;
}
