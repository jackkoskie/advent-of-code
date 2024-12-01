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

def getCount(element: int, sortedList: list[int]):
  if not element in sortedList:
    return 0
  else:
    index = sortedList.index(element)
    e = element
    i = 0
    while e == element:
      i+=1
      e = sortedList[index+i]
    return i

for line in data.split('\n'):
  cols = line.split('   ')
  left.append(int(cols[0]))
  insertSorted(int(cols[1]), right)

similarity = 0

for row in range(len(left)):
  similarity += left[row] * getCount(left[row], right)

print(similarity)



