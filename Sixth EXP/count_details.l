%option noyywrap
%{
#include <stdio.h>
int chars = 0, words = 0, sentences = 0, lines = 0, tabs = 0, numbers = 0, spaces = 0;
%}
%%
\n      { lines++; chars++; }
\t      { tabs++; chars++; }
[0-9]+  { numbers++; chars += yyleng; }
[ ]     { spaces++; chars++; }
[.!?]   { sentences++; chars++; }
[^\s]   { chars++; words++; }
.       { chars++; }
%%
int main() {
    printf("Enter text: ");
    yylex();
    printf("Characters: %d\nWords: %d\nSentences: %d\nLines: %d\nTabs: %d\nNumbers: %d\nSpaces: %d\n", chars, words, sentences, lines, tabs, numbers, spaces);
    return 0;
}
