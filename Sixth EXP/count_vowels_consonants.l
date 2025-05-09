%option noyywrap
%{
#include <stdio.h>
int vowels = 0, consonants = 0;
%}
%%
[aeiouAEIOU] { vowels++; }
[a-zA-Z]     { consonants++; }
.            { /* Ignore other characters */ }
%%
int main() {
    printf("Enter text: ");
    yylex();
    printf("Vowels: %d\n", vowels);
    printf("Consonants: %d\n", consonants);
    return 0;
}
