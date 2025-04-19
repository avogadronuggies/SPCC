%option noyywrap
%{
#include <stdio.h>
int conjunctions = 0;
%}
%%
(and|but|or|so|yet|for|nor) { conjunctions++; }
.                           { /* Ignore other characters */ }
%%
int main() {
    printf("Enter a sentence: ");
    yylex();
    if (conjunctions > 0)
        printf("The sentence is Compound.\n");
    else
        printf("The sentence is Simple.\n");
    return 0;
}
