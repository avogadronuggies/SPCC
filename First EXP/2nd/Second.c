#include <conio.h>
#include <stdio.h>
#include "Area.h"

int main() {
    int ch;
    double side, length, width, base, height, radius;
    do {
        printf("Enter your choice:\n");
        printf("1. Area of Square\n");
        printf("2. Area of Rectangle\n");
        printf("3. Area of Triangle\n");
        printf("4. Area of Circle\n");
        printf("5. Exit\n");
        printf("Choice: ");
        scanf("%d", &ch);
        switch (ch) {
            case 1:
                printf("Enter the side of the square: ");
                scanf("%lf", &side);
                printf("Area of Square: %.2f\n", AREA_SQUARE(side));
                break;
            case 2:
                printf("Enter the length and width of the rectangle: ");
                scanf("%lf %lf", &length, &width);
                printf("Area of Rectangle: %.2f\n", AREA_RECTANGLE(length, width));
                break;
            case 3:
                printf("Enter the base and height of the triangle: ");
                scanf("%lf %lf", &base, &height);
                printf("Area of Triangle: %.2f\n", AREA_TRIANGLE(base, height));
                break;
            case 4:
                printf("Enter the radius of the circle: ");
                scanf("%lf", &radius);
                printf("Area of Circle: %.2f\n", AREA_CIRCLE(radius));
                break;
            case 5:
                printf("Exiting the program.\n");
                break;
            default:
                printf("Invalid choice!\n");
        }
    } while (ch != 5);
    getch();
    return 0;
}