import sys
input = sys.stdin.readline

n = int(input())
sell = {}

for _ in range(n):
  title = input()
  if title not in sell:
    sell[title] = 1
  else:
    sell[title] += 1

max_value = max(sell.values())

best = []
for key, value in sell.items():
  if value == max_value:
    best.append(key)

best = sorted(best)
print(best[0])