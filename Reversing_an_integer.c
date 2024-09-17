#include <stdio.h>

int main(void)
{
    int number;
    printf("Enter the number: ");
    scanf("%d", &number);

    int arr[10];
    int i;
    int digits = 0;

    for (i = 0; number > 0; i++)
    {
        arr[i] = number % 10;
        number = number / 10;
        digits++;
    }

    printf("Reversed digits:\n");
    for (i = 0; i < digits; i++)
    {
        printf("%d", arr[i]);
    }

    printf("\n");
    return 0;
}
