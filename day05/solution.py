def read_input():
    with open('input') as file:
        return file.read().split('\n\n')

rule_block, page_block = read_input()
rules = {}

def check_page(page, rules):
    is_in_correct_order = True
    page_list = page.split(',')
    for index, num in enumerate(page_list):
        if not num in rules:
            continue
        rule = rules[num]
        for rule_num in rule:
            if not rule_num in page_list:
                continue
            rule_index = page_list.index(rule_num)
            if index > rule_index:
                is_in_correct_order = False
                break
    return is_in_correct_order
for rule in rule_block.split('\n'):
    key, value = rule.split('|')
    if key not in rules:
        rules[key] = []
    rules[key].append(value)

pages = page_block.split('\n')

correct_pages = []
incorrect_pages = []

for page in pages:
    is_in_correct_order = check_page(page, rules)
    if is_in_correct_order:
        correct_pages.append(page)
    else:
        incorrect_pages.append(page)

fixed_pages = []

print(incorrect_pages)

for page in incorrect_pages:
    working_page = page.split(',')
    has_been_fixed = False
    
    while not has_been_fixed:
        has_made_changes = False
        for index, num in enumerate(working_page):
            if not num in rules:
                continue
            rule = rules[num]
            for rule_num in rule:
                if not rule_num in working_page:
                    continue
                rule_index = working_page.index(rule_num)
                if index > rule_index:

                    working_page[index], working_page[rule_index] = working_page[rule_index], working_page[index]
                    has_made_changes = True
                    break
        if not has_made_changes:
            has_been_fixed = True
    
    fixed_pages.append(','.join(working_page))

total_of_correct_middle_page_numbers = 0
for page in correct_pages:
    page_list = page.split(',')
    total_of_correct_middle_page_numbers += int(page_list[len(page_list) // 2])

print('part 1 solution:',total_of_correct_middle_page_numbers)

total_of_fixed_middle_page_numbers = 0
for page in fixed_pages:
    page_list = page.split(',')
    total_of_fixed_middle_page_numbers += int(page_list[len(page_list) // 2])

print('part 2 solution:',total_of_fixed_middle_page_numbers)