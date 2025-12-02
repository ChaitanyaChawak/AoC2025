input = '/home/chai/Documents/AoC2025/inputs/day01.txt'

with open(input, 'r') as file:
  input_lines = [line.strip() for line in file]

current = 50
zerocounter = 0
zeropass = 0

for i in input_lines:
  if i[0] == 'L':
    
    if int(i[1:]) >= current and current > 0:
      zeropass += 1 + (int(i[1:]) - current) // 100
    elif current == 0 and int(i[1:]) > 0:
      zeropass += int(i[1:]) // 100

    current -= int(i[1:])
    current = current % 100

    if current == 0:
      zerocounter += 1

  elif i[0] == 'R':
    
    steps_to_first_zero = (100 - current) % 100
    if steps_to_first_zero == 0:
      steps_to_first_zero = 100

    if int(i[1:]) >= steps_to_first_zero:
      zeropass += 1 + (int(i[1:]) - steps_to_first_zero) // 100

    current += int(i[1:])
    current = current % 100

    if current == 0:
      zerocounter += 1

print(f'Part1: {zerocounter}')
print(f'Part2: {zeropass}')