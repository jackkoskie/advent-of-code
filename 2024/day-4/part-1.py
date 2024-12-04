with open('input.txt', 'r') as file:
  data = file.read()

# data = '''MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX'''

data = data.split('\n')
data = [list(i) for i in data]

count = 0

for i, row in enumerate(data):
  for j, col in enumerate(row):
    if col == 'X':
      # up
      if i >= 3 and data[i-1][j] == 'M' and data[i-2][j] == 'A' and data[i-3][j] == 'S':
        count += 1
      # down
      if i < len(data) - 3 and data[i+1][j] == 'M' and data[i+2][j] == 'A' and data[i+3][j] == 'S':
        count += 1
      # left
      if j >= 3 and data[i][j-1] == 'M' and data[i][j-2] == 'A' and data[i][j-3] == 'S':
        count += 1
      # right
      if j < len(row) - 3 and data[i][j+1] == 'M' and data[i][j+2] == 'A' and data[i][j+3] == 'S':
        count += 1
      # up-left
      if i >= 3 and j >= 3 and data[i-1][j-1] == 'M' and data[i-2][j-2] == 'A' and data[i-3][j-3] == 'S':
        count += 1
      # down-right
      if i < len(data) - 3 and j < len(row) - 3 and data[i+1][j+1] == 'M' and data[i+2][j+2] == 'A' and data[i+3][j+3] == 'S':
        count += 1
      # up-right
      if i >= 3 and j < len(row) - 3 and data[i-1][j+1] == 'M' and data[i-2][j+2] == 'A' and data[i-3][j+3] == 'S':
        count += 1
      # down-left
      if i < len(data) - 3 and j >= 3 and data[i+1][j-1] == 'M' and data[i+2][j-2] == 'A' and data[i+3][j-3] == 'S':
        count += 1

print(count)