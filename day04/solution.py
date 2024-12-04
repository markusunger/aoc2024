import re

def read_input():
    with open('input') as file:
        return file.read().splitlines()

input = read_input()

xmas_count = 0
x_mas_count = 0

# BEWARE: this is horrible code, I'm sorry

for i in range(len(input)):
    for j in range(len(input[0])):
        if input[i][j] == 'X':
            # check row
            if j + 3 < len(input[0]) and input[i][j+1] == 'M' and input[i][j+2] == 'A' and input[i][j+3] == 'S':
                xmas_count += 1
            # check reverse row
            if j - 3 >= 0 and input[i][j-1] == 'M' and input[i][j-2] == 'A' and input[i][j-3] == 'S':
                xmas_count += 1
            # check column
            if i + 3 < len(input) and input[i+1][j] == 'M' and input[i+2][j] == 'A' and input[i+3][j] == 'S':
                xmas_count += 1
            # check reverse column
            if i - 3 >= 0 and input[i-1][j] == 'M' and input[i-2][j] == 'A' and input[i-3][j] == 'S':
                xmas_count += 1
            # check all four diagonals
            if i + 3 < len(input) and j + 3 < len(input[0]) and input[i+1][j+1] == 'M' and input[i+2][j+2] == 'A' and input[i+3][j+3] == 'S':
                xmas_count += 1
            if i - 3 >= 0 and j - 3 >= 0 and input[i-1][j-1] == 'M' and input[i-2][j-2] == 'A' and input[i-3][j-3] == 'S':
                xmas_count += 1
            if i + 3 < len(input) and j - 3 >= 0 and input[i+1][j-1] == 'M' and input[i+2][j-2] == 'A' and input[i+3][j-3] == 'S':
                xmas_count += 1
            if i - 3 >= 0 and j + 3 < len(input[0]) and input[i-1][j+1] == 'M' and input[i-2][j+2] == 'A' and input[i-3][j+3] == 'S':
                xmas_count += 1
        if input[i][j] == 'A' and i - 1 >= 0 and j + 1 < len(input[0]) and i + 1 < len(input) and j - 1 >= 0:
            # is MAS in top-left to bottom-right diagonal in either direction?
            if ((input[i-1][j-1] == 'M' and input[i+1][j+1] == 'S') or (input[i-1][j-1] == 'S' and input[i+1][j+1] == 'M')):
                # is it also in top-right to bottom-left diagonal in either direction?
                if (input[i-1][j+1] == 'M' and input[i+1][j-1] == 'S') or (input[i-1][j+1] == 'S' and input[i+1][j-1] == 'M'):
                    x_mas_count += 1

   
print('part 1 solution:', xmas_count)
print('part 2 solution:', x_mas_count)

