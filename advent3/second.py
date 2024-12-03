import re

with open('input.txt', 'r') as file:
    content = file.read()


pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
instructions = re.findall(pattern, "".join(content))

enabled = True
result = 0

for inst in instructions:
    match inst[0]:
        case "do()":
            enabled = True
        case "don't()":
            enabled = False
        case _ if enabled:
            result += int(inst[1]) * int(inst[2])

print(result)