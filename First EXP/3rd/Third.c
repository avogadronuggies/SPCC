#include <conio.h>
#include <stdio.h>
#include <math.h>
#include "Convert.h"

int main() {
    int ch;
    double value;

    do {
        printf("Enter your choice:\n");
        printf("1. Celsius to Fahrenheit\n");
        printf("2. Fahrenheit to Celsius\n");
        printf("3. Metres to Feet\n");
        printf("4. Feet to Metres\n");
        printf("5. Litres to Cubic Feet\n");
        printf("6. Cubic Feet to Litres\n");
        printf("7. Exit\n");
        printf("Choice: ");
        scanf("%d", &ch);

        switch (ch) {
            case 1:
                printf("Enter temperature in Celsius: ");
                scanf("%lf", &value);
                printf("Celsius to Fahrenheit: %.2f\n", C_TO_F(value));
                break;
            case 2:
                printf("Enter temperature in Fahrenheit: ");
                scanf("%lf", &value);
                printf("Fahrenheit to Celsius: %.2f\n", F_TO_C(value));
                break;
            case 3:
                printf("Enter length in metres: ");
                scanf("%lf", &value);
                printf("Metres to Feet: %.2f\n", METRE_TO_FEET(value));
                break;
            case 4:
                printf("Enter length in feet: ");
                scanf("%lf", &value);
                printf("Feet to Metres: %.2f\n", FEET_TO_METRE(value));
                break;
            case 5:
                printf("Enter volume in litres: ");
                scanf("%lf", &value);
                printf("Litres to Cubic Feet: %.2f\n", LITRE_TO_CUBIC_FEET(value));
                break;
            case 6:
                printf("Enter volume in cubic feet: ");
                scanf("%lf", &value);
                printf("Cubic Feet to Litres: %.2f\n", CUBIC_FEET_TO_LITRE(value));
                break;
            case 7:
                printf("Exiting the program.\n");
                break;
            default:
                printf("Invalid choice!\n");
        }
    } while (ch != 7);

    getch();
    return 0;
}