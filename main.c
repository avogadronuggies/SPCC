#include <stdio.h>
#include "conversion.h"

int main()
{
    char binStr[32], hexStr[10];
    int dec;

    // Binary to Decimal
    printf("Enter binary number: ");
    scanf("%s", binStr);
    BIN_TO_DEC(binStr, dec);
    printf("Decimal: %d\n", dec);

    // Decimal to Binary
    printf("Enter decimal number: ");
    scanf("%d", &dec);
    DEC_TO_BIN(dec, binStr);
    printf("Binary: %s\n", binStr);

    // Binary to Hexadecimal
    printf("Enter binary number: ");
    scanf("%s", binStr);
    BIN_TO_HEX(binStr, hexStr);
    printf("Hexadecimal: %s\n", hexStr);

    // Hexadecimal to Binary
    printf("Enter hexadecimal number: ");
    scanf("%s", hexStr);
    HEX_TO_BIN(hexStr, binStr);
    printf("Binary: %s\n", binStr);

    return 0;
}
