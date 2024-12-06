with open('input.txt', 'r') as file:
  data = file.read()

# data = """47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47"""

data = data.split("\n\n")

rules = [i.split('|') for i in data[0].split("\n")]
updates = [i.split(',') for i in data[1].split("\n")]

def checkUpdate(update):
  changed = False
  fixed = update.copy()
  for i, page in enumerate(update):
      if page in [j[1] for j in rules]:
        rule = [k for k in rules if k[1] == page]
        for r in rule:
          if r[0] in update and r[0] not in update[:i]:
            if not changed:
              changed = True
            fixed[update.index(page)], fixed[update.index(r[0])] = fixed[update.index(r[0])], fixed[update.index(page)]

  return changed, fixed

count = 0

for update in updates:
  changed, fixed = checkUpdate(update)
  if changed:
    count += int(update[len(update) // 2])
print(count)
  
      
    