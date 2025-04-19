import re
from collections import defaultdict

KEYWORDS = {"int", "float", "if", "else", "while", "return", "void", "main"}
OPERATORS = {"+", "-", "*", "/", "=", "==", "!=", "<", ">", "<=", ">="}
PUNCTUATIONS = {";", ",", "(", ")", "{", "}"}

def classify_token(token):
    if token in KEYWORDS: return "Keyword [K]"
    if token in OPERATORS: return "Operator [O]"
    if token in PUNCTUATIONS: return "Punctuation [P]"
    if token.isdigit(): return "Literal [L]"
    if re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', token): return "Identifier [I]"
    return "Unknown"

def lexical_analyzer(code):
    tokens = re.findall(r'[a-zA-Z_][a-zA-Z0-9_]*|\d+|[+\-*/=<>!]=?|[;{},()\[\]]', code)
    lexeme_dict = defaultdict(set)
    for token in tokens:
        lexeme_dict[classify_token(token)].add(token)
    return lexeme_dict

def print_lexeme_table(lexeme_dict):
    print(f"{'Lexeme':<20} {'Tokens':<50}")
    print("_" * 70)
    for category, tokens in lexeme_dict.items():
        print(f"{category:<20} {', '.join(sorted(tokens)):<50}")

sample_code = """
int main() {
    if (a > b) a = 5; else b = 5;
}
"""
print_lexeme_table(lexical_analyzer(sample_code))


