with open('input', 'r') as file:
    input = file.read().splitlines()

def initialize_grid():
    grid = {}
    grid_dimensions = None
    guard_position = None
    guard_direction = None
    visited = None

    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char == '^':
                guard_position = (x, y)
                guard_direction = 'UP'
            elif char == '>':
                guard_position = (x, y)
                guard_direction = 'RIGHT'
            elif char == 'v':
                guard_position = (x, y)
                guard_direction = 'DOWN'
            elif char == '<':
                guard_position = (x, y)
                guard_direction = 'LEFT'
            grid[(x, y)] = char
    grid_dimensions = (len(input[0]), len(input))

    visited = set()
    visited.add((guard_position, guard_direction))

    return grid, grid_dimensions, guard_position, guard_direction, visited

def get_new_position(position, direction):
    if direction == 'UP':
        return (position[0], position[1] - 1)
    elif direction == 'DOWN':
        return (position[0], position[1] + 1)
    elif direction == 'LEFT':
        return (position[0] - 1, position[1])
    elif direction == 'RIGHT':
        return (position[0] + 1, position[1])

def turn_guard(direction):
    if direction == 'UP':
        return 'RIGHT'
    elif direction == 'RIGHT':
        return 'DOWN'
    elif direction == 'DOWN':
        return 'LEFT'
    elif direction == 'LEFT':
        return 'UP'
    
def walk_grid(grid, grid_dimensions, guard_position, guard_direction, visited, track_path=False):
    path = [] if track_path else None
    while True:
        new_position = get_new_position(guard_position, guard_direction)
        if new_position[0] < 0 or new_position[0] >= grid_dimensions[0] or new_position[1] < 0 or new_position[1] >= grid_dimensions[1]:
            break
        
        if (new_position, guard_direction) in visited:
            return True, path

        if grid[new_position] == '.':
            visited.add((new_position, guard_direction))
            if track_path:
                path.append(new_position)
            grid[guard_position] = '.'
            guard_position = new_position
            
        elif grid[new_position] == '#':
            guard_direction = turn_guard(guard_direction)
            visited.add((guard_position, guard_direction))

    return False, path


grid, grid_dimensions, guard_position, guard_direction, visited = initialize_grid()
has_loop, guard_path = walk_grid(grid, grid_dimensions, guard_position, guard_direction, visited, True)
visited_positions = {pos for pos, dir in visited}

print('part 1 solution:', len(visited_positions))

possible_obstacles = []
tested_positions = set()

for pos in guard_path:
    if pos in tested_positions:
        continue
    tested_positions.add(pos)
    
    grid, grid_dimensions, guard_position, guard_direction, visited = initialize_grid()
    if grid[pos] != '.':
        continue
    grid[pos] = '#'
    has_loop, _ = walk_grid(grid, grid_dimensions, guard_position, guard_direction, visited)
    if has_loop:
        possible_obstacles.append(pos)

print('part 2 solution:', len(possible_obstacles))