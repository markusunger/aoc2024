from itertools import pairwise

file = open('input')
input = file.read().split('\n')
file.close()

def is_safe(levels, problem_dampener=False):
    numbers = [int(x) for x in levels]
    
    if not problem_dampener:
        # part 1 logic
        for a, b in pairwise(numbers):
            if not (1 <= abs(b - a) <= 3):
                return False
        
        is_ascending = None
        for a, b in pairwise(numbers):
            if is_ascending is None:
                is_ascending = b > a
                continue
            if (is_ascending and b < a) or (not is_ascending and b > a):
                return False

        return True
    
    # part 2 logic
    for i in range(len(numbers)):
        test_sequence = numbers[:i] + numbers[i+1:]
        
        is_ascending = None
        valid = True
        
        for a, b in pairwise(test_sequence):
            if not (1 <= abs(b - a) <= 3):
                valid = False
                break
        
        if not valid:
            continue
            
        for a, b in pairwise(test_sequence):
            if is_ascending is None:
                is_ascending = b > a
                continue
            if (is_ascending and b < a) or (not is_ascending and b > a):
                valid = False
                break
        
        if valid:
            return True
    
    return False


safe_report_count_part1 = 0
safe_report_count_part2 = 0

for line in input:
    if is_safe(line.split()):
        safe_report_count_part1 += 1
    if is_safe(line.split(), True):
        safe_report_count_part2 += 1

print('part 1 solution:',safe_report_count_part1)
print('part 2 solution:',safe_report_count_part2)