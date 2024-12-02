with open('input.txt', 'r') as file:
  data = file.read()

# data = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9"""

reports = [i.split(' ') for i in data.split('\n')]

safeCount = 0

for report in reports:
  last = None
  up = None
  safe = True
  for i, level in enumerate(report):
    level = int(level)
    if last == None:
      last = level
      continue
    elif up == None:
      up = True if level > last else False
      if up and 1 <= level - last <= 3:
        last = level
        continue
      elif not up and 1 <= last - level <= 3:
        last = level
        continue
      else:
        safe = False
        break
    elif up:
      if level < last or not (1 <= level - last <= 3):
        safe = False
        break
      else:
        last = level
    elif not up:
      if level > last or not (1 <= last - level <= 3):
        safe = False
        break
      else:
        last = level
  
  if safe:
    safeCount += 1

print(safeCount)