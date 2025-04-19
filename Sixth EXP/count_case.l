%option noyywrap
%{
#include <stdio.h>
int upper = 0, lower = 0;
%}
%%
[A-Z] { upper++; }
[a-z] { lower++; }
.     { /* Ignore other characters */ }
%%
int main() {
    printf("Enter text: ");
    yylex();
    printf("Uppercase letters: %d\n", upper);
    printf("Lowercase letters: %d\n", lower);
    return 0;
}
