// 정수 1개 입력받아 카운트다운 출력하기

#include <stdio.h>
int main(void)  {
    int n;
    scanf("%d", &n);
    for(int i=n; i>0; i--) {
        printf("%d\n", i);
    }

    return 0;
}


