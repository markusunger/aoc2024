file = open('input')
input = file.read()
file.close()

input = input.split('\n')

first_list = []
second_list = []

for line in input:
    pair = line.split()
    first = int(pair[0])
    second = int(pair[1])
    first_list.append(first)
    second_list.append(second)

first_list.sort()
second_list.sort()

total = 0

for i in range(len(first_list)):
    abs_diff = abs(first_list[i] - second_list[i])
    total += abs_diff

print('part 1 solution:', total)

total2 = 0

for i in range(len(first_list)):
    count = second_list.count(first_list[i])
    total2 += count * first_list[i]

print('part 2 solution:', total2)
