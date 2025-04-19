%option noyywrap
%{
#include <stdio.h>
int tokens = 0;
%}
%%
[^\s]+ { tokens++; }
.      { /* Ignore other characters */ }
%%
int main() {
    printf("Enter text: ");
    yylex();
    printf("Tokens: %d\n", tokens);
    return 0;
}
