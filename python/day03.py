input = '/home/chai/Documents/AoC2025/inputs/day03.txt'

with open(input, 'r') as file:
  input_lines = [line.strip() for line in file]

total_joltage = 0
total_newjoltage = 0

def joltage(num):
    s = str(num)
    temp = s[:2]
    for i in range(1,len(s)):
        if s[i] > temp[0]:
            if i == len(s)-1: temp = temp[0]+s[i]
            else: temp = s[i:i+2]
        elif s[i] > temp[1] : temp = temp[0]+s[i]

    temp = int(temp)
    return temp

def remove_one(num):
    s = str(num)
    temp = s[:len(s)-1]
    for i in range(len(s)):
        if int(s[:i]+s[i+1:]) > int(temp):
            temp = s[:i]+s[i+1:]
    temp = int(temp)
    return temp

def new_joltage(num):
    s = str(num)
    temp = s[:12]
    while len(str(s))>=12:
        candidate = remove_one(s)
        if len(str(candidate))==12 and int(candidate) > int(temp):
            temp = candidate
            break
        s = candidate

    temp = int(temp)
    return temp

for i in input_lines:
    jolt = joltage(i)
    new_jolt = new_joltage(i)

    total_joltage += jolt
    total_newjoltage += new_jolt

print(f'Part1: {total_joltage}')
print(f'Part2: {total_newjoltage}')