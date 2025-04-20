# SPCC Experiment 8: 3AC, Quadruples, and Triples (No Optimization)

precedence = {'+': 1, '-': 1, '*': 2, '/': 2, 'uminus': 3}
temp_counter, three_ac = 1, []

def get_temp():
    global temp_counter
    temp = f"t{temp_counter}"
    temp_counter += 1
    return temp

def tokenize(expr):
    tokens, i = [], 0
    while i < len(expr):
        if expr[i].isspace(): i += 1
        elif expr[i] in '+-*/=()':
            tokens.append('uminus' if expr[i] == '-' and (i == 0 or expr[i-1] in '+-*/=( ') else expr[i])
            i += 1
        elif expr[i].isalnum():
            var = ''
            while i < len(expr) and expr[i].isalnum(): var += expr[i]; i += 1
            tokens.append(var)
        else: i += 1
    return tokens

def infix_to_postfix(tokens):
    output, stack = [], []
    for token in tokens:
        if token not in precedence and token not in '()': output.append(token)
        elif token == '(': stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(': output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence[token] <= precedence[stack[-1]]: output.append(stack.pop())
            stack.append(token)
    return output + stack[::-1]

def generate_3ac_from_postfix(postfix):
    stack = []
    for token in postfix:
        if token == 'uminus':
            temp = get_temp(); three_ac.append((temp, 'minus', stack.pop(), '')); stack.append(temp)
        elif token in precedence:
            op2, op1 = stack.pop(), stack.pop()
            temp = get_temp(); three_ac.append((temp, op1, token, op2)); stack.append(temp)
        else: stack.append(token)
    return stack.pop()

def generate_quadruples():
    return [('minus', instr[2], '', instr[0]) if instr[1] == 'minus' else (instr[2], instr[1], instr[3], instr[0]) for instr in three_ac]

def generate_triples():
    result_map, triples = {}, []
    for i, instr in enumerate(three_ac):
        if instr[1] == 'minus': triples.append(('minus', instr[2], ''))
        elif instr[2] == '=': triples.append(('=', instr[0], f"({result_map[instr[1]]})"))
        else:
            op1 = f"({result_map[instr[1]]})" if instr[1] in result_map else instr[1]
            op2 = f"({result_map[instr[3]]})" if instr[3] in result_map else instr[3]
            triples.append((instr[2], op1, op2))
        result_map[instr[0]] = i
    return triples

def main():
    global temp_counter, three_ac
    expr = input("Enter a statement (e.g. a = b * -c + b * -c): ").strip()
    temp_counter, three_ac = 1, []

    if '=' in expr:
        lhs, rhs = map(str.strip, expr.split('='))
        result = generate_3ac_from_postfix(infix_to_postfix(tokenize(rhs)))
        three_ac.append((lhs, result, '=', ''))
    else:
        generate_3ac_from_postfix(infix_to_postfix(tokenize(expr)))

    print("\n--- Three Address Code ---")
    for instr in three_ac:
        print(f"{instr[0]} = {'minus ' + instr[2] if instr[1] == 'minus' else f'{instr[1]} {instr[2]} {instr[3]}' if instr[2] != '=' else instr[1]}")

    print("\n--- Quadruples ---")
    for i, quad in enumerate(generate_quadruples()):
        print(f"{i}: ({quad[0]:^7}, {quad[1]:^5}, {quad[2]:^5}, {quad[3]:^5})")

    print("\n--- Triples ---")
    for i, triple in enumerate(generate_triples()):
        print(f"{i}: ({triple[0]:^7}, {triple[1]:^5}, {triple[2]:^5})")

if __name__ == "__main__":
    main()
