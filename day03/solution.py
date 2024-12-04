import re

def read_input():
    with open('input') as file:
        return file.read()

input = read_input()

tuples = re.findall(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', input)
total = 0
for a, b in tuples:
    total += int(a) * int(b)

print('part 1 solution:', total)

enablers = [(m.group(), m.start()) for m in re.finditer(r'(?:do|don\'t)\(\)', input)]
tuples = [(m.groups(), m.start()) for m in re.finditer(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', input)]

mul_enabled = True
last_control_pos = -1
total = 0

for (a, b), mul_pos in tuples:
    while enablers and enablers[0][1] < mul_pos:
        ctrl_statement, ctrl_pos = enablers.pop(0)
        mul_enabled = (ctrl_statement == 'do()')
        last_control_pos = ctrl_pos

    if mul_enabled:
        total += int(a) * int(b)

print('part 2 solution:', total)



