// 16진수 구구단?

#include <stdio.h>
int main(void)  {
    char c;
    int a;
    scanf("%X", &a);
    for(int i=1; i<=15; i++) {
        printf("%X*%X=%X\n", a,i, a*i);
    }

    return 0;
}