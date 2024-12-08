import itertools

with open('input', 'r') as file:
    input = file.read().splitlines()

def parse_input(input):
    antennas = {}
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char != '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))
    return antennas

def find_antinodes(antenna1, antenna2):
    dx = antenna2[0] - antenna1[0]
    dy = antenna2[1] - antenna1[1]

    node1 = (antenna1[0] - dx, antenna1[1] - dy)
    node2 = (antenna2[0] + dx, antenna2[1] + dy)

    return node1, node2


dimensions = (len(input[0]), len(input))
antennas = parse_input(input)

part1_antinodes = []

for antenna in antennas:
    pairs = list(itertools.combinations(antennas[antenna], 2))
    
    for (x1, y1), (x2, y2) in pairs:
        node1, node2 = find_antinodes((x1, y1), (x2, y2))
        if node1[0] >= 0 and node1[0] < dimensions[0] and node1[1] >= 0 and node1[1] < dimensions[1]:
            part1_antinodes.append(node1)
        if node2[0] >= 0 and node2[0] < dimensions[0] and node2[1] >= 0 and node2[1] < dimensions[1]:
            part1_antinodes.append(node2)

      

print('part 1 solution:', len(set(part1_antinodes)))