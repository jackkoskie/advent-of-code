with open('input.txt', 'r') as file:
  data = file.read()

# data = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#..."""

lab = [list(i) for i in data.split('\n')]

pos = [0, 0]
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
direction = 0

for i, row in enumerate(lab):
  for j, col in enumerate(row):
    if col == "^":
      pos = [i, j]
      direction = 0
      break
    elif col == ">":
      pos = [i, j]
      direction = 1
      break
    elif col == "v":
      pos = [i, j]
      direction = 2
      break
    elif col == "<":
      pos = [i, j]
      direction = 3
      break

while pos[0] >= 0 and pos[0] < len(lab) and pos[1] >= 0 and pos[1] < len(lab[0]):
  if lab[pos[0]][pos[1]] == "#":
    pos[0] -= directions[direction][0]
    pos[1] -= directions[direction][1]
    direction = (direction + 1) % 4
  else:
    lab[pos[0]][pos[1]] = "X"
  pos[0] += directions[direction][0]
  pos[1] += directions[direction][1]
  if pos[0] < 0 or pos[0] >= len(lab) or pos[1] < 0 or pos[1] >= len(lab[0]):
    break


count = 0
for row in lab:
  for col in row:
    if col == "X":
      count += 1

print(count)