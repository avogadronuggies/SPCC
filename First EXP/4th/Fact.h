#ifndef FACT_H
#define FACT_H

#define FACT(x) \
{ \
    int result = 1; \
    for (int i = 1; i <= x; i++) \
    { \
        result *= i; \
    } \
    printf("Factorial of %d is %d\n", x, result); \
}

#endif