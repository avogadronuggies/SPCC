import re
from collections import Counter, defaultdict

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
    categories = [classify_token(token) for token in tokens]
    lexeme_dict = defaultdict(set)
    for token, category in zip(tokens, categories):
        lexeme_dict[category].add(token)
    return lexeme_dict, Counter(categories)

def print_lexeme_table(lexeme_dict, count_dict):
    print(f"{'Lexeme':<30} {'Tokens':<50} {'Count':<10}")
    print("_" * 90)
    for category, tokens in lexeme_dict.items():
        print(f"{category:<30} {', '.join(sorted(tokens)):<50} {count_dict[category]:<10}")

sample_code = """
int main() {
    if (a > b)
        a = 5;
    else
        b = 5;
}
"""
lexeme_dict, count_dict = lexical_analyzer(sample_code)
print_lexeme_table(lexeme_dict, count_dict)


