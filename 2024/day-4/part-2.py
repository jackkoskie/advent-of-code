with open('input.txt', 'r') as file:
  data = file.read()

# data = '''.M.S......
# ..A..MSMS.
# .M.S.MAA..
# ..A.ASMSM.
# .M.S.M....
# ..........
# S.S.S.S.S.
# .A.A.A.A..
# M.M.M.M.M.
# ..........'''

data = data.split('\n')
data = [list(i) for i in data]

count = 0

for i, row in enumerate(data):
  for j, col in enumerate(row):
    if ((col == 'M' and i >= 2 and j < len(row) - 2 and data[i-1][j+1] == "A" and data[i-2][j+2] == "S") or (col == 'S' and i >= 2 and j < len(row) - 2 and data[i-1][j+1] == "A" and data[i-2][j+2] == "M")) and ((data[i][j+2] == "S" and data[i-2][j] == "M") or (data[i][j+2] == "M" and data[i-2][j] == "S")):
      count += 1


print(count)