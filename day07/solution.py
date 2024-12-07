import itertools
import functools

with open('input', 'r') as file:
    input = file.read().splitlines()

def evaluate(input, operators):
    test_value_sum = 0

    for line in input:
        test_value, numbers = line.split(': ')
        numbers = list(map(int, numbers.split(' ')))
        
        operator_combinations = list(itertools.product(operators, repeat=len(numbers) - 1))
        
        for operator_combo in operator_combinations:
            total = numbers[0]
            valid = True
            
            for i, num in enumerate(numbers[1:]):
                if operator_combo[i] == '+':
                    total += num
                elif operator_combo[i] == '*':
                    total *= num
                elif operator_combo[i] == '||':
                    total = int(str(total) + str(num))
                
                if total > int(test_value):
                    valid = False
                    break
            
            if valid and total == int(test_value):
                test_value_sum += int(test_value)
                break

    return test_value_sum

print('part 1 solution:', evaluate(input, ['+', '*']))
print('part 2 solution:', evaluate(input, ['+', '*', '||']))
        