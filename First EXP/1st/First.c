#include <conio.h>
#include <stdio.h>
#include "Calculator.h"

int main() {
    int ch;
    double num1, num2;
    do {
        printf("Enter your choice:\n");
        printf("1. Addition\n");
        printf("2. Subtraction\n");
        printf("3. Multiplication\n");
        printf("4. Division\n");
        printf("5. Power of 2\n");
        printf("6. Square Root\n");
        printf("7. Cube Root\n");
        printf("8. Exit\n");
        printf("Choice: ");
        scanf("%d", &ch);
        switch (ch) {
            case 1:
                printf("Enter two numbers: ");
                scanf("%lf %lf", &num1, &num2);
                printf("Result: %.2f\n", ADD(num1, num2));
                break;
            case 2:
                printf("Enter two numbers: ");
                scanf("%lf %lf", &num1, &num2);
                printf("Result: %.2f\n", SUB(num1, num2));
                break;
            case 3:
                printf("Enter two numbers: ");
                scanf("%lf %lf", &num1, &num2);
                printf("Result: %.2f\n", MUL(num1, num2));
                break;
            case 4:
                printf("Enter two numbers: ");
                scanf("%lf %lf", &num1, &num2);
                if (num2 != 0)
                    printf("Result: %.2f\n", DIV(num1, num2));
                else
                    printf("Error: Division by zero!\n");
                break;
            case 5:
                printf("Enter a number: ");
                scanf("%lf", &num1);
                printf("Result: %.2f\n", POWER_OF_2(num1));
                break;
            case 6:
                printf("Enter a number: ");
                scanf("%lf", &num1);
                if (num1 >= 0)
                    printf("Result: %.2f\n", SQUARE_ROOT(num1));
                else
                    printf("Error: Cannot compute square root of a negative number!\n");
                break;
            case 7:
                printf("Enter a number: ");
                scanf("%lf", &num1);
                printf("Result: %.2f\n", CUBE_ROOT(num1));
                break;
            case 8:
                printf("Exiting the program.\n");
                break;
            default:
                printf("Invalid choice!\n");
        }
    } while (ch != 8);
    getch();
    return 0;
}