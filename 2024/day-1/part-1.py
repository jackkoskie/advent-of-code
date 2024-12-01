with open('input.txt', 'r') as file:
  data = file.read()

# data = """3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3"""

left = []
right = []
difference = 0

def insertSorted(element: int, sortedList: list[int]):
  if len(sortedList) < 1:
    sortedList.append(element)
    return sortedList

  for i in range(len(sortedList)):
    if element <= sortedList[i]:
      sortedList.insert(i, element)
      return sortedList
  
  sortedList.append(element)
  return sortedList

for line in data.split('\n'):
  cols = line.split('   ')
  insertSorted(int(cols[0]), left)
  insertSorted(int(cols[1]), right)

for row in range(len(left)):
  difference += abs(left[row] - right[row])

print(f"Result: {difference}")
