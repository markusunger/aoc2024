file = open('input')
input = file.read()
file.close()

input = input.split('\n')

first_list = []
second_list = []

for line in input:
    (first, second) = line.split()
    first_list.append(int(first))
    second_list.append(int(second))

first_list.sort()
second_list.sort()

total = 0

for i in range(len(first_list)):
    total += abs(first_list[i] - second_list[i])

print('part 1 solution:', total)

total2 = 0

for i in range(len(first_list)):
    count = second_list.count(first_list[i])
    total2 += count * first_list[i]

print('part 2 solution:', total2)
