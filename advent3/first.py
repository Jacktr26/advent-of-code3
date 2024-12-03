import re

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"


with open('input.txt', 'r') as file:
    content = file.read()

matches = re.findall(pattern, content)

total_sum = 0
for match in matches:
    x, y = map(int, match)  # Convert captured groups to integers
    result = x * y
    total_sum += result
    print(f"Valid instruction: mul({x},{y}), Result: {result}")

print(f"Total sum of all valid instructions: {total_sum}")
