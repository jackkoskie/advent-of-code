from datetime import datetime as date

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

masterLab = [list(i) for i in data.split('\n')]

startingPos = [0, 0]
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
startingDirection = 0
count = 0

for i, row in enumerate(masterLab):
  for j, col in enumerate(row):
    if col == "^":
      startingPos = [i, j]
      startingDirection = 0
      break
    elif col == ">":
      startingPos = [i, j]
      startingDirection = 1
      break
    elif col == "v":
      startingPos = [i, j]
      startingDirection = 2
      break
    elif col == "<":
      startingPos = [i, j]
      startingDirection = 3
      break

def checkPos(obs):
  pos = startingPos.copy()
  direction = startingDirection
  path = []

  lab = [row.copy() for row in masterLab]
  lab[obs[0]][obs[1]] = "O"

  if lab[obs[0]][obs[0]] == "#" or lab[obs[0]][obs[0]] == "^":
    return False

  while pos[0] >= 0 and pos[0] < len(lab) and pos[1] >= 0 and pos[1] < len(lab[0]):
    if lab[pos[0]][pos[1]] == "#" or lab[pos[0]][pos[1]] == "O":
      pos[0] -= directions[direction][0]
      pos[1] -= directions[direction][1]
      direction = (direction + 1) % 4
    pos[0] += directions[direction][0]
    pos[1] += directions[direction][1]
    if pos[0] < 0 or pos[0] >= len(lab) or pos[1] < 0 or pos[1] >= len(lab[0]):
      return False
    if [pos[0], pos[1], direction] in path:
      return True
    else:
      path.append([pos[0], pos[1], direction])
    
    # displayLab = [row.copy() for row in lab]
    # displayLab[pos[0]][pos[1]] = "X"
    
    # print('\n'.join([''.join(i) for i in displayLab]))
    # print(pos, direction)
    # print(path)
    # print()

startTime = date.now()
rowTimes = []

for i in range(len(masterLab)):
  rowStart = date.now()
  for j in range(len(masterLab[0])):
    if checkPos([i, j]):
      count += 1
  rowTime = (date.now() - rowStart).total_seconds()
  rowTimes.append(rowTime)
  print(f"Row {i + 1}/{len(masterLab)}, Row Time: {round(rowTime, 2)}s, Total Time: {round((date.now() - startTime).total_seconds(), 2)}s, Average Row Time: {round(sum(rowTimes) / len(rowTimes), 2)}s, Estimated Time Remaining: {round(sum(rowTimes) / len(rowTimes) * (len(masterLab) - i - 1), 2)}s, Count: {count}")

print(count)