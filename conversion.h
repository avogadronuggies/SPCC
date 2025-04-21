// conversion_lib.h

#ifndef CONVERSION_LIB_H
#define CONVERSION_LIB_H

#include <stdio.h>
#include <math.h>
#include <string.h>

// Macro to convert binary string to decimal
#define BIN_TO_DEC(binStr, result)            \
{                                              \
    result = 0;                                \
    for (int i = 0; binStr[i] != '\0'; i++)    \
        result = result * 2 + (binStr[i] - '0');\
}

// Macro to convert decimal to binary
#define DEC_TO_BIN(dec, binStr)               \
{                                              \
    int i = 0, temp = dec;                     \
    char tempStr[32];                          \
    while (temp > 0) {                         \
        tempStr[i++] = (temp % 2) + '0';       \
        temp /= 2;                             \
    }                                          \
    tempStr[i] = '\0';                         \
    for (int j = 0; j < i; j++)                \
        binStr[j] = tempStr[i - j - 1];        \
    binStr[i] = '\0';                          \
}

// Macro to convert binary to hexadecimal
#define BIN_TO_HEX(binStr, hexStr)                                \
{                                                                 \
    int dec;                                                      \
    BIN_TO_DEC(binStr, dec);                                      \
    sprintf(hexStr, "%X", dec);                                   \
}

// Macro to convert hexadecimal to binary
#define HEX_TO_BIN(hexStr, binStr)                                \
{                                                                 \
    int dec;                                                      \
    sscanf(hexStr, "%x", &dec);                                   \
    DEC_TO_BIN(dec, binStr);                                      \
}

#endif
