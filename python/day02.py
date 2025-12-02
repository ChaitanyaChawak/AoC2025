input = '/home/chai/Documents/AoC2025/inputs/day02.txt'

with open(input, 'r') as file:
  input_lines = [line.strip() for line in file]

ranges = [line.strip() for line in input_lines[0].split(',') if line.strip()]

def isinvalid(num):
    s = str(num)
    length = len(s)
    if s[:length//2] == s[length//2:]:
        return True
    else: return False

def newisinvalid(num):
    s = str(num)
    length = len(s)
    multplier = length // 2
    for i in range (1, multplier+1):
        if s[:i]*(length//i) == s: return True
    return False

invalid_sum = 0
newinvalid_sum = 0

for i in ranges:
    a, b = i.split('-')
    a = int(a)
    b = int(b)

    for _ in range(a, b + 1):
        if isinvalid(_): invalid_sum += _
        if newisinvalid(_): newinvalid_sum += _
        
print(f'Part1: {invalid_sum}')
print(f'Part2: {newinvalid_sum}')