#include<stdio.h>
#include<conio.h>
void main()
{
    int n,i,f;
    f=i=1;
    clrscr();
    printf("Enter a Number to Find Factorial: ");
    scanf("%d",&n);
    while(i<=n)
    {
        f*=i;
        i++;
    }
    printf("The Factorial of %d is : %d",n,f);
    getch();
}
