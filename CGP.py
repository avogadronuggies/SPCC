def simulate_code_generation(statements):
    reg_desc = {'R0': '', 'R1': ''}
    addr_desc = {}
    output = []

    for stmt in statements:
        lhs, expr = map(str.strip, stmt.split('='))
        code = []

        parts = expr.split()
        reg = 'R0' if not reg_desc['R0'] else 'R1'

        if len(parts) == 3 and parts[1] in '+-':
            op1, op, op2 = parts
            code.append(f"MOV {op1}, {reg}")
            code.append(f"{'ADD' if op == '+' else 'SUB'} {op2}, {reg}")
        else:
            code.append(f"MOV {expr}, {reg}")

        reg_desc[reg] = lhs
        addr_desc[lhs] = f"{lhs} in {reg}"

        if lhs in ['d', 'result']:
            code.append(f"MOV {reg}, {lhs}")
            addr_desc[lhs] = f"{lhs} in {reg} and memory"

        reg_str = ', '.join([f"{r} contains {v}" if v else f"{r} empty" for r, v in reg_desc.items()])
        addr_str = ', '.join([f"{v} in {reg.split()[-1]}" for v, reg in addr_desc.items()])
        output.append((stmt, code, reg_str, addr_str))

    return output

def display_table(table):
    print(f"{'Statements':<15} | {'Code Generated':<30} | {'Register Descriptor':<40} | {'Address Descriptor'}")
    print("-" * 120)
    for stmt, code, reg_str, addr_str in table:
        code_str = '\n                  '.join(code)
        print(f"{stmt:<15} | {code_str:<30}                      | {reg_str:<40} | {addr_str}")

def main():
    print("Enter the 3-address code statements line by line. Type 'end' to finish:\n")
    stmts = []
    while (line := input()) != 'end':
        stmts.append(line)

    result = simulate_code_generation(stmts)
    print("\n--- Code Generation Output ---\n")
    display_table(result)

if __name__ == "__main__":
    main()
