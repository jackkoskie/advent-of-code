import re

with open('input.txt', 'r') as file:
  data = file.read()

# data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

validStrings = re.findall(r'mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\)', data)

total = 0
enabled = True

for string in validStrings:
  if string == "don't()":
    enabled = False
  elif string == "do()":
    enabled = True
  elif enabled:
    nums = re.findall(r'\d{1,3}', string)
    total += int(nums[0]) * int(nums[1])

print(total)
