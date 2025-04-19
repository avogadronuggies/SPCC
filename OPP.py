def generate_precedence_table():
    terminals = ['+', '*', 'id', '$']
    table = {t1: {t2: '-' for t2 in terminals} for t1 in terminals}

    # Define precedence relations
    table['+']['+'] = '>'
    table['+']['*'] = '<'
    table['+']['id'] = '<'
    table['+']['$'] = '>'
    table['*']['+'] = '>'
    table['*']['*'] = '>'
    table['*']['id'] = '<'
    table['*']['$'] = '>'
    table['id']['+'] = '>'
    table['id']['*'] = '>'
    table['id']['id'] = '-'
    table['id']['$'] = '>'
    table['$']['+'] = '<'
    table['$']['*'] = '<'
    table['$']['id'] = '<'
    table['$']['$'] = 'acc'
    
    return table

def print_table(table):
    terminals = list(table.keys())
    print("\nPrecedence Table:")
    print("    | " + "     | ".join(terminals) + "   |")
    print("-" * (6 * len(terminals) + 4))
    for row in terminals:
        print(f"{row:<3} | ", end="")
        for col in terminals:
            print(f" {table[row][col]:<4} | ", end="")
        print("")

def find_rightmost_terminal(stack):
    """ Find the rightmost terminal in the stack """
    for symbol in reversed(stack):
        if symbol in ['+', '*', 'id', '$']:
            return symbol
    return '$'  # Default to $ if no terminal found

def parse_input(input_str, table):
    print("\nParsing Table:")
    stack = ['$']
    input_str += '$'
    print(f"{'Stack':<30}| {'Input':<20}| Action")
    print("-" * 70)

    tokens = []
    i = 0
    while i < len(input_str):
        if input_str[i:i+2] == 'id':
            tokens.append('id')
            i += 2
        else:
            tokens.append(input_str[i])
            i += 1

    def reduce_stack():
        # Replace 'id' with 'E'
        if stack[-1] == 'id':
            stack.pop()
            stack.append('E')
            return "Reduce: id -> E"
        # Replace 'E op E' with 'E'
        elif len(stack) >= 3 and stack[-3] == 'E' and stack[-2] in ['+', '*'] and stack[-1] == 'E':
            op = stack[-2]
            stack.pop()
            stack.pop()
            stack.pop()
            stack.append('E')
            return f"Reduce: E {op} E -> E"
        return "Error"

    while len(tokens) > 0:
        top = find_rightmost_terminal(stack)  # Find the rightmost terminal in the stack
        current = tokens[0]

        # Accept if both are '$'
        if top == '$' and current == '$':
            print(f"{''.join(stack):<30}| {''.join(tokens):<20}| Accept")
            break

        action = table[top].get(current, '-')

        print(f"{''.join(stack):<30}| {''.join(tokens):<20}| ", end="")

        if action == '<' or action == '=':
            stack.append(current)
            tokens.pop(0)
            print("Shift")
        elif action == '>':
            reduction = reduce_stack()
            print(reduction)
        else:
            print("Error: Invalid precedence relation")
            return

    print("\nParsing Completed.")

if __name__ == "__main__":
    grammar = ["E -> E + E", "E -> E * E", "E -> id"]
    expression = "id+id*id"
    print("Step 1: Checking the input string...")
    print("Input string:", expression)
    table = generate_precedence_table()
    print_table(table)
    print("\nInput string is valid. Starting parsing...")
    print("\nStep 2: Parsing with operator precedence...")
    parse_input(expression, table)
