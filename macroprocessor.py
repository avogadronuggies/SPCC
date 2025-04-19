from tabulate import tabulate
import copy

# Read input and preprocess
with open('source.txt', 'r') as input_file:
    input_lines = [line.split() for line in input_file]

mdt, mnt, ala, macro_names = [], {}, [], []
appends, pass2_mdt = False, []

# PASS 1: Build MDT, MNT, and ALA
for line in input_lines:
    if line[0] == 'MACRO':
        appends = True
        continue
    if appends:
        mdt.append(line)
        if line[0] == 'MEND':
            appends = False

mdt_index = [i for i, line in enumerate(mdt) if line[0] == 'MACRO' or line[0] == 'MEND']
macro_names = [mdt[i][0] for i in mdt_index[:-1]]
mnt = {name: idx + 1 for name, idx in zip(macro_names, mdt_index[:-1])}
ala = [arg.strip(',=') for i in mdt_index[:-1] for arg in mdt[i][1:]]

# Replace args with ALA indices in MDT
for i, line in enumerate(mdt):
    if i not in mdt_index:
        mdt[i] = [f"#{ala.index(arg) + 1}" if arg in ala else arg for arg in line]

# PASS 2: Replace formal args with actual args
mend_location = next(i for i, line in enumerate(input_lines) if 'MEND' in line)
ala = [arg.split('=')[-1] if '=' in arg else arg for line in input_lines[mend_location + 1:] for arg in line[1:] if line[0] in macro_names]
arg_map = {formal: actual for formal, actual in zip(ala, ala)}

pass2_mdt = [
    [arg_map.get(token.strip(','), token) + (',' if token.endswith(',') else '') for token in line]
    for line in mdt if line[0] != 'MACRO'
]

# Display results
print("\nPASS 1:\n")
print("MNT:", tabulate([(i + 1, name, idx) for i, (name, idx) in enumerate(mnt.items())], headers=['Index', 'Macro Name', 'MDT Index'], tablefmt="grid"))
print("\nALA:", tabulate(enumerate(ala, start=1), headers=['Index', 'Arguments'], tablefmt="grid"))
print("\nMDT:", tabulate(enumerate([' '.join(line) for line in mdt], start=1), headers=['Index', 'Macro definition'], tablefmt="grid"))

print("\nPASS 2:\n")
print("ALA:", tabulate(enumerate(ala, start=1), headers=['Index', 'Arguments'], tablefmt="grid"))
print("MDT:", tabulate(enumerate([' '.join(line) for line in pass2_mdt], start=1), headers=['Index', 'Macro definition'], tablefmt="grid"))
