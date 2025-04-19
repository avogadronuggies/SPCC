from tabulate import tabulate
mot = {'STOP': '00', 'ADD': '01', 'SUB': '02', 'MULT': '03', 'MOVER': '04', 'MOVEM': '05', 'COMP': '06', 'BC': '07', 'DIV': '08', 'READ': '09', 'PRINT': '10'}
pot = {'START': '01', 'END': '02', 'ORIGIN': '03', 'LTORG': '04', 'EQU': '05'}
dl = {'DC': '01', 'DS': '02'}
registers = {'AREG': '01', 'BREG': '02', 'CREG': '03', 'DREG': '04'}
address, symbol_table, literal_table, pool_table = '', {}, {}, []

def get_code(table, key): return table.get(key, f"INVALID_{table}")

def allocate_literals(end_value, address):
    output, index = [], 1 if not literal_table else float('inf')
    for key, value in literal_table.items():
        if value == '':
            index = min(index, list(literal_table.keys()).index(key) + 1)
            literal_table[key], key_value = address, key.strip("='")
            output.append(f"{address} (AD,({end_value})) - (C,({key_value}))")
            address = str(int(address) + 1)
    pool_table.append(index)
    return output, address

def pass_1(assembly_code):
    global address
    output, statements = [], assembly_code.strip().split('\n')
    if 'START' in statements[0]:
        _, address = statements.pop(0).split()
        output.append([f"START {address}", f"(AD,({get_code(pot, 'START')})) - (C,({address}))"])
    else: return print('INVALID CODE')

    for statement in statements:
        parts = statement.split()
        if not parts: continue
        if parts[0] == 'END':
            end_value = get_code(pot, 'END')
            lines, address = allocate_literals(end_value, address)
            output.append([statement, '\n'.join(lines) if lines else f"{address} (AD,({end_value})) - _"])
        elif parts[0] in ['READ', 'PRINT']:
            mnemonic, dest = get_code(mot, parts[0]), parts[1]
            symbol_table.setdefault(dest, '')
            output.append([statement, f"{address} (IS,({mnemonic})) - (S,({list(symbol_table).index(dest) + 1}))"])
            address = str(int(address) + 1)
        elif parts[0] in mot:
            mnemonic, reg, dest = get_code(mot, parts[0]), get_code(registers, parts[1]), parts[2]
            symbol_table.setdefault(dest, '')
            output.append([statement, f"{address} (IS,({mnemonic})) ({reg}) (S,({list(symbol_table).index(dest) + 1}))"])
            address = str(int(address) + 1)
        elif parts[1] == 'DS':
            symbol_table[parts[0]] = address
            output.append([statement, f"{address} (DL,({get_code(dl, 'DS')})) - (C,({parts[2]}))"])
            address = str(int(address) + int(parts[2]))
    return output

def pass_2(output_table):
    return [[stmt, ''.join(filter(str.isdigit, instr)) + f" {list(symbol_table.values())[int(instr.split('(S,(')[1].split('))')[0]) - 1]}" if '(S' in instr else ''.join(filter(str.isdigit, instr))] for stmt, instr in output_table]

assembly_code = '''START 501
A DS 1
B DS 1
C DS 1
READ A
READ B
MOVER AREG, A
ADD AREG, B
MOVEM AREG, C
PRINT C
END'''

output_table = pass_1(assembly_code)
pass2_output = pass_2(output_table)

print('\nPass 1:')
print(tabulate(output_table, headers=["Source Code", "Intermediate Code"], tablefmt="grid"))
print('\nSymbol Table:')
print(tabulate([(i+1, sym, addr) for i, (sym, addr) in enumerate(symbol_table.items())], headers=["Index", "Symbol Name", "LC"], tablefmt="grid"))
print('\nPass 2:')
print(tabulate(pass2_output, headers=["Intermediate Code", "Machine Code"], tablefmt="grid"))