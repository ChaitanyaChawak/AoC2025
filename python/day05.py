input = 'inputs/day05.txt'

with open(input, 'r') as file:
  input_lines = [line.strip() for line in file]

input_lines = '''
3-5
10-14
16-20
12-18

1
5
8
11
17
32
'''.strip().split('\n')

fresh = set()
map_dict = {}
starts = set()
items = []
for line in input_lines:
    if '-' in line:
        start, end = map(int, line.split('-'))
        starts.add(start)
        if start in map_dict:
            if end > map_dict[start]:
                map_dict[start] = end
        else:
            map_dict[start] = end
    elif len(line) > 0: items.append(int(line))

for i in items:
    for line in starts:
        if i >= line and i <= map_dict[line]:
            fresh.add(i)
            # print(f'Adding {i} to fresh set')
            break
try:
    for i in starts:
        for j in starts:
            if (i > j) and (map_dict[i] > map_dict[j]):
                map_dict[j] = map_dict[i]
                del map_dict[i]
                continue
except KeyError:
    pass
            
total_fresh = 0
for i in map_dict:
    total_fresh = map_dict[i] - i + 1


print(f'Part1: {len(fresh)}')
print(f'Part2: {total_fresh}')
