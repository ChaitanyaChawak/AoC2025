input = 'inputs/day04.txt'

with open(input, 'r') as file:
  input_lines = [line.strip() for line in file]

def adjacent_rolls(grid):
    # print(grid, end='\n\n')
    rolls = 0
    x = 0
    y = 0
    max_y = len(grid[0])
    max_x = len(grid)
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    to_remove = []
    
    for x in range(max_x):
        for y in range(max_y):
            adj_rolls = 0
            if grid[y][x] != '@':
                continue
            else:
                for dy, dx in directions:
                    ny, nx = y + dy, x + dx
                    try :
                        if ny < 0 or nx < 0 or ny >= max_y or nx >= max_x:
                            continue
                        if grid[ny][nx] == '@':
                            adj_rolls += 1
                    except IndexError:
                        continue
                if adj_rolls < 4 :
                    rolls += 1
                    to_remove += [(y, x)]

    for y, x in to_remove:
        grid[y] = grid[y][:x] + '.' + grid[y][x+1:]

    # print(grid, end='\n\n')
    
    return rolls

def new_total_rolls(grid):
    total = 0
    possible = True
    part1_flag = True
    while possible:
        rolls = adjacent_rolls(grid)
        if rolls == 0:
            possible = False
        total += rolls
        if part1_flag:
            print(f'Part1: {total}')
            part1_flag = False
    
    return total

# print(f'Part1: {adjacent_rolls(input_lines)}')
print(f'Part2: {new_total_rolls(input_lines)}')

