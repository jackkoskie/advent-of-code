import re

with open('input.txt', 'r') as file:
  data = file.read()

# data = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

validStrings = re.findall(r'mul\(\d{1,3},\d{1,3}\)', data)

total = 0

for string in validStrings:
  nums = re.findall(r'\d{1,3}', string)
  total += int(nums[0]) * int(nums[1])

print(total)
